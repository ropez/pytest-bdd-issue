from pytest_bdd import scenario


@scenario('foo.feature', 'Some scenario')
def test_bar():
    pass
