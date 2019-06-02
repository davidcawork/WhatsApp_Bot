from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os



# Main 
def main():

    #Enter in Whatsapp Web and validate account
    try:    
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://web.whatsapp.com/")
        input('Please enter the QR code, press any key to continue...')
    except:
        print('[ERROR] It has been impossible to enter WhatsApp Web...')

    os.system('cls')
    print('Welcome! n.n')
    while True:
        
        cmd = input()

        if isCMD_msg(cmd) == '/msg':
            list_msg = Parse_msg(cmd)

            send_msg(list_msg,driver)



#To parse cmd
def isCMD_msg(cmd):
    return cmd.split(' ')[0]

#To parse msg command to a list [count, person, msg]
def Parse_msg(cmd):
    # /msg [count] person@msg
      
    list_aux = []

    #Count msg
    list_aux.append((cmd.split('[')[1]).split(']')[0])

    #Person or Group
    list_aux.append((cmd.split('] ')[1]).split('@')[0])

    #Msg
    list_aux.append((cmd.split('] ')[1]).split('@')[1])


    return list_aux

#To send
def send_msg(list_msg,driver):

    #To enter into a chat (You can delete this, its was only for me)
    if list_msg[1] == 'Yuli':
        list_msg[1] = 'Yuli 🐢'
    
   
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(list_msg[1]))
    user.click()


    msg_box = driver.find_elements_by_class_name('_13mgZ')
    for i in range(int(list_msg[0])):
        msg_box[0].send_keys(list_msg[2])
        driver.find_element_by_class_name('_3M-N-').click()

if __name__ == '__main__':
    main()
