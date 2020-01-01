#! /data/data/com.termux/files/usr/bin/env python3 

import shlex
import subprocess

args = shlex.split("/data/data/com.termux/files/usr/bin/am broadcast "
                   "--user 0 "
                   "-a net.dinglish.tasker.wx ")
subprocess.Popen(args)
