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

    if submitted:

        try:
            temperature = float(temperature)
            if temperature > 0:
                st.write(f"The temperature is: {temperature}")
                st.session_state['temperature'] = temperature
            else:
                st.write("The temperature should be greater than zero")
        except ValueError:
            st.write("You have not entered a valid temperature")

        try:
            density = float(density)
            if density > 0:
                st.write(f"The number density is: {density}")
                st.session_state['density'] = density
            else:
                st.write("The density should be greater than zero")
        except ValueError:
            st.write("You have not entered a valid density")

        try:
            number = int(number)
            if number > 0:
                st.write(f"The number of DPD bead types is: {number}")
                st.session_state['number'] = number
            else:
                st.write("The number of DPD bead types should be greater than zero")
        except ValueError:
            st.write("You have not entered a valid number of DPD bead types")
