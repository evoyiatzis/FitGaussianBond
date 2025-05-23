import streamlit as st
import altair as alt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

def gaussian_potential(x, *parameters):
    """function with the gaussian potential"""
    sum_gaussians = 0
    
    for j in range(0, n_gaussians):
        prefactor = parameters[3*j]/(parameters[3*j+1]*np.sqrt(np.pi/2))
        exponential = np.exp((-2*np.power(parameters[3*j+2]-x, 2))/np.power(parameters[3*j+1], 2))
        sum_gaussians += (prefactor*exponential)

    return sum_gaussians

# sum of squares
def ssq(z):
    return(np.sum(z**2))

st.header("An App to fit Gaussian functions to a bond probability density distribution")

st.markdown("This WebApp was created by Evangelos Voyiatzis.")

# Add interactive elements
with st.form("myform"):
    help_str = "The decimal separator must be a dot and not a comma. The file is assumed to have two columns of equal length: the first is the bond length and the second the probability density distribution "
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv"], help=help_str)
    n_gaussians = st.text_input("Number of Gaussians [integer]:")
    submit = st.form_submit_button("Plot data")
    if submit:
        if uploaded_file is not None:
            input_stream = uploaded_file.getvalue().decode('utf-8').replace(",", "").split()
            x = [float(i) for i in input_stream[0::2]]
            y = [float(i) for i in input_stream[1::2]]
            st.session_state['data'] = pd.DataFrame({'Bond Length': x, 'y': y})
        else:
            st.write("you need to upload a valid txt or csv file")

        try:
            n_gaussians = int(n_gaussians)
            if n_gaussians > 0:
                st.write(f"The number of Gaussian terms is: {n_gaussians}")
                st.session_state['n_gaussians'] = n_gaussians
            else:
                st.write("The number of Gaussian terms must be greater than zero")
        except ValueError:
            st.write("You have not entered a valid number of Gaussian terms")

# Plot the data
if 'data' in st.session_state:
    with st.form("myform2"):
        fig1 = alt.Chart(st.session_state['data']).mark_point(filled=True).encode(x='Bond Length',y='y') 
        submit2 = st.form_submit_button("Fit gaussian expression")
        if submit2:
            if 'n_gaussians' not in st.session_state:
                st.write("You have not entered a valid number of Gaussian terms")
            else:
                try:
                    st.write("Under Construction !")
                    #popt, pcov = curve_fit(gaussian_potential, bin_mid_points, prob_density_distr,p0)
                except RuntimeError as e:
                    st.write("Optimal parameters not found")
        else:
            st.altair_chart(fig1.interactive())

if st.button("Reset"):
    if 'data' in st.session_state:
        del st.session_state['data']
    if 'data_from_fitting' in st.session_state:
        del st.session_state['data_from_fitting']
    if 'n_gaussians'  in st.session_state:
        del st.session_state['n_gaussians'] 
    st.rerun()
