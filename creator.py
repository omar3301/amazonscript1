import os
try:from selenium import webdriver
except:os.system('pip install selenium')
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
try:from PIL import ImageGrab, ImageOps, Image, ImageSequence
except:
    os.system('pip install PILL')
    os.system('pip install pillow')
import PIL.Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
try:from twocaptcha import TwoCaptcha
except:
    os.system('pip install twocaptcha')
    os.system('pip install 2captcha-python')
try:import imageio.v2 as imageio
except:os.system('pip install imageio')
import subprocess
import time
import sys
try:from colorama import init, Fore, Back, Style
except:os.system('pip install colorama')
try:from licensing.models import *
except:os.system('pip install licensing')
from licensing.methods import Key, Helpers
try:import requests
except:os.system('pip install requests')
try:from faker import Faker
except:os.system('pip install faker')
import random
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
import nopecha
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

import winsound
init(autoreset=True)
nopecha.api_key = 'uccbwfrpk1_DAZ9EXN5'
balance = nopecha.Balance.get()
credit = balance['credit']

nopecha.api_key = 'I-901878RNSYEA'
balance = nopecha.Balance.get()
credit1 = balance['credit']

creditapi = requests.get('https://vak-sms.com/api/getBalance/?apiKey=8e98f9facdb1472aa561ea7c74e61bc6')

creditphone = creditapi.json()['balance']

creditapi1 = requests.get('https://vak-sms.com/api/getBalance/?apiKey=087b267dc7aa4f6aaae555b766ef1a65')
creditphone1 = creditapi1.json()['balance']
options = Options()
prefs = {
  "translate_whitelists": {"fr":"en"},
  "translate":{"enabled":"true"}
}
options.add_experimental_option("prefs", prefs)

def delet_line(file_name, line_number):
    with open(file_name) as file :
        lines = file.readlines()
        del lines[line_number]
        with open(file_name, 'w') as file:
            for line in lines:
                file.write(line)
def addToNote(file_name, type1):
    file111 = open(file_name, "a")
    file111.writelines(type1)
    file111.writelines('\n')
    file111.close() 
    
print(Fore.MAGENTA+'[1]'+Style.BRIGHT+Fore.GREEN+ ' mail.ru')
print(Fore.MAGENTA+'[2]'+Style.BRIGHT+Fore.GREEN+ ' outlook.com')
print(Fore.MAGENTA+'[3]'+Style.BRIGHT+Fore.GREEN+ ' hotmail.com')
print('\n')
typeM = input('>')
if typeM == '1':typeM = 'mail.ru'
if typeM == '2':typeM = 'outlook.com'
if typeM == '3':typeM = 'hotmail.com'

renga = int(input('Numper =>'))

print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' uccbwfrpk1_DAZ9EXN5' +'=>'+ Fore.YELLOW + str(credit) )
print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' I-901878RNSYEA' + '=>'+ Fore.YELLOW + str(credit1) )
nopechaapi = input('key => ')

if nopechaapi == 'A' or nopechaapi == 'a':
    nopechaapi = 'uccbwfrpk1_DAZ9EXN5'
if nopechaapi == 'B' or nopechaapi == 'b':
    nopechaapi = 'I-901878RNSYEA'
    
print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' vak-sms')
print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' sms-acktiwator.ru')
method = input('method => ')

if method == 'A' or method == 'a' :
    print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' RU 2 RUB')
    print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' PH 2 RUB')
    country = input('country => ')
    if country == 'A' or country == 'a':
        country = 'ru'
        code = 'RU'
        operator = 'patriot'
        precode = '7'
    if country == 'B' or country == 'b' :
        country = 'ph'
        code = 'ph'
        operator = 'smart'
        precode = '63'
    print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' phone gosu'+'=>'+ Fore.YELLOW + str(creditphone))
    print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' phone youpi'+'=>'+ Fore.YELLOW + str(creditphone1))
    api = input('vak api => ')
    if api == 'A' or api == 'a':
        api = '8e98f9facdb1472aa561ea7c74e61bc6'
    if api == 'B' or api == 'b':
        api = '087b267dc7aa4f6aaae555b766ef1a65'
        
if method == 'B' or method == 'b' :
    print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' RU 1 RUB')
    print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' UK 7 RUB')
    country = input('country => ')
    if country == 'A' or country == 'a':
        code = 'RU'
        precode = '+7'
    if country == 'B' or country == 'b' :
        code = 'GB'
        precode= '+44'
        
        
print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' yescaptha')
print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' nopecha ')
captha = input('captha solver => ')
if captha.lower() == 'a':
    extension_directory_1 = r"./yescaptha/"
    extension_directory_2 = r"./pva extension/"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--load-extension=" + extension_directory_1)


elif captha.lower() == 'b':

    
    options = webdriver.ChromeOptions()
    options.add_extension('dknlfmjaanfblgfdfebhijalfmhmjjjo.crx')


print(Fore.BLUE+'[A]'+Style.BRIGHT+Fore.GREEN+ ' yes')
print(Fore.BLUE+'[B]'+Style.BRIGHT+Fore.GREEN+ ' no')
proxy = input('captha proxy => ')
if proxy.lower() == 'a':
    extension_directory_1 = r"./yescaptha/"
    extension_directory_2 = r"./pva extension/"
    extension_directory_3 = r"./nopecha/"
    
    options = webdriver.ChromeOptions()
    if captha == 'A' or captha == 'a':
        options.add_argument("--disable-extensions-except=" + extension_directory_1 + "," + extension_directory_2) 
    if captha == 'B' or captha == 'b':
        options.add_argument("--disable-extensions-except=" + extension_directory_2+ "," + extension_directory_1) 
elif proxy.lower() == 'b':
    if captha == 'B' or captha == 'b' :
        extension_directory_1 = r"./yescaptha/"
        extension_directory_2 = r"./pva extension/"
        extension_directory_3 = r"./nopecha/"
        options.add_argument("--disable-extensions-except=" + extension_directory_3) 
        options = webdriver.ChromeOptions()
    
token = 'daa09aa66d274cff011e0e13b20ed44d' #email
api1 = '8709ed88b790acf14f0bd4791759b29b99606e83' #sms-acktiwator.ru
service = 'am'


status = 'send'

#chrome_options = webdriver.ChromeOptions()

#PROXY = random.choice(open('proxy.txt').readlines()).split(',')[0]
#print(PROXY)
#options = webdriver.ChromeOptions()
options.add_argument("--window-size=1980,1080")
options.add_argument("--window-position=-2000,0")
#options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_extension('dknlfmjaanfblgfdfebhijalfmhmjjjo.crx')
#options.add_extension('dknlfmjaanfblgfdfebhijalfmhmjjjo.crx')
options.add_extension('hupvpn.crx')

#options.add_extension('vpn.crx')


#options.add_argument('--proxy-server=%s' % PROXY)

while True:
    os.system('cls')
    driver = webdriver.Chrome(options=options)
    act = ActionChains(driver)


    time.sleep(5)
    try:
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
    except:pass
    if captha == 'B' or captha == 'b' :
        driver.get('https://nopecha.com/setup#'+nopechaapi+'|awscaptcha_auto_solve=true|awscaptcha_solve_delay=true|awscaptcha_solve_delay_time=1000|disabled_hosts=|enabled=true|funcaptcha_auto_open=true|funcaptcha_auto_solve=true|funcaptcha_solve_delay=true|funcaptcha_solve_delay_time=1000|hcaptcha_auto_open=true|hcaptcha_auto_solve=true|hcaptcha_solve_delay=true|hcaptcha_solve_delay_time=3000|uccbwfrpk1_DAZ9EXN5|perimeterx_auto_solve=false|perimeterx_solve_delay=true|perimeterx_solve_delay_time=1000|recaptcha_auto_open=true|recaptcha_auto_solve=true|recaptcha_solve_delay=true|recaptcha_solve_delay_time=2000|textcaptcha_auto_solve=false|textcaptcha_image_selector=|textcaptcha_input_selector=|textcaptcha_solve_delay=true|textcaptcha_solve_delay_time=100|turnstile_auto_solve=true|turnstile_solve_delay=true|turnstile_solve_delay_time=1000')

    time.sleep(5)
    try:
        for x in range(renga):  
            
            while True:                                              #Sign up
                r = requests.get('https://api.kopeechka.store/mailbox-get-email?site=amazon.com&mail_type='+typeM+'&sender=&regex=&token='+token+'&soft=&investor=&type=&subject=&clear=&api=2.0')      
                id = r.json()['id']
                Amazon_mail = r.json()['mail']
                print(Amazon_mail + Fore.GREEN + ' => created > ' + Fore.YELLOW + str(x) )
                x = x + 1
                time.sleep(2)
                driver.get('https://www.amazon.fr/ap/register?showRememberMe=true&openid.pape.max_auth_age=900&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=frflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.fr%2Fap%2Fcnep%3Fie%3DUTF8%26orig_return_to%3Dhttps%253A%252F%252Fwww.amazon.fr%252Fyour-account%26openid.assoc_handle%3Dfrflex%26pageId%3Dfrflex&prevRID=KR9N5KZE1NHGE1CMBKWY&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
                if "Enter the characters you see below" in driver.page_source :
                    driver.refresh()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((
                    By.XPATH, '//*[@id="ap_customer_name"]'))).send_keys('omarus')
                time.sleep(0.1)
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((
                    By.ID, 'ap_email'))).send_keys(Amazon_mail)
                time.sleep(0.1)
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((
                    By.ID, 'ap_password'))).send_keys(Amazon_mail)
                time.sleep(0.1)
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((
                    By.ID, 'ap_password_check'))).send_keys(Amazon_mail)
                time.sleep(0.1)
                driver.find_element(By.XPATH,'//*[@id="continue"]').click()

                if 'Email address already in use' in driver.page_source:             #alreadyUsed error(1)
                    requests.get('https://api.kopeechka.store/mailbox-cancel?id='+id+'&token='+token+'&type=json&api=2.0')
                    x = x - 1
                    continue
                break

            if 'Email address already in use' in driver.page_source:             #alreadyUsed error(1)
                requests.get('https://api.kopeechka.store/mailbox-cancel?id='+id+'&token='+token+'&type=json&api=2.0')
                x = x - 1
                continue

            driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))
            while True:                                                          #Contniue next tap   --  Put in prossinng -- put ID
                if "Solve this puzzle to protect your account" in driver.page_source:
                    addToNote('prossinng.txt', Amazon_mail+':'+id)
                    addToNote('IDMail.txt', id)
                    driver.switch_to.default_content()
                    if x < renga:
                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[x])
                    break
        for o in range(renga):                                                    #Captcha    --   OTP MAIL
            driver.switch_to.window(driver.window_handles[o])

            if 'Internal Error. Please try again later.' in driver.page_source: 
                print('help')      #get InternalERROR(2)
                winsound.Beep(1000, 50)
                winsound.Beep(2000, 100)
                winsound.Beep(500, 100)

            try:driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))
            except:pass
            try:
                if "Time limit exceeded. Please try again." in driver.page_source :
                    time.sleep(6)
                WebDriverWait(driver, 6).until(EC.presence_of_element_located((      
                    By.ID, "amzn-btn-audio-internal"))).click()
                print('audio')
                time.sleep(3)
                while True:
                    if "Enter your response" in driver.page_source:
                        audioDATA = driver.find_element(By.TAG_NAME,'audio').get_attribute('src')
                        nopecha.api_key = 'uccbwfrpk1_DAZ9EXN5'
                        # Call the Recognition API
                        text = nopecha.Recognition.solve(
                            type='awscaptcha',
                            audio_data=[audioDATA.removeprefix('data:audio/acc;base64,')]
                        )
                    # Print text to type
                    print(text)
                    driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div[2]/div/div[3]/div[2]/input').send_keys(text)
                    time.sleep(0.5)
                    driver.find_element(By.ID,'amzn-btn-verify-internal').click()
                    time.sleep(4)
                    try:
                        driver.find_element(By.ID,'amzn-btn-verify-internal')
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((      
                            By.ID, "amzn-btn-refresh-internal"))).click()
                        time.sleep(2)
                        continue
                    except:break
            except:pass
            
            driver.switch_to.default_content()
            time.sleep(1)

            #if 'Internal Error. Please try again later.' in driver.page_source: print(YG)      #get InternalERROR(2)

            while True:                                                                  #OTP MAIL        --     PUT NosDone
                if "Verify email address" in driver.page_source:break
            Amazon_mail,id = open('prossinng.txt').readline().rstrip('\n').split(':')
            while True:
                r = requests.get('https://api.kopeechka.store/mailbox-get-message?full=&id='+id+'&token='+token+'&type=json&api=2.0')
                time.sleep(1)
                if r.json()['value'] == 'WAIT_LINK':                                     #Wait OTP mail
                    print(Amazon_mail+Fore.CYAN+' > Wait OTP Mail')
                    continue
                break
            soup = BeautifulSoup(r.json()['fullmessage']) 
            OTP = str(soup.find_all('p',attrs={"class":"otp"})).removeprefix('[<p class="otp">').removesuffix('</p>]')
            print(Amazon_mail+Fore.CYAN+ ' > '+ OTP + ' > ' + Fore.YELLOW + str(o))
            driver.find_element(By.NAME,'code').send_keys(OTP)
            time.sleep(0.5)
            driver.find_element(By.CLASS_NAME,'a-button-input').click()
            delet_line('prossinng.txt', 0)                                                #clear prossinng
            addToNote('Nosdone.txt', Amazon_mail)

        if method == 'A' or method == 'a':
            r = requests.get('https://vak-sms.com/api/getNumber/?apiKey='+api+'&service='+service+'&country='+country+'&operator='+operator+'&softId=en')
            idNum = r.json()['idNum']
            A_N = str(r.json()['tel']).removeprefix(precode)                                       #createNEW number
            print(A_N + Fore.GREEN + '=> created vak-sms')
        if method == 'B' or method == 'b' :
            r = requests.get('https://sms-acktiwator.ru/api/getnumber/'+api1+'?id=45&code='+code+'')
            idNum = str(r.json()['id'])
            A_N = str(r.json()['number']).removeprefix(precode)
            print(A_N + Fore.GREEN + '=> created sms-acktiwator')
        for y in range(renga):                                                             #put Number    --    wait otp phone
            driver.switch_to.window(driver.window_handles[y])
            while True:
                if "Add mobile number" in driver.page_source:break

            driver.switch_to.default_content()
            time.sleep(1)
            driver.find_element(By.NAME,'cvf_phone_cc').send_keys(code.upper())
            driver.find_element(By.XPATH, '//*[@id="cvf-page-content"]/div/div/div/form/div[1]/div/div[2]/div/div[2]/input').send_keys(A_N)
            time.sleep(1)
            driver.find_element(By.NAME,'cvf_action').click()
            time.sleep(1)
            while True:
                if "It looks like you've requested a new OTP recently." in driver.page_source:
                    time.sleep(2)
                    driver.find_element(By.XPATH,'//*[@id="a-autoid-0"]/span/input').click()
                    time.sleep(2)
                    continue
                break
            tt = 0
            while True:
                tt = tt + 1
                time.sleep(1)
                if method == 'A' or method == 'a':
                    r2 = requests.get('https://vak-sms.com/api/getSmsCode/?apiKey='+api+"&idNum="+idNum+'&all')
                    print(r2.json())
                    if tt >= 30:
                        driver.find_element(By.NAME,'cvf_action').click()
                        tt = 0
                    if r2.json()['smsCode'] == None:continue                                   #waiting otp phone
                    OTP = r2.json()['smsCode'][y]   
                if method == 'B' or method == 'b' :
                    r2 = requests.get('https://sms-acktiwator.ru/api/getstatus/'+api1+'?id='+idNum+'')
                    print(r2.json())
                    if tt >= 30:
                        try:
                            driver.find_element(By.XPATH,'//*[@id="cvf-resend-code-section"]/a').click()
                            tt = 0
                        except:pass
                    if r2.json()== None:continue
                    OTP = str(r2.json()['small'])
                
                break
            driver.find_element(By.NAME,'code').send_keys(OTP)
            act.send_keys(Keys.TAB).perform()
            #if "The phone number you've entered already exists with another account." in driver.page_source : print(YG)
            time.sleep(0.1)
            #if 'Internal Error. Please try again later.' in driver.page_source: print(YG)
            if method == 'A' or method == 'a':
                requests.get('https://vak-sms.com/api/setStatus/?apiKey='+api+'&status=send&idNum='+str(idNum))
            if method == 'B' or method == 'b' :
                requests.get('https://sms-acktiwator.ru/api/play/'+api1+'?id='+idNum+'')
            if y != renga-1:time.sleep(10)

        for r in range(renga):
            driver.switch_to.window(driver.window_handles[r])
            act.send_keys(Keys.ENTER).perform()
            if r == 0:
                time.sleep(4)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((
                    By.ID,'auth-cnep-edit-phone-button'))).click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((
                    By.ID,'ap_delete_mobile_claim_link'))).click()
                time.sleep(2)
                act.send_keys(Keys.TAB).perform()
                time.sleep(0.1)
                act.send_keys(Keys.TAB).perform()
                time.sleep(0.5)
                act.send_keys(Keys.ENTER).perform()
                time.sleep(2)

        while True:
            try:                                         #Cancel Emails Done
                id = open('IDMail.txt').readline().rstrip('\n')
                requests.get('https://api.kopeechka.store/mailbox-cancel?id='+id+'&token='+token+'&type=json&api=2.0')
                delet_line('IDMail.txt', 0)
            except:break

        while True:
            try:                                         #transfare to DONE
                acc = open('Nosdone.txt').readline().rstrip('\n')
                addToNote ('Done.txt', acc)
                delet_line('Nosdone.txt', 0)
            except:break
        
        os.remove('Nosdone.txt')
        os.remove('prossinng.txt')
        driver.quit()

    except:
        frequency = 2000
        # Set duration to 1500 milliseconds (1.5 seconds)
        duration = 500
        # Make beep sound on Windows
        winsound.Beep(frequency, duration)
        winsound.Beep(200, 100)
        winsound.Beep(1000, 50)
        winsound.Beep(2000, 100)
        winsound.Beep(500, 100)
        time.sleep(2)
        driver.find_element(By.TAG_NAME,'body').screenshot('./Errs/'+'YG'+'.png')
        while True:
            try:                                          #Cancel Emails Err
                id = open('IDMail.txt').readline().rstrip('\n')
                requests.get('https://api.kopeechka.store/mailbox-cancel?id='+id+'&token='+token+'&type=json&api=2.0')
                delet_line('IDMail.txt', 0)
            except:break

        os.remove('prossinng.txt')
        os.remove('Nosdone.txt')
        input('Err')
