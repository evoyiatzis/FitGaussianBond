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

if all(x in st.session_state for x in ['number', 'temperature', 'density']):
    with st.form("second_form"):
        st.write("**Pure Component Density**")

        df2 = pd.DataFrame(0, index = np.arange(1, st.session_state.number+1, 1), columns=1, dtype=np.float64)
        edited_df2 = st.data_editor(df2)

        st.write("**Flory–Huggins parameters**")

        df = pd.DataFrame(0, index = np.arange(1, st.session_state.number+1, 1), columns=np.arange(1, st.session_state.number+1,1), dtype=np.float64)
        edited_df = st.data_editor(df)

        submit = st.form_submit_button("Submit")

        if submit:
            st.session_state['edited_df']= edited_df
            st.session_state['edited_df2']= edited_df2

if st.button("Reset"):
    if 'number' in st.session_state:
        del st.session_state['number']
    if 'temperature' in st.session_state:
        del st.session_state['temperature']
    if 'density' in st.session_state:
        del st.session_state['density']
    if 'edited_df' in st.session_state:
        del st.session_state['edited_df']
    if 'edited_df2' in st.session_state:
        del st.session_state['edited_df2']

    st.rerun()
