from typing import List
from domain.models import PatientInput, CMDSResult

class CMDSEvaluator:
    """
    Service class responsible for evaluating Cardiometabolic Disease Staging (CMDS).

    This service processes clinical measurements and diagnostic indicators to determine
    individual risk factor flags and calculate the overall CMDS stage (Stages 0–4)
    according to standard clinical guidelines.

    Attributes:
        STAGE_DESCRIPTIONS (dict[int, str]): Mapping of CMDS stage numbers to their 
            corresponding clinical summary descriptions.
    """

    STAGE_DESCRIPTIONS = {
        0: "Стадия 0. Отсутствие анализируемых факторов кардиометаболического риска, сахарного диабета 2-го типа и сердечно-сосудистых заболеваний",
        1: "Стадия 1. Низкий кардиометаболический риск. 10-летний риск развития СД 2-го типа возрастает в 1,75 раза. 10-летний риск развития сердечно-сосудистых заболеваний возрастает в 3,87 раза",
        2: "Стадия 2. Средний кардиометаболический риск. 10-летний риск развития СД 2-го типа возрастает в 4,6 раза. 10-летний риск развития сердечно-сосудистых заболеваний возрастает в 6,08 раза",
        3: "Стадия 3. Высокий кардиометаболический риск. 10-летний риск развития СД 2-го типа возрастает в 11 раз. 10-летний риск развития сердечно-сосудистых заболеваний возрастает в 6,3 раза",
        4: "Стадия 4. Очень высокий кардиометаболический риск. Очень высокий риск осложнений ССЗ и СД 2-го типа. 10-летний риск развития сердечно-сосудистых событий возрастает в 16,3 раза"
    }

    def evaluate(self, patient: PatientInput) -> CMDSResult:
        """
        Evaluates patient parameters to determine the CMDS risk stage.

        Args:
            patient (PatientInput): Structured dataclass containing clinical measurements.

        Returns:
            CMDSResult: Computed risk flags, stage score (0-4), and description.
        """
        is_obesity = self._check_abdominal_obesity(patient)
        is_high_blood_pressure = (patient.h_blood_pressure >= 130 or
                                  patient.l_blood_pressure >= 85)
        is_hypertension = patient.hypertension
        is_antihyp_therapy = patient.antihyp_therapy

        is_cholesterol_low = (
            (patient.cholesterol < 1.0)
            if patient.sex == "Мужской"
            else (patient.cholesterol < 1.2)
        )

        is_hypo_lipid_therapy = patient.hypo_lipidemic_therapy
        is_hypertriglyceridemia = patient.triglyceride_level >= 1.7
        is_prediabetes = self._check_prediabetes(patient)

        cm_risk_factors: List[bool] = [
            is_obesity,
            is_high_blood_pressure,
            is_hypertension,
            is_antihyp_therapy,
            is_cholesterol_low,
            is_hypo_lipid_therapy,
            is_hypertriglyceridemia
        ]

        diseases: List[bool] = [
            patient.cad_angina,
            patient.cad_mi,
            patient.chronic_heart_failure,
            patient.stenting_and_bypass,
            patient.stroke_or_ministroke,
            patient.peripheral_artery_disease
        ]

        count_true = cm_risk_factors.count(True)

        stage = self._determine_stage(
            is_diabetes = patient.diabetes_second_type,
            count_true = count_true,
            is_prediabetes = is_prediabetes,
            diseases = diseases
        )

        return CMDSResult(
            is_obesity = is_obesity,
            is_high_blood_pressure = is_high_blood_pressure,
            is_hypertension = is_hypertension,
            is_antihyp_therapy = is_antihyp_therapy,
            is_cholesterol_low = is_cholesterol_low,
            is_hypo_lipid_therapy = is_hypo_lipid_therapy,
            is_hypertriglyceridemia = is_hypertriglyceridemia,
            is_prediabetes = is_prediabetes,
            is_diabetes = patient.diabetes_second_type,
            is_cad = patient.cad_angina,
            is_cad_mi = patient.cad_mi,
            is_chf = patient.chronic_heart_failure,
            is_stenting_bypass = patient.stenting_and_bypass,
            is_stroke_or_ministroke = patient.stroke_or_ministroke,
            is_periph_artery_dis = patient.peripheral_artery_disease,
            stage = stage,
            cmds_stage_text = self.STAGE_DESCRIPTIONS.get(stage, "")
        )

    def _check_abdominal_obesity(self, patient: PatientInput) -> bool:
        """
        Determines the presence of abdominal obesity based on clinical thresholds.

        Evaluates waist circumference and waist-to-hip ratio (WHR) using sex-specific
        cutoff values (Waist >= 94 cm or WHR > 0.9 for males; Waist >= 80 cm or 
        WHR > 0.85 for females). If hip circumference is unavailable or non-positive,
        only the waist circumference threshold is evaluated.

        Args:
            patient (PatientInput): Structured object containing the patient's sex, 
                waist circumference, and optional hip circumference.

        Returns:
            bool: True if the patient meets the criteria for abdominal obesity, 
            False otherwise.
        """
        if patient.cir_hips and patient.cir_hips > 0:
            cir_waist_to_hips = round(patient.cir_waist / patient.cir_hips, 2)
            if patient.sex == "Мужской":
                return patient.cir_waist >= 94 or cir_waist_to_hips > 0.9
            return patient.cir_waist >= 80 or cir_waist_to_hips > 0.85

        threshold = 94 if patient.sex == "Мужской" else 80
        return patient.cir_waist >= threshold

    def _check_prediabetes(self, patient: PatientInput) -> bool:
        """
        Evaluates whether any laboratory prediabetes diagnostic criteria are met.

        Checks three independent glycemic indicators against clinical prediabetes ranges:
        - Fasting plasma glucose (FPG): 6.1 – 6.9 mmol/L
        - Post-prandial glucose (2h OGTT): 7.8 – 11.0 mmol/L
        - Glycated hemoglobin (HbA1c): 6.0% – 6.4%

        Args:
            patient (PatientInput): Structured object containing optional lab test 
                results for FPG, OGTT, and HbA1c.

        Returns:
            bool: True if at least one available laboratory test falls within 
            the prediabetic range, False otherwise.
        """
        is_fpg_high = (
            6.1 <= patient.fasting_plasma_glucose <= 6.9
            if patient.fasting_plasma_glucose is not None
            else False
        )
        is_glucose_pgtt_high = (
            7.8 <= patient.glucose_pgtt <= 11.0
            if patient.glucose_pgtt is not None
            else False
        )
        is_glyc_hemog_high = (
            6.0 <= patient.glycated_hemoglobin <= 6.4
            if patient.glycated_hemoglobin is not None
            else False
        )

        return is_fpg_high or is_glucose_pgtt_high or is_glyc_hemog_high

    def _determine_stage(
            self,
            is_diabetes: bool,
            count_true: int,
            is_prediabetes: bool,
            diseases: List[bool]
        ) -> int:
        """
        Determines the final CMDS risk stage (Stage 0 to Stage 4).

        Applies clinical decision rules based on disease presence, metabolic risk factor 
        counts, and prediabetes diagnosis:
        - Stage 4: Presence of Type 2 Diabetes OR all tracked cardiovascular diseases.
        - Stage 3: Prediabetes AND >= 3 risk factors without established CVD.
        - Stage 2: Prediabetes OR >= 3 risk factors without established CVD.
        - Stage 1: 1 or 2 risk factors without prediabetes or established CVD.
        - Stage 0: Zero active risk factors and no clinical conditions.

        Args:
            is_diabetes (bool): Indicates if Type 2 Diabetes is present.
            count_true (int): The total count of active cardiometabolic risk factors.
            is_prediabetes (bool): Indicates if prediabetes threshold criteria are met.
            diseases (List[bool]): Flags indicating established cardiovascular diseases.

        Returns:
            int: Calculated CMDS stage score ranging from 0 to 4.
        """
        has_any_disease = any(diseases)

        if is_diabetes or all(diseases):
            return 4

        if is_prediabetes and count_true >= 3 and not has_any_disease:
            return 3

        if (is_prediabetes or count_true >= 3) and not has_any_disease:
            return 2

        if count_true in (1, 2) and not is_prediabetes and not has_any_disease:
            return 1

        return 0