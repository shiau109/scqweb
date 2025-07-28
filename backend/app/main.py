from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust if your frontend runs on a different origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from .routers import wiring
from .resonator.router import router as resonator_router
app.include_router(resonator_router)

app.include_router(wiring.router, prefix="/wiring")



