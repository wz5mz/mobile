#! /data/data/com.termux/files/usr/bin/env python3 

import shlex
import subprocess


def send_var(testvar):
    args = shlex.split("/data/data/com.termux/files/usr/bin/am broadcast "
                       "--user 0 "
                       "-a net.dinglish.tasker.wx "
                       "-e testvar '{}' ".format(testvar))
   subprocess.Popen(args)

send_var('$92,000.00')
