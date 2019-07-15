#! /usr/bin/env python

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print ('*** Connected to host "%s"' % HOST)


    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonumously')
        f.quit()
        return
    print('*** Logged in as "anonymous"')


if __name__ == "__main__":
    main()