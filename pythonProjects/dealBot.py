import json
with open("GetDeals.json") as json_file:
    json_data = json.load(json_file)
itemCodes = []

for item in json_data["dealDetails"]:
	itemCodes.append(item)


for i in range(len(itemCodes)):
	print json_data["dealDetails"][itemCodes[i]]["percentOff"]