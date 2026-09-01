import flet as ft
from flet import (Container, Text, TextField, TextStyle, FontWeight, Colors, 
                  Button, Dropdown, dropdown, Icons, InputFilter, Column, Row, 
                  ResponsiveRow, ScrollMode, MainAxisAlignment, CrossAxisAlignment)

from domain import CMDSEvaluator, PatientInput, CMDSResult


class Calculator(Container):
    """
    UI component for the Cardiometabolic Disease Staging calculator.

    Encapsulates patient input controls, form submission logic, and result 
    display within a single reusable Flet Container.
    """

    def __init__(self):
        super().__init__()
        self.col = {"xs": 12, "md": 6}
        self.expand = True
        self.padding = 10
        
        self.evaluator = CMDSEvaluator()
        self.result_view = None

        self.sex = self._create_dropdown("Мужской", "Женский")
        self.cir_waist = self._create_textfield_int("в см", self.clear_error_textfield)
        self.cir_hips = self._create_textfield_int("в см", self.clear_error_textfield)
        
        self.h_blood_pressure = self._create_textfield_int("в мм", self.clear_error_textfield)
        self.h_blood_pressure.width = 60
        self.h_blood_pressure.col = {}
        
        self.l_blood_pressure = self._create_textfield_int("в мм", self.clear_error_textfield)
        self.l_blood_pressure.width = 60
        self.l_blood_pressure.col = {}
        
        self.hypertension = self._create_dropdown("Да", "Нет")
        self.antihyp_therapy = self._create_dropdown("Да", "Нет")
        self.cholesterol = self._create_textfield_float("в ммоль/л", self.clear_error_textfield)
        self.hypo_lipidemic_therapy = self._create_dropdown("Да", "Нет")
        self.triglyceride_level = self._create_textfield_float("в ммоль/л", self.clear_error_textfield)
        
        self.fasting_plasma_glucose = self._create_textfield_float("в ммоль/л", self.clear_group_errors)
        self.glucose_pgtt = self._create_textfield_float("в ммоль/л", self.clear_group_errors)
        self.glycated_hemoglobin = self._create_textfield_float("в %", self.clear_group_errors)
        
        self.diabetes_second_type = self._create_dropdown("Есть", "Нет")
        self.cad_angina = self._create_dropdown("Есть", "Нет")
        self.cad_mi = self._create_dropdown("Есть", "Нет")
        self.chronic_heart_failure = self._create_dropdown("Есть", "Нет")
        self.stenting_and_bypass = self._create_dropdown("Есть", "Нет")
        self.stroke_or_ministroke = self._create_dropdown("Есть", "Нет")
        self.peripheral_artery_disease = self._create_dropdown("Есть", "Нет")
        
        self.submit_btn = Button("Рассчитать", on_click=self.click_submit_btn)
        self.clear_btn = Button("Очистить", on_click=self.click_clear_btn)
        
        self._build_layout()

    def _build_layout(self) -> None:
        """Assembles exact original UI structure."""
        self.content = Column(
            scroll=ScrollMode.ADAPTIVE,
            tight=True,
            controls=[
                Text("Введите: ", size=20, weight=FontWeight.BOLD),
                ResponsiveRow(
                    spacing=10,
                    run_spacing=10,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text("Пол:", size=16, col={"xs": 6, "md": 3}),
                        self.sex,
                        
                        Text("Окружность талии:", size=16, col={"xs": 6, "md": 3}),
                        self.cir_waist,
                        
                        Text("Окружность бёдер:", size=16, col={"xs": 6, "md": 3}),
                        self.cir_hips,

                        Text("Артериальное давление:", size=16, col={"xs": 6, "md": 3}),
                        Row(
                            [
                                self.h_blood_pressure, 
                                Text("/", size=20), 
                                self.l_blood_pressure
                            ], 
                            col={"xs": 6, "md": 3}, 
                            spacing=5,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            alignment=MainAxisAlignment.START
                        ),

                        Text("Есть артериальная гипертензия?", size=16, col={"xs": 6, "md": 3}),
                        self.hypertension,

                        Text("Прием антигипертензивных препаратов:", size=16, col={"xs": 6, "md": 3}),
                        self.antihyp_therapy,

                        Text("ХС-ЛПВП:", size=16, col={"xs": 6, "md": 3}),
                        self.cholesterol,

                        Text("Прием гиполипидемических препаратов (статины, фибраты, др.):", size=16, col={"xs": 6, "md": 3}),
                        self.hypo_lipidemic_therapy,

                        Text("Уровень триглицеридов (ТГ):", size=16, col={"xs": 6, "md": 3}),
                        self.triglyceride_level,

                        Text("Гликемия натощак:", size=16, col={"xs": 6, "md": 3}),
                        self.fasting_plasma_glucose,

                        Text("Гликемия через 2 часа после ПГТТ:", size=16, col={"xs": 6, "md": 3}),
                        self.glucose_pgtt,

                        Text("Гликированный гемоглобин (HbA1с):", size=16, col={"xs": 6, "md": 3}),
                        self.glycated_hemoglobin,

                        Text("Наличие заболеваний:", size=20, weight=FontWeight.BOLD, col=12),
                        
                        Text("Сахарный диабет 2-го типа:", size=16, col={"xs": 6, "md": 3}),
                        self.diabetes_second_type,

                        Text("ИБС. Стабильная стенокардия:", size=16, col={"xs": 6, "md": 3}),
                        self.cad_angina,

                        Text("ИБС. Перенесенный острый коронарный синдром:", size=16, col={"xs": 6, "md": 3}),
                        self.cad_mi,

                        Text("ХСН:", size=16, col={"xs": 6, "md": 3}),
                        self.chronic_heart_failure,

                        Text("Стентирование и/или шунтирование в анамнезе:", size=16, col={"xs": 6, "md": 3}),
                        self.stenting_and_bypass,

                        Text("Острое нарушение мозгового кровообращения или Транзиторная ишемическая атака в анамнезе:", 
                             size=16, col={"xs": 6, "md": 3}),
                        self.stroke_or_ministroke,

                        Text("Заболевания периферических артерий:", size=16, col={"xs": 6, "md": 3}),
                        self.peripheral_artery_disease,
                    ]
                ),
                Row(controls=[self.submit_btn, self.clear_btn], alignment=MainAxisAlignment.CENTER, spacing=20)
            ]
        )

    # Factory Methods
    def _create_textfield_int(self, label_text, error_handling_func):
        return TextField(
            label=label_text, 
            label_style=TextStyle(color=Colors.GREY_500),
            input_filter=InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string=""),
            on_change=error_handling_func,
            col={"xs": 6, "md": 3},
            border_color=Colors.GREY_600,
            error_style=TextStyle(size=10.5),
            dense=True
        )
               
    def _create_textfield_float(self, label_text, error_handling_func):
        return TextField(
            label=label_text,
            label_style=TextStyle(color=Colors.GREY_500),
            input_filter=InputFilter(allow=True, regex_string=r"^\d*[.,]?\d*$", replacement_string=""),
            on_change=error_handling_func,
            border_color=Colors.GREY_600,
            col={"xs": 6, "md": 3},
            error_style=TextStyle(size=10.5),
            dense=True
        )
                        
    def _create_dropdown(self, option_1, option_2):
        return Dropdown(
            options=[
                dropdown.Option(option_1),
                dropdown.Option(option_2)
            ],
            on_select=self.clear_error_dropbox,
            border_color=Colors.GREY_600,
            col={"xs": 6, "md": 3},
            error_style=TextStyle(size=10.5),
            dense=True
        )

    # Errors Handling
    def clear_error_textfield(self, e):
        if e.control.error:
            e.control.error = None
            e.control.update()
            
    def clear_error_dropbox(self, e):
        if e.control.error_text:
            e.control.error_text = None
            e.control.update()
    
    def clear_group_errors(self, e):
        if e.control.value:
            self.fasting_plasma_glucose.error = None
            self.glucose_pgtt.error = None
            self.glycated_hemoglobin.error = None
            
            self.fasting_plasma_glucose.update()
            self.glucose_pgtt.update()
            self.glycated_hemoglobin.update()

    # Validation
    def validate_all(self, e) -> bool:
        is_valid = True
        
        required_fields = [
            (self.sex, "Это поле обязательно!", "error_text"),
            (self.cir_waist, "Это поле\nобязательно!", "error"),
            (self.h_blood_pressure, "Это поле обязательно!", "error"),
            (self.l_blood_pressure, "Это поле обязательно!", "error"),
            (self.hypertension, "Это поле\nобязательно!", "error_text"),
            (self.antihyp_therapy, "Это поле\nобязательно!", "error_text"),
            (self.cholesterol, "Это поле\nобязательно!", "error"),
            (self.hypo_lipidemic_therapy, "Это поле\nобязательно!", "error_text"),
            (self.triglyceride_level, "Это поле\nобязательно!", "error"),
            (self.diabetes_second_type, "Это поле\nобязательно!", "error_text"),
            (self.cad_angina, "Это поле\nобязательно!", "error_text"),
            (self.cad_mi, "Это поле\nобязательно!", "error_text"),
            (self.chronic_heart_failure, "Это поле\nобязательно!", "error_text"),
            (self.stenting_and_bypass, "Это поле\nобязательно!", "error_text"),
            (self.stroke_or_ministroke, "Это поле\nобязательно!", "error_text"),
            (self.peripheral_artery_disease, "Это поле\nобязательно!", "error_text"),
        ]

        for control, _, prop in required_fields:
            setattr(control, prop, None)
        for ctrl in [self.fasting_plasma_glucose, self.glucose_pgtt, self.glycated_hemoglobin]:
            ctrl.error = None

        for control, message, prop in required_fields:
            if control.value is None or str(control.value).strip() == "":
                setattr(control, prop, message)
                is_valid = False

        def parse_float(control, attr_name):
            val = control.value
            if not val:
                setattr(self, attr_name, 0.0)
                return True
            try:
                setattr(self, attr_name, float(val.replace(",", ".")))
                return True
            except ValueError:
                control.error = "Введите корректное число!"
                return False

        if not parse_float(self.cholesterol, "clear_chol"): is_valid = False
        if not parse_float(self.triglyceride_level, "clear_trig"): is_valid = False
        if not parse_float(self.fasting_plasma_glucose, "clear_fpg"): is_valid = False
        if not parse_float(self.glucose_pgtt, "clear_pgtt"): is_valid = False
        if not parse_float(self.glycated_hemoglobin, "clear_glyc_hem"): is_valid = False

        if not any([self.fasting_plasma_glucose.value, self.glucose_pgtt.value, self.glycated_hemoglobin.value]):
            msg = "Введите данные\nхотя бы в одно\nполе"
            self.fasting_plasma_glucose.error = msg
            self.glucose_pgtt.error = msg
            self.glycated_hemoglobin.error = msg
            is_valid = False

        self.update()
        return is_valid

    # Submission delegating directly to domain logic
    def click_submit_btn(self, e):
        if self.validate_all(e):
            patient_input = PatientInput(
                sex=self.sex.value,
                cir_waist=int(self.cir_waist.value),
                cir_hips=int(self.cir_hips.value) if self.cir_hips.value else None,
                h_blood_pressure=int(self.h_blood_pressure.value),
                l_blood_pressure=int(self.l_blood_pressure.value),
                hypertension=(self.hypertension.value == "Да"),
                antihyp_therapy=(self.antihyp_therapy.value == "Да"),
                cholesterol=float(self.cholesterol.value.replace(",", ".")),
                hypo_lipidemic_therapy=(self.hypo_lipidemic_therapy.value == "Да"),
                triglyceride_level=float(self.triglyceride_level.value.replace(",", ".")),
                fasting_plasma_glucose=float(self.fasting_plasma_glucose.value.replace(",", ".")) if self.fasting_plasma_glucose.value else None,
                glucose_pgtt=float(self.glucose_pgtt.value.replace(",", ".")) if self.glucose_pgtt.value else None,
                glycated_hemoglobin=float(self.glycated_hemoglobin.value.replace(",", ".")) if self.glycated_hemoglobin.value else None,
                diabetes_second_type=(self.diabetes_second_type.value == "Есть"),
                cad_angina=(self.cad_angina.value == "Есть"),
                cad_mi=(self.cad_mi.value == "Есть"),
                chronic_heart_failure=(self.chronic_heart_failure.value == "Есть"),
                stenting_and_bypass=(self.stenting_and_bypass.value == "Есть"),
                stroke_or_ministroke=(self.stroke_or_ministroke.value == "Есть"),
                peripheral_artery_disease=(self.peripheral_artery_disease.value == "Есть"),
            )

            result: CMDSResult = self.evaluator.evaluate(patient_input)

            if self.result_view:
                self.result_view.update_from_domain_result(result)

    # Reset UI
    def click_clear_btn(self, e=None):
        textfields_dropdowns = [
            self.cir_waist, self.cir_hips, self.h_blood_pressure, 
            self.l_blood_pressure, self.cholesterol, self.triglyceride_level, 
            self.fasting_plasma_glucose, self.glucose_pgtt, self.glycated_hemoglobin, 
            self.sex, self.hypertension, self.antihyp_therapy, 
            self.hypo_lipidemic_therapy, self.diabetes_second_type, self.cad_angina, 
            self.cad_mi, self.chronic_heart_failure, self.stenting_and_bypass, 
            self.stroke_or_ministroke, self.peripheral_artery_disease
        ]
        for i in textfields_dropdowns:
            i.value = ""
        
        self.update()

        if self.result_view:
            self.result_view.clear_view()