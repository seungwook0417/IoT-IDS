from scapy.all import Ether, ARP, srp, sniff, conf
from db import *
import time
import os
import sqlite3

n_range = "192.168.181.0/24"
Connection_Time = time.strftime("%Y/%m/%d/ %I:%M:%S")
iface = "ens33"
DATABASE = "./database.db"
conn = sqlite3.connect(DATABASE)

def reset():
    os.system('clear')

def frame():
    print('-' * 131)
    print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|'.format('IP Address', 'MAC Address', 'Device Name', 'Status',
                                                        'Connection Time'))
    print('-' * 131)


def detection(iprange="%s" % n_range):
    p = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=iprange)
    capture, nore = srp(p, iface=iface, timeout=2)
    connected_devices = len(capture)
    cur = conn.cursor()
    sql = "UPDATE attack SET devies = ? where id = 1"
    creds = (str(connected_devices))
    cur.execute(sql, creds)
    conn.commit()
    frame()
    for s, packet in capture:
        device.append([packet[ARP].psrc, packet[ARP].hwsrc])
    device.sort()
    for i in device:
        print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|'.format(i[0], i[1], '-', '-', '-'))
        print('-' * 131)


def get_mac(ip):
    p = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc

def ARP_detection(ip, mac, status):
    print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|'.format(ip, mac, '-', status, Connection_Time))
    cur = conn.cursor()
    sql = "SELECT * FROM device WHERE MAC = ?"
    creds = [str(mac)]
    check = cur.execute(sql, creds).fetchall()
    if check == []:
        sql = "INSERT INTO device(IP,MAC,Device,Status,currenttime) VALUES(?,?,?,?,?)"
        creds = [ip, mac, "-", status, Connection_Time]
    else:
        sql = "UPDATE device SET IP = ?, MAC = ?, Device = ?, Status = ?, currenttime = ?  where MAC = ?"
        creds = [ip, mac, "-", status, Connection_Time, mac]
    cur = conn.cursor()
    cur.execute(sql, creds)
    conn.commit()

def process(packet):
    if packet.haslayer(ARP):
        if packet[ARP].op == 2:
            try:
                # real MAC address of the sender
                target_ip = packet[ARP].psrc
                target_mac = get_mac(packet[ARP].psrc)
                attacker_mac = packet[ARP].hwsrc
                if target_mac != attacker_mac:
                    reset()
                    frame()
                    for i in device:
                        if i[1] == attacker_mac:
                            ARP_detection(i[0], i[1],"Attcker")
                        elif i[1] == target_mac:
                            ARP_detection(i[0], i[1],"Target")
                        else:
                            print('|{:^25}|{:^25}|{:^25}|{:^25}|{:^25}|'.format(i[0], i[1], '-', '-', '-'))
                        print('-' * 131)
            except IndexError:
                pass

if __name__ == "__main__":
    device = []
    initDB(DATABASE)
    detection()
    sniff(store=True, prn=process, iface=iface)
