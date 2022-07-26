import itertools

sizes = ['small', 'medium', 'large']
colours = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']
def combine(quantity, size, colour, animal):
    return '{} x {} {} {}'.format(quantity, size, colour, animal)

print(list(map(combine, itertools.count(), sizes, colours, animals)))