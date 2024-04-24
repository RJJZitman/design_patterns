class DatabaseConfig:
    def __init__(self):
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database_name = None

    def __str__(self):
        return f"Database Config: Host={self.host}, Port={self.port}, Username={self.username}, Password={self.password}, Database={self.database_name}"


class ApiConfig:
    def __init__(self):
        self.base_url = None
        self.supported_methods = []
        self.auth_token = None

    def __str__(self):
        return f"API Config: Base URL={self.base_url}, Supported Methods={self.supported_methods}, Auth Token={self.auth_token}"
