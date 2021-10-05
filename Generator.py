import random, string, requests, webbrowser, time, os
from colorama import *
from discord import Webhook, RequestsWebhookAdapter

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def banner():
  print(Fore.MAGENTA)
  print("""                
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ 
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒  
         ░  ░              ░         ░ ░  
                                          
""")
  print(CYAN)
  print("""
             Created by: 
     https://github.com/iSwearing
                                 """)
  print(RESET)

def nitroGen():
  NitroGenerado = False

  print(f"{YELLOW}[-] {WHITE}Ingresa el link de tu webhook para nitros invalidos")
  Pene1 = input()

  print(f"{YELLOW}[-] {WHITE}Ingresa el link de tu webhook para nitros validos")
  Pene2 = input()
  
  NitroValidoWebhook = Webhook.from_url(Pene2, adapter=RequestsWebhookAdapter())
  NitroInvalidoWebhook = Webhook.from_url(Pene1, adapter=RequestsWebhookAdapter())

  os.system("@title [-]        Generador Nitro")
  f = open("Nitro generado.txt", "w", encoding='utf-8')
  n = open("Nitro No-Valido.txt", "w", encoding='utf-8')
  while NitroGenerado == False:
    code = ('').join(random.choices(string.ascii_letters + string.digits,k=16))
    r = requests.get(
      f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    )
    if r.status_code == 100000:
      print(f"{GREEN}[-]             {WHITE}Code valido de nitro > discord.gift/{code}")
      f.write(f"Code nitro Valido Generado: discord.gift/{code}\n")
      NitroValidoWebhook.send(f"Nitro valido: discord.gift/{code}")
      NitroGenerado = True
    else:
      print(f"{RED}[-]             Code nitro No-Valido Generado: > discord.gift/{code}")
      n.write(f"Code nitro No-Valido Generado: discord.gift/{code}\n")
      NitroInvalidoWebhook.send(f"Nitro no-valido: discord.gift/{code}")
      time.sleep(1)



def Modos():
  print(f"""{CYAN}[-] {YELLOW}Selecciona una herramienta
{BLUE}[1] {WHITE}Generador Nitro""")

  OpcionSeleccionada = input()

  if OpcionSeleccionada == "1":
    nitroGen()
  else:
    print(f"{RED}[-] {WHITE}Opcion incorrecta")
    time.sleep(5)

def contraseña():
  print(f'{YELLOW}[-] {WHITE}Introduzca la contraseña')
  IntroduzcaContra = input()
  if IntroduzcaContra == "soygay":
    print(f'{GREEN}[-] {WHITE}Contraseña Correcta.')
    os.system("@title [-]        Elige un modo")
    print(f"{YELLOW}[-] {WHITE}Pack de Tools creado por Vladorceda & iSwearing ")
    Modos()
  else:
    print(f'{RED}[-]        {WHITE}Contraseña Incorrecta.')
    time.sleep(5)
  
os.system("@title [-]   https://github.com/iSwearing")
banner()
contraseña()
