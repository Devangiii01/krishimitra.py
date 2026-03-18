from flask import Flask, request, jsonify
from flask_cors import CORS 
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # isse java/react ko permission milti he bat karne ki
#1. "model.plk" box ko kholna
with open('model.plk', 'rb') as f:
    assets = pickle.load(f)
    model = assets['model']   # AI ka dimaag
    scaler = assets['scaler'] # paimana (scale)

@app.route('/')
def home():
    return "crop prediction server chalu hai!"   

@app.route('/predict', methods = ['POST'])
def predict():
    try:
        data = request.get_json()  # java se data lena (jason format me)
        user_input = np.array([data['n'], data['p'], data['k'],       # data ko list me sajana 
                                data['temperature'], data['humidity'],  # java se 7 no. aane chahiye
                                  data['ph'], data['rainfall']]
                                  )    

        user_input_scaled = scaler.transform(user_input)  # naye data ko usi paimana(scaler) se napna.
        prediction = model.predict(user_input_scaled)     # prediction karana
        return jsonify({'status':'success','crop': str(prediction[0])})  #jawab wapas bhejna
    
    except Exception as e:
        return jsonify({'status':'error', 'message': str(e)})
    
if __name__ == '__main__':
    #server ko 5000 port par chalu karna
    app.run(port=5000,debug=True)
         

        