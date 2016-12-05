import json

jsonString='{"arrayOfNUms":[{"number":0},{"number":1},{"number",2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'

print(jsonString)
jsonObj=json.loads(jsonString)


print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+jsonObj.get("arrayOfFruit")[2].get("number"))

print(jsonObj.get("arrayOfFruits")[2].get("fruit"))
