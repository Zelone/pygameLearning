
import pygame 
pygame.mixer.init()
import time
import random
soundObj = pygame.mixer.Sound('ding.wav')
#soundObj.play().set_volume(0.6,0.5) # do in range 0.1 to 0.6 only
channelObj = pygame.mixer.Channel(1)
allis=  [(i,j) for i in range(60) for j in range(60)]
random.shuffle(allis)
print(allis)
channelObj.play(soundObj,loops=100)
volswitch = 1
for i,j in allis:
    i+=20
    j+=20
    print(i,j)
    if(volswitch%3==0):
        time.sleep(soundObj.get_length()/2)
        print("/2")
    else: 
        time.sleep(soundObj.get_length()/4)
        print("/4")
    volswitch+=1
    
    channelObj.set_volume(i/100,j/100) # do in range 0.1 to 0.6 only 
    #soundObj.queue()

 # wait and let the sound play for 1 second
print('trswg')
soundObj.play().set_volume(0.2,0.2)
time.sleep(soundObj.get_length()) # wait and let the sound play for 1 second
#soundObj.stop() 

pygame.mixer.quit()
