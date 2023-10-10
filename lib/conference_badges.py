def badge_maker(name):
    msg = f"Hello, my name is {name}."
    return msg

def batch_badge_creator(names):
    batch_msg = []
    for name in names:
        msg = f"Hello, my name is {name}."
        batch_msg.append(msg)
    return batch_msg

def assign_rooms(names):
    rooms_msg = []
    room = 1
    def assign_room(room, name):
        room_msg = f"Hello, {name}! You'll be assigned to room {room}!"
        return room_msg
    for name in names:
        rooms_msg.append(assign_room(room, name))
        room += 1
    return rooms_msg

def printer(names):
    
    def my_print(list):
        for item in list:
            print(item)
    
    print_list = []
    print_list = batch_badge_creator(names)
    my_print(print_list)
    
    print_list = assign_rooms(names)
    my_print(print_list)
    
    return None
