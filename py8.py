from selenium import webdriver
import time
#weibourl = 'https://s.weibo.com/weibo?q=%23%E5%A5%A5%E6%96%AF%E5%8D%A1%23&wvr=6&Refer=SWeibo_box'
weibourl='http://data.10jqka.com.cn/market/longhu/'
def open_chrome():
    diver = webdriver.Chrome(executable_path='//Users/gongjie/Desktop/pythonstudy/chromedriver')
    diver.start_client()
    return diver

def find_weibo_seachnum():
   sel = "input#ggmxSearchIpt.search-input.autosearch"
   elems=driver.find_element_by_css_selector(sel).send_keys("万马股份")
   time.sleep(0.5)
   searchkey ='div.page-cont>div#ggmx.page-main.hxc3-trgger-box>div.table-tit>div.page-search-box>input.search-btn.autosearch-btn'
   elem = driver.find_element_by_css_selector(searchkey).click()
   return elems


while True:
    driver = open_chrome()
    driver.get(weibourl)
    time.sleep(2)
    print('aaa')
    num = find_weibo_seachnum()
    break