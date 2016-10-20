# Messing with RQ

Python's RQ module is great!  It makes working with Redis super easy!  Unfortunately it doesn't work everywhere.  Therefore I wrote up this little set of examples to use a (recently) verified version of redis with a recently verified version of Python-RQ.

##My set up

I'm using Ubuntu 16.04.  To install redis I made use of [digital oceans blog post](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04) which does a pretty good job of explaining how to do things.

I'm using Python-3.5.2 and pip3-8.1.2

I pip installed rq via - `sudo pip install rq` and rq-scheduler via `sudo pip install rq-scheduler`

##Running things

To run everything you'll need to schedule the jobs, do this by running:

`python main.py`

Then run:

`rq worker`

rq is a command that comes with the pip install of `python-rq`, please note: this doesn't install on Mac OSX.  So you won't be able to run jobs on that OS.  

 
