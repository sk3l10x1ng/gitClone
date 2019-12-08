#! /usr/bin/env python3
import subprocess
import sys
import os

def git():
    path = sys.argv[1]
    os.chdir(str(sys.argv[2]))
    if os.path.exists(path):
        with open(path,'r',encoding='utf-8') as f:
            for line in f:
                l = line.strip()
                if len(l.strip()) != 0:
                    print("#####################################################\n")
                    subprocess.run(['git', 'clone', l])
                    print("\n")

git()
