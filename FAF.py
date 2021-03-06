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
# On declare la concatenation -> voir la documentation officielle
(options, args) = parser.parse_args()

# Declaration des variables et affectation des options aux variables
arg = options.url
wordlist = options.wordlist
helps = options.help
s = options.seecode

# On declare la fonction de base du code
def initial():
    if(arg):
        req = requests.get(arg).status_code # On recupere le code HTTP dans une variable
        if req == 200:
            print("\n[!] Testing your URL, Please wait...")
            time.sleep(1)
            print("[OK] Test successful !\n")
            time.sleep(1)
            print("[!] Script is running, Press CTRL + C to stop\n")
            liste = open(wordlist, "r").readlines()
            for word in liste: # On test chaque mot dans la wordlist
                word = word.strip('\n')
                cmd = "%s%s" %(arg, word) # Concatenation de lURL et le mot de la wordlist
                cde = requests.post(cmd).status_code # Envoi de la requete avec le mot de la wordlist
                if cde == 200:
                    cde = str(cde)
                    if s == "200" or not s: # Pour pouvoir afficher si largument "s" est manquant
                        print("[*] Match Found: ("+(word)+") | CODE:"+(cde))
                elif cde == 401:
                    cde = str(cde)
                    if s == "401" or not s:
                        print("[?] Match Found with Auth Basic: ("+(word)+") | CODE:"+(cde))
                elif cde == 404:
                    cde = str(cde)
                    if s == "404" or not s:
                        print("[!] No match: ("+(word)+") | CODE:"+(cde))
                elif cde == 403:
                    cde = str(cde)
                    if s == "403" or not s:
                        print("[!] Forbidden Access: ("+(word)+") | CODE:"+(cde))                        
        elif req == 404:
            req = str(req)
            print("[!] Error Web client, please check your URL | CODE:"+(req))

# Fonction pour guider les utilisateurs
def helpuser():
    print("[SCRIPT HELP]")
    print("\nURL:")
    print("\t\t PROTOCOL    :\t\t\t\thttp://")
    print("\t\t             :\t\t\t\thttps://")
    print("\nOPTIONS:")
    print("\t\t -u --url   :\t\t\t\tFor testing URL ")
    print("\t\t -h --help   :\t\t\t\tThis Screen ")
    print("\t\t -s [CODE]  :\t\t\t\tSee only the code specified")
    print("\t\t -w [FILES]  :\t\t\t\tSpecified your Wordlist (This option is required)\n")
    print("[?] Example: python ./script.py -u http://www.domain.com/ [OPTIONS] -w wordlist.txt")

# Debut du code
try
    if __name__ == "__main__":
        if(arg): # Arguments de base pour le fonctionnement du code
            initial()
        if(helps): # Si lutilisateur passe en argument laide
            helpuser()
        if not(arg): # On test la condition si largument est manquant
            print("\n[!] Error script init ! Please check the manual with options -h or --help")
# On releve les erreurs en lien avec les certificats            
except requests.exceptions.SSLError:
     print("\n[!] Error with the SSL Certificate, It's appears doesn't match with the given domain...")
# On releve les erreurs en lien avec la mauvaise formulation de lURL        
except requests.exceptions.ConnectionError:
     print("\n[!] Connection Error : The URL it's invalid... check the '/' in your URL")
# On releve lexeption quand lutilisateur souhaite arreter le script
except KeyboardInterrupt:
    print("\nThe script was interrupted, quitting...")
