import psutil as ps
import time
from checknetwork import network_interface

net_interface = str(network_interface())
timer = 2


while True:
    time.sleep(timer)
    netio = ps.net_io_counters(pernic='True')
    net_usage = netio[net_interface].bytes_sent + netio[net_interface].bytes_recv
    conn = ps.net_connections()
    print(net_usage, 'bytes')
    total = 0
    for i, val in enumerate(conn):
        addr = val[3]
        status = val[5]
        print(addr)
        # print(status)
        total = i
    print("number of connections: ", str(total))
    print("--------------------------")
    print("--------------------------")
    print("--------------------------")
    print("--------------------------")
    break