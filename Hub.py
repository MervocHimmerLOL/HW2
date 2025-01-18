from datetime import date
from textwrap import indent
import json
from Item import Item


class Hub:
    _items: list
    _date: date
    _hub = None

    def __new__(cls, *args, **kwargs):
        print('Creating hub')
        if cls._hub == None:
            cls._hub = super().__new__(cls)
        else:
            print('There is already Hub existing')
        return cls._hub

    def __init__(self, hub_date=date.today(), *items):
        self._date = hub_date
        self._items = list(items)

    def __str__(self):
        result = ', '.join(item._name for item in self._items)
        return f"This is HUB, it contains following Items: {result}"

    def __repr__(self):
        result = ', '.join(item._name for item in self._items)
        return result

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    @property
    def hub_date(self):
        return self._date

    @hub_date.setter
    def date(self, hub_date=date.today()):
        self._date = hub_date

    def add_item(self, *items):
        for item in items:
            if isinstance(item, Item):
                self._items.append(item)
            else:
                raise TypeError("You can only add an Item instance!")

    def find_by_id(self, id):
        for item in self._items:
            if item._id == id:
                return self._items.index(item), item
        return -1, None

    def find_by_tags(self, *tags):
        result = list()
        for item in self._items:
            if item.is_tagged(*tags):
                result.append(item)
        return result

    def find_by_date(self, *args):
        if len(args) == 1:
            date_to = args[0]
            return [item for item in self._items if item.dispatch_time <= date_to]
        if len(args) == 2:
            date_to = args[1]
            date_from = args[0]
            return [item for item in self._items if date_from <= item.dispatch_time <= date_to]
        else:
            raise ValueError('Too much args!!!')

    def rm_item(self, i):
        if isinstance(i, int):
            for item in self._items:
                if item._id == i:
                    self._items.remove(item)
        if isinstance(i, Item):
            self._items.remove(i)

    def drop_items(self, *items):
        for item in items:
            self.rm_item(item)

    def clear_items(self):
        self._items = []

    def find_most_valuable(self, amount=1):
        if amount > len(self._items):
            amount = len(self._items)
        return sorted(self._items, key=lambda item: item.cost, reverse=True)[:amount]

    def save_as_json(self, json_path):
        """Сохранить Hub в JSON файл"""
        data = {
            "creation_date": self._date.isoformat(),
            "items": [
                {
                    'name': item._name,
                    'description': item._description,
                    'cost': item._cost,
                    'dis_time': item._dispatch_time.isoformat(),
                    'tags': item._tags
                }
                for item in self._items
            ]
        }
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_from_json(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            creation_date = date.fromisoformat(data["creation_date"])
            items = [
                Item(
                    item_data["name"],
                    item_data["description"],
                    item_data["cost"],
                    date.fromisoformat(item_data["dis_time"]),
                    *item_data["tags"]
                )
                for item_data in data["items"]
            ]
            return Hub(creation_date, *items)
