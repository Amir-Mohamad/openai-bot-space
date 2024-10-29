from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        response = self.client.post("https://mehrgpt.ir/api/auth/jwt/create", json={"username": "amirm", "password": "amir13845"})
        self.token = response.json()["access"]
        print(self.token)

    def on_request(self, request_type, name, response, **kwargs):
        if "Authorization" not in kwargs["headers"]:
            kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
            print("still running","*"*10)
    @task(1)
    def chat_history(self):
        self.client.get("https://mehrgpt.ir/")

    # @task(2)
    # def chat(self):
    #     self.client.post("/chat/1/", json={"user_message": "Hello"})

    # @task(1)
    # def list_bots(self):
    #     self.client.get("/bots/")

    # @task(1) #DONE
    # def list_bots_user(self):
    #     self.client.get("/bots/user/")

    # @task(1)
    # def create_bot(self):
    #     self.client.post("/bot/create/", json={"name": "New Bot", "description": "A new bot"})

    # @task(1)
    # def token_obtain_pair(self):
    #     self.client.post("/token/", json={"username": "testuser", "password": "password"})

    # @task(1)
    # def token_refresh(self):
    #     self.client.post("/token/refresh/", json={"refresh": "refresh_token"})

    # @task(1)
    # def token_verify(self):
    #     self.client.post("/token/verify/", json={"token": "access_token"})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)