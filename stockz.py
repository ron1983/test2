import pandas as pd
from pandas import DataFrame
import math
import os
import time
#读取文件-》分析数据-》写入文件 '月份 时间 代码	买入价	卖出价	数量	 买入流水 卖出流水'
df_empty = pd.DataFrame(columns=['月份', '时间', '代码', '买入价', '卖出价', '数量', '买入流水', '卖出流水'])
df_empty2 = pd.DataFrame(columns=['月份', '时间', '代码', '买入价', '卖出价', '数量', '买入流水', '卖出流水'])
df = pd.read_excel("./2b.xlsx", sheet_name=0, converters={u'证券代码': str})
#清理数据
def clear_df_empty2():
    df_empty2['月份'] = 0
    df_empty2['时间'] = 0
    df_empty2['代码'] = 0
    df_empty2['数量'] = 0
    df_empty2['买入价'] = 0
    df_empty2['买入流水'] = 0
    df_empty2['卖出价'] = 0
    df_empty2['卖出流水'] = 0
    return

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
#分析数据
#委托时间  证券代码 证券名称 买卖标志 委托类别 状态说明 委托价格 委托数量 委托编号 成交价格 成交数量	报价方式

for i in range(0, len(df)):
    #print(df.iloc[i,5])
    clear_df_empty2()
    if df.iloc[i, 5] == '已成' or df.iloc[i, 5] == '部成':
        df_empty2.loc[0, '月份'] = strmonth
        df_empty2['时间'] = str(idate)
        df_empty2['代码'] = df.iloc[i, 1]
        df_empty2['数量'] = df.iloc[i, 10]
        if df.iloc[i, 3] == '买入':
            df_empty2['买入价'] = df.iloc[i, 9]
            df_empty2['买入流水'] = df.iloc[i, 9] * df_empty2['数量']
        else:
            df_empty2['卖出价'] = df.iloc[i, 9]
            df_empty2['卖出流水'] = df.iloc[i, 9] * df_empty2['数量']
        print(df_empty2)
        df_empty = df_empty.append(df_empty2, ignore_index=True)
    else:
        print("没有成交")


#print(df_empty)
df_empty.sort_values(by='代码', ascending=False,inplace=True)
print("获取到所有的值：\n{0}".format(df_empty))  # 格式化输出
# 写入excel
if (os.path.exists('./2a.xlsx')):
    write = pd.ExcelWriter("./2a.xlsx", mode='a')
else:
    write = pd.ExcelWriter("./2a.xlsx", mode='w')

df_empty.to_excel(write, strmonth, index=0,startrow=0,startcol=0)

write.save()
write.close()
#print("获取到所有的值：\n{0}".format(df_empty))  # 格式化输出
