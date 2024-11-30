# Libraries
import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Title of the app
st.title("Glavu gore!")

st.markdown("**Pomoži nam da zabeležimo sve građevine u Srbiji gde postoji opasnost od obrušavanja**")

# Function to get address from latitude and longitude using reverse geocoding
def get_address(lat, lng):
    geolocator = Nominatim(user_agent="streamlit_map_app")
    location = geolocator.reverse((lat, lng), language='sr')  # language='sr' for Serbian
    return location.address if location else "Address not found"

# Create a Folium map centered on a specific location (e.g., Serbia) with a grayscale tile layer
m = folium.Map(location=[45.26535001807013, 19.829569286510928], zoom_start=15, 
               tiles="cartodbpositron")  # Greyscale tile layer

# Add a LatLngPopup to the map, which shows the clicked position
m.add_child(folium.LatLngPopup())

# Render the map in Streamlit using st_folium and capture the click event
map_data = st_folium(m, width=700)

# Extract the latitude and longitude from the map click event (if clicked)
location = None
if map_data and map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    location = get_address(lat, lon)

# User input fields below the map
st.subheader("Unos podataka o građevini")

# Location field - populated with the address from the clicked location
location_input = st.text_input("Lokacija", value=location if location else "")

# Input for building type
building_type = st.radio("Gradjevina", ["Privatna", "Javna"])

# Input for labeling status
labeling_status = st.radio("Obeleženo", ["Da", "Ne", "Delimično"])

# Input for additional description
description = st.text_area("Dodatni opis", "")

# Display the inputs
st.write(f"Uneta lokacija: {location_input}")
st.write(f"Vrsta građevine: {building_type}")
st.write(f"Obeleženo: {labeling_status}")
st.write(f"Opis: {description}")


# Add the submit button
if st.button("Unesi građevinu"):
    st.write(f"Gradjevina je uspešno unesena!")