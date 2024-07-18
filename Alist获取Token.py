import requests

# 设置请求的URL和请求体参数
url = "https://你的alist域名/api/auth/login"  # 替换为实际的API URL
payload = {
    "username": "你的登录用户名",  # 替换为实际的用户名
    "password": "你的登录密码",  # 替换为实际的密码
    # 如果有二步验证码，可以添加
    # "otp_code": "your_otp_code"
}

# 发送POST请求
response = requests.post(url, json=payload)

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()
    if data['code'] == 200:
        token = data['data']['token']
        print("Token:", token)
    else:
        print("Error message:", data['message'])
else:
    print("Failed to retrieve token. Status code:", response.status_code)
