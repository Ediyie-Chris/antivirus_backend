from flask import Flask, jsonify
from flask_cors import CORS
import psutil


app = Flask(__name__)
CORS(app)

def get_memory_info():
    mem_info = psutil.virtual_memory()
    
    total_memory  = mem_info.total
    available_memory = mem_info.available
    used_memory = mem_info.used
    free_memory = mem_info.free
    
    return {
        "total_memory": total_memory,
        "available_memory": available_memory,
        "used_memory": used_memory,
        "free_memory": free_memory
    }
    
    
@app.route('/memory_info', methods = ['GET'])
def memory_info():
    memory_info = get_memory_info()
    total_gb = memory_info['total_memory'] / (1024 **3)
    available_gb = memory_info['available_memory'] / (1024 ** 3)
    used_gb = memory_info['used_memory'] / (1024 ** 3)
    free_gb  = memory_info['free_memory'] / (1024 ** 3) 
    
    return jsonify({
        "total_memory": '{:.2f} GB'.format(total_gb),
        "available_gb": '{:.2f} GB'.format(available_gb),
        "used_gb": '{:.2f} GB'.format(used_gb),
        "free_gb": '{:.2f} GB'.format(free_gb)
    })
    

if __name__   == "__main__":
    app.run(debug=True, port=8000)
       