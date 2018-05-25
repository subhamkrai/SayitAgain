#!/usr/bin/python3

import webbrowser as wb

Google_Search = "https://www.google.com/search?q="

def G_Search(query):
    wb.open_new_tab(Google_Search + query)
