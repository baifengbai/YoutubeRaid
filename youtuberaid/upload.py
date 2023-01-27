import random
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()


options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\youss\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
print("\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory. Please make sure to name the video files like this --> Ex: vid1.mp4 vid2.mp4 vid3.mp4 etc..")
time.sleep(6)
if(True):
    print("\033[1;31;40m IMPORTANT: Please make sure the name of the videos are like this: vid1.mp4, vid2.mp4, vid3.mp4 ...  etc")
    dir_path = '.\\finalvideos'
    count = 0

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print("   ", count, " Videos found in the videos folder, ready to upload...")
    time.sleep(6)

    for i in range(count):
        bot = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

        bot.get("https://studio.youtube.com")
        time.sleep(3)
        upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()
        time.sleep(1)

        file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
        simp_path = 'finalvideos/vid{}.mp4'.format(str(i+1))
        abs_path = os.path.abspath(simp_path)
        
        file_input.send_keys(abs_path)

        time.sleep(7)

        next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
        

        

        for i in range(3):
            next_button.click()
            time.sleep(1)

        done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
        
        done_button.click()
        time.sleep(5)
        bot.quit()




