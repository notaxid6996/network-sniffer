import psutil
import socket


def detect_application_protocol(port):

    protocols = {
        80: "HTTP",
        443: "HTTPS",
        53: "DNS",
        22: "SSH",
        21: "FTP",
        25: "SMTP",
        110: "POP3",
        143: "IMAP",
        3306: "MySQL",
        5432: "PostgreSQL"
    }

    return protocols.get(
        port,
        "UNKNOWN"
    )


def is_external(ip):

    return not (
        ip.startswith("127.") or
        ip.startswith("192.168.") or
        ip.startswith("10.") or
        ip.startswith("172.")
    )


def get_connections():

    connections_data = []

    for conn in psutil.net_connections(
        kind="inet"
    ):

        try:

            if conn.raddr:

                process_name = "System Connection"
                pid = conn.pid

                if conn.pid:

                    try:

                        process = psutil.Process(
                            conn.pid
                        )

                        process_name = (
                            process.name()
                        )

                    except psutil.AccessDenied:

                        process_name = (
                            f"System PID {conn.pid}"
                        )

                    except psutil.NoSuchProcess:

                        process_name = (
                            f"Closed PID {conn.pid}"
                        )

                    except:

                        process_name = (
                            f"PID {conn.pid}"
                        )

                protocol = "UNKNOWN"

                if conn.type == socket.SOCK_STREAM:
                    protocol = "TCP"

                elif conn.type == socket.SOCK_DGRAM:
                    protocol = "UDP"

                connections_data.append({

                    "process": process_name,

                    "pid": pid,

                    "ip": conn.raddr.ip,

                    "port": conn.raddr.port,

                    "status": conn.status,

                    "protocol": protocol,

                    "app_protocol":
                    detect_application_protocol(
                        conn.raddr.port
                    )

                })

        except:
            pass

    return connections_data