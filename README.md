# NOTICE

**MAKE SURE YOU HAVE DOCKER AND PYTHON INSTALLED! PLACE THE PRODINFO YOU WANNA INJECT INTO TO "prodinfo.gen.bin" AND THE ONE USED AS A DONOR "prodinfo.donor.bin"**

**THE TOOL IS BROKEN SO IT WILL NOT INJECT INTO PRODINFOS WITH CERTS ALREADY IN THEM, THE TOOL ONLY WORKS WITH PRODINFO GENERATED FROM PRODINFO_GEN TOOL ATM!!**

While the tool does indeed sucessfully inject keys, serials, and certificates, the console for some reason **WILL NOT BOOT!**

if anybody would like to tinker with this and update the readme or the code, prs are welcome


# installation
```
git clone https://github.com/erew70/prodinfo-injection-tool.git
cd prodinfo-injection-tool
pip install -r requirements.txt
py -3 main.py

