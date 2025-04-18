# Raspberry Pi Docker Stack

This project defines a containerized monitoring and utility stack across two Raspberry Pis (`pi-4b` and `pi-5`). Each Pi runs services specific to its role in the system, managed via Docker Compose.

---

## 🧱 Architecture Overview

- **Pi 4B**: Primary monitoring hub, hosting system metrics, a PostgreSQL instance, a Flask-based Wake-on-LAN API, and dashboards via Grafana.
- **Pi 5**: Media and utility server hosting Plex, Transmission, FileBrowser, and Heimdall.

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

## 🍍 Pi 5 — Services Overview

Path: [`raspberry-pi-5/`](./raspberry-pi-5)

### 📦 Services

| Service         | Description                                                                  |
|-----------------|------------------------------------------------------------------------------|
| `plex`          | Media server for streaming your TV shows and movies                          |
| `transmission`  | BitTorrent client with a web UI for downloading content                       |
| `filebrowser`   | Simple file manager with a web interface for browsing and managing files      |
| `heimdall`      | Personal start page to manage and launch your other services                  |

---

## ⚙️ Configuration

### 📁 Environment Variables

Copy the example environment file and populate it with your own values:

```bash
cp raspberry-pi-5/sample.env raspberry-pi-5/.env
```

Then edit `.env` to match your setup:

```dotenv
# Common
PUID=1000
PGID=1000
TZ=Pacific/Auckland

# Media directories
MEDIA_TV_DIR=/mnt/unitek/storage/Tv
MEDIA_MOVIES_DIR=/mnt/unitek/storage/Movies
MEDIA_INCOMPLETE_DIR=/mnt/unitek/storage/transmission/incomplete

# Transmission credentials
TRANS_USER=transmission
TRANS_PASS=FwhUmqW55C59

# Optional port overrides
FILEBROWSER_PORT=8081
HEIMDALL_PORT=81
```

---

## 🚀 Running Pi 5 Stack

To build and run the `pi-5` stack:

```bash
cd raspberry-pi-5
docker compose up -d --build
```

This will:
- Load environment variables from `.env`
- Start Plex, Transmission, FileBrowser, and Heimdall

---

## 📊 Accessing Services

| Service        | URL                            |
|----------------|--------------------------------|
| Plex           | http://<pi5-ip>:32400/web      |
| Transmission   | http://<pi5-ip>:9091           |
| FileBrowser    | http://<pi5-ip>:8081           |
| Heimdall       | http://<pi5-ip>:81             |

Replace `<pi5-ip>` with the IP address or Tailscale domain of your Pi 5.

---

## 🧼 Maintenance & Updating

To update either stack after pulling Git changes:

```bash
cd raspberry-pi-4   # or raspberry-pi-5
git pull
docker compose down
docker compose up -d --build
```

---