#! /data/data/com.termux/files/usr/bin/env python3 

import shlex
import subprocess


def send_var(testvar):
    args = shlex.split("/data/data/com.termux/files/usr/bin/am broadcast "
                       "--user 0 "
                       "-a net.dinglish.tasker.schwabreport "
                       "-e testvar '{}' ".format(testvar.replace("'","")))
    subprocess.Popen(args)

send_var([(1,2), 'wade', 69, {key:value}])
