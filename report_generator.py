from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    total,
    safe,
    medium,
    high,
    threat_score
):

    pdf = SimpleDocTemplate(
        "Network_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Network Threat Analyzer Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Total Connections: {total}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Safe Connections: {safe}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Medium Risk: {medium}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"High Risk: {high}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Threat Score: {threat_score}/100",
            styles["BodyText"]
        )
    )

    pdf.build(content)