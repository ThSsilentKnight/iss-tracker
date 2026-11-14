import requests as req
import urllib.parse as parse
import json
import httpx

print("Script running. . . ")

url = "https://api.wheretheiss.at/v1/satellites/25544"

response = httpx.get(url)

data = response.json()

lon = round(data["longitude"], 2)
lat = round(data["latitude"], 2)
name = (data["name"]).upper()

print(f" {name} is at latitude {lat} --- longitude {lon}")

input("Press Enter to Exit")

