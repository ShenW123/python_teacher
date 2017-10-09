"""
Unit Test a function in the problem sets. Requires the student to create a function that is testable.

With the Inputs being the 3 values, and the returned value being the result before printing.
"""


import unittest
import signal

from src import ps1a
from ps1a_fail_cases import test_should_error_obj
from ps1a_pass_cases import test_pass_obj

TIMEOUT_VALUE = 5

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

class TestSequense(unittest.TestCase):
    pass

def test_pass_generator(annual_salary, portion_saved, total_cost, answer):
    def test(self):
        signal.alarm(TIMEOUT_VALUE)
        result = ps1a.main(annual_salary, portion_saved, total_cost)
        self.assertEqual(answer, result)
    return test

def test_should_error_generator(annual_salary, portion_saved, total_cost, answer):
    def test(self):
        with self.assertRaises(Exception) as raised:
            signal.alarm(TIMEOUT_VALUE)
            result = ps1a.main(annual_salary, portion_saved, total_cost)
            self.assertEqual(answer, result)
        self.assertFalse(raised, TimeoutException)
    return test

if __name__ == '__main__':
    for key, value in test_pass_obj.items():        
        test_name = 'test_pass_%s' % key
        test = test_pass_generator(value["annual_salary"], value["portion_saved"], value["total_cost"], value["answer"])
        setattr(TestSequense, test_name, test)

    
    for key, value in test_should_error_obj.items():
        test_name = 'test_should_error_%s' % key
        test = test_should_error_generator(value["annual_salary"], value["portion_saved"], value["total_cost"], value["answer"])
        setattr(TestSequense, test_name, test)

    unittest.main()
