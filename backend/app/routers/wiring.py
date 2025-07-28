from fastapi import APIRouter, Form
from wiring.attenuator import AttenuatorNoise
from fastapi.responses import Response
import numpy as np
import base64

router = APIRouter()


@router.post("/noise_attenuator_chain")
def noise_attenuator_chain(data: dict):
    input_noise = data["input_temperature"]
    chain = data["attenuator_chain"]
    for attenuator in chain:
        attenuation_dB = attenuator["attenuation"]
        if attenuation_dB < 0:
            raise ValueError("Attenuation must be non-negative")
        attenuation = 10 ** (attenuation_dB / 10) # Convert attenuation from dB to linear scale
        temperature = attenuator["temperature"]
        # Create an instance of AttenuatorNoise
        output_noise = AttenuatorNoise(attenuation, temperature).outputNoise(input_noise)
        input_noise = output_noise
    return {"output_temperature": output_noise}
