import matplotlib.pyplot as plt
import numpy as np
import io

def generate_plot(frequency, response):
    plt.figure()
    plt.plot(frequency, np.abs(response))
    plt.xlabel("Frequency")
    plt.ylabel("Response Magnitude")
    plt.title("Resonator Response")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf
