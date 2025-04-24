from fastapi import APIRouter, Form
from pydantic import BaseModel
from resonator.notch import ResonatorModel
from fastapi.responses import Response
import numpy as np

router = APIRouter()

class ResonatorInput(BaseModel):
    frequency: float
    fr: float
    Ql: float
    Qc: float
    phi: float
    delay: float
    alpha: float
    a: float

from app.services.plot_service import generate_plot

@router.post("/plot")
async def plot_response(
    alpha: float = Form(...),
    delay: float = Form(...),
    Ql: float = Form(...),
    Qc: float = Form(...),
    phi: float = Form(...),
    fr: float = Form(...),
    freq_start: float = Form(...),
    freq_end: float = Form(...),
    freq_points: int = Form(...)
):
    frequency = np.linspace(freq_start, freq_end, freq_points)
    model = ResonatorModel(fr, Ql, Qc, phi, delay, alpha)
    response = model.compute_response(frequency)
    buf = generate_plot(frequency, response)
    return Response(content=buf.getvalue(), media_type="image/png")

@router.post("/resonator/compute")
def calculate_resonator_response(input_data: ResonatorInput):
    model = ResonatorModel(
        frequency=1e9,
        # fr=input_data.fr,
        # Ql=input_data.Ql,
        # Qc=input_data.Qc,
        # phi=input_data.phi,
        # delay=input_data.delay,
        # alpha=input_data.alpha,
        # a=input_data.a
    )
    response = model.compute_response()
    return {"response": response.real}
