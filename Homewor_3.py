class Bulding:

    def __init__(self, buildingType, numberOfFloors):
        self.house = []
        self.house.append(buildingType)
        self.house.append(numberOfFloors)

    def __eq__(self, other):
        return self.house == other.house

House_1 = Bulding(123,321)
House_2 = Bulding(123,321)

if House_2 == House_1:
    print('отлично')