from celery import Celery
from celery.schedules import crontab
 
app = Celery('proj',
            broker='redis://:rootroot@192.168.0.103',
            backend='redis://:rootroot@192.168.0.103',
           # include=['my_celery.tasks']
            )

app.conf.beat_schedule = {
    'add-every-10-seconds':{
        'task':'periodic2_task.add',
        'schedule':10.0,
        'args':(12,12)
    },
    # 'cmd-every-bespoke':{
    #         'task':'periodic2_task.run_cmd',
    #         'schedule':crontab(hour=7,minute=6,day_of_week=4),
    #         'args':('df -f',)
    # },
    'cmd-every-bespoke':{
            'task':'periodic2_task.run_cmd',
            'schedule':30.0,
            'args':('df -f',)
    },
}

# 现在时间减8小时
app.conf.timezone = 'UTC'

@app.task
def add(x, y):
        print("running...", x, y)
        return x + y

import time, json
import subprocess
@app.task
def run_cmd(cmd):
    # time.sleep(10)
    cmd_obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return json.dumps(cmd_obj.stdout.read().decode('utf8'))


