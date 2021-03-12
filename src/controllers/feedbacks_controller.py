from models.Feedback import Feedback
from models.Project import Project
from main import db
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

feedbacks = Blueprint('feedbacks', __name__, url_prefix='/feedback')


@feedbacks.route('/project/<int:id>', methods=['POST'])
@login_required
def feedback_create(id):
    project = Project.query.filter_by(id=id).first()

    feedback = Feedback.query.filter_by(
        user_id=current_user.id,
        project_id=project.id
    ).first()

    if feedback:
        flash('Already given feedback in this project')
        return redirect(url_for('feedbacks.feedback_show_project', id=id))

    if project.user_id == current_user.id:
        flash('Cannot give feedback on your own project')
        return redirect(url_for('feedbacks.feedback_show_project', id=id))

    new_feedback = Feedback()
    new_feedback.text = request.form.get('text')
    new_feedback.user_id = current_user.id
    new_feedback.project_id = project.id

    db.session.add(new_feedback)
    db.session.commit()

    flash('Thank you for your Feedback')
    # return jsonify(feedback_schema.dump(new_feedback))
    return redirect(url_for('feedbacks.feedback_show_project', id=id))


@feedbacks.route('/<int:id>', methods=['GET'])
def feedback_show(id):
    feedback = Feedback.query.get(id)

    # return jsonify(feedback_schema.dump(feedback))
    return render_template("feedback.html", feedback=feedback)


@feedbacks.route('/project/<int:id>', methods=['GET'])
def feedback_show_project(id):
    feedbacks = Feedback.query.filter_by(project_id=id)
    project = Project.query.get(id)

    # return jsonify(feedbacks_schema.dump(feedback))
    return render_template(
        "feedback_index.html",
        feedbacks=feedbacks,
        project_name=project.name,
        project_id=id
    )


# @feedbacks.route('/<int:id>', methods=['DELETE'])
@feedbacks.route("/delete/<int:id>", methods=["GET"])
@login_required
def feedback_delete(id):
    feedback = Feedback.query.filter_by(id=id, user_id=current_user.id).first()

    if not feedback:
        flash('Unauthorised to delete this feedback')
        return redirect(url_for('feedbacks.feedback_show', id=id))

    project_id = feedback.project_id

    db.session.delete(feedback)
    db.session.commit()

    flash('Feedback Deleted')

    return redirect(url_for('feedbacks.feedback_show_project', id=project_id))


# @feedbacks.route('/<int:id>', methods=['PUT', 'PATCH'])
@feedbacks.route("/update/<int:id>", methods=["POST"])
@login_required
def feedback_update(id):
    feedback = Feedback.query.filter_by(id=id, user_id=current_user.id).first()

    if not feedback:
        flash('Unauthorised to update this feedback')
        return redirect(url_for('feedbacks.feedback_show', id=id))

    feedback.text = request.form.get('text')

    db.session.commit()

    flash('Feedback Updated')

    return redirect(url_for('feedbacks.feedback_show', id=id))


@feedbacks.route("/new/<int:id>", methods=["GET"])
def new_feedback(id):
    return render_template("new_feedback.html", id=id)


@feedbacks.route("/revise/<int:id>", methods=["GET"])
def revise_feedback(id):
    feedback = Feedback.query.get(id)
    return render_template("revise_feedback.html", feedback=feedback)
