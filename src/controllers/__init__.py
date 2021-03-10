from controllers.projects_controller import projects
from controllers.feedbacks_controller import feedbacks
from controllers.auth_controller import auth

registerable_controllers = [
    auth,
    projects,
    feedbacks
]