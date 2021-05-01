import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def submitForm(self):
        self.client.post("/predict", json={"funding":"10000000", "rounds":"4"})