def calculate_risk(port):

    safe_ports = [80, 443, 53]

    medium_ports = [
        21,
        22,
        25,
        110,
        143,
        3306
    ]

    if port in safe_ports:
        return "SAFE"

    elif port in medium_ports:
        return "MEDIUM"

    else:
        return "HIGH"