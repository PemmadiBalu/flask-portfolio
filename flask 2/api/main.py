
from flask import Flask
from app import app  # import your existing Flask app

# Vercel serverless entry point
def handler(environ, start_response):
    from werkzeug.wrappers import Request, Response
    request = Request(environ)
    response = app.full_dispatch_request()
    return response(environ, start_response)
