# -*- coding:utf-8 -*-

#################################################################
import os
import slack

from config import SLACK_TOCKEN, CHANNEL

client = slack.WebClient(token=SLACK_TOCKEN)

response = client.chat_postMessage(
    channel=CHANNEL,
    text="Hello world!")


assert response["ok"]


print('Done...')
