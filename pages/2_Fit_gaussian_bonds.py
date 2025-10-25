import streamlit as st
import altair as alt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

def gaussian_potential(x, *parameters):
    """function with the gaussian potential"""
    sum_gaussians = 0
    
    for j in range(0, int(len(parameters)/3)):
        prefactor = parameters[3*j]/(parameters[3*j+1]*np.sqrt(np.pi/2))
        exponential = np.exp((-2*np.power(parameters[3*j+2]-x, 2))/np.power(parameters[3*j+1], 2))
        sum_gaussians += (prefactor*exponential)

    return sum_gaussians

# sum of squares
def ssq(z):
    return(np.sum(z**2))

st.header("An App to fit Gaussian functions to a list of bond lengths")

# Add interactive elements
with st.form("myform"):
    help_str = "The decimal separator must be a dot and not a comma. The file is assumed to have two columns of equal length: the first is ignored and the second is the bond length"
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv"], help=help_str)
    n_gaussians = st.text_input("Number of Gaussians [integer]:")
    submit = st.form_submit_button("Plot data")
    if submit:
        if uploaded_file is not None:
            input_stream = uploaded_file.getvalue().decode('utf-8').replace(",", "").split()
            raw_data = [float(i) for i in input_stream[1::2]]
            hist, bin_edges = np.histogram(raw_data, bins='auto', density=True)
            bin_mid_points = [0.5*(bin_edges[i] + bin_edges[i+1]) for i in range(0, len(hist))]
            st.session_state['gb_data'] = pd.DataFrame({'bin mid points': bin_mid_points, 'Histogram': hist})
            
            try:
                n_gaussians = int(n_gaussians)
                if n_gaussians > 0:
                    st.session_state['gb_n_gaussians'] = n_gaussians
                    st.session_state['gb_mean_value'] = sum(bin_mid_points*hist)/len(bin_mid_points)
                else:
                    st.write("The number of Gaussian terms must be greater than zero")
            except ValueError:
                st.write("You have not entered a valid number of Gaussian terms")

        else:
            st.write("you need to upload a valid txt or csv file")

# Plot the data
if 'gb_data' in st.session_state:
    with st.form("myform2"):
        fig1 = alt.Chart(st.session_state['gb_data']).mark_point(filled=True).encode(x='bin mid points',y='Histogram')
        submit2 = st.form_submit_button("Fit gaussian expression")
        if submit2:
            if 'gb_n_gaussians' not in st.session_state:
                st.write("You have not entered a valid number of Gaussian terms")
            else:
                try:
                    p0 = [0] * (3 * st.session_state['gb_n_gaussians'])
                    for iel in range(0, st.session_state['gb_n_gaussians']):
                        p0[3 * iel] = 1.0 / st.session_state['gb_n_gaussians']
                        p0[3 * iel + 1] = st.session_state['gb_mean_value']
                        p0[3 * iel + 2] = 1.0 # should be corrected / improved
                    popt, pcov = curve_fit(gaussian_potential, st.session_state['gb_data']['bin mid points'], st.session_state['gb_data']['Histogram'], p0)
                    st.write(popt)
                except RuntimeError as e:
                    st.write("Optimal parameters not found")
        else:
            st.altair_chart(fig1.interactive())

if st.button("Reset"):
    if 'gb_data' in st.session_state:
        del st.session_state['gb_data']
    if 'gb_data_from_fitting' in st.session_state:
        del st.session_state['gb_data_from_fitting']
    if 'gb_n_gaussians' in st.session_state:
        del st.session_state['gb_n_gaussians'] 
    if 'gb_mean_value' in st.session_state:
        del st.session_state['gb_mean_value']
    st.rerun()
