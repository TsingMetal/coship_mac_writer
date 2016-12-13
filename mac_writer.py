from hex_string_to_int import hex_char_to_int
from mac_to_bin import mac_string_to_bin
from time import sleep, ctime
import os

usb_root = 'H:\\'

def main():
    while True:
        os.system('clear')
        print("Test starting...")
        while True:
            sn = getSn()
            stb_mac = getStbMac()
            eoc_mac = getEocMac()

            while eoc_mac == stb_mac:
                print("EOC_MAC = STB_MAC!! RETRY!!")
                stb_mac = getStbMac()
                eoc_mac = getEocMac()

            next_step = input("\nType 'N' to UNDO 'Y' to CONTINUE => ")
            if 'n' in next_step.lower():
                onEnd()
                break

            if genSnBin(sn) == 1:
                onEnd()
                break
            if genStbMacBin(stb_mac) == 1: 
                onEnd()
                break
            if genEocMacBin(eoc_mac) == 1:
                onEnd()
                break

            next_step = input("\nPress 'Enter' to Write SN&MAC")
            log(sn, stb_mac, eoc_mac)
            writeMac()

            next_step = input("\nType 'N' to re-write 'Y' to end => ")
            while 'n' in next_step.lower(): 
                writeMac()
                next_step = input("\nType 'N' to re-write 'Y' to end => ")

            print("\nWriting completed")
            onEnd()
            break
            
def getSn():
    print("\n" + "=" * 40 + "\n")
    sn = input("Input SN => ")
    while len(sn) != 19:
        sn = input("WRONG SN!!\n Input SN again => ")
    print("\n" + "=" * 40)
    return sn

def getStbMac():
    stb_mac = input("\nInput STB_MAC => ")
    while len(stb_mac) != 12 or \
            hex_char_to_int(stb_mac[-1]) % 2 == 0:
        stb_mac = input("WRONG STB_MAC!!\n Input again => ")
    return stb_mac

def getEocMac():
    eoc_mac = input("\nInput EOC_MAC => ")
    while len(eoc_mac) != 12:
        eoc_mac = input("WRONG EOC_MAC!!\n Input again => ")
    return eoc_mac

def genSnBin(sn):
    header = b'\xf1\xf2\xf3\xf4'
    footer = b'\x86\x87\x88\x89\x1f'
    sn_bin = bytes(sn, encoding="latin1")
    try:
        open(usb_root + 'sn.bin', 'wb').write(header + sn_bin + footer)
        print('\nGenerate "sn.bin"\tOK')
        sleep(0.5)
        return 0
    except:
        print("\nGenerate sn.bin WRONG!!")
        onEnd()
        return 1

def genStbMacBin(mac):
    header = b'\xf1\xf2\xf3\xf4'
    mac_bin = mac_string_to_bin(mac)
    try:
        open(usb_root + 'mac.bin', 'wb').write(header + mac_bin)
        print('\nGenerate "mac.bin"\tOK')
        sleep(0.5)
        return 0
    except:
        print('\nGenerate "mac.bin" WRONG!!')
        onEnd()
        return 1

def genEocMacBin(mac):
    header = b'\xf1\xf2\xf3\xf4'
    mac_bin = mac_string_to_bin(mac)
    try:
        open(usb_root + 'mac2.bin', 'wb').write(header + mac_bin)
        print('\nGenerate "mac2.bin"\tOK')
        sleep(0.5)
        return 0
    except:
        print("\nGenerate mac2.bin WRONG!!")
        onEnd()
        return 1

def writeMac():
    '''
    os.system("adb remount")
    os.system("adb shell")
    '''
    os.system("python")

def log(sn, mac, mac2):
    date = ctime()
    log_text = '''
       -----------------------------------------\n
       DATE:\t%s\n
       SN:\t%s\n
       STB_MAC:\t%s\n
       EOC_MAC:\t%s\n
       -----------------------------------------\n
    '''
    open('FML_LOG.txt', 'a').write(log_text % (date, sn, mac, mac2))

def onEnd(): # End currend circle
    print("\nProgram will re-start in 3 seconds")
    for i in range(3, 0, -1):
        print(i)
        sleep(1)
    os.system('clear')

if __name__ == '__main__':
    main()
