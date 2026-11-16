
from locust import HttpUser, task, between


class KubernetesUser(HttpUser):

    wait_time = between(1, 2)

    @task(3)
    def home(self):
        self.client.get("/")

    @task(5)
    def work(self):
        self.client.get("/work")

    @task(1)
    def health(self):
        self.client.get("/health")
