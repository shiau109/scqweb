import numpy as np





class AttenuatorNoise:
    def __init__(self, attenuation, temperature):
        """
        Parameters
        ----------
        A4K : float
            Attenuation factor at the 4 K stage.
        """
        self.attenuation = attenuation
        self.temperature = temperature

    def outputNoise(self, inputNoise):
        # placeholder: e.g. Johnson–Nyquist noise for R=50 Ω
        att = self.attenuation
        temp = self.temperature
        term1 = inputNoise / att
        term2 = (att - 1) / att * temp
        return term1 +term2

    