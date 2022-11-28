# adress = 'vyazma'
def aboba(adress):
    f = open('temp.txt', 'w', encoding="utf8")
    f1 = open(f'{adress}-pastvu-title.txt', 'r', encoding="utf8").read().splitlines()
    f2 = open(f'{adress}-pastvu-data.txt', 'r', encoding="utf8").read().splitlines()
    f3 = open(f'{adress}-links-order.txt', 'r', encoding="utf8").read().splitlines()
    f4 = open(f'{adress}-pastvu-links.txt', 'r', encoding="utf8").read().splitlines()
    for i in range(len(f2)):
        f2_list = f2[i].split(",")
        f2_list.reverse()
        f.write( '{' + '\n' +
                '"id"' + ':' + ' ' + str(i) + ',' + '\n' + 
                '"title"' + ':' + ' ' +'"' + str(f1[i]) + '"' + ',' + '\n' + 
                '"link"' + ':' + ' ' + '"' + f3[i] + '"' + ',' + '\n' + 
                '"image"' + ':' + ' ' + '"' +  f4[i] + '"' + ',' + '\n' + 
                '"list"' + ':' + ' ' + str(f2_list).replace("'", '"') + '\n'
                + '},' + '\n' 
                )
        # f1.write('"' + f3[i] + '"' + ' ' + ':' + ' ' + str(f2_list).replace("'", '"') + ',' + '\n')
        # print(f2_list)
    f.close()    

    f5 = open('temp.txt', 'r', encoding="utf8").read()
    f6 = open(f'out.json', 'a', encoding="utf8")

    f6.write('[' + '\n' + f5[:-2] +  '\n' + ']')
    f6.close()
aboba('one')
# aboba('kronv')
# aboba('grivcova')
# aboba('birzha')
# aboba('chajkovskogo')