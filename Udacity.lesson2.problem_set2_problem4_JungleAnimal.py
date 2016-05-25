def jungle_animal(animal, my_speed):
    assert isinstance(animal, str)
    # assert isinstance(my_speed, int)
    cheetah_speed = 115
    if animal == 'zebra':
        return "Try to ride a zebra!"
    elif animal == 'cheetah':
        if my_speed > cheetah_speed:
            return "Run!"
        else: 
            return "Stay calm and wait!"
    else:
        return "Introduce yourself!"

#assert jungle_animal(55, 140) == 'Introduce yourself!'

try:
    5 / ''
except TypeError:
    print "Haha, nice try dividing by 0 buddy, let's try that again!"
