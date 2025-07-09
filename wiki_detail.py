import requests
import html2text as ht
import time
import os
import json

class dropin_wiki_detail(object):
    '''获取多频百科的某一词条的具体信息'''
    def wiki_spider(self, typeId, dataId):
        time.sleep(2.31)
        #http://duopin_app_api.hearinmusic.com/app/ency/encyDetail?typeId=13&dataId=377
        url = 'http://duopin_app_api.hearinmusic.com/app/ency/encyDetail?'
        params = {
            'typeId':str(typeId),
            'dataId':str(dataId)
            }
        headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; NEM-AL10 Build/HONORNEM-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060133) NetType/WIFI Language/zh_CN'}
        response = requests.get(url=url, headers=headers, params=params).json()['data']
        #print(response)
        
        return response
    
    def save_style(self, wiki):
        '''该模块可以把保存风格为md文件'''
        if not os.path.exists('./style/md'):
                os.mkdir('./style/md')
                
        text_maker = ht.HTML2Text()
        text = text_maker.handle(wiki['content'])
        
        md_path = f"./style/md/{wiki['name']}.md"
        with open(md_path, 'w+', encoding='utf8') as fp:
            fp.write(f"#{wiki['name']}\n")
            fp.write(f'##基本信息\n')
            fp.write(f"###发源时间：{wiki['startTimeText']}\n###风格类型：{wiki['styleCategory']}\n")
            fp.write(f'##详情\n')
            fp.write(text)
            fp.write(f"###{wiki['remarks']}\n")
            fp.write(f"###{wiki['url']}\n")
            
        print(f"{wiki['name']}.md 保存完成")
    
    def typeId_chinese(self, typeId):
        typeId_dict = {
            '12':'艺人',#(最大10000)
            '13':'风格',#(最大379)
            '14':'厂牌',#(最大1933)
            '15':'场所',#(最大40)
            '16':'电音节',#(最大200)
            '17':'事件',#(最大3)
            '11':'其他'#(最大45)
        }
        return typeId_dict[typeId]
    
    def save_json(self, wiki, typeId):
        '''保存json模块'''
        path = f'./{self.typeId_chinese(typeId)}'
        if not os.path.exists(f'{path}'):
                os.mkdir(f'{path}')
                
        json_path = f"{path}/{wiki['name']}.json"
        fp = open(json_path, 'w', encoding='utf8')
        json.dump(wiki, fp = fp, ensure_ascii=False, indent=True)
        print(f"{wiki['name']}.json 保存完成")
    
    def run(self, typeId, dataId):
        response = self.wiki_spider(typeId, dataId)
        
        #命名合理化
        intab = "?*/\|.:><\""
        outtab = "          "
        trantab = str.maketrans(intab, outtab)
        response['name'] = response['name'].translate(trantab)
        
        self.save_json(response, str(typeId))
        
        '''
        if typeId == 13:
            # style
            #self.save_style(response)
            self.save_json(response, str(typeId))
        elif typeId == 12:
            # music
            #self.save_musician(response)
            self.save_json(response)
        '''   

if __name__ == "__main__":
    dropin_music = dropin_wiki_detail()
    #typeId, dataId
    dropin_music.run(13, 154)

