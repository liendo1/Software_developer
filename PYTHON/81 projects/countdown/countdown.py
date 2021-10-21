'''Countdown
Show a countdown timer using a seven segment display'''

import sys, time
import sevseg #import our sevseg program

#change this to any number of seconds:
secondsleft = 30

try:
    while True: #main program loop
        # clear the screen by printing several newlines
        print('\n' * 60)
        # get the hours/minutes/seconds from secondsleft:
        # For example : 7265  is 2 hours, 1 minute, 5 seconds
        hours = str(secondsleft // 3600)
        # and 7265 % 3600 is 65 and 65 // 60 is one minute
        minutes = str((secondsleft % 3600) // 60)
        # and 7265 % 60 is 5 seconds:
        seconds = str(secondsleft % 60)

        # get the digit string from the sevseg module
        hDigits = sevseg.getSevSegStr(hours,2)
        hTopRow, hMiddleRow,hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes,2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds,2)
        sTopRow, sMiddleRow,sBottomRow = sDigits.splitlines()

        #display the digits:
        print(hTopRow +    '   ' + mTopRow +    '   ' + sTopRow )
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if secondsleft == 0:
            print()
            print('   * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit')

        time.sleep(1) # Insert a one second pause.
        secondsleft -= 1
except KeyboardInterrupt:
    print('Countdown')
    sys.exit() # when Ctrl-C is pressed end the program