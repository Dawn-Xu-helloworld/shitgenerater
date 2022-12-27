import json, random
"""
看到menzi11的作品后有感而发所做，除部分名人名言引用自menzi11的作品外，其余部分均为自制
已经很努力试图让他生成的文本更可读了，但是还是不怎么可读啊啊啊啊啊啊啊
"""
theme = "狗屁不通"
# 加载语料库
with open("datas.json", "r", encoding="utf-8") as file:
    f = file.read()
    名人名言 = json.loads(f)["famous"]
    说过 = json.loads(f)["said"]
    铺垫 = json.loads(f)["end"]
    废话 = json.loads(f)["shit"]
    主题 = json.loads(f)["theme"]
    del f
# 加载配置文件
with open("config.json", "r", encoding="utf-8") as file:
    conf = file.read()
    名言权重 = json.loads(conf)["famous"]
    废话权重 = json.loads(conf)["shit"]
    主题权重 = json.loads(conf)["theme"]
    长度 = json.loads(conf)["length"]
    del conf
# 初始化
random.shuffle(名人名言)
random.shuffle(说过)
random.shuffle(铺垫)
random.shuffle(废话)
random.shuffle(主题)
global a, b, c, d, e
a, b, c, d, e = 0, 0, 0, 0, 0


def 抽取说过():
    global a
    try:
        return 说过[a]
    except:
        random.shuffle(说过)
        a = 0
        return 说过[a]
    finally:
        a += 1


def 抽取铺垫():
    global b
    try:
        return 铺垫[b]
    except:
        random.shuffle(铺垫)
        b = 0
        return 铺垫[b]
    finally:
        b += 1


def 抽取废话():
    global c
    try:
        return 废话[c]
    except:
        random.shuffle(废话)
        c = 0
        return 废话[c]
    finally:
        c += 1


def 抽取名言():
    global d
    try:
        return 名人名言[d].format(said=抽取说过(), end=抽取铺垫())
    except:
        random.shuffle(名人名言)
        d = 0
        return 名人名言[d].format(said=抽取说过(), end=抽取铺垫())
    finally:
        d += 1


def 抽取主题():
    global e
    try:
        return 主题[e].format(theme=theme)
    except:
        random.shuffle(主题)
        e = 0
        return 主题[e].format(theme=theme)
    finally:
        e += 1


def 分支():
    名言概率 = 名言权重 / (名言权重 + 废话权重 + 主题权重)
    废话概率 = 废话权重 / (名言权重 + 废话权重 + 主题权重)
    i = random.random()
    if i <= 名言概率:
        return 抽取名言() + 抽取主题()
    elif 名言概率 <= i <= (名言概率 + 废话概率):
        return 抽取废话() + 抽取主题()
    else:
        return 抽取主题()


if __name__ == '__main__':
    theme=input("输入主题\r\n")
    while True:
        txt = 抽取名言() + 抽取主题()
        count = 1
        while len(txt) <= 长度:
            txt += 分支()
            count += 1
            if count >= 长度 // 200:
                txt += "\r\n    "
                count = 1
        print(txt)
        input("按任意键再来一篇")
        print("\r\n\r\n")
