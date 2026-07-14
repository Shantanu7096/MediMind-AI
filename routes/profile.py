from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db

profile_bp = Blueprint("profile", __name__)


# ==========================================
# Profile Page
# ==========================================
@profile_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "profile.html",
        user=current_user
    )


# ==========================================
# Update Profile
# ==========================================
@profile_bp.route("/update_profile", methods=["POST"])
@login_required
def update_profile():

    try:

        current_user.fullname = request.form.get(
            "fullname",
            current_user.fullname
        )

        current_user.email = request.form.get(
            "email",
            current_user.email
        )

        current_user.phone = request.form.get(
            "phone",
            current_user.phone
        )

        age = request.form.get("age")
        current_user.age = int(age) if age else None

        current_user.gender = request.form.get(
            "gender",
            current_user.gender
        )

        current_user.blood_group = request.form.get(
            "blood_group",
            current_user.blood_group
        )

        height = request.form.get("height")
        current_user.height = float(height) if height else None

        weight = request.form.get("weight")
        current_user.weight = float(weight) if weight else None

        current_user.allergies = request.form.get(
            "allergies",
            current_user.allergies
        )

        current_user.chronic_diseases = request.form.get(
            "chronic_diseases",
            current_user.chronic_diseases
        )

        current_user.emergency_contact = request.form.get(
            "emergency_contact",
            current_user.emergency_contact
        )

        db.session.commit()

        flash(
            "Profile updated successfully!",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error: {str(e)}",
            "danger"
        )

    return redirect(
        url_for("profile.profile")
    )