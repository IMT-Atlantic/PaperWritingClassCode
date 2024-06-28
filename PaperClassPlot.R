setwd("D:/Rproject/Plot/PaperClass20240627")

library(openxlsx)
library(ggplot2)
library(tidyr)
library(patchwork)
library(RColorBrewer)
library(ggbreak)
library(svglite)

# import data
file_path <- "E:/EasyData/PaperClassData/Data20240627.xlsx"
data <- read.xlsx(file_path)

# 数据重塑ggplot2
data <- gather(data, key = "Group", value = "Tumor_Size", -Weeks)
## 简易绘图
# 绘图
ggplot(data, aes(x = Weeks, y = Tumor_Size, color = Group, group = Group)) +
  geom_line(size = 1) +                  
  geom_point(size = 2) +                 
  labs(title = "Tumor Size Over Time Dans Different Group", 
       x = "Weeks", 
       y = "Tumor Volume (mm³)") +         
  theme_minimal() +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(), 
        legend.position = "right")         

## 截断绘图
# 将数据从宽格式转换为长格式
dt <- pivot_longer(data, cols = -Weeks, names_to = "Group", values_to = "Tumor_Size")
# 截断y轴
p <- ggplot(dt, aes(x = Weeks, y = Tumor_Size, color = Group, group = Group)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  labs(
    title = "Tumor Size Over Time in Different Groups",
    x = "Weeks",
    y = "Tumor Volume (mm³)"
  ) +
  theme_minimal() +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    legend.position = "right"
  ) +
  scale_y_continuous(limits = c(0, 2000),
                     breaks = c(0, 200, 400))+
  scale_y_break(c(400, 500), scales = "free",
                ticklabels = c(500, 1000, 1500, 2000),
                expand = expansion(add = c(0, 0)),
                space = 1)
# 添加主坐标轴
p <- p + theme(
  axis.line = element_line(color = "black"),
  axis.ticks = element_line(color = "black"),
)
ggsave(plot = p, 'Result.png', width = 10, height = 8, dpi = 800)
ggsave("ResultR1.svg", plot = p, device = "svg", width = 10, height = 8, dpi = 800)












