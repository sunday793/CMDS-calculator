import flet as ft
from flet import (Container, Text, FontWeight, Colors, Icon, Icons, 
                  Column, Row, MainAxisAlignment)
from domain import CMDSResult


class Result(Container):
    """UI component for presenting CMDS evaluation results and risk indicators."""

    def __init__(self):
        super().__init__()
        self.col = {"xs": 12, "md": 6}
        self.padding = 10
        
        self.result_text = Text("Результат", size=20, weight=FontWeight.BOLD)
        self.result_text_2 = Text(
            "Факторы кардиометаболического риска", 
            size=18, 
            bgcolor=Colors.AMBER_200, 
            color=Colors.BLACK_87
        )
        
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
            controls=[
                Row([self.result_text], alignment=MainAxisAlignment.CENTER), 
                self.result_text_2, 
                Row([self.ab_ob_icon, Text("Абдоминальное ожирение", size=16, expand=True)]),
                Row([self.high_bl_pr_icon, Text("Повышенное артериальное давление", size=16, expand=True)]),
                Row([self.hyp_icon, Text("Наличие артериальной гипертензии", size=16, expand=True)]),
                Row([self.anti_h_th_icon, Text("Прием антигипертензивных препаратов", size=16, expand=True)]),
                Row([self.hs_lpvp_icon, Text("Снижение ХС-ЛПВП", size=16, expand=True)]),
                Row([self.hyp_lip_th_icon, Text("Прием гиполипидемических препаратов (статины, фибраты, др.)", size=16, expand=True)]),
                Row([self.hypertriglyceridemia_icon, Text("Гипертриглицеридемия", size=16, expand=True)]),
                Row([self.prediabetes_icon, Text("Предиабет", size=16)]),
                Text("Наличие заболеваний", size=18, bgcolor=Colors.AMBER_200, color=Colors.BLACK_87),
                Row([self.diabetes_sec_type_icon, Text("Сахарный диабет 2-го типа", size=16, expand=True)]),
                Row([self.cad_icon, Text("ИБС. Стабильная стенокардия", size=16, expand=True)]),
                Row([self.cad_mi_icon, Text("ИБС. Перенесенный острый коронарный синдром", size=16, expand=True)]),
                Row([self.chf_icon, Text("ХСН", size=16)]),
                Row([self.stent_bypass_icon, Text("Стентирование и/или шунтирование в анамнезе", size=16, expand=True)]),
                Row([self.stroke_or_ministroke_icon, Text("Острое нарушение мозгового кровообращения\nили Транзиторная ишемическая атака в анамнезе", size=16, expand=True)]),
                Row([self.periph_art_dis_icon, Text("Заболевания периферических артерий", size=16, expand=True)]),
                Text("Стадирование по CMDS (Cadriometabolic Disease Staging)", size=18, bgcolor=Colors.AMBER_200, color=Colors.BLACK_87),
                self.cmds_type_text
            ], 
            alignment=MainAxisAlignment.START
        )

    def display_result(self, value: bool, icon_r: Icon) -> None:
        """Updates icon color and shape based on evaluation flag state."""
        icon_r.icon = Icons.CHECK_CIRCLE if value else Icons.CANCEL
        icon_r.color = Colors.RED if value else Colors.GREEN
        self.update()

    def display_cmds(self, value: bool, text: str) -> None:
        """Updates and toggles visibility of the stage description text."""
        if value and text:
            self.cmds_type_text.value = text    
            self.cmds_type_text.visible = True 
        else:
            self.cmds_type_text.visible = False 
        self.update()

    def update_from_domain_result(self, result: CMDSResult) -> None:
        """Populates UI icons and result text using calculated CMDSResult dataclass."""
        self.display_result(result.is_obesity, self.ab_ob_icon)
        self.display_result(result.is_high_blood_pressure, self.high_bl_pr_icon)
        self.display_result(result.is_hypertension, self.hyp_icon)
        self.display_result(result.is_antihyp_therapy, self.anti_h_th_icon)
        self.display_result(result.is_cholesterol_low, self.hs_lpvp_icon)
        self.display_result(result.is_hypo_lipid_therapy, self.hyp_lip_th_icon)
        self.display_result(result.is_hypertriglyceridemia, self.hypertriglyceridemia_icon)
        self.display_result(result.is_prediabetes, self.prediabetes_icon)
        
        self.display_result(result.is_diabetes, self.diabetes_sec_type_icon)
        self.display_result(result.is_cad, self.cad_icon)
        self.display_result(result.is_cad_mi, self.cad_mi_icon)
        self.display_result(result.is_chf, self.chf_icon)
        self.display_result(result.is_stenting_bypass, self.stent_bypass_icon)
        self.display_result(result.is_stroke_or_ministroke, self.stroke_or_ministroke_icon)
        self.display_result(result.is_periph_artery_dis, self.periph_art_dis_icon)
        
        self.display_cmds(True, result.cmds_stage_text)

    def clear_view(self) -> None:
        """Resets view indicators and clears stage text."""
        icons = [
            self.ab_ob_icon, self.high_bl_pr_icon, self.hyp_icon, 
            self.anti_h_th_icon, self.hs_lpvp_icon, self.hyp_lip_th_icon, 
            self.hypertriglyceridemia_icon, self.prediabetes_icon, 
            self.diabetes_sec_type_icon, self.cad_icon, self.cad_mi_icon, 
            self.chf_icon, self.stent_bypass_icon, self.stroke_or_ministroke_icon, 
            self.periph_art_dis_icon
        ]
        for icon in icons:
            icon.icon = Icons.CIRCLE
            icon.color = Colors.GREY
            
        self.cmds_type_text.value = ""
        self.cmds_type_text.visible = False
        self.update()