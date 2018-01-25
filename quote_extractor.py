import json

orig_json_data = open("original_data.json").read()
#orig_json_data.replace('""','"')

orig_data = json.loads(orig_json_data)


# get rid of the icon information - what we need the is the id and name
# like this: {1:"Annie",2:"Aatrox"}
reduced_champ_list = {}
champ_quotes = {}

quiz_data = orig_data['quizData']
champ_list = orig_data['championList']

# add elements to reduced champ list
for champ in champ_list:
	i = champ['id']
	n = champ['name']
	reduced_champ_list[i] = n

# for c in reduced_champ_list:
# 	print("Champ data: " + c + " -> " + reduced_champ_list[c])

for i in quiz_data:
	champ = reduced_champ_list[i]
	champ_id_dict = quiz_data[i] # will get the quotes and triggers so {quotes: {...}, triggers:[...]
	quotes_dict = champ_id_dict['quotes'] # will get just the quotes dict so {champname.attack: {...}}
	quote_text = quotes_dict['text']
	print(quote_text)

print(champ_quotes)

