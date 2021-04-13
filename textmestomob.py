import requests

url = "https://www.fast2sms.com/dev/bulk"

message = input("Enter a Message : ")

contactno = input("Enter Contact No :")

payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno

headers = {
        'authorization': "sg1ZCzUX2UVi3SfVaYoKODx3SZEOxZcL2nwzLFJWvXoMIv7Lqeua0x7GYlYw",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)