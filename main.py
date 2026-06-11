from monitor import get_connections
from detector import calculate_risk
from logger import save_log
from alerts import generate_alert

connections = get_connections()

rows = []

total = 0
safe = 0
medium = 0
high = 0

for conn in connections:

    total += 1

    risk = calculate_risk(conn["port"])

    if risk == "SAFE":
        safe += 1

    elif risk == "MEDIUM":
        medium += 1

    elif risk == "HIGH":
        high += 1

    generate_alert(
        conn["process"],
        conn["ip"],
        conn["port"],
        risk
    )

    rows.append([
        conn["process"],
        conn["ip"],
        conn["port"],
        risk
    ])

    print(f"Process: {conn['process']}")
    print(f"IP: {conn['ip']}")
    print(f"Port: {conn['port']}")
    print(f"Risk: {risk}")
    print("-" * 50)

save_log(rows)

print("\nSUMMARY")
print("-" * 30)
print(f"Total Connections: {total}")
print(f"Safe Connections: {safe}")
print(f"Medium Risk: {medium}")
print(f"High Risk: {high}")