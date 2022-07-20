"""Read and print an integer series."""
import sys

def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]
    finally:
        f.close() # file will always be closed
    return series

series = read_series('recaman1.dat')
print(series)