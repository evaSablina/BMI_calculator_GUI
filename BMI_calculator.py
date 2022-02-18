import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")

# main code
def calculate_bmi():
    weight = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(weight / height ** 2)

    if bmi < 18.5:
        label_result['text'] = f'Your BMI is {bmi}, you are underweight.'
    elif bmi < 25:
        label_result['text'] = f'Your BMI is {bmi}, you have a normal weight.'
    elif bmi < 30:
        label_result['text'] = f'Your BMI is {bmi}, you are slightly overweight.'
    elif bmi < 35:
        label_result['text'] = f'Your BMI is {bmi}, you are obese.'
    else:
        label_result['text'] = f'Your BMI is {bmi}, you are clinically obese.'


# Create GUI

label_height = tkinter.Label(root, text="Height, m: ")
label_height.grid(column=0, row=0)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=0)


label_kg = tkinter.Label(root, text="Weight, kg: ")
label_kg.grid(column=0, row=1)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Calculate: ", command=calculate_bmi)
button_calculate.grid(column=0, row=2)


label_result = tkinter.Label(root, text="BMI: ")
label_result.grid(column=1, row=2)


"""Позволяет главному окну не закрываться"""
root.mainloop()
