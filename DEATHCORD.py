import os
import time
import random
from colorama import Fore
from discord_webhook import DiscordWebhook
import requests
from tkinter import messagebox
import webbrowser


def license():
    key = input(Fore.RED + f'[{Fore.LIGHTRED_EX}Enter license key{Fore.RED}]{Fore.RESET}: ')

    if key == 'I_SUCK_AT_MAKING_DATABASES':
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
    print(Fore.RED + '                     ▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██  ▄████▄   ▒█████   ██▀███  ▓█████▄ ')
    time.sleep(sleep_animation)
    print(Fore.RED + '                     ▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌')
    time.sleep(sleep_animation)
    print(Fore.RED + '                     ░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌')
    time.sleep(sleep_animation)
    print(Fore.RED + '                     ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌')
    time.sleep(sleep_animation)
    print(Fore.RED + '                     ░▒████▓ ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓')
    time.sleep(sleep_animation)
    print(Fore.RED + '                      ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒')
    time.sleep(sleep_animation)
    print(Fore.RED + '                      ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒')
    time.sleep(sleep_animation)
    print(Fore.RED + '                      ░ ░  ░    ░    ░   ▒    ░       ░  ░░ ░░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░')
    time.sleep(sleep_animation)
    print(Fore.RED + '                        ░       ░  ░     ░  ░         ░  ░  ░░ ░          ░ ░     ░        ░')
    time.sleep(sleep_animation)
    print(Fore.RED + '                      ░                                      ░                           ░      ')
    time.sleep(sleep_animation)
    print(Fore.RESET + '                                            github.com/FR-birdit/DEATH-CORD')
    time.sleep(sleep_animation)
    print(Fore.RESET + '                                                 discord.gg/xHuG65DvFU')
    time.sleep(sleep_animation)

    print('\n' * 2)
    time.sleep(sleep_animation)

    print(Fore.RED + '         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}01{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook message sender{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}08{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}15{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}22{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}     {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}02{Fore.RESET}] {Fore.RED}-{Fore.RESET} Webhook spamer{Fore.RESET}          {Fore.RESET}[{Fore.LIGHTRED_EX}09{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}16{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}23{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}     {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}03{Fore.RESET}] {Fore.RED}-{Fore.RESET} Message spamer{Fore.RESET}          {Fore.RESET}[{Fore.LIGHTRED_EX}10{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}17{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}24{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}     {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}04{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate tokens{Fore.RESET}         {Fore.RESET}[{Fore.LIGHTRED_EX}11{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}18{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}25{Fore.RESET}] {Fore.RED}-{Fore.RESET} Github{Fore.RESET}           {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}05{Fore.RESET}] {Fore.RED}-{Fore.RESET} Massive users spam{Fore.RESET}      {Fore.RESET}[{Fore.LIGHTRED_EX}12{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}19{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}26{Fore.RESET}] {Fore.RED}-{Fore.RESET} Discord{Fore.RESET}          {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}06{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate nitro{Fore.RESET}          {Fore.RESET}[{Fore.LIGHTRED_EX}13{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}20{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}27{Fore.RESET}] {Fore.RED}-{Fore.RESET} Tool info{Fore.RESET}        {Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + f'         ┃ {Fore.RESET}[{Fore.LIGHTRED_EX}07{Fore.RESET}] {Fore.RED}-{Fore.RESET} Generate IP{Fore.RESET}             {Fore.RESET}[{Fore.LIGHTRED_EX}14{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}21{Fore.RESET}] {Fore.RED}-{Fore.RESET} Coming soon!{Fore.RESET}  {Fore.RESET}[{Fore.LIGHTRED_EX}28{Fore.RESET}] {Fore.RED}-{Fore.RESET} Exit{Fore.RESET}         V1.1{Fore.RED}┃')
    time.sleep(sleep_animation)
    print(Fore.RED + '         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
    time.sleep(sleep_animation)

    death_cord()

print('')
def death_cord():
    try:
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
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '2':
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
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()
        elif user_input == '3':
            spam_url = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the request url\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            authorization_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Paste the token\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            spam_text = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Enter the spam text\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            repeat_spam = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many times to send message?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            payload = {'content': spam_text}

            header = {'authorization': authorization_text}

            for i in range(int(repeat_spam)):
                r = requests.post(spam_url, data=payload, headers=header)
            print(Fore.RED + f'Successfully sent {spam_text} {repeat_spam} times')

            input(Fore.LIGHTRED_EX + 'Press enter')
            start()
        elif user_input == '4':
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

        elif user_input == '5':
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
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '6':
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

        elif user_input == '7':
            sample_chars = "1234567890"
            generate_ips = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}How many to generate?\n{Fore.RED}┗{Fore.LIGHTRED_EX}')
            save_them = input(Fore.RED + f'┏{Fore.LIGHTRED_EX}Save them in ip.txt? (y/n)\n{Fore.RED}┗{Fore.LIGHTRED_EX}')

            first = ''
            second = ''
            third = ''
            fourth = ''

            for i in range(int(generate_ips)):
                repeat = random.randint(2, 3)
                for i in range(repeat):
                    first += random.choice(sample_chars)

                repeat = random.randint(2, 3)
                for i in range(repeat):
                    second += random.choice(sample_chars)

                repeat = random.randint(2, 3)
                for i in range(repeat):
                    third += random.choice(sample_chars)

                repeat = random.randint(2, 3)
                for i in range(repeat):
                    fourth += random.choice(sample_chars)

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

        elif user_input == '25':
            webbrowser.open('https://github.com/FR-birdit/DEATH-CORD')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '26':
            webbrowser.open('https://discord.gg/xHuG65DvFU')
            input(Fore.LIGHTRED_EX + 'Press enter')
            start()

        elif user_input == '27':
            print(Fore.RESET + f'Tool Name: {Fore.RED}DEATH-CORD')
            print(Fore.RESET + f'Version: {Fore.RED}1.1')
            print(Fore.RESET + f'Maded on: {Fore.RED}Pyhton 3.12')
            print(Fore.RESET + f'Creator: {Fore.RED}FR')
            print(Fore.RESET + f'Platform: {Fore.RED}Windows 10/Widnows 11')
            print(Fore.RESET + f'Github: {Fore.RED}https://github.com/FR-birdit/DEATH-CORD')
            print(Fore.RESET + f'Discord: {Fore.RED}https://discord.gg/xHuG65DvFU')

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