from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyperclip as pc
from webdriver_manager.chrome import ChromeDriverManager

class DiceRoomGenerator:
    def __init__(self):
        self.ROOM_LINK = ""
        self.SITE_LINK = "https://www.rollfunkydice.com/"
        self.SITE_MAP = {
            "buttons": {
                "generate": {
                    "xpath": '//*[@id="gatsby-focus-wrapper"]/div/main/div/div[1]/p/button'
                },
                "enter": {
                    "xpath": '//*[@id="roomTop"]/div[2]/div/div[2]/button'
                },
                "room_link": {
                    "xpath": '//*[@id="gatsby-focus-wrapper"]/div/main/div/div/div/div[1]/button'
                }
            },
            "inputs": {
                "name": {
                    "xpath": '//*[@id="name"]'
                }
            }
        }

        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.SITE_LINK)
        sleep(1)

    def generate_room(self):
        create_button = self.browser.find_element(By.XPATH,self.SITE_MAP["buttons"]["generate"]["xpath"])
        create_button.click()
        sleep(1)

    def enter_room(self):
        if self.ROOM_LINK == "":
            enter_button = self.browser.find_element(By.XPATH, self.SITE_MAP["buttons"]["enter"]["xpath"])
            enter_button.click()
            sleep(1)
        else:
            sleep(1)
            self.browser.get(self.ROOM_LINK)
            sleep(1)
    
    def get_room_link(self):
        link_button = self.browser.find_element(By.XPATH, self.SITE_MAP["buttons"]["room_link"]["xpath"])
        link_button.click()
        sleep(1)
        room_link = pc.paste()
        self.ROOM_LINK = room_link

        return room_link

    def close(self):
        self.browser.close()




