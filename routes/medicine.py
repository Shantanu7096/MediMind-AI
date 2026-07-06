from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from models.reminder import Reminder
from models import db
from models.medicine import Medicine

medicine_bp = Blueprint("medicine", __name__)


# ==========================================
# View All Medicines
# ==========================================
@medicine_bp.route("/medicines")
@login_required
def medicines():
    
    medicine_list = Medicine.query.filter_by(
        user_id=current_user.id
    ).order_by(Medicine.created_at.desc()).all()

    return render_template(
        "medicines.html",
        medicines=medicine_list
    )

@medicine_bp.route("/search_medicine")
@login_required
def search_medicine():

    keyword = request.args.get("q", "")

    medicines = Medicine.query.filter(

        Medicine.user_id == current_user.id,

        Medicine.medicine_name.like(f"%{keyword}%")

    ).all()

    return render_template(

        "medicines.html",

        medicines=medicines,

        keyword=keyword

    )
# ==========================================
# Add Medicine
# ==========================================
@medicine_bp.route("/add_medicine", methods=["POST"])
@login_required
def add_medicine():

    try:

        # Convert Time
        reminder_time = None
        if request.form.get("reminder_time"):
            reminder_time = datetime.strptime(
                request.form["reminder_time"],
                "%H:%M"
            ).time()

        # Convert Start Date
        start_date = None
        if request.form.get("start_date"):
            start_date = datetime.strptime(
                request.form["start_date"],
                "%Y-%m-%d"
            ).date()

        # Convert End Date
        end_date = None
        if request.form.get("end_date"):
            end_date = datetime.strptime(
                request.form["end_date"],
                "%Y-%m-%d"
            ).date()

        medicine = Medicine(

            user_id=current_user.id,

            medicine_name=request.form.get("medicine_name"),

            dosage=request.form.get("dosage"),

            medicine_type=request.form.get("medicine_type"),

            frequency=request.form.get("frequency"),

            food_instruction=request.form.get("food_instruction"),

            reminder_time=reminder_time,

            start_date=start_date,

            end_date=end_date,

            notes=request.form.get("notes"),

            status="Pending"

        )
        # Save medicine
        db.session.add(medicine)
        db.session.commit()

        # Create reminder automatically
        reminder = Reminder(
            medicine_id=medicine.id,
            reminder_time=medicine.reminder_time,
            reminder_date=medicine.start_date,
            status="Pending"
        )

        db.session.add(reminder)
        db.session.commit()
        
        
        flash(
            "Medicine added successfully!",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        flash(
            f"Error: {str(e)}",
            "danger"
        )

    return redirect(url_for("medicine.medicines"))

@medicine_bp.route("/edit_medicine/<int:id>")
@login_required
def edit_medicine(id):

    medicine = Medicine.query.filter_by(

        id=id,

        user_id=current_user.id

    ).first_or_404()

    return render_template(

        "edit_medicine.html",

        medicine=medicine

    )


@medicine_bp.route("/update_medicine/<int:id>", methods=["POST"])
@login_required
def update_medicine(id):

    medicine = Medicine.query.filter_by(

        id=id,

        user_id=current_user.id

    ).first_or_404()

    medicine.medicine_name = request.form["medicine_name"]

    medicine.dosage = request.form["dosage"]

    medicine.medicine_type = request.form["medicine_type"]

    medicine.frequency = request.form["frequency"]

    medicine.food_instruction = request.form["food_instruction"]

    medicine.notes = request.form["notes"]

    db.session.commit()

    flash(

        "Medicine Updated Successfully",

        "success"

    )

    return redirect(url_for("medicine.medicines"))


    
# ==========================================
# Delete Medicine
# ==========================================
@medicine_bp.route("/delete_medicine/<int:id>")
@login_required
def delete_medicine(id):

    medicine = Medicine.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if medicine:

        db.session.delete(medicine)

        db.session.commit()

        flash(
            "Medicine deleted successfully!",
            "success"
        )

    else:

        flash(
            "Medicine not found.",
            "danger"
        )

    return redirect(url_for("medicine.medicines"))


# ==========================================
# Mark Medicine as Taken
# ==========================================
@medicine_bp.route("/mark_taken/<int:id>")
@login_required
def mark_taken(id):

    medicine = Medicine.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if medicine:

        medicine.status = "Taken"

        db.session.commit()

        flash(
            "Medicine marked as Taken.",
            "success"
        )

    else:

        flash(
            "Medicine not found.",
            "danger"
        )

    return redirect(url_for("medicine.medicines"))


# ==========================================
# Mark Medicine as Missed
# ==========================================
@medicine_bp.route("/mark_missed/<int:id>")
@login_required
def mark_missed(id):

    medicine = Medicine.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if medicine:

        medicine.status = "Missed"

        db.session.commit()

        flash(
            "Medicine marked as Missed.",
            "warning"
        )

    else:

        flash(
            "Medicine not found.",
            "danger"
        )

    return redirect(url_for("medicine.medicines"))