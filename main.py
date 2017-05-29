import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
sys.path.insert(0, '/src/python/tf_files')
import label_image

# webapp
app = Flask(__name__)


@app.route('/api/mnist', methods=['POST'])
def mnist():
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    output1 = regression(input)
    output2 = convolutional(input)
    return jsonify(results=[output1, output2])

@app.route('/api/trydetect/<img>')
def tryDetect(img):
    return detect(img)

@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
