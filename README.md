# 🛍️ Decoupled E2E RFM Customer Segmentation System

An enterprise-ready, productionized Machine Learning system that automates **Recency, Frequency, and Monetary (RFM)** customer segmentation. The project transitions an experimental Jupyter Notebook workflow into a highly professional, containerized microservice architecture using a decoupled frontend UI and a high-performance machine learning API gateway.

---

## 🏗️ System Architecture & Responsibility Separation

This project abandons the junior pattern of monolithic scripting. Instead, it isolates responsibilities cleanly into independent layers communicating over a private virtual network.

```text
e2e-rfm-analysis/
├── backend/                  # Layer 1: Core ML Engine & API Gateway
│   ├── app/
│   │   ├── config.py         # System settings & environment parsing
│   │   ├── schemas.py        # Pydantic rigorous data contracts
│   │   └── main.py           # FastAPI runtime and lifespan asset control
│   ├── models/               # Serialized ML weights, scalars, and models
│   └── Dockerfile            # Optimized minimal Debian-Linux compilation
│
├── frontend/                 # Layer 2: Dumb Client Presentation Layer
│   ├── app.py                # Streamlit interface UI (Zero ML knowledge)
│   └── Dockerfile            # Isolated presentation environment
│
└── docker-compose.yml        # Layer 3: Infrastructure orchestration & private network
```

### Key Architectural Standards Implemented:

* **Strict Data Contracts:** Implemented runtime data type validation using **Pydantic** schemas (`schemas.py`) ensuring no structurally corrupted or malformed data payload ever hits the machine learning pipeline.
* **Optimized Lifespan Management:** Machine Learning models (`KMeans`) and preprocessing transforms (`StandardScaler`) are pre-loaded directly into system RAM **once** at server initialization using FastAPI's asynchronous `lifespan` manager, preventing heavy disk-I/O bottlenecks during user prediction loops.
* **Dumb UI Pattern:** The Streamlit frontend functions as a completely lightweight layout manager. It contains zero knowledge of `scikit-learn`, `pandas`, or the mathematical weight files—communicating entirely via JSON network transfers to the backend.

---

## 🛠️ Technology Stack

* **Core Logic & Modeling:** Python 3.11, Scikit-Learn
* **Asynchronous Backend API:** FastAPI, Uvicorn, Pydantic
* **Interactive Frontend UI:** Streamlit, Requests
* **Infrastructure & Portability:** Docker, Docker Compose

---

## 🚀 Getting Started (Local Production Execution)

The entire production ecosystem is completely containerized. You do not need Python, scikit-learn, or Streamlit installed locally on your host machine to run this project—only **Docker Desktop**.

### Prerequisites

* Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed, open, and running on your machine.

### Execution Blueprint

1. **Clone this repository** and navigate to the project root directory:
```bash
cd "D:\E2E Projects\E2E RFM Analysis"

```


2. **Compile and Launch the Ecosystem:**
Execute the single orchestration command to build the optimized multi-stage images, allocate the shared virtual bridge network, and spin up the microservices:
```bash
docker compose up --build

```


3. **Access the Applications:**
* **Interactive User Interface (Frontend):** Open your browser and navigate to `http://localhost:8501` to view and interact with the analytical dashboard.
* **Interactive API Documentation (Backend Gateway):** Navigate to `http://localhost:8000/docs` to inspect the automatically generated Swagger UI and test raw endpoint validation.



---

## ⚙️ Microservice Lifecycle Management

Manage the container workloads safely from your command line using the following operational infrastructure commands:

* **Pause System Execution:** Freeze running containers instantly in RAM without terminating states or reloading files:
```bash
docker compose pause

```


* **Resume System Execution:** Instantly unfreeze the cluster:
```bash
docker compose unpause

```


* **Graceful Stopping:** Halt container processes cleanly, releasing memory while retaining compiled images on disk for instantaneous restarts:
```bash
docker compose stop

```


* **Full Infrastructure Destruction:** Safely terminate execution, delete virtual microservice containers, and tear down the isolated internal bridge network to leave a clean machine environment:
```bash
docker compose down

```



---

## 💡 Engineering Insights & Takeaways

Transitioning this analytical tool into a containerized application provided critical insights into real-world software engineering practices for data science:

1. **The Myth of "Works on My Machine":** Wrapping applications inside explicit `Dockerfiles` guarantees absolute runtime parity between local testing and remote cloud platforms (AWS, GCP, Azure), eliminating version variance hazards.
2. **Microservice Scalability:** Decoupling the frontend from the API backend allows them to scale independently. In a heavy traffic production environment, the computational `backend-api` service could be scaled to multiple replicas behind a load balancer without touching or duplicating the presentation layer.