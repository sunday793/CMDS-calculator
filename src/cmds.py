import flet as ft
from flet import (Container, Page, Text, TextField,
                  TextStyle, FontWeight, Colors, Button, 
                  Dropdown, dropdown, Icon, Icons, IconButton,
                  InputFilter, Brightness, Column, Row, ResponsiveRow, 
                  ScrollMode, ThemeMode, Alignment, MainAxisAlignment, 
                  CrossAxisAlignment, Padding)


class Calculator(Container):
    def __init__(self):
        super().__init__()
        self.col = {"xs": 12, "md": 6}
        self.expand = True
        self.padding = 10
        LABEL_WIDTH = 150
        self.result_view = Result() 
        
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
               
                Row([self.h_blood_pressure, 
                     Text("/", size=20), 
                     self.l_blood_pressure], 
                    col={"xs": 6, "md": 3}, 
                    spacing=5,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    alignment= MainAxisAlignment.START ),

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
        return TextField(label= label_text, 
                         label_style=TextStyle(color=Colors.GREY_500),
                         input_filter=InputFilter(allow=True, regex_string=r"^[0-9]*$",replacement_string=""),
                         on_change=error_handling_func,
                         col={"xs": 6, "md": 3},
                         border_color=Colors.GREY_600,
                         error_style=TextStyle(size=10.5),
                         dense=True)
               
    def _create_textfield_float(self, label_text, error_handling_func):
        return TextField(label=label_text,
                         label_style=TextStyle(color=Colors.GREY_500),
                         input_filter=InputFilter(allow=True, regex_string=r"^\d*[.,]?\d*$",replacement_string=""),
                         on_change=error_handling_func,
                         border_color=Colors.GREY_600,
                         col={"xs": 6, "md": 3},
                         error_style=TextStyle(size=10.5),
                         dense=True)
                        
    def _create_dropdown(self, option_1, option_2):
        return Dropdown(options=[dropdown.Option(option_1),
                                 dropdown.Option(option_2)],
                        on_select=self.clear_error_dropbox,
                        border_color=Colors.GREY_600,
                        col={"xs": 6, "md": 3},
                        error_style=TextStyle(size=10.5),
                        dense=True)
                       
                       
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
    def validate_all(self, e):
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
                setattr(self, attr_name, 0)
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
        if is_valid:
            print(f"""Validated: 
                  пол - {self.sex.value}, 
                  ОТ - {self.cir_waist.value}, 
                  ОБ - {self.cir_hips.value}, 
                  blood_pr: {self.h_blood_pressure.value}/{self.l_blood_pressure.value},
                  гипертензия - {self.hypertension.value},
                  антигип терапия - {self.antihyp_therapy.value},
                  cholesterol - {self.cholesterol.value},
                  прием гиполипидемической терапии - {self.hypo_lipidemic_therapy.value},
                  гипертриглицеридемия - {self.triglyceride_level.value},
                  гликемия натощак - {self.fasting_plasma_glucose.value},
                  гликемия при ПГТТ - {self.glucose_pgtt.value},
                  гликированный гемоглобин - {self.glycated_hemoglobin.value},
                  диабет 2-го типа - {self.diabetes_second_type.value},
                  ИБС стенокардия - {self.cad_angina.value},
                  ИБС перенесенный ИМ - {self.cad_mi.value},
                  ХСН - {self.chronic_heart_failure.value},
                  стентирование/шунтирование - {self.stenting_and_bypass.value},
                  stroke or ministroke - {self.stroke_or_ministroke.value},
                  заболевания периферических артерий - {self.peripheral_artery_disease.value}
                  """)
        
        return is_valid

    
    # Submission the Result
    def click_submit_btn(self, e):
        print("------ Validation started ------")
        if self.validate_all(e):
            print("++++++ Validation passed ++++++")
            
            ab_ob_value = self.ab_obesity(e)
            h_bl_pr_value = self.blood_pressure(e)
            hyp_value = self.hyp_func(e)
            anti_h_th_value = self.anti_hyp_therapy_func(e)
            chol_value = self.cholesterol_func(e)
            hyp_lip_th_value = self.hypo_lipid_therapy_func(e)
            trig_value = self.trigl_level_func(e)
            
            self.fasting_plasma_glucose_func(e)
            self.glucose_pgtt_func(e)
            self.glycated_hemoglobin_func(e)
            prediabetes_value = self.prediabetes(e)
            
            diab_sec_type_value = self.diabetes_second_type_func(e)
            cad_value = self.cad_angina_func(e)
            cad_mi_value = self.cad_mi_func(e)
            chf_value = self.chf_func(e)
            stent_bypass_value = self.stenting_bypass_func(e)
            stroke_or_ministroke_value = self.stroke_or_ministroke_func(e)
            periph_art_dis_value = self.periph_artery_dis_func(e)
            
            
            self.display_result(ab_ob_value, self.result_view.ab_ob_icon)
            self.display_result(h_bl_pr_value, self.result_view.high_bl_pr_icon)
            self.display_result(hyp_value, self.result_view.hyp_icon)
            self.display_result(anti_h_th_value, self.result_view.anti_h_th_icon)
            self.display_result(chol_value, self.result_view.hs_lpvp_icon)
            self.display_result(hyp_lip_th_value, self.result_view.hyp_lip_th_icon)
            self.display_result(trig_value, self.result_view.hypertriglyceridemia_icon)
            self.display_result(prediabetes_value, self.result_view.prediabetes_icon)
            
            self.display_result(diab_sec_type_value, self.result_view.diabetes_sec_type_icon)
            self.display_result(cad_value, self.result_view.cad_icon)
            self.display_result(cad_mi_value, self.result_view.cad_mi_icon)
            self.display_result(chf_value, self.result_view.chf_icon)
            self.display_result(stent_bypass_value, self.result_view.stent_bypass_icon)
            self.display_result(stroke_or_ministroke_value, self.result_view.stroke_or_ministroke_icon)
            self.display_result(periph_art_dis_value, self.result_view.periph_art_dis_icon)
            
            cmds_zero_value = self.stage_zero(e)
            cmds_one_value = self.stage_one(e)
            cmds_two_value = self.stage_two(e)
            cmds_three_value = self.stage_three(e)
            cmds_four_value = self.stage_four(e)
            
            if cmds_zero_value:
                cmds_zero_stage = "Стадия 0. Отсутствие анализируемых факторов кардиометаболического риска, сахарного диабета 2-го типа и сердечно-сосудистых заболеваний"
                self.display_cmds(True, cmds_zero_stage, self.result_view.cmds_type_text)
            elif cmds_one_value:
                cmds_first_stage = "Стадия 1. Низкий кардиометаболический риск. 10-летний риск развития СД 2-го типа возрастает в 1,75 раза. 10-летний риск развития сердечно-сосудистых заболеваний возрастает в 3,87 раза"
                self.display_cmds(True, cmds_first_stage, self.result_view.cmds_type_text)
            elif cmds_two_value:
                cmds_second_stage = "Стадия 2. Средний кардиометаболический риск. 10-летний риск развития СД 2-го типа возрастает в 4,6 раза. 10-летний риск развития сердечно-сосудистых заболеваний возрастает в 6,08 раза"
                self.display_cmds(True, cmds_second_stage, self.result_view.cmds_type_text)
            elif cmds_three_value:
                cmds_third_stage = "Стадия 3. Высокий кардиометаболический риск. 10-летний риск развития СД 2-го типа возрастает в 11 раз. 10-летний риск развития сердечно-сосудистых заболеваний возрастает в 6,3 раза"
                self.display_cmds(True, cmds_third_stage, self.result_view.cmds_type_text)
            elif cmds_four_value:
                cmds_fourth_stage = "Стадия 4. Очень высокий кардиометаболический риск. Очень высокий риск осложнений ССЗ и СД 2-го типа. 10-летний риск развития сердечно-сосудистых событий возрастает в 16,3 раза"
                self.display_cmds(True, cmds_fourth_stage, self.result_view.cmds_type_text)
            else:
                self.result_view.cmds_type_text.visible = False
                self.result_view.update()
            
        else:
            print(">>>>>> Validation failed <<<<<<")
        self.result_view.update()
    
    # Clear the Result
    def click_clear_btn(self):
        
        icons = [self.result_view.ab_ob_icon, self.result_view.high_bl_pr_icon,
                 self.result_view.hyp_icon, self.result_view.anti_h_th_icon,
                 self.result_view.hs_lpvp_icon, self.result_view.hyp_lip_th_icon,
                 self.result_view.hypertriglyceridemia_icon, self.result_view.prediabetes_icon,
                 self.result_view.diabetes_sec_type_icon, self.result_view.cad_icon,
                 self.result_view.cad_mi_icon, self.result_view.chf_icon,
                 self.result_view.stent_bypass_icon, self.result_view.stroke_or_ministroke_icon,
                 self.result_view.periph_art_dis_icon]
        for i in icons:
            i.icon = Icons.CIRCLE
            i.color = Colors.GREY
            self.result_view.update()
            
        textfields_dropdowns = [self.cir_waist, self.cir_hips, self.h_blood_pressure, 
                                self.l_blood_pressure, self.cholesterol, self.triglyceride_level, 
                                self.fasting_plasma_glucose, self.glucose_pgtt, self.glycated_hemoglobin, 
                                self.sex, self.hypertension, self.antihyp_therapy, 
                                self.hypo_lipidemic_therapy, self.diabetes_second_type, self.cad_angina, 
                                self.cad_mi, self.chronic_heart_failure, self.stenting_and_bypass, 
                                self.stroke_or_ministroke, self.peripheral_artery_disease]
        for i in textfields_dropdowns:
            i.value = ""
            self.result_view.update()

        self.display_cmds(True, "", self.result_view.cmds_type_text)
        self.result_view.update()
        
    # Displaying the Result
    def display_result(self, value, icon_r):
        new_icon_icon = Icons.CHECK_CIRCLE if value else Icons.CANCEL
        new_icon_color = Colors.RED if value else Colors.GREEN
        
        icon_r.icon = new_icon_icon
        icon_r.color = new_icon_color
      
        self.result_view.update()
        
    def display_cmds(self, value, text, target_control):
        if value:
            target_control.value = text    
            target_control.visible = True 
        else:
            target_control.visible = False 
          
        self.result_view.update()
        
    # Risk Factors Functions
    def ab_obesity(self, e):
        self.is_obesity = False
        if self.cir_hips.value:
            cir_waist_to_hips = round((int(self.cir_waist.value) / int(self.cir_hips.value)), 2)
            print(f"ОТ/ОБ: {cir_waist_to_hips}")
            
            if self.sex.value == 'Мужской' and int(self.cir_waist.value) >= 94 and cir_waist_to_hips > 0.9:
                print("1_Abdominal Obesity found")
                print(f"self.is_obesity: {self.is_obesity}")
                self.is_obesity = True
                return self.is_obesity
            elif self.sex.value == 'Мужской' and int(self.cir_waist.value) >= 94 or cir_waist_to_hips > 0.9:
                print("2_Abdominal Obesity found")
                print(f"self.is_obesity: {self.is_obesity}")
                self.is_obesity = True
                return self.is_obesity
            elif self.sex.value == 'Женский' and int(self.cir_waist.value) >= 80 and cir_waist_to_hips > 0.85:
                print("3_Abdominal Obesity found")
                print(f"self.is_obesity: {self.is_obesity}")
                self.is_obesity = True
                return self.is_obesity
            elif self.sex.value == 'Женский' and int(self.cir_waist.value) >= 80 or cir_waist_to_hips > 0.85:
                print("4_Abdominal Obesity found")
                print(f"self.is_obesity: {self.is_obesity}")
                self.is_obesity = True
                return self.is_obesity
            else:
                print("there is no abdominal obesity")
                print(f"self.is_obesity: {self.is_obesity}")
                return self.is_obesity
        else:
            if self.sex.value == 'Мужской' and int(self.cir_waist.value) >= 94:
                print("5_Abdominal Obesity found")
                print(f"self.is_obesity: {self.is_obesity}")
                self.is_obesity = True
                return self.is_obesity
            elif self.sex.value == 'Женский' and int(self.cir_waist.value) >= 80:
                print("6_Abdominal Obesity found")
                print(f"self.is_obesity: {self.is_obesity}")
                self.is_obesity = True
                return self.is_obesity
            else:
                print("there is no abdominal obesity")
                print(f"self.is_obesity: {self.is_obesity}")
                return self.is_obesity
            
    def blood_pressure(self, e):
        self.is_high_bl_pr = False
        
        if int(self.h_blood_pressure.value) >= 130 or int(self.l_blood_pressure.value) >= 85:
            self.is_high_bl_pr = True
            print(f"High blood pressure: {self.is_high_bl_pr}")
            return self.is_high_bl_pr
        else:
            print(f"High blood pressure: {self.is_high_bl_pr}")
            return self.is_high_bl_pr
            
    def hyp_func(self, e):
        self.is_hypertension = False
        
        if self.hypertension.value == "Да":
            self.is_hypertension = True
            print(f"Есть АГ: {self.is_hypertension}")
            return self.is_hypertension
        else:
            print(f"Есть АГ: {self.is_hypertension}")
            return self.is_hypertension
            
    def anti_hyp_therapy_func(self, e):
        self.is_anti_hyp_therapy = False
        
        if self.antihyp_therapy.value == "Да":
            self.is_anti_hyp_therapy = True
            print(f"Прием антигип терапии: {self.is_anti_hyp_therapy}")
            return self.is_anti_hyp_therapy
        else:
            print(f"Прием антигип терапии: {self.is_anti_hyp_therapy}")
            return self.is_anti_hyp_therapy
            
    def cholesterol_func(self, e):
        self.is_cholesterol_low = False
        self.clear_chol = self.clear_chol
        
        if (self.sex.value == 'Мужской') and (self.clear_chol < 1.0):
            self.is_cholesterol_low = True
            print(f"cholesterol low: {self.sex.value} {self.is_cholesterol_low}")
            return self.is_cholesterol_low
        elif (self.sex.value == 'Женский') and (self.clear_chol < 1.2):
            self.is_cholesterol_low = True
            print(f"cholesterol low: {self.sex.value} {self.is_cholesterol_low}")
            return self.is_cholesterol_low
        else:
            print(f"cholesterol low: {self.is_cholesterol_low}")
            return self.is_cholesterol_low
        
    def hypo_lipid_therapy_func(self, e):
        self.is_hypo_lipid_therapy = False
        
        if self.hypo_lipidemic_therapy.value == "Да":
            self.is_hypo_lipid_therapy = True
            print(f"is_hypo_lipid_therapy: {self.is_hypo_lipid_therapy}")
            return self.is_hypo_lipid_therapy
        else:
            print(f"is_hypo_lipid_therapy: {self.is_hypo_lipid_therapy}")
            return self.is_hypo_lipid_therapy
    
    def trigl_level_func(self, e):
        self.is_hypertriglyceridemia = False
        self.clear_trig = self.clear_trig
        
        if self.clear_trig >= 1.7:
            self.is_hypertriglyceridemia = True
            print(f"is_hypertriglyceridemia - {self.is_hypertriglyceridemia}")
            return self.is_hypertriglyceridemia
        else:
            print(f"is_hypertriglyceridemia - {self.is_hypertriglyceridemia}")
            return self.is_hypertriglyceridemia
    
    # Prediabetes Functions
    def fasting_plasma_glucose_func(self, e):
        self.is_fpg_high = False
        self.clear_fpg = self.clear_fpg
        
        if self.clear_fpg >= 6.1 and self.clear_fpg <= 6.9:
            self.is_fpg_high = True
            print(f"fpg value: {self.clear_fpg} and is_fpg_high: {self.is_fpg_high}")
            return self.is_fpg_high
        else:
            print(f"fpg value: {self.clear_fpg} and is_fpg_high: {self.is_fpg_high}")
            return self.is_fpg_high
        
    def glucose_pgtt_func(self, e):
        self.is_glucose_pgtt_high = False
        self.clear_pgtt = self.clear_pgtt
        
        if self.clear_pgtt >= 7.8 and self.clear_pgtt <= 11.0:
            self.is_glucose_pgtt_high = True
            print(f"is_glucose_pgtt: {self.is_glucose_pgtt_high}")
            return self.is_glucose_pgtt_high
        else:
            print(f"is_glucose_pgtt: {self.is_glucose_pgtt_high}")
            return self.is_glucose_pgtt_high
            
    def glycated_hemoglobin_func(self, e):
        self.is_glyc_hemog_high = False
        self.clear_glyc_hem = self.clear_glyc_hem
        
        if self.clear_glyc_hem >= 6.0 and self.clear_glyc_hem <= 6.4:
            self.is_glyc_hemog_high = True
            print(f"is_glyc_hemog_high: {self.is_glyc_hemog_high}")
            return self.is_glyc_hemog_high
        else:
            print(f"is_glyc_hemog_high: {self.is_glyc_hemog_high}")
            return self.is_glyc_hemog_high
        
    def prediabetes(self, e):
        self.is_prediabetes = False
        
        if self.is_fpg_high or self.is_glucose_pgtt_high or self.is_glyc_hemog_high:
            self.is_prediabetes = True
            print(f"""\nprediabetes found: {self.is_prediabetes}
                  гликемия натощак (is_fpg_high) - {self.is_fpg_high}
                  гликемия при ПГТТ (is_glucose_pgtt_high) - {self.is_glucose_pgtt_high}
                  гликированный гемоглобин (is_glyc_hemog_high) - {self.is_glyc_hemog_high}
                  """)
            return self.is_prediabetes
        else:
            print(f"no prediabetes: {self.is_prediabetes}")
            return self.is_prediabetes
    
    # Diseases Functions
    def diabetes_second_type_func(self, e):
        self.is_diabetes = False
        
        if self.diabetes_second_type.value == "Есть":
            self.is_diabetes = True
            print(f"is_diabetes: {self.is_diabetes}")
            return self.is_diabetes
        else:
            print(f"is_diabetes: {self.is_diabetes}")
            return self.is_diabetes
            
    def cad_angina_func(self, e):
        self.is_cad = False
        
        if self.cad_angina.value == "Есть":
            self.is_cad = True
            print(f"is_cad: {self.is_cad}")
            return self.is_cad
        else:
            print(f"is_cad: {self.is_cad}")
            return self.is_cad
        
    def cad_mi_func(self, e):
        self.is_cad_mi = False
        
        if self.cad_mi.value == "Есть":
            self.is_cad_mi = True
            print(f"is_cad_mi: {self.is_cad_mi}")
            return self.is_cad_mi
        else:
            print(f"is_cad_mi: {self.is_cad_mi}")
            return self.is_cad_mi

    def chf_func(self, e):
        self.is_chf = False
        
        if self.chronic_heart_failure.value == "Есть":
            self.is_chf = True
            print(f"is_chf: {self.is_chf}")
            return self.is_chf
        else:
            print(f"is_chf: {self.is_chf}")
            return self.is_chf
            
    def stenting_bypass_func(self, e):
        self.is_stenting_bypass = False
        
        if self.stenting_and_bypass.value == "Есть":
            self.is_stenting_bypass = True
            print(f"is_stenting_bypass: {self.is_stenting_bypass}")
            return self.is_stenting_bypass
        else:
            print(f"is_stenting_bypass: {self.is_stenting_bypass}")
            return self.is_stenting_bypass
            
    def stroke_or_ministroke_func(self, e):
        self.is_stroke_or_ministroke = False
        
        if self.stroke_or_ministroke.value == "Есть":
            self.is_stroke_or_ministroke = True
            print(f"is_stroke_or_ministroke: {self.is_stroke_or_ministroke}")
            return self.is_stroke_or_ministroke
        else:
            print(f"is_stroke_or_ministroke: {self.is_stroke_or_ministroke}")
            return self.is_stroke_or_ministroke
        
    def periph_artery_dis_func(self, e):
        self.is_periph_artery_dis = False
        
        if self.peripheral_artery_disease.value == "Есть":
            self.is_periph_artery_dis = True
            print(f"is_periph_artery_dis: {self.is_periph_artery_dis}")
            return self.is_periph_artery_dis
        else:
            print(f"is_periph_artery_dis: {self.is_periph_artery_dis}")
            return self.is_periph_artery_dis
            
    # CMDS Functions
    def stage_zero(self, e):
        self.is_stage_zero = False
        
        self.cm_risk_factors = [self.is_obesity, self.is_high_bl_pr, 
            self.is_hypertension, self.is_anti_hyp_therapy, 
            self.is_cholesterol_low, self.is_hypo_lipid_therapy, 
            self.is_hypertriglyceridemia]
        
        self.diseases = [self.is_diabetes, self.is_cad, self.is_cad_mi,
            self.is_chf, self.is_stenting_bypass,
            self.is_stroke_or_ministroke, self.is_periph_artery_dis]
        
        if not any(self.cm_risk_factors) and not any(self.diseases) and not self.is_prediabetes:
            print(">>> no cardiometabolic risk factors and diseases found <<<")
            self.is_stage_zero = True
            return self.is_stage_zero
        else:
            print("stage_zero: False")
            return self.is_stage_zero
    
    def stage_one(self, e):
        self.is_stage_one = False
        
        self.count_true = self.cm_risk_factors.count(True)
        print(f"list self.cm_factor_risks: {self.cm_risk_factors}")
        print(f"count_true: {self.count_true}")
        
        if not any(self.diseases) and not self.is_prediabetes and (self.count_true == 1 or self.count_true == 2):
            self.is_stage_one = True
            print("stage 1")
            return self.is_stage_one
        else:
            print("no stage 1")
            return self.is_stage_one
            
    def stage_two(self, e):
        self.is_stage_two = False
        
        if self.is_prediabetes and not any(self.cm_risk_factors) and not any(self.diseases):
            self.is_stage_two = True
            print(f"stage 2 - is_prediabetes: {self.is_prediabetes}, risk factors: {self.count_true}")
            return self.is_stage_two
        elif self.count_true >= 3 and self.is_prediabetes == False and not any(self.diseases):
            self.is_stage_two = True
            print(f"stage 2 - is_prediabetes: {self.is_prediabetes}, risk factors: {self.count_true}")
            return self.is_stage_two
        else:
            print("no stage 2")
            return self.is_stage_two
    
    def stage_three(self, e):
        self.is_stage_three = False
        
        if self.is_prediabetes and self.count_true >= 3 and not any(self.diseases):
            self.is_stage_three = True
            print(f"stage 3, count_true: {self.count_true}")
            # print("stage 3")
            return self.is_stage_three
        else:
            print("no stage 3")
            return self.is_stage_three
       
    def stage_four(self, e):
        self.is_stage_four = False
        diseases = [self.is_cad, self.is_cad_mi,
            self.is_chf, self.is_stenting_bypass,
            self.is_stroke_or_ministroke, self.is_periph_artery_dis]
        if self.is_diabetes or all(diseases):
            self.is_stage_four = True
            print("stage 4")
            return self.is_stage_four
        else:
            print("no stage 4")
            return self.is_stage_four
                    
            
class Result(Container):
    def __init__(self):
        super().__init__()
        self.col = {"xs": 12, "md": 6}
        self.padding = 10
        
        self.result_text = Text("Результат", size=20, weight=FontWeight.BOLD)
        self.result_text_2 = Text("Факторы кардиометаболического риска", size=18, 
                                  bgcolor=Colors.AMBER_200, color=Colors.BLACK_87)
        self.ab_ob_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30) 
        self.high_bl_pr_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.hyp_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.anti_h_th_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)    
        self.hs_lpvp_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)    
        self.hyp_lip_th_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)    
        self.hypertriglyceridemia_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)    
        self.prediabetes_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)    
        self.diabetes_sec_type_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)    
        self.cad_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.cad_mi_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.chf_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.stent_bypass_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.stroke_or_ministroke_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        self.periph_art_dis_icon = Icon(Icons.CIRCLE, color=Colors.GREY, size=30)
        
        self.cmds_type_text = Text("", size=16)
        
        
        self.content = Column(
            controls = [
                        Row([self.result_text], alignment=MainAxisAlignment.CENTER), 
                        self.result_text_2, 
                        Row([self.ab_ob_icon, 
                             Text("Абдоминальное ожирение", size=16)]),
                        Row([self.high_bl_pr_icon,
                            Text("Повышенное артериальное давление", size=16)]),
                        Row([self.hyp_icon,
                             Text("Наличие артериальной гипертензии", size=16)]),
                        Row([self.anti_h_th_icon,
                             Text("Прием антигипертензивных препаратов", size=16)]),
                        Row([self.hs_lpvp_icon,
                             Text("Снижение ХС-ЛПВП", size=16)]),
                        Row([self.hyp_lip_th_icon,
                             Text("Прием гиполипидемических препаратов (статины, фибраты, др.)", size=16)]),
                        Row([self.hypertriglyceridemia_icon,
                             Text("Гипертриглицеридемия", size=16)]),
                        Row([self.prediabetes_icon,
                             Text("Предиабет", size=16)]),
                        Text("Наличие заболеваний", size=18, bgcolor=Colors.AMBER_200, color=Colors.BLACK_87),
                        Row([self.diabetes_sec_type_icon,
                             Text("Сахарный диабет 2-го типа", size=16)]),
                        Row([self.cad_icon,
                             Text("ИБС. Стабильная стенокардия", size=16)]),
                        Row([self.cad_mi_icon,
                             Text("ИБС. Перенесенный острый коронарный синдром", size=16)]),
                        Row([self.chf_icon,
                             Text("ХСН", size=16)]),
                        Row([self.stent_bypass_icon,
                             Text("Стентирование и/или шунтирование в анамнезе", size=16)]),
                        Row([self.stroke_or_ministroke_icon,
                             Text("Острое нарушение мозгового кровообращения\nили Транзиторная ишемическая атака в анамнезе", 
                                  size=16)]),
                        Row([self.periph_art_dis_icon,
                             Text("Заболевания периферических артерий", size=16)]),
                        Text("Стадирование по CMDS (Cadriometabolic Disease Staging)", size=18, 
                             bgcolor=Colors.AMBER_200, color=Colors.BLACK_87),
                        self.cmds_type_text
                        ], 
            alignment=MainAxisAlignment.START
        )
        
def change_theme_func(e):
    page = e.page
    
    if page.theme_mode == ThemeMode.DARK:
        page.theme_mode = ThemeMode.LIGHT
        e.control.icon = Icons.DARK_MODE
    elif page.theme_mode == ThemeMode.LIGHT:
        page.theme_mode = ThemeMode.DARK
        e.control.icon = Icons.LIGHT_MODE
    elif page.theme_mode == ThemeMode.SYSTEM and e.control.icon == Icons.DARK_MODE:
        page.theme_mode = ThemeMode.DARK
        e.control.icon = Icons.LIGHT_MODE
    elif page.theme_mode == ThemeMode.SYSTEM and e.control.icon == Icons.LIGHT_MODE:
        page.theme_mode = ThemeMode.LIGHT
        e.control.icon = Icons.DARK_MODE
    page.update()


def main(page: Page):
    page.title = 'CMDS'
    page.theme_mode = ThemeMode.SYSTEM
    
    is_dark = page.platform_brightness == Brightness.DARK
    
    # page.window.width = 1000
    # page.window.height = 600
    
    page.scroll = ScrollMode.AUTO
    
    calc = Calculator()
    res = Result()
    
    calc.result_view = res
    
 
    change_theme_light_btn = IconButton(icon=Icons.LIGHT_MODE,
                                  on_click=change_theme_func,
                                  tooltip="Изменить тему")

    change_theme_dark_btn = IconButton(icon=Icons.DARK_MODE,
                                  on_click=change_theme_func,
                                  tooltip="Изменить тему")

    # pw = Text("All rigths reserved", 
    #           text_align=TextAlign.CENTER, 
    #           style=TextTheme.display_small)
    
    # footer_container = Container(
    #     content=pw,
    #     bottom=20,
    #     left = 0,
    #     right=0,
    #     alignment = Alignment(0, 0))
    
    # page.overlay.append(footer_container)
    # page.bottom_appbar.content(footer_container)
    
    sources = Container(
        content=Text(
    """Источники:
1.	The progression of cardiometabolic disease: Validation of a new cardiometabolic disease staging system applicable to obesity / F. Guo, D. R. Moellering, W. T. Garvey, 2014; 
2.	Концепция новых национальных клинических рекомендаций по ожирению / Е. В. Шляхто, С. В. Недогода, А. О. Конради [и др.], 2016; 
3.	Ожирение : оценка и тактика ведения пациентов. Коллективная монография / О. М. Драпкина, И. В. Самородская, М. А. Старинская [и др.], 2021]

    """,
        size=16
        )
    )
    
    row_cont = ResponsiveRow(
        controls=[calc, 
                  res,
                  Container(height=100),
                  sources],
        spacing=10,
        run_spacing=10 # Gap between rows when they wrap
    )
    
    if is_dark == True:
        page.add(Text("Калькулятор расчета кардиометаболического риска", size=40, align=Alignment(0, 1)), 
                Row([change_theme_light_btn], alignment=MainAxisAlignment.CENTER),
                row_cont)
        page.update()
    else:
        page.add(Text("Калькулятор расчета кардиометаболического риска", size=40, align=Alignment(0, 1)), 
                Row([change_theme_dark_btn], alignment=MainAxisAlignment.CENTER),
                row_cont)
        page.update()
    
ft.run(main)