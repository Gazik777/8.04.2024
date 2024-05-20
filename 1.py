class Fraction:
    count = 0
    def __init__(self, chislitel, znamenatel):
        self.chisl = chislitel
        self.znam = znamenatel
        Fraction.count += 1

    @staticmethod
    def getCount():
        print("Количество созданных обьектов -", Fraction.count)

FractionOne = Fraction(92, 81)
FractionTwo = Fraction(71, 50)

print("Ваша дробь -", FractionOne.chisl, "/", FractionOne.znam)
print("Ваша дробь -", FractionTwo.chisl, "/", FractionTwo.znam)
Fraction.getCount()