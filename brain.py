import docker
import time

client = docker.from_env()
IMAGE_NAME = "my-worker"
DESIRED_COUNT = 3  # We want 3 workers running at once!

def get_running_workers():
    """Finds all containers that have our specific label"""
    return client.containers.list(filters={"label": "managed_by=aegis"})

def start_worker(index):
    """Starts a worker with a unique name and label"""
    name = f"worker-replica-{index}-{int(time.time())}"
    print(f"🚀 Spawning replica: {name}")
    
    client.containers.run(
        IMAGE_NAME,
        name=name,
        detach=True,
        labels={"managed_by": "aegis"},
        # We don't map ports to the host here to avoid port conflicts
    )

def reconcile():
    """The master loop that maintains the count"""
    print(f"--- Aegis Orchestrator Active (Target: {DESIRED_COUNT} replicas) ---")
    while True:
        try:
            current_workers = get_running_workers()
            current_count = len(current_workers)
            
            print(f"📊 Status: {current_count}/{DESIRED_COUNT} instances running")

            if current_count < DESIRED_COUNT:
                diff = DESIRED_COUNT - current_count
                print(f"⚠️ Shortage detected! Need {diff} more.")
                for i in range(diff):
                    start_worker(i)
            
            elif current_count > DESIRED_COUNT:
                print("✂️ Too many workers! Scaling down...")
                # Remove the oldest one
                current_workers[0].remove(force=True)

        except Exception as e:
            print(f"❌ Error in control loop: {e}")

        time.sleep(5)

if __name__ == "__main__":
    reconcile()