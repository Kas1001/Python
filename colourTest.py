def colour(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print(kwargs)

k = {'red':21, 'green':68, 'blue':120, 'alpha':52, 'beta':75}
print(colour(**k))