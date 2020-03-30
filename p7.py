import requests
import datetime
api_url='https://api.github.com/search/repositories?q=language:python'
#得到项目列表和项目的时间
# rev_info = requests.get(api_url).json()['items'][0]
# print(rev_info)
# for item in rev_info:
#     create_time = item['created_at']
#     print(create_time)
#    # s_date = create_time
#    # if(create_time - now)

#得到现在的时间
#2020-02-21T12:35:31Z
d1 = '2020-02-21T12:35:31Z'
d2 = datetime.datetime.strptime(d1,'%Y-%m-%dT%H:%M:%SZ')
print(d2)
now = datetime.datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')
print(now)
# d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
# # d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
# # delta = d1 - d2
# # print delta.days