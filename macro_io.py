# CW_mac_io_func.py       RK 09-01-23
# Functions to read and write 'disk' files to eeprom and take user input for macros.

import Morse                # Morse module converts text to CW dits and dahs.
import sys                  # Part if Micropython OS.
mo = Morse.MORSE_FUNC       # Sets up the mo. prefix to call funcs from Morse module.

class CW_TERMINAL:          # This is the name, or 'wrapper' of the function.

    #============================= Prints out a list of macros ========================
    def printmaclist(maclst):
        #l = len(maclst)
        for n in range (10):
            macro = (str(maclst[n]))
            if macro != "":                # Skip empty macros
                print('macro #', end = (''))
                print(n, macro)            # prints macro number and macro string
        print ('WPM =',maclst[10])      
        return()
    #===================================================================================
    
    #========= This function reads a list from a the 'disk' file on the Pico. ==========
    def readisk ():    
        file = open("macros.txt","r")      # Open file macros.txt for read
        readstr = file.read()              # and read it (is a string) into RAM
        file.close()
        maclistNew =  readstr.split('\n')  # Converts string into list. '\n' separates the lines
        return maclistNew
    #===================================================================================
    
    #===================================================================================
    def macroinput(maclist):     # Function to write and store macros for the CW program.
        
        while (True): 
            print('enter macro number to edit, 0 - 9, * to exit')
            macnum = (sys.stdin.read(1))
            macnum = macnum[0]       # Only read the first character typed
            #if str(macnum) == "":   # Trap null string if user just hits 'enter'
                    #macnum = " "    # Need a char here so 'enter' doesn't exit.
            if  (((macnum < '0') or  (macnum > '9')) and (macnum !='*')):       
                print('Try again, must be number 0 - 9')
            if ((macnum >= '0') and  (macnum <= '9')):      # A valid macro number was entered so exit this while loop.
                break
            if (macnum =='*'):       # Exit the macro input routine. 
                break                
        if  (macnum == '*'):         # Exit the function and
            return (maclist)         # return maclist.
       
        if (macnum != '*'):          # If all is OK and user has not bailed out store the macro.
            print('\nType text for macro',macnum)    
            mactxtin = (sys.stdin.readline())
            mactxtin = mactxtin.rstrip()       # Remove any characters at end of macro string.
            print('Macro ', macnum, 'is: ', end=("")); print(mactxtin)
            maclist[int (macnum)] = mactxtin   # Store the macro string to the list.
            CW_TERMINAL.writedisk(maclist)     # Store the list to Pico eeprom.
            return (maclist)                   # Return the new list to calling program.
    
    #=====================================================================================
        
    #================ This function writes a list to a disk file. ========================
    def writedisk (maclist):
        file = open("macros.txt","w")           # open a file to write mac data to. 
        l=len (maclist)                         # Number of items in list
        for n in range(l):                      # Increment thru items
            file.write (str(maclist[n] + "\n")) # Must include a linefeed or all data runs together
        file.close()                            # Close file when finished writing.
        return maclist
    #=====================================================================================
    def checkforfile():  # This must be called before macroinput() function is called because
                         # trying to open non-exsistant file generates an error.
        try:                                    # From "Micropython-docs" page 54
            file = open("macros.txt","r")       # Test for absent macro file on disk.
        except OSError:                         # if the exception is an "OSError"
            print('File not found, blank macro file created.\n')
            emptylist = ['','','','','','','','','','','12','']  # Declare a 12 item list
                                                # and store default 12 WPM in position 10.
            file = open("macros.txt","w")       # Opens a new macros.txt file on disk.
            l = len (emptylist)
            for n in range(l):                  # Can't write list to disk, only a string
                file.write (str(emptylist[n] + "\n"))
            file.close()
        return()
    #=====================================================================================
    def cw_mode(delay, tone):             # Function to send CW, called from main by typing 'C'.

        maclist = CW_TERMINAL.readisk()       
        print("Type characters to send:\n")
        while(True):                      #  This is the CW loop.   
            char = sys.stdin.read(1)      # Reads one char without pressing 'enter'
            if char == "\n":              # If 'Enter' key pressed senf LF to terminal.
                print("\n")               # Just a line feed
            mo.Send_cw (char.upper(), delay,tone) # Sends the character, WPM, and sidetone freq.            
            if char == '`':               # ` key starts macro TX mode.
                macnum = ""               # Make sure macnum is null.
                macnum = sys.stdin.read(1)  
                while (True):             # Macro selection loop
                    if macnum == "W" or macnum == "w":    # Set code speed                      
                        speed = (sys.stdin.read(2))
                        dig1 = ord(speed[0]); dig2 = ord(speed[1]) # ord returns the decimal value of character.
                        if ( dig1 >=48 and dig1<=57 and dig2 >=48 and dig2<=57): # testing for valid integer 0-9.
                            maclist[10] = (speed)
                            speed = int(speed)            # speed is string from keyboard, must convert to integer.
                            delay = int(1200/speed)
                            #maclist[10] = str(speed)
                            print('WPM set to', speed)
                        else:
                            print('Invalid input: Enter code speed between 05 to 50 WPM.')                      
                        macnum = ">"            # Flag signal to exit back to CW mode.
                        break
                    if macnum == "L" or macnum == "l":    # Lists stored macros
                        print("\n")             # A line feed so L doesn't mess up macro list
                        CW_TERMINAL.printmaclist(maclist)
                        macnum = ">"            # Flag signal to exit back to CW mode.
                        break
                    if len(macnum) > 1:
                        macnum = sys.stdin.read(1)   # too many chars entered, try again.
                    if str (macnum) < "0" or str(macnum) > "9":
                        macnum = sys.stdin.read(1)   # Out of range, try again.
                        macnum = ">"            # Flag signal to exit back to CW mode.
                        break
                    if str(macnum) >= "0" and str(macnum) <= "9":
                        break                   # Got a valid maco number so send it.
                if macnum == ">":               # If macros listed return to CW mode, not menu
                    txt = " "
                    continue                    # Back to  while(True) CW mode loop                    
                macnum = int(macnum)
                print("\n",maclist[macnum], end = "")
                txt = maclist[macnum]
            
                n = len(txt)                            # Get the number of chars typed in                
                for ch_pos in range(0, n):              # and send them one at a time to
                    mo.Send_cw (txt[ch_pos].upper(), delay,tone)
                print("\n")
    
    #====================================================================================
          


       
