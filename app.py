import streamlit as st
import numpy as np
import joblib


#joblib.dump(model, "logistic_model.pkl")
model = joblib.load("logistic_model.pkl")

st.title("🎓 Predict Your Engineering Major")
st.subheader("Answer a few questions to see where your interest aligns.")

engines = st.slider("Interest in engines/machines", 1, 5, 3)
aviation = st.slider("Interest in planes/aviation", 1, 5, 3)

work_pref = st.radio("Preferred work area:", [
    "Fluid dynamics and aerodynamics",
    "Thermodynamics and mechanics",
    "I like both equally",
    "I’m not sure yet"
])
work_map = {
    "Fluid dynamics and aerodynamics": 1,
    "Thermodynamics and mechanics": 0,
    "I like both equally": 0.5,
    "I’m not sure yet": 0.5
}

excite = st.radio("What excites you most?", [
    "Jet engines and aircraft systems",
    "Space exploration and satellite systems",
    "Robotics and mechanical devices",
    "Automotive design and engines"
])
excite_map = {
    "Jet engines and aircraft systems": 1,
    "Space exploration and satellite systems": 1,
    "Robotics and mechanical devices": 0,
    "Automotive design and engines": 0
}

design = st.radio("Preferred design challenge:", [
    "Optimizing aerodynamic surfaces for aircraft",
    "Designing energy-efficient mechanical parts",
    "Both",
    "Neither"
])
design_map = {
    "Optimizing aerodynamic surfaces for aircraft": 1,
    "Designing energy-efficient mechanical parts": 0,
    "Both": 0.5,
    "Neither": 0
}

project = st.radio("Final-year project choice:", [
    "Designing a flight simulation system",
    "Modeling a spacecraft component",
    "Building an autonomous robot",
    "Developing a fuel-efficient car engine"
])
project_map = {
    "Designing a flight simulation system": 1.0,
    "Modeling a spacecraft component": 0.75,
    "Building an autonomous robot": 0.25,
    "Developing a fuel-efficient car engine": 0.0
}

work_type = st.radio("Preferred work type:", [
    "Simulating or analyzing flight and aerodynamic behaviour",
    "Designing and building mechanical systems",
    "Both equally"
])
work_type_map = {
    "Simulating or analyzing flight and aerodynamic behaviour": 1,
    "Designing and building mechanical systems": 0,
    "Both equally": 0.5
}

career = st.radio("Where do you see yourself working?", [
    "Aerospace engineering",
    "Automotive or manufacturing engineering",
    "Research and academia",
    "Still exploring"
])
career_map = {
    "Aerospace engineering": 1,
    "Automotive or manufacturing engineering": 0,
    "Research and academia": 0.5,
    "Still exploring": 0.5
}

goal = st.radio("Do you wanna have broader field to choose in higher studies?", ["Yes", "NO"])
goal_map = {"Yes": 0, "NO": 1}

}

# Make prediction
if st.button("Predict"):
    inputs = np.array([[
        engines,
        aviation,
        work_map[work_pref],
        excite_map[excite],
        design_map[design],
        project_map[project],
        work_type_map[work_type],
        career_map[career],
        goal_map[goal],
       
    ]])

    prediction = model.predict(inputs)[0]
    result = "🛩️ You tend to choose **Aeronautical Engineering**." if prediction == 1 else "⚙️ You tend to choose **Mechanical Engineering**."
    st.success(result)
