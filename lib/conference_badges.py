def badge_maker(name):
    message = f"Hello, my name is {name}."
    return message

def batch_badge_creator(names):
    msgs = [f"Hello, my name is {name}." for name in names]
    return msgs
    #or def batch_badge_creator(names):
    # msgs = []
    # for name in names:
    #     msgs.append("Hello, my name is {}.".format(name))
    # return msgs

def assign_rooms(names):
    counter = 1
    assign = []
    while counter < 9:
        for name in names:
            guest = f"Hello, {name}! You'll be assigned to room {counter}!"
            assign.append(guest)  
            counter +=1
    return assign   
    
    

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)

