import socket
from datetime import datetime
import time


def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def network_error():
    turned_off = False
    timer = 0
    while True:

        time.sleep(1)
        if is_connected() == False:
            current_date = datetime.now().strftime("%x") 
            time_turn_off = datetime.now().strftime("%X")
            turned_off = True
            timer += 1
            print(timer)
            print("INTERNET OFF")
        elif is_connected() == True and turned_off == True:
            turned_off = False
            print(str(current_date) + " The internet disconnected at " + str(time_turn_off) + " for " + str(timer) + " seconds!")
        else:
            print("INTERNET ON")


network_error()