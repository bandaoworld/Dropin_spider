import requests
import json

class WeeklyVote(object):
    def __init__(self):
        self.voteFilterUrl = 'https://webapi.hearinmusic.com/dp/vote/getMusicVoteFilter?awId=4'
        self.voteListUrl = 'https://webapi.hearinmusic.com/dp/vote/musicVoteList'
        self.header = {
            'content-type':'application/json;charset=UTF-8',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
    
    def getVoteFilter(self):
        voteFilter = {}
        response = requests.get(url=self.voteFilterUrl, headers=self.header).json()["data"]["voteFilter"]
        # print(response)
        """
        flag：2     提名中
        flag：1     进行中
        flag：0     已结束
        """
        for i in response:
            voteFilter.update({f"第{i['num']}期":i["voteId"]})

        print(voteFilter)
        return voteFilter
        
    def getVoteList(self, voteId):
        voteDict = {}
        data = {
            "sortType":0,
            "voteId":voteId,
        }
        response = requests.post(url=self.voteListUrl, headers=self.header, data=json.dumps(data)).json()["data"]
        for i in response:
            voteDict.update({f"{i['artist']} - {i['name']}":i["relatedLinkList"][0]["url"]})

        # print(voteList)
        return voteDict

    def saveVoteList(self, voteName, voteDict):
        textPath = f"./{voteName}.txt"
        for (count, vote) in enumerate(voteDict):
            print(vote)
            with open(textPath, 'a+', encoding='utf8') as fp:
                    fp.write(f"{count+1}《{vote}》\n{voteDict[vote]}\n\n")
    
    def run(self):
        voteIdList = self.getVoteFilter()
        
        # 默认取进行中的投票
        voteName = list(voteIdList.keys())[1]
        
        voteId = voteIdList[voteName] 
        print(voteId)
        
        voteDict = self.getVoteList(voteId)
        self.saveVoteList(voteName, voteDict)
        
        
if __name__ == "__main__":
    weeklyVote = WeeklyVote()
    weeklyVote.run()
    print('over!')

