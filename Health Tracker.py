import streamlit as st
import matplotlib.pyplot as plt

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

# Streamlit App Layout
st.title("Personalized Health Tracker")

# Input Section
age = st.slider('Enter your age', 1, 100, 25)
weight = st.slider('Enter your weight (in kg)', 30, 150, 70)
height = st.slider('Enter your height (in meters)', 1.0, 2.2, 1.70)
activity_level = st.selectbox('Select your activity level', ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active'])

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
if bmi < 18.5:
    st.write("You are underweight. Consider increasing your calorie intake and focusing on strength training.")
elif 18.5 <= bmi <= 24.9:
    st.write("You have a healthy weight! Maintain your current diet and exercise routine.")
elif 25 <= bmi <= 29.9:
    st.write("You are overweight. Aim to reduce calorie intake by 500 kcal/day and incorporate cardio exercises.")
else:
    st.write("You are in the obese range. It’s advised to consult a healthcare provider for personalized advice.")

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
    ax.plot(days, water_recommendation, label="Recommended Water Intake (liters)")
    ax.set_xlabel("Days")
    ax.set_ylabel("Water Intake (liters)")
    ax.legend()
    st.pyplot(fig)

# Option to Track Progress
if st.checkbox('Track progress'):
    st.write("You can add a progress tracking feature using data input and graphs here.")

