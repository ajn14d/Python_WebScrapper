from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/black-thrustmaster-hotas-warthog-joystick/p/N82E16826280021?Item=N82E16826280021&Tpk=26-280-021"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)