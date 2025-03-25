import uuid

class IDGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IDGenerator, cls).__new__(cls)
        return cls._instance

    def generate_id(self):
        return str(uuid.uuid4())
