import os

print ("""
┌──────────────────────────────────────────────┐
│┏━   ┏━┃  ┃ ┃  ┏━┃  ┏━┛  ┏━┃  ┃    ┏━┃  ┛  ━┏┛│
│┃ ┃  ┃ ┃  ┃ ┃  ┏━┃  ━━┃  ┏━┛  ┃    ┃ ┃  ┃   ┃ │
│┛ ┛  ━━┛   ┛   ┛ ┛  ━━┛  ┛    ━━┛  ━━┛  ┛   ┛ │
└──────────────────────────────────────────────┘
İNSTALLİNG NETHUNTER
""")

os.system("pkg install wget -y")
os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
os.system("chmod +x install-nethunter-termux")
os.system("./install-nethunter-termux")
