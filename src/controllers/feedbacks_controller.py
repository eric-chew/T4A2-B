from models.Feedback import Feedback
from models.Project import Project
from main import db
from schemas.FeedbackSchema import feedback_schema
from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
# from flask import Blueprint, request, render_template, abort, redirect, url_for
from flask_login import login_required, current_user

feedbacks = Blueprint('feedbacks', __name__, url_prefix='/feedback')


@feedbacks.route('/project/<int:id>', methods=['POST'])
@login_required
def feedback_create(id):
    project = Project.query.filter_by(id=id).first()

    feedback = Feedback.query.filter_by(user_id=current_user.id).first()

    if feedback:
        return abort(400, description='Already given feedback in this project')

    if project.user_id == current_user.id:
        return abort(400, description='Cannot give feedback on your own project')

    new_feedback = Feedback()
    new_feedback.text = request.form.get('text')
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
@login_required
def feedback_delete(id):
    feedback = Feedback.query.filter_by(id=id, user_id=current_user.id).first()

    if not feedback:
        return abort(400, description='Unauthorised to delete this feedback')

    db.session.delete(feedback)
    db.session.commit()

    return jsonify({'msg': 'Feedback Deleted'})


@feedbacks.route('/<int:id>', methods=['PUT', 'PATCH'])
@login_required
def feedback_update(id):
    feedback = Feedback.query.filter_by(id=id, user_id=current_user.id).first()

    if not feedback:
        return abort(400, description='Unauthorised to update this feedback')

    feedback.text = request.form.get('text')

    db.session.commit()

    return jsonify(feedback_schema.dump(feedback))
