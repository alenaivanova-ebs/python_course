# 1. В отеле есть 3 типа номеров: royal (2-3 комнаты), lux (1-2 комнаты), standard (1 комната).
# надо добавить метод для создания номеров и хранения их в виде словаря.

# 2. В комнате есть мебель для ванной, спальни и зала (если есть зал).
# нужно добавить метод для добавления и удаления из комнаты мебели в любом количестве.

# 3. Нужно создать один метод для изменения любого номера по заданным параметрам,
# в том числе удалению и изменению номеров и комнат.

class Room:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.__dict__[key] = val

    def add(self, furniture_type, count):
        if furniture_type in self.__dict__:
            self.__dict__[furniture_type] = self.__dict__[furniture_type] + count
        else:
            self.__dict__[furniture_type] = count

    def delete(self, furniture_type, count):
        self.__dict__[furniture_type] = self.__dict__[furniture_type] - count


class Bathroom(Room):
    def __str__(self):
        print('bathroom')
        print(self.__dict__)


class BedRoom(Room):
    def __str__(self):
        print('bedroom')
        print(self.__dict__)


class HotelRoom:
    def __init__(self, *args, room_type):
        self.room_type = room_type
        self.rooms = []
        for val in args:
            self.rooms.append(val)

    def add(self, room):
        self.rooms.append(room)

    def delete(self, room):
        self.rooms.remove(room)

    def add_or_delete(self, room, action):
        if action == 'add':
            self.rooms.append(room)
        else:
            self.rooms.remove(room)

    def update(self, new_room_type):
        self.room_type = new_room_type

    def __str__(self):
        print('Room type:' + self.room_type)
        for room in self.rooms:
            print(room.__str__())


# standart room
bathroom_st = Bathroom(chair=2, table=1)
bedroom_st = BedRoom(chair=1, table=1, bed=1)
bathroom_st.delete('chair',1)
hotel_room_st = HotelRoom(bathroom_st, bedroom_st, room_type='standart')
bathroom_st.__str__()

# lux room
bathroom_lux = Bathroom(chair=1, table=1)
bedroom_lux1 = BedRoom(chair=2, table=2, bed=1)
bedroom_lux2 = BedRoom(chair=2, table=2, bed=1)
hotel_room_lux = HotelRoom(bathroom_lux, bedroom_lux1, bedroom_lux2, room_type='lux')

# royal room
bathroom_royal = Bathroom(chair=1, table=1)
bedroom_royal1 = BedRoom(chair=2, table=2, bed=1)
bedroom_royal2 = BedRoom(chair=2, table=2, bed=1)
bedroom_royal3 = BedRoom(chair=2, table=2, bed=1)
hotel_room_royal = HotelRoom(bathroom_royal, bedroom_royal1, bedroom_royal2, bedroom_royal3, room_type='royal')
hotel_room_royal.add_or_delete(bathroom_royal, 'delete')
hotel = {}


def add_rooms(roomtype, room_count):
    if roomtype == 'royal':
        hotel_room = hotel_room_royal
    elif roomtype == 'lux':
        hotel_room = hotel_room_lux
    else:
        hotel_room = hotel_room_st
    list_of_rooms = []
    for i in range(1, room_count):
        list_of_rooms.append(hotel_room)

    hotel[roomtype] = list_of_rooms


# add rooms to the hotel
add_rooms('royal', 2)
add_rooms('lux', 3)
add_rooms('standart', 4)

# print rooms in the hotel
for key in hotel:
    print(f'Count of {key} hotel rooms: {len(hotel[key])}')
