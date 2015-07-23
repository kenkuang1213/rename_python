#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
for filename in os.listdir("."):
    filename_split = filename.split()
    if len(filename_split) > 2:
        newfilename = filename_split[len(filename_split) - 1].upper()
        for i in range(0, len(filename_split) - 1):
            if filename_split[i] != "HD":
                newfilename = newfilename + " " + filename_split[i]
        if re.match("^[A-Z]+-[0-9]+", newfilename):
            os.rename(filename, newfilename)
        else:
            print newfilename
