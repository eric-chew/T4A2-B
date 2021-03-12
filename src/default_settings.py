import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get('DB_URI')

        if not value:
            raise ValueError('DB_URI is not set')

        return value

    # @property
    # def AWS_ACCESS_KEY_ID(self):
    #     value = os.getenv('AWS_ACCESS_KEY_ID')
    #     if not value:
    #         raise ValueError('AWS_ACCESS_KEY_ID is not set')
    #     return value

    # @property
    # def AWS_SECRET_ACCESS_KEY(self):
    #     value = os.getenv('AWS_SECRET_ACCESS_KEY')

    #     if not value:
    #         raise ValueError('AWS_SECRET_ACCESS_KEY is not set')
    #     return value

    @property
    def SECRET_KEY(self):
        value = os.environ.get('SECRET_KEY')

        if not value:
            raise ValueError('SECRET_KEY is not set')

        return value


class DevelopmentConfig(Config):
    DEBUG = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get('DB_URI_DEV')

        if not value:
            raise ValueError('DB_URI_DEV is not set')

        return value


class ProductionConfig(Config):
    @property
    def SECRET_KEY(self):
        value = os.environ.get('SECRET_KEY')

        if not value:
            raise ValueError('SECRET_KEY is not set')

        return value


class TestingConfig(Config):
    TESTING = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get('DB_URI_TEST')

        if not value:
            raise ValueError('DB_URI_TEST is not set')

        return value


environment = os.environ.get('FLASK_ENV')

if environment == 'production':
    app_config = ProductionConfig()
elif environment == 'testing':
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
