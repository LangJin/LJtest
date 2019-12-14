cd /software/ljtest

source env/bin/activate

gunicorn run:app -c gunconfig.py
