#!/usr/bin/python
import sys, os
# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
""" [!] Programado por Mark Security [!]"""
os.system("clear")
print " "
print "  ___  ___              _      _____                          "
print "  |  \/  |             | |    /  ___|                         "
print "  | .  . |  __ _  _ __ | | __ \ `--.  _ __    __ _  _ __ ___  "
print "  | |\/| | / _` || '__|| |/ /  `--. \| '_ \  / _` || '_ ` _ \ "
print "  | |  | || (_| || |   |   <  /\__/ /| |_) || (_| || | | | | |"
print "  \_|  |_/ \__,_||_|   |_|\_\ \____/ | .__/  \__,_||_| |_| |_|"
print "	------------------= Mark Spam Priv8 =------------------------"
print "  ===|[ SMS Spammer ]|==="
print "  [01] Nova sessão:        "
print "  [02] Repetir sessão:          "
print "  [03] Atulizar           "
print "  [00] Sair"
print
Spammer = raw_input(" Escolha:  ")

if (Spammer == '01' or Spammer == '1'):
       print " "
       print " SMS TEMPO DE FLOOD:(1s - 10min)             "
       Delay = raw_input(" Tempo: ")
       Number = raw_input(" Numero: ")
       Message = raw_input(" Mensagem: ")
       os.system("watch -n %s termux-sms-send -n %s %s " % (Delay, Number, Message))
       sys.exit()

elif (Spammer == '02' or Spammer == '2'):
       print "Em breve..."

elif (Spammer == '03' or Spammer == '3'):
       os.system("git clone")

elif (Spammer == '00' or Spammer == '0'):
       print "\n[!] Saindo do programa..."
       sys.exit()

else:
       print "\n[!] Erro: Input errado..."
       time.sleep(1)
       restart_program()
