# 🛡️ Threat Vision - Network Threat Analyzer

Threat Vision is a real-time cybersecurity monitoring platform that analyzes active network connections, detects suspicious activities, classifies risks, and provides security insights through an interactive SOC-style dashboard.

## 🚀 Features

* Real-Time Network Monitoring
* Threat Detection Engine
* Risk Classification (SAFE, MEDIUM, HIGH)
* Threat Score Calculation
* Security Alert Generation
* Protocol Analysis
* Live Connection Tracking
* CSV Log Generation
* Dashboard Visualization
* Search and Filter Functionality
* Threat Activity Graph
* Exportable Reports

---

## 📌 Project Overview

Threat Vision continuously monitors active network connections and collects information such as:

* Process Name
* IP Address
* Port Number
* Network Protocol
* Application Protocol
* Connection Status

The collected information is analyzed to detect suspicious activities and classify connections into different threat levels.

---

## 🏗️ Project Structure

```text
threat_vision/
│
├── app.py
├── monitor.py
├── detector.py
├── alerts.py
├── logger.py
├── network_log.csv
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ⚙️ Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

* psutil
* csv
* threading
* webbrowser

### Visualization

* Chart.js

---

## 🔍 Working Methodology

1. Monitor active network connections.
2. Collect process, IP, and port information.
3. Analyze network protocols.
4. Detect suspicious activities.
5. Classify risks into:

* 🟢 SAFE
* 🟡 MEDIUM
* 🔴 HIGH

6. Calculate Threat Score.
7. Generate alerts.
8. Store logs in CSV format.
9. Update dashboard visualization.

---

## 📊 Dashboard Features

* Total Connections
* Safe Connections
* Medium Risk Connections
* High Risk Connections
* Threat Score
* Live Monitoring
* Security Alerts
* Threat Graph
* Search Functionality
* Activity Logs

---

## 📸 Screenshots

### Dashboard

Add your screenshots here.

```text
screenshots/
├── dashboard.png
├── threat_graph.png
├── alerts.png
└── live_monitoring.png
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/threat-vision.git
cd threat-vision
```

### Install Dependencies

```bash
pip install flask psutil
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📈 Future Scope

* AI-Based Threat Detection
* Machine Learning Models
* Intrusion Detection System Integration
* Cloud Monitoring
* Geographic IP Tracking
* Threat Intelligence Feeds
* Mobile Application
* Automated Incident Response

---

## 🎯 Objectives

* Improve network visibility.
* Detect suspicious activities.
* Generate security alerts.
* Provide real-time analytics.
* Maintain activity logs.
* Enhance cybersecurity awareness.

---

## 📚 References

* Python Documentation
* Flask Documentation
* Psutil Documentation
* Chart.js Documentation
* OWASP Security Guidelines
* NIST Cybersecurity Framework

---

## 👨‍💻 Authors

* Abhishek Soni
* Nayan Dilliwar
* Pankaj Yadav

### Guide

**Mr. Govind Singh**

Department of Information Technology
Shri Shankaracharya Technical Campus

---

## 📜 License

This project is developed for academic and educational purposes.
