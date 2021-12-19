import psutil

def network_interface():
    addresses = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    available_networks = []
    for intface, addr_list in addresses.items():
        if any(getattr(addr, 'address').startswith("169.254") for addr in addr_list):
            continue
        elif intface in stats and getattr(stats[intface], "isup"):
            available_networks.append(intface)
    choice = available_networks[1]
    # print(len(available_networks))
    return choice

if __name__ == '__main__':
    network_interface()