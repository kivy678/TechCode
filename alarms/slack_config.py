# -*- coding:utf-8 -*-

import os
from urllib.parse import urljoin

############################# TOCKEN #############################
SLACK_TOCKEN    = 'xoxb-969435419377-981408058743-Dkn2qY7RrjdKeFTlxA9mhN0X'

##################################################################
BASE_URL        = "https://registry.my-netdata.io/images/"

RED_IMAGE       = urljoin(BASE_URL, "alert-128-red.png")
ORANGE_IMAGE    = urljoin(BASE_URL, "alert-128-orange.png")
GREEN_IMAGE     = urljoin(BASE_URL, "check-mark-2-128-green.png")

RED_COLOR       = "#ca414b"
ORANGE_COLOR    = "#ffc107"
GREEN_COLOR     = "#77ca6d"


