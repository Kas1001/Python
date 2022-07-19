""" Demonstrate raiding a refrigerator"""

from contextlib import closing

class Refrigerator:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take_food(self, food):
        print(f"Finding {food}...")
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("Close fridge door.")

def raid(food):
    with closing(Refrigerator()) as r:
        r.open()
        r.take_food(food)

raid('bacon')
raid('deep fried pizza')