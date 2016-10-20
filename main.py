from redis import Redis
from rq import Queue
from functions_to_run import *

q = Queue(connection=Redis())
job1 = q.enqueue(add,args=(3,4,))
job2 = q.enqueue(fib,args=(5,))

job1.result
