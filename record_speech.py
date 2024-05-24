import board
import time
import analogio
import digitalio
import gc

# Define the pin connected to the pushbutton
button_pin = board.GP21

# Create a digital input object for the pushbutton
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN  # Use pull-down resistor

led = digitalio.DigitalInOut(board.GP19)
led.direction = digitalio.Direction.OUTPUT

mic = analogio.AnalogIn(board.A1)


def get_voice_data():
    n_samples = 8000
    samples = []
    led.value = True
    start_time = time.monotonic()
    for i in range(0, n_samples * 14):
        if i % 14 == 0:
            samples.append((mic.value * 3.3 / 65536) - 1.6)
    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    print(f"Number of samples : {len(samples)}")
    print(f"Time taken: {elapsed_time} seconds")
    sampling_rate_khz = len(samples) / (elapsed_time * 1000)
    print(f"Sampling rate : {sampling_rate_khz} kilohertz")
    print(f"Max frequency captured : {sampling_rate_khz/2} kilohertz")

    if len(samples) % 2 != 0:
        samples = samples[1:]

    led.value = False
    gc.collect()
    return samples


while True:
    if button.value:
        time.sleep(1)
        led.value = True
        spectrogram = get_voice_data()
        led.value = False
        gc.collect()
        time.sleep(1)
        for i in spectrogram:
            print(i)
        print("END")
        spectrogram = None
        gc.collect()
        time.sleep(1)
    else:
        led.value = False
    time.sleep(0.1)
