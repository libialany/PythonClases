DNA = "GCGCCUUGCCCCAUGCAUGGGUUAACAUUGACAUCUGGUG"
complement = {
    "A": "U",
    "U": "A",
    "G": "C",
    "C": "G"
}
complement_seq = ""
for base in DNA:
    # print("before: ", base)
    # print("after: ", complement[base])
    # print("------")
    complement_seq += complement[base]
print(f' Complement: {complement_seq}')
reverse_complement = complement_seq[::-1]
print(f"Reverse Complement: {reverse_complement}")
