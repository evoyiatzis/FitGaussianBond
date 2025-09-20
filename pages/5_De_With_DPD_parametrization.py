import streamlit as st

st.header("Parametrization of DPD models using the De With approach")

st.text("This is a WebApp for the parametrization of DPD models using the de With methodology. "
        "The reference is 'A generalized method for parameterization of dissipative particle dynamics for variable bead volumes' "
        "Europhysics Letters DOI:10.1209/0295-5075/102/40009")

with st.form("my_form"):
    st.write("**System Properties**")
    temperature = st.text_input("Temperature in DPD units usually 1.0 [float]")
    density = st.text_input("Number density in DPD units usually 3.0 [float]")
    number = st.text_input("Number of DPD bead types in the system [integer]")
    submitted = st.form_submit_button("Submit")
