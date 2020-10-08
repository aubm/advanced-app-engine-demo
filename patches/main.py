import os

from flask import Flask, render_template
from google.cloud import secretmanager
from pymongo import MongoClient

app = Flask(__name__)
client = secretmanager.SecretManagerServiceClient()


def get_secret(secret_id, version_id):
    name = f"projects/{gcp_project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name)
    return response.payload.data.decode("UTF-8")


gcp_project_id = os.getenv('GCP_PROJECT_ID')
mongo_user = get_secret('mongo_user', 1)
mongo_password = get_secret('mongo_password', 1)
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
