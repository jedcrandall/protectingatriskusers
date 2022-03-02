# Angelica

An app downloaded from anzhi.com was found to filter sensitive words.  The app is available here:

[http://www.anzhi.com/pkg/7456_com.qingtime.baoku.html](http://www.anzhi.com/pkg/7456_com.qingtime.baoku.html)

The SHA-256 digest of the *.apk file analyzed is:

8e9ddafcc717902f1c77c7ebf262ca27aaf0a2e41758377497076367200dbcda

com.qingtime.icare.member.control.SensitiveWordFiltering.FinderUtil

## App description

Copied from anzhi.com and translated with Google Translate: "Angelica uses
modern technology to organize genealogy, local chronicles and historical
archives to form a vast humanistic knowledge map. Everyone will benefit from
it, explore their own family tree in the most elegant way, explore the
humanistic memory related to themselves, find their own position and story in
the vast history, let human beings be linked in a more loving way, and let
everyone Individuals can better retain their digital assets and realize the
ultimate concern of human beings."

## What keywords are filtered?

The list of filtered keywords is included as a plain text asset, so is easy to extract.  The complete list is [here](sensitivewords.txt) and English translations via Google Translate are [here](sensitivewords-english.txt).

## How is the keyword list updated, if at all?

No evidence was found that the keyword list is dynamically updated.  The
asset could be updated whenever the app is updated, but the filtering logic
was analyzed and there does not appear to be any place where keywords are added
other than using the resource.

The following is the source code where the asset with sensitive keywords is loaded into the module used for filtering, and is the only place where the routines to update the list of filtered words were found to occur:

```java
public static String[] readSensitiveWordFile(Context context) throws Exception {
        InputStreamReader inputStreamReader = new InputStreamReader(context.getResources().getAssets().open("sensitivewords.txt"), "UTF-8");
        try {
            HashSet hashSet = new HashSet();
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            while (true) {
                String readLine = bufferedReader.readLine();
                if (readLine != null) {
                    hashSet.add(readLine);
                } else {
                    String[] strArr = new String[hashSet.size()];
                    hashSet.toArray(strArr);
                    inputStreamReader.close();
                    StringBuilder stringBuilder = new StringBuilder();
                    stringBuilder.append("set==");
                    stringBuilder.append(strArr.toString());
                    Log.e("ryan", stringBuilder.toString());
                    return strArr;
                }
            }
        } catch (Exception e) {
            throw e;
        } catch (Throwable th) {
            inputStreamReader.close();
        }
    }
```

