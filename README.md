# NOTICE

**MAKE SURE YOU HAVE DOCKER AND PYTHON INSTALLED! PLACE THE PRODINFO YOU WANNA INJECT INTO TO "prodinfo.gen.bin" AND THE ONE USED AS A DONOR "prodinfo.donor.bin"**

Stability: ✅ (tool is working)

The tool works as long as you inject into a prodinfo that has been generated from [Prodinfo_gen](https://github.com/CaramelDunes/prodinfo_gen)

if you are injecting a prodinfo from another console into prodinfo.gen.bin, make sure to use deviceID patch! Please read: https://github.com/EliseZeroTwo/deviceid-exosphere-builder (my tool generates a patch for you if you select default or 5)

please dont go online after using this tool unless you came from [my switch unban guide and you know what you are doing](https://github.com/erew70/SWITCH-UNBAN-GUIDE)

if anybody would like to tinker with this and update the readme or the code, prs are welcome

# docs
oct = onlne cert 

os = other stuff (such as device cert, but i dont have a device cert in my prodinfos)

s = serial

ks = keys

di = deviceID

gamecard key/cert injection will come soon, for now just restore the prodinfo (if its another console) then place the donor prodinfo where it should go for prodinfo gen then generate it. this tool will soon support it

there are parts to each of these labeled as "pt" so every 2 parts is a start and end address, so oct_pt_1 is the start address and oct_pt_2 is the end adress and so on. Adding new injection options is easy since you just have to add new offsets, copy and paste one of the functions and rewrite it with the new offsets, then allow this function to be used as a option in main.py

source: https://switchbrew.org/wiki/Calibration

some good amount of credit goes to this repo, as i based this tool off of theirs: https://github.com/eXhumer/eXCertXtract/

# installation
```
git clone https://github.com/erew70/prodinfo-injection-tool.git
cd prodinfo-injection-tool
pip install -r requirements.txt
py -3 main.py
