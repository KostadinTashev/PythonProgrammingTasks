input_temperature = input()
if 'F' in input_temperature:
    input_temperature = float(input_temperature[:-1])
    print(round((input_temperature - 32) * 5 / 9))
elif 'C' in input_temperature:
    input_temperature = float(input_temperature[:-1])
    print(round(input_temperature * 9 / 5 + 32))
