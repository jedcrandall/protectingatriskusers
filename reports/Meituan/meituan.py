#!/usr/bin/python3

import sys
import re

uid1 = re.compile('utm.*uuid=[0-9a-fA-F]+')
uid1trim = re.compile('uuid=0000000000000[0-9a-fA-F]+')
uid2 = re.compile('&id=[0-9a-fA-F]+&packageName=com.sankuai.meituan')
uid2trim = re.compile('&id=0000000000000[0-9a-fA-F]+')
uid3 = re.compile('uuid=[0-9a-fA-F]+.*utm')
uid3trim = re.compile('uuid=0000000000000[0-9a-fA-F]+')
sharkid = re.compile('M-SHARK-TRACEID: [0-9a-fA-F]+')
pragmaid1 = re.compile('pragma-..id: [0-9a-fA-F]+')
pragmaid2 = re.compile('pragma-unionid: [0-9a-fA-F]+')
pragmaid3 = re.compile('pragma-uuid: [0-9a-fA-F]+')
pragmaid4 = re.compile('utm-content: [0-9a-fA-F]+')
pragmaid5 = re.compile('pragma-device: [0-9a-fA-F]+')
uaid = re.compile('User-Agent: AiMeiTuan.{40,200}-[a-z]+')
uaidtrim = re.compile('[0-9a-fA-F]{32,80}-[a-z]+')
four43 = re.compile('\"u\":\"[0-9a-fA-F]+')
four43trim = re.compile('\"u\":\"[0-9a-fA-F]+')


lat = re.compile("lat=[0-9\.\-]+")
lng = re.compile("lng=[0-9\.\-]+")
mypos = re.compile("mypos=[0-9\.\-]+%2C[0-9\.\-]+")
lattrim = re.compile("mypos=[0-9\.\-]+")
lngtrim = re.compile("%2C[0-9\.\-]+")
latlng = re.compile("latlng=[0-9\.\-]+%2C[0-9\.\-]+")
lattrimlat = re.compile("latlng=[0-9\.\-]+")

ipre = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{5}\-[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{5}:")

utmidreference = "5E5DF6CB118C41B3829A92A059DA09AE"
gpsreference = "-111\.6"

lastip = "0.0.0.0"

utmid = None
latstr = None
lngstr = None

for line in sys.stdin:
    #find IP info
    ipstrnew = None
    m = re.search(ipre, line)
    if m:
        ipstr = m.group()[22:22+21]
        dots = 0
        ipstrnew = ""
        for c in ipstr:
            if c != '0' and c != '.':
                ipstrnew = ipstrnew + c
            elif c == '.':
                dots = dots + 1
                if dots <= 3:
                    if len(ipstrnew) > 0:
                        if ipstrnew[-1] == '.':
                            ipstrnew = ipstrnew + '0'
                    ipstrnew = ipstrnew + '.'
                else:
                    ipstrnew = ipstrnew + ':'
            elif c == '0' and len(ipstrnew) > 0:
                if ipstrnew[-1] >= '0' and ipstrnew[-1] <= '9':
                    ipstrnew = ipstrnew + '0'

    # Print info for last packet, if it has an ID, before moving on...
    if ipstrnew:
        if utmid:
            print(lastip + "...\n" + utmid, end = '')
            if latstr and lngstr:
                print(" " + latstr + "," + lngstr)
            else:
                print("")
        elif latstr or lngstr:
            print("GPS without ID...")
            print(line)
        utmid = None
        latstr = None
        lngstr = None
        lastip = ipstrnew

    # find IDs
    m = re.search(uid1, line)
    if m:
        trim = re.search(uid1trim, m.group())
        if trim:
            utmid = trim.group()[18:18+32]
        else:
            print("Something went wrong trimming uid1")
            print(line)
            exit(0)
    m = re.search(uid2, line)
    if m:
        trim = re.search(uid2trim, m.group())
        if trim:
            utmid = trim.group()[17:17+32]
        else:
            print("Something went wrong trimming uid2")
            print(line)
            exit(0)
    m = re.search(uid3, line)
    if m:
        trim = re.search(uid3trim, m.group())
        if trim:
            utmid = trim.group()[18:18+32]
        else:
            print("Something went wrong trimming uid3")
            print(line)
            exit(0)
    m = re.search(sharkid, line)
    if m:
        utmid = m.group()[33:33+32]
    m = re.search(pragmaid1, line)
    if m:
        utmid = m.group()[13:13+32].upper()
    m = re.search(pragmaid2, line)
    if m:
        utmid = m.group()[16:16+32].upper()
    m = re.search(pragmaid3, line)
    if m:
        utmid = m.group()[26:26+32].upper()
    m = re.search(pragmaid4, line)
    if m:
        utmid = m.group()[13:13+32].upper()
    m = re.search(pragmaid5, line)
    if m:
        utmid = m.group()[15:15+32].upper()
    m = re.search(uaid, line)
    if m:
        trim = re.search(uaidtrim, m.group())
        if trim:
            utmid = trim.group()[0:0+32].upper()
        else:
            print("Something went wrong trimming uaid")
            print(line)
            exit(0)
    m = re.search(four43, line)
    if m:
        trim = re.search(four43trim, m.group())
        if trim:
            utmid = trim.group()[18:18+32].upper()
        else:
            print("Something went wrong trimming four43")
            print(line)
            exit(0)

    #find GPS
    latm = re.search(lat, line)
    if (latm):
        latstr = latm.group()
    lngm = re.search(lng, line)
    if (lngm):
        latstr = lngm.group()
    myposm = re.search(mypos, line)
    if (myposm):
        latm = re.search(lattrim, myposm.group())
        lngm = re.search(lngtrim, myposm.group())
        if latm and lngm:
            latstr = "lat=" + latm.group()[6:]
            lngstr = "lng=" + lngm.group()[3:]
        else:
            print("Something went wrong trimming mypos")
            print(line)
            exit(0)
    latlngm = re.search(latlng, line)
    if (latlngm):
        latm = re.search(lattrimlat, latlngm.group())
        lngm = re.search(lngtrim, latlngm.group())
        if latm and lngm:
            latstr = "lat=" + latm.group()[7:]
            lngstr = "lng=" + lngm.group()[3:]
        else:
            print("Something went wrong trimming latlng")
            print(line)
            exit(0)


    # Find things we don't yet have an re for...
    linereference = line.upper()
    if (utmidreference in linereference) and not utmid:
        print(line)
    if (gpsreference in linereference) and not (latstr or lngstr):
        print(line)


# Print info for last packet, if it has an ID
if utmid:
    print(lastip + "...\n" + utmid, end = '')
    if latstr and lngstr:
        print(" " + latstr + "," + lngstr)
    else:
        print("")
elif latstr or lngstr:
    print("GPS without ID...")
    print(line)


