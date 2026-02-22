from flask import Blueprint, request, jsonify
from your_database_module import Skill, db  # Import your database models and db session

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('/skills', methods=['POST'])
def add_skill():
    data = request.json
    new_skill = Skill(name=data['name'], description=data['description'])  # Adjust according to your model
    db.session.add(new_skill)
    db.session.commit()
    return jsonify({'id': new_skill.id, 'name': new_skill.name}), 201

@skills_bp.route('/skills', methods=['GET'])
def get_skills():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    filters = request.args.get('filter', None)

    query = Skill.query
    
    if filters:
        query = query.filter(Skill.name.ilike(f'%{filters}%'))  # Example filter

    skills = query.paginate(page, per_page, error_out=False)
    result = {
        'skills': [{'id': skill.id, 'name': skill.name, 'description': skill.description} for skill in skills.items],
        'total': skills.total,
        'page': skills.page,
        'per_page': skills.per_page
    }

    return jsonify(result)

@skills_bp.route('/skills/<int:id>', methods=['DELETE'])
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': 'Skill deleted successfully'}), 204
