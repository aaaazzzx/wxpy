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
# <Friend: 游否>
henghengma_houzhui = '\n——来自傻狗机器人'

# 发送文本
henghengma.send('啦啦啦，一只大臭狗%s'%(henghengma_houzhui))


# 堵塞线程，并进入 Python 命令行
embed()
