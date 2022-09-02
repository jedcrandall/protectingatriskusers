
# Dendrogram for comparing Android apps

This is the source code used to make dendrograms like [This one]() for [this project]().  It's not a polished product by far, but hopefully is useful to someone.

## Files included

- dendro.py is the main Python script for building the dendrogram 
- compare.c is a very simple C program to calculate the cosine similarity between files

## Usage

It's unlikely that it will run unmodified on your machine.  README is currently
a work in progress...

[](https://github.com/zgkom/anzhi_apk_download)

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
