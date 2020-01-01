#! /data/data/com.termux/files/usr/bin/env python3 

import shlex
import subprocess

def send_intent(wx_string, wx_daily, wx_icon, wx_city, wx_state):
    args = shlex.split("/data/data/com.termux/files/usr/bin/am broadcast "
                       "--user 0 "
                       "-a net.dinglish.tasker.wx ")
    subprocess.Popen(args)
