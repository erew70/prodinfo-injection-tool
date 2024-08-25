from util.read_write import *
from util.data import offsets
import os, platform, sys

docker_path = r"C:\Program Files\Docker\Docker"

donor = 'prodinfo.donor.bin'
gen = 'prodinfo.gen.bin'




def getOspt():
    return sys.platform


def show_menu():
    print("Welcome to the Prodinfo Injector Tool!")
    print("1. Do default")
    print("2. Inject SSL Cert From DONOR")
    print("3. Inject Serial From DONOR")
    print("4. Inject console-unqiue keys (NOT PROD.KEYS!)")
    print("5. Create DeviceID patch to allow booting after injection")
    print("6. Exit")
    print("gamecard key injections coming soon....")


def default():
    with open('prodinfo.donor.bin', 'rb'):
        importSSLCert(gen, donor)
        importOtherStuff(gen, donor)
        importSerial(gen,donor)
        importKeys(gen,donor)
        importNewDeviceID(gen,donor)
        print("Default has been injected!")
        print(f"Creating Patch with: {getDeviceID(donor)}")
        if os.path.exists("output"):
            try:
                device_id = getDeviceID(donor)
                os.system(f'powershell docker run -ti --rm -e DEVICEID=0x{device_id} -v "$PWD/output:/output" pablozaiden/deviceid-exosphere-builder:latest')
            except:
                print("an error has occured creating your patch. please make sure docker is installed!")

        else:
            try:
                os.system("mkdir output")
                device_id = getDeviceID(donor)
                os.system(f'powershell docker run -ti --rm -e DEVICEID=0x{device_id} -v "$PWD/output:/output" pablozaiden/deviceid-exosphere-builder:latest')
            except:
                print("an error has occured creating your patch. please make sure docker is installed!")


def injectCert():
   with open('prodinfo.donor.bin', 'rb'):
        importSSLCert(gen, donor)
        importOtherStuff(gen, donor)
        importNewDeviceID(gen, donor)
        input("SSL Cert Sucessfully injected!")


def injectSerial():
    with open('prodinfo.donor.bin', 'rb'):
        importSerial(gen, donor)
        importNewDeviceID(gen, donor)
        input("Serial Info Sucessfully injected!")

def injectKeys():
    with open('prodinfo.donor.bin', 'rb'):
        importKeys(gen, donor)
        importNewDeviceID(gen, donor)
        input("Keys Sucessfully injected!")

def create_deviceID_patch():
    print(f"Creating Patch with: {getDeviceID(donor)}")
    if os.path.exists("output"):
        try:
            device_id = getDeviceID(donor)
            os.system(f'powershell docker run -ti --rm -e DEVICEID=0x{device_id} -v "$PWD/output:/output" pablozaiden/deviceid-exosphere-builder:latest')
        except:
            print("an error has occured creating your patch. please make sure docker is installed! if deviceid_exosphere.bin already exists, please delete it!")

    else:
        try:
            os.system("mkdir output")
            device_id = getDeviceID(donor)
            os.system(f'powershell docker run -ti --rm -e DEVICEID=0x{device_id} -v "$PWD/output:/output" pablozaiden/deviceid-exosphere-builder:latest')
        except:
            print("an error has occured creating your patch. please make sure docker is installed! if deviceid_exosphere.bin already exists, please delete it!")

def main():
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            default()
        elif choice == 2:
            injectCert()
        elif choice == 3:
            injectSerial()
        elif choice == 4:
            injectKeys()
        elif choice == 5:
            create_deviceID_patch()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


oS = getOspt()

if oS == "win32":
    if not os.path.exists(docker_path):
        print(f"⚠️ Docker does not exist!")
        input("Press enter or close the window to exit (please install docker!)")
        exit(1)
    else:
        if __name__ == "__main__":
            main()
else:
    print("ERR: CANNOT CHECK FOR DOCKER INSTALLATION, RUNNING ANYWAY (make sure docker is installed!)")
    if __name__ == "__main__":
        main()

