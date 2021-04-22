# overriding example

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__(self):
        return f"Time = {self.hour} : {self.minute} : {self.second}"

start=Time(7,45,12)
print(start)