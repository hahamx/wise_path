# -*- coding:utf-8 -*-
from locust import HttpLocust, TaskSet, events, task
import Queue
import time
import json
import subprocess
import random


class strees(TaskSet):
    def on_start(self):
        print "start stress chain"
        self.name = ["Aaron", "Ann", "Athena", "Augustine", "Atwood", "Jack", "Jacqueline", "Jennifer", "Fanny",
                     "Frank", "Freda", "Felix", "Zora", "Zebulon"]
        self.pare = ["Smith", "Jones", "Williams", "Taylor", "Brown", "Davies", "Evans", "", "Thomas", "Johnson",
                     "Roberts", "", "Lewis", "Harris",
                     "Clarke", "Patel", "Jackson", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen"]
        pass

    @task(1)
    def get_block(self):
        r1 = self.client.get("http://127.0.0.1:5002/blocks")
        print "{},{}".format("get_block", r1)
        print("Get wrong respone:" + r1.content)
        pass

    @task(1)
    def get_txion(self):
        names = "{}.{}".format(random.choice(self.name), random.choice(self.pare))
        name_t = "{}.{}".format(random.choice(self.name), random.choice(self.pare))
        amount = random.choice(range(100000))
        jsonp = {"from": names, "to": name_t, "amount": amount}
        r3 = self.client.post("http://127.0.0.1:5002/txion", json=jsonp)
        print "{},{}".format("txion", r3)
        print("Get wrong respone:" + r3.content)
        pass

    @task(1)
    def get_mine(self):
        r2 = self.client.get("http://127.0.0.1:5002/")
        print "{},{}".format("mine", r2)
        print("Get wrong respone:" + r2.content)
        pass


class web_user(HttpLocust):
    weight = 1
    task_set = strees
    user_data_queue = Queue.Queue()
    for ind in xrange(100):
        data = "%s-%d" % (ind, int(time.time()))
        user_data_queue.put_nowait(data)
    min_wait = 1000
    max_wait = 3000
    pass


class mobile_user(HttpLocust):
    weight = 3
    task_set = strees
    user_data_queue = Queue.Queue()
    for ind in xrange(100):
        data = "%s-%d" % (ind, int(time.time()))
        user_data_queue.put_nowait(data)
    min_wait = 500
    max_wait = 2000
    pass


if __name__ == '__main__':
    p1 = subprocess.Popen(
        'locust -f ./lo_req.py --host=http://127.0.0.1:5002 --logfile=./mark/locust.log --loglevel=INFO --no-web -c 2 -r 1 -t 10',
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p1.communicate()
