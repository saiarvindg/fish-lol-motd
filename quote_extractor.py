import json

orig_json_data = open("original_data.json").read()

orig_data = json.loads(orig_json_data)

t = type(orig_data["quizData"])
p = orig_data["quizData"]
pkeys = p.keys()

for k in pkeys:
	print(k)

#print(p)