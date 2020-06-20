from apscheduler.schedulers.blocking import BlockingScheduler
from covidapp.views import send_message,send_welcome,send_tweets,send_hotspots
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covidbot.settings")
django.setup()
from covidapp.models import UserDetails
send_welcome()
sched = BlockingScheduler()
sched.add_job(send_message, 'cron', hour='4', minute='30')
sched.add_job(send_message,'cron',hour='16',minute='30')
sched.add_job(send_message,'cron',hour='17',minute='5')
sched.add_job(send_message,'cron',hour='17',minute='30')
sched.add_job(send_message,'cron',hour='17',minute='57')
#sched.add_job(send_message,'interval',seconds=10)
sched.start()