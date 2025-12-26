import requests
import os
import time


url = "https://openrouter.ai/api/v1/chat/completions"
ai_model = "anthropic/claude-3-haiku"
api_key = "your openrouter apiKey"
message = "hello"
history = [{
    "role": "system",
    "content": "You are a front-end development assistant , you task is to do what I ask you to do and tell me the brief of your adjusts and edits , nothing else . I am the backend developper , so you should help me in front end , ask me what you want , bcz we are team "
}]

headers = {
    "Authorization" : f"Bearer {api_key}",
    "Content-Type" : "application/json"
}

colors = {
    "reset": "\033[0m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m"
}


def print_banner():
    banner = r'''_____ _____    _    ___                           
|  ___| ____|  / \  |_ _|                         | |_  |  _|   / _ \  | |                          |  _| | |___ / ___ \ | |                          |_|   |_____/_/   \_\___|                          '''

    os.system('clear')
    os.system("figlet feai")
    #print(colors["bg_blue"] + colors["black"] + banner)
    print()
    print(colors["bg_magenta"]+"====Π[ FRONT END AI BY ::: YASSIN ]"+ colors["reset"])
    print('\n\n')


def help_menu():
    print("________________[MENU]_____________")
    print("|  1- exit : quit the Assistance  |")
    print("|  2- new : new session           |")
    print("|                                 |")
    print("|_________________________________|")
    
def prompt(msg):

    history.append({"role":"user","content":msg})
    data = {
        "model" : ai_model,
        "messages" : history
    }

    response = requests.post(url, headers=headers, json=data)
    
    
    if response.status_code == 200:
        ai_res = response.json()["choices"][0]["message"]["content"]
        history.append({"role":"assistant","content":ai_res})
        return ai_res
    else :
        print(f"ERROR {response.status_code} \n {response.text}")
        exit
    
    
def start():
    print_banner()
    msg = ''
    while(msg != "exit"):
        msg = input(colors["bg_green"] + colors["black"] + "You" + colors["reset"] + " : ")
        
        
        if msg.strip() == "" or msg == None or len(msg) < 4 :
            print("please ! avoid empty and small prompts")
            continue
        
        match msg:
            case "exit":
                print()
                print("Turning off " , end="", flush=True)
                for i in range(3):
                    time.sleep(1)
                    print(".", end="", flush=True)
                print()
                print("See you next time !!")
                break
            case "help":
                help_menu()
                continue
            
            case "new_":
                history.clear()
                history.append({
                    "role": "system",
                    "content": "You are a front-end development assistant , you task is to do what I ask you to do and tell me the brief of your adjusts and edits , nothing else . I am the backend developper , so you should help me in front end , ask me what you want , bcz we are team "
                })
                
                print("{ New Session Started ! }")
                print()
                continue

        ai_res = prompt(msg)
        print(colors["bg_cyan"] + colors["black"] + "Ai" + colors["reset"] +" : " , ai_res)
            
            
            
start()
