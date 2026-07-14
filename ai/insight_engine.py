from models.medicine import Medicine
from models.water import WaterLog
from models.sleep import SleepLog
from models.bmi import BMI
from models.reminder import Reminder


class InsightEngine:

    # ========================================
    # Health Score
    # ========================================

    @staticmethod
    def health_score(user_id):

        total = Medicine.query.filter_by(
            user_id=user_id
        ).count()

        taken = Medicine.query.filter_by(
            user_id=user_id,
            status="Taken"
        ).count()

        if total == 0:
            return 0

        return round((taken / total) * 100)

    # ==========================================
    # Water Insight
    # ==========================================

    @staticmethod
    def water_insight(user_id):

        water = WaterLog.query.filter_by(
            user_id=user_id
        ).order_by(
            WaterLog.id.desc()
        ).first()

        if not water:

            return {

                "title": "Water Intake",

                "message": "No water record found."

            }

        if water.glasses >= 8:

            return {

                "title": "Water Intake",

                "message": "Excellent! You achieved today's water goal."

            }

        if water.glasses >= 5:

            return {

                "title": "Water Intake",

                "message": "Good. Drink a few more glasses today."

            }

        return {

            "title": "Water Intake",

            "message": "Your water intake is low. Stay hydrated."

        }

    # ==========================================
    # Sleep Insight
    # ==========================================

    @staticmethod
    def sleep_insight(user_id):

        sleep = SleepLog.query.filter_by(
            user_id=user_id
        ).order_by(
            SleepLog.id.desc()
        ).first()

        if not sleep:

            return {

                "title": "Sleep",

                "message": "No sleep record available."

            }

        if sleep.total_hours >= 8:

            return {

                "title": "Sleep",

                "message": "Excellent sleep duration."

            }

        if sleep.total_hours >= 7:

            return {

                "title": "Sleep",

                "message": "Good sleep. Maintain this routine."

            }

        if sleep.total_hours >= 6:

            return {

                "title": "Sleep",

                "message": "Sleep duration is slightly low."

            }

        return {

            "title": "Sleep",

            "message": "Poor sleep duration. Try sleeping earlier."

        }

    # ==========================================
    # BMI Insight
    # ==========================================

    @staticmethod
    def bmi_insight(user_id):

        bmi = BMI.query.filter_by(
            user_id=user_id
        ).order_by(
            BMI.id.desc()
        ).first()

        if not bmi:

            return {

                "title": "BMI",

                "message": "BMI record not available."

            }

        return {

            "title": "BMI",

            "message": f"Your BMI is {bmi.bmi_value:.1f} ({bmi.category})."

        }

    # ==========================================
    # Medicine Insight
    # ==========================================

    @staticmethod
    def medicine_insight(user_id):

        pending = Medicine.query.filter_by(
            user_id=user_id,
            status="Pending"
        ).count()

        missed = Medicine.query.filter_by(
            user_id=user_id,
            status="Missed"
        ).count()

        taken = Medicine.query.filter_by(
            user_id=user_id,
            status="Taken"
        ).count()

        return {

            "taken": taken,

            "pending": pending,

            "missed": missed

        }

    # =========================================
    # Reminder Insight
    # =========================================

    @staticmethod
    def reminder_insight(user_id):

        reminders = Reminder.query.join(
            Medicine
        ).filter(
            Medicine.user_id == user_id
        ).count()

        return reminders

    # ==========================================
    # Overall Insight
    # ==========================================

    @staticmethod
    def generate(user_id):

        score = InsightEngine.health_score(
            user_id
        )

        insights = []

        insights.append(

            InsightEngine.water_insight(
                user_id
            )

        )

        insights.append(

            InsightEngine.sleep_insight(
                user_id
            )

        )

        insights.append(

            InsightEngine.bmi_insight(
                user_id
            )

        )

        medicine = InsightEngine.medicine_insight(
            user_id
        )

        if medicine["missed"] > 0:

            insights.append({

                "title": "Medicine",

                "message": f"You missed {medicine['missed']} medicine(s)."

            })

        elif medicine["pending"] > 0:

            insights.append({

                "title": "Medicine",

                "message": f"You still have {medicine['pending']} pending medicine(s)."

            })

        else:

            insights.append({

                "title": "Medicine",

                "message": "Great! All medicines are completed."

            })

        if score >= 90:

            summary = "Excellent health routine."

        elif score >= 75:

            summary = "Very good health management."

        elif score >= 60:

            summary = "Average health routine."

        else:

            summary = "Health routine needs improvement."

        return {

            "health_score": score,

            "summary": summary,

            "insights": insights

        }

    # ==========================================
    # Dashboard Tips
    # ==========================================

    @staticmethod
    def dashboard_tips(user_id):

        data = InsightEngine.generate(
            user_id
        )

        tips = []

        for item in data["insights"]:

            tips.append(item["message"])

        return tips

    # ==========================================
    # Status
    # ==========================================

    @staticmethod
    def status():

        return {

            "engine": "Insight Engine",

            "version": "2.0",

            "status": "Running"

        }
