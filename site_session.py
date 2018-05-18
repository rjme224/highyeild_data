# -*- coding: utf-8 -*-
"""
Created on Thu May 17 06:38:45 2018

@author: rjme2
"""

def sitelogin(email, password):
    import requests
    from lxml import html
    LOGIN_URL = "https://myfarm.highyieldag.com/login" 
    
    #open a persistent session to the login
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath
                              ("//input[@name='csrf_token']/@value")))[0]
    # Create payload
    payload = {
        "email": email,
        "password": password,
        "csrf_token": authenticity_token
        }
    site_session = session_requests.post(LOGIN_URL, data=payload,
                               headers=dict(referer=LOGIN_URL))
    return session_requests, site_session


    
    
    
    