#!/usr/bin/env python3
# Binary download - Chapter 17 - binaryul.py

from ftplib import FTP
import sys, getpass, os.path

if len(sys.argv) != 5:
    print("usage:", sys.argv[0], "<host> <username> <localfile> <remotedir>")
    exit(2)

host, username, localfile, remotedir = sys.argv[1:]
prompt = "Enter password for {} on {}: ".format(username, host)
password = getpass.getpass(prompt)

ftp = FTP(host)
ftp.login(username, password)
ftp.cwd(remotedir)
with open(localfile, 'rb') as f:
    ftp.storbinary('STOR %s' % os.path.basename(localfile), f)
ftp.quit()
