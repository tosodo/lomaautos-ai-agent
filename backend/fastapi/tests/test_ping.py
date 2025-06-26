from fastapi.testclient import TestClient
from main import app  # <-- adjust this if the file is named something else

client = TestClient(app)
