import unittest
import Components
from Components.Processor import Processor 

class TestProcessor(unittest.TestCase):

    def test_processor(self):
        processor = Processor(3.5, 4)
        self.assertEqual(processor.freq, 3.5)
        self.assertEqual(processor.cores, 4)

if __name__ == '__main__':
    unittest.main()