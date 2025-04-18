# Raspberry Pi Docker Stack

This project defines a containerized monitoring and utility stack across two Raspberry Pis (`pi-4b` and `pi-5`). Each Pi runs services specific to its role in the system, managed via Docker Compose.

---

## 🧱 Architecture Overview

- **Pi 4B**: Primary monitoring hub, hosting system metrics, a PostgreSQL instance, a Flask-based Wake-on-LAN API, and dashboards via Grafana.
- **Pi 5**: (coming soon) Additional node-exporter metrics source and possibly auxiliary services.

---

## 🍓 Pi 4B — Services Overview

Path: [`raspberry-pi-4/`](./raspberry-pi-4)

### 📦 Services

| Service         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `flask`         | Lightweight API to remotely wake devices using Wake-on-LAN                  |
| `postgres`      | PostgreSQL 15 instance for metric or application storage                    |
| `prometheus`    | Time-series database and monitoring tool                                    |
| `node-exporter` | Exposes system-level metrics (CPU, RAM, disk, etc.) for Prometheus          |
| `alertmanager`  | Sends alerts based on Prometheus rules (e.g., via Discord webhook)          |
| `grafana`       | Visualization layer to create and view dashboards from Prometheus data      |

---

## ⚙️ Configuration

### 📁 Environment Variables

Copy the example environment file and populate it with your own values:

```bash
cp raspberry-pi-4/sample.env raspberry-pi-4/.env
```

Then edit `.env` to match your setup (e.g. MAC addresses, database credentials, webhook URLs).

```dotenv
# Example .env values

WAKE_MAC_ADDRESS=A1:A1:37:49:37:89
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=metrics
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...

# Optional overrides
FLASK_PORT=5000
GRAFANA_PORT=3000
```

---

## 🚀 Running Pi 4B Stack

To build and run the `pi-4b` stack:

```bash
cd raspberry-pi-4
docker compose up -d --build
```

This will:
- Load environment variables from `.env`
- Build the Flask image
- Start all services (Prometheus, Grafana, PostgreSQL, etc.)

---

## 📊 Accessing Services

| Service        | URL                            |
|----------------|--------------------------------|
| Flask API      | http://<pi4-ip>:5000/*         |
| Grafana        | http://<pi4-ip>:3000           |
| Prometheus     | http://<pi4-ip>:9090           |
| Alertmanager   | http://<pi4-ip>:9093           |
| Node Exporter  | http://<pi4-ip>:9100/metrics   |

Replace `<pi4-ip>` with the IP address or Tailscale domain of your Pi 4B.

---

## 🍍 Pi 5 — Coming Soon

Configuration and service details for the Pi 5 will be added here in the next update.

---

## 🧼 Maintenance & Updating

To update the stack after pulling Git changes:

```bash
cd raspberry-pi-4
git pull
docker compose down
docker compose up -d --build
```

---

## 📝 License

MIT (or your preferred license)
