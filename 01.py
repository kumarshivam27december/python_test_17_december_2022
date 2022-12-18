k=['ten','twenty','thirty']
v=[10,20,30]



k.insert(1,v[0])
k.insert(3,v[1])
k.insert(5,v[2])
print(k)




def cnvrt(k):
    res_dct={k[i]: k[i+1] for i in range(0,len(k),2)}
    return res_dct
print(cnvrt(k))



