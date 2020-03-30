import pandas as pd
from pandas import DataFrame
import math
import os
import time

df_empty = pd.DataFrame(columns=['月份', '时间', '代码', '买入价', '卖出价', '数量', '买入流水', '卖出流水'])
df_empty2 = pd.DataFrame(columns=['月份', '时间', '代码', '买入价', '卖出价', '数量', '买入流水', '卖出流水'])
df = pd.read_excel("/Users/gongjie/Desktop/pythonstudy/2b.xlsx", sheet_name=0, converters={u'证券代码': str})


# 获得数据行数
total_rows = df.index + 1

print(total_rows)

# 默认数据
i = 0
#获得时间
itime = time.localtime(time.time())
imonth = itime.tm_mon
idate = itime.tm_mday
strmonth = str(imonth)+'月'
print(imonth,idate)

for i in range(0, len(df)):

    if df.iloc[i, 3] == '买入':

        df_empty2.loc[0, '月份'] = strmonth
        df_empty2['时间'] = str(idate)
        df_empty2['代码'] = df.iloc[i, 1]
        df_empty2['买入价'] = df.iloc[i, 4]
        df_empty2['卖出价'] = 0
        df_empty2['数量'] = df.iloc[i, 5]
        df_empty2['买入流水'] = df.iloc[i, 6]
        df_empty2['卖出流水'] = 0
    # print(df_empty2)
    else:
        df_empty2['月份'] = strmonth
        df_empty2['时间'] = str(idate)
        df_empty2['代码'] = df.iloc[i, 1]
        df_empty2['买入价'] = 0
        df_empty2['卖出价'] = df.iloc[i, 4]
        df_empty2['数量'] = df.iloc[i, 5]
        df_empty2['买入流水'] = 0
        df_empty2['卖出流水'] = df.iloc[i, 6]


    df_empty = df_empty.append(df_empty2, ignore_index=True)

print(df_empty)

print("获取到所有的值：\n{0}".format(df_empty))  # 格式化输出

# 写入excel
if (os.path.exists('/Users/gongjie/Desktop/2a.xlsx')):
    write = pd.ExcelWriter("/Users/gongjie/Desktop/2a.xlsx", mode='a')
else:
    write = pd.ExcelWriter("/Users/gongjie/Desktop/2a.xlsx", mode='w')

df_empty.to_excel(write, strmonth, index=0,startrow=0,startcol=0)

write.save()
write.close()
print("获取到所有的值：\n{0}".format(df_empty))  # 格式化输出
