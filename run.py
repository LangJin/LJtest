# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from app import create_app
from flask_cors import CORS


app = create_app()
cors = CORS(app, supports_credentials=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
