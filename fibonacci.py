n=int(input('nereye kadar?'))

sıra=[0,1]
for i in range(0,n):
    an = sıra[i] + sıra[i + 1]
    sıra.append(an)



print(sıra)