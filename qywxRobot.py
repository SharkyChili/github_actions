import requests

def main():
    # 点餐助手
    request_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=dd18a2b8-94d8-4a59-a61a-f529fd60f964";

    # 请求头
    header = {
        "Content-Type": "application/json"
    }

    # 请求体
    body = {
        "msgtype" : "text",
        "text" : {
            "content" : "企微机器人测试，来自python"
        }
    }

    # 发送post请求
    response = requests.post(url= request_url, json = body, headers= header)

    # 打印结果
    print(response.json())


if __name__ == '__main__':
    main()

