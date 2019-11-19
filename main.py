# /usr/bin/python3
# Author == Shawn Dooley
# Save 10 minutes every 2 weeks with this autofiller 
import pyautogui as pg
import time

def main():
    if input('Hover over the first LATSNET cell and enter <Y> on the python interpreter to continue:\n' ) == 'Y':
        time.sleep(2)
        pg.click()
        for x in range(2):
            weekday()
        for x in range(2):
            weekend()
        for x in range(5):
            weekday()
        for x in range(2):
            weekend()
        for x in range(3):
            weekday()
def weekday():
    pg_string = '9:00 AM\t12:30 PM\t1:00 PM\t5:00 PM{0}'.format('\t'*13)
    pg.typewrite(pg_string,0.02)


def weekend():
    pg_string = '{0}'.format('\t'*15)
    pg.typewrite(pg_string,0.02)

main()
