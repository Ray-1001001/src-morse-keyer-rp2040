# "Morse.py" file is a function to xmit a Morse character on the
# Raspberry Pi Pico H. Converts text to dits and dahs. You can
# add characters, see line 46 onward.
# RK 08/28/23
import machine
import utime
led = machine.Pin(25, machine.Pin.OUT)  # Blink the on board LED on Pico.
key = machine.Pin(15, machine.Pin.OUT)  # Pin15 is Pico pin20, is keyline.
sidetone = machine.PWM(machine.Pin(14)) # generate tone for spkr Pico pin 19.
rfout = machine.PWM(machine.Pin(10))    # RF output on Pico pin 14.
rfout.freq(7020000)                     # Sets RF freq. Machine.freq dependant.

class MORSE_FUNC:                       # This is the name of the function.

    def Send_cw (ch, delay, tone):      # tone sets pitch of sidetone. tone and delay
        sidetone.freq(tone)             # are passed from CW_mac__io_func cw_mode.   
                
        # dot produces a Morse dot one delay unit long
        def dot (delay):
            sidetone.duty_u16(30000)    # Start generating sidetone ~50% duty cycle.
            rfout.duty_u16(33000)       # Start RF output.
            led.value(1)                # lights LED.
            key.value(1)                    # Key line high, 3.3V.
            utime.sleep_ms(delay)
            led.value(0)                # LED off
            key.value(0)                # Key line grounded.
            sidetone.duty_u16(0)        # 0 duty cycle stops the side tone.
            rfout.duty_u16(0)           # Stop RF output.
            utime.sleep_ms(delay)
            
        # dash produces a Morse dash 3 delay units long    
        def dash (delay):
            sidetone.duty_u16(30000)
            rfout.duty_u16(33000)
            led.value(1)
            key.value(1)
            utime.sleep_ms(delay * 3)
            led.value(0)
            key.value(0)
            sidetone.duty_u16(0)
            rfout.duty_u16(0)
            utime.sleep_ms(delay)
            
        def eoc():     # Time between letters, normally same as dash.
            utime.sleep_ms(delay * 3)
        #  Morse code translation follows:          
        if (ch == 'A'):
           dot (delay); dash(delay)
           eoc()       # eoc puts pause between chars
        elif (ch == 'B'):
            dash(delay); dot(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == 'C'):
            dash(delay); dot(delay); dash(delay); dot(delay)
            eoc()
        elif (ch == 'D'):
            dash(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == 'E'):
            dot(delay);
            eoc()
        elif (ch == 'F'):
            dot(delay); dot(delay); dash(delay); dot(delay)
            eoc()
        elif (ch == 'G'):
            dash(delay); dash(delay); dot(delay);
            eoc()
        elif (ch == 'H'):
            dot(delay); dot(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == 'I'):
            dot(delay); dot(delay)
            eoc()
        elif (ch == 'J'):
            dot(delay); dash(delay); dash(delay); dash(delay) 
            eoc()
        elif (ch == 'K'):
            dash(delay); dot(delay); dash(delay)
            eoc()
        elif (ch == 'L'):
            dot(delay); dash(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == 'M'):
            dash(delay); dash(delay)
            eoc()
        elif (ch == 'N'):
            dash(delay); dot(delay)
            eoc()
        elif (ch == 'O'):
            dash(delay); dash(delay); dash(delay)
            eoc()
        elif (ch == 'P'):
            dot(delay); dash(delay); dash(delay); dot(delay)
            eoc()
        elif (ch == 'Q'):
            dash(delay); dash(delay); dot(delay); dash(delay) 
            eoc()
        elif (ch == 'R'):
            dot(delay); dash(delay); dot(delay)
            eoc()
        elif (ch == 'S'):
            dot(delay); dot(delay); dot(delay)
            eoc()  
        elif (ch == 'T'):
            dash(delay);
            eoc()
        elif (ch == 'U'):
            dot(delay); dot(delay); dash(delay)
            eoc()
        elif (ch == 'V'):
            dot(delay); dot(delay); dot(delay); dash(delay)
            eoc()
        elif (ch == 'W'):
            dot(delay); dash(delay); dash(delay)
            eoc()
        elif (ch == 'X'):
            dash(delay); dot(delay); dot(delay); dash(delay)
            eoc()
        elif (ch == 'Y'):
            dash(delay); dot(delay); dash(delay); dash(delay)
            eoc()
        elif (ch == 'Z'):
            dash(delay); dash(delay); dot(delay); dot(delay)
            eoc()

        elif (ch == '1'):
            dot(delay); dash(delay); dash(delay); dash(delay); dash(delay); 
            eoc()
        elif (ch == '2'):
            dot(delay); dot(delay); dash(delay); dash(delay); dash(delay); 
            eoc()
        elif (ch == '3'):
            dot(delay); dot(delay); dot(delay); dash(delay); dash(delay); 
            eoc()
        elif (ch == '4'):
            dot(delay); dot(delay); dot(delay); dot(delay); dash(delay)
            eoc()
        elif (ch == '5'):
            dot(delay); dot(delay); dot(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == '6'):
            dash(delay); dot(delay); dot(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == '7'):
            dash(delay); dash(delay); dot(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == '8'):
            dash(delay); dash(delay); dash(delay); dot(delay); dot(delay)
            eoc()
        elif (ch == '9'):
            dash(delay); dash(delay); dash(delay); dash(delay); dot(delay)
            eoc()
        elif (ch == '0'):
            dash(delay); dash(delay); dash(delay); dash(delay); dash(delay); 
            eoc()
        elif (ch == ','):
            dash(delay); dash(delay); dot(delay); dot(delay);dash(delay);dash(delay)
            eoc()
        elif (ch == '/'):
            dash(delay); dot(delay); dot(delay); dash(delay); dot(delay)
            eoc()   
        elif (ch == '.'):
            dot(delay); dash(delay); dot(delay); dash(delay); dot(delay); dash(delay);  
            eoc()
        elif (ch == '?'):
            dot(delay); dot(delay); dash(delay); dash(delay); dot(delay); dot(delay)
        elif (ch == ' '):
            eoc(); eoc() 
        return()

