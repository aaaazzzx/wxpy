# 导入模块

from wxpy import *
bot = Bot()

# 机器人账号自身
myself = bot.self

# 搜索名称
found = bot.friends().search('哼哼妈', sex=FEMALE, city='宜春')
# [<Friend: 游否>]
# 确保搜索结果是唯一的，并取出唯一结果
henghengma = ensure_one(found)
# <Friend: 哼哼妈>
my_friend = ensure_one(bot.search('机器狗'))


tuling = Tuling(api_key='2dd9d79961c745f481bfc6dae9f5ae34')    # 申请的 API KEY

# 使用图灵机器人自动与指定好友聊天
@bot.register(henghengma)
def reply_my_friend(msg):
    tuling.do_reply(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
        tuling.do_reply(msg)




# henghengma_houzhui = '\n——来自傻狗机器人'

# 发送文本
# henghengma.send('啦啦啦，一只大臭狗%s'%(henghengma_houzhui))


# 堵塞线程，并进入 Python 命令行
embed()
