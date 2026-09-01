import flet as ft
from flet import (Container, Page, Text, Row, ResponsiveRow, 
                  ScrollMode, ThemeMode, Brightness, 
                  IconButton, Icons, Alignment, MainAxisAlignment)

from presentation import Calculator, Result


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
    page.title = 'Калькулятор расчета кардиометаболического риска по Cardiometabolic Disease Staging (CMDS)'
    page.theme_mode = ThemeMode.SYSTEM
    
    is_dark = page.platform_brightness == Brightness.DARK
    page.scroll = ScrollMode.AUTO
    
    calc = Calculator()
    res = Result()
    
    calc.result_view = res
 
    change_theme_light_btn = IconButton(
        icon=Icons.LIGHT_MODE,
        on_click=change_theme_func,
        tooltip="Изменить тему"
    )

    change_theme_dark_btn = IconButton(
        icon=Icons.DARK_MODE,
        on_click=change_theme_func,
        tooltip="Изменить тему"
    )

    sources = Container(
        content=Text(
            """При составлении калькулятора использовались источники:
1.	The progression of cardiometabolic disease: Validation of a new cardiometabolic disease staging system applicable to obesity / F. Guo, D. R. Moellering, W. T. Garvey, 2014; 
2.	Концепция новых национальных клинических рекомендаций по ожирению / Е. В. Шляхто, С. В. Недогода, А. О. Конради [и др.], 2016; 
3.	Ожирение : оценка и тактика ведения пациентов. Коллективная монография / О. М. Драпкина, И. В. Самородская, М. А. Старинская [и др.], 2021]
    """,
            size=16
        )
    )
    
    row_cont = ResponsiveRow(
        controls=[
            calc, 
            res,
            Container(height=100),
            sources
        ],
        spacing=10,
        run_spacing=10
    )
    
    theme_btn = change_theme_light_btn if is_dark else change_theme_dark_btn

    page.add(
        Text(
            "Калькулятор расчета кардиометаболического риска по Cardiometabolic Disease Staging (CMDS)", 
            size=40, 
            align=Alignment(0, 1), 
            selectable=False
        ), 
        Row([theme_btn], alignment=MainAxisAlignment.CENTER),
        row_cont
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)