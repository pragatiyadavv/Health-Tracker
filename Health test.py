import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)


# Function to calculate daily calorie needs
def calculate_calories(weight, height, age, activity_level):
    if activity_level == "Sedentary":
        factor = 1.2
    elif activity_level == "Lightly Active":
        factor = 1.375
    elif activity_level == "Moderately Active":
        factor = 1.55
    else:
        factor = 1.725
    bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5  # For men, adjust for women
    return bmr * factor


# Function to recommend water intake
def calculate_water_intake(weight):
    return weight * 0.033  # 33 ml per kg of body weight


# Function to provide food recommendations based on BMI
def food_recommendations(bmi):
    if bmi < 18.5:
        return "Increase your intake of whole grains, healthy fats, and protein-rich foods."
    elif 18.5 <= bmi <= 24.9:
        return "Maintain a balanced diet rich in fruits, vegetables, lean proteins, and whole grains."
    elif 25 <= bmi <= 29.9:
        return "Focus on portion control and include more vegetables, fruits, and lean proteins in your meals."
    else:
        return "Consult with a nutritionist for a personalized meal plan focusing on whole, low-calorie foods."


# Streamlit App Layout
st.title("Personalized Health Tracker")

# Input Section
age = st.slider('Enter your age', 1, 100, 25)
weight = st.slider('Enter your weight (in kg)', 30, 150, 70)
height = st.slider('Enter your height (in meters)', 1.0, 2.2, 1.70)
activity_level = st.selectbox('Select your activity level',
                              ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active'])

# Calculate BMI and other metrics
bmi = calculate_bmi(weight, height)
calories_needed = calculate_calories(weight, height, age, activity_level)
water_intake = calculate_water_intake(weight)

# Display Results
st.subheader("Health Summary:")
st.write(f"**Your BMI**: {bmi:.2f}")
st.write(f"**Daily Calorie Needs**: {calories_needed:.2f} kcal")
st.write(f"**Recommended Water Intake**: {water_intake:.2f} liters/day")

# Recommendations based on BMI
st.subheader("Recommendations:")
st.write(food_recommendations(bmi))

# Exercise Recommendations based on activity level
st.subheader("Exercise Recommendations:")
if activity_level == "Sedentary":
    st.write("Consider adding 30 minutes of light exercises like walking or cycling to your daily routine.")
elif activity_level == "Lightly Active":
    st.write("Good job! Try to include 3-4 days of moderate exercise per week, such as jogging or swimming.")
elif activity_level == "Moderately Active":
    st.write("You're active! Continue with 4-5 days of moderate to intense exercise to maintain fitness.")
else:
    st.write("Great! You're highly active. Focus on balancing cardio and strength training.")

# Water Intake Visualization (Optional)
if st.checkbox('Show water intake recommendation graph'):
    days = list(range(1, 8))
    water_recommendation = [water_intake] * 7  # Same recommendation for 7 days
    fig, ax = plt.subplots()
    ax.plot(days, water_recommendation, marker='o', label="Recommended Water Intake (liters)", color='blue')
    ax.fill_between(days, water_recommendation, color='skyblue', alpha=0.4)
    ax.set_xlabel("Days")
    ax.set_ylabel("Water Intake (liters)")
    ax.set_title("Recommended Water Intake Over a Week")
    ax.legend()
    st.pyplot(fig)

# Track Progress
if st.checkbox('Track progress'):
    st.write("You can add a progress tracking feature using data input and graphs here.")
    # Input for progress tracking
    progress_weight = st.number_input("Enter your current weight (kg) for tracking:", min_value=30, max_value=150,
                                      value=weight)
    st.write(f"**Current Weight for Tracking**: {progress_weight} kg")

    # Track historical data
    historical_weights = []
    if 'weights' not in st.session_state:
        st.session_state.weights = []

    # Add weight to historical data
    if st.button("Add to Progress"):
        st.session_state.weights.append(progress_weight)

    if st.session_state.weights:
        st.write("Your weight tracking history:")
        st.line_chart(st.session_state.weights)

# Add a motivational quote
st.sidebar.header("Motivational Quote")
st.sidebar.write("**Keep pushing forward! Every small step counts towards a healthier you!**")
