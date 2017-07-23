class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    @staticmethod
    def walk():
        print("Waddle, waddle, waddle")

    @staticmethod
    def swim():
        print("Come on it, the water's lovely")

    @staticmethod
    def quack():
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    @staticmethod
    def walk():
        print("Waddle, waddle, I waddle too")

    @staticmethod
    def swim():
        print("Come on in, but it's a bit chilly this far South")

    @staticmethod
    def quack():
        print("Are you 'avin' a larf? I'm a penguin!")


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
