from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.fitness_workout_nutrition_coach.models import AgenticFitnessWorkoutNutritionCoachSession, AgenticFitnessWorkoutNutritionCoachItem
from app.domain.fitness_workout_nutrition_coach.schemas import AgenticFitnessWorkoutNutritionCoachSessionCreate, AgenticFitnessWorkoutNutritionCoachItemCreate

class AgenticFitnessWorkoutNutritionCoachService:
    @staticmethod
    def create_session(db: Session, data: AgenticFitnessWorkoutNutritionCoachSessionCreate) -> AgenticFitnessWorkoutNutritionCoachSession:
        db_obj = AgenticFitnessWorkoutNutritionCoachSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticFitnessWorkoutNutritionCoachSession:
        return db.query(AgenticFitnessWorkoutNutritionCoachSession).filter(AgenticFitnessWorkoutNutritionCoachSession.id == session_id).first()
