from src.bayescoin import BayesCoin
from pytest import approx


def test_class_works():
    bc = BayesCoin()
    assert isinstance(bc, BayesCoin)
    assert sum(bc.data.values()) == 1


def test_choose_coin():
    bc = BayesCoin()
    bc.choose_coin()
    assert bc.coin in [0.30, 0.45, 0.75]


def test_flip_coin():
    bc = BayesCoin()
    bc.choose_coin()
    flip = bc.flip_coin()
    assert flip in [0, 1]


def test_update_priors():
    bc = BayesCoin()
    bc.coin = 0.30
    # bc.update_priors(1)
    # assert bc.data[0.3] == approx(0.2, abs=1e-3)
    # assert bc.data[0.45] == approx(0.3, abs=1e-3)
    # assert bc.data[0.75] == approx(0.5, abs=1e-3)
    bc.update_priors(0)
    assert bc.data[0.3] == approx(0.466666, abs=1e-1)
    assert bc.data[0.45] == approx(0.366666, abs=1e-1)
    assert bc.data[0.75] == approx(0.166666, abs=1e-1)
