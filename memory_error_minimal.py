import time
import wifi
import ssl
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT
from secrets import secrets
import neopixel
import board


def aio_message_callback(client, feed_id, payload):
    pass
    print(f"{feed_id} = {payload}")

wifi.radio.connect(secrets["ssid"], secrets["password"])
print('Wifi Connected')

pool = socketpool.SocketPool(wifi.radio)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)
pixel.brightness = 0.1

RED      = 0xff0000
GREEN    = 0x00ff00
BLUE     = 0x0000ff
pixel[0] = BLUE


# Initialize a new MQTT Client object
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    username=secrets["aio_username"],
    password=secrets["aio_key"],
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

io = IO_MQTT(mqtt_client)
io.on_message = aio_message_callback

# Connect to Adafruit IO
io.connect()
print("Connected to Adafruit IO")

io.subscribe_to_time("seconds")

timer = 0
pixel[0] = GREEN

while True:

    if (time.monotonic() - timer) >= 0.3:
        timer = time.monotonic()
        # io.loop(timeout=0.2)

        try:
            io.loop(timeout=0.01)
        except MemoryError as e:
            pixel[0] = RED
        except Exception as e:
            print(e)

        
