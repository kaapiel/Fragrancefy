import json
import requests

url = "https://waft.com/api/fragrances"

header = {
    "header": "Essential Oil Combinations"
}

fragrances = []
for i in range(0, 497):
    params = {
        "term": "",
        "loadingIndex": i
    }
    response = requests.get(url, params=params).json()
    for fragrance in response["data"]:
        fragrance_obj = {
            "name": fragrance["name"],
            "male": fragrance["male"],
            "female": fragrance["female"],
            "image": fragrance["image"],
            "accords": []
        }
        for accord in fragrance["accords"]:
            accord_obj = {
                "name": accord["name"],
                "weight": accord["weight"],
                "oils": []
            }
            fragrance_obj["accords"].append(accord_obj)
        fragrances.append(fragrance_obj)

header["fragrances"] = fragrances

print(json.dumps(header, indent=2))

with open("./fragrances.json", "w") as outfile:
    outfile.write(json.dumps(header, indent=2))