# NOTICE

⚠️ please dont go online after using this tool (yet) ⚠️


**MAKE SURE YOU HAVE DOCKER AND PYTHON INSTALLED! PLACE THE PRODINFO YOU WANNA INJECT INTO TO "prodinfo.gen.bin" AND THE ONE USED AS A DONOR "prodinfo.donor.bin", THESE FILES MUST BE DECRYPTED! ATMOSPHERE MAKES AUTOMATIC PRODINFO BACKUPS AT "atmosphere/automatic_backups"!**

**BLANKING OPTION ONLY BLANKS "prodinfo.gen.bin"! BLANKING DOES NOT WORK ON 17.0.0+ WITHOUT PATCHES!**


**JUST THIS TOOL IS NOT ENOUGH FOR A COMPLETE UNBAN! (but its part of it!)**

Check this to fix prodinfo blanking crashes: https://github.com/fruityloops1/nim-prodinfo-blank-fix

For injections from another factory prodinfo, (that isnt tied to your switch) please read: https://github.com/EliseZeroTwo/deviceid-exosphere-builder

Heres what injections work right now:

| Amiibos | GameCards | Online | Blanking |
|:-------:|:---------:|:------:|:------:|
|✅|✅|✅ |✅|

* a blank.bin has been supplied for you to build your prodinfo from scratch
* Amiibos already work from prodinfo_gen but if you want you can inject amiibos yourself
* also injecting into factory prodinfo (one that hasnt been generated) also works 👍




# so how does this work?
this tool works by reading bytes from the donor prodinfo that is provided and injecting it into the prodinfo gen file, pretty straightforward.

# docs
oct = onlne cert 

os = other stuff (such as device cert, but i dont have a device cert in my prodinfos)

s = serial

ks = keys

di = deviceID

gc = gamecard

ao = amiibo


there are parts to each of these labeled as "pt" so every 2 parts is a start and end address, so oct_pt_1 is the start address and oct_pt_2 is the end adress and so on. Adding new injection options is easy since you just have to add new offsets, copy and paste one of the functions and rewrite it with the new offsets, then allow this function to be used as a option in main.py

source: https://switchbrew.org/wiki/Calibration

some good amount of credit goes to this repo, as i based this tool off of theirs: https://github.com/eXhumer/eXCertXtract/

# Installation
```
git clone https://github.com/erew70/prodinfo-injection-tool.git
cd prodinfo-injection-tool
py -3 main.py
```

# Support

if you need my help, add me on discord: erew0962
