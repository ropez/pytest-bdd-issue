print "\n", __name__

def pytest_pyfunc_call(pyfuncitem):
    print 'pytest_pyfunc_call hook'

def pytest_generate_tests(metafunc):
    print 'pytest_generate_tests hook'
