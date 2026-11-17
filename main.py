import httpx

print("Script running. . . ")

url = "https://api.wheretheiss.at/v1/satellites/25544"

try: 
  response = httpx.get(url)
  print(response)
except:
    print(f"Error caught")

else:
    data = response.json()

    lon = round(data["longitude"], 2)
    lat = round(data["latitude"], 2)
    name = (data["name"]).upper()

    nominatim_url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}"

    req = httpx.get(nominatim_url)

    print(f" {name} is at latitude {lat} --- longitude {lon}")
    print(req)
finally:
    input("Press Enter to Exit Please. . .")