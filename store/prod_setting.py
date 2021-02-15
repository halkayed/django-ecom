import os
from .settings import *

SECRET_KEY = os.environ('SECRET_KEY')

DEBUG = TRUE

ALLOWED_HOSTS = ['notmystore.herokuapp.com']