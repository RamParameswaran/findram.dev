from locust import HttpUser, TaskSet, task, between


class LoadTest_HomePage(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def get_homepage(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Got wrong response")

    @task(1)
    def get_blog(self):
        with self.client.get("/blog/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Got wrong response")
