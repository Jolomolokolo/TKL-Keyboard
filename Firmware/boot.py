import board
import digitalio
import storage
import usb_cdc
import usb_hid

# Use the BOOT button to enable CIRCUITPY access (e.g. for development)
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

# If BOOT is *not pressed*, disable CIRCUITPY storage
if button.value:
    storage.disable_usb_drive()

# Enable serial console and USB HID (keyboard, optionally mouse/media)
usb_cdc.enable(console=True, data=True)

usb_hid.enable(
    devices=[
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.MOUSE,  # optional
        # usb_hid.Device.CONSUMER_CONTROL,  # optional for media keys
    ]
)
