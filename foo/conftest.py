print "\n", __name__

def pytest_pyfunc_call(pyfuncitem):
    print 'hook!'
