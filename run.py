# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from app import create_app



app = create_app("Develop")


if __name__ == "__main__":
    app.run()
