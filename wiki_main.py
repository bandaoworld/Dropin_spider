import requests
import json
#from fake_useragent import UserAgent
#from wiki_detail import *

class dropin_wiki(object):
    '''获取多频百科的列表'''
    def wiki_spider(self, typeId):
        url = 'http://duopin_app_api.hearinmusic.com/app/ency/searchChildPage'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'okhttp/3.8.1'
            }
        payload = {
            "pageSize":'10000',  #在这里修改最大值
            "typeId":typeId, 
            "pageNum":'1'
            }
        #typeId分类讨论
        if typeId == '12' or typeId == '13' or typeId == '16' or typeId == '11':
            payload["encySearchList"] = [{"keyword":"","parentId":"-1","typeId":"-1"},{"keyword":"","parentId":"-1","typeId":"-1"}]
        elif typeId == '14' or typeId == '15':
            payload["encySearchList"] = [{"keyword":"","parentId":"-1","typeId":"-1"},{"keyword":"","parentId":"-1","typeId":"-1"}, {"keyword":"","parentId":"-1","typeId":"-1"}]
        elif typeId == '17':
            payload["encySearchList"] = [{"keyword":"","parentId":"-1","typeId":"-1"}]    
            
        response = requests.post(url=url, headers=headers, data=json.dumps(payload)).json()['data']['records']
        #print(response)
        name_list = [i['name'] for i in response]
        dataId_list = [i['dataId'] for i in response]
        print(len(dataId_list))
        return dataId_list, name_list
        
    def save_info(self, typeId, dataId_list, name_list):
        '''保存某个typeId下dataId对应关系'''
        typeId_dict = {
            '12':'艺人',#(最大10000)
            '13':'风格',#(最大379)
            '14':'厂牌',#(最大1933)
            '15':'场所',#(最大40)
            '16':'电音节',#(最大200)
            '17':'事件',#(最大3)
            '11':'其他'#(最大45)
        }
        info_dict = {dataId_list[count]:name_list[count] for count in range(len(dataId_list))}
        #print(info_dict)
        json_path = f"./{typeId_dict[typeId]}.json"
        fp = open(json_path, 'w', encoding='utf8')
        json.dump(info_dict, fp = fp, ensure_ascii=False, indent=4, sort_keys=True)
        
    def run(self, typeId):
        dataId_list, name_list = self.wiki_spider(typeId)
        self.save_info(typeId,  dataId_list, name_list)
        
        return dataId_list, name_list     

if __name__ == "__main__":
    dropin = dropin_wiki()
    dropin.run('12')
    print('over!')


