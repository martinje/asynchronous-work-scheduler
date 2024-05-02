import random
import threading
import datetime, time

import uuid
from flask import Flask, request, jsonify

ids = {}

app = Flask(__name__)

def work(id, sleep_time_in_seconds):
    global ids
    ids[id]['status'] = "working"
    now = datetime.datetime.now
    with open("log.txt", "a") as file:
        file.write(f"Id={id} - {now()}: Working...\n")
        time.sleep(sleep_time_in_seconds)
        file.write(f"Id={id} - {now()}: Done working!\n")
    ids[id]['status'] = 'done'

    


@app.route('/api', methods=['POST'])
def create():
    global ids
    # Generate a random guid.
    # The guid will be used to identify the request.
    # This is useful for debugging purposes.
    id = str(uuid.uuid4())

    # random sleept time between 60 and 300 seconds
    sleep_time_in_seconds = random.randint(60, 300)
    
    # calculate exact times from now() and sleep_time_in_seconds
    time_now = datetime.datetime.now()
    time_then = time_now + datetime.timedelta(seconds=sleep_time_in_seconds)


    # add guid to the ids dictionary
    ids[id] = { 'status': 'added', 'estimated_time_completion': time_then.strftime("%Y-%m-%d %H:%M:%S") }


    # Start the work in a new thread, pass in the id
    thread = threading.Thread(target=work, args=(id, sleep_time_in_seconds))
    
    thread.start()


    # Return the id with a 202
    return jsonify({'id': id, 'status_url' : 'http://localhost:5000/api?id=' + id}), 202

@app.route('/api', methods=['GET'])
def status():
    global ids
    
    

    # Get the id from the request
    inbound_id = request.args.get('id')

    id_not_sent = inbound_id is None
    id_not_in_queue = inbound_id not in ids.keys()
    if id_not_sent or id_not_in_queue:
        return jsonify({'message': 'Invalid id!'}), 400
    
    estimated_time_completion = ids[inbound_id]['estimated_time_completion']
    seconds_to_completion = (datetime.datetime.strptime(estimated_time_completion, "%Y-%m-%d %H:%M:%S") - datetime.datetime.now()).total_seconds()

    # Check if job is done.
    if ids[inbound_id]['status'] == "done":
        return jsonify({'message': 'Job is done!'}), 200
    else:
        payload = {
            'message': 'Job is still in progress!', 
            'estimated_time_completion': estimated_time_completion,
            'seconds_to_completion': seconds_to_completion
        }
        return jsonify(payload), 202
        


    



    
    
    


    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run()