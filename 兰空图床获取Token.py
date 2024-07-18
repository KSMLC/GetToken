import requests


def generate_token(url, email, password):
    url = url + "/api/v1/tokens"
    headers = {"Accept": "application/json"}
    data = {
        "email": email,
        "password": password
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        if response_json["status"]:
            token = response_json["data"]["token"]
            return token
        else:
            print("Failed to generate token. Message:", response_json["message"])
    else:
        print("Failed to generate token. Status code:", response.status_code)

    return None


print("注意：URL链接结尾不能有/")
url = input("请输入URL (例如：https://img.ksmlc.cn): ")
email = input("请输入登录图床的邮箱: ")
password = input("请输入登录图床的密码: ")

token = generate_token(url, email, password)
if token:
    auth_token = "Bearer " + token
    print("Auth Token:", auth_token)
    print("Auth Token:后边的都是")
