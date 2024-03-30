print("Fahrenheit\tCelsius")
for celsius in range(0, 151, 10): 
    fahrenheit = (celsius * 9/5) + 32
    print(f"{fahrenheit}\t\t{celsius:.1f}")
