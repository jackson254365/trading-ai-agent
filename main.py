from webhook_server import app

if __name__ == '__main__':
    # It's recommended to use a production-ready WSGI server
    # like Gunicorn or uWSGI instead of the built-in Flask server.
    app.run(port=5000, debug=True)