from flask import Flask, request
app = Flask(__name__)
led_state = "OFF"
@app.route('/led', methods=['GET'])
def get_led_state():
    return led_state

@app.route('/led', methods=['POST'])
def set_led_state():
    global led_state
    data = request.json
    if 'state' in data and data['state'] in ['ON', 'OFF']:
        led_state = data['state']
        return {'status': 'success', 'state': led_state}, 200
    else:
        return {'status': 'error', 'message': 'Invalid state'}, 400
    
if __name__ == '__main__':
    app.run(host='',port=5000)