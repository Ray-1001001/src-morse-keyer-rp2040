# src-morse-keyer-rp2040

This is a Morse keyer that will transmit CW on 7020Khz, produce an audio tone, and key a transceiver. It connects to a PC USB port and is controlled by a terminal program such as Terra Term.  There are 10 macros for message storage and the morse characters can be sent by typing from the keyboard.

Tera Term setup
Open Terra Term.and connect the programmed Pico to the USB port on the laptop with a USB to 
type B cable.
1--If you get
   ---------------------------------------
   Tera Term: Error window
   Cannot open COMx. Not found.
   ---------------------------------------
   go to 'Setup'  'Serial port...'
     Click on 'Port' and choose a COM port from the list.
     Click on 'New open'.  The setup window will close
     Go back to 'Setup'   'Terminal...'
     Click on 'Local echo' to enable it.
     Check 'New-line', Receive and Transmit must be set
     to CR.
   
2--To test for correct COM port choice, press 'enter',
   you should see:
   (L)ist,   (E)dit,   (W)pm,   (C)W mode
   
   If not, go back to step 1 and choose a new serial port.
   Click on 'Close and New open' and test for correct
   COM port by pressing 'enter'.


3--Save the Terra Term setup.
   Go to 'Setup'  'Save setup'
   Click on Save. This window opens.
   ---------------------------------------
   TERATERM.INI already exists.
   Do you want to replace it?
   ---------------------------------------
   Click on 'Yes'.
Operating the CW Keyer
The bold text indicates messages that appear in the terminal window. Figure 6 shows the text in 
terminal window. Two macros were created and the code speed set to 16 WPM. The macros were
then listed.
Press 'enter' and the menu will appear.
     (L)ist,   (E)dit,   (W)pm,   (C)W mode
Type L to list the macros stored in the Pico memory.  
Type E to edit any one of the ten macros numbered 0-9
that are stored in the Pico memory.  To edit macro #3 press
E3 'enter' and you will see:
   enter macro number to edit, 0 - 9, * to exit
   3     
Indicates you have chosen to write and store to macro 3.
   Type text for macro 3
Program is asking for the macro text. To store “AJ4YN Chesapeake, VA”  just type it without the
quotes and press 'enter'. The macro will be stored and you will be returned to the menu.
    (L)ist,   (E)dit,   (W)pm,   (C)W mode
Type 'L' to list the macros.  If no macros have been stored only the code speed in WPM will be 
shown. For the above example you will see:
   AJ4YN Chesapeake, VA
   WPM = xx
Type W to set the code speed in words/minute.  Typing
W15 then 'enter' will set the code speed to 15 WPM. Note that the code speed must have two 
digits. For 5 WPM you must type W05. W5 will result in an error.
Type C to enter the CW keyboard mode where you can type
a message and send it out in CW mode.  Start typing and
the keyer will begin transmitting CW right away. The on board LED will blink as the rig is 
keyed.
To return to the menu type *.  This will immediately stop


transmitting and display the following:
You have interrupted the transmission by typing an '*'.
Please press the ENTER key to continue...
Press 'enter' to return to the menu.
     (L)ist,   (E)dit,   (W)pm,   (C)W mode
While in the CW mode you can transmit a stored macro, list the stored macros, and change the 
code speed in WPM.
To transmit a macro type` followed by the macro number you want to send. The ` (back tick) key
is usually just to the left of the numeral 1 key. To send macro number three, type `3 and the 
message stored in macro 3 will be sent.
To see a list of your macros while in CW mode, type `L and the macro list will be displayed 
along with the code speed. To set the code speed type `W followed by a two digit speed between 
05 and 50 WPM.  To set the code speed to nine WPM type `W09.  Typing `W9 results in an 
error.
