import asyncio
import aiohttp
import sys
import os
import random
from colorama import Fore, Style, init

init(autoreset=True)

# قائمة متنوعة من الـ User-Agents لتجاوز حماية التعرف على البوتات
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
]

# منصات مع روابط مجهزة خصيصاً للتعامل مع استجابات تيك توك وغيرها
PLATFORMS = {
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}/",
    "X (Twitter)": "https://x.com/{}",
    "GitHub": "https://github.com/{}",
    "Telegram": "https://t.me/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "Twitch": "https://www.twitch.tv/{}",
    "Medium": "https://medium.com/@{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Behance": "https://www.behance.net/{}"
}

def banner():
    os.system('clear')
    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════╗
║         {Fore.WHITE}LEX-OSINT PRO | ANTI-BOT BYPASS ENGINE{Fore.CYAN}           ║
║            {Fore.GREEN}Advanced Headers & Stealth Mode{Fore.CYAN}              ║
╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """)

async def check_platform(session, name, url_template, username, found_list, semaphore):
    async with semaphore:
        url = url_template.format(username)
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        
        try:
            # إضافة تأخير عشوائي بسيط جداً لمنع كشف السكربت كبوت
            await asyncio.sleep(random.uniform(0.1, 0.5))
            
            async with session.get(url, headers=headers, timeout=10, allow_redirects=True) as response:
                status = response.status
                text = await response.text()
                
                is_found = False
                
                # فحص خاص بمنصة تيك توك لتجاوز الحماية
                if "tiktok.com" in url:
                    if status == 200 and "Couldn't find this account" not in text and "User not found" not in text:
                        is_found = True
                else:
                    # المعيار العام لبقية المنصات
                    if status == 200:
                        false_indicators = ["page not found", "not found", "doesn't exist", "404", "no profile"]
                        if not any(ind in text.lower() for ind in false_indicators):
                            is_found = True

                if is_found:
                    print(f"{Fore.GREEN}[+] {name:<15} : {Fore.WHITE}{url}")
                    found_list.append(f"{name}: {url}")
                else:
                    print(f"{Fore.RED}[-] {name:<15} : Not Found")
                    
        except Exception:
            pass

async def main():
    banner()
    username = input(f"{Fore.YELLOW}أدخل اسم المستخدم المراد فحصه: {Fore.WHITE}").strip()
    if not username:
        return

    print(f"\n{Fore.CYAN}[*] جاري الفحص بتفعيل وضع التخفي (Stealth Mode) لتجاوز الحماية...\n{Style.RESET_ALL}")
    
    found_list = []
    semaphore = asyncio.Semaphore(10) # تقليل عدد الطلبات المتزامنة قليلاً لتفادي حظر الـ Rate Limit
    
    connector = aiohttp.TCPConnector(limit=20, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [
            check_platform(session, name, url_temp, username, found_list, semaphore)
            for name, url_temp in PLATFORMS.items()
        ]
        await asyncio.gather(*tasks)

    print(f"\n{Fore.CYAN}══════════════════════════════════════════════════════════")
    print(f"{Fore.GREEN}[✓] انتهى الفحص! الحسابات الصحيحة المكتشفة: {len(found_list)}")
    
    if found_list:
        filename = f"{username}_pro_results.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for item in found_list:
                f.write(item + "\n")
        print(f"{Fore.CYAN}[*] تم حفظ النتائج في: {Fore.WHITE}{filename}")
    print(f"{Fore.CYAN}══════════════════════════════════════════════════════════{Style.RESET_ALL}\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
