import unittest
from PropertyDetails import PAOPropertyDetails

class TestPAExtraction(unittest.TestCase):
    
    def test_PAExtraction(self):
        result = PAOPropertyDetails('WALSH MICHAEL')
        self.assertEqual(result.PA_Owner_Name,'WALSH MICHAEL')

if __name__ == '__main__':
    unittest.main()