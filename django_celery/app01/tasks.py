#_author_ : duany_000
#_date_ : 2018/2/2
# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

import time, json
import subprocess
@shared_task
def run_cmd(cmd):
    time.sleep(10)
    cmd_obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return json.dumps(cmd_obj.stdout.read().decode('utf8'))

