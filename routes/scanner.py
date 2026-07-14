import os
import json
from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)

from flask_login import (
    login_required,
    current_user
)

from werkzeug.utils import secure_filename

from models import db
from models.medicine import Medicine

from ai.ocr import OCRScanner
from ai.vision import GeminiVision
from ai.medicine_parser import parse_medicine

scanner_bp = Blueprint(
    "scanner",
    __name__
)

UPLOAD_FOLDER = "static/uploads"

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "webp"
}


def allowed_file(filename):

    return (

        "." in filename

        and

        filename.rsplit(".", 1)[1].lower()

        in ALLOWED_EXTENSIONS

    )


def empty_medicine():

    return {

        "medicine_name": "",

        "manufacturer": "",

        "generic_name": "",

        "dosage": "",

        "frequency": "",

        "food_instruction": "",

        "pack_size": "",

        "expiry": "",

        "notes": "",

        "confidence": 0

    }


# =======================================================
# Scanner Home
# =======================================================

@scanner_bp.route("/scanner")
@login_required
def scanner():

    return render_template(

        "scanner.html",

        medicine=empty_medicine(),

        medicines=[],

        image_path=None,

        ocr_text=""

    )


# =======================================================
# Scan Prescription
# =======================================================

@scanner_bp.route(
    "/scan_image",
    methods=["POST"]
)
@login_required
def scan_image():

    medicines = []

    medicine = empty_medicine()

    image_path = None

    ocr_text = ""

    mode = request.form.get(

        "scan_mode",

        "ocr"

    )

    if "image" not in request.files:

        flash(

            "Please upload an image.",

            "danger"

        )

        return redirect(

            url_for(

                "scanner.scanner"

            )

        )

    file = request.files["image"]

    if file.filename == "":

        flash(

            "No image selected.",

            "danger"

        )

        return redirect(

            url_for(

                "scanner.scanner"

            )

        )

    if not allowed_file(

        file.filename

    ):

        flash(

            "Only PNG, JPG, JPEG and WEBP images are supported.",

            "danger"

        )

        return redirect(

            url_for(

                "scanner.scanner"

            )

        )

    os.makedirs(

        UPLOAD_FOLDER,

        exist_ok=True

    )

    filename = secure_filename(

        file.filename

    )

    filepath = os.path.join(

        UPLOAD_FOLDER,

        filename

    )

    file.save(filepath)

    image_path = "/" + filepath.replace(

        "\\",

        "/"

    )

    # ===========================================
    # EASY OCR MODE
    # ===========================================

    if mode == "ocr":

        try:

            ocr_text = OCRScanner.extract_text(

                filepath

            )

            medicine = parse_medicine(

                ocr_text

            )

        except Exception as e:

            flash(

                f"OCR Error : {e}",

                "danger"

            )

            return render_template(

                "scanner.html",

                medicine=empty_medicine(),

                medicines=[],

                image_path=image_path,

                ocr_text=""

            )

    # ===========================================
    # GEMINI VISION MODE
    # ===========================================

    elif mode == "vision":

        try:

            medicines = GeminiVision.extract_prescription(

                filepath

            )

            if len(medicines) > 0:

                medicine = medicines[0]

        except Exception as e:

            flash(

                str(e),

                "danger"

            )

            return render_template(

                "scanner.html",

                medicine=empty_medicine(),

                medicines=[],

                image_path=image_path,

                ocr_text=""

            )

    return render_template(

        "scanner.html",

        medicine=medicine,

        medicines=medicines,

        image_path=image_path,

        ocr_text=ocr_text

    )
# =======================================================
# Save Single Medicine (OCR)
# =======================================================

@scanner_bp.route(
    "/save_scanned_medicine",
    methods=["POST"]
)
@login_required
def save_scanned_medicine():

    try:

        reminder_time = None

        if request.form.get("reminder_time"):

            reminder_time = datetime.strptime(

                request.form["reminder_time"],

                "%H:%M"

            ).time()

        medicine = Medicine(

            user_id=current_user.id,

            medicine_name=request.form.get(
                "medicine_name"
            ),

            dosage=request.form.get(
                "dosage"
            ),

            medicine_type=request.form.get(
                "medicine_type"
            ) or "Tablet",

            frequency=request.form.get(
                "frequency"
            ),

            food_instruction=request.form.get(
                "food_instruction"
            ),

            reminder_time=reminder_time,

            start_date=datetime.today().date(),

            end_date=None,

            notes=request.form.get(
                "notes"
            ),

            status="Pending"

        )

        db.session.add(

            medicine

        )

        db.session.commit()

        flash(

            "Medicine saved successfully.",

            "success"

        )

    except Exception as e:

        db.session.rollback()

        flash(

            f"Database Error : {e}",

            "danger"

        )

    return redirect(

        url_for(

            "medicine.medicines"

        )

    )


# =======================================================
# Save All Medicines (Gemini Vision)
# =======================================================

@scanner_bp.route(
    "/save_all_medicines",
    methods=["POST"]
)
@login_required
def save_all_medicines():

    try:

        medicines = json.loads(

            request.form.get(

                "medicines"

            )

        )

        count = 0

        for med in medicines:

            medicine = Medicine(

                user_id=current_user.id,

                medicine_name=med.get(

                    "medicine_name",

                    ""

                ),

                dosage=med.get(

                    "dosage",

                    ""

                ),

                medicine_type="Tablet",

                frequency=med.get(

                    "frequency",

                    ""

                ),

                food_instruction=med.get(

                    "food_instruction",

                    ""

                ),

                reminder_time=None,

                start_date=datetime.today().date(),

                end_date=None,

                notes=med.get(

                    "notes",

                    ""

                ),

                status="Pending"

            )

            db.session.add(

                medicine

            )

            count += 1

        db.session.commit()

        flash(

            f"{count} medicines saved successfully.",

            "success"

        )

    except Exception as e:

        db.session.rollback()

        flash(

            f"Error : {e}",

            "danger"

        )

    return redirect(

        url_for(

            "medicine.medicines"

        )

    )


# =======================================================
# Delete Uploaded Image
# =======================================================

@scanner_bp.route(
    "/delete_scan",
    methods=["POST"]
)
@login_required
def delete_scan():

    image = request.form.get(

        "image_path"

    )

    try:

        if image:

            path = image.lstrip("/")

            if os.path.exists(path):

                os.remove(path)

    except:

        pass

    flash(

        "Scan deleted.",

        "success"

    )

    return redirect(

        url_for(

            "scanner.scanner"

        )

    )


# =======================================================
# API Endpoint
# =======================================================

@scanner_bp.route(
    "/scan_api",
    methods=["POST"]
)
@login_required
def scan_api():

    if "image" not in request.files:

        return jsonify({

            "success":False,

            "message":"No Image"

        })

    file = request.files["image"]

    if not allowed_file(

        file.filename

    ):

        return jsonify({

            "success":False,

            "message":"Invalid Image"

        })

    os.makedirs(

        UPLOAD_FOLDER,

        exist_ok=True

    )

    filename = secure_filename(

        file.filename

    )

    filepath = os.path.join(

        UPLOAD_FOLDER,

        filename

    )

    file.save(

        filepath

    )

    try:

        medicines = GeminiVision.extract_prescription(

            filepath

        )

        return jsonify({

            "success":True,

            "medicines":medicines

        })

    except Exception as e:

        return jsonify({

            "success":False,

            "message":str(e)

        })


# =======================================================
# Scanner Status
# =======================================================

@scanner_bp.route(
    "/scanner_status"
)
@login_required
def scanner_status():

    return jsonify({

        "status":"Running",

        "version":"3.0",

        "ocr":"EasyOCR",

        "vision":"Gemini Vision",

        "database":"Connected"

    })
    