import sys
import requests

# 点餐助手
request_url = sys.argv[1]

# 请求头
header = {
    "Content-Type": "application/json"
}

# 请求体
body = {
    "msgtype" : "text",
    "text" : {
        "content" : "点餐提醒（from github actions）"
    }
}

# 发送post请求
response = requests.post(url= request_url, json = body, headers= header)

# 打印结果
print(response.json())
