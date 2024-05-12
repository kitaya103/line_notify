import requests

# 替換為您的 LINE Notify 權杖
token = "0hpbcAwcxJPESy0W0cQxiAk3aA3OGbE1vebUsSd4fN0"

# 替換為您要傳送的訊息
message = "Hello, world!"

# 發送 LINE Notify 訊息
url = "https://notify-api.line.me/api/notify"
headers = {"Authorization": f"Bearer {token}"}
data = {"message": message}
response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("訊息傳送成功！")
else:
    print("訊息傳送失敗！")
