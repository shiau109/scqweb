import numpy as np
import matplotlib.pyplot as plt

class ResonatorModel:
    def __init__(self, fr=1e9, Ql=5e3, Qc=10e3, phi=0, delay=0, alpha=0, a=1):
        """
        Initialize the resonator model with given parameters.
        """
        self.fr = fr
        self.Ql = Ql
        self.Qc = Qc
        self.phi = phi
        self.delay = delay
        self.alpha = alpha
        self.a = a

    def frequency_response(self, frequency):
        """
        Compute the resonator response based on the initialized parameters.
        """
        term_env = self.a *np.exp(-1j * (2*np.pi * frequency * self.delay -self.alpha) )
        term_resonator = 1.0 - (self.Ql / self.Qc) * np.exp(1j * self.phi) / (1.0 + 2j * self.Ql * (frequency - self.fr) / self.fr)
        return term_env * term_resonator
    
    def plot_response(self, frequency, kind='magnitude'):
        """
        Generate a matplotlib figure of the resonator response.

        Parameters:
            frequency (array-like): Frequencies at which to evaluate the response.
            kind (str): 'magnitude' or 'phase' or 'iq' to plot the amplitude or phase response.

        Returns:
            matplotlib.figure.Figure: The generated figure object.
        """
        # Compute the complex response
        response = self.frequency_response(frequency)

        # Create a matplotlib figure and axis
        fig, ax = plt.subplots()

        # Plot magnitude or phase
        match kind:
            case 'magnitude':
                self._plot_magnitude(ax, frequency, response)
            case 'phase': 
                self._plot_phase(ax, frequency, response)
            case 'iq':
                self._plot_iq(ax, response)
            case _:
                raise ValueError("Invalid plot type. Choose 'magnitude', 'phase', or 'iq'.")

        return fig
    def _plot_magnitude(self, ax, frequency, response):
        """
        Plot the magnitude of the resonator response.
        """
        ax.plot(frequency, np.abs(response), label='Magnitude')
        ax.set_ylabel('Magnitude')
        ax.set_xlabel('Frequency (Hz)')
        ax.legend()

    def _plot_phase(self, ax, frequency, response):
        """
        Plot the phase of the resonator response.
        """
        ax.plot(frequency, np.angle(response), label='Phase (rad)')
        ax.set_ylabel('Phase (rad)')
        ax.set_xlabel('Frequency (Hz)')
        ax.legend()

    def _plot_iq(self, ax, response):
        """
        Plot the I/Q components of the resonator response.
        """
        ax.plot(np.real(response), np.imag(response), label='I/Q')
        ax.set_xlabel('I')
        ax.set_ylabel('Q')
        ax.legend()
        ax.set_aspect('equal', 'box')