import streamlit as st

st.set_page_config(page_title='DPD multipage application')

st.title('Homepage')

st.text('It provides a few tools for the derivation of DPD models')

st.text('The Gaussian Apps describes a solution for fitting eqn 2 in 'Multicentered Gaussian-Based Potentials for Coarse-Grained Polymer Simulations: Linking Atomistic and Mesoscopic Scales'"

st.text("The standard DPD parametrization App derives the parameters of DPD models using the Groot De Warren methodology. "
        "The reference is 'Dissipative particle dynamics: "
        "Bridging the gap between atomistic and mesoscopic simulation' "
        "J. Chem. Phys. DOI:10.1063/1.474784")

st.text("This WebApp was created by Evangelos Voyiatzis.")
