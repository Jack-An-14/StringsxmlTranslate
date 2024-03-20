#!/usr/bin
import threading
import time

import workThread
import queue
import xml.etree.ElementTree as ET

from XmlLanguagePraser.threadPool import threadPool

# now is test, when completed, is main
# work thread is ok
# thread = workThread.workThread(1, "你好", "cn", "en")



if __name__=='__main__':
    # work queue
    tree = ET.parse('strings.xml')
    root = tree.getroot()
    fromlang = input("文本语言")
    tolang = input("翻译语言")

    pool = threadPool(3, 1000, 20)
    lock = threading.Lock()
    i = 0
    for child in root:
        if child.tag == "string" and child.text is not None:
            lock.acquire()
            try:
                var = workThread.workThread(i, child.text, fromlang, tolang, child)
                pool.submit(var)
                i += 1
            finally:
                lock.release()
    # 线程池任务join等待
    tree.write('strings.xml', encoding='utf-8')
