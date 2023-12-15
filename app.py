from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from diamond_price_predication.pipeline.predication import PredictionPipeline
from diamond_price_predication import logger

app=Flask(__name__)

@app.route('/', methods=['GET'])
def homePage(): 
    return render_template("index.html")

@app.route('/train',methods=['GET'])
def training(): 
    os.system("python main.py")
    return "Traning Sucessfully"

@app.route("/predict", methods=['POST', 'GET'])
def predict_datapoint(): 
    if request.method == 'GET': 
        return render_template('form.html')
    
    else: 
        carat=float(request.form['carat'])
        depth=float(request.form['depth'])
        table=float(request.form['table'])
        x=float(request.form['x'])
        y=float(request.form['y'])
        z=float(request.form['z'])
        cut=float(request.form['cut'])
        color=float(request.form['color'])
        clarity=float(request.form['clarity'])
        
        final_new_data=[carat,depth,table,x,y,z,cut, color, clarity]
        
        logger.info(f"Final_new_data: {final_new_data}")
        
        data=np.array(final_new_data).reshape(1,9)
        
        logger.info(f"final data after reshapeing(1,9) : {data}")
        
        obj=PredictionPipeline()
        predict=obj.predict(data)
        
        return render_template('form.html', final_result=predict)
        
        





if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)