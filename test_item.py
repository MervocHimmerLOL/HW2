import unittest
from Item import Item
from datetime import date


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item('', '', 1, date.today(), 't', 'e', 's')
        self.item2 = Item('', '', 1, date.today())

    def test_item_id(self):
        'Проверка того что у разных Items разные id'
        self.assertNotEqual(self.item1._id, self.item2._id)

    def test_len(self):
        'Проверка того что при добавлении тэгов меняется значение len(item)'
        y = Item('Name', 'Description', date.today(), 1)
        for i in range(5):
            y.add_tag([f'tag{i}'])
        self.assertEqual(len(y), 5)

    def test_equal_tags(self):
        'Проверка того что если к предмету добавить два идентичных тега - их колчество будет один'
        i = Item('Name', 'description', date.today(), 1)
        i.add_tag(*['t', 'tag', 't'])
        self.assertEqual(len(i), 2)

    def test_is_tagged(self):
        self.assertTrue(self.item1.is_tagged('t'))
        self.assertTrue(self.item1.is_tagged(['t', 'e', 's']))

    def test_copy(self):
        self.item3 = self.item1.copy()
        self.assertEqual(
            [self.item3._name, self.item3._description, self.item3._cost, self.item3._dispatch_time, self.item3._tags],
            [self.item1._name, self.item1._description, self.item1._cost, self.item1._dispatch_time, self.item1._tags])
        self.assertNotEqual(self.item3._id, self.item1._id)
