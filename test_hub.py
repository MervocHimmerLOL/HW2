import unittest
from Hub import Hub
from datetime import date
from Item import Item
import unittest


class TestHub(unittest.TestCase):

    def setUp(self):
        self.item1 = Item("fish", 'The talking fish', 5, date(2025, 1, 15), 'sea', 'sexy', 'fish-ish')
        self.item2 = Item("fish_", 'The talking fish_', 7, date(2025, 1, 10), 'sea', 'sexy', 'fish-ish')
        self.hub1 = Hub(date.today())
        self.hub2 = Hub(date.today())
        self.hub1.add_item(self.item1)
        self.hub1.add_item(self.item2)

    def test_hub_singleton(self):
        'Проверка того что hub - синглтон'  # небольшая документация к тесту
        self.assertIs(self.hub1, self.hub2)

    def test_len(self):
        'Проверка того что при добавлении предметов меняется значение len(item)'
        h = Hub(date.today())
        for i in range(5):
            h.add_item(Item(f'item{i}', f'desc{i}', f'time{date.today()}',
                            i)),  # ваш конструктор может отличаться, передайте нужные параметры
        self.assertEqual(len(h), 5)

    def test_getitem(self):
        'Проверка того, что мы можем взять объект Item в Hub'
        self.assertEqual(self.hub1[0], self.item1)

    def test_find_by_id(self):
        self.assertEqual(self.hub1.find_by_id(self.item1._id), (self.hub1._items.index(self.item1), self.item1))

    def test_find_by_tags_(self):
        self.assertEqual(self.hub1.find_by_tags(['sexy', 'sea']), [self.item1, self.item2])

    def test_rm_item_by_id(self):
        self.hub1.rm_item(self.item1._id)
        self.assertEqual(self.hub1._items, [self.item2])

    def test_find_by_date(self):
        self.assertEqual(self.hub1.find_by_date(date(2025, 1, 10)), [self.item2])
        self.assertEqual(self.hub1.find_by_date(date(2025, 1, 10), date.today()), self.hub1._items)

    def test_rm_item_by_item(self):
        self.hub1.rm_item(self.item2)
        self.assertEqual(self.hub1._items, [self.item1])

    def test_drop_items(self):
        self.hub1.drop_items(self.item1, self.item2)
        self.assertEqual(self.hub1._items, [])

    def test_clear_items(self):
        self.hub1.clear_items()
        self.assertEqual(self.hub1._items, [])

    def test_find_most_valuable(self):
        self.assertEqual(self.hub1.find_most_valuable(), [self.item2])
        self.assertEqual(self.hub1.find_most_valuable(2), [self.item2, self.item1])
        self.assertEqual(self.hub1.find_most_valuable(1000), [self.item2, self.item1])
