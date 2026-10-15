import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

st.title('Passenger Survival Chance in the Titanic Journey')
pclass = st.slider('Enter the Passenger Class',1,3)
sex = st.selectbox('Select Gender',['male','female'])
sibsp = st.slider('Enter the total no. of Sibling & Spouce',0,10)
parch = st.slider('Enter the total no. of Parent & Child',0,8)
fare = st.number_input('Enter the Fair')
embarked = st.selectbox('Enter the boarding point',['Southampton','Cherbourg','Queenstown'])


df = pd.DataFrame({
    'Pclass':pclass,
    'Sex':sex,
    'SibSp':sibsp,
    'Parch':parch,
    'Fare':fare,
    'Embarked':embarked
},index=[0])

if st.button('Show Data'):
    st.write(df)

with open('label_encoder.pkl','rb') as file:
    label = pickle.load(file)
with open('one_hot_encoder.pkl','rb') as file:
    ohe = pickle.load(file)
with open('standard_scaler.pkl','rb') as file:
    scaler = pickle.load(file)

model = load_model('model.h5')
#--------- Encoding
df['Sex']=label.transform(df[['Sex']])

emb = pd.DataFrame(ohe.transform(df[['Embarked']]),columns=ohe.get_feature_names_out())
df = pd.concat((df,emb),axis=1)
df.drop(columns=['Embarked'],inplace = True)

#------------- Scaling
df[df.columns] = scaler.transform(df[df.columns])

if st.button('Encoded Data'):
    st.write(df)

#--------------  Prediction

pred = model.predict(df)
pred = pred[0][0]

def Chance(pred):
    if pred>=0.5:
        return 'The Person will likely Survive :)'
    else:
        return 'Likely Not Survived :<'
    
if st.button('Predict Survival Chances'):
    st.write('The Probability of Survival Chances',pred)
    st.write(Chance(pred))