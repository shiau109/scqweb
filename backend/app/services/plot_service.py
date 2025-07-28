import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import io


def generate_plot( fig:Figure ):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf
