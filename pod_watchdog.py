"""
Monitors a fake list of pod statuses and simulates an agent loop:
observe -> reason -> act.
This is a real script that could be extended to live `kubectl` output.
"""

# Simulated pod state list (in real use, this would come from `kubectl get pods`)
pod_statuses = [
    {"name": "web-api", "status": "Running"},
    {"name": "auth-service", "status": "CrashLoopBackOff"},
    {"name": "db", "status": "Running"},
]

def observe(pods):
    return [pod for pod in pods if pod["status"] != "Running"]

def reason(pod):
    if pod["status"] == "CrashLoopBackOff":
        return f"Pod {pod['name']} is crashing. Suggest checking logs and image version."
    else:
        return f"Pod {pod['name']} has unknown issue: {pod['status']}."

def act(plan):
    print("ACTION:", plan)

if __name__ == "__main__":
    problematic_pods = observe(pod_statuses)
    if not problematic_pods:
        print("✅ All pods are healthy.")
    else:
        for pod in problematic_pods:
            action = reason(pod)
            act(action)
