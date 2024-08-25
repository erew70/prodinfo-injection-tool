# prdinfo-injection
## NOTICE: PRODINFO.bin must be decrypted! (atmosphere already makes decrypted prodinfo backups in: atmosphere/automatic_backups)

how to inject ssl cert and other PRODINFO data

Tool is coming out soon....


[Source](https://switchbrew.org/wiki/Calibration)

[Reference](https://github.com/eXhumer/eXCertXtract/blob/main/exnut/_cal0.py)

Tools:

[HXD](https://mh-nexus.de/en/hxd/)


to inject prodinfo with a new cert, open up the prodinfo you want to replace and the donor one your using to inject

open it in hxd

then go to these offset bytes and replace them:


00000AE0 to 00000AF0

00002A90 to 00002CD0

00003AF0 to 00003C10

00000AD0 to 00002310

00003AE0 to 00003AF0

what i would do is copy from all the way to those offsets and paste it into the prodinfo you wanna inject

nice to know where certs are stored but it does not boot : (

to check if you did it correctly i would load it into nxnandmanager

you can probably inject into a prodinfo gen tool bin file, but idk i havent tested (crash too?)
