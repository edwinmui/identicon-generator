import unittest
from app.utils.identicon_utils import IdenticonUtils


class TestIdenticonUtils(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.iu = IdenticonUtils()

    def test_generate_hash_same_names(self):
        name1 = "edwin"
        name2 = "edwin"

        hash1 = self.iu.generate_hash(name1)
        hash2 = self.iu.generate_hash(name2)

        self.assertEqual(hash1, hash2)

    def test_generate_hash_diff_names(self):
        name1 = "edwin"
        name2 = "edwinm"

        hash1 = self.iu.generate_hash(name1)
        hash2 = self.iu.generate_hash(name2)

        self.assertNotEqual(hash1, hash2)

    def test_get_random_color_same_hash(self):
        hash1 = "8e6e509fba12de7be9ff1cb5333a69d2"
        hash2 = "8e6e509fba12de7be9ff1cb5333a69d2"

        color1 = self.iu.get_random_color(hash1)
        color2 = self.iu.get_random_color(hash2)

        self.assertEqual(color1, color2)

    def test_get_random_color_diff_hash(self):
        hash1 = "8e6e509fba12de7be9ff1cb5333a69d2"
        hash2 = "58123e75957a916941de4ddb5252aa95"

        color1 = self.iu.get_random_color(hash1)
        color2 = self.iu.get_random_color(hash2)

        self.assertNotEqual(color1, color2)


if __name__ == "__main__":
    unittest.main()
