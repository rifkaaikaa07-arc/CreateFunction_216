def convert_temperature(value, unit):
    """Konversi suhu Celsius <-> Fahrenheit"""
    if unit == 'C':
        return (value * 9 / 5) + 32
    elif unit == 'F':
        return (value - 32) * 5 / 9
    else:
        return "Unit tidak valid, gunakan 'C' atau 'F'"

print(convert_temperature(100, 'C')) 
print(convert_temperature(212, 'F'))   
print(convert_temperature(37, 'C'))  