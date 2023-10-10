def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms_msg = []
    room = 1
    for name in names:
        rooms_msg.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return rooms_msg

def printer(names):
    for name in batch_badge_creator(names):
        print (name)
    for room in assign_rooms(names):
        print (room)
