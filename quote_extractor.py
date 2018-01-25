import json
import re

orig_json_data = open("original_data.json").read()
extracted_data_file = open("extracted_data.txt","w")

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


for i in quiz_data:
	champ = reduced_champ_list[i]
	champ_id_dict = quiz_data[i] # will get the quotes and triggers so {quotes: {...}, triggers:[...]
	quotes_dict = champ_id_dict['quotes'] # will get just the quotes dict so {champname.action: {...}}
	for q in quotes_dict: # q will be the champname.action
		actual_quote = quotes_dict[q]['text']
		champ_quotes[actual_quote] = champ

for x in champ_quotes:
	print(x + " - " + champ_quotes[x])
	cq = x + " - " + champ_quotes[x]

	# take out weird unicode characters and keep ascii only
	cq_clean = re.sub(r'[^\x00-\x7f]',r'',cq)

	# replacing new lines with tabs
	# Reasoning: in the actual motd, a random line number will be chosen and that will be printed out
	# So if there is quote that has new lines in it, then the rest of the quote will not be printed
	# If there are tabs, then a simple regex can be performed to replace tabs with new line right after
	# the line is selected
	cq_clean = re.sub(r'\n',r'\t',cq_clean)

	extracted_data_file.write(cq_clean)
	extracted_data_file.write("\n") # so a line number can be chosen properly

extracted_data_file.close()

