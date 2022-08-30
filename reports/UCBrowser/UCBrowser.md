UC Browser
============

UC Browser is free browser developed by UCWeb. The international Android
version is available in the Google Play store and the Chinese Android version
can be downloaded from:

 [http://www.uc.cn](http://www.uc.cn)
 
We analyzed different versions of the international and Chinese Android app.
Researchers had [previously
reported](https://www.usenix.org/conference/foci16/workshop-program/presentation/knockel)
PII being sent with easily decryptable encryption and insecure update
mechanisms in UC Browser, so we sought to answer the question of if these
issues persist in the latest versions of UC Browser and gather more context.

App description
------------

UC Browser is a popular mobile web browser developed by UCWeb, who are owned by the Alibaba Group. The application is the [second most used mobile browser in China](https://gs.statcounter.com/browser-market-share/mobile/china/#monthly-202110-202202) and the [fifth most used mobile browser worldwide](https://gs.statcounter.com/browser-market-share/mobile/worldwide/#monthly-202110-202202).

It has been the subject of several security and privacy concerns:

  * Both Android versions of the application were found to leak a significant amount of personal and personally-identifiable data, the details can be found in the [report](https://citizenlab.ca/2015/05/a-chatty-squirrel-privacy-and-security-issues-with-uc-browser/) released by the Citizen Lab on May 21, 2015. 
  * Both Android versions and the Windows version were found to transmit personally identifiable information with easily decryptable encryption, and the Windows version was vulnerable to arbitrary code execution during software updates.  The details can be found in [Privacy and Security Issues in BAT Web Browsers](https://www.usenix.org/system/files/conference/foci16/foci16-paper-knockel.pdf).
  * UC Browser was [banned in India](https://www.indiatoday.in/india/story/centre-announces-ban-chinese-apps-privacy-issues-1695265-2020-06-29) on June 29, 2020.
  * Both Android and iOS versions were found to exfiltrate user browsing and search history even when the browser is used in incognito mode. Details can be found in [here](https://hookgab.medium.com/ucbrowser-privacy-study-ecff96fbcee4).
  * Other [concerns](https://news.drweb.com/show/?i=13176)



Update process
------------

We analyzed the international Android app version 13.4.0.1306, downloaded in January 2022, to find out if the insecure update mechanism [reported by researchers in the past](https://www.usenix.org/conference/foci16/workshop-program/presentation/knockel) was still vulnerable in the latest versions of UC Browser.

The browser checks for updates by making an HTTPS POST request to
puds.ucweb.com. This request contains details of the phone like the Android OS
version, CPU type and screen dimensions. 

~~~java
if (com.uc.common.a.j.b.bg(str2)) {
    c cVar2 = this.gLY.get("ucmobile");
    if (cVar2 != null) {
        str2 = cVar2.gLv;
    }
    str2 = "https://puds.ucweb.com/upgrade/index.xhtml";
} 
~~~

This request contains details of the phone like the Android OS version, CPU
type and screen dimensions. 

~~~java
byte[] encryptByExternalKey;
byte[] s;
rP.setMethod("POST");
b bVar2 = bVar;
com.uc.business.e.f fVar = new com.uc.business.e.f();
fVar.setImei("");
fVar.lU(Build.MODEL);
fVar.width = com.uc.common.a.i.b.getScreenWidth();
fVar.height = com.uc.common.a.i.b.getScreenHeight();
fVar.setImsi("");
com.uc.base.util.i.b.bMk();
fVar.lV(com.uc.base.util.i.b.getSmsNo());
fVar.lW("");
com.uc.business.e.c cVar2 = new com.uc.business.e.c();
m.b(cVar2);
ax axVar = new ax();
axVar.cUa = fVar;
axVar.cTZ = cVar2;
e eVar = bVar2.gMK.gMj;
axVar.kDX = bVar2.gMK.gMj.mMode;
ArrayList<com.uc.business.e.a> arrayList = axVar.kBN;
com.uc.base.util.i.b.bMk();
arrayList.add(b.fx("os_ver", com.uc.base.util.i.b.getRomInfo()));
arrayList.add(b.fx("processor_arch", e.getCpuArch()));
arrayList.add(b.fx("cpu_arch", e.ht()));
String hv = e.hv();
arrayList.add(b.fx("cpu_vfp", hv));
arrayList.add(b.fx("net_type", String.valueOf(com.uc.base.system.a.si())));
arrayList.add(b.fx("net_ap", String.valueOf(com.uc.base.system.a.getNetworkClass())));
arrayList.add(b.fx("fromhost", eVar.gLF));
arrayList.add(b.fx("plugin_ver", eVar.gLG));
arrayList.add(b.fx("target_lang", eVar.gLM));
arrayList.add(b.fx("system_lang", eVar.gLN));
arrayList.add(b.fx("vitamio_cpu_arch", eVar.gLO));
arrayList.add(b.fx("vitamio_vfp", eVar.gLP));
arrayList.add(b.fx("vitamio_vfp3", eVar.gLQ));
arrayList.add(b.fx("plugin_child_ver", eVar.gLS));
arrayList.add(b.fx("ver_series", eVar.gLR));
arrayList.add(b.fx("child_ver", com.uc.browser.f.aCu()));
boolean equalsIgnoreCase = "ucmobile".equalsIgnoreCase(bVar2.gMK.gMj.gLD);
boolean equals = com.uc.browser.z.fg("turnapp_pro", "").equals(bVar2.gMK.gMj.gLD);
byte[] bArr = null;
                        
~~~

UC Browser Android version 13.4.0.1306 verifies the digital signature of the APK downloaded for upgrade before installation:

~~~java
public static Signature[] a(Context context, String str, ValueCallback<Object[]> valueCallback) {
    Throwable th;
    long currentTimeMillis;
    boolean booleanValue;
    Signature[] signatureArr;
    int i;
    boolean z;
    Log.d("SignatureVerifier", String.format("getUninstalledAPKSignature(): archiveApkFilePath = %1s", str));
    Signature[] signatureArr2 = null;
    try {
        currentTimeMillis = System.currentTimeMillis();
        Boolean valueOf = Boolean.valueOf(Boolean.parseBoolean(UCCore.getParam(CDParamKeys.CD_KEY_SHARE_CORE_COMMONALITY_FORCE_VERIFY_V1)));
        booleanValue = valueOf == null ? false : valueOf.booleanValue();
    } catch (Throwable th2) {
        th = th2;
    }
    if (!booleanValue) {
        if (!UCCyclone.detectZipByFileType(str)) {
            z = false;
        } else {
            z = a.a(str) ? true : m.a(str);
        }
        if (z) {
            Log.d("SignatureVerifier", "摘要校验V2!");
            X509Certificate[][] b2 = a.b(str);
            signatureArr = new Signature[b2.length];
            for (int i2 = 0; i2 < b2.length; i2++) {
                signatureArr[i2] = new Signature(b2[i2][0].getEncoded());
            }
            i = 2;
            if (valueCallback != null) {
                try {
                    valueCallback.onReceiveValue(new Object[]{10, Integer.valueOf(i)});
                } catch (Throwable unused) {
                }
            }
            if (signatureArr != null || signatureArr.length <= 0) {
                Log.e("SignatureVerifier", "摘要校验失败");
            } else {
                try {
                    Log.d("SignatureVerifier", "摘要校验成功!");
                    signatureArr2 = signatureArr;
                } catch (Throwable th3) {
                    th = th3;
                    signatureArr2 = signatureArr;
                    Log.e("SignatureVerifier", th.getMessage());
                    return signatureArr2;
                }
            }
            Log.i("SignatureVerifier", "耗时：" + (System.currentTimeMillis() - currentTimeMillis) + "ms");
            return signatureArr2;
        }
    }
    Log.d("SignatureVerifier", "摘要校验V1! 强制V1:".concat(String.valueOf(booleanValue)));
    signatureArr = b(context, str);
    i = 1;
    if (valueCallback != null) {
    }
    if (signatureArr != null) {
    }
    Log.e("SignatureVerifier", "摘要校验失败");
    Log.i("SignatureVerifier", "耗时：" + (System.currentTimeMillis() - currentTimeMillis) + "ms");
    return signatureArr2;
}
~~~
            
Thus it is not possible to cause the browser to download an arbitrary APK, only
APKs signed by UCWeb can be installed. The Android system prevents users from
downgrading apps but if there are other UCWeb applications signed with the same
key as UC Browser they could potentially be installed.  In short, the
vulnerability identified in previous work that allowed arbitrary code execution
has been fixed, but more work is necessary to determine if the fix is
sufficient.  Futhermore, any updates that occur outside of the context of an
established app store remove protections the user would otherwise have, such as
auditibility of the binary that they were sent combined with assurance that
other users were served the same binary.


User's data transmission
------------

We analyzed the international Android app version 13.4.0.1306, downloaded in
January 2022, to find out if the behavior [reported by
researchers in the
past](https://www.usenix.org/conference/foci16/workshop-program/presentation/knockel)
where UC Browser sends PII over the Internet with easily decryptable encryption still persists in the latest versions.

It was [previously
found](https://hookgab.medium.com/ucbrowser-privacy-study-ecff96fbcee4) that
data exfiltration happens even in incognito mode in UC Browser. The visited
URL, the IP of the user and a proprietary ID were sent by the browser
(hereafter referred to as UC Browser's `uid`). This could be used to
fingerprint users.

The above was discovered by noticing a lot of pingbacks to UCWeb servers, then
manually inspecting the requests to find that the data was AES encrypted before
being sent. The key was found in the APK using JADX.  We started testing this
behaviour in the android version that we reverse engineered. We found that the
code that pushes the encrypted data to px-intl.ucweb.com/v1/crash/upload is
still in the APK.

~~~java
if (!TextUtils.isEmpty("http://px-intl.ucweb.com/api/v1/crash/upload")) {
    aVar.dku = "http://px-intl.ucweb.com/api/v1/crash/upload";
    if (!TextUtils.isEmpty("inapppatch5")) {
        aVar.appSubVersion = "inapppatch5";
        aVar.dks = bVar;
        if (aVar.dla != null) {
            String str5 = aVar.dla.eFm;
            com.a.a.a.ca("logDir", str5);
            com.a.a.a.ca("projectName", aVar.dkl);
            com.a.a.a.ca(Constants.KEY_APP_VERSION, aVar.appVersion);
            com.a.a.a.ca("appSubVersion", aVar.appSubVersion);
            com.a.a.a.ca("buildSeq", aVar.buildSeq);
            com.a.a.a.ca("utdid", aVar.dkn);
            com.a.a.a.ca("appSecret", aVar.dkm);
            if (!aVar.dkp.containsKey("bserial")) {
                aVar.dkp.put("bserial", aVar.buildSeq);
            }
            if (!aVar.dkp.containsKey("bsver")) {
                aVar.dkp.put("bsver", aVar.appSubVersion);
            }
            if (!aVar.dkp.containsKey("utdid")) {
                aVar.dkp.put("utdid", aVar.dkn);
            }
            if (!aVar.dkp.containsKey(WPKFactory.INIT_KEY_APP_ID)) {
                aVar.dkp.put(WPKFactory.INIT_KEY_APP_ID, aVar.appId);
            }
            if (aVar.dks == null) {
                aVar.dks = new com.a.a.a.d(aVar.dku, aVar.appId, aVar.dkm, aVar.appVersion, aVar.appSubVersion, aVar.buildSeq, aVar.dkn);
            }
            com.a.a.a.a(new com.a.a.a(aVar.context, aVar.dla, aVar.dkl, str5, aVar.appVersion, aVar.appId, aVar.dkm, aVar.buildSeq, aVar.dkn, aVar.dkp, aVar.dkr, aVar.dks));
            com.a.a.a WT = com.a.a.a.WT();
            com.a.a.c.a aVar2 = jXW;
            WT.dki.dkt = new WeakReference<>(aVar2);
            return;
        }
        throw new IllegalArgumentException("ulogSetup should not be empty");
    }
    throw new IllegalArgumentException("appSubVersion should not be empty");
}
~~~

Furthermore, the AES key is still in the APK as well and it is the same as the
one that had been previously found.

~~~java
package com.uc.browser.l;

public final class m {
    public static String appId = "UCMobileIntl";
    public static String dkm = "QcBe1t#jvn9$ea8f";
}
~~~

Reports every website visited in plaintext
------------

We analyzed the international Android version from the Google Play store,
version V13.4.0.1306, to see what PII UC Browser sends that might be visible on
the Internet without any encryption.

We found a behavior that is readily visible in plaintext in a packet capture of
the traffic generated by UC Browser.  For every website visited, basic
information such as the domain name for the website and the title of the web
page is sent in JSON format over unencrypted HTTP to `logsug.ucweb.com`.  This
behavior is only observed when the browser is *not* in Incognito mode.  This
behavior occurs whether or not the web page being visited uses HTTPS.

While the domain name (from which the title of the web page could be obtained)
is visible in DNS requests and SNI, sending the information to a web service
with a domain name that is predictable can potentially put users at additional
risk beyond leaks of this information *via* DNS or SNI.  For example, an
attacker that controls the DNS system within a region could poison the
`logsug.ucweb.com` domain in users' operating system caches.  Then, every UC
Browser user in the region would report this information to an IP address of
the attacker's choosing, even if the user connected to a VPN (note that VPNs do
not typically flush the OS DNS cache when they are initiated).

UC Browser client to server when visiting `tibetaction.net`:

~~~http
POST /api/v1/client_event?uc_param_str=vesvlanwdnutbipc&ve=13.4.0.1306&sv=inapppatch564&la=en-US&nw=WIFI&dn=35157706627-1a6968d7&ut=AARqTBouUfPoVJko1ks5O1eKjLf8yqUorUf7DbfBX9KXIw%3D%3D&bi=355&pc=AASUXdrOqk3joqQMJ2ahqw9AQRxVtdsLL85CZFdUCUtAcG%2Bdxn%2FO1Yr1xnGpTyt6%2BuAaaNExNjruUat9pcqohYKH HTTP/1.1
Host: logssug.ucweb.com
Connection: keep-alive
Content-Length: 155
Content-Type: application/json
User-Agent:
Accept-Encoding: gzip, deflate

{"stat":[{"vendor":"browser_local","ac":"clk","region":"_ctumv","row":0,"kw":"tibe","title":"Tibet Action Institute","url":"https:\/\/tibetaction.net\/"}]}
~~~

Server response to client:

~~~apache
HTTP/1.1 200 OK
Server: Tengine
Date: Wed, 23 Feb 2022 08:19:34 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 16
Connection: keep-alive
Set-Cookie: PLAY_ERRORS=; Max-Age=0; Expires=Wed, 23 Feb 2022 08:19:34 GMT; Path=/
Set-Cookie: PLAY_FLASH=; Max-Age=0; Expires=Wed, 23 Feb 2022 08:19:34 GMT; Path=/
Set-Cookie: PLAY_SESSION=; Max-Age=0; Expires=Wed, 23 Feb 2022 08:19:34 GMT; Path=/
Cache-Control: no-cache

{"success":true}POST /api/v1/client_event?uc_param_str=vesvlanwdnutbipc&ve=13.4.0.1306&sv=inapppatch564&la=en-US&nw=WIFI&dn=35157706627-1a6968d7&ut=AARqTBouUfPoVJko1ks5O1eKjLf8yqUorUf7DbfBX9KXIw%3D%3D&bi=355&pc=AASUXdrOqk3joqQMJ2ahqw9AQRxVtdsLL85CZFdUCUtAcG%2Bdxn%2FO1Yr1xnGpTyt6%2BuAaaNExNjruUat9pcqohYKH
~~~

UC Browser client to server when visiting `asu.edu`:


~~~apache
HTTP/1.1
Host: logssug.ucweb.com
Connection: keep-alive
Content-Length: 158
Content-Type: application/json
User-Agent:
Accept-Encoding: gzip, deflate

{"stat":[{"vendor":"browser_local","ac":"clk","region":"_ctumv","row":0,"kw":"asu","title":"Arizona State University | ASU","url":"https:\/\/www.asu.edu\/"}]}
~~~

Server response to client:

~~~apache
HTTP/1.1 200 OK
Server: Tengine
Date: Wed, 23 Feb 2022 08:19:43 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 16
Connection: keep-alive
Set-Cookie: PLAY_ERRORS=; Max-Age=0; Expires=Wed, 23 Feb 2022 08:19:43 GMT; Path=/
Set-Cookie: PLAY_FLASH=; Max-Age=0; Expires=Wed, 23 Feb 2022 08:19:43 GMT; Path=/
Set-Cookie: PLAY_SESSION=; Max-Age=0; Expires=Wed, 23 Feb 2022 08:19:43 GMT; Path=/
Cache-Control: no-cache

{"success":true}
~~~

A packet capture of the above behavior is [here](uc.pcap).

Further analysis of PII sent with easily decryptable encryption
============

It was [previously found](https://hookgab.medium.com/ucbrowser-privacy-study-ecff96fbcee4) that data exfiltration happened in incognito mode in UC Browser. The visited URL, the IP of the user and a proprietary ID were sent by the browser. This could be used to fingerptint users. This was found in version 13.4.0.1306 of the international UC Browser app. 

Above we analyzed the international Android app version 13.4.0.1306 downloaded on January 2022 and found the following:

  * The code that pushes the encrypted data to px-intl.ucweb.com/v1/crash/upload is still in the APK.
  * The user information is still AES encrypted and the key is hardcoded in the APK.
  * The hardcoded AES key is same as the one that had been previously found.

Because Internet users in China use the Chinese version of UC Browser rather
than the international version, we also reverse engineered the Chinese UC
Browser app versions: 13.2.1303, 13.4.0.1306, and 13.9.4.1175. We found that:

  * The app sends encrypted data to px.ucweb.com/v1/crash/upload while on incognito mode.
  * The user information is still AES encrypted and the key is hardcoded in the APK.
  * The AES key is different in the international and Chinese versions of the application. The data being transmitted is also different.
  * If a proxy is detected, the AES encrypted data is not sent.
  * There are 7 more different kinds of files that are encrypted and sent to px.ucweb.com/v1/crash/upload. These files are sent even if a proxy is detected.
  * Every file contains different information, and these files do contain URL's visited during an incognito session.
  * All files contain what seems to be a session ID, some files contain the URL's visited while on incognito mode.
  
Description of our set up:
  * We used [JADX](https://github.com/skylot/jadx) for static analysis.
  * We used an emulated phone and a rooted Motorola phone for our analysis.
  * [Genymotion](https://aws.amazon.com/marketplace/pp/prodview-stl3s5srj7gq2) was used for the emulated phone.
  * [Frida-tools](https://frida.re/docs/android/) was used for dynamic analysis.
  * [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) was used to implement Frida scripts on the emulated phone.
  
The following information regards the Chinese UC Browser app versions:
13.2.1303, 13.4.0.1306, and 13.9.4.1175.
  
com.UCMobile-0-jssdkidx.log files:
------------


The files named "______-com.UCMobile-0-jssdkidx.log" are sent while on incognito mode, as part of the body of a request to to px.ucweb.com/v1/crash/upload. Here is an example of one of these reuqests:
~~~
POST https://px.ucweb.com/api/v1/raw/upload HTTP/1.1
Connection: close
Content-Type: multipart/form-data; boundary=Thj1653583826983Thj
wpk-header: app=UCMobile&cver=0&de=2&os=android&sd=M9lnVEhJnqmDAaRtnjqsjAJu2vbIPJIEFfMDgzDreKKgWa5qKR61wz82Z3khVZGi&seq=202205261238541124225&sver=1.0&tm=1653583826&type=jssdkidx&ver=13.9.4.1175&sign=41a3dd60d5b874cd9806a69e14a1dddf
User-Agent: Dalvik/2.1.0 (Linux; U; Android 10; Genymotion 'Phone' version Build/QQ1D.200105.002)
Host: px.ucweb.com
Accept-Encoding: gzip
Content-Length: 749

Hex
  

0000000000 2d 2d 54 68 6a 31 36 35 33 35 38 33 38 32 36 39   --Thj16535838269
0000000010 38 33 54 68 6a 0d 0a 43 6f 6e 74 65 6e 74 2d 44   83Thj..Content-D
0000000020 69 73 70 6f 73 69 74 69 6f 6e 3a 20 66 6f 72 6d   isposition: form
0000000030 2d 64 61 74 61 3b 20 6e 61 6d 65 3d 22 66 69 6c   -data; name="fil
0000000040 65 22 3b 20 66 69 6c 65 6e 61 6d 65 3d 22 32 30   e"; filename="20
0000000050 32 32 30 35 32 36 31 32 33 38 35 34 31 31 32 2d   220526123854112-
0000000060 34 32 32 35 2d 31 33 2e 39 2e 34 2e 31 31 37 35   4225-13.9.4.1175
0000000070 2d 31 31 31 37 35 2d 63 6f 6d 2e 55 43 4d 6f 62   -11175-com.UCMob
0000000080 69 6c 65 2d 30 2d 6a 73 73 64 6b 69 64 78 2e 6c   ile-0-jssdkidx.l
0000000090 6f 67 22 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70   og"..Content-Typ
00000000a0 65 3a 20 61 70 70 6c 69 63 61 74 69 6f 6e 2f 6f   e: application/o
00000000b0 63 74 65 74 2d 73 74 72 65 61 6d 0d 0a 43 6f 6e   ctet-stream..Con
00000000c0 74 65 6e 74 2d 54 72 61 6e 73 66 65 72 2d 45 6e   tent-Transfer-En
00000000d0 63 6f 64 69 6e 67 3a 20 62 69 6e 61 72 79 0d 0a   coding: binary..
00000000e0 0d 0a 7c 47 75 d6 14 a4 15 67 78 e4 eb 17 ad 32   ..|Gu....gx....2
00000000f0 4a fd 3f 77 6a 31 d4 e7 c9 87 9f a5 71 4b 99 62   J.?wj1......qK.b
0000000100 03 e2 a6 29 81 ae ea be 55 ed c8 b3 10 01 1d 28   ...)....U......(
0000000110 23 c8 5d 1f 0d 27 61 51 03 7a 4e d5 d8 31 fd 77   #.]..'aQ.zN..1.w
0000000120 c1 c8 6d d6 58 e5 c7 77 83 5a bb a7 21 08 ab aa   ..m.X..w.Z..!...
0000000130 67 84 f7 7e 86 6f ca 48 d6 59 99 cd a1 ac 89 f0   g..~.o.H.Y......
0000000140 e6 bd 27 2d c4 8c 7c 7a cc 9a fd f7 e9 e4 25 e8   ..'-..|z......%.
0000000150 6b a4 6f 19 7d ca 22 5a 28 75 8f 6b 64 fe 79 63   k.o.}."Z(u.kd.yc
0000000160 d4 c4 24 df 97 2e 25 2b 6d fc 3f c9 33 be 95 c6   ..$...%+m.?.3...
0000000170 27 d5 d4 6b 8b b4 ba 7e 19 fc f0 cc 8e 30 51 08   '..k...~.....0Q.
0000000180 f7 9c cf 14 14 d8 e2 49 5c 28 47 aa 0f cd 53 48   .......I\(G...SH
0000000190 c1 7d b4 26 d8 19 c1 de fe 38 ba ac d0 65 85 3f   .}.&.....8...e.?
00000001a0 07 56 ad 33 84 5b de 21 82 64 58 28 3e 11 58 c2   .V.3.[.!.dX(>.X.
00000001b0 a9 bb 93 a5 94 60 49 cd 2d af b4 36 85 db ce 42   .....`I.-..6...B
00000001c0 99 11 39 bf f3 80 8e ab fb d3 39 18 1b d2 10 96   ..9.......9.....
00000001d0 f7 b5 cb e9 95 0a 64 e5 12 2b 95 a0 95 df 05 88   ......d..+......
00000001e0 a7 4d ec 8b 2f 80 db 7f 14 bf f9 b6 31 9f 4d fa   .M../.......1.M.
00000001f0 39 90 45 e3 8e 42 e1 d0 19 88 9c 86 54 7c 58 71   9.E..B......T|Xq
0000000200 41 7f 9f 78 c8 d3 14 29 58 00 b8 6a cb 2d 1d c6   A..x...)X..j.-..
0000000210 db 78 08 e2 6c d7 04 38 a3 b3 04 30 a9 52 db 9c   .x..l..8...0.R..
0000000220 94 22 95 c3 c2 22 dc 93 90 a1 12 c3 aa 51 86 4e   ."...".......Q.N
0000000230 81 b8 77 a8 1e a0 71 f2 5b 7e 24 28 31 49 00 85   ..w...q.[~$(1I..
0000000240 64 af f2 19 9e 76 c4 52 99 1d ce a2 d6 3d e2 21   d....v.R.....=.!
0000000250 bb 5f 2a 40 a6 33 74 96 98 49 b4 c5 b4 1f 18 ed   ._*@.3t..I......
0000000260 3d 79 08 b6 da 8a 7a 21 0a b8 c9 ab 0b 8c 8b d2   =y....z!........
0000000270 b5 7a a7 21 a8 0a 45 ed 35 c1 bd 92 54 fe d4 db   .z.!..E.5...T...
0000000280 ae 5c c4 dc c9 fe 4c 46 06 a2 17 29 22 02 b3 d8   .\....LF...)"...
0000000290 d8 42 93 25 68 63 a9 82 fb 40 d5 11 40 bd 6e 26   .B.%hc...@..@.n&
00000002a0 13 09 dc aa 3b ff 35 5f 4b a7 22 84 51 1d d0 c7   ....;.5_K.".Q...
00000002b0 0f 6f 6a 72 8a 19 3c 37 d5 d9 44 f5 45 de 43 1d   .ojr..<7..D.E.C.
00000002c0 a6 09 11 30 a1 98 83 f4 aa eb 10 58 b4 a2 51 99   ...0.......X..Q.
00000002d0 87 b3 0d 0a 2d 2d 54 68 6a 31 36 35 33 35 38 33   ....--Thj1653583
00000002e0 38 32 36 39 38 33 54 68 6a 2d 2d 0d 0a            826983Thj--..
~~~

We can see the name of the file in plaintext "filename=20220526123854112-4225-13.9.4.1175-11175-com.UCMobile-0-jssdkidx.log". This file contains the data collected while in incognito mode. The file is gziped and then AES encrypted. The following is the corresponding response to this request:
~~~
HTTP/1.1 200 OK
Date: Thu, 26 May 2022 16:58:35 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: close
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE
Content-Encoding: gzip
[decoded gzip] XML
  

{"cip":"69.113.233.231","msg":"成功","stm":1653584315,"code":0,"cver":1329}
~~~

The AES key is found in the APK of all versions we analyzed.

~~~java
if (!TextUtils.isEmpty("UCMobile")) {
	aHr.appId = "UCMobile";
	if (!TextUtils.isEmpty("Ine34@32b#jeRs2h")) {
		aHr.appSecret = "Ine34@32b#jeRs2h";
		a.C0154a aHq = aHr.aHq("13.9.6.1177");
~~~


Using [Frida-tools](https://frida.re/docs/android/) we found the IV and AES algorithm being used:

~~~
Creating AES secret key, plaintext:\n0000  49 6E 65 33 34 40 33 32 62 23 6A 65 52 73 32 68  Ine34@32b#jeRs2h
Performing encryption/decryption
Initialization Vector: \n0000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Algorithm: AES/CBC/PKCS5Padding
~~~

With this information we decrypted and gunziped the request to find the data being sent:
~~~
{"w_msg":"FlutterEngineConstructed","w_c1":"1","w_avgv1":"467","w_tm":"1653583133","w_succ":"1","w_bid":"ucfe","w_category":"100","ps":"com.UCMobile","pid":"7091","stime":"1653583084853","type":"jssdkidx","fr":"android","pkg":"com.UCMobile","vcode":"11175","dsp_w":"600","rom":"10","dsp_d":"100","uid":"Yo5ZzzBhUf0DAMaMYbLwrVuI","wid":"aae242b1-eddc-4881-bd18-5748d2f812a0","tmem":"7793","sdkver":"1.0.0.10","ctime":"1653583133","model":"Genymotion-'Phone'-version","lang":"en","dsp_dpi":"160","net":"wifi","brand":"google","dsp_h":"976","ver":"13.9.4.1175","product":"UCMobile","utdid":"Yo5ZzzBhUf0DAMaMYbLwrVuI","bsver":"ucrelease","bver":"13.9.4.1175","bserial":"220519170754","appid":"UCMobile","amem":"6062","sdk":"29","tzone":"America\/New_York"}
{"w_msg":"ExecuteDartEntrypoint","w_c1":"1","w_succ":"1","w_bid":"ucfe","w_category":"101","w_avgv1":"497","w_tm":"1653583133","ps":"com.UCMobile","pid":"7091","stime":"1653583084853","type":"jssdkidx","fr":"android","pkg":"com.UCMobile","vcode":"11175","dsp_w":"600","rom":"10","dsp_d":"100","uid":"Yo5ZzzBhUf0DAMaMYbLwrVuI","wid":"aae242b1-eddc-4881-bd18-5748d2f812a0","tmem":"7793","sdkver":"1.0.0.10","ctime":"1653583133","model":"Genymotion-'Phone'-version","lang":"en","dsp_dpi":"160","net":"wifi","brand":"google","dsp_h":"976","ver":"13.9.4.1175","product":"UCMobile","utdid":"Yo5ZzzBhUf0DAMaMYbLwrVuI","bsver":"ucrelease","bver":"13.9.4.1175","bserial":"220519170754","appid":"UCMobile","amem":"6061","sdk":"29","tzone":"America\/New_York"}
~~~

Use this [link](https://gchq.github.io/CyberChef/#recipe=From_Hexdump()Drop_bytes(0,226,false)Drop_bytes(0,-27,false)AES_Decrypt(%7B'option':'UTF8','string':'Ine34@32b%23jeRs2h'%7D,%7B'option':'Hex','string':'00%2000%2000%2000%2000%2000%2000%2000%2000%2000%2000%2000%2000%2000%2000%2000'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)Gunzip()&input=MDAwMDAwMDAwMCAyZCAyZCA1NCA2OCA2YSAzMSAzNiAzNSAzMyAzNSAzOCAzMyAzOCAzMiAzNiAzOSAgIC0tVGhqMTY1MzU4MzgyNjkKMDAwMDAwMDAxMCAzOCAzMyA1NCA2OCA2YSAwZCAwYSA0MyA2ZiA2ZSA3NCA2NSA2ZSA3NCAyZCA0NCAgIDgzVGhqLi5Db250ZW50LUQKMDAwMDAwMDAyMCA2OSA3MyA3MCA2ZiA3MyA2OSA3NCA2OSA2ZiA2ZSAzYSAyMCA2NiA2ZiA3MiA2ZCAgIGlzcG9zaXRpb246IGZvcm0KMDAwMDAwMDAzMCAyZCA2NCA2MSA3NCA2MSAzYiAyMCA2ZSA2MSA2ZCA2NSAzZCAyMiA2NiA2OSA2YyAgIC1kYXRhOyBuYW1lPSJmaWwKMDAwMDAwMDA0MCA2NSAyMiAzYiAyMCA2NiA2OSA2YyA2NSA2ZSA2MSA2ZCA2NSAzZCAyMiAzMiAzMCAgIGUiOyBmaWxlbmFtZT0iMjAKMDAwMDAwMDA1MCAzMiAzMiAzMCAzNSAzMiAzNiAzMSAzMiAzMyAzOCAzNSAzNCAzMSAzMSAzMiAyZCAgIDIyMDUyNjEyMzg1NDExMi0KMDAwMDAwMDA2MCAzNCAzMiAzMiAzNSAyZCAzMSAzMyAyZSAzOSAyZSAzNCAyZSAzMSAzMSAzNyAzNSAgIDQyMjUtMTMuOS40LjExNzUKMDAwMDAwMDA3MCAyZCAzMSAzMSAzMSAzNyAzNSAyZCA2MyA2ZiA2ZCAyZSA1NSA0MyA0ZCA2ZiA2MiAgIC0xMTE3NS1jb20uVUNNb2IKMDAwMDAwMDA4MCA2OSA2YyA2NSAyZCAzMCAyZCA2YSA3MyA3MyA2NCA2YiA2OSA2NCA3OCAyZSA2YyAgIGlsZS0wLWpzc2RraWR4LmwKMDAwMDAwMDA5MCA2ZiA2NyAyMiAwZCAwYSA0MyA2ZiA2ZSA3NCA2NSA2ZSA3NCAyZCA1NCA3OSA3MCAgIG9nIi4uQ29udGVudC1UeXAKMDAwMDAwMDBhMCA2NSAzYSAyMCA2MSA3MCA3MCA2YyA2OSA2MyA2MSA3NCA2OSA2ZiA2ZSAyZiA2ZiAgIGU6IGFwcGxpY2F0aW9uL28KMDAwMDAwMDBiMCA2MyA3NCA2NSA3NCAyZCA3MyA3NCA3MiA2NSA2MSA2ZCAwZCAwYSA0MyA2ZiA2ZSAgIGN0ZXQtc3RyZWFtLi5Db24KMDAwMDAwMDBjMCA3NCA2NSA2ZSA3NCAyZCA1NCA3MiA2MSA2ZSA3MyA2NiA2NSA3MiAyZCA0NSA2ZSAgIHRlbnQtVHJhbnNmZXItRW4KMDAwMDAwMDBkMCA2MyA2ZiA2NCA2OSA2ZSA2NyAzYSAyMCA2MiA2OSA2ZSA2MSA3MiA3OSAwZCAwYSAgIGNvZGluZzogYmluYXJ5Li4KMDAwMDAwMDBlMCAwZCAwYSA3YyA0NyA3NSBkNiAxNCBhNCAxNSA2NyA3OCBlNCBlYiAxNyBhZCAzMiAgIC4ufEd1Li4uLmd4Li4uLjIKMDAwMDAwMDBmMCA0YSBmZCAzZiA3NyA2YSAzMSBkNCBlNyBjOSA4NyA5ZiBhNSA3MSA0YiA5OSA2MiAgIEouP3dqMS4uLi4uLnFLLmIKMDAwMDAwMDEwMCAwMyBlMiBhNiAyOSA4MSBhZSBlYSBiZSA1NSBlZCBjOCBiMyAxMCAwMSAxZCAyOCAgIC4uLikuLi4uVS4uLi4uLigKMDAwMDAwMDExMCAyMyBjOCA1ZCAxZiAwZCAyNyA2MSA1MSAwMyA3YSA0ZSBkNSBkOCAzMSBmZCA3NyAgICMuXS4uJ2FRLnpOLi4xLncKMDAwMDAwMDEyMCBjMSBjOCA2ZCBkNiA1OCBlNSBjNyA3NyA4MyA1YSBiYiBhNyAyMSAwOCBhYiBhYSAgIC4ubS5YLi53LlouLiEuLi4KMDAwMDAwMDEzMCA2NyA4NCBmNyA3ZSA4NiA2ZiBjYSA0OCBkNiA1OSA5OSBjZCBhMSBhYyA4OSBmMCAgIGcuLn4uby5ILlkuLi4uLi4KMDAwMDAwMDE0MCBlNiBiZCAyNyAyZCBjNCA4YyA3YyA3YSBjYyA5YSBmZCBmNyBlOSBlNCAyNSBlOCAgIC4uJy0uLnx6Li4uLi4uJS4KMDAwMDAwMDE1MCA2YiBhNCA2ZiAxOSA3ZCBjYSAyMiA1YSAyOCA3NSA4ZiA2YiA2NCBmZSA3OSA2MyAgIGsuby59LiJaKHUua2QueWMKMDAwMDAwMDE2MCBkNCBjNCAyNCBkZiA5NyAyZSAyNSAyYiA2ZCBmYyAzZiBjOSAzMyBiZSA5NSBjNiAgIC4uJC4uLiUrbS4/LjMuLi4KMDAwMDAwMDE3MCAyNyBkNSBkNCA2YiA4YiBiNCBiYSA3ZSAxOSBmYyBmMCBjYyA4ZSAzMCA1MSAwOCAgICcuLmsuLi5%2BLi4uLi4wUS4KMDAwMDAwMDE4MCBmNyA5YyBjZiAxNCAxNCBkOCBlMiA0OSA1YyAyOCA0NyBhYSAwZiBjZCA1MyA0OCAgIC4uLi4uLi5JXChHLi4uU0gKMDAwMDAwMDE5MCBjMSA3ZCBiNCAyNiBkOCAxOSBjMSBkZSBmZSAzOCBiYSBhYyBkMCA2NSA4NSAzZiAgIC59LiYuLi4uLjguLi5lLj8KMDAwMDAwMDFhMCAwNyA1NiBhZCAzMyA4NCA1YiBkZSAyMSA4MiA2NCA1OCAyOCAzZSAxMSA1OCBjMiAgIC5WLjMuWy4hLmRYKD4uWC4KMDAwMDAwMDFiMCBhOSBiYiA5MyBhNSA5NCA2MCA0OSBjZCAyZCBhZiBiNCAzNiA4NSBkYiBjZSA0MiAgIC4uLi4uYEkuLS4uNi4uLkIKMDAwMDAwMDFjMCA5OSAxMSAzOSBiZiBmMyA4MCA4ZSBhYiBmYiBkMyAzOSAxOCAxYiBkMiAxMCA5NiAgIC4uOS4uLi4uLi45Li4uLi4KMDAwMDAwMDFkMCBmNyBiNSBjYiBlOSA5NSAwYSA2NCBlNSAxMiAyYiA5NSBhMCA5NSBkZiAwNSA4OCAgIC4uLi4uLmQuLisuLi4uLi4KMDAwMDAwMDFlMCBhNyA0ZCBlYyA4YiAyZiA4MCBkYiA3ZiAxNCBiZiBmOSBiNiAzMSA5ZiA0ZCBmYSAgIC5NLi4vLi4uLi4uLjEuTS4KMDAwMDAwMDFmMCAzOSA5MCA0NSBlMyA4ZSA0MiBlMSBkMCAxOSA4OCA5YyA4NiA1NCA3YyA1OCA3MSAgIDkuRS4uQi4uLi4uLlR8WHEKMDAwMDAwMDIwMCA0MSA3ZiA5ZiA3OCBjOCBkMyAxNCAyOSA1OCAwMCBiOCA2YSBjYiAyZCAxZCBjNiAgIEEuLnguLi4pWC4uai4tLi4KMDAwMDAwMDIxMCBkYiA3OCAwOCBlMiA2YyBkNyAwNCAzOCBhMyBiMyAwNCAzMCBhOSA1MiBkYiA5YyAgIC54Li5sLi44Li4uMC5SLi4KMDAwMDAwMDIyMCA5NCAyMiA5NSBjMyBjMiAyMiBkYyA5MyA5MCBhMSAxMiBjMyBhYSA1MSA4NiA0ZSAgIC4iLi4uIi4uLi4uLi5RLk4KMDAwMDAwMDIzMCA4MSBiOCA3NyBhOCAxZSBhMCA3MSBmMiA1YiA3ZSAyNCAyOCAzMSA0OSAwMCA4NSAgIC4udy4uLnEuW34kKDFJLi4KMDAwMDAwMDI0MCA2NCBhZiBmMiAxOSA5ZSA3NiBjNCA1MiA5OSAxZCBjZSBhMiBkNiAzZCBlMiAyMSAgIGQuLi4udi5SLi4uLi49LiEKMDAwMDAwMDI1MCBiYiA1ZiAyYSA0MCBhNiAzMyA3NCA5NiA5OCA0OSBiNCBjNSBiNCAxZiAxOCBlZCAgIC5fKkAuM3QuLkkuLi4uLi4KMDAwMDAwMDI2MCAzZCA3OSAwOCBiNiBkYSA4YSA3YSAyMSAwYSBiOCBjOSBhYiAwYiA4YyA4YiBkMiAgID15Li4uLnohLi4uLi4uLi4KMDAwMDAwMDI3MCBiNSA3YSBhNyAyMSBhOCAwYSA0NSBlZCAzNSBjMSBiZCA5MiA1NCBmZSBkNCBkYiAgIC56LiEuLkUuNS4uLlQuLi4KMDAwMDAwMDI4MCBhZSA1YyBjNCBkYyBjOSBmZSA0YyA0NiAwNiBhMiAxNyAyOSAyMiAwMiBiMyBkOCAgIC5cLi4uLkxGLi4uKSIuLi4KMDAwMDAwMDI5MCBkOCA0MiA5MyAyNSA2OCA2MyBhOSA4MiBmYiA0MCBkNSAxMSA0MCBiZCA2ZSAyNiAgIC5CLiVoYy4uLkAuLkAubiYKMDAwMDAwMDJhMCAxMyAwOSBkYyBhYSAzYiBmZiAzNSA1ZiA0YiBhNyAyMiA4NCA1MSAxZCBkMCBjNyAgIC4uLi47LjVfSy4iLlEuLi4KMDAwMDAwMDJiMCAwZiA2ZiA2YSA3MiA4YSAxOSAzYyAzNyBkNSBkOSA0NCBmNSA0NSBkZSA0MyAxZCAgIC5vanIuLjw3Li5ELkUuQy4KMDAwMDAwMDJjMCBhNiAwOSAxMSAzMCBhMSA5OCA4MyBmNCBhYSBlYiAxMCA1OCBiNCBhMiA1MSA5OSAgIC4uLjAuLi4uLi4uWC4uUS4KMDAwMDAwMDJkMCA4NyBiMyAwZCAwYSAyZCAyZCA1NCA2OCA2YSAzMSAzNiAzNSAzMyAzNSAzOCAzMyAgIC4uLi4tLVRoajE2NTM1ODMKMDAwMDAwMDJlMCAzOCAzMiAzNiAzOSAzOCAzMyA1NCA2OCA2YSAyZCAyZCAwZCAwYSAgICAgICAgICAgIDgyNjk4M1Roai0tLi4)
 for the decryption algorithm to decrypt the request.
 
None of the URL's visted nor the IP of the user are being sent in files of this
type. However the identifier "wid":"aae242b1-eddc-4881-bd18-5748d2f812a0" seems
to stay constant through a sesion. For us a session ends when the phone is
rebooted.
 
Other Files Being Sent
------------

We found 7 more different kinds of files being encrypted and sent to px.ucweb.com/v1/crash/upload. The type of each file, categorized by UC Browser in the APK, are the following:
~~~
"api", "fluerr", "jssdkidx", "pvuv", "t1t3detail", "jserr", "bkpg".
~~~

Every file contains different information, the data that is common to all of them is given in the following table:

| Data Found in all Files | 
| --------------- | 
|"ps":"com.UCMobile" | 
|"pid":"7091" | 
|"stime":"1653583084853"  |
|"type":"jssdkidx" or "type":"pvuv" or "type":"api" or "type":"fluerr" | 
|"w_bid":"ucfe"  | 
|"fr":"android"  | 
|"dsp_w":600  | 
|"vcode":"11175"  | 
|"uid":"Yo5ZzzBhUf0DAMaMYbLwrVuI"  | 
|"rom":"10"  |  |
|"wid":"aae242b1-eddc-4881-bd18-5748d2f812a0"  | 
|"model":"Genymotion-'Phone'-version"  | 
|"lang":"en"  | 
|"net":"wifi"  | 
|"brand":"google" | 
|"dsp_h":"976"  | 
|"w_url":"https:\/\/www.amazon.cn\/"  | 
|"product":"UCMobile"  | 
|"ver":"13.9.4.1175"  |
|"bsver":"ucrelease"  | 
|"bver":"13.9.4.1175"  | 
|"bserial":"220519170754" | 
|"build_model":"Genymotion 'Phone' version"  | 
|"tzone" :"America\/New_York" | 
|"crserial":"220517150500" |

Notice that the values in this table are taken from a specific file in a request we captured.

Interestingly, these files do contain URL's visited during an incognito
session. They containt UC Browser's `uid` that was identified by past reverse engineering efforts as a persistent ID and is described in more detail below.  They also contain the identifier
"wid":"aae242b1-eddc-4881-bd18-5748d2f812a0" which seems to stay constant
throughout a sedsion. None of the files were found to contain the IP address of
the user, but IP addresses can easily be extracted from the unencrypted packet
headers. These files are sent to px.ucweb.com/v1/crash/upload even if a proxy
is detected.

Here is an example of one of these requests: 
~~~
POST https://px.ucweb.com/api/v1/raw/upload HTTP/1.1
wpk-header: app%3DUCMobile%26cp%3Dgzip%26cver%3D1329%26de%3D3%26os%3Dandroid%26sd%3DMaWvGVmYtTxGBV9qn0sUf5ctAGNtVeNM3RABjiDn3GleTB8wxwnKKxYJcb_-cpqo%26seq%3D16536704404051047%26sver%3D1329%26tm%3D1653670440%26type%3Dpvuv%26ver%3D13.9.4.1175%26sign%3D5fc086acb3753d413015e0a0320073e5
Connection: close
Content-Type: multipart/form-data;boundary=----WebKitFormBoundaryP0Rfzlf32iRoMhmb
User-Agent: Dalvik/2.1.0 (Linux; U; Android 10; Genymotion 'Phone' version Build/QQ1D.200105.002)
Host: px.ucweb.com
Accept-Encoding: gzip
Content-Length: 842
Hex
  

0000000000 2d 2d 2d 2d 2d 2d 57 65 62 4b 69 74 46 6f 72 6d   ------WebKitForm
0000000010 42 6f 75 6e 64 61 72 79 50 30 52 66 7a 6c 66 33   BoundaryP0Rfzlf3
0000000020 32 69 52 6f 4d 68 6d 62 0d 0a 43 6f 6e 74 65 6e   2iRoMhmb..Conten
0000000030 74 2d 44 69 73 70 6f 73 69 74 69 6f 6e 3a 20 66   t-Disposition: f
0000000040 6f 72 6d 2d 64 61 74 61 3b 6e 61 6d 65 3d 22 66   orm-data;name="f
0000000050 69 6c 65 22 3b 66 69 6c 65 6e 61 6d 65 3d 22 70   ile";filename="p
0000000060 76 75 76 5f 67 7a 69 70 5f 33 5f 31 5f 32 32 35   vuv_gzip_3_1_225
0000000070 31 37 5f 31 30 36 37 5f 31 36 35 33 36 37 30 34   17_1067_16536704
0000000080 34 30 30 32 35 22 0d 0a 0d 0a 00 03 7d 77 e9 f4   40025"......}w..
0000000090 9b 08 78 58 55 fa cb 81 49 61 44 db b3 11 0f 33   ..xXU...IaD....3
00000000a0 44 0c 32 22 10 23 9a 8b 73 4e 79 d5 14 5a 5c 40   D.2".#..sNy..Z\@
00000000b0 57 89 03 67 1e 43 57 a1 62 3a 16 4c f1 0c f4 32   W..g.CW.b:.L...2
00000000c0 f9 3f 90 46 fb 78 b4 16 89 dd d0 c7 01 99 d5 96   .?.F.x..........
00000000d0 e3 3d 0b 37 e2 ee f5 f3 d4 03 f9 ec 35 cb 86 32   .=.7........5..2
00000000e0 12 62 2f d9 20 20 2d 64 e5 ff 91 f5 f2 bb 10 95   .b/.  -d........
00000000f0 64 91 70 93 ed 7e 93 f8 cf 5c dd a4 d4 dd c8 e7   d.p..~...\......
0000000100 df b8 9c 71 47 bf f9 df 87 46 81 82 a9 34 01 ac   ...qG....F...4..
0000000110 4f c7 62 25 af 4a 5e 41 c1 e1 99 2d f9 2f f8 4a   O.b%.J^A...-./.J
0000000120 77 4c 9b 38 b1 c4 05 46 09 4e 01 e7 86 5f 07 48   wL.8...F.N..._.H
0000000130 29 a0 06 a3 7c ec bc e9 7c f5 8d b1 42 1c 1f dc   )...|...|...B...
0000000140 7d b9 d6 92 e6 fb 49 06 66 7a 4f f7 c0 82 3e 47   }.....I.fzO...>G
0000000150 0d 19 92 a5 9a 27 ee 40 2d 10 5c 24 28 13 fc 23   .....'.@-.\$(..#
0000000160 5f ef 57 83 58 1a 1a 2a ae 1b e7 f6 bc e0 03 5f   _.W.X..*......._
0000000170 99 f3 fc 9d b3 ae 14 32 91 62 a5 26 7c f4 ab 18   .......2.b.&|...
0000000180 c7 4c c0 76 40 d3 a2 fc c0 b9 3f ce 7d 34 6c 1a   .L.v@.....?.}4l.
0000000190 0b c2 24 2b a8 e8 ec 8a b8 16 34 13 71 d9 af 23   ..$+......4.q..#
00000001a0 4e e3 5f 12 4e d0 81 7b 48 c2 a5 61 46 c5 74 72   N._.N..{H..aF.tr
00000001b0 08 f5 c1 29 2a 78 a3 82 74 d2 25 1f 61 16 54 98   ...)*x..t.%.a.T.
00000001c0 60 87 f5 5e b0 c4 e0 7e d2 74 b1 3f 74 69 4a 1f   `..^...~.t.?tiJ.
00000001d0 64 75 7e da 4a 71 b0 4e a8 e8 d1 c3 94 44 56 f9   du~.Jq.N.....DV.
00000001e0 9d f8 f2 ab 46 ab 23 e2 85 85 9c 32 f5 f1 92 a2   ....F.#....2....
00000001f0 27 20 74 b1 fd 83 9e 37 8f f9 15 8d 7e b1 f0 9a   ' t....7....~...
0000000200 0b 90 82 84 b3 17 6e 45 f3 89 dc a6 9c cd 67 f9   ......nE......g.
0000000210 96 1e 11 88 e6 82 ca 84 af e9 c2 a0 3e 02 a3 9f   ............>...
0000000220 5e 42 8d b2 f5 f0 59 30 79 4a ca a2 8a 17 14 3d   ^B....Y0yJ.....=
0000000230 01 25 02 43 f8 a2 17 54 88 30 94 f2 8c df d1 d2   .%.C...T.0......
0000000240 da 6e 2d c8 59 58 76 e6 4e 38 f6 b8 9c d0 6b b7   .n-.YXv.N8....k.
0000000250 11 3f ed bb 1d ba c2 9d 01 f2 e0 45 46 63 b5 bb   .?.........EFc..
0000000260 76 d9 08 4d e7 26 8c 53 97 d8 50 92 46 31 e4 2a   v..M.&.S..P.F1.*
0000000270 ef e5 b7 23 4a 7d 35 66 5c ab c1 d6 6c 99 77 41   ...#J}5f\...l.wA
0000000280 7c c3 4c d9 40 c3 c3 37 a3 5e 3f 89 f1 af 2e fa   |.L.@..7.^?.....
0000000290 bf 4c 8e 53 73 4b 84 86 c5 fc 1e 04 70 8b b8 45   .L.SsK......p..E
00000002a0 da c1 04 ba 51 b2 c1 6e 0a f0 78 89 23 37 1e b2   ....Q..n..x.#7..
00000002b0 89 b9 13 a1 d9 03 7c 4f 73 28 12 e0 71 21 d5 a3   ......|Os(..q!..
00000002c0 3e ba 9e 2b cf 59 c7 20 cb ee f6 33 49 b5 57 bc   >..+.Y. ...3I.W.
00000002d0 44 f0 68 8c c3 07 9e 7a 1b 91 c8 37 5e 5a fb af   D.h....z...7^Z..
00000002e0 3d 49 9b 53 01 62 e0 0e b8 1c 50 a9 36 ca 51 aa   =I.S.b....P.6.Q.
00000002f0 ed 32 9b 4d 94 8a a7 58 c4 7d d7 b4 0e 4c 17 e6   .2.M...X.}...L..
0000000300 11 09 84 92 30 08 6d e9 9e 25 e5 49 d6 8c f6 04   ....0.m..%.I....
0000000310 fb 65 74 19 55 fc c4 ba 0e 11 44 03 0d 0a 2d 2d   .et.U.....D...--
0000000320 2d 2d 2d 2d 57 65 62 4b 69 74 46 6f 72 6d 42 6f   ----WebKitFormBo
0000000330 75 6e 64 61 72 79 50 30 52 66 7a 6c 66 33 32 69   undaryP0Rfzlf32i
0000000340 52 6f 4d 68 6d 62 2d 2d 0d 0a                     RoMhmb--..
~~~

This request contains data corresponding to the file type "puvv". The following is the response to this request:
~~~
HTTP/1.1 200 OK
Date: Fri, 27 May 2022 17:53:37 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: close
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE
Content-Encoding: gzip
[decoded gzip] XML
  

{"cip":"69.113.233.231","msg":"成功","stm":1653674017,"code":0,"cver":1329}
~~~


Using Frida tools we found the plaintext corresponding to the data being sent on these files. For the above request, the following is the corresponding data being sent:
~~~
{"ps":"com.UCMobile","pid":22517,"stime":1653670416721,"type":"pvuv","w_bid":"u4_default","fr":"android","pkg":"com.UCMobile","dsp_w":600,"vcode":11175,"uid":"Yo5ZzzBhUf0DAMaMYbLwrVuI","rom":"10","wid":"4eb70d2e-198b-4dd2-b8ef-28900f28aed6","ctime":1653670453,"model":"genymotion-'phone'-version","lang":"en","net":"wifi","brand":"google","dsp_h":976,"w_url":"https:\/\/www.amazon.cn\/","product":"UCMobile","ver":"13.9.4.1175","utdid":"Yo5ZzzBhUf0DAMaMYbLwrVuI","bsver":"ucrelease","bver":"13.9.4.1175","bserial":"220519170754","build_model":"Genymotion 'Phone' version","w_tm":1653670453,"appid":"UCMobile","sdk":29,"tzone":"America\/New_York","crver":"4.29.0.0","sdk_ver":"1.5.1","crserial":"220517150500"}
~~~

Notice that it contains the URL of the website we visited while in incognito mode "w_url":"https:\/\/www.amazon.cn\/". It does not contain the IP of the client.


UC Browser's `uid` to identify the user
------------------
We statically analyzed the Chinese version of UC Browser, version 13.9.4.1175, to determine how the `uid` field seen multiple times above is populated.  The following Java code indicates that the `uid` field is a user-specific identifier.

~~~java
    public final synchronized com.uc.browser.service.b.b ctr() {
        String str;
        String str2;
        List<f> cye = cye();
        f fVar = null;
        if (cye != null && cye.size() > 0) {
            if (cye.size() > 0) {
                fVar = cye.get(0);
            }
            long j = -1;
            for (int i = 0; i < cye.size(); i++) {
                if (cye.get(i).nFD > j) {
                    long j2 = cye.get(i).nFD;
                    fVar = cye.get(i);
                    j = j2;
                }
            }
            StringBuilder sb = new StringBuilder("[Thread:");
            sb.append(Thread.currentThread().getName());
            sb.append("] ");
            if (fVar == null) {
                str = "not";
            } else {
                str = "";
            }
            sb.append(str);
            sb.append("found user(UserID:");
            if (fVar == null) {
                str2 = "";
            } else {
                str2 = fVar.nFz;
            }
            sb.append(str2);
            sb.append("),lastLoginTime:");
            sb.append(j);
            com.uc.util.base.j.b.d("AccountDataHelper", sb.toString());
            return b(fVar);
        }
        return null;
    }
~~~
