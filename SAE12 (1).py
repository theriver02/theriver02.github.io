import os
import socket
import psutil
import time

## Partie 1
os.system('clear')
#Récupérer l'addresse ip
host= os.popen('hostname -I')
host = host.read()
print("L'adresse ip est : ",host)
#Récupérer l'addresse mac
mac=os.popen("ip a | egrep link/ether | awk '{print $2}' | tail -1")
print("L'adresse mac est : ",mac.read())
#Récupérer l'adresse réseau
network=os.popen("netstat -r | grep 'U[ \t]' | head -1 | awk '{print $1}'")
network=network.read()
print("L'adresse du réseau est ", network)
#Récuperer l'adresse de broscast
brd=os.popen("ip a | egrep 'brd' | egrep 'inet' | awk '{print $4}'")
brd=brd.read()
print("L'adresse de broscast est : ",brd)
#Récuperer l'adresse de la passerelle
passerelle=os.popen("netstat -rn | grep 'UG[ \t]' | awk '{print$2}'")
passerelle=passerelle.read()
print("L'adresse de la passerelle est ", passerelle)
#Recuperer le masque réseau
masque=os.popen("netstat -r | grep 'U[ \t]' | head -1 | awk '{print $3}'")
print("L'adresse du masque est ", masque.read())
#Récupérer le dns
dns= os.popen("dig | grep \"SERVER\" | awk '{print $3}' | awk -F '#' '{print $1}'")
print("L'adresse du dns est : ", dns.read())
#Permet de voir quel port qui sont allumées sur le réseau
#port=os.popen('nmap -sn'+network.read())
#print(port.read())


##Partie 2
#Savoir si la carte réseau est activé
ps=(psutil.net_io_counters(pernic=True))
ip=host
#Savoir si la configuration ip est correcte
if ip > network and ip < brd:
    print("L'adresse IP est dans la plage réseau\n")
else :
    print("L'adresse IP n'est pas dans la plage réseau\n")
##Pinger la passerelle
for i in range(1):
    try:
        requete = os.system("ping -c 2 "+passerelle)
        if requete==0:
            print("Connexion à la passerelle est opérationel\n\n")
        else:
            print("Connexion à la passerelle n'est pas opérationel\n\n")
    except:
        print("erreur")


ipConnu = ['www.google.com', 'www.cisco.fr']

for f in range(2):
    try:
        requete = os.system("ping -c 2 "+ipConnu[f])
        if requete==0:
            print("Le serveur DNS "+ipConnu[f]+" fonctionne\n\n")
        else:
            print("Le serveur DNS "+ipConnu[f]+" ne fonctionne pas\n\n")
    except:
        print("erreur")
