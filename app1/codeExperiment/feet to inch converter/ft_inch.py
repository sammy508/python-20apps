import PySimpleGUI as sg
from converter import converter



label1 = sg.Text("Enter feet")
input1 = sg.InputText(tooltip="enter", key= 'feet')

label2 = sg.Text("Enter inches")
input2 = sg.InputText(tooltip="enter",key='inch')

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Converter", layout=[
    [label1,input1], [label2, input2], [button],[output_label]
])

while True:
    event,value = window.read()
    feet = float(value['feet'])
    inches = float(value['inch'])

    result = converter(feet,inches)

    window["output"].update(value=f"{result} meter")
    

    break
window.read()
print(converter)
window.close()

