import unittest
from MyHashTable import MyHashTable

class MyHashTableTests(unittest.TestCase):
    def test_when_keyValue_is_added_then_containsKey_return_true(self):
        sut = MyHashTable()
        sut.Add("myKey","myvalue")
        self.assertTrue(sut.ContainsKey("myKey"))

    def test_when_keyValue_is_not_added_then_containsKey_raise_KeyError(self):
        sut = MyHashTable()
        with self.assertRaises(KeyError):
            sut.ContainsKey("myKey")

    def test_when_keyValue_is_added_then_get_return_value(self):
        sut = MyHashTable()
        sut.Add("myKey","myvalue")
        self.assertEqual(sut.Get("myKey"), "myvalue")

    def test_when_key_added_is_None_then_get_return_value(self):
        sut = MyHashTable()
        sut.Add(None,"myvalue")
        self.assertEqual(sut.Get(None), "myvalue")
    
    def test_when_key_collision_occurs_then_get_return_expected_values(self):
        sut = MyHashTable(1)
        sut.Add("my1stKey","aValue")
        sut.Add("my2ndKey","anotherValue")
        self.assertEqual(sut.Get("my1stKey"), "aValue")
        self.assertEqual(sut.Get("my2ndKey"), "anotherValue")

if __name__ == '__main__':
    unittest.main()