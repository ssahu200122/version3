import json
import subprocess
import os

# --- CONFIGURATION ---
JSON_FILE = "data.json"  # Ensure this is the correct path to your file
COUNTER_FILE = os.path.join(os.environ["TEMP"], "edge_profile_idx.txt")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# ---------------------

def launch_cycle():
    # 1. Load the JSON data
    if not os.path.exists(JSON_FILE):
        print(f"Error: {JSON_FILE} not found.")
        return

    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    
    # Get list of account names (the keys in your JSON)
    accounts = list(data.keys())
    total_accounts = len(accounts)

    # 2. Get the current index
    idx = 0
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            try:
                idx = int(f.read().strip())
            except ValueError:
                idx = 0

    # Safety check if JSON changed and index is now out of bounds
    if idx >= total_accounts:
        idx = 0

    # 3. Extract the profile command
    # This takes "--profile-directory=Default" from your JSON
    profile_arg = data[accounts[idx]]["cmd"]
    
    print(f"Opening profile for: {accounts[idx]}")

    # 4. Launch Edge
    # We pass the argument exactly as it appears in your 'cmd' field
    subprocess.Popen([EDGE_PATH, profile_arg])

    # 5. Save next index
    next_idx = (idx + 1) % total_accounts
    with open(COUNTER_FILE, "w") as f:
        f.write(str(next_idx))

if __name__ == "__main__":
    launch_cycle()