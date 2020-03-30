from selenium import webdriver
import time
#weibourl = 'https://s.weibo.com/weibo?q=%23%E5%A5%A5%E6%96%AF%E5%8D%A1%23&wvr=6&Refer=SWeibo_box'
weibourl='http://www.shanghai-xingyu.com/?m=vod-play-id-5250-src-1-num-1.html'
def open_chrome():
    diver = webdriver.Chrome(executable_path='//Users/gongjie/Desktop/pythonstudy/chromedriver')
    diver.start_client()
    return diver

def find_weibo_seachnum():
   sel = "div#mvideo.video.dplayer.dplayer-no-danmaku.dplayer-paused>div.dplayer-video-wrap>video.dplayer-video.dplayer-video-current"
   elems=driver.find_element_by_css_selector(sel).get_attribute("ppp-src")
   time.sleep(0.5)

   return elems


while True:
    driver = open_chrome()
    driver.get(weibourl)
    time.sleep(8)
    print('aaa')
    num = find_weibo_seachnum()
    print(num)
    print('ddd')
    break