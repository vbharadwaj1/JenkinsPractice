from src import calc


def test_add():
	assert calc.add(5,5) == 10
	

def test_mul():
	assert calc.mul(5,2) == 10
