# prdinfo-injection
how to inject new ssl cert


[Source](https://switchbrew.org/wiki/Calibration)

Tools:

[HXD](https://mh-nexus.de/en/hxd/)


to inject prodinfo with a new cert, open up the prodinfo you want to replace and the donor one your using to inject

open it in hxd

then go to these offset bytes and replace them:


00000AE0 to 00000AF0

00002A90 to 00002CD0

00003AF0 to 00003C10

00000AD0 to 00002310

what i would do is copy from all the way to those offsets and paste it into the new one

if you did it correctly you have injected a new certificate into your prodinfo, so basically if you injected an unbanned cert into your banned prodinfo, now your prodinfo is unbanned. but i wouldnt use it yet so wait please dont do anything : )
