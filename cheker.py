import docker

try:
    # This connects Python to your local Docker app
    client = docker.from_env()
    
    # This asks Docker for a list of all running containers
    containers = client.containers.list()
    
    print("--- Connection Successful! ---")
    print(f"I found {len(containers)} containers running on your system.")
    
except Exception as e:
    print("--- Connection Failed ---")
    print(f"Error: {e}")
    print("Make sure Docker Desktop is open and running!")