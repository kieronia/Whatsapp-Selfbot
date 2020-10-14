
from selenium import webdriver
import sys, pathlib, time, os, requests, random,choice, datetime
from colorama import Fore, init, Back, Style
init(convert=True)

driver = webdriver.Chrome(executable_path= r'C:\Users\kieronia\.wdm\drivers\chromedriver\win32\84.0.4147.30\lel\chromedriver.exe')
#chromedriver path here 

count = 0
newcount = 0

os.system("title Whatsapp Selfbot Demonstration!")


logo = f"""
{Fore.WHITE} > {Fore.GREEN}██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗ ██████╗ 
 {Fore.WHITE}>{Fore.GREEN} ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗
 {Fore.WHITE}>{Fore.GREEN} ██║ █╗ ██║███████║███████║   ██║   ███████╗███████║██████╔╝██████╔╝
{Fore.WHITE} >{Fore.GREEN} ██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██╔══██║██╔═══╝ ██╔═══╝ 
 {Fore.WHITE}>{Fore.GREEN} ╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║██║  ██║██║     ██║     
 {Fore.WHITE}>{Fore.GREEN}  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                   
 {Fore.WHITE}>{Fore.GREEN} ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗         
 {Fore.WHITE}>{Fore.GREEN} ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝         
 {Fore.WHITE}>{Fore.GREEN} ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║            
 {Fore.WHITE}>{Fore.GREEN} ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║            
 {Fore.WHITE}>{Fore.GREEN} ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║            
 {Fore.WHITE}>{Fore.GREEN} ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝         
 {Fore.WHITE}>{Fore.GREEN} For more demonstrations, visit https://github.com/kieronia
"""                                           

print(f"{Fore.GREEN}{logo}")
driver.get("https://web.whatsapp.com/")
os.system("cls")
input(f"{logo}\n{Fore.RED} > {Fore.WHITE}Please Login And Select A Conversation \n {Fore.RED}> {Fore.WHITE}Press Enter When Logged In And In A Conversation \n {Fore.RED}> {Fore.WHITE}")
os.system("cls")



while True:
    try:
        message = driver.find_element_by_xpath(f'//*[@id="main"]/div[3]/div/div/div[3]/div[{count}]/div/div/div/div[1]/div/span[1]/span').text
        message = message.lower()
        
        #print(message) #used this too visualise processes when making it, if your looking for a smooth experience then leave this commented out, if your tryna learn from my code I reccomend printing...
        if message == "!help":
            print("!help requested")
            messagebox = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            messagebox.send_keys("You requested the help command - this is demonstration project of a selfbot through selenium from https://github.com/kieronia/Whatsapp-Selfbot - Enjoy")
            time.sleep(0.1)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            newcount = count + 1

        elif "!spam" in message:
            message = message.replace("!spam","")
            print("!spam requested")
            for i in range(0,10):
                messagebox = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                messagebox.send_keys(message)
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            newcount = count + 1

        elif "!ascii" in message:
            message = message.replace("!ascii","")
            print("!ascii requested")
            link = f"http://artii.herokuapp.com/make?text={message}"
            asciiart = requests.get(link).text
            messagebox = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')#if enter = send this will look TERRIBLE
            messagebox.send_keys(asciiart)
            time.sleep(0.1)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            newcount = count + 1                        
        elif "!time" in message:
            print("!time requested")
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            messagebox = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            messagebox.send_keys(f"The current time is {hour}:{minute}:{second}")
            time.sleep(0.1)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            newcount = count + 1                    
        elif "!rickroll" in message:
            print("!rickroll requested")
            rickrolllyircs = requests.get("https://pastebin.com/raw/wwvdjvEj").text
            messagebox = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            messagebox.send_keys(rickrolllyircs)
            time.sleep(0.1)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            newcount = count + 1    

        elif "!8ball" in message:
            message = message.replace("!8ball","")
            print("!8ball requested")
            balie = ["no", "Duhhh.", "Obviously", "Maybe", "Shut up dude ", "yes", "I don't care", "Ask again later", "Don't count on it", "Most likely", "Without a doubt", "bruh stop bugging me", "outlook good", "Concentrate and ask me again", "you've got to be kidding me ", "ofc!", "yeah mate", "I'll win the lottery before that happens", "bro you're stupid for even thinking that","The ball is in your court"]
            balloutcome = choice(balie)
            messagebox = driver.find_element_by_xpath(f'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            messagebox.send_keys(f"{balloutcome} // In answer to your question '{message}'")
            time.sleep(0.1)
            driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
            newcount = count + 1    


    except:
        pass


    count = count + 1  
    if count > 300:
        count = newcount
