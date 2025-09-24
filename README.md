# Patient Insurance Categorizer API

A **FastAPI** based API that categorizes patient insurance data using **Pydantic** models. This project also includes a **Streamlit frontend** for easy interaction and is **deployed on Render** for live usage.

---

## 🚀 Features

- **FastAPI backend** for fast, efficient API endpoints.
- **Pydantic models** for data validation and structured input/output.
- **Streamlit frontend** for an interactive user interface.
- **Deployed on Render** → accessible online without local setup.
- Clean and modular project structure for easy maintenance.

---

## 📦 Project Structure

patient-insurance-api/
│── app_up.py # FastAPI entrypoint
│── config/ # Configuration files
│── model/ # Machine learning / categorization models
│── schema/ # Pydantic schemas for data validation
│── requirements.txt # Python dependencies
│── Dockerfile # Docker container setup
│── README.md
│── LICENSE
└── streamlit_frontend/ # Streamlit frontend files

yaml
Copy code

---

## ⚡ API Endpoints

### Base Endpoint
GET /

css
Copy code
**Response:**
```json
{
  "message": "Hello, Render with Docker!"
}
Health Check
bash
Copy code
GET /health
Response:

json
Copy code
{
  "status": "ok"
}
Insurance Categorizer Endpoint
bash
Copy code
POST /categorize
Request Body Example:

json
Copy code
{
  "patient_name": "John Doe",
  "age": 45,
  "insurance_type": "Private",
  "medical_history": ["diabetes", "hypertension"]
}
Response Example:

json
Copy code
{
  "patient_name": "John Doe",
  "insurance_category": "High Risk"
}
Note: Endpoint structure depends on the model/schema defined in schema/ and model/.

🖥 Streamlit Frontend
You can run the Streamlit app locally:

bash
Copy code
cd streamlit_frontend
streamlit run app.py
The frontend interacts with the deployed FastAPI API to categorize patient insurance data.

🌐 Live Deployment
API URL (Render): https://fast-api-patient-insurance-by-chatak.onrender.com

Streamlit Frontend: Interacts with the deployed API for real-time categorization.

🛠 Installation & Local Setup
Clone the repo:

bash
Copy code
git clone https://github.com/YOUR_USERNAME/Fast_API-patient_insurance.git
cd Fast_API-patient_insurance
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run FastAPI locally:

bash
Copy code
uvicorn app_up:app --reload --host 0.0.0.0 --port 8000
Access API at:
http://localhost:8000

Run Streamlit frontend locally (optional):

bash
Copy code
cd streamlit_frontend
streamlit run app.py
🐳 Docker Deployment
Already configured for Render. Locally, you can test with Docker:

bash
Copy code
docker build -t fastapi-insurance-app .
docker run -p 8000:8000 fastapi-insurance-app
📌 Dependencies
fastapi

pydantic

uvicorn[standard]

streamlit (for frontend)

Any ML libraries you used for categorization (e.g., scikit-learn, pandas, numpy)

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

💡 Notes
Make sure to add any environment variables (e.g., DB URLs or API keys) in .env or Render dashboard.

Streamlit frontend is optional; API works independently.

🙌 Author
Shwetank Maurya

GitHub: https://github.com/Shwetank-Maurya

Deployed API: https://fast-api-patient-insurance-by-chatak.onrender.com

yaml
Copy code

---

If you want, I can also create a **GitHub-ready version with badges** for Python version, Render deployment, and Streamlit that looks more **professional and visually appealing** on your repo.  

Do you want me to do that next?
