import os

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

mongo_user = os.getenv('MONGO_USER', 'admin')
mongo_password = os.getenv('MONGO_PASSWORD', 'admin')
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', 27017)
mongo_database = os.getenv('MONGO_DATABASE', 'admin')
mongo_authentication_database = os.getenv('MONGO_AUTHENTICATION_DATABASE', 'admin')

client = MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format(mongo_user, mongo_password, mongo_host, mongo_port,
                                                                   mongo_authentication_database))


@app.route('/')
def root():
    db = client[mongo_database]
    employees = list(db.employees.find({}).sort([('name', 1)]).limit(100))
    return render_template('index.html', employees=employees)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
