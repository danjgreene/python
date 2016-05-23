def jungle_animal(animal, my_speed):
    cheetah_speed = 115
    if animal == 'zebra':
        print "Try to ride a zebra!"
    elif animal == 'cheetah':
        if my_speed > cheetah_speed:
            print "Run!"
        else: 
            print "Stay calm and wait!"
    else:
        print "Introduce yourself!"