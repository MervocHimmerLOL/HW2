from datetime import date
import json





class Item:
    _id: int
    _name: str
    _description: str
    _dispatch_time: date
    _tags: list
    _cost: int
    __global_id = 0

    def __init__(self, name, description, cost, dis_time=date.today(), *tags):
        self._id = Item.__global_id
        self._name = name
        self._description = description
        self._dispatch_time = dis_time
        self._cost = cost
        self._tags = list(tags)
        Item.__global_id += 1

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        if cost < 0:
            raise ValueError("The cost of an item can not be below zero!")
        self._cost = cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == self._name:
            raise ValueError("Names do not differ!")
        self._name = name

    @property
    def dispatch_time(self):
        return self._dispatch_time

    @dispatch_time.setter
    def dispatch_time(self, dis_time=date.today()):
        self._dispatch_time = dis_time

    def __str__(self):
        return f"This is {self._name}, {self._description}, Dispatch time: {self._dispatch_time}, it costs:{self.cost} can be found with following tags: {', '.join(self._tags[:3])}"

    def __repr__(self):
        return f"{self._name + ': ' + ', '.join(self._tags[:3])}"

    def __len__(self):
        return len(self._tags)

    def __lt__(self, other):
        return self.cost < other.cost

    def add_tag(self, *tags):
        for tag in tags:
            if tag not in self._tags:
                self._tags.append(tag)

    def is_tagged(self, tags):
        if isinstance(tags, (list, tuple, set)):
            return all(tag in self._tags for tag in tags)
        return tags in self._tags

    def rm_tag(self, tags):
        for tag in tags:
            if tag in self._tags:
                self._tags.remove(tag)

    def copy(self):
        return Item(self._name, self._description, self._cost, self._dispatch_time, *self._tags)

    def save_as_json(self, json_path):
        data = {'name': self._name,
                'description': self._description,
                'cost': self._cost,
                'dis_time': self._dispatch_time.isoformat(),
                'tags': self._tags}
        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def create_from_json(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            dispatch_time = date.fromisoformat(data["dis_time"])
            return Item(data['name'], data['description'], data['cost'], dispatch_time, *data['tags'])