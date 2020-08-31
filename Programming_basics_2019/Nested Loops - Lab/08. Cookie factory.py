batches_count = int(input())
for batch in range(1, batches_count + 1):
    has_flour = False
    has_eggs = False
    has_sugar = False
    has_all = False
    while True:
        product = input()
        if product == 'sugar':
            has_sugar = True
        elif product == 'flour':
            has_flour = True
        elif product == 'eggs':
            has_eggs = True

        has_all = has_flour and has_eggs and has_sugar
        if product == 'Bake!':
            if not has_all:
                print('The batter should contain flour, eggs and sugar!')
            else:
                print(f'Baking batch number {batch}...')
                break
