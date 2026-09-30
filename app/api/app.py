import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/visits")
def visits():
    return jsonify(visits=r.incr("visits"))