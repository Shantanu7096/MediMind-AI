from io import BytesIO

from flask import Blueprint
from flask import send_file

from flask_login import login_required
from flask_login import current_user

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from models.medicine import Medicine
from models.water import WaterLog
from models.sleep import SleepLog
from models.bmi import BMI


report_bp = Blueprint(
    "report",
    __name__
)


@report_bp.route("/download_report")
@login_required
def download_report():

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    elements = []

    # =====================================================
    # Title
    # =====================================================

    elements.append(

        Paragraph(

            "MediMind AI Health Report",

            title_style

        )

    )

    elements.append(

        Spacer(1, 20)

    )

    # =====================================================
    # User Information
    # =====================================================

    elements.append(

        Paragraph(

            "<b>User Information</b>",

            styles["Heading2"]

        )

    )

    user_data = [

        ["Name", current_user.fullname],

        ["Email", current_user.email],

        ["Phone", current_user.phone or "-"],

        ["Age", current_user.age or "-"],

        ["Gender", current_user.gender or "-"],

        ["Blood Group", current_user.blood_group or "-"]

    ]

    user_table = Table(

        user_data,

        colWidths=[120, 320]

    )

    user_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.lightblue),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(

        user_table

    )

    elements.append(

        Spacer(1,20)

    )

    # =====================================================
    # Medicines
    # =====================================================

    medicines = Medicine.query.filter_by(

        user_id=current_user.id

    ).all()

    elements.append(

        Paragraph(

            "<b>Medicine Records</b>",

            styles["Heading2"]

        )

    )

    medicine_data = [

        [

            "Medicine",

            "Dosage",

            "Frequency",

            "Status"

        ]

    ]

    if medicines:

        for med in medicines:

            medicine_data.append([

                med.medicine_name,

                med.dosage,

                med.frequency or "-",

                med.status

            ])

    else:

        medicine_data.append([

            "No Medicines",

            "-",

            "-",

            "-"

        ])

    medicine_table = Table(

        medicine_data,

        colWidths=[150,90,120,80]

    )

    medicine_table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,0),10)

        ])

    )

    elements.append(

        medicine_table

    )

    elements.append(

        Spacer(1,20)

    )

    # =====================================================
    # Water Tracker
    # =====================================================

    water = WaterLog.query.filter_by(

        user_id=current_user.id

    ).order_by(

        WaterLog.id.desc()

    ).first()

    elements.append(

        Paragraph(

            "<b>Water Intake</b>",

            styles["Heading2"]

        )

    )

    if water:

        water_data = [

            ["Today's Glasses", water.glasses],

            ["Daily Goal", water.goal]

        ]

    else:

        water_data = [

            ["Today's Glasses","No Record"],

            ["Daily Goal","No Record"]

        ]

    water_table = Table(

        water_data,

        colWidths=[180,180]

    )

    water_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.lightblue),

            ("BOTTOMPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(

        water_table

    )

    elements.append(

        Spacer(1,20)

    )
    # =====================================================
    # Sleep Tracker
    # =====================================================

    sleep = SleepLog.query.filter_by(

        user_id=current_user.id

    ).order_by(

        SleepLog.id.desc()

    ).first()

    elements.append(

        Paragraph(

            "<b>Sleep Report</b>",

            styles["Heading2"]

        )

    )

    if sleep:

        sleep_data = [

            ["Sleep Duration", f"{sleep.total_hours} Hours"],

            ["Sleep Quality", sleep.sleep_quality]

        ]

    else:

        sleep_data = [

            ["Sleep Duration", "No Record"],

            ["Sleep Quality", "No Record"]

        ]

    sleep_table = Table(

        sleep_data,

        colWidths=[180,180]

    )

    sleep_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.lightgreen),

            ("BOTTOMPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(

        sleep_table

    )

    elements.append(

        Spacer(1,20)

    )

    # =====================================================
    # BMI Report
    # =====================================================

    bmi = BMI.query.filter_by(

        user_id=current_user.id

    ).order_by(

        BMI.id.desc()

    ).first()

    elements.append(

        Paragraph(

            "<b>BMI Report</b>",

            styles["Heading2"]

        )

    )

    if bmi:

        bmi_data = [

            ["BMI", str(round(bmi.bmi,2))],

            ["Category", bmi.category]

        ]

    else:

        bmi_data = [

            ["BMI","No Record"],

            ["Category","No Record"]

        ]

    bmi_table = Table(

        bmi_data,

        colWidths=[180,180]

    )

    bmi_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.lavender),

            ("BOTTOMPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(

        bmi_table

    )

    elements.append(

        Spacer(1,20)

    )

    # =====================================================
    # Health Summary
    # =====================================================

    total = Medicine.query.filter_by(

        user_id=current_user.id

    ).count()

    taken = Medicine.query.filter_by(

        user_id=current_user.id,

        status="Taken"

    ).count()

    if total > 0:

        score = round(

            (taken / total) * 100

        )

    else:

        score = 0

    if score >= 90:

        summary = "Excellent medicine adherence. Keep maintaining your healthy routine."

    elif score >= 75:

        summary = "Good health management. Continue following your medication schedule."

    elif score >= 50:

        summary = "Average health management. Try not to miss your medicines."

    else:

        summary = "Your medicine adherence is low. Follow reminders regularly."

    elements.append(

        Paragraph(

            "<b>Health Summary</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            f"<b>Health Score :</b> {score}%",

            styles["BodyText"]

        )

    )

    elements.append(

        Spacer(1,8)

    )

    elements.append(

        Paragraph(

            summary,

            styles["BodyText"]

        )

    )

    elements.append(

        Spacer(1,20)

    )

    # =====================================================
    # Footer
    # =====================================================

    elements.append(

        Paragraph(

            "<b>Generated by MediMind AI</b>",

            styles["Heading3"]

        )

    )

    elements.append(

        Paragraph(

            "This report is generated automatically using your stored health records.",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            "This report is for educational purposes only and should not replace professional medical advice.",

            styles["Italic"]

        )

    )

    # =====================================================
    # Build PDF
    # =====================================================

    doc.build(

        elements

    )

    buffer.seek(0)

    return send_file(

        buffer,

        download_name="Health_Report.pdf",

        as_attachment=True,

        mimetype="application/pdf"

    )
    