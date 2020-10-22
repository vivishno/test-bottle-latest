import os
from waitress import serve
from Application.app import app

serve(app,host="0.0.0.0",port=os.environ["PORT"])
