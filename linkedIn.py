# The various libraries need to be imported to make the job much quicker
# These contain useful pre-written code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import math
import random
import requests
import datetime
import csv
import LinkedInParam
from time import sleep
from bs4 import BeautifulSoup





driver = webdriver.Firefox(executable_path= "C:\\BrowserDrivers\\geckodriver.exe")

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
profile.update_preferences()

driver.get(url='https://www.linkedin.com/')
sleep(1)

# Giriş Yap düğmesini buluyoruz.
sign_in = driver.find_element(by='link text', value='Oturum aç')
sign_in.click()
sleep(3)

# Girdi bölümünü bulup kullanıcı bilgilerimizi giriyoruz.
email_entry = driver.find_element(by='css selector', value='#username')
password_entry = driver.find_element(by='css selector', value='#password')

# For every letter in our email, we will set a random time between keystrokes
for letter in LinkedInParam.username:
    sleep(random.uniform(.1, .4))
    email_entry.send_keys(letter)

# Şifremizin her harfi için, 0.1 ve 0.4 sn arasında rastgele bir süre bekliyoruz.
for letter in LinkedInParam.password:
    sleep(random.uniform(.1, .4))
    password_entry.send_keys(letter)

# Enter tuşuna basıyoruz
password_entry.send_keys(Keys.RETURN)
sleep(5)

# Arama alanını bulup tıklıyoruz.
search_bar = driver.find_element(by='css selector', value='.search-global-typeahead__input')
search_bar.click()
sleep(.5)

# for letter in job_role:
#    sleep(random.uniform(.1, .4))
#    search_bar.send_keys(letter)

#    search_bar.send_keys(Keys.RETURN)
#    sleep(1)


is_ilanlari = driver.find_element_by_link_text("İş İlanları")
is_ilanlari.click()

sleep(2)

job_search_bar = driver.find_element_by_class_name("jobs-search-box__text-input")
job_search_bar.click()
sleep(1.5)

for letter in LinkedInParam.desired_job:
   sleep(random.uniform(.1, .4))
   job_search_bar.send_keys(letter)

job_search_bar.send_keys(Keys.RETURN)
sleep(3)

source = requests.get(driver.current_url).text
soup = BeautifulSoup(source, 'lxml')

i = 0
j = 0

writer = csv.writer(open(LinkedInParam.file_name, 'w', encoding='utf-8'))

writer.writerow(['Job_Title', 'Job_Description', 'company', 'location ', 'Industry', 'Employment_type', 'Job Function',
                 'Experience_Level'])

while (j < 10):

    present_url = 'https://www.linkedin.com/jobs/search/?keywords=' + LinkedInParam.desired_job + '&location=' + LinkedInParam.desired_location + '&start=' + str(i)

    driver.get(present_url)
    scroll = driver.find_element_by_class_name('jobs-search-results')
    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    scroll.send_keys(Keys.PAGE_DOWN)

    sleep(1)

    # ActionChains(driver).move_to_element(
    #     driver.find_element_by_class_name('search-results-pagination-section')).perform()

    jobs = driver.find_elements_by_class_name('job-card-search__title')

    for job in jobs:
        current_url = driver.current_url

        try:
            job.click()
        except:
            pass

        try:
            company_name = driver.find_element_by_class_name('jobs-details-top-card__company-url')
            company_name = company_name.text

            if company_name:
                company_name = company_name.strip()
        except:
            company_name = None

        try:
            job_name = driver.find_element_by_class_name('jobs-details-top-card__job-title')
            job_name = job_name.text

            if job_name:
                job_name = job_name.strip()
        except:
            job_name = None

        try:
            job_description = driver.find_element_by_xpath('//*[@id="job-details"]')
            job_description = job_description.text

            if job_description:
                job_description = job_description.strip()
        except:
            job_description = None

        try:
            employement_type = driver.find_element_by_class_name('js-formatted-employment-status-body')
            employement_type = employement_type.text

            if employement_type:
                employement_type = employement_type.strip()
        except:
            employement_type = None

        try:
            industry = driver.find_element_by_class_name('js-formatted-industries-list')
            industry = industry.find_elements_by_class_name('jobs-box__list-item')
            industry = [ind.text for ind in industry]
            industry = ','.join(industry)

            if industry:
                industry = industry.strip()
        except:
            industry = None

        try:
            location = driver.find_element_by_class_name('jobs-details-top-card__bullet')
            location = location.text

            if location:
                location = location.strip()
        except:
            location = None

        try:
            job_function = driver.find_element_by_class_name('js-formatted-job-functions-list')
            job_function = job_function.text

            if job_function:
                job_function = job_function.strip()
        except:
            job_function = None

        try:
            experience_Level = driver.find_element_by_class_name('js-formatted-exp-body')
            experience_Level = experience_Level.text

            if experience_Level:
                experience_Level = experience_Level.strip()
        except:
            experience_Level = None

        writer.writerow([job_name, job_description, company_name, location, industry, employement_type,
                         job_function, experience_Level, current_url])
        sleep(2)

    i = i + 25

    j = j + 1

print("İşlem tamamlandı..." + "program kapatılıyor!")
driver.quit()