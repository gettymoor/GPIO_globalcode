import requests
url = ("https://maker.ifttt.com/trigger/HTU/with/key/dL7PYUwGme-j962hF7m4nO")
r = requests.get(url)


c = r.status_code
print(c)

