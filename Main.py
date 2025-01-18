from Item import Item
from Hub import Hub
from datetime import date
#Насоздавали экземпляров от Item
catfish = Item('Catfish', 'Regular catfish', 12, date(2024, 10, 13), 'sea', 'fish', 'large')
clownfish = Item('Clownfish', 'Regular clownfish', 7, date(2024, 12, 13), 'sea', 'fish', 'small')
aerosmith_album = Item('Aerosmith - Aerosmith. 1973', 'Glam-Rock classic', 50, date(2025, 1, 1), 'music', 'album',
                       'Columbia', 'Glam-Rock')
prosthesis = Item('Left hand prosthesis', 'Left hand prosthesis with a silver color', 1, date.today(), 'hand')
#Hub наш
hub = Hub(date(2025, 1, 1), catfish, clownfish, aerosmith_album, prosthesis)
#задачки
A = [item for item in hub if item.name[0].lower() == 'a']
Outdated = [item for item in hub if item.dispatch_time < hub.hub_date]
MostValuable = hub.find_most_valuable(3)
Others = [item for item in hub if item not in (A + MostValuable + Outdated)]
print(A, Outdated, MostValuable, Others, sep='\n')
#полигон json-ов
item = Item("Fish", "Fresh fish", 5, date(2025, 1, 12), "sea", "fish")
item.save_as_json("item.json")
from_json_item = Item.create_from_json("item.json")
print(from_json_item)
#Шото не так UPD: ВСЁ ТАК!
hub.save_as_json('hub.json')
from_json_hub = Hub.read_from_json('hub.json')
print(from_json_hub)