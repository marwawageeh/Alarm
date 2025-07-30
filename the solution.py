#installing  simpleaudio library This library helps in playing sounds
import simpleaudio as sa

#this library To deal with time
import datetime

# enter the disered time
time=input("Enter the alarm: ")

# play this alarm then enter the diserd time  It tells you that it agrees to alert you
filename = "C:/Users/MaKaNaK/Desktop/my app oopby python/sound/find.wav"
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing 


# Make current time always equal to the time in your city
while True:
    timo= datetime.datetime.now()

# Specify the hour, time and minutes
    now=timo.strftime("%H:%M:%S")

    #If the clock is now like the user wrote it, we will do the following
    if now==time:
        # play that alarm 
        
        filename = "C:/Users/MaKaNaK/Desktop/my app oopby python/sound/time of action.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing  # Wait until sound has finished playing
 
        #The computer's current time has exceeded the required time. Take a break
        if now > time: 
           break  
         


          



