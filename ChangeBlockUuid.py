from ConnectionToolV2 import *

json1 = BPJSON()
json1.loadJSON('blueprint.json')

olduuid = "9f0f56e8-2c31-4d83-996c-d00a9b296c3f"  # Logic Gate
newuuid = input("New Uuid: ")
if newuuid == '':
    newuuid = "bc336a10-675a-4942-94ce-e83ecb4b501a"

for i in json1.jsonFile["bodies"][0]["childs"]:
    if i["shapeId"] == olduuid:
        i["shapeId"] = newuuid
        if i["controller"]["mode"] == 0:
            i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgA"
        elif i["controller"]["mode"] == 1:
            i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgB"
        elif i["controller"]["mode"] == 2:
            i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgC"
        elif i["controller"]["mode"] == 3:
            i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgD"
        elif i["controller"]["mode"] == 4:
            i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgE"
        elif i["controller"]["mode"] == 5:
            i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgF"
        i["controller"].pop("mode")

json1.saveJSON('blueprint.json')