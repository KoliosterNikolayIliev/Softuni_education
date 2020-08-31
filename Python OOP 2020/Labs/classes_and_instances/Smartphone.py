class Smartphone:
    def __init__(self, memory, ):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        memory_after_app = self.memory - app_memory
        if memory_after_app > 0 and not self.is_on:
            return f"Turn on your phone to install {app}"
        if self.is_on and memory_after_app < 0:
            return f"Not enough memory to install {app}"
        self.apps.append(app)
        self.memory = memory_after_app
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
