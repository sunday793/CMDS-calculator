from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PatientInput:
    """
    Data transfer object containing raw clinical parameters for a patient.

    Attributes:
        sex (str): Biological sex of the patient ("Мужской" or "Женский").
        cir_waist (int): Waist circumference in centimeters.
        cir_hips (Optional[int]): Hip circumference in centimeters, if available.
        h_blood_pressure (int): Systolic blood pressure in mmHg.
        l_blood_pressure (int): Diastolic blood pressure in mmHg.
        hypertension (bool): Flag indicating diagnosed essential hypertension.
        antihyp_therapy (bool): Flag indicating active antihypertensive drug therapy.
        cholesterol (float): High-density lipoprotein (HDL) cholesterol in mmol/L.
        hypo_lipidemic_therapy (bool): Flag indicating active lipid-lowering therapy.
        triglyceride_level (float): Serum triglyceride level in mmol/L.
        fasting_plasma_glucose (Optional[float]): Fasting plasma glucose level in mmol/L.
        glucose_pgtt (Optional[float]): Post-glucose load (2h OGTT) level in mmol/L.
        glycated_hemoglobin (Optional[float]): Glycated hemoglobin (HbA1c) level in %.
        diabetes_second_type (bool): Flag indicating diagnosed Type 2 Diabetes Mellitus.
        cad_angina (bool): Flag indicating Coronary Artery Disease with stable angina.
        cad_mi (bool): Flag indicating history of Myocardial Infarction.
        chronic_heart_failure (bool): Flag indicating Chronic Heart Failure.
        stenting_and_bypass (bool): Flag indicating coronary stenting or CABG history.
        stroke_or_ministroke (bool): Flag indicating history of stroke or TIA.
        peripheral_artery_disease (bool): Flag indicating Peripheral Artery Disease.
    """
    sex: str
    cir_waist: int
    cir_hips: Optional[int]
    h_blood_pressure: int
    l_blood_pressure: int
    hypertension: bool
    antihyp_therapy: bool
    cholesterol: float
    hypo_lipidemic_therapy: bool
    triglyceride_level: float
    fasting_plasma_glucose: Optional[float]
    glucose_pgtt: Optional[float]
    glycated_hemoglobin: Optional[float]
    diabetes_second_type: bool
    cad_angina: bool
    cad_mi: bool
    chronic_heart_failure: bool
    stenting_and_bypass: bool
    stroke_or_ministroke: bool
    peripheral_artery_disease: bool

@dataclass(frozen=True)
class CMDSResult:
    """
    Data transfer object containing evaluated risk indicators and final CMDS stage.

    Attributes:
        is_obesity (bool): Calculated flag for abdominal obesity.
        is_high_blood_pressure (bool): Flag indicating elevated blood pressure (>=130/85 mmHg).
        is_hypertension (bool): Flag indicating diagnosed hypertension status.
        is_anti_hyp_therapy (bool): Flag indicating active antihypertensive treatment.
        is_cholesterol_low (bool): Flag indicating abnormally low HDL cholesterol.
        is_hypo_lipid_therapy (bool): Flag indicating active lipid-lowering treatment.
        is_hypertriglyceridemia (bool): Flag indicating elevated triglycerides (>=1.7 mmol/L).
        is_prediabetes (bool): Flag indicating prediabetes criteria are met.
        is_diabetes (bool): Flag indicating Type 2 Diabetes presence.
        is_cad (bool): Flag indicating Coronary Artery Disease (angina).
        is_cad_mi (bool): Flag indicating prior Myocardial Infarction.
        is_chf (bool): Flag indicating Chronic Heart Failure.
        is_stenting_bypass (bool): Flag indicating coronary revascularization history.
        is_stroke_or_ministroke (bool): Flag indicating cerebrovascular disease history.
        is_periph_artery_dis (bool): Flag indicating Peripheral Artery Disease.
        stage (int): Assigned Cardiometabolic Disease Stage (0 to 4).
        cmds_stage_text (str): Detailed clinical description corresponding to the stage.
    """
    is_obesity: bool
    is_high_blood_pressure: bool
    is_hypertension: bool
    is_antihyp_therapy: bool
    is_cholesterol_low: bool
    is_hypo_lipid_therapy: bool
    is_hypertriglyceridemia: bool
    is_prediabetes: bool
    is_diabetes: bool
    is_cad: bool
    is_cad_mi: bool
    is_chf: bool
    is_stenting_bypass: bool
    is_stroke_or_ministroke: bool
    is_periph_artery_dis: bool
    stage: int
    cmds_stage_text: str
