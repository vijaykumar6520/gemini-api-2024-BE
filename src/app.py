from flask import Flask, request, Response, stream_with_context, jsonify
from flask_cors import cross_origin
import logging
from dotenv import load_dotenv
load_dotenv(".env")
from flask import request
import requests
from routes.health import health
import os
import json

# THIS FILE SHOULD ONLY CONTAIN ROUTING AND LOGGING
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/api/health")
@cross_origin()
def health_route():
    try:
        healthResponse = health() 
        return {"message": healthResponse }, 201
    except Exception as e:
        logging.error(e, exc_info=True)
        return {"success": False, "message": "Internal server error"}, 500
