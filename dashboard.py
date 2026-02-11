from flask import Flask, render_template_string
import docker

app = Flask(__name__)
client = docker.from_env()

# This is a simple HTML template to show our containers
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aegis Orchestrator Dashboard</title>
    <style>
        body { font-family: sans-serif; background: #1a1a1a; color: white; padding: 20px; }
        .container-card { 
            background: #333; border-radius: 8px; padding: 15px; margin-bottom: 10px;
            border-left: 10px solid #4CAF50;
        }
        .status-running { color: #4CAF50; font-weight: bold; }
        .header { border-bottom: 2px solid #555; padding-bottom: 10px; }
    </style>
</head>
<body>
    <h1 class="header">🛡️ Aegis Control Plane</h1>
    <h2>Managed Replicas: {{ count }}</h2>
    {% for c in containers %}
    <div class="container-card">
        <strong>ID:</strong> {{ c.short_id }} | 
        <strong>Name:</strong> {{ c.name }} | 
        <span class="status-running">Status: {{ c.status }}</span>
    </div>
    {% endfor %}
    <script>setTimeout(function(){ location.reload(); }, 3000);</script>
</body>
</html>
"""

@app.route('/')
def index():
    # Only show containers managed by our brain
    workers = client.containers.list(filters={"label": "managed_by=aegis"})
    return render_template_string(HTML_TEMPLATE, containers=workers, count=len(workers))

if __name__ == "__main__":
    print("🖥️ Dashboard running at http://localhost:8080")
    app.run(port=8080)