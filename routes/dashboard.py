from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.reminder import Reminder
from datetime import date
from models.medicine import Medicine
from models.water import WaterLog
from models.sleep import SleepLog
from models.bmi import BMI
from routes.medicine import medicines

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
    
    water = WaterLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        WaterLog.id.desc()
    ).first()

    sleep = SleepLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        SleepLog.id.desc()
    ).first()

    bmi = BMI.query.filter_by(
        user_id=current_user.id
    ).order_by(
        BMI.id.desc()
    ).first()

    tips = []

    if water:
        if water.glasses < 8:
            tips.append("💧 Drink more water today.")
        else:
            tips.append("✅ Great job meeting your water goal!")

    if sleep:
        if sleep.total_hours < 7:
            tips.append("😴 Try to sleep at least 7–8 hours.")
        else:
            tips.append("✅ Your sleep duration looks good.")

    if bmi:
        if bmi.category != "Normal":
            tips.append(f"⚖️ Your BMI is {bmi.category}. Maintain a healthy lifestyle.")
        else:
            tips.append("❤️ Your BMI is in the normal range.")

    return render_template(
        "dashboard.html",
        user=current_user,
        medicines=medicines,
        medicine_count=medicine_count,
        taken_count=taken_count,
        pending_count=pending_count,
        missed_count=missed_count,
        health_score=health_score,
        today_reminders=today_reminders,
        water=water,
        sleep=sleep,
        bmi=bmi,
        tips=tips
    )