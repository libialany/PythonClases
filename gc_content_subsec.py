DNA_reverse_complement = "AUCGCGUAACACAGCUGCAU"
len_DNA_reverse_complement = len(DNA_reverse_complement)
print(f'DNA Reverse Complement: {DNA_reverse_complement}')
print(f'DNA Reverse Complement length: {len_DNA_reverse_complement}')
k=10
res = []

for i in range(0,len_DNA_reverse_complement - k + 1, k):
    subseq = DNA_reverse_complement[i:i + k]
    res.append(
        round((subseq.count('C') + subseq.count('G')) / len(subseq) * 100))
print(f'GC Content of subsequences of length {k}: {res}%')

