import pyautogui
import keyboard
import time

lista_ip = [
    "192.168.1.97",
    "255.255.255.224",
    "192.168.1.126",
    "2001:DB8:ACAD:A::FF/64",
    "FE80::1",
    "192.168.1.98",
    "255.255.255.224",
    "192.168.1.126",
    "2001:DB8:ACAD:A::15/64",
    "FE80::1",
    "192.168.1.145",
    "255.255.255.240",
    "192.168.1.158",
    "2001:DB8:ACAD:B::FF/64",
    "FE80::1",
    "192.168.1.146",
    "255.255.255.240",
    "192.168.1.158",
    "2001:DB8:ACAD:B::15/64",
    "FE80::1"
    ]

terminale_1 = [
    "en",
    "conf terminal",
    "hostname Building-1",
    "enable secret class12345",
    "service password-encryption",
    "banner motd $This is Router$",
    "security passwords min-length 10",
    "login block-for 120 attempts 2 within 30",
    "no ip domain-lookup",
    "ip domain-name ITExamAnswers.net",
    "crypto key generate rsa",
    "1024",
    "line console 0",
    "password cisco12345",
    "login",
    "logging synchronous",
    "exec-timeout 60",
    "exit",
    "line vty 0 4",
    "password cisco12345",
    "transport input ssh",
    "login local",
    "logging synchronous",
    "exec-timeout 60",
    "exit",
    "line aux 0",
    "password cisco12345",
    "login",
    "logging synchronous",
    "exec-timeout 60",
    "exit",
    "ip ssh version 2",
    "ip ssh time-out 120",
    "username netadmin privilege 15 secret Cisco_CCNA7",
    "interface g0/0",
    "ip address 192.168.1.126 255.255.255.224",
    "description First Floor LAN",
    "ipv6 address 2001:DB8:ACAD:A::1/64",
    "ipv6 address fe80::1 link-local",
    "no shutdown",
    "exit",
    "interface g0/1",
    "ip address 192.168.1.158 255.255.255.240",
    "description Second Floor LAN",
    "ipv6 address 2001:DB8:ACAD:B::1/64",
    "ipv6 address fe80::1 link-local",
    "no shutdown",
    "exit",
    "ipv6 unicast-routing",
    "exit",
    "write",
    ]

terminale_2 = [
    "enable",
    "conf terminal",
    "enable secret class12345",
    "service password-encryption",
    "banner motd $Second Floor Switch$",
    "no ip domain-lookup",
    "line console 0",
    "password cisco12345",
    "login",
    "logging synchronous",
    "exec-timeout 60",
    "exit",
    "line vty 0 15",
    "password cisco12345",
    "login",
    "logging synchronous",
    "exec-timeout 60",
    "exit",
    "interface vlan 1",
    "ip address 192.168.1.157 255.255.255.240",
    "no shutdown",
    "ip default-gateway 192.168.1.158",
    "exit",
    "write",    
    ]

def operazione_1():
    for word in lista_ip:
        x = True
        while x:
            if keyboard.read_key() == "0":
                x = False
            else:
                pass

        pyautogui.press("backspace")
        pyautogui.typewrite(word)

def operazione_2():
    for word in terminale_1:
        x = True
        while x:
            if keyboard.read_key() == "0":
                x = False
            else:
                pass

        pyautogui.press("backspace")
        pyautogui.typewrite(word)
        
def operazione_3():
    for word in terminale_2:
        x = True
        while x:
            if keyboard.read_key() == "0":
                x = False
            else:
                pass

        pyautogui.press("backspace")
        pyautogui.typewrite(word)

def main():
    while True:
        if keyboard.read_key() == '1':
            # print("PRESSED 1")
            operazione_1()
        else:
            pass

        if keyboard.read_key() == '2':
            # print("PRESSED 2")
            operazione_2()
        else:
            pass

        if keyboard.read_key() == '3':
            # print("PRESSED 3")
            operazione_3()
        else:
            pass
    

if __name__ == "__main__":
    main()
