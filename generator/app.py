from flask import Flask, jsonify
import random
import time

app = Flask(__name__)
iscd = ["005930", "005940", "005950"]

items = {
    "MKSC_SHRN_ISCD" : "",
    "BSOP_HOUR" : random.randrange(100000, 900000),
    "HOUR_CLS_CODE" : str(0),
    "ASKP1" : random.randrange(1000, 9999),
    "ASKP2" : random.randrange(1000, 9999),
    "ASKP3" : random.randrange(1000, 9999),
    "ASKP4" : random.randrange(1000, 9999),
    "ASKP5" : random.randrange(1000, 9999),
    "ASKP6" : random.randrange(1000, 9999),
    "ASKP7" : random.randrange(1000, 9999),
    "ASKP8" : random.randrange(1000, 9999),
    "ASKP9" : random.randrange(1000, 9999),
    "ASKP10" : random.randrange(1000, 9999),
    "BIDP1" : random.randrange(1000, 9999),
    "BIDP2" : random.randrange(1000, 9999),
    "BIDP3" : random.randrange(1000, 9999),
    "BIDP4" : random.randrange(1000, 9999),
    "BIDP5" : random.randrange(1000, 9999),
    "BIDP6" : random.randrange(1000, 9999),
    "BIDP7" : random.randrange(1000, 9999),
    "BIDP8" : random.randrange(1000, 9999),
    "BIDP9" : random.randrange(1000, 9999),
    "BIDP10" : random.randrange(1000, 9999),
    "ASKP_RSQN1" : random.randrange(100000, 900000),
    "ASKP_RSQN2" : random.randrange(100000, 900000),
    "ASKP_RSQN3" : random.randrange(100000, 900000),
    "ASKP_RSQN4" : random.randrange(100000, 900000),
    "ASKP_RSQN5" : random.randrange(100000, 900000),
    "ASKP_RSQN6" : random.randrange(100000, 900000),
    "ASKP_RSQN7" : random.randrange(100000, 900000),
    "ASKP_RSQN8" : random.randrange(100000, 900000),
    "ASKP_RSQN9" : random.randrange(100000, 900000),
    "ASKP_RSQN10" : random.randrange(100000, 900000),
    "BIDP_RSQN1" : random.randrange(100000, 900000),
    "BIDP_RSQN2" : random.randrange(100000, 900000),
    "BIDP_RSQN3" : random.randrange(100000, 900000),
    "BIDP_RSQN4" : random.randrange(100000, 900000),
    "BIDP_RSQN5" : random.randrange(100000, 900000),
    "BIDP_RSQN6" : random.randrange(100000, 900000),
    "BIDP_RSQN7" : random.randrange(100000, 900000),
    "BIDP_RSQN8" : random.randrange(100000, 900000),
    "BIDP_RSQN9" : random.randrange(100000, 900000),
    "BIDP_RSQN10" : random.randrange(100000, 900000),
    "TOTAL_ASKP_RSQN" : random.randrange(100000, 900000),
    "TOTAL_BIDP_RSQN" : random.randrange(100000, 900000),
    "OVTM_TOTAL_ASKP_RSQN" : random.randrange(100000, 900000),
    "OVTM_TOTAL_BIDP_RSQN" : random.randrange(100000, 900000),
}

# GET /api/check
@app.route("/api/check")
def check():
  return "success"


# GET /api/hoka/{sec}
@app.route("/api/hoka/<int:iscd>")
def getHoka():
  items["MKSC_SHRN_ISCD"] = str(iscd)
  return jsonify(items)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
