# HSBC (app for a British Bank)

An app downloaded from anzhi.com was found to contain a keyword filter list.
The app is available here:

[http://www.anzhi.com/pkg/1977_cn.com.hsbc.hsbcchina.html](http://www.anzhi.com/pkg/1977_cn.com.hsbc.hsbcchina.html)

The SHA-256 digest of the *.apk file analyzed is:

d5ced5a54f73963598a780a2a5efe869a5735547d170747a6c5ba4c6b882089f

## App description

Copied from anzhi.com and translated with Google Translate: "HSBC China Mobile
Banking helps you enjoy comprehensive banking services anytime, anywhere! Four
major highlights: Comprehensive account management: including full account
management of debit and credit cards. Deposits, domestic and foreign currency
transfers, foreign exchange services, wealth management services and credit
card services, etc. Global Account Management: View your HSBC same-name account
balances in China and other countries and make real-time foreign currency
cross-border transfers to global HSBC same-name accounts. Multiple security
guarantees: Two-factor password verification, different authentication methods
can be set according to the security level, including security device,
fingerprint, SMS, or password verification, making your mobile banking
operations more secure. Services at your fingertips: instant inquiry of nearby
bank outlets and ATMs, online customer service at any time, and one-click call
to the HSBC service hotline. More features, stay tuned! IMPORTANT NOTE: This
App and all its contents are provided by HSBC Bank (China) Limited ("HSBC
China") and are intended for use by existing HSBC China customers only. If you
are not an existing HSBC China customer, please do not download this app.
Before you download and use this application, please note that (1) HSBC China
is not authorized to conduct banking business, accept deposits or provide
investment advisory or trading services in Hong Kong; (2) the content of this
application is only for HSBC Reference for existing customers in China; (3) The
products and services mentioned in this application are not approved for sale
or provision in Hong Kong; and (4) all information in this application must not
be forwarded to or shared with any other person ."

## What keywords are filtered?

The list of filtered keywords is included as a plain text asset within a Javascript, so is easy to extract.  The complete list is [here](sensitivewords.txt) and English translations via Google Translate are [here](sensitivewords-english.txt).

## How is the keyword list updated, if at all?

No evidence was found that the keyword list is dynamically updated.  

## What is censored?

It appears to be field names for records handled in the app that are filtered. 

```javascript
function(){return e.checkSensitiveWords("couterpartyName")})
function(){return e.checkSensitiveWords("insuranceName")})
function(){return e.checkSensitiveWords("providorName")})
function(){return e.checkSensitiveWords("schoolName")})
function(){return e.checkSensitiveWords("relativeName")})
function(){return e.checkSensitiveWords("relationship")})
function(){return e.checkSensitiveWords("hospitalName")})
function(){return e.checkSensitiveWords("otherCounterpartyName")})
function(){return e.checkSensitiveWords("specificPurchase")})
function(){return e.checkSensitiveWords("other")})
```

