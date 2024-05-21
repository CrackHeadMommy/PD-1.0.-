import PySimpleGUI as sg
from preces import product as prod
from functions import add, remove

layoutMain = [
    [sg.Text("Izvelne")],
    [sg.Button("Pievienot Lietas"), sg.Button("Rediget Inventaru")],
    [sg.Button("Izslegt")]
]

layoutInput = [
    [sg.Text("Preces pievienošana:")],
    [sg.Text("Nosaukums: "), sg.InputText(key="name")],
    [sg.Text("Skaits: "), sg.InputText(key="amountA")],
    [sg.Text("Tips: "), sg.Radio("Detaļa", group_id="add", default=True, key="detala"), sg.Radio("Programmatūra", group_id="add", key="programma")],
    [sg.Button("Pievienot")],
    [sg.Button("Atpakal")]
]

layoutOutput = [
    [sg.Listbox(values=[], key="output", size=(60, 20))],
    [sg.Button("Nonemt"), sg.InputText(key="amountR"), sg.InputText(key="nameR")],
    [sg.Button("Atpakal.")]
]

layout = [
    [sg.Column(layoutMain, key="Main"), sg.Column(layoutInput, visible=False, key="Input"), sg.Column(layoutOutput, visible=False, key="Output")]
]

window = sg.Window('Uzskaititajs', layout)

Stack = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Izslegt':
        break

    if event == "Pievienot Lietas":
        window['Input'].update(visible=True)
        window['Main'].update(visible=False)

    if event == "Rediget Inventaru":
        window['Output'].update(visible=True)
        window['Main'].update(visible=False)

    if event == "Atpakal":
        window['Input'].update(visible=False)
        window['Main'].update(visible=True)

    if event == "Atpakal.":
        window['Output'].update(visible=False)
        window['Main'].update(visible=True)

    if event == "Pievienot":
        item = prod(values["name"], values["amountA"], values['detala'])
        Stack = add(Stack, item)

    if event == "Nonemt":
        Stack = remove(Stack, values["nameR"], values["amountR"])

    list_display = []
    for product in Stack:
        if product.amount != 0:
            list_display.append(f"{product.amount} preces \"{product.name}\" kas ir {product.typ()}")

    window["output"].update(values=list_display)

window.close()
