import streamlit as st
import tkinter as tk

root = tk.Tk()
label= tk.Label(root,
text="Created By Engr M.Kamil Hanif")
label.pack(side=tk.BOTTOM)
root.mainloop()


def convert_units(value, from_unit, to_unit, conversion_type):
    conversion_factors = {
        "length": {
            "meters_to_km": 0.001,
            "km_to_meters": 1000,
            "meters_to_inches": 39.3701,
            "inches_to_meters": 0.0254    
        },
        "temperature": {
            "celsius_to_fahrenheit": lambda c: (c * 9/5) + 32,
            "fahrenheit_to_celsius": lambda f: (f - 32) * 5/9
        },
        "weight": {
            "kg_to_g": 1000,
            "g_to_kg": 0.001,
            "kg_to_lbs": 2.20462,
            "lbs_to_kg": 0.453592
        },
        "volume": {
            "liters_to_gallons": 0.264172,
            "gallons_to_liters": 3.78541,
            "cubic_meters_to_liters": 1000,
            "liters_to_cubic_meters": 0.001
        },
        "time": {
            "seconds_to_minutes": 1 / 60,
            "minutes_to_seconds": 60,
            "hours_to_minutes": 60,
            "minutes_to_hours": 1 / 60
        },
        "speed": {
            "mps_to_kmph": 3.6,
            "kmph_to_mps": 1 / 3.6
        },
        "area": {
            "sq_meters_to_sq_km": 1e-6,
            "sq_km_to_sq_meters": 1e6,
            "sq_inches_to_sq_cm": 6.4516,
            "sq_cm_to_sq_inches": 0.155
        },
        "pressure": {
            "atm_to_pa": 101325,
            "pa_to_atm": 1 / 101325
        }
    }

    # Select conversion based on type
    if conversion_type == "Length":
        if from_unit == "meters" and to_unit == "km":
            return value * conversion_factors["length"]["meters_to_km"]
        elif from_unit == "km" and to_unit == "meters":
            return value * conversion_factors["length"]["km_to_meters"]
        elif from_unit == "meters" and to_unit == "inches":
            return value * conversion_factors["length"]["meters_to_inches"]
        elif from_unit == "inches" and to_unit == "meters":
            return value * conversion_factors["length"]["inches_to_meters"]

    elif conversion_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return conversion_factors["temperature"]["celsius_to_fahrenheit"](value)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return conversion_factors["temperature"]["fahrenheit_to_celsius"](value)

    elif conversion_type == "Weight":
        if from_unit == "kg" and to_unit == "g":
            return value * conversion_factors["weight"]["kg_to_g"]
        elif from_unit == "g" and to_unit == "kg":
            return value * conversion_factors["weight"]["g_to_kg"]
        elif from_unit == "kg" and to_unit == "lbs":
            return value * conversion_factors["weight"]["kg_to_lbs"]
        elif from_unit == "lbs" and to_unit == "kg":
            return value * conversion_factors["weight"]["lbs_to_kg"]

    elif conversion_type == "Volume":
        if from_unit == "liters" and to_unit == "gallons":
            return value * conversion_factors["volume"]["liters_to_gallons"]
        elif from_unit == "gallons" and to_unit == "liters":
            return value * conversion_factors["volume"]["gallons_to_liters"]
        elif from_unit == "cubic meters" and to_unit == "liters":
            return value * conversion_factors["volume"]["cubic_meters_to_liters"]
        elif from_unit == "liters" and to_unit == "cubic meters":
            return value * conversion_factors["volume"]["liters_to_cubic_meters"]

    elif conversion_type == "Time":
        if from_unit == "seconds" and to_unit == "minutes":
            return value * conversion_factors["time"]["seconds_to_minutes"]
        elif from_unit == "minutes" and to_unit == "seconds":
            return value * conversion_factors["time"]["minutes_to_seconds"]
        elif from_unit == "hours" and to_unit == "minutes":
            return value * conversion_factors["time"]["hours_to_minutes"]
        elif from_unit == "minutes" and to_unit == "hours":
            return value * conversion_factors["time"]["minutes_to_hours"]

    elif conversion_type == "Speed":
        if from_unit == "m/s" and to_unit == "km/h":
            return value * conversion_factors["speed"]["mps_to_kmph"]
        elif from_unit == "km/h" and to_unit == "m/s":
            return value * conversion_factors["speed"]["kmph_to_mps"]

    elif conversion_type == "Area":
        if from_unit == "sq meters" and to_unit == "sq km":
            return value * conversion_factors["area"]["sq_meters_to_sq_km"]
        elif from_unit == "sq km" and to_unit == "sq meters":
            return value * conversion_factors["area"]["sq_km_to_sq_meters"]
        elif from_unit == "sq inches" and to_unit == "sq cm":
            return value * conversion_factors["area"]["sq_inches_to_sq_cm"]
        elif from_unit == "sq cm" and to_unit == "sq inches":
            return value * conversion_factors["area"]["sq_cm_to_sq_inches"]

    elif conversion_type == "Pressure":
        if from_unit == "atm" and to_unit == "Pa":
            return value * conversion_factors["pressure"]["atm_to_pa"]
        elif from_unit == "Pa" and to_unit == "atm":
            return value * conversion_factors["pressure"]["pa_to_atm"]

    return None

# Streamlit app
def main():
    st.title("🍳 Unit Converter")
    
    st.sidebar.header("Select Conversion Type")
    conversion_type = st.sidebar.radio(
        "Choose conversion type", 
        ("Length", "Temperature", "Weight", "Volume", "Time", "Speed", "Area", "Pressure")
    )

    # Define units for each conversion type
    units = {
        "Length": ["meters", "km", "inches"],
        "Temperature": ["Celsius", "Fahrenheit"],
        "Weight": ["kg", "g", "lbs"],
        "Volume": ["liters", "gallons", "cubic meters"],
        "Time": ["seconds", "minutes", "hours"],
        "Speed": ["m/s", "km/h"],
        "Area": ["sq meters", "sq km", "sq inches", "sq cm"],
        "Pressure": ["atm", "Pa"]
    }

    # Unit selection
    units_list = units[conversion_type]
    from_unit = st.selectbox("From unit", units_list)
    to_unit = st.selectbox("To unit", units_list)
    
    # Input value
    value = st.number_input("Enter value", value=1.0)

    # Perform conversion
    if st.button("Click for Convert"):
        result = convert_units(value, from_unit, to_unit, conversion_type)
        if result is not None:
            st.write(f"Converted value: {result} {to_unit}")
        else:
            st.write("Invalid conversion!")

if __name__ == "__main__":
    main()


# Your main content
st.title("")

st.write("Thank you❤")

# Adding a footer at the bottom of the page
footer = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    <div class="footer">
        <p>Created by Engr M.Kamil Hanif | mkamilhanif789@gmail.com</p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
