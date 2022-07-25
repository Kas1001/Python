from re import M
import time

def make_timer():
    last_called = None # Never
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed

t = make_timer()
print(t())
print(t())