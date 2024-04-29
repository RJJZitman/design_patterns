from config import AppConfig
from sub_builders import ApiConfigBuilder, DatabaseConfigBuilder


if __name__ == "__main__":
    app_builder = AppConfig.get_app_config_builder()
    # TODO: breaks without instantiating subbuilders. look into registery
    # api = ApiConfigBuilder(config=AppConfig())
    # db = DatabaseConfigBuilder(config=AppConfig())
    print(dir(app_builder))

    app_config = app_builder\
        .databaseconfigbuilder\
            .with_host("localhost")\
            .with_port(5432)\
            .with_credentials("admin", "password")\
            .with_database("my_database")\
        .apiconfigbuilder\
            .with_base_url("https://api.example.com")\
            .with_supported_methods(["GET", "POST", "PUT", "DELETE"])\
            .with_auth_token("my_api_token")\
        .build()

    print(f"config template: \n{AppConfig.get_app_config_builder().build()}")
    print(75*"-")
    print(f"app_config: \n{app_config}")
