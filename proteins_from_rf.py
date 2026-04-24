"""
['A', 'P', 'C', 'P', 'M', 'H', 'G', 'L', 'T', 'L', 'T', 'S', 'G']
['R', 'L', 'A', 'P', 'C', 'M', 'G', '_', 'H', '_', 'H', 'L', 'V']
['A', 'L', 'P', 'H', 'A', 'W', 'V', 'N', 'I', 'D', 'I', 'W']
['H', 'Q', 'M', 'S', 'M', 'L', 'T', 'H', 'A', 'W', 'G', 'K', 'A']
['T', 'R', 'C', 'Q', 'C', '_', 'P', 'M', 'H', 'G', 'A', 'R', 'R']
['P', 'D', 'V', 'N', 'V', 'N', 'P', 'C', 'M', 'G', 'Q', 'G']
"""

current_prot = []
proteins = []
aa_seq = ['R', 'L', 'A', 'P', 'C', 'M', 'G', '_', 'H', '_', 'H', 'L', 'V']
for aa in aa_seq:
    if aa == "_":
        # STOP accumulating amino acids if _ - STOP was found
        if current_prot:
            for p in current_prot:
                proteins.append(p)
            current_prot = []
    else:
        # START accumulating amino acids if M - START was found
        if aa == "M":
            current_prot.append("")
        for i in range(len(current_prot)):
            current_prot[i] += aa
print(f'Current Protein: {current_prot}')
print(f'Proteins from amino acid sequence: {proteins}')
