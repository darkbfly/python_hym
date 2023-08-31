'''
活动入口:（若链接打不开，可复制到手机浏览器里打开）

http://ebb.maisucaiya.cloud/user/index.html?mid=1694834307044081664

http://ebb.maisucaiya.cloud/user/index.html?mid=1694834307044081664
# 青龙定时 每30分钟一次
# 抓包 http://ebb.vinse.cn/api headers中的  un，uid，token填到脚本最下方的,脚本最下方的，脚本最下方的，脚本最下方的，脚本最下方的cklist中，把xxxx替换成你的参数
带推送服务，请先配置好推送在运行
appToken请看推送文档
#https://wxpusher.zjiecode.com/docs/#/


key # key从这里获取http://175.24.153.42:8882/getkey

'''
import time
import random
import requests
import re

key=''#这个是填回调服务器的key
appToken=''#这个是填wxpusher的appToken

topicIds=0 #这个是wxpusher的topicIds改成你自己的


def push(title,link,text,type):
    str1='''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>TITLE</title>
<style type=text/css>
   body {
   	background-image: linear-gradient(120deg, #fdfbfb 0%, #a5d0e5 100%);
    background-size: 300%;
    animation: bgAnimation 6s linear infinite;
}
@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
</style>
</head>
<body>
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
<p><a href="LINK">阅读检测文章</a></p><br>
<p><a href="http://175.24.153.42:8882/setstatus?key=KEY&type=TYPE&val=0">阅读完成确认</a></p><br>
</body>
</html>
    '''
    content=str1.replace('TITTLE',title).replace('LINK',link).replace('TEXT',text).replace('TYPE',type).replace('KEY',key)
    datapust = {
      "appToken":appToken,
      "content":content,
      "summary":title,
      "contentType":2,
      "topicIds":[topicIds],
    }
    urlpust = 'http://wxpusher.zjiecode.com/api/send/message'
    try:
        p = requests.post(url=urlpust, json=datapust).text
        print(p)
        return True
    except:
        print('推送失败！')
        return False
checkDict={
'Mzg2Mzk3Mjk5NQ==':['欢乐的小鱼儿','gh_cf733a65ca3d'],
}
def setstatus():
    u='http://175.24.153.42:8882/setstatus'
    p={'key':key,'type':'rrb','val':'1'}
    r=requests.get(u,params=p)
    print(r.text)

def getstatus():
    u = 'http://175.24.153.42:8882/getstatus'
    p = {'key':key,'type': 'rrb'}
    r = requests.get(u, params=p)
    return r.text
def getinfo(link):
    try:
        r=requests.get(link)
        #print(r.text)
        html = re.sub('\s', '', r.text)
        biz=re.findall('varbiz="(.*?)"\|\|', html)
        if biz!=[]:
            biz=biz[0]
        if biz=='' or biz==[]:
            if '__biz' in link:
                biz = re.findall('__biz=(.*?)&', link)
                if biz != []:
                    biz = biz[0]
        nickname = re.findall('varnickname=htmlDecode\("(.*?)"\);', html)
        if nickname!=[]:
            nickname=nickname[0]
        user_name = re.findall('varuser_name="(.*?)";', html)
        if user_name!=[]:
            user_name=user_name[0]
        msg_title = re.findall("varmsg_title='(.*?)'\.html\(", html)
        if msg_title!=[]:
            msg_title=msg_title[0]
        text=f'公众号唯一标识：{biz}|文章:{msg_title}|作者:{nickname}|账号:{user_name}'
        print(text)
        return nickname,user_name,msg_title,text,biz
    except Exception as e:
        print(e)
        print('异常')
        return False
class WXYD:
    def __init__(self, cg):
        self.cg=cg
        self.headers = {
            'Host': 'ebb.vinse.cn',
            'un': cg['un'],
            'mid': '1694834307044081664',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'uid': cg['uid'],
            'platform': '0',
            'token': cg['token'],
            'Origin': 'http://ebb10.twopinkone.cloud',
            'Referer': 'http://ebb10.twopinkone.cloud/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }
    # 请求个人信息
    def userinfo(self):
        u = f"http://ebb.vinse.cn/api/user/info"
        p = {"pageSize": 10}
        r = requests.post(u, headers=self.headers, json=p)
        rj = r.json()
        print(r.text)
        if rj.get('code') == 0:
            nick_name = rj.get('result').get('nickName')
            self.moneyCurrent = rj.get('result').get('integralCurrent')
            print(f'{nick_name}帮豆：{self.moneyCurrent}')
            return True
        return False

    def getUserSignDays(self):
        u = f"http://ebb.vinse.cn/api/user/getUserSignDays"
        p = {"pageSize": 10}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)
        rj = r.json()
        if int(rj.get('result').get('signStatus')) == 1:
            print("今天已经签到过了")
            return True
        u = f"http://ebb.vinse.cn/api/user/sign"
        p = {"pageSize": 10}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)
        rj = r.json()
        print(r.text)
        if rj.get('code') == 0:
            print(f'签到成功，获得{rj.get("result").get("point")}帮豆')
            return True
        print(f'签到失败 {rj}')
        return False
    def getEntryUrl(self):
        h = {
            'Host': 'u.cocozx.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'http://mr89010752.ixmgwcb.cn',
        }
        u=f'https://u.cocozx.cn/ipa/read/getEntryUrl?fr=ebb0726&uid={self.cg["uid"]}'
        r=requests.get(u,headers=h)
        print(r.text)
        rj=r.json()
        link=rj.get('result').get('url')
        n = re.findall('//mr(.*?)\.', link)[0]
        u=f'http://u.cocozx.cn/api/common/ustr?t={n}'
        p={"un":None,"token":None,"pageSize":20}
        r = requests.post(u, headers=h,json=p)
        print(r.text)
        rj = r.json()
        link=rj.get('result').get('str')+'endok'
        self.group = re.findall('&group=(.*?)endok', link)[0]
        u='http://u.cocozx.cn/ipa/read/info'
        p={"fr":"ebb0726","uid":self.cg['uid'],"group":self.group,"un":None,"token":None,"pageSize":20}
        r = requests.post(u, headers=h, json=p)
        print(r.text)
    def read(self):
        h= {
            'Host': 'u.cocozx.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Origin': 'http://mr89010752.ixmgwcb.cn',
        }
        while True:
            print('-'*50)
            u = f'http://u.cocozx.cn/ipa/read/read'
            p = {"fr":"ebb0726","uid":self.cg['uid'],"group":self.group,"un":None,"token":None,"pageSize":20}
            r = requests.post(u, headers=h, json=p)
            print(r.text)
            rj = r.json()
            if rj.get('code') == 0:
                status = rj.get('result').get('status')
                if status == 10:
                    url=rj.get('result').get('url')
                    a=getinfo(url)
                    if self.testCheck(a,url)==False:
                        return False
                    print('获取文章成功，准备阅读')
                    ts = random.randint(7, 10)
                    print(f'本次模拟读{ts}秒')
                    time.sleep(ts)
                    sub = self.submit()
                    if sub == True: return True
                    if sub == False: return False
                elif status==30:
                    print('未知情况')
                    time.sleep(2)
                    continue
                elif status==50 or status==80:
                    print('您的阅读暂时失效，请明天再来')
                    return False
                else:
                    print('本次推荐文章已全部读完')
                    return True
            else:
                print('read err')
                return False
    def testCheck(self,a,url):
        if checkDict.get(a[4]) != None:
            setstatus()
            for i in range(60):
                if i % 30 == 0:
                    push('人人帮过检测', url, a[3], 'rrb')
                getstatusinfo = getstatus()
                if getstatusinfo == '0':
                    print('过检测文章已经阅读')
                    return True
                elif getstatusinfo == '1':
                    print(f'正在等待过检测文章阅读结果{i}秒。。。')
                    time.sleep(1)
                else:
                    print('服务器异常')
                    return False
            print('过检测超时中止脚本防止黑号')
            return False
        else:return True
    def submit(self):
        h = {
            'Host': 'u.cocozx.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Origin': 'http://mr89010752.ixmgwcb.cn',
        }
        u = f'http://u.cocozx.cn/ipa/read/submit'
        p = {"fr":"ebb0726","uid":self.cg['uid'],"group":self.group,"un":None,"token":None,"pageSize":20}
        r = requests.post(u, headers=h, json=p)
        print(r.text)
        rj = r.json()
        if rj.get('code') == 0:
            result = rj.get('result')
            print(f'获得{result.get("val")}帮豆')
            progress = result.get('progress')
            if progress > 0:
                print(f'本轮剩余{progress - 1}篇文章，继续阅读阅读')
            else:
                print('阅读已完成')
                print('-' * 50)
                return True
        else:
            print('异常')
            return False

    # 提现
    def withdraw(self):
        if self.moneyCurrent < 10000:
            print('没有达到提现标准')
            return False
        elif 3000 <= self.moneyCurrent < 10000:
            txm = 3000
        elif 10000 <= self.moneyCurrent < 50000:
            txm = 10000
        elif 50000 <= self.moneyCurrent < 100000:
            txm = 50000
        else:
            txm = 100000
        u = f"http://ebb.vinse.cn/apiuser/aliWd"
        p = {"val": txm, "pageSize": 10}
        r = requests.post(u, headers=self.headers, json=p)
        print(r.text)

    def main(self):
        if self.userinfo():
            time.sleep(2)
            self.getUserSignDays()
            time.sleep(2)
            self.getEntryUrl()
            time.sleep(2)
            self.read()
            time.sleep(2)
        self.userinfo()
        time.sleep(2)
        self.withdraw()


if __name__ == '__main__':
    cklist = [
        {'un': '13107644225','uid':'1697151889185046528','token':'cf20aa2d40984d32e0dae6f7df80fcdb' }
    ]
    for i in cklist:
        api = WXYD(i)
        api.main()
