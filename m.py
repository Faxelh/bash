#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time

def _cls():
 if os.name == 'nt':
  os.system('cls')
 else:
  os.system('clear')

raw_input = input
####################################################################################################
ts = .009
def Auto(a):
 for o in a + "\n":
  sys.stdout.write(o)
  sys.stdout.flush()
  time.sleep(ts)

def hack():
    hacking = [" ", '.', '..', '...']
    for h in hacking:
        sys.stdout.write("\r\033[1;91m[\033[38;5;112m●\033[1;91m] \033[38;5;118mPlz wait we check if there is an update\033[1;33m" + h)
        sys.stdout.flush()
        time.sleep(1)

Dev_faxel =("""
\033[1;97m╔═════════════════════════════════╗
\033[1;97m║\033[1;91m[\033[1;93m©\033[1;91m]\033[38;5;95m  Dev \033[1;97m:\033[38;5;214m Faxel ── \033[38;5;112m\033[3;5;1m@faxelh\033[3;0;0m   \033[1;91m[\033[1;93m©\033[1;91m]\033[1;97m║
\033[1;97m╚═════════════════════════════════╝ """)
####################################################################################################
def prec():
 f = "\x1b[2K"
 sys.stdout.write(f)

def Update():
 _cls();print(Dev_faxel)
 print("\033[1;97m║ \x1b[38;5;115m Please enter\x1b[38;5;112m O\x1b[38;5;115m or\x1b[38;5;198m N\x1b[38;5;115m. \x1b[38;5;113mThank  \033[1;97m║")
 dmd = raw_input("\033[1;97m╚\033[1;31m▶ \033[1;97mDo you want to check if there is an update? \x1b[1;91m: \x1b[38;5;91m")
 if dmd == "n" or dmd == "N":
  Update()
 elif dmd == "o" or dmd == "O":
  _cls();hack();prec()
  #_cls();
  print(Dev_faxel)
  os.system('git pull')
  raw_input("\t\033[1;91m[\033[38;5;90m!\033[1;91m]\033[1;9;38;5;95m Hit Enter \033[1;0;1;91m[\033[38;5;9m!\033[1;91m]")
  #os.system("cd $HOME/bash && python3 setup.py ")
  os.system("exit(1)")
  os.system("python3 setup.py ")
 else:
  print("\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m The option \x1b[3;5;1;38;5;97m" + dmd + "\x1b[3;0;0;1;97m is unavailable. \x1b[1;91m[\x1b[1;97m+\x1b[1;91m]")
  time.sleep(6);Update()
####################################################################################################
if __name__ == "__main__":
 try:
  Update()
 except Exception as e:
  x = sys.exc_info()
  print("\033[1;97m" + 35 * "═")
  print(f"\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Error \x1b[1;91m:\x1b[38;5;95m {x[0].__name__}\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Text \x1b[1;91m :\x1b[38;5;92m {e}\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Line \x1b[1;91m :\x1b[38;5;95m {x[2].tb_lineno}")
  print("\x1b[38;5;199m Please install the required modules and restart.")
  print("\033[1;97m" + 35 * "═")
  time.sleep(6)
