from app_config import AppConfigBuilder
from component_builders import DatabaseConfigBuilder


if __name__ == "__main__":
    app_builder = AppConfigBuilder()
    db_b = DatabaseConfigBuilder()
    print(dir(db_b))
    print(dir(app_builder))
    print(app_builder.implementations)

    app_config = app_builder\
        .database_builder()\
            .with_host("localhost")\
            .with_port(5432)\
            .with_credentials("admin", "password")\
            .with_database("my_database")\
        .api_builder()\
            .with_base_url("https://api.example.com")\
            .with_supported_methods(["GET", "POST", "PUT", "DELETE"])\
            .with_auth_token("my_api_token")\
        .build()

    print(app_config)
