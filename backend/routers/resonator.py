from fastapi import APIRouter
from pydantic import BaseModel
from resonator.calculator import ResonatorModel

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

@router.post("/resonator/compute")
def calculate_resonator_response(input_data: ResonatorInput):
    model = ResonatorModel(
        frequency=input_data.frequency,
        fr=input_data.fr,
        Ql=input_data.Ql,
        Qc=input_data.Qc,
        phi=input_data.phi,
        delay=input_data.delay,
        alpha=input_data.alpha,
        a=input_data.a
    )
    response = model.compute_response()
    return {"response": response}
