import json

path = 'blueprint.json'  # The blueprint files needs to be in the same folder as this script!

olduuid = "9f0f56e8-2c31-4d83-996c-d00a9b296c3f"  # Logic Gate
newuuid = "bc336a10-675a-4942-94ce-e83ecb4b501a"  # Quick Logic Gate

with open(path, 'r', encoding='utf8') as file:
    data = file.read()
    json1 = json.loads(data)

for j in range(len(json1["bodies"])):
    for i in json1["bodies"][j]["childs"]:
        if i["shapeId"] == olduuid:
            i["shapeId"] = newuuid
            if i["controller"]["mode"] == 0:
                i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgA"  # The Data for AND mode
            elif i["controller"]["mode"] == 1:
                i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgB"  # OR
            elif i["controller"]["mode"] == 2:
                i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgC"  # XOR
            elif i["controller"]["mode"] == 3:
                i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgD"  # NAND
            elif i["controller"]["mode"] == 4:
                i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgE"  # NOR
            elif i["controller"]["mode"] == 5:
                i["controller"]["data"] = "gExVQQAAAAEFBQDAAgAAAAIAbW9kZQgF"  # XNOR
            i["controller"].pop("mode")

with open(path, 'w') as file:
    file.write(json.dumps(json1, indent=2))