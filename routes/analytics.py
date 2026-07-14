from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.medicine import Medicine
from models.water import WaterLog
from models.sleep import SleepLog
from models.bmi import BMI

analytics_bp = Blueprint(
    "analytics",
    __name__
)


@analytics_bp.route("/analytics")
@login_required
def analytics():

    # =====================================================
    # Medicines
    # =====================================================

    medicines = Medicine.query.filter_by(
        user_id=current_user.id
    ).all()

    total_medicines = len(medicines)

    taken_count = len([
        m for m in medicines
        if m.status == "Taken"
    ])

    pending_count = len([
        m for m in medicines
        if m.status == "Pending"
    ])

    missed_count = len([
        m for m in medicines
        if m.status == "Missed"
    ])

    if total_medicines > 0:

        medicine_score = round(
            (taken_count / total_medicines) * 100
        )

    else:

        medicine_score = 0

    # =====================================================
    # Water
    # =====================================================

    water = WaterLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        WaterLog.id.desc()
    ).first()

    if water:

        water_percent = round(
            (water.glasses / water.goal) * 100
        )

        water_percent = min(
            water_percent,
            100
        )

    else:

        water_percent = 0

    # =====================================================
    # Sleep
    # =====================================================

    sleep = SleepLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        SleepLog.id.desc()
    ).first()

    if sleep:

        sleep_percent = round(
            (sleep.total_hours / 8) * 100
        )

        sleep_percent = min(
            sleep_percent,
            100
        )

    else:

        sleep_percent = 0

    # =====================================================
    # BMI
    # =====================================================

    bmi = BMI.query.filter_by(
        user_id=current_user.id
    ).order_by(
        BMI.id.desc()
    ).first()

    bmi_percent = 0

    if bmi:

        if 18.5 <= bmi.bmi <= 24.9:

            bmi_percent = 100

        elif bmi.bmi < 18.5:

            bmi_percent = 70

        else:

            bmi_percent = 70

    # =====================================================
    # Overall Health Score
    # =====================================================

    health_score = round(

        medicine_score * 0.40 +

        water_percent * 0.20 +

        sleep_percent * 0.20 +

        bmi_percent * 0.20

    )

    # =====================================================
    # Render
    # =====================================================

    return render_template(

        "analytics.html",

        # Main objects
        medicines=medicines,
        water=water,
        sleep=sleep,
        bmi=bmi,

        # Statistics
        total_medicines=total_medicines,
        taken_count=taken_count,
        pending_count=pending_count,
        missed_count=missed_count,

        medicine_score=medicine_score,
        health_score=health_score,

        water_percent=water_percent,
        sleep_percent=sleep_percent,
        bmi_percent=bmi_percent

    )