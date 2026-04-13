# unit_testing_sim.py

"""
Definition: Unit testing is a software testing method by which individual units of source code 
are tested to determine whether they are fit for use. Python's 'unittest' is the built-in framework.
"""

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

print("Running simulated unit tests...")
# In a real scenario, we'd run unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestMathOperations)
result = unittest.TextTestRunner(verbosity=0).run(suite)
print(f"Tests run: {result.testsRun}, Errors: {len(result.errors)}, Failures: {len(result.failures)}")
