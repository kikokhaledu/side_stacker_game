import json
import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_lobby(self):
        self.client.get(url="/")
        
    @task
    def get_setup(self):
        self.client.get(url="/setup/")


        
    