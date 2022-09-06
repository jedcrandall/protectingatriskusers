
# Dendrogram for comparing Android apps

This is the source code used to make dendrograms like [This one](anzhiandbuiltins.png) for [this
project](https://github.com/jedcrandall/protectingatriskusers).  It's not a
polished product by far, but hopefully is useful to someone.

## Files included

- dendro.py is the main Python script for building the dendrogram 
- compare.c is a very simple C program to calculate the cosine similarity between files

## Usage

It's unlikely that it will run unmodified on your machine.  You'll need APKs
and data scraped from the Anzhi app store and then you'll need to extract
strings from them in a special way.  Reach out to
[me](https://jedcrandall.github.io/) and I can provide files or assistance in
generating them.  Basically, you scrape the data with
[this](https://github.com/zgkom/anzhi_apk_download) and then do something like
this to make the ``tarred and feathered'' versions of the APKs:

```bash
rm -rf /tmp/papk/*
rm -rf /tmp/papk/.*
timeout 1m unzip $1 -d /tmp/papk/
mkdir /tmp/papk/jadxoutput
pushd .
cd /tmp/papk/jadxoutput
timeout 10m /home/jedi/jadx/build/jadx/bin/jadx $1
cd /tmp/papk/
find . > filelist.txt
popd
timeout 1m tar -cz /tmp/papk > /home/jedi/tmp/anzhitarredandfeathered/$thename.tgz
tar --to-stdout -xzf /home/jedi/tmp/anzhitarredandfeathered/$thename.tgz | strings -n 10 | tr -cd [:alpha:] > /home/jedi/tmp/anzhitarredandfeathered/$thename.tgz.txt
```

Then compile compare.c and run the Python script:

```bash
gcc compare.c -o compare -lm
python3 dendro.py
```

It'll open the dendrogram in a browser so you can play with zooming and such
and then export.
