class ConvTemperature:
    count1 = 0
    @staticmethod
    def fromFarenToCels(number):
        res1 = (number - 32)*5/9
        print(res1)
        ConvTemperature.count1 += 1
    @staticmethod
    def fromCelsToFaren(number):
        res = number * 9/5 + 32
        print(res)
        ConvTemperature.count1 += 1
    @staticmethod
    def getCount():
        print("Количество -", ConvTemperature.count1)

ConvTemperature.fromFarenToCels(25)
ConvTemperature.fromCelsToFaren(25)
ConvTemperature.getCount()