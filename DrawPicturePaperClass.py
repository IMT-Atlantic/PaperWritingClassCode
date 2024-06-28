import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 导入数据
file_path = "E:/EasyData/PaperClassData/Data20240627.xlsx"
data = pd.read_excel(file_path)

# 数据转换
df = pd.melt(data, id_vars=['Weeks'], var_name='Group', value_name='Tumor_Size')

# 创建图形对象
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8),
                               gridspec_kw={'height_ratios': [1, 1], 'hspace': 0.05})

# 绘图
for key, grp in df.groupby(['Group']):
    ax1.plot(grp['Weeks'], grp['Tumor_Size'], label=key)
    ax1.scatter(grp['Weeks'], grp['Tumor_Size'], s=20)
    ax2.plot(grp['Weeks'], grp['Tumor_Size'], label=key)
    ax2.scatter(grp['Weeks'], grp['Tumor_Size'], s=20)

# 设置轴标签和标题
ax1.set_title('Tumor Size Over Time in Different Groups')
ax1.set_ylabel('Tumor Volume (mm³)')
ax2.set_xlabel('Weeks')
ax2.set_ylabel('Tumor Volume (mm³)')

# 设置y轴范围和断轴效果
ax1.set_ylim(500, 2000)  # 上段y轴
ax2.set_ylim(0, 400)    # 下段y轴

# 隐藏上下子图之中的x轴刻度，避免重叠
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  # 上轴不显示x轴标签
ax2.xaxis.tick_bottom()

# 设置比例尺
ax1.yaxis.set_major_locator(MultipleLocator(500))
ax2.yaxis.set_major_locator(MultipleLocator(100))

# 自定义中断y轴的符号
d = .015  # 中断符号的比例大小
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot((-d, +d), (-d, +d), **kwargs)  # 左上
ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # 右上

kwargs.update(transform=ax2.transAxes)  # 切换到下轴
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # 左下
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # 右下

# 设置主题
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.legend(loc='upper left')

# 保存结果
plt.savefig('Resultpython.png', dpi=800)
plt.savefig('Resultpython.svg', format='svg', dpi=800)

plt.show()