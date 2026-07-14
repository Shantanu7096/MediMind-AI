from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, date

from models import db
from models.sleep import SleepLog

sleep_bp = Blueprint("sleep", __name__)


@sleep_bp.route("/sleep")
@login_required
def sleep():

    today = date.today()

    log = SleepLog.query.filter_by(
        user_id=current_user.id,
        log_date=today
    ).first()

    return render_template(
        "sleep.html",
        log=log
    )


@sleep_bp.route("/save_sleep", methods=["POST"])
@login_required
def save_sleep():

    today = date.today()

    sleep_time = datetime.strptime(
        request.form["sleep_time"],
        "%H:%M"
    )

    wake_time = datetime.strptime(
        request.form["wake_time"],
        "%H:%M"
    )

    # Handle sleeping across midnight
    if wake_time < sleep_time:
        wake_time = wake_time.replace(day=wake_time.day + 1)

    hours = round(
        (wake_time - sleep_time).seconds / 3600,
        2
    )

    if hours >= 8:
        quality = "Excellent"
    elif hours >= 7:
        quality = "Good"
    elif hours >= 6:
        quality = "Average"
    else:
        quality = "Poor"

    log = SleepLog.query.filter_by(
        user_id=current_user.id,
        log_date=today
    ).first()

    if log:

        log.sleep_time = sleep_time.time()
        log.wake_time = wake_time.time()
        log.total_hours = hours
        log.sleep_quality = quality

    else:
        log = SleepLog(

    user_id=current_user.id,

    sleep_time=sleep_time.time(),

    wake_time=wake_time.time(),

    total_hours=hours,

    sleep_quality=quality,

    log_date=today

)

        db.session.add(log)

    db.session.commit()

    flash(
        "Sleep record saved successfully.",
        "success"
    )

    return redirect(
        url_for("sleep.sleep")
    )