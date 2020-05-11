from flask import Flask ,render_template,request,jsonify
import pandas as pd
import numpy as np
from flask_cors import CORS,cross_origin

app1=Flask(__name__)
@app1.route('/',methods=['GET','POST'])
@cross_origin()
def homepage():
    return render_template('index.html')
@app1.route('/process',methods=['POST'])
@cross_origin()
def process1():
    if(request.method=='POST'):
        year_of_exp=request.form['year_of_exp']
        result=process(float(year_of_exp))
        return render_template('result.html', result=result)
def process(year_of_exp):
    data=pd.read_csv("E:\i neuron ML\datasets\examples\Salary_Data.csv")
    #print(data)
    #print(data.shape)
    x=data['YearsExperience']
    x=np.array(x)

    y=data['Salary']
    y=np.array(y)

    from sklearn.linear_model import LinearRegression
    Regressor=LinearRegression()
    Regressor.fit(x[:,np.newaxis],y[:,np.newaxis])
    result=Regressor.predict([[year_of_exp]])
    return result
if __name__=='__main__':

    app1.run(debug=True)