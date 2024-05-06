import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('iris.csv')

# 1. 绘制散点图
sns.scatterplot(data=df, x='Sepal.Length', y='Sepal.Width', hue='Species')
# x轴为萼片长度,y轴为萼片宽度,颜色区分种类
plt.show()

# 2. 绘制箱图
sns.boxplot(data=df, x='Petal.Length', hue='Species')
# 变量为花瓣长度,颜色区分种类
plt.show()

# 3. 绘制小提琴图
sns.violinplot(data=df, x='Petal.Length', hue='Species')
# 变量为花瓣长度,颜色区分种类
plt.show()

# 4. 计算统计量
stats = df.groupby('Species').agg(['min', 'mean'])
# 按照种类分组,agg聚合函数中的min,mean计算最小值和平均值
print(stats)

# 5. 计数
count = df[df['Sepal.Length'] > 6].groupby('Species').size()
# 按照种类分组,统计萼片长度大于6的数量
print(count)