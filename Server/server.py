from flask import Flask, request, jsonify
import util
import cv2

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    # return '+OK' 
    # image_data = request.form['image_data']
    # response = request.files.get("image_data", "")
    response = request.files['image_data']
    # response.save('./hell/kohli.jpg')
    # img = cv2.imread('_data/arvind.jpeg', 1)
    # cv2.imshow('Photo',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # info = json.loads(request.data['info'])
    print("This is response---------------->",response)
    # response = jsonify(util.classify_image(image_data))
    return response
    print(response)

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000,debug=True)