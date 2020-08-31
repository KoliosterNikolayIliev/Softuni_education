countries = [x for x in input().split(", ")]
capitals = [x for x in input().split(", ")]
print('\n'.join([f"{k} -> {v}" for k, v in {countries[i]: capitals[i] for i in range(len(countries))}.items()]))
