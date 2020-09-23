#!/usr/bin/python
#coding:utf-8
import os, sys, time, random, requests, re
from optparse import *

# Declaration des options/arguments et on place par defaut sur False pour ajouter nos options
parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--url", dest="url")
parser.add_option("-w", "--wordlist", dest="wordlist")
parser.add_option("-s", "--see-code", dest="seecode")

# On place action pour retirer la demande d argument obligatoire pour la valeur help
parser.add_option("-h", "--help", dest="help", action="store_true", help="help")

(options, args) = parser.parse_args()

# Declaration des variables et affectation des options aux variables
arg = options.url
wordlist = options.wordlist
helps = options.help
s = options.seecode

# Fonction de base du code
def initial():
    if(arg):
        req = requests.get(arg).status_code
        if req == 200:
            print("[!] Testing your URL, Please wait...")
            time.sleep(2)
            print("\n[OK] Test successful !\n")
            time.sleep(1)
            print("[!] Script is running, Press CTRL + C to stop\n")
            liste = open(wordlist, "r").readlines()
            for word in liste:
                word = word.strip('\n')
                cmd = "%s%s" %(arg, word)
                cde = requests.post(cmd).status_code
                if cde == 200:
                    cde = str(cde)
                    if s == "200":
                        print("[*] Match Found: ("+(word)+") | CODE:"+(cde))
                elif cde == 401:
                    cde = str(cde)
                    if s == "401":
                        print("[?] Match Found with Auth Basic: ("+(word)+") | CODE:"+(cde))
                elif cde == 404:
                    cde = str(cde)
                    if s == "404":
                        print("[!] No match: ("+(word)+") | CODE:"+(cde))
        elif req == 404:
            cde = str(cde)
            print("[!] Error Web client, please check your URL | CODE:"+(cde))

# Fonction pour guider les utilisateurs
def helpuser():
    print("[SCRIPT HELP]")
    print("\nURL:")
    print("\t\t PROTOCOL    :\t\t\t\thttp://")
    print("\t\t             :\t\t\t\thttps://")
    print("\nOPTIONS:")
    print("\t\t -h --help   :\t\t\t\tThis Screen ")
    print("\t\t -sc [CODE]  :\t\t\t\tSee only the code specified")
    print("\t\t -w [FILES]  :\t\t\t\tSpecified your Wordlist (This option is required)\n")
    print("[?] Example: python ./script.py -u http://www.domain.com/ [OPTIONS] -w wordlist.txt")

# Debut du code
if __name__ == "__main__":
    if(arg):
        initial()
    if(helps):
        helpuser()
    else:
        print("\n[!] Error script init ! Please check the manual with options -h or --help")
