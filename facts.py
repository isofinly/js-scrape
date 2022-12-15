f = open('facts.txt', 'r', encoding="utf8").read().splitlines()
f1 = open('temp.txt', 'w', encoding="utf8")
for i in range(len(f)):
    f1.write( '{' + '\n' +
                '"id"' + ':' + ' ' + str(i) + ',' + '\n' + 
                '"fact"' + ':' + ' ' +'"' + str(f[i]) + '"' + '\n'  
                + '},' + '\n'
            )
    
f1.close()
f5 = open('temp.txt', 'r', encoding="utf8").read()
f6 = open(f'facts.json', 'a', encoding="utf8")

f6.write('[' + '\n' + f5[:-2] +  '\n' + ']')
f6.close()