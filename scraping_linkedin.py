from selenium import webdriver
import time


link_linkedin = "https://www.linkedin.com/feed/"

def open_edge_navigator():
    navigator = webdriver.Edge()

    navigator.get(link_linkedin)

    navigator.maximize_window()

    time.sleep(10)

if __name__ == '__main__':
    open_edge_navigator()