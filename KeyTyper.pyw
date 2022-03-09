import pyautogui
import keyboard
import time

# PC-A configuration so it is the configuration of the ROUTER
conf_pcA = [
    'enable', 
        'configure terminal ', 
        'no ip domain-lookup', 
        'hostname Router-A', 
        'banner motd #Unauthorized access to this device is prohibited!#',
        
        'interface g0/0/0', 
        'description Connect to Subnet B', 
        'ip address 172.16.1.65 255.255.255.224', 
        'no shutdown', 
        'exit',
            
        'interface g0/0/1', 
        'description Connect to Subnet A', 
        'ip address 172.16.1.1 255.255.255.192', 
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
    'hostname Switch-A', 
    'banner motd #Unauthorized access to this device is prohibited!#', 
    
    'interface vlan 1', 
    'description Switch Subnet A', 
    'ip address 172.16.1.2 255.255.255.192', 
    'no shutdown ', 
    'exit', 
    
    'ip default-gateway 172.16.1.1',

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
    '172.16.1.62',
    '255.255.255.192',
    '172.16.1.1',

    '172.16.1.94',
    '255.255.255.224',
    '172.16.1.65'
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

def main():
    while True:
        if keyboard.is_pressed('ctrl+1+7+r'):
            print("PRESSED ctrl+1+7+r")

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
        else: 
            pass
    

if __name__ == "__main__":
    main()
