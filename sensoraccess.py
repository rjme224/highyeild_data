import requests
from lxml import html
import pandas as pd
import io


USERNAME = "rj.merrick@ufl.edu"
PASSWORD = "P^thon32"
csv_loc = 'HphickbrtNE7'

def highyield(email, password, csv_loc):
    
    LOGIN_URL = "https://myfarm.highyieldag.com/login"
    URL = "http://myfarm.highyieldag.com/getcsv/{}/0".format(csv_loc)

    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]
    # Create payload
    payload = {
            "email": USERNAME, 
            "password": PASSWORD, 
            "csrf_token": authenticity_token
            }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

        # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))


    df = pd.read_csv(io.StringIO(result.text), index_col = 0)
    return df