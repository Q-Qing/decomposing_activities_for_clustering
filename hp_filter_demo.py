import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)
# load the data
# userlist = [847471356, 850191387, 868504679, 248176800, 864101616, 1182684141, 847863843]
userid = 847471356
path1 = 'E:\\SJTU HEALTH\\steps\\'+ repr(userid)+'.csv'
df_day = pd.read_csv(path1, header=None)
df_day.columns = ['date', 'steps', 'count']
df_day['date'] = pd.to_datetime(df_day['date'])

path2 = 'E:\\PythonProjects\\AnomalyDetection\\data\\5minStepsWithRealID-iphone00.csv'
df_minutes = pd.read_csv(path2)
df_user = df_minutes.loc[df_minutes[' user ID'] == userid]

# path3 = 'C:\\Users\\93208\\Documents\\WeChat Files\\wxid_48p9lu80ny0t22\\FileStorage\\File\\2019-05\\checkinitialrows.csv'
# df_accu = pd.read_csv(path3)
# df_accuser = df_accu.loc[df_accu['userid'] == 935660647]
# print(df_accuser)

# list_acc = df_accuser.iloc[0,3:].values.tolist()
list_days = df_day.iloc[:,1].values.tolist()
list_days = list_days[0:60]
list_minutes = df_user.iloc[5,5:293].values.tolist()

cycle_day, trend_day = sm.tsa.filters.hpfilter(list_days, 100)
cycle_minutes, trend_minutes = sm.tsa.filters.hpfilter(list_minutes, 100)
print(trend_day)
df_plt = pd.DataFrame()
df_plt['day_steps'] = list_days
df_plt['trend_day'] = trend_day
df_plt['cycle_day'] = cycle_day
df_plt2 = pd.DataFrame()
df_plt2['minute_steps'] = list_minutes
df_plt2['trend_minute'] = trend_minutes
df_plt2['cycle_minute'] = cycle_minutes
fig, ax1 = plt.subplots()
df_plt[['day_steps','trend_day']].plot(ax=ax1,fontsize=16)
plt.show()
fig, ax2 = plt.subplots()
df_plt2[['minute_steps','trend_minute']].plot(ax=ax2,fontsize=16)
plt.show()

