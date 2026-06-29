<div align="center">

<!-- Logo / Banner -->
<img src="https://img.shields.io/badge/BioMark-Attendance%20System-6C63FF?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyYTUgNSAwIDAgMSA1IDUgNSA1IDAgMCAxLTUgNSA1IDUgMCAwIDEtNS01IDUgNSAwIDAgMSA1LTV6TTIgMjB2LTFjMC00LjQgMy42LTggOC04czggMy42IDggOHYxeiIvPjwvc3ZnPg==&logoColor=white" alt="BioMark" height="50"/>

# 🎭 BioMark

### Smart Biometric Attendance System

*Effortless check-ins through Face Recognition & Voice Authentication*

<br/>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22C55E?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-FF6B6B?style=flat-square)](CONTRIBUTING.md)

<br/>

[🚀 Quick Start](#-quick-start) • [📖 Docs](#-how-it-works) • [🖼 Screenshots](#-screenshots) • [🤝 Contributing](#-contributing)

</div>

---

## 🌟 What is BioMark?

**BioMark** is a dual-biometric attendance management system that replaces traditional roll calls and swipe cards with **real-time face recognition** and **voice authentication**. Designed for schools, colleges, offices, and enterprises — BioMark makes attendance marking fast, fraud-proof, and hands-free.

> No cards. No PINs. No proxies. Just your face and your voice.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎭 **Face Recognition** | Real-time identification using deep learning models |
| 🎙️ **Voice Authentication** | Speaker verification to prevent proxy attendance |
| 🔐 **Dual-Layer Security** | Both biometrics must match for successful check-in |
| 📊 **Live Dashboard** | Instant attendance reports and analytics |
| 📁 **Auto Export** | Attendance logs saved to CSV / Excel automatically |
| 🌐 **Web Interface** | Browser-based admin panel for managing users & reports |
| ☁️ **Cloud Ready** | Optional cloud sync for multi-campus or remote teams |
| 📱 **Notifications** | Email/SMS alerts for absent or late members |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────┐
│                   BioMark System                │
│                                                 │
│  ┌──────────┐    ┌────────────────────────┐     │
│  │  Camera  │───▶│  Face Detection Module  │     │
│  └──────────┘    │  (OpenCV + dlib/FaceNet)│     │
│                  └──────────┬─────────────┘     │
│  ┌──────────┐              │                    │
│  │Microphone│───▶  ┌───────▼──────────────┐     │
│  └──────────┘      │  Biometric Validator  │     │
│                    │  (Face + Voice Match) │     │
│  ┌──────────┐      └───────┬──────────────┘     │
│  │  Voice   │───▶          │                    │
│  │  Module  │      ┌───────▼──────────────┐     │
│  └──────────┘      │   Attendance Engine   │     │
│                    │   (Log + Export)      │     │
│                    └───────┬──────────────┘     │
│                            │                    │
│                    ┌───────▼──────────────┐     │
│                    │    Dashboard / DB    │     │
│                    └──────────────────────┘     │
└─────────────────────────────────────────────────┘
```

---

## ⚙️ How It Works

### Step 1 — Enrollment (One-time Setup)
The user registers by:
- 📸 Capturing **multiple face angles** (front, left, right, up, down)
- 🎙️ Recording a **voice passphrase** (e.g., "My name is [Name]")
- 🗂️ Profiles are encoded and stored securely in the local database

### Step 2 — Daily Attendance
1. User stands in front of the camera
2. System **detects and identifies the face** in real time
3. User **speaks a passphrase** for voice verification
4. On **dual match** → attendance is marked ✅
5. On failure → access is denied and flagged 🚫

### Step 3 — Reporting
- Attendance auto-saves to `attendance_logs/` as `.csv`
- Dashboard shows daily/weekly/monthly stats
- Export reports with one click

---

## 🛠️ Tech Stack

### Core
| Component | Technology |
|---|---|
| Language | Python 3.1+ |
| Face Detection |  `dlib`, `face_recognition` |
| Face Embedding | FaceNet / DeepFace |
| Voice Recognition | `SpeechRecognition`, `pyaudio` |
| Speaker Verification | Resemblyzer / MFCC features |
| Database | Supabase |



## 🔒 Privacy & Security

- ✅ All biometric data is **stored locally** — no data sent to external servers by default
- ✅ Face encodings are **one-way hashed** numerical vectors, not raw images
- ✅ Voice embeddings are **non-reversible** feature vectors
- ✅ Database is **encrypted at rest** (optional AES-256)
- ✅ Compliant with basic **GDPR / PDPA** principles (data minimization, consent-based enrollment)
- ✅ Admin-only access to logs and user management

> ⚠️ It is the deployer's responsibility to inform users about biometric data collection and obtain proper consent.

---



## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting PRs.




<div align="center">

Made with ❤️ by the **Sonu kumar yadav**

⭐ Star this repo if BioMark helped you!

[🐛 Report Bug](issues) • [💡 Request Feature](issues) • [📧 Contact](mailto:your@email.com)

</div>
