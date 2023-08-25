import requests

url = "https://the-weather-api.p.rapidapi.com/api/weather/campinas"

headers = {
	"X-RapidAPI-Key": "724e85b619msh43fd1e63ffc34c2p182bbejsn8fe4d03ef7fb",
	"X-RapidAPI-Host": "the-weather-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

def printInfo(info):
    print(info.get("city"))
    print(info.get("temp") + " graus")
    print(info.get("insight_description"))


printInfo(data.get("data"))

if int(data.get("data").get("temp")) <= 20:
    print("Se agasalhe pois irá fazer " + data.get("data").get("temp") + " graus")

elif int(data.get("data").get("temp")) >= 21 or int(data.get("data").get("temp")) <= 26:
    print("Hoje está um dia agradável")
    
else:
	print("Hoje o dia está quente, passe um protetor solar.")