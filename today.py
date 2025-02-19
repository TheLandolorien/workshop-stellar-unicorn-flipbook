# Source: https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/stellar_unicorn

import time
import network
import ntptime
import machine

# You will need to create or update the file secrets.py with your network credentials using Thonny
# in order for the example to update using the NTP.

# WIFI_CONFIG.py should contain:
# SSID = ""
# PSK = ""
# COUNTRY = ""

try:
    from WIFI_CONFIG import SSID, PSK
except ImportError:
    print("Create WIFI_CONFIG.py with your WiFi credentials")

graphics = None

WIDTH = 16  # StellarUnicorn.WIDTH
HEIGHT = 16  # StellarUnicorn.HEIGHT

rtc = machine.RTC()

DAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

# Enable the Wireless
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def network_connect(ssid, psk):

    # Number of attempts to make before timeout
    max_wait = 5

    # Sets the Wireless LED pulsing and attempts to connect to your local network.
    print(f"Connecting to {ssid}...")
    wlan.config(pm=0xA11140)  # Turn WiFi power saving off for some slow APs
    wlan.connect(ssid, psk)

    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print("waiting for connection...")
        time.sleep(1)

    # Handle connection error. Switches the Warn LED on.
    if wlan.status() != 3:
        print("Unable to connect. Attempting connection again")


# Function to sync the Pico RTC using NTP
def sync_time():

    try:
        network_connect(SSID, PSK)
    except NameError:
        print("Create WIFI_CONFIG.py with your WiFi credentials")

    if wlan.status() < 0 or wlan.status() >= 3:
        try:
            ntptime.settime()
        except OSError:
            print("Unable to sync with NTP server. Check network and try again.")


def init():
    sync_time()


def draw():
    # Pens
    RED = graphics.create_pen(120, 0, 0)
    WHITE = graphics.create_pen(255, 255, 255)

    current_t = rtc.datetime()

    # Set the pen to Red and clear the screen.
    graphics.set_pen(WHITE)
    graphics.clear()

    # Measures the length of the text to help us with centring later.
    day_length = graphics.measure_text(DAYS[current_t[3]], 1)
    date_length = graphics.measure_text(str(current_t[2]), 1)

    graphics.set_font("bitmap6")
    graphics.set_pen(RED)
    graphics.rectangle(0, 0, WIDTH, 7)
    graphics.set_pen(WHITE)
    graphics.text(DAYS[current_t[3]], (WIDTH // 2) - (day_length // 2), 0, 16, 1)

    graphics.set_pen(RED)
    graphics.set_font("bitmap6")
    graphics.text(str(current_t[2]), (WIDTH // 2) - (date_length // 2) + 1, 8, 16, 1)

    graphics.set_pen(graphics.create_pen(0, 0, 0))
