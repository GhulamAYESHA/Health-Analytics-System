import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Health Analytics System",
    layout="centered"
)

st.title("❤️ Health Analytics System")
st.markdown("A simple real-world health analysis app using standard formulas")

st.divider()

# ---------------- USER INPUTS ----------------
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age (years)", min_value=10, max_value=100)
weight = st.number_input("Weight (kg)", min_value=30.0)
height = st.number_input("Height (cm)", min_value=120.0)

activity = st.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ]
)

goal = st.selectbox(
    "Health Goal",
    ["Maintain Weight", "Lose Weight", "Gain Weight"]
)

st.divider()

# ---------------- CALCULATIONS ----------------
if st.button("🔍 Analyze Health"):

    # BMI Calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # BMR Calculation (Mifflin–St Jeor)
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Activity Factors
    activity_factor = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }

    tdee = bmr * activity_factor[activity]

    if goal == "Lose Weight":
        target_calories = tdee - 500
    elif goal == "Gain Weight":
        target_calories = tdee + 500
    else:
        target_calories = tdee

    # ---------------- OUTPUT ----------------
    st.success(f"BMI: {bmi:.2f}")
    st.info(f"BMI Category: {category}")
    st.write(f"BMR: {bmr:.0f} kcal/day")
    st.write(f"Daily Calorie Requirement: {tdee:.0f} kcal/day")
    st.warning(f"Recommended Calories: {target_calories:.0f} kcal/day")

    # ---------------- BMI CHART ----------------
    fig, ax = plt.subplots(figsize=(7, 2))

    # WHO BMI ranges
    ax.barh(["Underweight"], [18.5], color="#cce5ff")
    ax.barh(["Normal"], [6.4], left=18.5, color="#d4edda")
    ax.barh(["Overweight"], [5], left=25, color="#fff3cd")
    ax.barh(["Obese"], [15], left=30, color="#f8d7da")

    # User BMI marker
    ax.axvline(bmi, color="black", linewidth=2)
    ax.text(bmi + 0.3, 0.1, f"Your BMI: {bmi:.1f}")

    ax.set_xlim(10, 45)
    ax.set_xlabel("BMI Scale")
    ax.set_yticks([])
    ax.set_title("BMI Classification (WHO Standard)")

    st.pyplot(fig)
