# game.py

import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    def __check_dictionary(self, word):
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = r.json()
        return response['found']



def random_grid():
    from random import choice
    from string import ascii_uppercase
    return ''.join((choice(ascii_uppercase) for i in range(9)))


def is_valid(word, grid):
    grid_cp=str(grid)
    ok=True
    for i in range(len(word)):
        print(f"{i}  car = {word[i]}")
        if word[i] not in grid_cp:
            ok=False
        else:
            index=grid_cp.find(word[i])
            print(f"trouve a {index}")
            grid_cp=grid_cp.replace(word[i], "",1)
    return ok

#grid=random_grid()
#print(f"grid={grid}")

#word=input("votre mot :")
#print(f"result={is_valid(word, grid)}")

