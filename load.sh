#! /data/data/com.termux/files/usr/bin/bash

cd ~/.termux/tasker/
git clone "https://github.com/wz5mz/mobile.git"
for file in ~/.termux/tasker/mobile/*
do
   termux-fix-shebang "$file"
   chmod +x "$file"
done
mv -v ~/.termux/tasker/mobile/* ~/.termux/tasker/
rm -rf mobile
