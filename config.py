import os
baseddir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHMY_COMMIT_ON_TEARDOWN = True
    ### FLASKY_SUBJECT_PREFIX = '[Flasky]'
    ### FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    ### FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    
    ###MAIL_SERVER = 'smtp.googlemail.com'
    ###MAIL_PORT = '587'
    ###MAIL_USE_TLS = True
    ###MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    ###MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'mysql://flaskuser:Passw0rd@localhost/flask'
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'mysql://flaskuser:Passw0rd@localhost/test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql://flaskuser:Passw0rd@localhost/production'

config = {
          'development' : DevelopmentConfig,
          'testing' : TestingConfig,
          'production' : ProductionConfig,
          
          'default' : DevelopmentConfig
          }