from flask import Flask, render_template, send_file
from monitor import get_connections, is_external
from detector import calculate_risk
from report_generator import generate_pdf

app = Flask(__name__)


@app.route("/")
def home():

    connections = get_connections()

    external_connections = []

    for conn in connections:

        if is_external(conn["ip"]):
            external_connections.append(conn)

    external_count = len(external_connections)

    total = len(connections)

    safe = 0
    medium = 0
    high = 0

    alerts = []

    for conn in connections:

        risk = calculate_risk(
            conn["port"]
        )

        conn["risk"] = risk

        if risk == "SAFE":

            safe += 1

        elif risk == "MEDIUM":

            medium += 1

        elif risk == "HIGH":

            high += 1

            if len(alerts) < 5:

                alerts.append({
                    "process": conn["process"],
                    "port": conn["port"]
                })

    if total > 0:

        threat_score = int(
            ((medium * 30) + (high * 100))
            / total
        )

    else:

        threat_score = 0

    return render_template(
        "index.html",
        total=total,
        safe=safe,
        medium=medium,
        high=high,
        external_count=external_count,
        threat_score=threat_score,
        alerts=alerts,
        connections=connections
    )


@app.route("/pdf")
def pdf_report():

    connections = get_connections()

    total = len(connections)

    safe = 0
    medium = 0
    high = 0

    for conn in connections:

        risk = calculate_risk(
            conn["port"]
        )

        if risk == "SAFE":
            safe += 1

        elif risk == "MEDIUM":
            medium += 1

        elif risk == "HIGH":
            high += 1

    if total > 0:

        threat_score = int(
            ((medium * 30) + (high * 100))
            / total
        )

    else:

        threat_score = 0

    generate_pdf(
        total,
        safe,
        medium,
        high,
        threat_score
    )

    return send_file(
        "Network_Report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":

    import threading
    import webbrowser

    def open_browser():

        webbrowser.open(
            "http://127.0.0.1:5000"
        )

    threading.Timer(
        1,
        open_browser
    ).start()

    app.run(
        debug=True
    )