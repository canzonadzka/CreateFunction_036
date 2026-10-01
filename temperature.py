def convert (value, unit) :
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9 
    else:
        print("tidak ada unit yang sesuai")
        