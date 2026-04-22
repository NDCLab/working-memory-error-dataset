# Load libraries
library(afex)
library(emmeans)
library(reshape2)
library(rstatix)
library(ordinal)
library(ggplot2)
library(ggeffects)
library(interactions)
library(dplyr)
library(tibble)
library(rempsyc)

# ==============================================================================
# Analyses for the paper
# Experiment 1
# ==============================================================================

# ------------------------------------------------------------------------------
# [Preliminary] WM response type
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)
analysis_name <- "prelim_wm_resp"
csv_path <- sprintf("%swme-face-new/prelim_wm_resp.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$resp_type <- as.factor(df$resp_type)
df$resp_type <- relevel(df$resp_type, ref = 2)
df$proportion <- scale(df$proportion)

model <- lmer(proportion ~ resp_type + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

emm <- emmeans(model, ~ resp_type)
posthoc_results <- pairs(emm, adjust = "fdr")
print(posthoc_results)
confint(posthoc_results)

# ------------------------------------------------------------------------------
# [Preliminary] Flanker accuracy
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)
analysis_name <- "prelim_fl_acc"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-new/prelim_fl_acc.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$proportion <- scale(df$proportion)
df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- contr.sum(2)

model <- lmer(proportion ~ congruent + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))


# ------------------------------------------------------------------------------
# [Preliminary] Flanker RT; effect of congruency only
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)
analysis_name <- "prelim_fl_rt_congruency"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-new/prelim_fl_rt.csv", home_dir)

df <- read.csv(csv_path)
df <- subset(df, df$acc == "correct")
df$sub <- as.factor(df$sub)
df$rt <- scale(df$rt)

df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- -rev(contr.sum(2))

model <- lmer(rt ~ congruent + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ------------------------------------------------------------------------------
# [Preliminary] Flanker RT; effect of accuracy only
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)
analysis_name <- "prelim_fl_rt_accuracy"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-new/prelim_fl_rt.csv", home_dir)

df <- read.csv(csv_path)
df <- subset(df, df$congruent == "incongruent")
df$sub <- as.factor(df$sub)
df$rt <- scale(df$rt)

df$acc <- as.factor(df$acc)
contrasts(df$acc) <- -rev(contr.sum(2))

model <- lmer(rt ~ acc + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ------------------------------------------------------------------------------
# [Preliminary] Flanker RT; effect of accuracy AND congruency
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)
analysis_name <- "prelim_fl_rt"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-new/prelim_fl_rt.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$rt <- scale(df$rt)

df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- -rev(contr.sum(2))

df$acc <- as.factor(df$acc)
contrasts(df$acc) <- -rev(contr.sum(2))

model <- lmer(rt ~ congruent * acc + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

library(ggplot2)
interaction_plot <- ggplot(df, aes(x = congruent, y = rt, color = acc, group = acc)) +
  stat_summary(fun = mean, geom = "line", linewidth = 1) +
  stat_summary(fun.data = mean_se, geom = "errorbar", width = 0.1) +
  stat_summary(fun = mean, geom = "point", size = 3) +
  labs(
    title = "Interaction of Congruency and Accuracy on Reaction Time",
    x     = "Congruency",
    y     = "Reaction Time (ms)",
    color = "Accuracy"
  ) +
  theme_bw()

print(interaction_plot)

# ------------------------------------------------------------------------------
# [Main] Average recognition and 2s
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-new/main_wm_con.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- rev(contr.sum(2))
df$similarity <- scale(df$similarity)
df$prop_correct <- scale(df$prop_correct)

analysis_name <- "main_wm_con"
model <- lmer(similarity ~ congruent + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))
# round(confint(model), 2)

analysis_name <- "main_wm_con_2"
model <- lmer(prop_correct ~ congruent + (1 | sub), data = df)
summary(model)
# round(confint(model), 2)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-new/apa_tables/", home_dir)

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-new/main_wm_acc.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$acc <- as.factor(df$acc)
contrasts(df$acc) <- rev(contr.sum(2))
df$similarity <- scale(df$similarity)
df$prop_correct <- scale(df$prop_correct)

analysis_name <- "main_wm_acc"
model <- lmer(similarity ~ acc + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))
# round(confint(model), 2)

analysis_name <- "main_wm_acc_2"
model <- lmer(prop_correct ~ acc + (1 | sub), data = df)
summary(model)
# round(confint(model), 2)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ==============================================================================
# Experiment 2
# ==============================================================================

# ------------------------------------------------------------------------------
# [Preliminary] WM response type
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
analysis_name <- "prelim_wm_resp"
csv_path <- sprintf("%swme-face-jitter-l/prelim_wm_resp.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$resp_type <- as.factor(df$resp_type)
df$resp_type <- relevel(df$resp_type, ref = 2)
df$proportion <- scale(df$proportion)

model <- lmer(proportion ~ resp_type + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

emm <- emmeans(model, ~ resp_type)
posthoc_results <- pairs(emm, adjust = "fdr")
print(posthoc_results)
confint(posthoc_results)

# ------------------------------------------------------------------------------
# [Preliminary] Flanker accuracy
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
analysis_name <- "prelim_fl_acc"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/prelim_fl_acc.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$proportion <- scale(df$proportion)
df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- contr.sum(2)

model <- lmer(proportion ~ congruent + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ------------------------------------------------------------------------------
# [Preliminary] Flanker RT; effect of congruency only
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
analysis_name <- "prelim_fl_rt_congruency"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/prelim_fl_rt.csv", home_dir)

df <- read.csv(csv_path)
df <- subset(df, df$acc == "correct")
df$sub <- as.factor(df$sub)
df$rt <- scale(df$rt)

df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- -rev(contr.sum(2))

model <- lmer(rt ~ congruent + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ------------------------------------------------------------------------------
# [Preliminary] Flanker RT; effect of accuracy only
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
analysis_name <- "prelim_fl_rt_accuracy"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/prelim_fl_rt.csv", home_dir)

df <- read.csv(csv_path)
df <- subset(df, df$congruent == "incongruent")
df$sub <- as.factor(df$sub)
df$rt <- scale(df$rt)

df$acc <- as.factor(df$acc)
contrasts(df$acc) <- -rev(contr.sum(2))

model <- lmer(rt ~ acc + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ------------------------------------------------------------------------------
# [Preliminary] Flanker RT; effect of accuracy AND congruency
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
analysis_name <- "prelim_fl_rt"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/prelim_fl_rt.csv", home_dir)

df <- read.csv(csv_path)
df$sub <- as.factor(df$sub)
df$rt <- scale(df$rt)

df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- -rev(contr.sum(2))

df$acc <- as.factor(df$acc)
contrasts(df$acc) <- -rev(contr.sum(2))

model <- lmer(rt ~ congruent * acc + (1 | sub), data = df)
summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s.docx", table_output_path, analysis_name))

# ------------------------------------------------------------------------------
# [Main] Trial-level models (Congruency effects)
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)

sample <- "hr"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/long_data_full.csv", home_dir)

df <- read.csv(csv_path)
df <- subset(df, df$acc == 1) # take only correct trials for incon vs con analysis
df$sub <- as.factor(df$sub)

df$congruent <- as.factor(df$congruent)
contrasts(df$congruent) <- rev(contr.sum(2))

if (sample == "similarity") {
  df$similarity <- ordered(df$similarity)
  model <- clmm(similarity ~ congruent * poly(jitter, 2) + (1 | sub), data = df)
} else if (sample == "hr") {
  df$similarity <- ifelse(df$similarity == 2, 1, 0)
  df$similarity <- as.factor(df$similarity)
  model <- glmer(similarity ~ congruent * poly(jitter, 2) + (1 | sub), data = df, family = binomial)
}

summary(model)
confint(model)

# ------------------------------------------------------------------------------
# JN plot
# ------------------------------------------------------------------------------
plot_name <- "JN_2s"
y_label_name <- "Incongruent - Congruent Effect of RSI (Log-Odds)"
title <- "Effect of RSI on WM Recognition Performance"  
font <- "Arial"

jitter_range <- seq(min(df$jitter), max(df$jitter), length.out = 750)

emm_contrast <- emmeans(model, 
                        specs = pairwise ~ congruent | jitter,
                        at = list(jitter = jitter_range))

contrast_summary <- summary(emm_contrast$contrasts, infer = c(TRUE, TRUE))
contrast_df <- as.data.frame(contrast_summary)

contrast_df <- contrast_df %>%
  mutate(
    significant = ifelse(asymp.LCL * asymp.UCL > 0, "p < .05", "p ≥ .05")
  )

my_plot <- ggplot(contrast_df, aes(x = jitter, y = estimate)) +
  
  # --- Add Significance Shading (Johnson-Neyman style) ---
  # This geom_ribbon shades the entire background based on the 'significant'
  # variable we created. It's drawn first to be in the background.
  geom_ribbon(aes(ymin = -Inf, ymax = Inf, fill = significant), alpha = 0.2) +
  
  # --- Original Plot Layers ---
  # Add a horizontal line at y=0 (the null effect)
  geom_hline(yintercept = 0, linetype = "dashed", color = "grey50") +
  
  # Add the confidence interval ribbon (e.g., 95% CI)
  # We set 'fill' directly to avoid interfering with the significance legend.
  geom_ribbon(aes(ymin = asymp.LCL, ymax = asymp.UCL), alpha = 0.3, fill = "black") +
  
  # Add the line for the point estimate
  geom_line(color = "black", linewidth = 1) +
  
  # --- Customize Labels and Title ---
  labs(
    title = title, # Add a main title
    x = "RSI (ms)",
    y = y_label_name,
    fill = "Significance" # This renames the legend title
  ) +
  
  # --- Control Colors and Legend for Significance Shading ---
  scale_fill_manual(
    values = c("p < .05" = "lightcoral", "p ≥ .05" = "grey80"),
    labels = c("p < .05", "n.s.")
  ) +
  
  # --- Theme and Font Size Control ---
  theme_minimal() +
  theme(
    # Apply the font to the title
    plot.title = element_text(size = 18, hjust = 0.5, family = font),
    
    # Apply the font to axis labels
    axis.title.x = element_text(size = 14, family = font),
    axis.title.y = element_text(size = 14, family = font),
    
    # Apply the font to axis tick labels (the numbers)
    axis.text.x = element_text(size = 12, family = font),
    axis.text.y = element_text(size = 12, family = font),
    
    # Apply the font to the legend
    legend.title = element_text(size = 12, family = font),
    legend.text = element_text(size = 11, family = font),
    legend.position = "top"
  )

print(my_plot)

# ggsave(
#   filename = sprintf("%s/%s.png", table_output_path, plot_name),
#   plot = my_plot,
#   width = 8,        # Width in inches
#   height = 6,       # Height in inches
#   dpi = 600,        # Dots per inch (resolution)
#   bg = "white"      # Specify a white background
# )

# ------------------------------------------------------------------------------
# [Supplement] Trial-level models (Accuracy effects)
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
analysis_name <- "single_trial_2s"
# analysis_name <- "single_trial_3"
sample <- "similarity"
home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/long_data_full.csv", home_dir)

df <- read.csv(csv_path)
df <- subset(df, df$congruent == 0) # take only incongruent trials for err vs corr analysis

df$sub <- as.factor(df$sub)
df_to_check <- subset(df, df$acc == 0)
agg_df <- aggregate(df_to_check$acc ~ sub, data = df_to_check, FUN = length)
sub_list <- filter(agg_df, agg_df$`df_to_check$acc` >= 6)$sub

df <- df[df$sub %in% sub_list, ]

df$acc <- as.factor(df$acc)
contrasts(df$acc) <- rev(contr.sum(2))

if (sample == "similarity") {
  df$similarity <- ordered(df$similarity)
  model <- clmm(similarity ~ acc + (1 | sub), data = df)
} else if (sample == "hr") {
  df$similarity <- ifelse(df$similarity == 2, 1, 0)
  df$similarity <- as.factor(df$similarity)
  model <- glmer(similarity ~ acc + (1 | sub), data = df, family = binomial)
}

summary(model)
confint(model)

# ------------------------------------------------------------------------------
# [Supplement] Average WMRI and recognition peformance by congruency (N bins)
# ------------------------------------------------------------------------------
rm(list = ls())

appendix_code_path <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/working-memory-error-dataset/code/statistics/"
source(sprintf("%s/lmer_export_apa.R", appendix_code_path))

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
table_output_path <- sprintf("%swme-face-jitter-l/apa_tables/", home_dir)
df_var <- "congruent"
sample <- "similarity"
n_bins <- 10

if (sample == "similarity") {
  analysis_name <- sprintf("main_wm_%s", df_var)
} else if (sample == "hr") {
  analysis_name <- sprintf("main_wm_con_2_%s", df_var)
}

home_dir <- "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path <- sprintf("%swme-face-jitter-l/%sile_data_%s_%s.csv", home_dir, n_bins, sample, df_var)
df <- read.csv(csv_path)

df$sub <- as.factor(df$sub)
df$congruent <- as.factor(df$congruent)  
contrasts(df$congruent) <- rev(contr.sum(2))

df$rsi <- as.numeric(df$rsi)
df$rsi <- scale(df$rsi)

if (sample == "similarity") {
  df$similarity <- scale(df$similarity)
  model <- lmer(similarity ~ congruent * poly(rsi, 2) + (1 | sub), data = df)
} else if (sample == "hr") {
  df$hr <- scale(df$hr)
  model <- lmer(hr ~ congruent * poly(rsi, 2) + (1 | sub), data = df)
}

summary(model)
# lmer_export_apa(model = model, path = sprintf("%s/%s_%s.docx", table_output_path, analysis_name, n_bins))