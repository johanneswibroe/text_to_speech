from selenium import webdriver
import pywinauto
from pywinauto.keyboard import send_keys
import time

#Given a txt file with a list of words in it (one on each line), 
#this script will go to an online text to speech synthesizer
#and download each word. This will be done by using pywinauto to "move"
#the cursor to the download button in the browser(!!!)



#opens up your file with the words within them
with open( "path", "r") as f:
    wordstring=f.read()
#splits into a python list
wordlist = wordstring.split()
print (wordlist)

for word in wordlist:

    #opens up chrome on selenium's server
    driver = webdriver.Chrome()
    #goes to the chosen website
    driver.get('https://voicegenerator.io/')
    driver.maximize_window()
    textbox=driver.find_element_by_id("inputArea")
    textbox.clear()
    textbox.send_keys(word)
    #finds the downloadbutton by id. 
    downloadbutton=driver.find_element_by_id("downloadBtn").click()
    #waits 1 second, to allow the browser to load.
    time.sleep(1)
    
    send_keys("{ENTER}")
    
    #this part moves the cursor to the button! Mileage may vary,
    #so play around with the coordinates for moving the cursor
    pywinauto.mouse.click(button='left', coords=(1410, 750))
    time.sleep(1)
    pywinauto.mouse.click(button='left', coords=(1380, 720))
    time.sleep(1)
    driver.quit()

#river.find_element_by_xpath("//select/option[@value='Google UK English Female']").click()
#dropdown.click()
 
 
