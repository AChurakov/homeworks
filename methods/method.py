

class Homework():
    def __init__(self):
        pass

    def get_methods(self,obj):
        for p in dir(obj):
            if not p.startswith('_'):
                print(p)
        return True


hw = Homework()

hw1 = hw.get_methods(1)
print(hw1)

