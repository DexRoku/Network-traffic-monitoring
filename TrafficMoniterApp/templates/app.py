from flask import Flask, render_template
import psutil
import time

app = Flask(__name__)

def get_network_traffic():
    # Get network statistics
    stats = psutil.net_io_counters(pernic=True)

    # Calculate the total bytes sent and received across all interfaces
    total_sent = sum(stat.bytes_sent for stat in stats.values())
    total_recv = sum(stat.bytes_recv for stat in stats.values())

    return total_sent, total_recv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traffic')
def traffic():
    total_sent, total_recv = get_network_traffic()
    return {
        'sent': total_sent,
        'received': total_recv
    }

if __name__ == '__main__':
    app.run(host='192.168.0.38', port=5000)

