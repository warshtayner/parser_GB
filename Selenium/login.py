from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebD
from selenium.webdriver.support import expected_conditions as EC

service = Service('./chromedriver')
driver = webdriver.Chrome(service=service)