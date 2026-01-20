gender = input("Enter biological gender (female/male): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin > 155:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin > 167:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")

else:
    print("Invalid gender entered.")
