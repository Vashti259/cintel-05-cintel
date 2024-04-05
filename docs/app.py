import shiny

from shiny import reactive, render

# From shiny.express, import just ui
from shiny.express import ui

# Imports from Python Standard Library to simulate live data
import random
from datetime import datetime

# Import icons as you like
# --------------------------------------------

from faicons import icon_svg

# --------------------------------------------
# FOR LOCAL DEVELOPMENT
# --------------------------------------------
# Add all packages not in the Std Library
# to requirements.txt:
# faicons
# shiny
# shinylive


# And install them into an active project virtual environment (usually in .venv)

# SET UP THE REACIVE CONTENT


# PLANNING: We want to get a fake temperature and
@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic. Get random between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now" and use string format strftime() method to format it
    #
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    # Return everything we need
    return latest_dictionary_entry


# Use a type hint to make it clear that it's an integer (: int)

UPDATE_INTERVAL_SECS: int = 1

# Initialize a REACTIVE CALC that our display components can call


@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic. Get random between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now" and use string format strftime() method to format it
    #
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    # Return everything we need
    return latest_dictionary_entry


# Define the Shiny UI Page layout - Page Options

# Call the ui.page_opts() function
# Set title to a string in quotes that will appear at the top
# Set fillable to True to use the whole page width for the UI

ui.page_opts(title="Antarctica Express: Live Data (Basic)", fillable=True)

# Define the Shiny UI Page layout - Sidebar

with ui.sidebar(open="open"):
    ui.h2("Vashti's Antarctic Live Data", class_="text-center")

    ui.p(
        "A demonstration of real-time changes in temperature readings in Antarctica.",
        class_="text-center",
    )

    ui.hr()

    ui.h6("Links:")

    ui.a(
        "GitHub Source",
        href="https://https://github.com/Vashti259/cintel-05-cintel",
        target="_blank",
    )

    ui.a(
        "GitHub App",
        href="https://https://vashti259.github.io/cintel-05-cintel//",
        target="_blank",
    )

    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")

# In Shiny Express, everything not in the sidebar is in the main panel

ui.h2("-18 c")


@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"


ui.p("warmer than usual")
icon_svg("sun")


ui.hr()

ui.h2("Current Date and Time")


@render.text
def display_time():
    """Get the latest reading and return a 04:47:43"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"


with ui.layout_columns():
    with ui.card():
        ui.card_header("Current Temperature (-18 degrees celsius)")

with ui.layout_columns():
    with ui.card():
        ui.card_header("Current Numbers in Motion (-16, -18, -15))")

# Install Shiny Themes Package
from shinyswatch import theme
from shiny.express import render, ui

theme.darkly()

# Create a deque by passing in a list with values
from collections import deque

temp_deque_A = deque([-16, -18, -15])
len(temp_deque_A)
msft_Temperature = deque(maxlen=3)
print(temp_deque_A)

from shiny.express import input, ui

ui.input_date_range("daterange", "Date range", start="2020-01-01")


@render.text
def value():
    return f"{input.daterange()[0]} to {input.daterange()[1]}"
