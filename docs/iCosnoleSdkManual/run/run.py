with open('..\\_book\\gitbook\\theme.js', '+r', encoding="utf-8") as file:
    content = file.read()

target = "if(m)for(n.handler"

if target in content:
    content = content.replace(target, "if(false)for(n.handler")
    # 读写偏移位置移到最开始处
    with open('..\\_book\\gitbook\\theme.js', '+r', encoding="utf-8") as file:
        file.seek(0, 0)
        file.write(content)
        # 设置文件结尾 EOF
        # 是设置文件结尾为了避免多字符 替换为少字符后文件尾部有原文件残余字符
        file.truncate()
        file.close()
    print("替换成功")
else:
    print("无需替换")
