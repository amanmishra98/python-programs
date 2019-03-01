try:
    r = []
    f=open("f:\\Py programs\\file handling\\A.txt","r")
    print(f.name)
    for s in f :
        #s=f.readline()
        #a=eval(s)
        #print(type(a))
        #print(a)
        #l=list(a)
        #print(l)
        line = s.split(',')
        line[2:] = map(int,line[2:])
        r = sum(line[2:])/3
        line.append(result)
        line = list(map(str,line))
        new_str = line.join(',')
        r.append(new_str)
        print(join(r))
    f.close()
    fp = open('f:\\Py programs\\file hadling\\A.txt',"w")
    fp.write('\n'.join(r))
    fp.close()
    print("Operation sucessfull")
except:
        print("end of the line")
        

   
            
    
    
