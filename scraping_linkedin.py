from selenium import webdriver
import time


def open_edge_navigator():
    navigator = webdriver.Edge()
    time.sleep(10)

if __name__ == '__main__':
    open_edge_navigator()