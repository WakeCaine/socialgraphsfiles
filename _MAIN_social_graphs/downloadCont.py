import subprocess
import time
import os
from pathlib import Path
import csv
import sys
import json
import threading
from contextlib import suppress

csv.field_size_limit(9999999)

#Curl can be used from python
class MyThread(threading.Thread):
    __slots__ = ('file', 'currentThread')
    def run(self):
        print("{} started!".format(self.getName()))
        with open("contributors/" + self.file, newline='\n', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                jsonName = line.split("/")[4] + "_" + line.split("/")[5] + ".json"
                cmd = "curl -u " + accounts[self.currentThread] + " -X GET " + line + " > " + jsonName
                print(cmd)
                my_file = Path(jsonName)
                if my_file.is_file():
                    print("DUPLICATE FILE: " + jsonName)
                else:
                    with suppress(Exception):
                        subprocess.run(cmd, shell=True, universal_newlines=True, check=True)
        print("{} finished!".format(self.getName()))

currentThread = 0

#Those are temporary accounts that were used to downlaod files
accounts = [
"waketemp1:5fa836f09b4e224ec50af7172968802a41feff83",
"waketemp2:99a580dc529bc09cc361f42d12117873e6a55498",
"waketemp3:bfc9337fec07f46a108c541d4428d3ccaccc2ba2",
"waketemp4:85064ef1a97464559eac9d976da291b4da76101b",
"waketemp5:33135ce53776e20aab95b07cada0c9d586479371",
"waketemp6:d49b895e8126694401d60266ecfb0405026ed8f5",
"waketemp7:0fe08bd43e82e214c4c33570858abb15232387bc",
"waketemp8:ca5ad325bdf54bf30584a0b1616ddc8ebfc39488",
"waketemp9:cfc2314cc0e749425f843eac0387c6a5c7d31303",
"waketemp10:44c1aa3e19217772373f68f541fa0472bf070165",
"waketemp11:9c1b1c9a661b7b814fb68a20e61bee7af0aaf19c",
"waketemp12:d0678c34e7d6f9fec3374d9359fb4a0f36111f8c",
"waketemp13:edd976172d55c47d385f148c363c3d2e14ff4b1e",
"waketemp14:c537b0446c96031dd6ef03cef9776c50466c020d",
"waketemp15:5eee187a4fe099e9fe6116bbf4ab4d24581b5c92",
"waketemp16:5f184b86dbfa93bc248ad6ce88ee18df89611c7c",
"waketemp17:358bd4d1be502955450c6a292027d62021665b4b",
"waketemp18:dd45e00edd2d199b434b5fd358a5eca012b9b485",
"waketemp19:202128435b1c1cb5200f65fea535095cde920109",
"waketemp20:9fc666a74f94a485b6be3637a4dd3b1b0b911316",
"waketemp21:3c1be784edacc166975df4da4c52d274d27d9f1e",
"waketemp22:8e8c8e393c871399423efa88960bd5ce70ccff35",
"waketemp23:464135cc21a55648679fb43ff65398fd378498f7",
"waketemp24:16c0353bdbc1c016cd483cde6f257f5b54619bf6",
"waketemp25:7fb73cc38edb794ed9dc012ec904ed7671bd9057"
]

listT = []
count = 0
for file in os.listdir('contributors'):
    if currentThread == len(accounts):
        time.sleep(3600)
        currentThread = 0
    mythread = MyThread(name = "Thread-{}".format(currentThread + 1))  # ...Instantiate a thread and pass a unique ID to it
    mythread.file = file
    mythread.currentThread = currentThread
    mythread.start()
    currentThread += 1
