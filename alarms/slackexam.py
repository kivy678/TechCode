# -*- coding:utf-8 -*-

#################################################################
import os
import slack
import time

images_base_url="https://registry.my-netdata.io/images/banner-icon-144x144.png"
images_base_url2="https://registry.my-netdata.io/images/alert-128-red.png"
images_base_url3="https://registry.my-netdata.io/images/alert-128-orange.png"
images_base_url4="https://registry.my-netdata.io/images/acheck-mark-2-128-green.png"


client = slack.WebClient(token=SLACK_TOCKEN)


attach = [
      {
          "fallback": "Plain-text summary of the attachment.",						# 알림 내용
          
          "pretext": "Optional text that appears above the attachment block",		# 헤더 라인
          "color": "#91b996",														# 바 색상
          "author_name": "Bobby Tables",											# 이름
          "author_link": "http://",													# 링크
          "author_icon": "http://",													# 아이콘 링크

          "title": "Slack API Documentation",										# 제목
          "title_link": "http://",													# 제목 링크
          "text": "Optional text that appears within the attachment",				# 본문 내용
          "fields": [
              {
                  "title": "Priority",
                  "value": "High",
                  "short": False
              }
          ],
          "image_url": "http://",													# 알림 및 본문 이미지 링크
          "thumb_url": "http://",													# 본문 보조 이미지(왼쪽) 링크

          "footer": "Slack API",													# 풋터 이름
          "footer_icon": "http://",													# 풋터 아이콘 링크
          "ts": time.time()															# UTC
      }
  ]

response = client.chat_postMessage(channel=CHANNEL, attachments=attach)


assert response["ok"]


print('Done...')
