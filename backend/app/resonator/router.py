
from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel
from resonator.notch import ResonatorModel
from fastapi.responses import Response
import numpy as np
import base64
from typing import List

router = APIRouter(prefix="/resonator")

from app.resonator.upload import upload_resonator_file
router.post("/upload")(upload_resonator_file)

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

@router.post("/plot_mag")
async def plot_response_mag(
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
    buf = generate_plot( model.plot_response(frequency,"magnitude") )
    return Response(content=buf.getvalue(), media_type="image/png")

@router.post("/plot_phase")
async def plot_response_phase(
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
    buf = generate_plot( model.plot_response(frequency,"phase") )
    return Response(content=buf.getvalue(), media_type="image/png")

@router.post("/plot_iq")
async def plot_response_iq(
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
    buf = generate_plot( model.plot_response(frequency,"iq") )
    return Response(content=buf.getvalue(), media_type="image/png")

@router.post("/compute")
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
    response = model.frequency_response()
    return {"response": response.real}

@router.post("/plot_all")
async def plot_all(
    alpha: float   = Form(...),
    delay: float   = Form(...),
    Ql:    float   = Form(...),
    Qc:    float   = Form(...),
    phi:   float   = Form(...),
    fr:    float   = Form(...),
    freq_start: float = Form(...),
    freq_end:   float = Form(...),
    freq_points: int   = Form(...)
):
    frequency = np.linspace(freq_start, freq_end, freq_points)
    model = ResonatorModel(fr, Ql, Qc, phi, delay, alpha)

    out = {}
    for mode in ("magnitude", "phase", "iq"):
        buf = generate_plot(model.plot_response(frequency, mode))
        out[mode] = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

    return out


from fastapi import Depends
import os
from app.services.user import get_current_user

@router.get("/list")
def list_uploaded_resonator_files(user: str = Depends(get_current_user)):
    folder = os.path.join("uploads", user, "resonator")
    if not os.path.exists(folder):
        return []

    files = [
        {"name": f, "label": "", "selected": False}
        for f in os.listdir(folder)
        # if f.endswith(".csv")
    ]
    return files

class PlotRequest(BaseModel):
    files: list[str]
    labels: list[str]

from .parser import parse_resonator_file
@router.post("/plot_group")
def plot_selected_files(request: PlotRequest, user: str = Depends(get_current_user)):
    import matplotlib.pyplot as plt
    import numpy as np
    import io
    import base64

    fig, ax = plt.subplots()
    for file, label in zip(request.files, request.labels):
        path = os.path.join("uploads", user, "resonator", file)
        data = parse_resonator_file(path)
        freq = data["frequency"]
        real = data["real"]
        imag = data["imag"]
        ax.plot(freq, np.abs(real + 1j * imag), label=label)

    ax.set_title("Combined Resonator Plot")
    ax.legend()

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return Response(content=buf.read(), media_type="image/png")

class RemoveFileRequest(BaseModel):
    filename: str

@router.post("/remove")
def remove_uploaded_file(data: RemoveFileRequest, user: str = Depends(get_current_user)):
    file_path = os.path.join("uploads", user, "resonator", data.filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    try:
        os.remove(file_path)
        return {"status": "deleted", "filename": data.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {e}")