import tkinter as tk
from tkinter import ttk

#root window
window = tk.Tk()
window.geometry('500x500')

#app container
appContainer = tk.Frame()
appContainer.grid_columnconfigure(0, weight=1)
appContainer.grid_columnconfigure(1, weight=1)
appContainer.grid_rowconfigure(0, weight=1)
appContainer.grid_rowconfigure(1, weight=1)

#frames
#Description Frame
jobDescFrame = tk.Frame(appContainer)
jobDescFrame.grid(row=0,column=0,sticky='w')


#labels
#Description Frame
jobNameLabel = tk.Label(jobDescFrame,
                        text = 'Job Name: ')
jobNameLabel.grid(column=0,row=0,sticky='e')

jobNumLabel = tk.Label(jobDescFrame,
                        text = 'Job Number: ')
jobNumLabel.grid(column=0,row=1,sticky='e')

jobProjEngLabel = tk.Label(jobDescFrame,
                        text = 'Project Engineer: ')
jobProjEngLabel.grid(column=0,row=2,sticky='e')

jobAutoEngLabel = tk.Label(jobDescFrame,
                        text = 'Automation Engineer: ')
jobAutoEngLabel.grid(column=0,row=3,sticky='e')

jobRTU1Label = tk.Label(jobDescFrame,
                        text = 'RTU1: ')
jobRTU1Label.grid(column=0,row=4, sticky='e')

jobRTU2Label = tk.Label(jobDescFrame,
                        text = 'RTU2: ')
jobRTU2Label.grid(column=0,row=5,sticky='e')


#entrys
#Description Frame

jobNameEntry = tk.Entry(jobDescFrame)
jobNameEntry.grid(column=1, row=0)

jobNumEntry = tk.Entry(jobDescFrame)
jobNumEntry.grid(column=1, row=1)

jobProjEngEntry = tk.Entry(jobDescFrame)
jobProjEngEntry.grid(column=1, row=2)

jobAutoEngEntry = tk.Entry(jobDescFrame)
jobAutoEngEntry.grid(column=1, row=3)


#comboboxes
#Description Frame
RTU1Combobox = ttk.Combobox(jobDescFrame,
                            values=
                            ['3555',
                            '3350',
                            '3530',
                            'Other'],
                            width=10
                            )
RTU1Combobox.grid(column=1,row=4,sticky='w')

RTU2Combobox = ttk.Combobox(jobDescFrame,
                            values=
                            ['3555',
                            '3350',
                            '3530',
                            'Other',
                            'None'],
                            width=10)

RTU2Combobox.grid(column=1,row=5,sticky='w')


#event handlers
#Description Frame



#main loop
appContainer.pack(fill='both')
window.mainloop()

