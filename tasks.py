from celery import Celery

app = Celery('tasks',
        broker='redis://:rootroot@192.168.0.103',
        backend='redis://:rootroot@192.168.0.103')


@app.task
def add(x, y):
        print("running...", x, y)
        return x + y

import time, json
import subprocess
@app.task
def run_cmd(cmd):
    time.sleep(10)
    cmd_obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return json.dumps(cmd_obj.stdout.read().decode('utf8'))
