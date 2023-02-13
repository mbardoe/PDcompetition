from random import random

from strategy import Strategy
from tournament import Tournament, RandomTournament


# def strategy1(num_rounds, player1_history, player2_history):
#     if num_rounds == 1:
#         return "C"
#     else:
#         return player2_history[-1]
# titfortat = Strategy("Tit4Tat", strategy1)



if __name__ == "__main__":
    def strategy1(num_rounds, player1_history, player2_history):
        if num_rounds==1:
            return "C"
        else:
            return player2_history[-1]

    table1=Strategy("Table1", strategy1)

    def strategy2(num_rounds, player1_history, player2_history):
        return "D"



    table2=Strategy("Table2", strategy2)

    def strategy3(num_rounds, player1_history, player2_history):
        return "D"

    table3=Strategy("Table3", strategy3)

    def strategy4(num_rounds, player1_history, player2_history):
        if num_rounds==1:
            return "C"
        elif num_rounds%4==0:
            return "D"
        else:
            return player2_history[-1]


    table4=Strategy("Table4", strategy4)

    tournament=RandomTournament([table1, table2, table3, table4], .9)
    #tournament = RandomTournament([Strategy.jerk(), Strategy.jerk(), Strategy.jerk(), Strategy.random(), Strategy.random(), Strategy.niceguy(), Strategy.niceguy(),
    #                         Strategy.titfortat(), Strategy.titfortat(), Strategy.titfortat(), Strategy.titfortat()], .8)

    tournament.play_tournament()
    tournament.report_scores()










