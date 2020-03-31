# -*- coding:utf-8 -*-

import os
import time

import slack

from slack_config import *


class Slacker:
    def __init__(self, context):
        self.context = context

        self._channel = channel

        self._fallback  = {"fallback": context.fallback}

        self._pretext   = {"pretext": context.pretext}
        self._color     = {"color": context.color}

        self._title     = {"title": context.title}
        self._title_link = {"title_link": context.title_link}

        self._text      = {"text": context.text}

        self._image_url = {"image_url": context.image_url}
        self._thumb_url = {"thumb_url": context.thumb_url}

        self._footer    = {"footer": context.footer}

        self._ts        = {"ts": context.ts}

        self._client    = None
        self.connectSlack()

    def connectSlack(self):
        if not self._client:
            try:
                self._client = slack.WebClient(token=SLACK_TOCKEN)
                return True

            except Exception as e:
                print(e)
                return False

    def sendMessage(self, message):
        response = self._client.chat_postMessage(channel=context.channel, text=message)
        assert response["ok"]

    def sendAlarms(self):
        response = self._client.chat_postMessage(channel=context.channel, attachments=[self.buildAttach()])
        assert response["ok"]

    def buildAttach(self):
        attach = dict()

        attach.update(self._fallback)

        attach.update(self._pretext)
        attach.update(self._color)

        attach.update(self._title)
        attach.update(self._title_link)

        attach.update(self._text)

        attach.update(self._image_url)
        attach.update(self._thumb_url)

        attach.update(self._footer)

        attach.update(self._ts)

        return attach

    class Builder:
        def __init__(self):
            self.channel = "#general"

            self.fallback   = "중요 알람입니다."

            self.pretext    = "헤더라인"
            self.color      = GREEN_COLOR

            self.title      = "타이틀"
            self.title_link = False

            self.text       = "내용"

            self.image_url  = False
            self.thumb_url  = GREEN_IMAGE

            self.footer     = "by Sender"

            self.ts         = time.time()


        def __getattr__(self, key):
            try:
                return self.__dict__[key]
            except KeyError as e:
                return None

        def setChannel(self, channel):
            self.channel = channel
            return self

        def setFallback(self, fallback):
            self.fallback = fallback
            return self

        def setPretext(self, pretext):
            self.pretext = pretext
            return self

        def setColor(self, color):
            self.color = color
            return self

        def setTitle(self, title):
            self.title = title
            return self

        def setTitle_link(self, title_link):
            self.title_link = title_link
            return self

        def setText(self, text):
            self.text = text
            return self

        def setImage_url(self, image_url):
            self.image_url = image_url
            return self

        def setThumb_url(self, thumb_url):
            self.thumb_url = thumb_url
            return self

        def setFooter(self, footer):
            self.footer = footer
            return self

        def setTs(self, ts):
            self.ts = ts
            return self

        def build(self):
            return Slacker(self)


a = Slacker.Builder()                                   \
            .setChannel("#test")                        \
            .setText("큰 문제가 발생하였습니다.")           \
            .build()

a.sendAlarms()
