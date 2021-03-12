from models.Project import Project
from main import db
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

projects = Blueprint('projects', __name__, url_prefix='/projects')


@projects.route('/', methods=['GET'])
def project_index():
    projects = Project.query.all()

    # return jsonify(projects_schema.dump(projects))
    return render_template("projects_index.html", projects=projects)


@projects.route('/', methods=['POST'])
@login_required
def project_create():
    name = request.form.get('name')
    link = request.form.get('link')
    description = request.form.get('description')

    new_project = Project()
    new_project.name = name
    new_project.link = link
    new_project.description = description
    new_project.user_id = current_user.id

    db.session.add(new_project)
    db.session.commit()

    flash('Project Created!')
    # return jsonify(project_schema.dump(new_project))
    return redirect(url_for('projects.project_show', id=new_project.id))


@projects.route('/<int:id>', methods=['GET'])
def project_show(id):
    project = Project.query.get(id)

    # return jsonify(project_schema.dump(project))
    return render_template("project.html", project=project)


@projects.route('/my_projects', methods=['GET'])
@login_required
def project_show_user():
    projects = Project.query.filter_by(user_id=current_user.id)

    # return jsonify(projects_schema.dump(projects))
    return render_template("projects_user.html", projects=projects)


# @projects.route('/<int:id>', methods=['DELETE'])
@projects.route("/delete/<int:id>", methods=['GET'])
@login_required
def project_delete(id):
    project = Project.query.filter_by(id=id, user_id=current_user.id).first()

    if not project:
        flash('Unauthorised to delete this project')
        return redirect(url_for('projects.project_show', id=id))

    db.session.delete(project)
    db.session.commit()

    flash('Project Deleted')
    return redirect(url_for('projects.project_show_user'))


# @projects.route('/<int:id>', methods=['PUT', 'PATCH'])
@projects.route("/update/<int:id>", methods=['POST'])
@login_required
def project_update(id):
    project = Project.query.filter_by(id=id, user_id=current_user.id).first()

    if not project:
        flash('Unauthorised to update this project')
        return redirect(url_for('projects.project_show', id=id))

    project.name = request.form.get('name')
    project.link = request.form.get('link')
    project.description = request.form.get('description')

    db.session.commit()

    flash('Project Updated')
    # return jsonify(project_schema.dump(project))
    return redirect(url_for('projects.project_show', id=id))


@projects.route("/new", methods=["GET"])
def new_project():
    return render_template("new_project.html")


@projects.route("/revise/<int:id>", methods=["GET"])
def revise_project(id):
    project = Project.query.get(id)
    return render_template("revise_project.html", project=project)
