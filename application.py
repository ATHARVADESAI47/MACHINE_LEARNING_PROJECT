from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

# Global error handler
@app.errorhandler(500)
def internal_error(error):
    return render_template('home.html', error="Internal server error occurred. Please try again."), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('home.html', error="Page not found."), 404

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            # Validate required fields
            required_fields = ['gender', 'ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course', 'reading_score', 'writing_score']
            for field in required_fields:
                if not request.form.get(field):
                    return render_template('home.html', error=f"Missing required field: {field}")
            
            # Validate numeric scores
            try:
                reading_score = float(request.form.get('reading_score'))
                writing_score = float(request.form.get('writing_score'))
                if not (0 <= reading_score <= 100 and 0 <= writing_score <= 100):
                    return render_template('home.html', error="Scores must be between 0 and 100")
            except ValueError:
                return render_template('home.html', error="Scores must be valid numbers")
            
            data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=reading_score,
                writing_score=writing_score
            )
            pred_df=data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline=PredictPipeline()
            print("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            print("after Prediction")
            return render_template('home.html', results=results[0])
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return render_template('home.html', error=f"Prediction failed: {str(e)}")
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        