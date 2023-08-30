import tkinter as tk
from tkinter import ttk
import folium

def show_map():
    # Create a map centered at a specific location
    m = folium.Map(location=[latitude, longitude], zoom_start=12)
    
    # Add markers based on coordinates from your database
    for coord in coordinates_from_database:
        folium.Marker([coord['latitude'], coord['longitude']], popup=coord['name']).add_to(m)
    
    # Create HTML file and open it in a browser
    m.save('map.html')
    import webbrowser
    webbrowser.open('map.html')

window = tk.Tk()
window.title('Map Example')

# Replace with your actual data
latitude = 51.5074  # Example latitude
longitude = -0.1278  # Example longitude
coordinates_from_database = [
    {'latitude': 51.5074, 'longitude': -0.1278, 'name': 'Location 1'},
    {'latitude': 51.5174, 'longitude': -0.1378, 'name': 'Location 2'}
]

show_map_button = ttk.Button(window, text='Show Map', command=show_map)
show_map_button.pack()

window.mainloop()
