import random as r


class BayesCoin:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.coins = [0.30, 0.45, 0.75]
        self.data = {coin: 1. / 3. for coin in self.coins}

    # ------------------------------------------------------------ #

    def choose_coin(self):
        self.coin = r.choice(self.coins)
    # ------------------------------------------------------------ #

    def flip_coin(self):
        return 1 if r.random() < self.coin else 0
    # ------------------------------------------------------------ #

    def update_priors(self, flip):
        print('before update:', self.data)
        denominator = list(map(lambda coin: (1 - coin if flip == 0 else coin) * self.data[coin], self.coins))
        self.data = {self.coins[i]: numerator / sum(denominator) for i,
                     numerator in enumerate(denominator)}
        self.debug(flip, denominator)

    # ------------------------------------------------------------ #

    def debug(self, flip, denominator):
        print('coin:', self.coin, 'flip:', flip)
        # print('denominator:', denominator)
        print('data:', self.data)
        # print('sum of priors:', sum(self.data.values()))
        # print('sum of denominator:', sum(denominator))
        print('-' * 100)
    # ------------------------------------------------------------ #
