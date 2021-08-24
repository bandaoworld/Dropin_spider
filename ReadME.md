#1.这是一个Dropin多频的爬虫
##多频百科api,[视频使用教程](https://www.bilibili.com/video/av377571588)
####例子：http://duopin_app_api.hearinmusic.com/app/ency/encyDetail?typeId=13&dataId=377
```
GET方法
url = 'http://duopin_app_api.hearinmusic.com/app/ency/encyDetail?'

params = {
    'typeId':str(typeId),
    'dataId':str(dataId)
}

#typeId和中文对应的关系
typeId_dict = {
    '12':'艺人',#(最大10000+)
    '13':'风格',#(最大379)
    '14':'厂牌',#(最大1933)
    '15':'场所',#(最大40)
    '16':'电音节',#(最大200)
    '17':'事件',#(最大3)
    '11':'其他'#(最大45)
}

dataId的json放在了dataId_json文件夹中
```
###爬虫主体在wiki_main.py（获取多频百科的列表）和wiki_detail.py（获取多频百科的某一词条的具体信息）中
###spider.py把两个结合，爬取全部的多频百科全部的内容

---------------
#2.其他接口（都为GET方法）
####以下的pageSize为返回的内容数量，memberId为用户的id
```
关注api:http://duopin_app_api.hearinmusic.com/app/fans/idolList?
params = {'pageSize':'20', 'isAsc':'desc', 'pageNum':'1', 'memberId':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/fans/idolList?pageSize=20&isAsc=desc&pageNum=1&memberId=104
```

```
粉丝api:http://duopin_app_api.hearinmusic.com/app/fans/fansList?
params = {'pageSize':'20', 'isAsc':'desc', 'pageNum':'1', 'memberId':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/fans/fansList?pageSize=20&isAsc=desc&pageNum=1&memberId=104
```

```
个人信息api：http://duopin_app_api.hearinmusic.com/app/member/info?
params = {'memberId':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/member/info?memberId=104
```

```
查看个人发布api: http://duopin_app_api.hearinmusic.com/app/article/list3?
params = {'pageSize':'20', 'pageNum':'1', 'memberId':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/article/list3?pageSize=20&pageNum=1&memberId=104
```

```
评论api:http://duopin_app_api.hearinmusic.com/app/comment/list?
params = {'memberId':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/comment/list?articleId=5915
```
####以下的id为文章的id
```
信号(文章)url:http://dropinapp.hearinmusic.com/#/signalDet?
params = {'id':'%s'}
例子：http://dropinapp.hearinmusic.com/#/signalDet?id=5915
```

```
信号(文章)分享url:http://dropinapp.hearinmusic.com/#/signalShare?
params = {'id':'%s'}
例子：http://dropinapp.hearinmusic.com/#/signalShare?id=5915
```

```
信号(文章)api:http://duopin_app_api.hearinmusic.com/app/article/v1_0/detailWeb?
params = {'id':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/article/v1_0/detailWeb?id=5915
```
####以下的id为频段的id
```
频段info_api：http://duopin_app_api.hearinmusic.com/app/channel/detail?
params = {'id':'%s'}
例子：http://duopin_app_api.hearinmusic.com/app/channel/detail?&id=976
```
####以下的orderType为请求的类型，pageSize为返回的内容数量，channelIds为频段的id
```
频段content_api:http://duopin_app_api.hearinmusic.com/app/article/list3?
params = {'orderType':'CHANNEL_NEW', 'pageSize':'20', 'channelIds':'%s', 'pageNum':'1'}
例子：http://duopin_app_api.hearinmusic.com/app/article/list3?orderType=CHANNEL_NEW&pageSize=20&channelIds=976&pageNum=1
```

```
首页api:http://duopin_app_api.hearinmusic.com/app/article/list3?
params = {'orderType':'HOME', 'pageSize':'20', 'pageNum':'1'}
例子：http://duopin_app_api.hearinmusic.com/app/article/list3?orderType=HOME&pageSize=20&pageNum=1
```

```
研究所api:http://duopin_app_api.hearinmusic.com/app/search/research
无params
```
####以下的keyword为关键字
```
搜索api：http://duopin_app_api.hearinmusic.com/app/search/searchAll?
params = {'keyword':'avicii'}
例子：http://duopin_app_api.hearinmusic.com/app/search/searchAll?keyword=avicii
```
