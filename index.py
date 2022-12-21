# from threading import Thread
from flask import Flask, request, send_file
from utils import read_as_binary
from uuid import uuid4
import qrcode
import image
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return "nothing here, but it's fine."


@app.route('/qrcode', methods=['GET'])
def api_test():
	args = request.args.to_dict()
	data = args.get("data")
	qr = qrcode.QRCode(version=10, box_size=20, border=4)
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image(fill="black", back_color="white")
	filename = f"{str(uuid4())}.png"
	img.save(filename)
	return send_file(read_as_binary(filename), download_name="qrcode.png")


# port = int(os.environ.get("PORT", 3080))
# api.run(host="0.0.0.0", debug=False, port=port)
# api_Thread = Thread(target=api.run, args=(), kwargs={"host": "0.0.0.0", "debug": False, "port": port})
