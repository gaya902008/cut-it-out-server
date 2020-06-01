from flask import Flask, escape, request, jsonify,make_response

app = Flask(__name__)

@app.route('/<string:videoURL>', methods=['GET'])
def cut(videoURL):
    return jsonify({"data":"005:32,014:31,025:31"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)