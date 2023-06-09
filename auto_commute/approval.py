"""
module that automate commute approval task
"""
# Author : Lotimuah <kwmg0754@gmail.com>

import os, random, time
from pytz import timezone
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--email", type=str)
    parser.add_argument("--passwd", type=str)

    args = parser.parse_args()

    os.makedirs("./screen_shots", exist_ok=True)
    login_url    = "https://dashboard.wantedspace.ai/auth/email"
    approval_url = "https://dashboard.wantedspace.ai/approval/sent"

    now         = datetime.now(timezone("Asia/Seoul"))
    work_start  = now + timedelta(days=3)
    work_end    = now + timedelta(days=7)
    period      = f'{work_start.year}.{work_start.month}.{work_start.day} ~ {work_end.year}.{work_end.month}.{work_end.day}'
    time_window = f'오전 10시 ~ 오후 7시'
    text = f'\n\n기간: {period}\n시간: {time_window}\n'
    temp = True

    options = Options()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # login page 접속
    driver.get(login_url)

    time.sleep(10)

    # login page에서 email 입력
    driver.find_element(
        By.XPATH, 
        '//*[@id="join"]/div[1]/div/div/div[1]/div[2]/div/input'
        ).send_keys(args.email)

    time.sleep(10)

    # 확인 버튼 클릭
    driver.find_element(
        By.XPATH, 
        '//*[@id="join"]/div[1]/div/div/div[2]/div[2]/button'
        ).click()

    time.sleep(10)

    # 패스워드 입력
    driver.find_element(
        By.XPATH, 
        '//*[@id="join"]/div[1]/div/div/div[1]/div[2]/div/input'
        ).send_keys(args.passwd)

    time.sleep(10)

    # 확인 버튼 클릭
    driver.find_element(
        By.XPATH, 
        '//*[@id="join"]/div[1]/div/div/div[2]/div[2]/button[2]'
        ).click()

    time.sleep(10)

    # 결재 페이지 이동
    driver.get(approval_url)

    time.sleep(10)

    # 결재 작성하기 버튼 클릭
    driver.find_element(
        By.CSS_SELECTOR,
        "#ct > div > div:nth-child(4) > div.display-flex > button",
    ).click()

    time.sleep(10)

    # 결제 템플릿 선택(유연 근무제 신청서)
    driver.find_element(
        By.XPATH,
        # '#modal5 > div > div > div.modal-body > div > table > tbody > tr:nth-child(7) > td'
        # '//*[@id="modal5"]/div/div/div[2]/div/table/tbody/tr[7]/td'
        '/html/body/div[1]/div[1]/div[4]/div/div[3]/div/div/div/div[2]/div/table/tbody/tr[7]/td'
    ).click()

    time.sleep(10)

    # 유연 근무 기간 및 시간 입력 칸 element
    elem = driver.find_element(
        By.CLASS_NAME,
        'fr-wrapper'
        )
    
    time.sleep(10)

    # 클릭 후 text 입력
    webdriver.ActionChains(driver).move_to_element(elem).click().send_keys(text).perform()

    time.sleep(10)

    if temp:
        # 임시 저장 버튼 클릭
        driver.find_element(
            By.CSS_SELECTOR,
            '#wrap > div:nth-child(3) > div > div.sc-eJDSGI.gAXKGF > div.sc-jfvxQR.kUrDKQ > \
            div > div:nth-child(6) > div.d-flex-space.mt-3 > div:nth-child(1) > button',
        ).click()
    else:
        # 결재 요청 버튼 클릭
        driver.find_element(
            By.CSS_SELECTOR,
            '#wrap > div:nth-child(3) > div > div.sc-eJDSGI.gAXKGF > div.sc-jfvxQR.kUrDKQ > div > \
            div:nth-child(6) > div.d-flex-space.mt-3 > div:nth-child(2) > button.btn.btn-primary'
        ).click()                                                                                               

    time.sleep(10)

    # driver.get_screenshot_as_file("/root/auto-commute/screen_shots/test2.png")

    driver.quit()