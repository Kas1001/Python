def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.encode('unicode-escape').decode('ascii')
    return wrap

class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()
@tracer
#def rotate_list(l):
#    return l[1:] + [l[0]]

#l = [1, 2, 3]
#l = rotate_list(l)
#print(l)

#l = rotate_list(l)
#print(l)

#l = rotate_list(l)
#print(l)

#tracer.enabled = False

#l = rotate_list(l)
#print(l)

#l = rotate_list(l)
#print(l)

#l = rotate_list(l)
#print(l)

@escape_unicode
def norwegian_island_maker(name):
    return name + 'øy'

print(norwegian_island_maker('Llama'))