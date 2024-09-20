# install.packages(c("afex", "emmeans", "reshape2"))

# Load libraries
library(afex)
library(emmeans)
library(reshape2)

rm(list = ls())

condition <- "corr"
home_dir = "/Users/fzaki001/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Documents/DA/"
csv_path = sprintf("%swme-face-new/wme-new-%s-anova-df.csv", home_dir, condition)
df <- read.csv(csv_path)

df$sub = as.character(df$sub)
df$response = as.factor(df$response)

if (condition == "corr") {
  df$corr = as.factor(df$corr)
  levels(df$corr) <- c("Corr", "Err")
  anova_result <- aov_car(value ~ response * corr + Error(sub/(response * corr)), 
                        data = df)
  emm <- emmeans(anova_result, ~ response * corr)
} else if (condition == "con") {
  df$con = as.factor(df$con)
  levels(df$con) <- c("Congruent", "Incongruent")
  anova_result <- aov_car(value ~ response * con + Error(sub/(response * con)), 
                        data = df)
  emm <- emmeans(anova_result, ~ response * con)
}

# View ANOVA table
summary(anova_result)

# Pairwise comparisons for ResponseType within Congruency
pairs(emm, by = condition)
pairs(emm, by = "response")
pairs(emm, adjust = "fdr")