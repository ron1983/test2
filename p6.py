#https://api.github.com/users/kennethreitz/starred
import requests
import webbrowser
starred_id = []
laststared_id=[]
#获得全部star
strard_url = 'https://api.github.com/users/kennethreitz/starred'
rev_info = requests.get(strard_url).json()
#print(rev_info[2]['id'])
for strjson in rev_info:
    print(strjson['id'])
    #for id2 in strjson:
        #print(strjson['id'])


#     starred_id.append(iid)
# #对比新增star保存到newstarred_id
# urllist = []
# if laststared_id:
#     laststared_id = starred_id
# else:
#     for nid in starred_id:
#         if nid not in laststared_id:
#             urllist = rev_info['owner']
#             webbrowser.open(urllist['url'])
#


#open newstarred_id