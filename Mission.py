import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'
df = pd.read_csv('가공데이터.csv', encoding="cp949")
df2 = df[['사용일자']].values
date = df2[0,0]

df3 = df[['노선명', '승차총승객수']].groupby(['노선명'], as_index=False).mean().sort_values(by='승차총승객수', ascending=False).head(5).values
df4 = df[['노선명', '승차총승객수']].groupby(['노선명'], as_index=False).mean().sort_values(by='승차총승객수', ascending=True).head(5).values
xp = np.array(df3[:,0])
yp = np.array(df3[:,1])
xp2 = np.array(df4[:,0])
yp2 = np.array(df4[:,1])

df5 = df[['역명', '승차총승객수']].sort_values(by='승차총승객수', ascending=False).head(5).values
xp3 = np.array(df5[:,0])
yp3 = np.array(df5[:,1])

df6 = df[['노선명', '승차총승객수']].groupby(['노선명'], as_index=False).mean().round(1).values
xp4 = np.array(df6[:,0])
yp4 = np.array(df6[:,1])

# 승차객수 상위 5개 노선과 하위 5개 노선
plt.subplot(1, 2, 1)
plt.bar(xp, yp, width=0.3)
plt.title('승차객수 상위 5개 노선')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.subplot(1, 2, 2)
plt.bar(xp2, yp2, width=0.3, color='orange')
plt.title('승차객수 하위 5개 노선 ('+str(date)+')')
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# 승차객수 상위 5개 역
# mycolors = ['red', 'green', 'blue', 'orange', 'magenta']
# plt.bar(xp3, yp3, width=0.5, color=mycolors, alpha=0.5)
# plt.title('승차객수 상위 5개 역 ('+str(date)+")")
# plt.grid(axis='y', linestyle='--', linewidth=0.5)

# 노선별 평균 승차객수
# subwaycolors = ['#0052A4', '#00A84D', '#EF7C1C', '#00A5DE', '#996CAC', '#CD7C2F', '#747F00', '#E6186C', '#BB8336', '#BDB092', '#003DA5', '#0052A4', '#0052A4', '#77C4A3', '#0052A4', '#0C8E72', '#0090D2', '#00A5DE', '#D4003B', '#F5A200', '#F04938', '#B0CE18', '#EF7C1C', '#0052A4', '#77C4A3']
# plt.figure(figsize=(14,7))
# plt.bar(xp4, yp4, width=0.5, color=subwaycolors)
# plt.title("노선별 평균 승차객수 ("+str(date)+")")
# plt.grid(axis='y', linestyle='--', linewidth=0.5)
# plt.xticks(xp4, rotation=45)

plt.show()