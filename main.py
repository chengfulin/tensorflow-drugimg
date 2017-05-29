import numpy as np
import sys
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
sys.path.insert(0, '/src/python/tf_files')
import label_image

# webapp
app = Flask(__name__)


@app.route('/api/trydetect/<img>')
def tryDetect(img):
    return detect(img)

@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
