import streamlit as st
import pandas as pd
import numpy as np
import torch
#Dicts
manufacturer_dic = {'Acura': 0,
 'Alfa-Romeo': 1,
 'Audi': 2,
 'BMW': 3,
 'Buick': 4,
 'Cadillac': 5,
 'Chevrolet': 6,
 'Chrysler': 7,
 'Dodge': 8,
 'Ferrari': 9,
 'Fiat': 10,
 'Ford': 11,
 'GMC': 12,
 'Harley-Davidson': 13,
 'Honda': 14,
 'Hyundai': 15,
 'Infiniti': 16,
 'Jaguar': 17,
 'Jeep': 18,
 'Kia': 19,
 'Lexus': 20,
 'Lincoln': 21,
 'Mazda': 22,
 'Mercedes-Benz': 23,
 'Mercury': 24,
 'Mini': 25,
 'Mitsubishi': 26,
 'Nissan': 27,
 'Pontiac': 28,
 'Porsche': 29,
 'Ram': 30,
 'Rover': 31,
 'Saturn': 32,
 'Subaru': 33,
 'Tesla': 34,
 'Toyota': 35,
 'Volkswagen': 36,
 'Volvo': 37}
condition_dic = {'excellent': 0, 'fair': 1, 'good': 2, 'like new': 3, 'new': 4, 'salvage': 5}
fuel_dic = {'diesel': 0, 'electric': 1, 'fuel': 2, 'gas': 3, 'hybrid': 4, 'other': 5}
title_dic = {'clean': 0, 'lien': 1, 'missing': 2, 'parts only': 3, 'rebuilt': 4, 'salvage': 5}
transmission_dic = {'automatic': 0, 'manual': 1, 'other': 2}
drive_dic = {'4 wheel drive': 0, 'front wheel drive': 1, 'rear wheel drive': 2}
type_dic = {'SUV': 0, 'bus': 1, 'convertible': 2, 'coupe': 3, 'hatchback': 4, 'mini-van': 5, 'offroad': 6, 'other': 7, 'pickup': 8, 'sedan': 9, 'truck': 10, 'van': 11, 'wagon': 12}
state_dic = {
    "Alabama": 0,
    "Alaska": 1,
    "Arizona": 2,
    "Arkansas": 3,
    "California": 4,
    "Colorado": 5,
    "Connecticut": 6,
    "Delaware": 7,
    "Florida": 8,
    "Georgia": 9,
    "Hawaii": 10,
    "Idaho": 11,
    "Illinois": 12,
    "Indiana": 13,
    "Iowa": 14,
    "Kansas": 15,
    "Kentucky": 16,
    "Louisiana": 17,
    "Maine": 18,
    "Maryland": 19,
    "Massachusetts": 20,
    "Michigan": 21,
    "Minnesota": 22,
    "Mississippi": 23,
    "Missouri": 24,
    "Montana": 25,
    "Nebraska": 26,
    "Nevada": 27,
    "New Hampshire": 28,
    "New Jersey": 29,
    "New Mexico": 30,
    "New York": 31,
    "North Carolina": 32,
    "North Dakota": 33,
    "Ohio": 34,
    "Oklahoma": 35,
    "Oregon": 36,
    "Pennsylvania": 37,
    "Rhode Island": 38,
    "South Carolina": 39,
    "South Dakota": 40,
    "Tennessee": 41,
    "Texas": 42,
    "Utah": 43,
    "Vermont": 44,
    "Virginia": 45,
    "Washington": 46,
    "West Virginia": 47,
    "Wisconsin": 48,
    "Wyoming": 49}
#Lists
manufacturer_list = ['Acura',
 'Alfa-Romeo',
 'Audi',
 'BMW',
 'Buick',
 'Cadillac',
 'Chevrolet',
 'Chrysler',
 'Dodge',
 'Ferrari',
 'Fiat',
 'Ford',
 'GMC',
 'Harley-Davidson',
 'Honda',
 'Hyundai',
 'Infiniti',
 'Jaguar',
 'Jeep',
 'Kia',
 'Lexus',
 'Lincoln',
 'Mazda',
 'Mercedes-Benz',
 'Mercury',
 'Mini',
 'Mitsubishi',
 'Nissan',
 'Pontiac',
 'Porsche',
 'Ram',
 'Rover',
 'Saturn',
 'Subaru',
 'Tesla',
 'Toyota',
 'Volkswagen',
 'Volvo']
condition_list = ['excellent', 'fair', 'good', 'like new', 'new', 'salvage']
fuel_list = ['diesel', 'electric', 'fuel', 'gas', 'hybrid', 'other']
title_list = ['clean', 'lien', 'missing', 'parts only', 'rebuilt', 'salvage']
transmission_list = ['automatic', 'manual', 'other']
drive_list = ['4 wheel drive', 'front wheel drive', 'rear wheel drive']
type_list = ['SUV', 'bus', 'convertible', 'coupe', 'hatchback', 'mini-van', 'offroad', 'other', 'pickup', 'sedan', 'truck', 'van', 'wagon']
state_list = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
#Page
st.set_page_config(page_title='Craigslist Car Price Prediction by Group 8')
#Model
model = torch.load('cars.pkl')
#Site
st.markdown("<h2 style='text-align: center;'>Craigslist Car Price Prediction  🚗</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
odometer = col1.number_input(label='Enter number on Odometer in miles, e.g: 200 mile (enter number only)', help='Odometer reading')
year =  col1.slider('Enter the year when the car was manufactured, e.g: 2005', 1903,2022,2010,help='The year when the car was made.')
manufacturer_val = col1.selectbox(label='Enter the manufacturer of the car', options=manufacturer_list, help='manufacturer?')
manufacturer = manufacturer_dic[manufacturer_val]
condition_val = col1.selectbox(label='Enter the condition of the car', options=condition_list, help='condition?')
condition = condition_dic[condition_val]
fuel_val = col1.selectbox(label='Enter the fuel type of the car', options=fuel_list, help='fuel?')
fuel = fuel_dic[fuel_val]
title_val = col2.selectbox(label='Enter the title status of the car', options=title_list, help='title?')
title = title_dic[title_val]
transmission_val = col2.selectbox(label='Enter the transmission of the car', options=transmission_list, help='transmission?')
transmission = transmission_dic[transmission_val]
drive_val = col2.selectbox(label='Enter the drive of the car', options=drive_list, help='drive?')
drive = drive_dic[drive_val]
type_val = col2.selectbox(label='Enter the type of the car', options=type_list, help='type?')
type = type_dic[type_val]
state_val = col2.selectbox(label='Enter the state of the car', options=state_list, help='state?')
state = state_dic[state_val]

input_tensor = torch.tensor([(year-1903)/(2022-1903),manufacturer/37.,condition/5.,fuel/5.,odometer/10000000.,title/5.,transmission/2.,drive/2.,type/12.,state/50.],dtype=torch.float)
prediction = col1.button('Prediction')

if prediction: 
        y = model(input_tensor) * 229500
        y = round(float(y),2)
        final = 'The predicted price of the car is $ '+ str(y)
        st.success(final)
