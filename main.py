from random import randint, choice
import time, pickle

game_choice = 0
start_choice = 0
caught_item = 0

with open("caught_fishes.dat", "rb") as file:
    caught_fishes = pickle.load(file)
    list(caught_fishes)

fish_list = ["Судак", "Окунь", "Ерш", "Плотва","Лещ", "Густера", "Сазан", "Карп", "Карась", "Линь", "Голавль", "Язь"]


def random_fishing():
    caught_item = randint(1, 3)
    if caught_item == 1:
        catch = choice(fish_list)
        print("Вы поймали рыбу:", catch, sep='')
        caught_fishes.append(catch)
        with open("caught_fishes.dat", "wb") as file:
            pickle.dump(caught_fishes, file)
        if catch == "Язь":
            print("Вот она, рыба моей мечты ,вот ОНА, ВОТ ОНА! ЗДОРОВЕННЫЙ ЯЗЬ-ЯЯЯЯЯЯЯЯЯЯЗЗЗЗЗЬ, ЯЯЯЯЯЯЯЯЯЯЗЗЗЗЬ!")
        print("Рыбалка закончена")
        time.sleep(1)
        starting(start_choice)
    elif caught_item == 2:
        print("Вместо рыбы вы зацепили корягу. Лучше чем ничего.")
        print("Рыбалка закончена")
        time.sleep(1)
        starting(start_choice)
    elif caught_item == 3:
        print("С крючка сорвалась!")
        time.sleep(0.5)
        print("Рыбалка закончена")
        time.sleep(1)
        starting(start_choice)


   
def fishing_game(game_choice):
    print("Вы пошли рыбачить...", "\n")
    print("1-Закинуть крючок")
    print("2-Закончить рыбалку")
    while game_choice != 1 or 2:
        game_choice = input()
        if game_choice == '1':
            print("Вы закинули крючок в воду. Подождите 3-5 секунд")
            time.sleep(randint(3, 5))
            random_fishing()
        if game_choice == '2':
            starting(start_choice)
            
def inventory_info():
    print("Рыбы, которых вы смогли поймать:", "\n")
    print(', '.join(caught_fishes), "\n")
    starting(start_choice)

def starting(start_choice):
    print("Чем займëмся?", "\n")
    print("1-Начать рыбалку")
    print("2-Пойманные рыбы")
    while start_choice != 1 or 2:
        start_choice = input()
        if start_choice == '1':
            fishing_game(game_choice)
        elif start_choice == '2':
            inventory_info()
        else:
            start_choice = input()



#Начало программы
print("Доброго времени суток! :)", "\n")
starting(start_choice)
