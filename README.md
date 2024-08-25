# NOTICE

**MAKE SURE YOU HAVE DOCKER AND PYTHON INSTALLED! PLACE THE PRODINFO YOU WANNA INJECT INTO TO "prodinfo.gen.bin" AND THE ONE USED AS A DONOR "prodinfo.donor.bin"**

**THE TOOL IS BROKEN SO IT WILL NOT INJECT INTO PRODINFOS WITH CERTS ALREADY IN THEM, THE TOOL ONLY WORKS WITH PRODINFO GENERATED FROM PRODINFO_GEN TOOL ATM!!**

While the tool does indeed sucessfully inject keys, serials, and certificates, the console for some reason **WILL NOT BOOT!**

if anybody would like to tinker with this and update the readme or the code, prs are welcome

# docs
oct = onlne cert 
os = other stuff (such as device cert, but i dont have a device cert in my prodinfos)
s = serial
ks = keys
di = deviceID

there are parts to each of these labeled as "pt" so every 2 parts is a start and end adress, so oct_pt_1 is the start adress and oct_pt_2 is the end adress and so on. Adding new injection options is easy since you just have to add new offsets, copy and paste one of the functions and rewrite it with the new offsets, then allow this function to be used as a option in main.py

source: https://switchbrew.org/wiki/Calibration

some credit goes to this repo, as i based this tool off of theirs: https://github.com/eXhumer/eXCertXtract/

# installation
```
git clone https://github.com/erew70/prodinfo-injection-tool.git
cd prodinfo-injection-tool
pip install -r requirements.txt
py -3 main.py
