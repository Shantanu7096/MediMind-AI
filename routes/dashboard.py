from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.reminder import Reminder
from datetime import date
from models.medicine import Medicine

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    medicines = Medicine.query.filter_by(
        user_id=current_user.id
    ).order_by(Medicine.created_at.desc()).all()

    medicine_count = len(medicines)

    taken_count = Medicine.query.filter_by(
        user_id=current_user.id,
        status="Taken"
    ).count()

    pending_count = Medicine.query.filter_by(
        user_id=current_user.id,
        status="Pending"
    ).count()

    missed_count = Medicine.query.filter_by(
        user_id=current_user.id,
        status="Missed"
    ).count()

    # Health Score
    if medicine_count > 0:
        health_score = round((taken_count / medicine_count) * 100)
    else:
        health_score = 0

    today = date.today()

    today_reminders = Reminder.query.join(
        Medicine
    ).filter(
        Medicine.user_id == current_user.id,
        Reminder.reminder_date == today
    ).order_by(
        Reminder.reminder_time
    ).all()
    
    return render_template(
        "dashboard.html",
        user=current_user,
        medicines=medicines,
        medicine_count=medicine_count,
        taken_count=taken_count,
        pending_count=pending_count,
        missed_count=missed_count,
        health_score=health_score,
        today_reminders=today_reminders
    )