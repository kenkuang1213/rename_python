#! /usr/bin/env python
import os
for filename in os.listdir("."):
	if filename.startswith("fixed."):
		os.rename(filename,filename[6:])

