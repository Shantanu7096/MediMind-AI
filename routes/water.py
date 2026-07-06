from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from datetime import date

from models import db
from models.water import WaterLog

water_bp = Blueprint(
    "water",
    __name__
)


@water_bp.route("/water")
@login_required
def water():

    today = date.today()

    log = WaterLog.query.filter_by(
        user_id=current_user.id,
        log_date=today
    ).first()

    if not log:

        log = WaterLog(
            user_id=current_user.id,
            glasses=0,
            goal=8,
            log_date=today
        )

        db.session.add(log)
        db.session.commit()

    return render_template(
        "water.html",
        log=log
    )


@water_bp.route("/add_water")
@login_required
def add_water():

    today = date.today()

    log = WaterLog.query.filter_by(
        user_id=current_user.id,
        log_date=today
    ).first()

    if log.glasses < log.goal:

        log.glasses += 1

        db.session.commit()

    flash(
        "Water intake updated.",
        "success"
    )

    return redirect(
        url_for("water.water")
    )