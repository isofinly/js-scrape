f1 = open('out.json', 'r', encoding="utf8").read()
f2 = open('new_in.json', 'r', encoding="utf8").read()
f3 = open('two-links.txt', 'r', encoding="utf8").read().splitlines()
f = open('temp.txt', 'w+', encoding="utf8")
for i in range(0,34):
    print(eval(f1)[i].get('qr'))
    print(eval(f1)[i].get('title'))
    f.write( '{' + '\n' +
                '"id"' + ':' + ' ' + str(i) + ',' + '\n' + 
                '"title"' + ':' + ' ' + '"' + str(eval(f1)[i].get('title')) + '"' + ',' + '\n' + 
                '"qr"' + ':' + ' ' + '"' + str(eval(f1)[i].get('qr')) + '"' + ',' + '\n' +
                 '"link"' + ':' + ' ' + '"' + eval(f1)[i].get('link') + '"' + '\n' + 
                '},' + '\n' 
                )
        # f1.write('"' + f3[i] + '"' + ' ' + ':' + ' ' + str(f2_list).replace("'", '"') + ',' + '\n')
        # print(f2_list)
    
for i in range(0,23):
        print(eval(f2)[i].get('name'))
        print(f3[i]+f'#{i}')
        print(f'qr_codes/people/qr{i}.png')
        f.write( '{' + '\n' +
                    '"id"' + ':' + ' ' + str(i+34) + ',' + '\n' + 
                    '"title"' + ':' + ' ' + '"' + str(eval(f2)[i].get('name')) + '"' + ',' + '\n' + 
                    '"qr"' + ':' + ' ' + '"' + f'qr_codes/people/qr{i}.png' + '"' + ',' + '\n' +
                    '"link"' + ':' + ' ' + '"' + str(f3[i]+f'#{i}') + '"' + '\n' + 
                    '},' + '\n' 
                )
f.close() 
f5 = open('temp.txt', 'r', encoding="utf8").read()
f6 = open(f'full_qr_out.json', 'a', encoding="utf8")

f6.write('[' + '\n' + f5[:-2] +  '\n' + ']')
f6.close()
# for i in range(len(f3)):