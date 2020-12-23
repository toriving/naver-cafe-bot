# -*- coding: utf-8 -*-
import os
import urllib.request
import requests


def post_article(token):
    token = token
    header = "Bearer " + token
    clubid = os.environ.get('CLUB_ID')
    menuid = os.environ.get('MENU_ID')

    url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"

    subject = urllib.parse.quote("네이버 Cafe api Test Python")
    content = urllib.parse.quote("<font color='red'>python multi-part</font>로 첨부한 글입니다. <br> python 이미지 첨부 <br> <img src='#0' />")
    data = {'subject': subject, 'content': content}
    files = [
        ('image', ('YOUR_FILE_1', open('YOUR_FILE_1', 'rb'), 'image/jpeg', {'Expires': '0'})),
        ('image', ('YOUR_FILE_2', open('YOUR_FILE_2', 'rb'), 'image/jpeg', {'Expires': '0'}))
        ]

    headers = {'Authorization': header }
    response = requests.post(url, headers=headers, data=data, files=files)

    rescode = response.status_code

    if(rescode==200):
        print(response.text)
    else:
        print(rescode)

    return rescode