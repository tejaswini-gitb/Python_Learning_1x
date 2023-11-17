
class GF:
    def car(self):
        return "old car"

class F:
    def car(self):
        return " mimi cooper"

class S(F):
    def car(self):
        return "2 mercedez"

#son= F()
son= S()
print(son.car())