from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    # wait_time = between(0.5, 3.0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(3)
    def hello_world(self):
        self.client.get("/")

    @task(2)
    def hello_user(self):
        self.client.get("/Locust")