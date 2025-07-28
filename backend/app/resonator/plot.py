import matplotlib.pyplot as plt
import io
import numpy as np

def plot_resonator_response(freq, real, imag, mode="magnitude") -> bytes:
    fig, ax = plt.subplots()
    complex_data = real + 1j * imag

    if mode == "magnitude":
        ax.plot(freq, abs(complex_data))
    elif mode == "phase":
        ax.plot(freq, np.angle(complex_data))
    elif mode == "iq":
        ax.plot(real, imag)
    else:
        raise ValueError("Unsupported mode")

    ax.set_title(f"Resonator Response - {mode}")
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return buf.read()
