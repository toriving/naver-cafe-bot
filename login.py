# -*- coding: utf-8 -*-
import os

from selenium import webdriver


def get_token():
    chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
    naver_id = os.environ.get('NAVER_ID')
    naver_pw = os.environ.get('NAVER_PW')
    naver_cid = os.environ.get('NAVER_CLIENT_ID')
    naver_redirect = os.environ.get('NAVER_REDIRECT')
    driver = webdriver.Chrome(chromedriver_path)  # driver = webdriver.PhantomJS()
    driver.implicitly_wait(3)
    driver.get('https://nid.naver.com/nidlogin.login')
    driver.find_element_by_name('id').send_keys(naver_id)
    driver.find_element_by_name('pw').send_keys(naver_pw)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    state = "toriving"
    req_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=token&client_id=%s&redirect_uri=%s&state=%s' % (naver_cid, naver_redirect, state)

    driver.get(req_url)
    driver.find_element_by_xpath('//*[@id="confirm_terms"]/a[2]').click()
    redirect_url = driver.current_url
    token = redirect_url.split("access_token=")[1].split("&state=")[0]
    driver.quit()

    if len(token) == 0:
        return None

    print(token)
    return token
