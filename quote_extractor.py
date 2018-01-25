import json

orig_json_data = open("original_data.json").read()

orig_data = json.loads(orig_json_data)

t = type(orig_data["quizData"])
q = orig_data["quizData"]
qkeys = q.keys()

for k in qkeys:
	print(k)

#print(p)