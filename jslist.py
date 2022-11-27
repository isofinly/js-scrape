import json
f1 = open('images.txt', 'a', encoding="utf8")
# open_file = open('/Users/isofinly/VSC-Projects/site-repo/src/constants/adresses/birzha.json', 'r', encoding="utf8").readlines()
with open('/Users/isofinly/VSC-Projects/site-repo/src/constants/adresses/vyazma.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    for i in range(len(fcc_data)):
        print(fcc_data[i].get('image'))
        f1.write(str(fcc_data[i].get('image')) + '\n')
f1.close()        

# birzha.json
# chajkovskogo.json
# grivcova.json
# kronv.json
# vyazma.json