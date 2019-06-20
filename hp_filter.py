import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import os

path = 'E:\\PythonProjects\\AnomalyDetection\\data\\5minStepsWithRealID-iphone00.csv'
df = pd.read_csv(path)
userid = 847471356
df_user = df.loc[df[' user ID'] == userid]
print(df_user)

list_result = []
rows = df_user.shape[0]
for row in range(rows):
    print(row)
    list_minutes = df_user.iloc[row,5:-1]
    cycle, trend = sm.tsa.filters.hpfilter(list_minutes, 100)
    print(trend)
    list_result.append(trend)

df_result = pd.DataFrame(list_result)
print(df_result)
df_result.to_csv('result//'+repr(userid)+'_hp_filter.csv',header=False)
'''
list_result = []
i = 0
for userid in userlist:
    df_user = df.loc[df['userid'] == userid]
    list_ave = df_user.iloc[0, 3:].values.tolist()
    cycle, trend = sm.tsa.filters.hpfilter(list_ave, 100)
    trend = trend.tolist()
    cycle = cycle.tolist()
    list_result.append([userid, 'trend'] + trend)
    # os.system('pause')
    df_plt = pd.DataFrame()
    df_plt['original data'] = list_ave
    df_plt['cycle'] = cycle
    df_plt['trend'] = trend
    fig, ax = plt.subplots()
    df_plt[['original data', 'trend']].plot(ax=ax, fontsize=16)
    plt.savefig('result//figs//'+repr(userid)+"_fig.png")

print(list_result)
df_result = pd.DataFrame(list_result)
# df_result = list_result
df_result.to_csv('result//hp_filter.csv')
'''