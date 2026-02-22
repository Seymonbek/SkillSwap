from flask import Blueprint, request, jsonify

# Initialize Blueprint
jobs_bp = Blueprint('jobs', __name__)

jobs = []  # In-memory storage for jobs

@jobs_bp.route('/jobs', methods=['POST'])
def create_job():
    job_data = request.json
    jobs.append(job_data)
    return jsonify(job_data), 201

@jobs_bp.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

@jobs_bp.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    if job_id < len(jobs):
        return jsonify(jobs[job_id])
    return jsonify({'error': 'Job not found'}), 404

@jobs_bp.route('/jobs/<int:job_id>/milestone', methods=['PATCH'])
def update_job_milestone(job_id):
    if job_id < len(jobs):
        milestone_data = request.json
        jobs[job_id]['milestone'] = milestone_data['milestone']
        return jsonify(jobs[job_id]), 200
    return jsonify({'error': 'Job not found'}), 404

