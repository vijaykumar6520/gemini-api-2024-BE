from flask import Flask, request, Response, stream_with_context, jsonify
from flask_cors import cross_origin
import logging
from dotenv import load_dotenv
load_dotenv(".env")
from flask import request
import requests
import os
import json
from routes.health import health
from routes.gemini import call_gemini

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

@app.route("/api/prompt", methods=["POST"])
@cross_origin()
def gemini_prompt():
    try:
        body = request.get_json()

        print(body)
        resp = call_gemini(body['prompt'])

        return {"res": resp}, 200

    except Exception as e:
        logging.error(e, exc_info=True)
        return {"success": False, "message": "Internal server error"}, 500
