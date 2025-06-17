#decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Aram")

#adapter

class OldMusicPlayer:
    def play_music_file(self, filename):
        print(f"Playing {filename} in old format")

class NewMusicPlayer:
    def play(self, filename):
        print(f"Streaming {filename} online")

class MusicAdapter:
    def __init__(self, old_player): 
        self.old_player = old_player

    def play(self, filename):
        self.old_player.play_music_file(filename)

old = OldMusicPlayer()
adapter = MusicAdapter(old)
adapter.play("song.mp3")

#singleton
class DataBase:
    _instance = None  # private static variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        # If no instance exists, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance  # Return the single instance

    def __init__(self, user, psw, port):
        # Initialize only once
        if not hasattr(self, '_initialized'):
            self.user = user
            self.psw = psw
            self.port = port
            self._initialized = True  # Mark initialization complete

    def show_config(self):
        print(f"User: {self.user}, Password: {self.psw}, Port: {self.port}")


# Testing Singleton
db1 = DataBase("admin", "1234", 5432)
db2 = DataBase("guest", "5678", 3306)

print(id(db1), id(db2))  # Same id, meaning same object
db1.show_config()        # Output: admin, 1234, 5432
db2.show_config()        # Also shows admin, 1234, 5432

#
def connect(self):
    print(f"Connecting to DB: {self.user}, {self.psw}, {self.port}")

def close(self):
    print("Closing the database connection")

def read(self):
    return "Data from the database"

def write(self, data):
    print(f"Writing to the database: {data}")

#Chain of responsability
class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return True


class CheckUserExists(Handler):
    def handle(self, request):
        if request.get("user") != "admin":
            print("User not found")
            return False
        return super().handle(request)


class CheckPassword(Handler):
    def handle(self, request):
        if request.get("password") != "123":
            print("Wrong password")
            return False
        return super().handle(request)


chain = CheckUserExists(CheckPassword())
chain.handle({"user": "admin", "password": "123"})
chain.handle({"user": "admin", "password": "wrong"})

#Chain
class Step:
    def __init__(self, next_step=None):
        self.next = next_step

    def process(self, data):
        if self.next:
            return self.next.process(data)
        return data


class AddOne(Step):
    def process(self, data):
        return super().process(data + 1)


class MultiplyByTwo(Step):
    def process(self, data):
        return super().process(data * 2)


pipeline = AddOne(MultiplyByTwo())
print(pipeline.process(3))