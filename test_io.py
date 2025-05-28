import unittest
from uvsim import UVSim  # Import the UVSim class from uvsim.py
import unittest.mock

class TestUVSimIO(unittest.TestCase):
    def setUp(self):
        self.sim = UVSim()
        self.sim.memory = [0] * 100

    def test_read_success(self):
        with unittest.mock.patch('builtins.input', return_value="1234"):
            self.sim.read(10)
            self.assertEqual(self.sim.memory[10], 1234)

    def test_write_success(self):
        self.sim.memory[10] = 5678
        with unittest.mock.patch('builtins.print') as mock_print:
            self.sim.write(10)
            mock_print.assert_called_with(5678)

if __name__ == '__main__':
    unittest.main()
