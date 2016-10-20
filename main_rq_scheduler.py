from redis import Redis
from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from functions_to_run import *

scheduler = Scheduler(connection=Redis())

scheduler.enqueue_at(datetime(2020,1,1), do_nothing)
scheduler.enqueue_in(timedelta(seconds=5, do_nothing)
