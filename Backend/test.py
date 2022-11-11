import requests #  pip install requests

response = requests.get("http://127.0.0.1:4000/get_field_user")
print(response.content())