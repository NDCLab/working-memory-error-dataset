import os
import shutil
import cv2
import dlib
import imageio
import numpy as np
from glob import glob
from tqdm import tqdm
from imutils import face_utils

# Make sure alignfaces is installed:
# pip install "alignfaces @ git+https://git@github.com/SourCherries/auto-face-align.git"
import alignfaces as af

'''
The morphing algorithm is taken from https://github.com/2773kartik/Face_Morphing/tree/main
- Face Morphing program that takes two images as input and generates n frames (specified by user) to perform face morphing 
Using delaunay triangulation. Please ensure that the dimensions of both images in input are same.
"shape_predictor_68_face_landmarks.dat" used to detect 68 landmark points on face
'''

# --- Global Configurations ---
path = "neutralC/"
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

# --- Functions ---
def find_i(point, tr):
    """Return indices of triangles in image"""
    cnt = 0
    for index in tr:
        if point == index:
            return cnt
        cnt += 1

def triangulate(img, point):
    """Delaunay triangulations"""
    subs = cv2.Subdiv2D((0, 0, img.shape[1], img.shape[0]))
    for p_val in point:
        subs.insert(p_val)
    return subs.getTriangleList()

def combineResult(img1, img2, img, t1, t2, t, alpha):
    """Combine input and output via affine transform"""
    rect1 = cv2.boundingRect(np.float32([t1]))
    rect2 = cv2.boundingRect(np.float32([t2]))
    rect = cv2.boundingRect(np.float32([t]))
    
    t1_cropped, t2_cropped, t_cropped = [], [], []

    for i in range(3):
        t1_cropped.append(((t1[i][0] - rect1[0]), (t1[i][1] - rect1[1])))
        t2_cropped.append(((t2[i][0] - rect2[0]), (t2[i][1] - rect2[1])))
        t_cropped.append(((t[i][0] - rect[0]), (t[i][1] - rect[1])))

    mask = np.zeros((rect[3], rect[2], 3), dtype=np.float32)
    cv2.fillPoly(mask, [np.int32(t_cropped)], (1.0, 1.0, 1.0), 16)

    img1_roi = img1[rect1[1]:rect1[1] + rect1[3], rect1[0]:rect1[0] + rect1[2]]
    img2_roi = img2[rect2[1]:rect2[1] + rect2[3], rect2[0]:rect2[0] + rect2[2]]

    size = (rect[2], rect[3])
    warp1 = cv2.getAffineTransform(np.float32(t1_cropped), np.float32(t_cropped))
    warp_img1 = cv2.warpAffine(img1_roi, warp1, size)
    
    warp2 = cv2.getAffineTransform(np.float32(t2_cropped), np.float32(t_cropped))
    warp_img2 = cv2.warpAffine(img2_roi, warp2, size)

    result_roi = (1. - alpha) * warp_img1 + alpha * warp_img2

    img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]] = \
        img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]] * (1 - mask) + result_roi * mask

def get_points(img):
    """Mark the landmarks and return coordinates"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    
    shaped = None
    for (i, rect) in enumerate(rects):
        shaped = predictor(gray, rect)
        shaped = face_utils.shape_to_np(shaped)
        
    h, w, c = img.shape
    triangle = []
    
    if shaped is not None:
        for coord in shaped:
            triangle.append((int(coord[0]), int(coord[1])))
            
    triangle.extend([(0, 0), (0, h-1), (w-1, h-1), (w-1, 0)])
    return triangle

def morph_faces(image_1, morph_list, frames=25):
    """Batch face morphing function"""
    fps = frames / 2
    image = cv2.imread(image_1)
    
    for image_2 in morph_list:
        image1 = cv2.imread(image_2)
    
        triangle1 = get_points(image)
        triangle2 = get_points(image1)
    
        dlny1 = triangulate(image, triangle1)
    
        triangle_index = []
        for t in dlny1:
            pt1, pt2, pt3 = (t[0], t[1]), (t[2], t[3]), (t[4], t[5])
            add = [(find_i(pt1, triangle1), find_i(pt2, triangle1), find_i(pt3, triangle1))]
            triangle_index.extend(add)
    
        output_name = image_1.split("/")[-1][:-4] + "_" + image_2.split("/")[-1][:-4]
        output_dir = f'./morphed/{output_name}'
        
        if os.path.exists(output_dir):
            print(f"Directory '{output_dir}' already exists. Skipping iteration.")
        else:
            os.mkdir(output_dir)
            gif_path = './morphed/morph.gif'
            
            with imageio.get_writer(gif_path, mode='I', duration=0.05) as writer:
                for frame in range(frames):
                    alpha_factor = (frame + 1) / frames
                    triangle_middle = []
                    
                    for i in range(len(triangle1)):
                        x = int(((1 - alpha_factor) * triangle1[i][0]) + (alpha_factor * triangle2[i][0]))
                        y = int(((1 - alpha_factor) * triangle1[i][1]) + (alpha_factor * triangle2[i][1]))
                        triangle_middle.append((x, y))
                    
                    morphed_image = np.zeros(image.shape, dtype=image.dtype)
                    
                    for j in range(len(triangle_index)):
                        x, y, z = triangle_index[j][0], triangle_index[j][1], triangle_index[j][2]
                        t1 = [triangle1[x], triangle1[y], triangle1[z]]
                        t2 = [triangle2[x], triangle2[y], triangle2[z]]
                        t_mid = [triangle_middle[x], triangle_middle[y], triangle_middle[z]]
                        combineResult(image, image1, morphed_image, t1, t2, t_mid, alpha_factor)
                    
                    cv2.imwrite(f'{output_dir}/{frame}.jpg', morphed_image)
                    
                    # gif_image = cv2.cvtColor(morphed_image, cv2.COLOR_BGR2RGB)
                    # writer.append_data(gif_image)
                    
            cv2.destroyAllWindows()


# --- Main Execution Scripts ---
if __name__ == '__main__':
    
    # ---------------------------------------------------------
    # PART 1: Single interactive face morph
    # ---------------------------------------------------------
    frames = int(input("How many frames to generate? ")) # 20 recommended (optimal)
    fps = frames / 2
    
    # example morph
    image = cv2.imread('/Users/fzaki001/Downloads/neutral_clean/CFD-MF-305-014-N.jpg')
    image1 = cv2.imread('/Users/fzaki001/Downloads/neutral_clean/CFD-MF-321-003-N.jpg')

    triangle1 = []
    triangle2 = []
    
    n = int(input("Get tiepoint manually (press 1) or automatically (press 2): "))
    if n == 1:
        with open("file1.txt", "r") as f:
            for i in f:
                a, b, c, d = map(int, i.split())
                triangle1.append((a, b))
                triangle2.append((c, d))
    elif n == 2:
        triangle1 = get_points(image)
        triangle2 = get_points(image1)

    dlny1 = triangulate(image, triangle1)

    triangle_index = []
    for t in dlny1:
        pt1, pt2, pt3 = (t[0], t[1]), (t[2], t[3]), (t[4], t[5])
        add = [(find_i(pt1, triangle1), find_i(pt2, triangle1), find_i(pt3, triangle1))]
        triangle_index.extend(add)

    # Output directory setup
    parent_dir = './'
    v_dir = 'output_gif'
    img_dir = 'output_images'
    
    # os.mkdir(os.path.join(parent_dir, v_dir))
    # os.mkdir(os.path.join(parent_dir, img_dir))

    output_path = './output_images'
    gif_path = './output_gif/morph.gif'

    with imageio.get_writer(gif_path, mode='I', duration=0.05) as writer:
        for frame in range(frames):
            alpha_factor = (frame + 1) / frames
            triangle_middle = []
            
            for i in range(len(triangle1)):
                x = int(((1 - alpha_factor) * triangle1[i][0]) + (alpha_factor * triangle2[i][0]))
                y = int(((1 - alpha_factor) * triangle1[i][1]) + (alpha_factor * triangle2[i][1]))
                triangle_middle.append((x, y))
            
            morphed_image = np.zeros(image.shape, dtype=image.dtype)
            
            for j in range(len(triangle_index)):
                x, y, z = triangle_index[j][0], triangle_index[j][1], triangle_index[j][2]
                t1 = [triangle1[x], triangle1[y], triangle1[z]]
                t2 = [triangle2[x], triangle2[y], triangle2[z]]
                t_mid = [triangle_middle[x], triangle_middle[y], triangle_middle[z]]
                combineResult(image, image1, morphed_image, t1, t2, t_mid, alpha_factor)
            
            cv2.imwrite(f'{output_path}/{frame}.jpg', morphed_image)
            gif_image = cv2.cvtColor(morphed_image, cv2.COLOR_BGR2RGB)
            writer.append_data(gif_image)

    cv2.destroyAllWindows()

    # ---------------------------------------------------------
    # PART 2: Batch processing variables setup (Not actively called)
    # ---------------------------------------------------------
    try:
        img_list = [i for i in os.listdir("neutral_clean/") if i.endswith(".jpg")]
        # example image to make a batch
        image_1_batch = "neutral_clean/CFD-LM-243-075-N.jpg"
        morph_list_batch = ["neutral_clean/" + i for i in img_list]
        
        # Example call: morph_faces(image_1=image_1_batch, morph_list=morph_list_batch, frames=25)
    except FileNotFoundError:
        pass


    # ---------------------------------------------------------
    # PART 3: Auto-Face-Align Processing
    # ---------------------------------------------------------
    paths = ['/Users/fzaki001/Downloads/neutralC/subset/']
    file_prefix = ""
    file_postfix = "jpg"

    for my_faces_path in tqdm(paths):
        # Estimate landmarks.
        af.get_landmarks(my_faces_path, file_prefix, file_postfix, start_fresh=True)
        landmark_features, files = af.get_landmark_features(my_faces_path)
        aligned_path = af.align_procrustes(
            my_faces_path, 
            file_prefix='',  
            file_postfix='jpg',
            exclude_features=['jawline', 'left_iris', 'right_iris', 'mouth_inner'],
            include_features=None,
            adjust_size='default',
            size_value=None,
            color_of_result='grayscale'
        )
        
        af.get_landmarks(aligned_path, file_prefix, file_postfix)
        the_aperture, aperture_path = af.place_aperture(
            aligned_path, 
            file_prefix,
            file_postfix,
            aperture_type="MossEgg",
            contrast_norm="max",
            color_of_result="rgb"
        )

    # Remove initial folders with morphs (keep only aligned and cropped)
    try:
        for folder in [i for i in os.listdir("morphed_matched/") if i.endswith("N")]:
            shutil.rmtree("morphed_matched/" + folder)
    except FileNotFoundError:
        pass