# Automated-Container-Lifecycle-Manager-Observability-Suite

# Aegis: High-Availability Microservice Orchestrator & Control Plane

Aegis is a custom-built, self-healing orchestration engine designed to maintain the "Desired State" of a containerized microservice cluster. It mimics the core logic of Kubernetes by implementing a **Reconciliation Loop**—continuously monitoring service health and automatically recovering from infrastructure failures.



## 🚀 Features
- **State Reconciliation:** Automatically detects when a container crashes or stops and spawns a replacement within 5 seconds.
- **Horizontal Scaling:** Manages multiple replicas of a service using Docker Labels for identification.
- **Health-Check Pattern:** Uses an application-level heartbeat (`/health` endpoint) rather than just checking if a process is running.
- **Observability Dashboard:** A real-time web interface to monitor the lifecycle and status of managed replicas.
- **Automated Lifecycle Management:** Handles the build, deployment, and cleanup of ephemeral container instances.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Infrastructure:** Docker SDK for Python
- **Monitoring/Web:** Flask (for Dashboard and Heartbeats)
- **Containerization:** Docker & Docker Desktop

## 🏗️ Architecture
Aegis operates on a **Controller Pattern**:
1. **Observer:** Polls the Docker Socket to get the "Actual State" of the system.
2. **Diff:** Compares the Actual State against the "Desired State" (e.g., 3 replicas).
3. **Actuator:** Executes Docker commands to start or kill containers to reach equilibrium.



## 🚦 Getting Started

### Prerequisites
- Docker Desktop installed and running.
- Python 3.x installed.
- **Important:** Enable "Expose daemon on tcp://localhost:2375" in Docker Desktop settings.

### Installation
1. Clone the repository:
   ```bash
   git clone [ https://github.com/DipuYadav5253/Automated-Container-Lifecycle-Manager-Observability-Suite.git]([https://github.com/yourusername/aegis-orchestrator.git](https://github.com/DipuYadav5253/Automated-Container-Lifecycle-Manager-Observability-Suite).git)
   cd aegis-orchestrator


Install dependencies:

Bash
pip install docker flask requests
Running the System
Build the Worker Image:

Bash
docker build -t my-worker .
Start the Orchestrator (The Brain):

Bash
python brain.py
Launch the Dashboard:

Bash
python dashboard.py
Access the UI: Open http://localhost:8080 in your browser.

🧪 Testing Self-Healing
To witness the self-healing capability, kill a running container manually:

Bash
docker stop <container_name>
Observe the Brain logs or the Dashboard; Aegis will detect the failure and spin up a new instance automatically to maintain the replica count.

📝 Future Improvements
[ ] Resource-Based Scaling: Scale replicas based on CPU/RAM usage.

[ ] Rolling Updates: Update images without downtime by replacing containers one by one.

[ ] Load Balancing: Add an Nginx layer to distribute traffic across active replicas.

Developed as a Master-Level Infrastructure Project for Software Engineering Portfolio.   
