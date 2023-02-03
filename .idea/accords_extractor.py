import requests
import json

url = "https://waft.com/api/fragrances"

header = {
    "header": "Accords"
}

accords = []
for i in range(0, 497):
    params = {
        "term": "",
        "loadingIndex": i
    }
    response = requests.get(url, params=params).json()
    for fragrance in response["data"]:
        for accord in fragrance["accords"]:
            accord_obj = {
                "name": accord["name"],
            }
            if accord_obj in accords:
                continue
            else:
                accords.append(accord_obj)

header["accords"] = accords

print(json.dumps(header, indent=2))

with open("./accords.json", "w") as outfile:
    outfile.write(json.dumps(header, indent=2))