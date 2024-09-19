import streamlit as st

# Add custom CSS for layout and buttons
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 14px;  /* Smaller font size */
        padding: 6px 12px; /* Adjusted padding for a smaller button */
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin: 0 auto;  /* Centers button horizontally */
    }

    .stButton>button:active {
        background-color: black; /* Change color to black when clicked */
        color: white;
    }

    .stButton>button:hover {
        background-color: black;  /* Hover effect to black */
    }

    .stTextArea textarea {
        font-size: 16px;
        padding: 10px;
        border: 2px solid #000; /* Set border color to black */
        border-radius: 4px;
        color: #000; /* Ensure text remains black */
    }

    .stSelectbox select {
        font-size: 16px;
        padding: 8px;
        border-radius: 4px;
    }

    h1 {
        color: #4CAF50;
        font-weight: bold;
    }

    /* Fix alignment issues */
    .stColumn {
        display: flex;
        justify-content: flex-start; /* Align content to the left for a cleaner layout */
        align-items: center;      /* Align vertically to the middle */
    }

    /* Make buttons smaller and align them properly */
    .stButton {
        width: auto !important;
        margin-right: 10px;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.markdown("<h1>Validator Tool</h1>", unsafe_allow_html=True)

# Create column for dropdown (button will be placed below)
col1 = st.columns([1])[0]

# Dropdown to select a test case inside the first column
with col1:
    test_cases = ["Select a test case", "Test Case 1", "Test Case 2", "Test Case 3"]
    selected_test_case = st.selectbox("Select a Test Case", test_cases)

    # Search button now placed below the dropdown
    search_button = st.button("Search")

# Initialize the text in the answer box
initial_answer = ""

# Logic to update the answer when the search button is pressed
if search_button and selected_test_case != "Select a test case":
    answer = f"Answer for {selected_test_case}"  # Simulating an answer based on the selected test case
else:
    answer = initial_answer

# Text area for displaying the answer
st.text_area("Answer", value=answer, height=150)

# Create columns for Validate and Reset buttons
col3, col4 = st.columns([1, 1])

# Validate button
with col3:
    validate_button = st.button("Validate")

# Reset button
with col4:
    reset_button = st.button("Reset")

# Placeholder for validation message
validation_message = st.empty()

# Logic for validation and reset
if validate_button:
    validation_message.text_area("Validation Message", value="Your answer has been validated", height=100)

if reset_button:
    st.experimental_rerun()
