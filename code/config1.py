"""
###################################如需一对多推送请用 "|" 隔开uids#####################
###################################如需帮别人挂记得让他扫你的应用二维码加入你应用##################

"""
"""
#######################################(充值购买配置(即钢镚)###########################

活动入口,微信打开：http://2482241.k.gbl.njnhp5d2r0ez.cloud/?p=2482241

czgmconfig = [
    {'name': '多账号示例', 'ck': '请不要填这里', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': '多账号示例', 'ck': '请不要填这里', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]

为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key

通过浏览器打开链接获取:http://175.24.153.42:8882/getkey

参数填在下方
"""
czgmconfig = [
    {
        "name": "这里填账号的备注",
        "ck": "这里是钢镚的ck",
        "uids": "这里是要推送到的UID",
        "key": "这里是链接中获取到的Key",
    },
]
######################################################################################
"""
###############################美添赚配置##############################################

活动入口,微信打开：http://tg.1694188516.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=125051
mtzconfig = [
    {'name': '多账户示例', 'ck': '不要填在这里', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': '多账户示例', 'ck': '不要填在这里', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]

ck:账号的ck,抓包的任意接口headers中的Authorization参数

为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key

通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
"""
mtzconfig = [
    {
        "name": "1",
        "ck": "share:login:283880b7fa7cfd98a76732e6c4b2b3d0",
        "uids": "UID_51054",
        "key": "7a0014ef6232534c95f1c53aca6bd7d0",
    },
]
#########################################################################
"""
######################小阅阅的参数配置列表#################################

活动入口,微信打开：https://sd8690.viptaoyou.top:10261/yunonline/v1/auth/e9a46f47cb3bbb8e5c194f2771cf21e4?codeurl=sd8690.viptaoyou.top:10261&codeuserid=2&time=1694188607

xyyconfig = [
    {'name': '多账户示例', 'ck': '不要填在这里', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': '多账户示例', 'ck': '不要填在这里', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
ck:账号的ck,抓包的任意接口headers中的Authorization参数

为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key

通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
"""
xyyconfig = [
    {"name": "这里是账号的备注", "ck": "这里是小阅阅的ck", "uids": "要推送到UID", "key": "链接中获取到的key"},
]
#########################################################################
"""
##############################星空阅读和元宝阅读配置#######################

活动入口,微信打开

星空阅读阅读：http://mr1694188748657.yupgszx.cn/ox/index.html?mid=3G72UTPA8 

元宝阅读：http://mr1694188785426.uvritjq.cn/coin/index.html?mid=AG5QA7QBR

注:注册完两个平台只需要抓其中一个平台从参数即可跑两个平台

xkybconfig = [
    {'name': '多账户示例', 'un': '不要填在这里', 'token': 'xxx',"uids": 'UIDxxx|UIDxxx|UIDxxx','key':'xxxx'},
    {'name': '多账户示例', 'un': '不要填在这里', 'token': 'xxx',"uids": 'xxx','key':'xxxx'},
]

ck:账号的ck,抓包的任意接口headers中的Authorization参数

注:注册完两个平台只需要抓其中一个平台从参数即可跑两个平台

key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。

为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key

通过浏览器打开链接获取:http://175.24.153.42:8882/getkey

"""
xkybconfig = [
    {
        "name": "这里是账号的备注",
        "un": "星空和元宝的un",
        "token": "星空和元宝的token",
        "uids": "要推送到的UID",
        "key": "上面链接获取key",
    },
]
##################################这里填推送平台的token#######################################
"""

参数解释
appToken:wxpusher的参数，在你创建应用的过程中，你应该已经看到appToken，如果没有保存，可以通过下面的方式重制它。
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 应用管理->appToken->重置appToken
"""
appToken = "AT_tKPJbBmD238BNUTJ2kttRtmibwwcSlmh"
#########################################################################
"""
其他参数
参数解释
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
printf:日志打印参数，0是不打印调试日志，1是打印调试日志
dictType:标志参数请勿修改
"""
threadingf = 1
printf = 1
dictType = {
    "czgm": "充值购买过检测",
    "mtzyd": "美添赚过检测",
    "xyyyd": "小阅阅过检测",
    "ybxkhh": "星空元宝过检测",
    "yuanbao": "元宝过检测",
    "xingkong": "星空过检测",
}

ybtxbz = 3000
xktxbz = 3000
czgmtxbz = 3000
xyytxbz = 3000
# 3000为提现的金币数,按需更改
# 3000为提现的金币数,按需更改
# 3000为提现的金币数,按需更改
# 3000为提现的金币数,按需更改
