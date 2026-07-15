def sum_of_multiples(limit, multiples):
    set_of_multi = set()
    for base in multiples:
        if base != 0:
            set_of_multi.update( multi for multi in range(base,limit,base))
    return sum(set_of_multi)
