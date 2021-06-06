#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,platform,time, sys

def _cls():
    if os.name == 'nt':
         os.system('cls')
    else:
         os.system('clear')         

try:
    print("\n\033[38;5;245m Installation des paquets")
    _cls()
    os.system("apt update && apt install curl -y && apt install python -y && apt install nano -y && apt install toilet -y && apt install ruby -y")
    os.system("gem install lolcat")
except :
    _cls()

def Setupbash():
  _cls()
  print("\n\033[38;5;198m Suppression du bash.bashrc d'origine");time.sleep(4)
  os.system("rm /data/data/com.termux/files/usr/etc/bash.bashrc");time.sleep(3)
  print("\n\033[38;5;118m Configuration du nouveau du bash.bashrc")
  os.system("curl -LO https://raw.githubusercontent.com/threat0/bash/master/bash.bashrc")
  os.system("mv bash.bashrc /data/data/com.termux/files/usr/etc");time.sleep(3)
  os.system(" toilet -f term -F border Configuration Terminer. Faxel | lolcat")

if __name__ == "__main__":
      try:
       Setupbash()
      except Exception as e:
       x = sys.exc_info()
       print("\033[1;97m" + 35 * "═")
       print(f"\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Erreur \x1b[1;91m:\x1b[38;5;95m {x[0].__name__}\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Texte \x1b[1;91m :\x1b[38;5;92m {e}\n\x1b[1;91m[\x1b[1;97m+\x1b[1;91m]\x1b[1;97m Ligne \x1b[1;91m :\x1b[38;5;95m {x[2].tb_lineno}")
       print("\x1b[38;5;199m Veuillez installé les modules requis puis relancé.")
       print("\033[1;97m" + 35 * "═")
       time.sleep(5)