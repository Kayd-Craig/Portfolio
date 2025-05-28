import unittest
from uvsim import UVSim  # Import the UVSim class from uvsim.py

class TestUVSimBranching(unittest.TestCase):
    def setUp(self):
        self.sim = UVSim()
        self.sim.memory = [0] * 100
        self.sim.accumulator = 0
        self.sim.program_counter = 0

    def test_branch_success(self):
        self.sim.branch(50)
        self.assertEqual(self.sim.program_counter, 50)

    def test_branch_if_zero_success(self):
        self.sim.accumulator = 0
        self.sim.branch_if_zero(20)
        self.assertEqual(self.sim.program_counter, 20)

    def test_branch_if_zero_fail(self):
        self.sim.accumulator = 1
        self.sim.branch_if_zero(20)
        self.assertNotEqual(self.sim.program_counter, 20)

    def test_branch_if_negative_success(self):
        self.sim.accumulator = -10
        self.sim.branch_if_negative(30)
        self.assertEqual(self.sim.program_counter, 30)

    def test_branch_if_negative_fail(self):
        self.sim.accumulator = 10
        self.sim.branch_if_negative(30)
        self.assertNotEqual(self.sim.program_counter, 30)

    def test_branch_if_positive_success(self):
        self.sim.accumulator = 10
        self.sim.branch_if_positive(40)
        self.assertEqual(self.sim.program_counter, 40)

    def test_branch_if_positive_fail(self):
        self.sim.accumulator = -10
        self.sim.branch_if_positive(40)
        self.assertNotEqual(self.sim.program_counter, 40)

if __name__ == '__main__':
    unittest.main()
