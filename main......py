import streamlit as st

# Create a Streamlit app
st.title('Audit and Assurance Calculator')

# Sidebar to select the type of calculation and input data
calculation_type = st.sidebar.radio("Select Calculation Type", ["Audit", "Assurance"])
calculate = st.sidebar.button("Calculate")

if calculation_type == "Audit":
    st.sidebar.subheader("Audit Input")
    total_assets = st.sidebar.number_input("Total Assets", min_value=0.0, value=1000000.0, step=1000.0)
    inherent_risk = st.sidebar.number_input("Inherent Risk", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    control_risk = st.sidebar.number_input("Control Risk", min_value=0.0, max_value=1.0, value=0.1, step=0.01)

    if calculate:
        # Calculate Audit Risk
        audit_risk = inherent_risk * control_risk
        st.write(f"Total Assets: ${total_assets}")
        st.write(f"Total Audit Risk: {audit_risk * 100:.2f}%")
        st.write("Interpretation: Audit risk is the likelihood of material misstatement in the financial statements. A lower audit risk indicates a more reliable audit.")

elif calculation_type == "Assurance":
    st.sidebar.subheader("Assurance Input")
    confidence_level = st.sidebar.number_input("Confidence Level (%)", min_value=0, max_value=100, value=95)
    sample_size = st.sidebar.number_input("Sample Size", min_value=1, step=1)
    error_rate = st.sidebar.number_input("Error Rate (%)", min_value=0, max_value=100, step=1)

    if calculate:
        # Calculate the Margin of Error
        margin_of_error = 100 - confidence_level
        st.write(f"Margin of Error: {margin_of_error}%")

        # Calculate the Assurance Percentage
        assurance_percentage = 100 - margin_of_error
        st.write(f"Assurance Percentage: {assurance_percentage}%")

        # Calculate the Estimated Error
        estimated_error = (error_rate / 100) * sample_size
        st.write(f"Estimated Error: {estimated_error}")
        
        st.write("Interpretation: Assurance percentage represents the level of confidence in the sample results. A higher assurance percentage indicates greater confidence. Estimated error is the expected error in the sample.")

st.subheader('Calculated Results')
# Display results based on the selected calculation type