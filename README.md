# 🏥 Patient Insurance Categorizer API

A **FastAPI**-based REST API that categorizes patient insurance data using **Pydantic** models for structured validation. Includes a **Streamlit** frontend for easy interaction and is **deployed on Render** for live usage.

---

## 🚀 Features

- ⚡ **FastAPI backend** for fast, efficient API endpoints
- ✅ **Pydantic models** for data validation and structured input/output
- 🖥️ **Streamlit frontend** for an interactive user interface
- 🌐 **Deployed on Render** → accessible online without local setup
- 🐳 **Dockerized** for consistent deployment across environments
- 🗂️ **Clean and modular project structure** for easy maintenance

---

## 🏗️ Architecture

```
User Input (Streamlit UI)
        ↓
FastAPI Backend (app_up.py)
        ↓
Pydantic Validation (schema/)
        ↓
Categorization Logic (model/)
        ↓
JSON Response → Streamlit Display
```

---

## 📂 Project Structure

```
Fast_API-patient_insurance/
├── __pycache__/            # Python cache
├── config/                 # Configuration files
├── model/                  # Categorization logic
├── schema/                 # Pydantic data models
├── app_up.py               # FastAPI main application
├── frontend.py             # Streamlit frontend
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Backend     | FastAPI           |
| Validation  | Pydantic          |
| Frontend    | Streamlit         |
| Deployment  | Render            |
| Container   | Docker            |
| Language    | Python 3.8+       |

---

## 📋 Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shwetank-Maurya/Fast_API-patient_insurance-.git
cd Fast_API-patient_insurance-
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Backend

```bash
uvicorn app_up:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`

Interactive docs at: `http://localhost:8000/docs`

### 4. Run the Streamlit Frontend

```bash
streamlit run frontend.py
```

Frontend will be available at: `http://localhost:8501`

---

## 🐳 Docker Deployment

```bash
# Build the Docker image
docker build -t patient-insurance-api .

# Run the container
docker run -p 8000:8000 patient-insurance-api
```

---

## 🌐 Live Demo

The application is deployed on **Render** and accessible online without any local setup.

---

## 📡 API Endpoints

| Method | Endpoint       | Description                         |
|--------|----------------|-------------------------------------|
| GET    | `/`            | Health check                        |
| POST   | `/categorize`  | Categorize patient insurance data   |
| GET    | `/docs`        | Interactive Swagger UI              |
| GET    | `/redoc`       | ReDoc API documentation             |


---

## 🔧 Configuration

Edit files in the `config/` directory to customize:
- Categorization thresholds
- Insurance plan mappings
- Risk level criteria

---

## 👨‍💻 Author

**Shwetank Maurya**

- GitHub: [@Shwetank-Maurya](https://github.com/Shwetank-Maurya)
- Email: sd3564086@gmail.com

---

## 📄 License

This project is licensed under the Unlicense - see the [LICENSE](LICENSE) file for details.
