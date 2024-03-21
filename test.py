#!/usr/bin/python3
# coding=UTF-8
import getopt
import threading
import time

import workThread
import queue
import xml.etree.ElementTree as ET

import threadPool
from threadPool import threadPool as threadPool
import sys

# now is test, when completed, is main
# work thread is ok



if __name__=='__main__':
    # work queue
    fromL = None
    toL = None
    file = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:t:r:", ["fromL=", "toL="])
    except getopt.GetoptError:
        print('test.py error args, please check')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-f':
            fromL = arg
        elif opt == '-t':
            toL = arg
        elif opt == '-r':
            file = arg
# debug
    print(fromL, toL, file)
    try:
        tree = ET.parse(file)
    except ET.ParseError:
        print("file path error, please check")
        sys.exit(1)

    root = tree.getroot()

    pool = threadPool(3, 1000, 20)
    lock = threading.Lock()
    i = 0
    for child in root:
        if child.tag == "string" and child.text is not None:
            lock.acquire()
            try:
                var = workThread.workThread(i, child.text, fromL, toL, child)
                pool.submit(var)
                i += 1
            finally:
                lock.release()
    # thread pool task join() wait
    tree.write(file, encoding='utf-8')
