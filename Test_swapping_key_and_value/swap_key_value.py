class swapping_key_and_value :
    def swap_dict_keys_values(d):
        return {v: k for k, v in d.items()}
#d = {'a': 1, 'b': 2, 'c': 3}
#swapped_d = swap_dict_keys_values(d)
#print(swapped_d)
# Résultat: {1: 'a', 2: 'b', 3: 'c'}
