import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import platform

# List of tokens
TOKENS = [
    "52894d31200fcfd79ce2efe68919da64",
    "6215269b094249c56747a7ed7050d7c7",
    "f50fe0c29a5ece318119849ee3b1c3ee"
]

def get_news_details(auth_token):
    options = webdriver.ChromeOptions()

    if platform.system() == 'Darwin':
        options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    elif platform.system() == 'Windows':
        options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.coingecko.com/zh/candy")

    if not auth_token or auth_token == "YOUR_GOOGLE_AUTH_TOKEN_HERE":
        raise ValueError("Access token is missing. Please configure it properly.")

    # Set the session_id cookie
    driver.add_cookie({"name": "_session_id", "value": auth_token})

    # Wait for the page to load
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    driver.refresh()

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the page source
    html = driver.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find the button
    button = driver.find_element(By.ID, "collectButton")
    button_text = soup.find('button', {'id': 'collectButton'}).text.strip()
    balance_div = soup.find('div', {'data-candy-target': 'balance'}).text

    return balance_div, button,button_text

# Iterate over the tokens and perform sign-in
for i, token in tqdm(enumerate(TOKENS), total=len(TOKENS), desc="Signing in"):
    balance_div, button, button_text = get_news_details(token)
    if button_text == 'Collect Candy':
        button.click()
    else:
        print(balance_div)

    random_interval = random.randint(12, 24) * 3600
