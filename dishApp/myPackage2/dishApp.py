class Meal:
    def __init__(self,name,withMeat,ingridients):
        self.name = name
        self.withMeat = withMeat
        self.ingridients = ingridients

class Ingridient:
    def __init__(self,name,count):
        self.name = name
        self.count = count

ingridients = [Ingridient("pomidor", 0), Ingridient("ogorek",0) ,Ingridient("salata",0), Ingridient("oliwa",0), Ingridient("jajka",0), Ingridient("boczek",0)]

dish_Menu = [Meal("Salatka grecka",False, [ingridients[1],ingridients[2],ingridients[3],ingridients[0]]),
            Meal("Jajecznica z boczkiem", True, [ingridients[4],ingridients[5]])]


def showDishes():
    for x in dish_Menu:
        print(x.name)


def create_shopping_list(number_first,number_second):
    shop_list = []

    for x in dish_Menu[0].ingridients:
        for y in ingridients:
            if x == y:
                y.count = y.count + number_first

    for x in dish_Menu[1].ingridients:
        for y in ingridients:
            if x == y:
                y.count = y.count + number_second

    print("Potrzebne produkty:\n")
    for x in ingridients:
        print("Nazwa: " + x.name + " Ilość: " + str(x.count))








