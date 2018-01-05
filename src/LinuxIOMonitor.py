import psutil

def get_key():

    key_info = psutil.net_io_counters(pernic=True).keys()

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

    return key_info, recv, sent


def get_rate(func):

    import time

    key_info, old_recv, old_sent = func()

    time.sleep(1)

    key_info, now_recv, now_sent = func()

    net_in = {}
    net_out = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)

    return key_info, net_in, net_out


while 1:
    try:
         key_info, net_in, net_out = get_rate(get_key)

         for key in key_info:
             if key.__contains__("Ethernet") or key.__contains__("eth0"):
                print('%s: Input:\t %sKB/s, Output:\t %sKB/s' % (key, net_in.get(key), net_out.get(key)))
    except KeyboardInterrupt:
        exit()
