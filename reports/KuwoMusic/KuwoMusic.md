Kuwo Music
============

A free music streaming application developed by Beijing Kuwo Technology.

We analyzed version 10.1.2.6 from the Tencent app store.


App description
------------

Kuwo Music is a popular music streaming service that provides millions of
Chinese songs in high quality.  This app has more than [129 million monthly
active users](https://musicinfo.io/streaming-services/).

Tencent Music [bought a majority
stake](https://www.techinasia.com/chinas-massive-music-streaming-industry-differs-spotify)
in China Music Corp, which operated Kugou and Kuwo. According to Music Business
Worldwide, Tencent Music doesn't actually own any of the music services it
operates: QQ Music, Kugou, Kuwo and WeSing. Instead, [Tencent Music has
effective operational
control](https://www.musicbusinessworldwide.com/tencent-music-isnt-actually-a-chinese-company-why-should-the-global-music-business-care/)
over the services and the ability to consolidate their financial statements,
but does not give Tencent Music's shareholders any voting rights.

According to their [website](https://jx.kuwo.cn/ether/jx_about_us.html), Kuwo Juxing is a large-scale online live broadcast platform jointly created by Kuwo Music in 2016. Kuwo Juxing [can be accessed from the Kuwo Music application](https://inf.news/en/tech/fac70513758ead527409a48dae7cd778.html), this is done by Kuwo Music downloading and installing Kuwo Juxing's APK.

Unencrypted PII (Personally Identifiable Information)
------------

We found that Kuwo creates identifiers to uniquely identify users and their
devices and sends these identifiers over plaintext HTTP as the user uses the
app.

Upon installation, Kuwo creates two files in a folder called `.setting`:
`device_id.text` to serve as a substitute if the IMEI is unavailable and
`uid.text` to identify the user.  Along with other identifying information, these are included in reports on the user's use of the app that are periodically uploaded to an HTTP server:

~~~java
    private StringBuilder a(String str, String str2, String str3, int i) {
        if (TextUtils.isEmpty(str) || TextUtils.isEmpty(str2)) {
            return null;
        }
        if (str3 == null) {
            str3 = "";
        }
        String format = this.f2788f.format(new Date());
        boolean a2 = cn.kuwo.base.config.c.a(cn.kuwo.base.config.b.f2335d, cn.kuwo.base.config.b.bY, false);
        String a3 = cn.kuwo.base.config.c.a(cn.kuwo.base.config.b.f2338f, cn.kuwo.base.config.b.sI, cn.kuwo.base.config.b.sJ);
        StringBuilder sb = new StringBuilder(4096);
        sb.append("2%09<SRC:");
        sb.append(cn.kuwo.base.utils.b.f4195c);
        sb.append(LogDef.f2713a);
        sb.append(str);
        sb.append("|PROD:");
        sb.append("kwplayer");
        sb.append("|VER:");
        sb.append(cn.kuwo.base.utils.b.f4194b);
        sb.append("|VER_CODE:");
        sb.append(10130);
        sb.append("|PLAT:");
        sb.append("ar");
        sb.append("|ABI:");
        sb.append(cn.kuwo.base.utils.b.f4198f);
        sb.append("|FROM:");
        sb.append(cn.kuwo.base.utils.b.f4197e);
        sb.append("|OLDFROM:");
        sb.append(cn.kuwo.base.utils.b.g);
        sb.append("|{");
        sb.append(cn.kuwo.base.utils.b.f4197e);
        sb.append("}");
        sb.append("|ERR:");
        sb.append(str2);
        sb.append("|SUBERR:");
        sb.append(i);
        sb.append("|UI:");
        sb.append(cn.kuwo.base.config.c.a("", cn.kuwo.base.config.b.bb, "0"));
        sb.append("|VIP_TYPE:");
        sb.append(SpecialInfoUtil.w());
        sb.append("|HARDWARE_ID:");
        sb.append(cn.kuwo.base.utils.j.f());
        sb.append("|HarmonyOS:");
        sb.append(av.i());
        sb.append("|DEVID:");
        sb.append(cn.kuwo.base.utils.j.f4438c);
        sb.append("|ANDROID_ID:");
        sb.append(cn.kuwo.base.utils.j.g());
        sb.append("|OAID:");
        sb.append(cn.kuwo.base.utils.j.b());
        sb.append("|U:");
        sb.append(cn.kuwo.base.utils.b.g());
        sb.append("|IMEI:");
        sb.append(cn.kuwo.base.utils.j.f4438c);
        sb.append("|UUID:");
        sb.append(cn.kuwo.base.utils.j.f4438c);
        sb.append("|Q36:");
        sb.append(a3);
        sb.append("|DEV:");
        sb.append(Build.MANUFACTURER);
        sb.append(" ");
        sb.append(Build.MODEL);
        sb.append(" ");
        sb.append(Build.DEVICE);
        sb.append("|OSV:");
        sb.append(Build.VERSION.RELEASE);
        sb.append("|NE:");
        sb.append(NetworkStateUtil.i());
        sb.append("|NET_AVALIABLE:");
        sb.append(NetworkStateUtil.a());
        sb.append("|NE_TYPE:");
        sb.append(NetworkStateUtil.i());
        sb.append("|PRIVACY_AGREED:");
        sb.append(AppPrivacyPolicy.isPrivacyPolicyAgreed());
        sb.append("|WIFI_ONLY:");
        sb.append(cn.kuwo.base.config.c.a("", cn.kuwo.base.config.b.fm, false));
        sb.append("|CT:");
        sb.append(format);
        sb.append("|CIP:");
        sb.append(cn.kuwo.base.utils.b.I);
        sb.append("|LSTYPE:");
        sb.append("kwplayer");
        sb.append("|PU:");
        sb.append(cn.kuwo.base.utils.b.g());
        if (g.a()) {
            sb.append("|DEP:1");
        }
        sb.append("|MEM:");
        sb.append(cn.kuwo.base.utils.j.n());
        sb.append("|OFFLN:");
        sb.append(0);
        sb.append("|UNICOMFLOW:");
        sb.append(KwFlowManager.getInstance(App.a()).isProxyUser() ? 1 : 0);
        sb.append("|PROJECT:");
        sb.append(KwFlowManager.getInstance(App.a()).isProxying() ? 1 : 0);
        sb.append("|LOC:");
        ad.a b2 = ad.b((Context) null);
        if (b2 != null) {
            sb.append(b2.f4038a);
            sb.append(";");
            sb.append(b2.f4039b);
        } else {
            sb.append("unknown");
        }
        sb.append("|GPS:");
        ad.a a4 = ad.a((Context) null);
        if (a4 != null) {
            sb.append(a4.f4038a);
            sb.append(";");
            sb.append(a4.f4039b);
        } else {
            sb.append("0;0");
        }
        sb.append("|DBG:");
        sb.append(a2 ? 1 : 0);
        if (!TextUtils.isEmpty(str3)) {
            sb.append("|");
            sb.append(str3.replace("\n", "@"));
        }
        sb.append(Operators.G);
        return sb;
    }
~~~

An example of such a report is here:

~~~
2%09<SRC:kwplayer_ar_10.1.2.6|ACT:HTTPS_REQUEST|PROD:kwplayer|VER:10.1.2.6|VER_CODE:10126|PLAT:ar|ABI:armeabi|FROM:kwplayer_ar_10.1.2.6_qq.apk|OLDFROM:kwplayer_ar_10.1.2.6_qq.apk|{kwplayer_ar_10.1.2.6_qq.apk}|ERR:HTTPS_REQUEST|SUBERR:0|UI:0|VIP_TYPE:0|HARDWARE_ID:89f0fc7642df85b31bcb0d21602af669|HarmonyOS:false|DEVID:638c10470c965b16|ANDROID_ID:638c10470c965b16|OAID:|U:2474088579|IMEI:638c10470c965b16|UUID:638c10470c965b16|Q36:f785081a374970bf718ea19810001cf16503|DEV:motorola moto g(7) plus lake_n|OSV:10|NE:WIFI|NET_AVALIABLE:true|NE_TYPE:WIFI|PRIVACY_AGREED:true|WIFI_ONLY:false|CT:2022/06/01 13:46:05.306 -0700|CIP:|LSTYPE:kwplayer|PU:2474088579|DEP:1|MEM:3927642112|OFFLN:0|UNICOMFLOW:0|PROJECT:0|LOC:unknown|GPS:0;0|DBG:0|HTTPS_RESULT:false>
~~~

The "638c10470c965b16" used for `DEVID`, `ANDROID_ID`, `IMEI`, and `UUID` is
from the aforementioned `device_id.text`, while the "2474088579" for `U` and
`PU` comes from the aformentioned `uid.text`.  Analysis of the code reveals
that if the app is running in an Android environment that allows actual
collection of information like the phone number, IMEI, etc. then those PII are
included instead of the ID numbers generated on the app's first execution.

The `HARDWARE_ID` is generated by taking an MD5 cryptographic digest of some fields from the class `android.os.Build`:

~~~java
B = MD5(Build.ID + Build.FINGERPRINT + Build.HARDWARE + Build.BOARD + Build.BRAND + Build.DEVICE + Build.HOST + Build.MANUFACTURER + Build.MODEL + Build.DISPLAY + Build.PRODUCT + Build.TAGS + Build.TYPE + Build.USER);
~~~

Once a report is generated, which happens essentially at least once a minute
every time the user is engaging with the app, the report is base 64 encoded and
sent over plain HTTP to `log.kuwo.cn`.  This domain has a TTL of 120 seconds
(relevant because attacks to collect PII may be combined with DNS poisoning),
and resolves to IP addresses in the `175.102.178.0/24` range, which is located
inside China.

The following Linux command serves as a proof of concept for how the reports
can be viewed by a gateway router or any in- or on-path attacker (in this case
a Linux-based WiFi access point, where the interface passed as the `-i` option is the WiFi interface that the phone connects to).

```bash
sudo tcpflow -c -i <<your_interface_here>> | strings -n 80 | grep -o "MiUwOTxTUkM6a3dw.*==" | while read line; do echo ""; echo -n "------------"; date | tr -d '\n'; echo "------------"; echo $line | base64 -d -; done | tee kuwo.txt
```

[Example output is here.](kuwo.txt)

On Debian distributions, tcpflow can be installed with `sudo apt install
tcpflow`.

As the user uses different parts of the app, they are eventually prompted for
permission for the app to access their location.  After this the GPS field will
be populated with their GPS coordinates.  [Here is a pcap showing this
behavior.](kuwowithgps.pcap).  The CIP field is also sometimes populated with
the client's IP address, but we have been unable to reproduce this behavior
consistently.  To some extent it's moot because the client's current IP will be
in the packet headers of the unencrypted connection, but if the app retains the
client IP informaiton and does not update it when the client, e.g., connects to
a VPN then that mmight have implications.

A slight modification to the comman above will enable tcpflow to process the above pcap:

```bash
tcpflow -c -r kuwowithgps.pcap | strings -n 80 | grep -o "MiUwOTxTUkM6a3dw.*==" | while read line; do echo ""; echo -n "------------"; date | tr -d '\n'; echo "------------"; echo $line | base64 -d -; done | tee kuwo.txt
```

