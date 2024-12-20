def sort(width, height, length, mass):
    # Calculate the volume of the package (in cm³)
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Sorting logic based on the criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"