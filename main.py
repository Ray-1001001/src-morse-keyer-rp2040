# This is the "main" program. It offers a menu choice for writing and editing
# up to 10 macros and CW keyboard operation.       RK. 08/17/23
# Macros are recalled with the ` key. `7 will send macro 7.
# The * key bails out of CW mode and returns to the menu.
# This code , main.py, macro_io.py, and morse.py is not copywrited.
# It is for the amatuer community to use and experiment with.

import macro_io                 # Functions tp read and store macros.
import Morse                    # Function converts text to dots and dashes.
import utime                    # Part of MicroPython operating system for time delays. 
import sys                      # MicroPython OS, required for sys.stdin.read().
import micropython              # Part of MicroPython OS.
import machine                  # Part of MicroPython OS. Required for keyboardInterrupt() functions.

mo = Morse.MORSE_FUNC       # Sets up the mo. prefix to call funcs from Morse.py.
cw = macro_io.CW_TERMINAL   # Sets up the cw. prefix to call funcs from macro_io.py.
# MORSE_FUNC and CW_TERMINAL are class names for Morse.py and macro_io.py files. 
machine.freq (140400000)    # CLock freq must be set to this to get 7020 KHz output freq.
rfout = machine.PWM(machine.Pin(10))    # machine.Pin 10 is pin 14 on Pico PCB.
rfout.freq(7020000)         # Set RF to 7020KHz. Must use 140400000 clock freq or freq error.
led = machine.Pin(25, machine.Pin.OUT)  # Blinks the on board LED on Pico
key = machine.Pin(15, machine.Pin.OUT)  # machine.Pin 15 is Pico pin 20, is the keyline.
sidetone = machine.PWM(machine.Pin(14)) # Generates sidetone for spkr Pico pin 19.
dummy = sys.stdin.read(1)   # Dummy input needed or else following not printed.
print('--------------------------------------------------------')
print('A simple Morse keyer for transmitting CW by AJ4YN. V4.10')
print('RF sidetone at 7020 KHZ. Po = 1.2mW')
print('--------------------------------------------------------')
cw.checkforfile()               # If no macros.txt file, create and load a blank macro list.
                                # to prevent error when calling cw.readisk() function.                                  
maclist = cw.readisk()          # Read in any macros that were stored in disk file.
speed = (maclist[10])           # Default code speed in WPM stored in line 11 of macros.txt
delay = int(1200/int(speed))    # speed is string so int(speed) converts it to integer.

tone = 1600                     # The sidetone frequency in Hz, change this to your preference.
#---------------------------------------------------------------------------------------------
goodread = False
while(True):                    # This is where the program runs. It's a continous loop.
    if goodread == False:       # Displays the menu line if False.
        print('(L)ist, (E)dit, (W)pm, (C)W mode\r')
    goodread = False
    choice = sys.stdin.read(1)            # Reads one char without pressing 'enter'
    if choice == 'L' or choice == 'l':    # List the macros
        goodread = True                   # and do not display the menu line again.
        print('\n')
        cw.printmaclist(maclist)          # Prints a list of macros stored in macro.txt file.
        
    if choice == 'E' or choice == 'e':    # This is for entering a macro.
        goodread = False        # Display menu line after returning from macro edit.
        print('\n')
        maclist = cw.macroinput(cw.readisk())   # readisk() is function to read user macro input.
   
    if choice == 'W' or choice == 'w':    # This sets the codde speed in WPM.
        goodread = True
        print('\nSpeed is', maclist[10], 'WPM. Enter new speed, 05 to 50 WPM.')
        speed = (sys.stdin.read(2))
        dig1 = ord(speed[0]); dig2 = ord(speed[1]) # ord returns the decimal value of character.
        if ( dig1 >=48 and dig1<=57 and dig2 >=48 and dig2<=57): # testing for valid integer
            maclist[10] = (speed)        # Store the new code speed in the list.
            speed = int(speed)           # It's a string so convert to int for math.
            delay = int(1200/speed)
            print('WPM set to', speed)
            cw.writedisk (maclist)       # Store the new WPM to the macros.txt file.                    
        else:                            # You screwed up and hit the wrong keys!
            print('Invalid input: Enter code speed between 05 to 50 WPM.')
            continue                     # Inform the user and continue in the speed choice loop.        
    
    if choice == 'C' or choice == 'c':
        goodread = True
        print ('\nIn CW keyboard mode, (*) to exit\n')
        micropython.kbd_intr(42)          # keyboard interrupt is set to the * key
        try:
            cw.cw_mode(delay,tone)
        except KeyboardInterrupt:         # Bail out if * entered
            key.value(0)
            led.value(0)
            sidetone.duty_u16(0)          # 0 duty cycle stops the side tone
            rfout.duty_u16(0)             # and the rf output.
            micropython.kbd_intr(3)       # Keyboard int enabled ***ERASE finish debugging. Restore above line***
            goodread = False
            print("\nYou have interrupted the transmission by typing an '*'.")
            x = input("Please press the ENTER key to continue...\n\n")            
            continue 



                                                   
