import pyautogui
import keyboard
import time

# PC-A configuration so it is the configuration of the ROUTER
# 192.168.10.0 R1 is default array
conf_pcA = [
    'enable', 
    'configure terminal ', 
    'no ip domain-lookup', 
    'hostname R1', # to change ID 3
    'banner motd #Unauthorized access to this device is prohibited!#',
        
    'interface g0/0/0', 
    'description Connect to Subnet B', 
    'ip address 192.168.10.129 255.255.255.192', # to change ID 7
    'no shutdown', 
    'exit',
            
    'interface g0/0/1', 
    'description Connect to Subnet A', 
    'ip address 192.168.10.1 255.255.255.128', # to change ID 12
    'no shutdown ', 
    'exit', 

    'enable secret NoOneShouldKnow', 
    'service password-encryption', 
    'security passwords min-length 10',

    'ip domain-name netsec.com', 
    'username netadmin secret Ci$co12345',

    'line console 0', 
    'password C@nsPassw!', 
    'login', 
    'exit',
            
    'line vty 0 15', 
    'transport input ssh', 
    'login local', 
    'exit', 
            
    'crypto key generate rsa', 
    '1024', 
    'exit', 
    'copy running-config startup-config', 
    ]

# PC-B configuration so it is the configuration of the SWITCH
conf_pcB = [
    'enable', 
    'configure terminal ', 
    'no ip domain-lookup', 
    'hostname S1', # to change ID 3
    'banner motd #Unauthorized access to this device is prohibited!#', 
    
    'interface vlan 1', 
    'description Switch Subnet A', 
    'ip address 192.168.10.2 255.255.255.128', # to change ID 7
    'no shutdown ', 
    'exit', 
    
    'ip default-gateway 192.168.10.1', # to change ID 10

    'enable secret NoOneShouldKnow', 
    'service password-encryption',
    
    'ip domain-name netsec.com', 
    'username netadmin secret Ci$co12345', 
    
    'line console 0', 
    'password C@nsPassw!', 
    'login', 
    'exit', 
    
    'line vty 0 15', 
    'transport input ssh', 
    'login local', 
    'exit', 
    
    'crypto key generate rsa', 
    '1024', 

    'int range f0/1 - 4, f0/7 - 24, g0/1 - 2', 
    'description Unused switch ports', 
    'shutdown', 

    'end', 
    'copy running-config startup-config'
    ]

# IP configuration for PC-A and PC-B
conf_ip = [
    '192.168.10.126', # to change ID 0
    '255.255.255.128', # to change ID 1
    '192.168.10.1', # to change ID 2

    '192.168.10.190', # to change ID 3
    '255.255.255.192', # to change ID 4
    '192.168.10.129' # to change ID 5
    ]

def operazione_1():
    for word in conf_pcA:
        x = True
        while x:
            if keyboard.read_key() == "0":
                x = False
            else:
                pass

        pyautogui.press("backspace")
        pyautogui.typewrite(word)

def operazione_2():
    for word in conf_pcB:
        x = True
        while x:
            if keyboard.read_key() == "0":
                x = False
            else:
                pass

        pyautogui.press("backspace")
        pyautogui.typewrite(word)
        
def operazione_3():
    for word in conf_ip:
        x = True
        while x:
            if keyboard.read_key() == "0":
                x = False
            else:
                pass

        pyautogui.press("backspace")
        pyautogui.typewrite(word)

def common_operations():
    time.sleep(2)
    while True:
        if keyboard.is_pressed('ctrl+1'):
            print("PRESSED ctrl+1")
            operazione_1()
        else:
            pass

        if keyboard.is_pressed('ctrl+2'):
            print("PRESSED ctrl+2")
            operazione_2()
        else:
            pass

        if keyboard.is_pressed('ctrl+3'):
            print("PRESSED ctrl+3")
            operazione_3()
        else:
            pass

def main():
    while True:
        # 192.168.10.0 R1
        if keyboard.is_pressed('ctrl+1+9+r'):
            print("PRESSED ctrl+1+9+r")

            # same as default
            common_operations()
        else: 
            pass

        # 192.168.10.0 RT
        if keyboard.is_pressed('ctrl+1+9+r+t'):
            print("PRESSED ctrl+1+9+r+t")

            # change only hostname, ip are the same
            conf_pcA[3] = 'hostname Central-RT'
            conf_pcB[3] = 'hostname Central-SW'

            common_operations()
        else: 
            pass

        # 209.165.201.0 RT
        if keyboard.is_pressed('ctrl+2+0+r+t'):
            print("PRESSED ctrl+2+0+r+t")

            # change ip and hostame
            conf_pcA[3] = 'hostname Central-RT'
            conf_pcA[7] = 'ip address 209.165.201.33 255.255.255.224'
            conf_pcA[12] = 'ip address 209.165.201.1 255.255.255.224'

            conf_pcB[3] = 'hostname Central-SW'
            conf_pcB[7] = 'ip address 209.165.201.2 255.255.255.224'
            conf_pcB[10] = 'ip default-gateway 209.165.201.1'

            conf_ip[0] = '209.165.201.30'
            conf_ip[1] = '255.255.255.224'
            conf_ip[2] = '209.165.201.1'
            conf_ip[3] = '209.165.201.62'
            conf_ip[4] = '255.255.255.224'
            conf_ip[5] = '209.165.201.33'

            common_operations()
        else: 
            pass

        # 172.16.1.0 A
        if keyboard.is_pressed('ctrl+1+7+a'):
            print("PRESSED ctrl+1+7+a")

            # change ip and hostame
            conf_pcA[3] = 'hostname Router-A'
            conf_pcA[7] = 'ip address 172.16.1.65 255.255.255.224'
            conf_pcA[12] = 'ip address 172.16.1.1 255.255.255.192'

            conf_pcB[3] = 'hostname Switch-A'
            conf_pcB[7] = 'ip address 172.16.1.2 255.255.255.192'
            conf_pcB[10] = 'ip default-gateway 172.16.1.1'

            conf_ip[0] = '172.16.1.62'
            conf_ip[1] = '255.255.255.192'
            conf_ip[2] = '172.16.1.1'
            conf_ip[3] = '172.16.1.94'
            conf_ip[4] = '255.255.255.224'
            conf_ip[5] = '172.16.1.65'

            common_operations()
        else: 
            pass

        # 172.16.1.0 R1
        if keyboard.is_pressed('ctrl+1+7+r'):
            print("PRESSED ctrl+1+7+r")

            # hostame are same change ip           
            conf_pcA[7] = 'ip address 172.16.1.65 255.255.255.224'
            conf_pcA[12] = 'ip address 172.16.1.1 255.255.255.192'

            conf_pcB[7] = 'ip address 172.16.1.2 255.255.255.192'
            conf_pcB[10] = 'ip default-gateway 172.16.1.1'

            conf_ip[0] = '172.16.1.62'
            conf_ip[1] = '255.255.255.192'
            conf_ip[2] = '172.16.1.1'
            conf_ip[3] = '172.16.1.94'
            conf_ip[4] = '255.255.255.224'
            conf_ip[5] = '172.16.1.65'

            common_operations()
        else: 
            pass

        # 192.168.10.0 A
        if keyboard.is_pressed('ctrl+1+9+a'):
            print("PRESSED ctrl+1+9+a")

            # change ip and hostame
            conf_pcA[3] = 'hostname Router-A'
            conf_pcA[7] = 'ip address 192.168.10.129 255.255.255.192'
            conf_pcA[12] = 'ip address 192.168.10.1 255.255.255.128'

            conf_pcB[3] = 'hostname Switch-A'
            conf_pcB[7] = 'ip address 192.168.10.2 255.255.255.128'
            conf_pcB[10] = 'ip default-gateway 192.168.10.1'

            conf_ip[0] = '192.168.10.126'
            conf_ip[1] = '255.255.255.128'
            conf_ip[2] = '192.168.10.1'
            conf_ip[3] = '192.168.10.190'
            conf_ip[4] = '255.255.255.192'
            conf_ip[5] = '192.168.10.129'

            common_operations()
        else: 
            pass
    

if __name__ == "__main__":
    main()
