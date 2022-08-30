import streamlit as st
import joblib

#load the joblib model
model_nb=joblib.load('Heart-Disease-Prediction')

st.title('HEART DISEASE PREDICTOR')

age=st.number_input('Enter your Age:')
sex=st.number_input('Enter your Gender(0 is male and 1 female):')
cp=st.number_input('Enter chest pain type (1=angina, 2=pericarditis, 3=myocarditis):')
trestbps=st.number_input('Enter resting blood pressure:')
chol=st.number_input('Enter serum cholestoral in mg/dl:')
fbs=st.number_input('Enter fasting blood sugar:')
restecg=st.number_input('Enter resting electrocardiographic results:')
thalach=st.number_input('Enter maximum heart rate achieved:')
exang=st.number_input('Enter exercise induced angina:')
oldpeak=st.number_input('Enter depression induced by exercise relative to rest:')
ca=st.number_input('Enter number of major vessels (0-3) colored by flourosopy:')
thal=st.number_input('Enter type of defect:(0 = normal; 1 = fixed defect; 2 = reversable defect):')
op=model_nb.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,ca,thal]])


if st.button('PREDICT'):
  if age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,ca,thal!=0:
    if  op==1:
      st.title("no heart disease")
    else:
      st.title("you have a heart disease please consult a doctor")
   else:
    st.title("please enter the data")
    
    
    
    
    
    
    
    
    
                 
