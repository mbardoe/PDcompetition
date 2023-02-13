from random import random


class Strategy(object):
    idCounter = 1

    def __init__(self, name: str, strategy):
        self.name = name
        self.score = 0
        self.my_strategy = strategy
        # self.my_strategy = lambda turn, my_history, opp_history: "C"

    @classmethod
    def titfortat(cls):
        def strategy1(num_rounds, player1_history, player2_history):
            if num_rounds == 1:
                return "C"
            else:
                return player2_history[-1]

        Strategy.idCounter += 1
        return cls(f"titfortat{Strategy.idCounter}", strategy1)

    @classmethod
    def jerk(cls):
        def strategy1(num_rounds, player1_history, player2_history):
            return "D"

        Strategy.idCounter += 1
        return cls(f"Jerk{Strategy.idCounter}", strategy1)

    @classmethod
    def niceguy(cls):
        def strategy1(num_rounds, player1_history, player2_history):
            return "C"

        Strategy.idCounter += 1
        return cls(f"NiceGuy{Strategy.idCounter}", strategy1)

    @classmethod
    def random(cls):
        def strategy1(num_rounds, player1_history, player2_history):
            if random() < .5:
                return "C"
            else:
                return "D"

        Strategy.idCounter += 1
        return cls(f"Random{Strategy.idCounter}", strategy1)

    def play(self, turn, my_history, opp_history):
        return self.my_strategy(turn, my_history, opp_history)

    def reset_score(self):
        self.score = 0

    def update_score(self, update):
        self.score += update

    def update_strategy(self, func):
        self.my_strategy = func
