import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_super_secret_key")
    DEBUG = False
    RESTX_MASK_SWAGGER = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tt_dev_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(basedir, 'tt_test_database.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
