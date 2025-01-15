from fastapi.testclient import TestClient
from app.main import app

# Inicializa el cliente de prueba de FastAPI
client = TestClient(app)

def test_healthcheck():
    # Realiza una solicitud GET al endpoint de healthcheck
    response = client.get("/healthcheck")
    # Valida el código de estado
    assert response.status_code == 200
    # Valida la respuesta JSON
    assert response.json() == {"status": "ok"}
