import PySimpleGUI as sg



label1 = sg.Text("Enter feet")
input1 = sg.InputText(tooltip="enter")

label2 = sg.Text("Enter inches")
input2 = sg.InputText(tooltip="enter")

button = sg.Button("Convert")

window = sg.Window("Converter", layout=[
    [label1,input1], [label2, input2], [button]
])

window.read()
window.close()

