f1 = open('out2.txt', 'w', encoding="utf8")
f2 = open('pastvu-data.txt', 'r', encoding="utf8").read().splitlines()
f3 = open('links-order.txt', 'r', encoding="utf8").read().splitlines()
f4 = open('pastvu-links.txt', 'r', encoding="utf8").read().splitlines()
for i in range(len(f2)):
    f2_list = f2[i].split(",")
    f2_list.reverse()
    f1.write( '{' + '\n' +
             '"id"' + ':' + ' ' + str(i) + ',' + '\n' + 
             '"title"' + ':' + ' ' +'"' + str(f2_list[0]) + '"' + ',' + '\n' + 
             '"link"' + ':' + ' ' + '"' + f3[i] + '"' + ',' + '\n' + 
             '"image"' + ':' + ' ' + '"' +  f4[i] + '"' + ',' + '\n' + 
             '"list"' + ':' + ' ' + str(f2_list).replace("'", '"') + '\n'
             + '},' + '\n' 
             )
    # f1.write('"' + f3[i] + '"' + ' ' + ':' + ' ' + str(f2_list).replace("'", '"') + ',' + '\n')
    # print(f2_list)
f1.close()    

f5 = open('out2.txt', 'r', encoding="utf8").read()
f6 = open('out3.json', 'w', encoding="utf8")

f6.write('[' + '\n' + f5[:-2] +  '\n' + ']')
f6.close()
