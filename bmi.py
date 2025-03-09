import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Increase calorie intake, focus on proteins and healthy fats.", "#FFD700"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Maintain your current lifestyle and keep exercising.", "#008000"
    elif 25 <= bmi < 29.9:
        return "Overweight", "Consider a balanced diet and regular exercise.", "#FFA500"
    else:
        return "Obese", "Consult a doctor or nutritionist for guidance.", "#FF0000"

def unit_converter():
    st.sidebar.header("Unit Converter")
    conversion_type = st.sidebar.selectbox("Choose conversion type:", ["Length", "Temperature", "Area", "Volume", "Weight"])
    value = st.sidebar.number_input("Enter value:", min_value=0.0, format="%.2f")
    
    conversion_data = []
    
    if conversion_type == "Length":
        conversion_data = [
            ["Meters", value * 0.3048],
            ["Feet", value * 3.28084]
        ]
    elif conversion_type == "Temperature":
        conversion_data = [
            ["Celsius", (value - 32) * 5/9],
            ["Fahrenheit", (value * 9/5) + 32]
        ]
    elif conversion_type == "Area":
        conversion_data = [
            ["Square meters", value * 0.092903],
            ["Square feet", value * 10.764]
        ]
    elif conversion_type == "Volume":
        conversion_data = [
            ["Liters", value * 3.78541],
            ["Gallons", value / 3.78541]
        ]
    elif conversion_type == "Weight":
        conversion_data = [
            ["Kilograms", value * 0.453592],
            ["Pounds", value / 0.453592]
        ]
    
    if conversion_data:
        df = pd.DataFrame(conversion_data, columns=["Unit", "Converted Value"])
        st.sidebar.table(df)

def main():
    st.markdown("""
        <style>
            .big-font {font-size:22px !important; font-weight: bold;}
            .green {color: #0080900;}
            .yellow {color: #FFD700;}
            .orange {color: #FFA500;}
            .red {color: #FF0000;}
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Enhanced BMI Calculator")
    unit_converter()  # Sidebar unit converter with table
    
    st.subheader("User Information")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
    with col2:
        gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
    
    st.subheader("Measurement Details")
    col3, col4 = st.columns(2)
    with col3:
        weight_unit = st.selectbox("Select weight unit:", ["Kilograms", "Pounds"])
        weight = st.number_input("Enter your weight:", min_value=1.0, format="%.2f")
    
    with col4:
        height_unit = st.selectbox("Select height unit:", ["Meters", "Centimeters", "Feet & Inches"])
    
    if height_unit == "Meters":
        height = st.number_input("Enter your height:", min_value=0.5, format="%.2f")
    elif height_unit == "Centimeters":
        height = st.number_input("Enter your height (cm):", min_value=50.0, format="%.2f") / 100
    else:
        feet = st.number_input("Feet:", min_value=1, format="%d")
        inches = st.number_input("Inches:", min_value=0, max_value=11, format="%d")
        height = (feet * 0.3048) + (inches * 0.0254)
    
    if weight_unit == "Pounds":
        weight *= 0.453592  # Convert pounds to kg
    
    if st.button("Calculate BMI", help="Click to calculate your Body Mass Index"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            category, advice, color = bmi_category(bmi)
            st.markdown(f"""<p class='big-font {color[1:]}'>Your BMI is: {bmi:.2f}</p>""", unsafe_allow_html=True)
            st.markdown(f"""<p class='big-font {color[1:]}'>Category: {category}</p>""", unsafe_allow_html=True)
            st.markdown(f"""<p class='big-font'>Health Advice: {advice}</p>""", unsafe_allow_html=True)
        else:
            st.error("Please enter a valid height.")

if __name__ == "__main__":
    main()
