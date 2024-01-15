import PySimpleGUI as sg
import os

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Clock singal')],
            [sg.Text("Switches")],
            [sg.Text("LEDs")],
            [sg.Text("7 segment display")],
            [sg.Text("Buttons")],
            [sg.Button('Ok'), sg.Button('Cancel')] 
         ]

if not os.path.exists("output"):
    os.makedirs("output")

with open("output/constraints.xdc", "w") as file:
    file.write("This is a new text file.\n")
    file.write("line 2")
    file.close()


# Create the Window
window = sg.Window('Python constrainsfile creator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()