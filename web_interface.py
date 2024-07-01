from flask import Flask, jsonify
from scheduler import tasks
from dependency_management import executed_tasks

app = Flask(__name__)


@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify([task.__dict__ for task in tasks])


@app.route('/tasks/<task_id>/status', methods=['GET'])
def task_status(task_id):
    status = "completed" if executed_tasks.get(task_id) else "pending"
    return jsonify({"task_id": task_id, "status": status})


if __name__ == '__main__':
    app.run(port=5000)
