#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        dirname_split = dirname.split()
        if len(dirname_split) > 2:
            newdirname = dirname_split[len(dirname_split) - 1].upper()
            for i in range(0, len(dirname_split) - 1):
                if dirname_split[i] != "HD":
                    newdirname = newdirname + " " + dirname_split[i]
            if re.match("^[A-Z]+-[0-9]+", newdirname):
                os.rename(dirname, newdirname)
            else:
                print dirname + "cannot rename"
