from random import random

from strategy import Strategy
from tournament import Tournament


# def strategy1(num_rounds, player1_history, player2_history):
#     if num_rounds == 1:
#         return "C"
#     else:
#         return player2_history[-1]
# titfortat = Strategy("Tit4Tat", strategy1)



if __name__ == "__main__":
    #tournament = Tournament([Strategy.jerk(), Strategy.jerk(), Strategy.jerk(), Strategy.random(), Strategy.random(), Strategy.niceguy(), Strategy.niceguy(),
    #                         Strategy.titfortat(), Strategy.titfortat(), Strategy.titfortat(), Strategy.titfortat()], 50)
    
    tournament.play_tournament()
    tournament.report_scores()
