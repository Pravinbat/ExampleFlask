import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/ubuntu/ExampleFlask')
from my_flask_app import app as application
application.secret_key = '123'