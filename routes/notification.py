from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from models import db
from models.notification import Notification

notification_bp = Blueprint(
    "notification",
    __name__
)


@notification_bp.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return render_template(
        "notifications.html",
        notifications=notifications
    )


@notification_bp.route("/notification/read/<int:id>")
@login_required
def read_notification(id):

    notification = Notification.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    notification.is_read = True

    db.session.commit()

    return redirect(
        url_for("notification.notifications")
    )


@notification_bp.route("/notification/delete/<int:id>")
@login_required
def delete_notification(id):

    notification = Notification.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(notification)

    db.session.commit()

    return redirect(
        url_for("notification.notifications")
    )