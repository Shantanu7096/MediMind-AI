from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.medicine import Medicine
from ai.medicine_ai import MedicineAI

medicine_ai_bp = Blueprint(
    "medicine_ai",
    __name__
)


@medicine_ai_bp.route("/medicine_info/<int:id>")
@login_required
def medicine_info(id):

    medicine = Medicine.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    ai_response = MedicineAI.explain_medicine(

        medicine_name=medicine.medicine_name,

        dosage=medicine.dosage,

        food_instruction=medicine.food_instruction

    )

    return render_template(

        "medicine_info.html",

        medicine=medicine,

        ai_response=ai_response

    )