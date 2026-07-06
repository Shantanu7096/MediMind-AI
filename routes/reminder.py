from flask import Blueprint
from flask import render_template

from flask import redirect, url_for, flash
from models import db

from flask_login import login_required
from flask_login import current_user

from models.reminder import Reminder
from models.medicine import Medicine

reminder_bp = Blueprint(
    "reminder",
    __name__
)


@reminder_bp.route("/reminders")
@login_required
def reminders():

    reminder_list = Reminder.query.join(
        Medicine
    ).filter(

        Medicine.user_id == current_user.id

    ).order_by(

        Reminder.reminder_date,
        Reminder.reminder_time

    ).all()

    return render_template(

        "reminders.html",

        reminders=reminder_list

    )
    
@reminder_bp.route("/complete_reminder/<int:id>")
@login_required
def complete_reminder(id):

    reminder = Reminder.query.get_or_404(id)

    reminder.status = "Completed"

    db.session.commit()

    flash(
        "Reminder marked as completed.",
        "success"
    )

    return redirect(url_for("reminder.reminders"))