import os

ascii_sanat = """\033[93m
⠀
⠀⠀⠀⠀
⠀ _   _  ______      __      _____ _____  _      ____    _   ______
 | \\ | |/ __ \\ \\    / /\\    / ____|  __ \\| |    / __ \\  | |  __   __|
 |  \\| | |  | \\ \\  / /  \\  | (___ | |__) | |   | |  | | | |   | |
 |   ` | |  | |\\ \\/ / /\\ \\  \\___ \\|  ___/| |   | |  | | | |   | |
 | |\\  | |__| | \\  / ____ \\ ____) | |    | |___| |__| | | |   | |
 |_| \\_|\\____/   \\/_/    \\_\\_____/|_|    |______\\____/  |_|   |_⠀'⠀⠀
      İnstagram :@novasploit ||
                   ~ Coded By NOVASPLOİT ~
1) TERMUX PACKAGES İNSTALL
2) NETHUNTER İNSTALL
3) TOOLS İN GİTHOOB
4) NETHUNTER TOOLS İNSTALLER
\033[0m"""

def termux_temel_kurulum():
    
    print("Termux temel kurulumu yapılıyor...")

def nethunter_kurulum():
   
    print ("Nethunter kurulumu yapılıyor...")

def githubdan_tool_ekle():
    print("\nTOOLLAR EKLE")
    print("[1] Tool 1 KRAWTER SQL ")
    print("[2] Tool 2 İNSTA BRUTEFORCE")
    print("[3] Tool 3 007THEBOND ")
    print("[4] Tool 4 SQLMAP ")
    print("[5] Tool 5 cupp ")
    print("[6] Tool 6 Camhack")
    print("[7] Tool 7 Doxxer-Toolkit")
    print("[8] Tool 8 Termux-Hydra ")
    print("[9] Tool 9 Red Hawk")
    print("[10] Tool 10 Mr.Holmes ")
    
    tool = input("\nİSTEDİĞİNİZ TOOL NUMARASI: ")

    if tool == "1":
        os.system("git clone https://github.com/KraWterr/Sql-krawter")
        print ("KRAWTER SQL yükleniyor...")
    elif tool == "2":
        os.system("git clone https://github.com/akashblackhat/instagrame-hacking")
        print ("İnstagram Brute Force yükleniyor...")
    elif tool == "3":
        os.system("git clone https://github.com/Deadshot0x7/007-TheBond")
        print ("007TheBond yükleniyor...")
    elif tool == "4":
        os.system("git clone https://github.com/sqlmapproject/sqlmap")
        print ("SQLMAP yükleniyor...")
    elif tool == "5":
        os.system("git clone https://github.com/Mebus/cupp")
        print ("Cupp yükleniyor...")
    elif tool == "6":
        os.system("git clone https://github.com/techchipnet/CamPhish")
        print ("Camhack yükleniyor...")
    elif tool == "7":
        os.system("git clone https://github.com/Euronymou5/Doxxer-Toolkit")
        print ("Doxxer-Toolkit yükleniyor...")
    elif tool == "8":
        os.system("git clone https://github.com/iamunixtz/Termux-Hydra ")
        print ("Termux-Hydra yükleniyor...")
    elif tool == "9":
        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK ")
        print ("Red Hawk yükleniyor...")
    elif tool == "10":
        os.system("git clone https://github.com/Lucksi/Mr.Holmes")
        print ("Mr.Holmes yükleniyor...")
    else:
        print ("Geçersiz araç numarası")

while True:
    print(ascii_sanat)

    islem = input("SEÇ ")

    if islem == "1" or islem == "01":
        os.system("""pkg install kotlin -y
pkg install openjdk-17 -y
pkg install ecj -y
pkg install ghc -y
pkg install groovy -y
pkg install golang -y
pkg install pforth -y
pkg install erlang -y
pkg install elixir -y
pkg install dart -y
pkg install ldc -y
pkg install ecl -y
pkg install tinyscheme -y
pkg install guile -y
pkg install smalltalk -y
pkg install swift -y
pkg install tcl -y
pkg install php -y
pkg install pip pip2 -y
pip install colorama -y
pip install telethon -y
pip install --upgrade pip -y
pkg install clang -y
pkg install vim -y
pkg install nano -y
apt install proot -y
pkg install cat -y
pkg install figlet -y
pkg install cmatrix -y
pkg install perl -y
pkg install nmap -y
pkg install openssl -y
pkg install nodejs -y
pkg install wordlist -y
pkg install ruby -y
termux-install-tl -y
pkg install rust -y
pkg install scala -y
pkg install racket -y
pkg install swi-prolog -y
pkg install lua52 lua53 lua54 -y
pkg install kotlin -y
pkg install openjdk-17 -y
pkg install ecj -y
pkg install ghc -y
pkg install groovy -y
pkg install golang -y
pkg install pforth -y
pkg install erlang -y
pkg install elixir -y
pkg install dart -y
pkg install ldc -y
pkg install python python2 python3 -y
pkg install wget -y
pkg install weechat -y
pkg install science-repo -y
pkg install root-repo -y
pkg install x11-repo -y
pkg install toilet -y
pkg install nodejs-lts -y
pkg install yarn -y
pkg install build-essential -y
pkg install python-numpy -y
pkg install electrum -y
pkg install opencv-python -y
pkg install asciinema -y
pkg install matplotlib -y
pkg install python-cryptography -y
pip install pandas -y
pip install pyzmq -y
pkg install python-tkinter -y
pkg install git -y
apt install curl -y
apt install dnsutils -y
pip install wordlist -y
apt install bash -y
apt install nodejs -y
pip install requests -y
apt install clang -y
apt install jq -y
apt install macchanger -y
apt install tar -y
apt install zip -y
apt install unzip -y
apt install tor -y
apt install wget -y
apt install wcalc -y
pip install instaloader -y
apt install openssl -y
pip install requests -y
pip install beautifulsoup4 -y
apt install tmate -y
apt install bmon -y
apt update -y
apt upgrade -y""")
    elif islem == "2" or islem == "02":
        os.system("""python novahunter.py""")
    elif islem == "3" or islem == "03":
        githubdan_tool_ekle()
    elif islem == "4" or islem == "04":
        os.system("""python3 novainstaller.py""")
    else:
        print ("Geçersiz seçim")
