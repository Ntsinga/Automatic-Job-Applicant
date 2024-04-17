from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_path=r"C:\Users\USER\Dev\chromedriver-win64\chromedriver.exe"
service=Service(executable_path=chromedriver_path)
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome(service=service,options=options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3800645463&geoId=106943612&keywords=Python%20Developer&location=Uganda&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true&sortBy=R")

signIn_button1=driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
signIn_button1.click()
email=WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"#username")))
email.send_keys('example@gmail.com')
password=driver.find_element(By.CSS_SELECTOR,"#password")
password.send_keys("password")
signIn_button2=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
signIn_button2.click()

job_offers=WebDriverWait(driver,10).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".disabled")))

for job in job_offers:
    job.click()
    # dropdown=WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="ember39"]/svg/use')))
    # dropdown.click()
    save_button=driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    save_button.click()
    follow_button=WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/section/section/div[1]/div[1]/button/span')))
    driver.execute_script("arguments[0].scrollIntoView(true);", follow_button)
    follow_button.click()
