import requests

czesc1 = "https://translate.google.pl/translate_tts?ie=UTF-8&q="
czesc2 = "&tl=pl&client=tw-ob&ttsspeed="
speed = "1.0"
text = input()
url = czesc1 + text + czesc2 + speed
url = url.replace(" ", "%20")
result = requests.get(url)
newFile = open("szybko.mp3", "wb")
newFile.write(result.content)