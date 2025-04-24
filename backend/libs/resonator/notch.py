import numpy as np

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

    def compute_response(self, frequency):
        """
        Compute the resonator response based on the initialized parameters.
        """
        term_env = self.a *np.exp(-1j * (2*np.pi * frequency * self.delay -self.alpha) )
        term_resonator = 1.0 - (self.Ql / self.Qc) * np.exp(1j * self.phi) / (1.0 + 2j * self.Ql * (frequency - self.fr) / self.fr)
        return term_env * term_resonator
