n=int(input('nereye kadar?'))

sequence=[0,1]
for i in range(0,n):
    an = sequence[i] + sequence[i + 1]
    sequence.append(an)
print(sequence)