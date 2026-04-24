
adn_reverse_complement = "AUCGCGUAACACAGCUGCAU"
print(f'DNA Reverse Complement: {adn_reverse_complement}')
len_adn_reverse_complement = len(adn_reverse_complement)
print(f'DNA Reverse Complement length: {len_adn_reverse_complement}')

nro_bases_c = adn_reverse_complement.count("C")
nro_bases_g = adn_reverse_complement.count("G")

gc_content = round((nro_bases_c + nro_bases_g) / len_adn_reverse_complement * 100)
print(f'GC Content: {gc_content}%')