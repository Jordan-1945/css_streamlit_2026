# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:06:52 2026

@author: sphum
"""

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Post-doc Medicinal Chemistry, fellow University of Johannesburg", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Contact"],
)

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Jordan Tonga Lembe"
    field = "Medicinal Chemistry"
    institution = "University of Johannesburg"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
    "https://www.brettelliott.com/wp-content/uploads/2024/01/Natural-or-synthetic.jpg",
    caption="from nature to cure"
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
    else:
        uploaded_file = "citations.csv"
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
        


        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")



elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jordant@uj.ac.za"
    st.write(f"You can reach me at {email}.")