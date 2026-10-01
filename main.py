import os

from nicegui import ui

encendido = False


def cambiar_estado():
    global encendido
    encendido = not encendido

    if encendido:
        estado.text = "Estado actual: Encendido"
        estado.style("color: green; font-size: 24px")
        boton.set_text("Apagar")
        boton.props("color=green")
    else:
        estado.text = "Estado actual: Apagado"
        estado.style("color: red; font-size: 24px")
        boton.set_text("Encender")
        boton.props("color=red")


with ui.column().classes("w-full h-screen items-center justify-center"):
    with ui.card().style("width:300px; background-color:blue;").classes("items-center"):
        ui.label("Mi Primera App").style("font-size: 24px; font-weight: bold")

        ui.image("nice.png").style("width:250px")

        estado = ui.label("Estado actual: Apagado").style("color: red; font-size: 24px")

        boton = ui.button(
            "Encender", icon="lightbulb", color="red", on_click=cambiar_estado
        ).style("color: white")

ui.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
