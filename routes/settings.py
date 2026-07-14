from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from models import db

settings_bp = Blueprint("settings", __name__)


# ==========================================
# Settings Page
# ==========================================
@settings_bp.route("/settings")
@login_required
def settings():

    return render_template(
        "settings.html",
        user=current_user
    )


# ==========================================
# Change Password
# ==========================================
@settings_bp.route("/change_password", methods=["POST"])
@login_required
def change_password():

    current_password = request.form.get("current_password")
    new_password = request.form.get("new_password")
    confirm_password = request.form.get("confirm_password")

    if not check_password_hash(
        current_user.password,
        current_password
    ):

        flash(
            "Current password is incorrect.",
            "danger"
        )

        return redirect(
            url_for("settings.settings")
        )

    if new_password != confirm_password:

        flash(
            "New passwords do not match.",
            "danger"
        )

        return redirect(
            url_for("settings.settings")
        )

    if len(new_password) < 6:

        flash(
            "Password must be at least 6 characters.",
            "warning"
        )

        return redirect(
            url_for("settings.settings")
        )

    current_user.password = generate_password_hash(
        new_password
    )

    db.session.commit()

    flash(
        "Password changed successfully.",
        "success"
    )

    return redirect(
        url_for("settings.settings")
    )


# ==========================================
# Update Notification Settings
# ==========================================
@settings_bp.route("/update_notifications", methods=["POST"])
@login_required
def update_notifications():

    # Future feature
    flash(
        "Notification settings saved.",
        "success"
    )

    return redirect(
        url_for("settings.settings")
    )


# ==========================================
# Delete Account
# ==========================================
@settings_bp.route("/delete_account", methods=["POST"])
@login_required
def delete_account():

    try:

        db.session.delete(current_user)

        db.session.commit()

        flash(
            "Your account has been deleted.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error: {str(e)}",
            "danger"
        )

        return redirect(
            url_for("settings.settings")
        )