from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from datetime import date

from models import db
from models.bmi import BMI

bmi_bp = Blueprint(
    "bmi",
    __name__
)


@bmi_bp.route("/bmi")
@login_required
def bmi():

    latest = BMI.query.filter_by(
        user_id=current_user.id
    ).order_by(
        BMI.id.desc()
    ).first()

    return render_template(
        "bmi.html",
        bmi=latest
    )


@bmi_bp.route("/save_bmi", methods=["POST"])
@login_required
def save_bmi():

    height = float(request.form["height"])

    weight = float(request.form["weight"])

    bmi_value = round(
        weight / ((height / 100) ** 2),
        2
    )

    if bmi_value < 18.5:
        category = "Underweight"

    elif bmi_value < 25:
        category = "Normal"

    elif bmi_value < 30:
        category = "Overweight"

    else:
        category = "Obese"

    record = BMI(

        user_id=current_user.id,

        height=height,

        weight=weight,

        bmi=bmi_value,

        category=category,

        log_date=date.today()

    )

    db.session.add(record)

    db.session.commit()

    flash(
        "BMI saved successfully.",
        "success"
    )

    return redirect(
        url_for("bmi.bmi")
    )