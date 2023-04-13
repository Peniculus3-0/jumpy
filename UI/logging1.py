import logging

#DEBUG: Detailed information, typically of interest only when diagnosing problems.

#INFO: Confirmation that things are working as expected.

#WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

#ERROR: Due to a more serious problem, the software has not been able to perform some function.

#CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(level=logging.DEBUG, filename='test.log',format='%(asctime)s:%(levelname)s:%(message)s')
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

add_result = add(12, 3)
logging.debug('Add: 7 + 3 = %d' % add_result)