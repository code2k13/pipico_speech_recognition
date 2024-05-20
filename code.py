import board
import time
import analogio
import digitalio
import ulab
import gc
from yes_model_min import predict
from no_model_min import predict

button = digitalio.DigitalInOut(board.GP21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

led_system = digitalio.DigitalInOut(board.GP19)
led_system.direction = digitalio.Direction.OUTPUT

led_detect = digitalio.DigitalInOut(board.GP18)
led_detect.direction = digitalio.Direction.OUTPUT

#system is ready
for i in range(0,4):
    led_system.value = True
    time.sleep(0.025)
    led_system.value = False
    time.sleep(0.025)

mic = analogio.AnalogIn(board.A1) 

def get_speech_spectrogram():
    n_samples = 8192
    samples = []
    led_system.value = True    
    
    for i in range(n_samples * 14):
        if i % 14 == 0:
            samples.append(100*((mic.value * 3.3 / 65536) - 1.65))

    if len(samples) % 2 != 0:
        samples = samples[1:]

    led_system.value = False
    gc.collect()

    data_array = ulab.numpy.array(samples,dtype=ulab.numpy.float)
    samples = None
    time.sleep(1)
    gc.collect()

    def calculate_spectrogram_segment(segment):
        spectrogram = ulab.utils.spectrogram(segment)
        spectrogram[0] = 0  # set DC component to 0
        return spectrogram

    def average_bins(spectrogram, bin_size):
        num_bins = len(spectrogram) // bin_size
        averaged_bins = [ulab.numpy.mean(spectrogram[i*bin_size:(i+1)*bin_size]) for i in range(num_bins)]
        return averaged_bins

    segment_size = 1024
    bin_size = 32
    result_spectrogram = []

    for start in range(0, len(data_array), segment_size):
        segment = data_array[start:start + segment_size]
        
        if len(segment) == segment_size:
            segment_spectrogram = calculate_spectrogram_segment(segment)
            half_spectrogram = segment_spectrogram[:segment_size // 2]               
            averaged_bins = average_bins(half_spectrogram, bin_size)
            result_spectrogram.extend(averaged_bins)

    data_array = None
    gc.collect()
    result = ulab.numpy.array(result_spectrogram,dtype=ulab.numpy.float)
    result_spectrogram = None
    gc.collect()
    min_val = ulab.numpy.min(result)
    max_val = ulab.numpy.max(result)
    gc.collect()
    normalized_result = (result - min_val) / (max_val - min_val)   

    return normalized_result

def detected():
    for _ in range(3):
        led_detect.value = True  
        time.sleep(0.5) 
        led_detect.value = False 
        time.sleep(0.5)

while True:
    if button.value:  
        time.sleep(1)
        led_system.value = True
        spectrogram = get_speech_spectrogram()
        prediction = predict(ulab.numpy.array(spectrogram))
        print("score:",prediction)
        if prediction[0] > 0.70:
             detected()
        led_system.value = False
        gc.collect()
        time.sleep(1)
        spectrogram = None
        gc.collect()
        time.sleep(1)        
    else:
        led_system.value = False
    time.sleep(0.1)

 