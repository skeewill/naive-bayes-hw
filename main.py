from src.bayescoin import BayesCoin

bc = BayesCoin()
bc.choose_coin()

for i in range(100):
    flip = bc.flip_coin()
    bc.update_priors(flip)
