from wiki_detail import *
from wiki_main import *
from concurrent.futures import ThreadPoolExecutor
import os

if __name__ == "__main__":
    dropin = dropin_wiki()
    detail = dropin_wiki_detail()
    
    typeId_dict = {
        '12':'艺人',#(最大10000)
        '13':'风格',#(最大379)
        '14':'厂牌',#(最大1933)  1962
        '15':'场所',#(最大40)
        '16':'电音节',#(最大200)
        '17':'事件',#(最大3)
        '11':'其他'#(最大45) 54
    }
    
    typeId = 13
    
    #新建文件夹
    basedir = os.path.abspath(os.path.dirname(__file__))
    if not os.path.exists(os.path.join(basedir, f'{detail.typeId_chinese(str(typeId))}')):
        os.mkdir(os.path.join(basedir, f'{detail.typeId_chinese(str(typeId))}'))
 
 
    dataId_list, name_list = dropin.run(str(typeId))
      
    with ThreadPoolExecutor(100) as t:
        for count in range(len(dataId_list)):
            t.submit(detail.run, typeId, dataId_list[count])
            
    print('over!')
