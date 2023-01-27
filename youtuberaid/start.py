
# Created by @Yourboyaladin

import requests,os,time
import random 
from random import choice
from pystyle import * 
from colorama import *
from rich.traceback import install
from rich.console import Console
import sys

install()
console = Console()

class dwonTiktok:

            #init Function
            def __init__(self):

                def api1():
                    url = "https://www.tikwm.com/api/user/posts"
                    print("""[Example: @tiktok ]\n""")
                    # Api: https://www.tikwm.com 

                    KeyError = False
                    while not KeyError:
                        try:
                            url = "https://www.tikwm.com/api/user/posts"

                            querystring = {"unique_id":"", "count":"10","cursor":"0"}
                            querystring["unique_id"] = input(f"{Fore.YELLOW}Enter User:{Fore.WHITE} ")

                            s = requests.Session()
                            gen = s.headers['User-Agent']

                            header = {
                                "User-Agent": gen
                            }

                            request_data = requests.request("GET", url, headers=header, params=querystring).json()
                            break         
                        except:
                            pass

                    username = request_data["data"]["videos"][0]['author']["unique_id"]



                    if not os.path.exists(f"./finalvideos"):
                        os.makedirs(f"./finalvideos")

                    videos = request_data["data"]["videos"]

                    print(f"""\n{Fore.CYAN}[Programs] {Fore.GREEN}[Status] {Fore.RED}@{username} {Fore.YELLOW}Have Published {Fore.BLUE}{len(videos)} {Fore.YELLOW}Videos. Downloading them...""")
                    console.log("[cyan][Status][/cyan] Already Downloaded Videos Will Be Skipped.\n")


                    count = 0

                    
                    for video in videos:
                        
                        count += 1
                        download_url = video["play"]
                        #uri = video["video_id"]
                        uri = f"vid{count}"
                        title = video['title']
                        limit = str(f'{title:80.80}')
                        print(f"""{Fore.CYAN}[Programs] {Fore.YELLOW}[Title] {Fore.GREEN}{limit}\r""")
                        # download start time                           
                        start = time.time()
                        # data size of each download                                        
                        chunk_size = 1024

                        if not os.path.exists(f"./finalvideos/{uri}.mp4"):

                            video_bytes = requests.get(download_url, stream=True)
                            total_length = int(video_bytes.headers.get("Content-Length"))
                            console.log(f"[green][Status][/green] File size: " + "{size:.2f} MB".format(size = total_length / chunk_size /1024)) 
                            with open(f'./finalvideos/{uri}.mp4', 'wb') as out_file:
                                out_file.write(video_bytes.content)
                                end = time.time() 

                                print(f"{Fore.CYAN}[Programs] {Fore.GREEN}[Status] {Fore.WHITE}Timelapse:{Fore.YELLOW}"+ " %.2fs" % (end - start))
                                print(f"""{Fore.CYAN}[Programs] {Fore.YELLOW}[File] {Fore.GREEN}{uri}.mp4{Fore.YELLOW} Downloaded\n""")
                                time.sleep(0.7)
                            
                        else:
                            print(f"{Fore.CYAN}[Programs] {Fore.YELLOW}[File] {Fore.GREEN}{uri}.mp4{Fore.WHITE} already exists! Skipping...\n")
                            time.sleep(0.7) 
                            continue
                    time.sleep(1) 
                    console.log(f"[cyan][Status][/cyan] Download process done : [red] Processing upload ...")

                # Download All Video From Tiktok User Function
                def api2():

                    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/user/posts"
                    print("""[Example: @tiktok ]\n""")

                    key = [
                        "cbb685f815msh9bb9a7c12e7952fp1c55ddjsn1313cb0b6392",
                        "bc72be337fmshb7473c97adae84ep1ed443jsna2e9de2f00f5",
                        "ae52c34202mshc9cc27d0dfd4288p178654jsnb7a8a5a2042f"
                    ]
                    api_key = random.choice(key)

                    querystring = {"unique_id":"", "count":"10","cursor":"0"}
                    querystring["unique_id"] = input(f"{Fore.YELLOW}Enter User:{Fore.WHITE} ")

                    headers = {
                        "X-RapidAPI-Key": api_key,
                        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
                    }

                    request_data = requests.request("GET", url, headers=headers, params=querystring).json()
                    order = []
                    username = request_data["data"]["videos"][0]['author']["unique_id"]

                    if not os.path.exists(f"./finalvideos"):
                        os.makedirs(f"./finalvideos")

                    videos = request_data["data"]["videos"]

                    print(f"""\n{Fore.CYAN}[Programs] {Fore.GREEN}[Status] {Fore.RED}@{username} {Fore.YELLOW}Have Published {Fore.BLUE}{len(videos)} {Fore.YELLOW}Videos. Downloading them...""")
                    console.log("[cyan][Status][/cyan] Already Downloaded Videos Will Be Skipped.\n")


                    count = 0
                    for video in videos:
                        
                        count += 1
                        download_url = video["play"]
                        #uri = video["video_id"]
                        uri = f"vid{count}"
                        title = video['title']
                        limit = str(f'{title:80.80}')
                        print(f"""{Fore.CYAN}[Programs] {Fore.YELLOW}[Title] {Fore.GREEN}{limit}\r""")
                        # download start time                           
                        start = time.time()
                        # data size of each download                                        
                        chunk_size = 1024

                        if not os.path.exists(f"./finalvideos/{uri}.mp4"):

                            video_bytes = requests.get(download_url, stream=True)
                            total_length = int(video_bytes.headers.get("Content-Length"))
                            console.log(f"[green][Status][/green] File size: " + "{size:.2f} MB".format(size = total_length / chunk_size /1024)) 
                            with open(f'./finalvideos/{uri}.mp4', 'wb') as out_file:
                                out_file.write(video_bytes.content)
                                end = time.time() 

                                print(f"{Fore.CYAN}[Programs] {Fore.GREEN}[Status] {Fore.WHITE}Timelapse:{Fore.YELLOW}"+ " %.2fs" % (end - start))
                                print(f"""{Fore.CYAN}[Programs] {Fore.YELLOW}[File] {Fore.GREEN}{uri}.mp4{Fore.YELLOW} Downloaded\n""")
                                time.sleep(0.7)
                            
                        else:
                            print(f"{Fore.CYAN}[Programs] {Fore.YELLOW}[File] {Fore.GREEN}{uri}.mp4{Fore.WHITE} already exists! Skipping...\n")
                            time.sleep(0.7) 
                            continue
                    time.sleep(1) 
                    console.log(f"[cyan][Status][/cyan]  Successfully downloaded [green]{count}[/green] videos ✓")
                    
                    

                if __name__ == "__main__":

                    if not os.path.exists("./finalvideos"):
                        os.makedirs("./finalvideos")
                    os.system('cls')
                    banner = f"""{Fore.LIGHTRED_EX} 
 ____  _     _____            _    _ 
/ ___|| |__  _   _  __ _  ___| | _(_)
\___ \| '_ \| | | |/ _` |/ _ \ |/ / |
 ___) | | | | |_| | (_| |  __/   <| |
|____/|_| |_|\__,_|\__, |\___|_|\_\_|
                   |___/ Created by @Yourboyaladin
                                """
                    print(Center.XCenter(banner))
                    print(f'{Fore.BLUE}')
                    fns = [api1, api2]
                    choice(fns)()
                    time.sleep(1)

if __name__ == "__main__":
            
            os.system("cls" if os.name == "nt" else "clear"); os.system("title Shugeki by @Yourboyaladin" if os.name == "nt" else "")
            
            dwonTiktok()
            os.system("python upload.py")
            
        
    
    
