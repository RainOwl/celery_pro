from celery import Celery
from celery.schedules import crontab
 
app = Celery('proj',
            broker='redis://:rootroot@192.168.0.103',
            backend='redis://:rootroot@192.168.0.103',
           # include=['my_celery.tasks']
            )

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
               
    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)
                        
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(crontab(hour='15,16', minute='*/2', day_of_week='fri'),
                            test.s('Happy Mondays!'),
                                                            )
                                 
@app.task
def test(arg):
    print("running-->",arog
            )
