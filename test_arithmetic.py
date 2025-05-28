import unittest
from uvsim import UVSim

class TestUVSimOperations(unittest.TestCase):
    def setUp(self):
      self.sim = UVSim()  # Assuming UVSim is the class containing these methods
      self.sim.memory = [0] * 100  # Initialize memory with 100 zeros
      self.sim.accumulator = 0
    
    def test_add_success(self):
      self.sim.memory[10] = 5
      self.sim.add(10)
      self.assertEqual(self.sim.accumulator, 5)
    
    def test_subtract_success(self):
      self.sim.memory[10] = 5
      self.sim.accumulator = 10
      self.sim.subtract(10)
      self.assertEqual(self.sim.accumulator, 5)
    
    def test_divide_by_zero(self):
      self.sim.memory[10] = 0
      with self.assertRaises(ZeroDivisionError):
          self.sim.divide(10)
    def test_multiply_success(self):
      self.sim.memory[10] = 5
      self.sim.accumulator = 2
      self.sim.multiply(10)
      self.assertEqual(self.sim.accumulator, 10)
    
    def test_add_overflow(self):
      self.sim.memory[10] = 9999  # Example large number
      self.sim.accumulator = 9999
      self.sim.add(10)
      self.assertTrue(self.sim.accumulator <= 9999)  # Assuming accumulator has a limit
      
    def test_subtract_underflow(self):
      self.sim.memory[10] = 9999  # Example large number
      self.sim.accumulator = -9999
      self.sim.subtract(10)
      self.assertTrue(self.sim.accumulator >= -9999)  # Assuming negative limit on accumulator
      
    def test_divide_success(self):
      self.sim.memory[10] = 5
      self.sim.accumulator = 20
      self.sim.divide(10)
      self.assertEqual(self.sim.accumulator, 4)
      
    def test_multiply_overflow(self):
      self.sim.memory[10] = 9999  # Example large number
      self.sim.accumulator = 9999
      self.sim.multiply(10)
      self.assertTrue(self.sim.accumulator <= 9999)  # Assuming accumulator has a limit

if __name__ == '__main__':
      unittest.main()
