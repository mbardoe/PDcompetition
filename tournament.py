from strategy import Strategy
class Tournament():

    def __init__(self, strategies: list[Strategy], num_rounds: int):
        self.strategies = strategies

        self.num_rounds = num_rounds
        self.scores = dict(zip(self.strategies, [0] * len(strategies)))

    @staticmethod
    def compute_payoffs(player1, player2):
        if player1 == "C" and player2 == "C":
            return 2, 2
        elif player1 == "C" and player2 == "D":
            return -1, 3
        elif player1 == "D" and player2 == "C":
            return 3, -1
        else:
            return 0, 0

    def play_tournament(self):
        keys = list(self.strategies)
        num_keys = len(keys)
        for i in range(num_keys):
            player1 = self.strategies[i]

            for j in range(i + 1, num_keys):
                player1_history = []
                player2 = self.strategies[j]
                player2_history = []
                for k in range(self.num_rounds):
                    player1_outcome = player1.play(k + 1, player1_history, player2_history)
                    player2_outcome = player2.play(k + 1, player2_history, player1_history)
                    player1_history.append(player1_outcome)
                    player2_history.append(player2_outcome)
                    outcome = self.compute_payoffs(player1_outcome, player2_outcome)
                    player1.update_score(outcome[0])
                    player2.update_score(outcome[1])

    def report_scores(self):
        for strategy in self.strategies:
            print(f"{strategy.name}: {strategy.score}")

if __name__=="__main__":
    print(Tournament.compute_payoffs("C", "C"))
    print(Tournament.compute_payoffs("D", "C"))
    print(Tournament.compute_payoffs("C", "D"))
    print(Tournament.compute_payoffs("D", "D"))
