class Conv:
    count1 = 0
    @staticmethod
    def fromMetricToFurhlong(number):
        print("Перевод из метров в фурлонг")
        res1 = number / 201
        print(res1)
        Conv.count1 += 1

    @staticmethod
    def fromFurhlongToMetric(number):
        print("Перевод из фурлонг в метры")
        res1 = number * 201
        print(res1)
        Conv.count1 += 1

    @staticmethod
    def fromTogToKg(number):
        print("Перевод из тог в кг")
        res = number * 12.7
        print(res)
        Conv.count1 += 1

    @staticmethod
    def fromKgToTog(number):
        print("Перевод из кг в тог")
        res = number / 12.7
        print(res)
        Conv.count1 += 1

    @staticmethod
    def getCount():
        print("Количество -", Conv.count1)

Conv.fromMetricToFurhlong(25)
Conv.fromFurhlongToMetric(25)
Conv.fromKgToTog(25)
Conv.fromTogToKg(25)
Conv.getCount()

