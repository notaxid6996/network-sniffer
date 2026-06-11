def generate_alert(process, ip, port, risk):

    if risk == "HIGH":

        print("\n" + "=" * 50)
        print("ALERT! HIGH RISK CONNECTION DETECTED")
        print(f"Process: {process}")
        print(f"IP: {ip}")
        print(f"Port: {port}")
        print(f"Risk: {risk}")
        print("=" * 50)