
def convert_dms_to_dd(reference, dms_dict):
    
    if reference == "S" or reference == "W":
        reference = -1
    else:
        reference = 1
        
    degree = dms_dict["D"]
    minute = dms_dict["M"]
    second = dms_dict["S"]
    frac_second = second - int(second)

    return reference * (degree + minute / 60 + second / 3600 + frac_second / 36000)

# example use: convert_dms_to_dd("N", {"S": 55.55, "M": 22.22, "D": 33.33})
