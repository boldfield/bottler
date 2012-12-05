import os
import boto
from boto.s3.bucket import Bucket
from flask import Flask
from bottler import index, pypi


class App(Flask):

    def __init__(self, *args, **kw):
        super(App, self).__init__(*args, **kw)
        self.configure()

    def configure(self):
        self.url_map.strict_slashes = False
        settings = self.get_env('SETTINGS')
        settings = settings or 'bottler.settings.dev'

        self.config.from_object('bottler.settings.base')
        self.config.from_object(settings)

        self.from_env('AUTH_USERNAME')
        self.from_env('AUTH_PASSWORD')
        self.from_env('S3_BUCKET')
        self.from_env('SITE_NAME', 'Bottler Code Index')

        self.configure_s3()
        self.configure_blueprints()

    def get_env(self, key):
        if key:
            envvar = 'BOTTLER_%s' % key
            if envvar in os.environ and os.environ[envvar]:
                return os.environ[envvar]

    def from_env(self, key, default=None):
        if not key:
            return
        value = self.get_env(key)
        if value is not None:
            self.config[key] = value
        elif default is not None:
            self.config[key] = default

    def configure_s3(self):
        self.s3 = boto.connect_s3()
        self.bucket = self.config.get('S3_BUCKET')
        self.bucket = Bucket(self.s3, name=self.bucket)
        self.teardown_appcontext(self.teardown_s3)

    def configure_blueprints(self):
        self.register_blueprint(index.plan)
        self.register_blueprint(pypi.plan, url_prefix='/pypi')

    def teardown_s3(self, response):
        self.s3.close()
