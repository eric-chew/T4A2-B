from models.Feedback import Feedback
from models.Project import Project
from models.User import User
from main import db
from schemas.FeedbackSchema import feedback_schema, feedbacks_schema
from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
from flask_login import login_required, current_user

feedbacks = Blueprint('feedbacks', __name__, url_prefix='/feedback')

@feedbacks.route('/', methods=['POST'])
@login_required
def feedback_create():
    project = Project.query.filter_by(user_id=current_user.id).first()
    
    if not project:
        return abort(400, description="Can't give feedback without a project!")
    
    new_feedback = Feedback()
    new_feedback.text = request.form.get("text")
    new_feedback.user_id = current_user.id
    new_feedback.project_id = project.id

    db.session.add(new_feedback)
    db.session.commit()
    
    return jsonify(feedback_schema.dump(new_feedback))

@feedbacks.route('/<int:id>', methods=['GET'])
def feedback_show(id):
    feedback = Feedback.query.get(id)
    
    return jsonify(feedback_schema.dump(feedback))

@feedbacks.route('/<int:id>', methods=['DELETE'])
def feedback_delete(id):
    feedback = Feedback.query.get(id)
    
    project = Project.query.filter_by(id=feedback.project_id, user_id=current_user.id).first()
    
    if not project:
        return abort(400, description='Unauthorised to delete this feedback')
    
    db.session.delete(feedback)
    db.session.commit()
    
    return jsonify(feedback_schema.dump(feedback))

@feedbacks.route('/<int:id>', methods=['PUT', 'PATCH'])
@login_required
def feedback_update(id):
    feedback = Feedback.query.get(id)
    
    project = Project.query.filter_by(id=feedback.project_id, user_id=current_user.id).first()
    
    if not project:
        return abort(400, description='Unauthorised to update this feedback')
    
    feedback.text = request.form.get('text')
    feedback.project_id = project.id
    feedback.user_id = current_user.id
    
    db.session.commit()
    
    return jsonify(feedback_schema.dump(feedback))