"""
Постановка задачи:

Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
"""


class House:
    def __init__(self, name, number_of_floors):
        self.number_of_floors = int(number_of_floors)
        self.name = name

    def go_to(self, new_floor):
        if int(new_floor) < 1 or int(new_floor) > self.number_of_floors:
            print("Такого этажа не существует")

        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
# print(h1.name)
h2.go_to(10)
# print(h2.name)
