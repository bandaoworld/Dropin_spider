import requests
#from fake_useragent import UserAgent

def spider():
    url = 'http://duopin_app_api.hearinmusic.com/app/article/list3'
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060133) NetType/WIFI Language/zh_CN'}
    params = {'orderType':'CHANNEL_NEW', 'pageSize':'20', 'channelIds':'976', 'pageNum':'1'}
    response = requests.get(url=url, headers=headers, params=params).content.decode()
    print(response)

if __name__ == "__main__":
    spider()
    print('over!')









