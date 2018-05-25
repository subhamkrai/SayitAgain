#!/usr/bin/python3

from selenium import webdriver


YouTube_Search = "https://www.youtube.com/results?search_query="

def start_browser():
    return webdriver.Firefox('/usr/bin/geckodriver-v0.20.1-linux64/')

def Y_Search(query):
    browser = start_browser()
    browser.get(YouTube_Search+query)
    elem = browser.find_element_by_id('video-title')
    elem.click()
