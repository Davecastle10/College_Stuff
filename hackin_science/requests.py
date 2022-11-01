import requests

x = requests.get("https://requests.readthedocs.io/")
print(x.text)


#make sure request is imported properly.