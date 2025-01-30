from .base import *

DEBUG = False

ALLOWED_HOSTS = ["sbgnc.pythonanywhere.com"]

CORS_ALLOWED_REGEX = [
    # https://fantastic-invention-gpvprvpxwpcvr5p-3000.app.github.dev/
    r"^https://\w+\.github\.dev$",
]
