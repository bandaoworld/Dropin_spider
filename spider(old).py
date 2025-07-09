from wiki_detail import *
from wiki_main import *
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    dropin = dropin_wiki()
    detail = dropin_wiki_detail()
    
    typeId = 15
    
    file_list = os.listdir(f'./{detail.typeId_chinese(str(typeId))}/json')
    
    
    dataId_list, name_list = dropin.run(str(typeId))
    
    for count in range(len(dataId_list)):
            
            print(count)
            if name_list[count] + '.json' in file_list:
                print(name_list[count] +'.json 该文件已存在')
                continue
            else:
                for i in range(3):
                    #尝试爬取三次
                    try:
                        detail.run(typeId, dataId_list[count])
                        break
                    except:
                        pass
   
                    
    print('over!')
