with open('nameslist.txt', 'r') as f:
    def name_counter(f):
        name = f.readline().strip()
        names = {'Darth': 0, 'Luke': 0, 'Lea': 0}
        while name:
            if name == 'Darth':
                names['Darth'] += 1
            elif name == 'Luke':
                names['Luke'] += 1
            elif name == 'Lea':
                names['Lea'] += 1
            name = f.readline().strip()
        print(names.values())

    name_counter(f)