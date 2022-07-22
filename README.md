# tbrute
## 私から離れた人に対する復讐の為のcode
## 私は私から離れて行った人を一生許しません。
## このプログラムでのbruteforceが終わったらTwitterをbruteforceします。
## もしもあなたにも許せない人が居るのであればこのプログラムのINLINE19の最初の.までをID→Base64、その次をtimestamp+1293840000をBase64にしてください、最後の文字列はHMACを使用しており確率はabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_(64)^27で1/5.846,01e+48です。
## 私はこれを私のbotnetを使用してでも探し当てますが、あなたが一台のPCを使用してする場合かなりの時間を要するでしょう。
## 1Network tbrute.pyを使用する場合、Tor Proxy(https://github.com/dperson/torproxy )をWSL等で建ててください。
## 速さ重視のSecureでRateLimitをbypassしてあるtorrec設定
```
ExcludeNodes {JP},{US},{CN},104.244.72.115,45.61.184.239,206.55.74.0,118.163.74.160,46.182.106.190,185.14.97.147,193.218.118.90,87.120.254.105,104.244.76.44,188.240.210.20,85.195.206.134,193.46.254.45,146.59.234.220,23.184.48.61,64.98.231.29,87.121.52.47,{IT},{FI}
StrictNodes 1
NumEntryGuards 5
MaxCircuitDirtiness 1
```
さらにSecureにしたい場合は以下の国を追加してください。
```
JP, US, KR, RU, CN, FR, FX, TH, TW, UA, SG, TR, HK, PL, MN, FI, PW, IN, BR, BR, PH, PK, SA, AU, NZ, CA, IL, AL, BE, BG, HR, CZ, DK, EE, DE, GR, HU, IS, IT, LV, LT, LU, AN, NL, NO, PT, RO, SK, SI, ES, TR, GB
```
--
# tbrute 
## Code for revenge on those who have left my side
## I will never forgive anyone who runs away or leaves me.
## I will bruteforce Twitter once this is done.
## If you are someone not able to forgive t it, please change the first . of INLINE19 in this program to ID -> Base64, and the next to timestamp+1293840000 to Base64. The last string uses HMAC, which can only be done by bruteforce, and the probability is abcdefghijklmnopqrstuvwxyzA The probability is 1/5.846,01e+48 with abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_(64)^27.
## I'll try to find this even using my botnet, but it will take quite a while if you use one PC.
