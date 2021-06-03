from locust import HttpUser, task, between
import time

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 2.0)
    
    def on_start(self):
        self.client.post("/login", {"username":"locust-user"})
        pass

    def on_stop(self):
        self.client.get("/logout")
        pass

    @task(4)
    def test_index(self):
        self.client.get("/")

    @task(3)
    def test_user_profile(self):
        self.client.get("/Locust")

    @task(2)
    def test_user_friends(self):
        self.client.get("/Locust")
        time.sleep(2)
        self.client.get("/Locust/friends")