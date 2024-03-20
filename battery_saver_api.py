from flask import Flask, request, jsonify
from flask_cors import CORS
import psutil
import subprocess

app = Flask(__name__)
CORS(app)

PROGRAMS_TO_MONITOR = ["firefox", "chrome", "visualstudio"]

def shutdown_program(program_name):
    try:
        subprocess.run(["taskkill", "/F", "/IM", program_name + ".exe"], shell=True)
        return f"Program '{program_name}' has been shut down"
    except Exception as e:
        return f"Failed to shut down program '{program_name}': {e}"
    
    
def check_ram_usage(max_ram_usage):
    memory_usage = psutil.virtual_memory().used
    
    if memory_usage > max_ram_usage:
        shutdown_msgs = [shutdown_program(program) for program in  PROGRAMS_TO_MONITOR]
        return {"status": "success", "message": "Programs shut down successfully"}
    else:
        return {"status": "info", "message": "RAM usage is within the limit"}
    
@app.route('/ram-monitor', methods = ['POST'])
def ram_monitor():
    data = request.json
    max_ram_gb = data.get('max_ram_gb')
    max_ram_usage  = max_ram_gb * 1024 * 1024 * 1024
    return jsonify(check_ram_usage(max_ram_usage))


if __name__ == "__main__":
    app.run(debug=True, port=9900)        