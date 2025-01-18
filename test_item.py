import unittest
from Item import Item
from datetime import date
import random


def rand_item():
    item_names = ['Banana', 'Apple', 'Pineapple', 'Door', 'Airplane', 'Ruler of everything', 'Skull']
    item_tags = ['Tag', 'Taggifull', 'Watery', 'sea', 'fire', 'explosive', 'what', 'zero']
    while True:
        yield Item(
            item_names[random.randint(0, len(item_names)-1)],
            'this is test product',
            random.randrange(101),
            date(2025, random.randint(1, 12), random.randint(1, 28)),
            item_tags[random.randint(0, len(item_tags)-1)])

class TestItem(unittest.TestCase):


    def setUp(self):
        item_gen = rand_item()
        self.item101 = Item('', '', 1, date.today(), 't', 'e', 's')
        self.item1 = next(item_gen)
        self.item2 = next(item_gen)

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
        'Проверка на теги'
        self.assertTrue(self.item101.is_tagged('t'))
        self.assertTrue(self.item101.is_tagged(['t', 'e', 's']))

    def test_copy(self):
        "Проверка копирования самого себя"
        self.item3 = self.item1.copy()
        self.assertEqual(
            [self.item3._name, self.item3._description, self.item3._cost, self.item3._dispatch_time, self.item3._tags],
            [self.item1._name, self.item1._description, self.item1._cost, self.item1._dispatch_time, self.item1._tags])
        self.assertNotEqual(self.item3._id, self.item1._id)

    def test_items_list(self):
        "Проверка работоспособности Item._items"
        self.assertEqual(self.item1._id, Item._items.index(self.item1))
        self.assertEqual(self.item2._id, Item._items.index(self.item2))
        self.assertEqual(self.item101._id, Item._items.index(self.item101))