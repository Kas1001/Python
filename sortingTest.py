scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin', 'Niels Bohr', 'Dian Fossey', 'Isaac Newton', 'Grace Hopper', 'Charles Darwin', 'Lise Meitner']

print(sorted(scientists, key=lambda name: name.split()[-1]))