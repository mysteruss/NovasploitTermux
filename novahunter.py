import os

print ("""\033[93m
┌──────────────────────────────────────────────┐
│┏━   ┏━┃  ┃ ┃  ┏━┃  ┏━┛  ┏━┃  ┃    ┏━┃  ┛  ━┏┛│
│┃ ┃  ┃ ┃  ┃ ┃  ┏━┃  ━━┃  ┏━┛  ┃    ┃ ┃  ┃   ┃ │
│┛ ┛  ━━┛   ┛   ┛ ┛  ━━┛  ┛    ━━┛  ━━┛  ┛   ┛ │
└──────────────────────────────────────────────┘
İNSTALLİNG NETHUNTER
\033[0m""")

os.system("pkg install wget -y")
os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
os.system("chmod +x install-nethunter-termux")
os.system("bash install-nethunter-termux")
