# ZLAPS — Frequency-Based Phone Communication

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](#) [![CI](https://img.shields.io/badge/ci-pending-lightgrey)](#)

ZLAPS is a lightweight Python library that demonstrates frequency-based dialing combined with a simple text-messaging layer. It is designed for experimentation and low-bandwidth scenarios (community, educational, and embedded device use). This repo contains the core signal generation, messaging handlers, and helpers to prepare a small wireless/embedded distribution.

Status: alpha — experimental, educational use only.

Table of Contents
- Features
- Quick highlights
- Prerequisites
- Installation
- Quick start
- Examples
- Module overview
- Technical specs & limitations
- Wireless distribution & verification
- Troubleshooting
- Contributing & Code of Conduct
- License & Support

Features
- Frequency-based dialing (tone generation in the 20–250 Hz range)
- Text messaging with conversation history
- Low-sound mode (narrower frequency range for limited hardware)
- Hybrid communication (tones + text)
- Utilities for packaging and distributing to mobile/embedded devices

Quick highlights
- Minimal, educational implementation intended for demonstrations and research.
- Designed to be portable to Linux-based devices (including Raspberry Pi) and Termux on Android.
- Includes examples showing dialing, message exchange, and hybrid use.

Prerequisites
- Python 3.7 or newer
- pip (or pip3)
- NumPy (signal generation uses NumPy arrays)
- An audio output device for playback or a WAV writer for file export

Installation

From source (recommended for development)
```bash
git clone https://github.com/askforkris90/zlaps.git
cd zlaps
python3 -m pip install -r requirements.txt
# optionally install in editable mode for development
python3 -m pip install -e .
```

Run examples
```bash
# From project root
python3 examples.py
```

Android (Termux)
```bash
pkg update && pkg install python
pip install numpy
git clone https://github.com/askforkris90/zlaps.git
cd zlaps
python3 communication_core.py
```

Notes
- If you publish a package to PyPI, replace the source install steps with `pip install zlaps`.
- If a binary audio output is not available on your device, use the included save/export helpers to write WAV files.

Quick start (minimal, runnable example)
```python
from communication_core import CommunicationCore

# Create a communication endpoint (no network required for local examples)
comm = CommunicationCore(user_id="demo", low_sound_mode=True)

# Dial: returns metadata about the generated signal (no playback required)
result = comm.dial_out(recipient="loretta", number_sequence="555-1234")
print(result)  # e.g. {'status': 'ok', 'signal_length': 44100, ...}

# Send/receive text
comm.send_text(recipient="loretta", message_content="Hello Loretta!")
comm.receive_text(sender="loretta", message_content="Hi there!")
print(comm.get_conversation_history("loretta"))
```

Examples
- See examples.py for end-to-end demos:
  - Basic frequency dialing
  - Send & receive text
  - Hybrid communication
  - Back-and-forth exchanges

Module overview
- frequency_dialer.py — Frequency generation and tone sequencing
  - FrequencyConfig: settings for generation
  - FrequencyDialer: creates tones, sequences, and exports audio
- text_handler.py — Message model and conversation tracker
  - Message: single message object
  - TextHandler: send/receive and history management
- communication_core.py — Orchestrator combining dialing and messaging
  - CommunicationCore: primary interface used in examples
- wireless_download.py — Utilities for packaging for wireless/mobile devices
  - WirelessDownloadManager, WirelessPackage, MobileOptimizer

Technical specs & limitations
- Default sample rate: 44,100 Hz
- Frequency range (configurable): 20–250 Hz
- Low-sound mode: 20–120 Hz (device/hardware dependent)
- Tone duration (default): 1.0 second per digit (configurable)
- Audio format: WAV (mono, 16-bit) for exports
- Note on hardware: Many mobile phone speakers and small embedded speakers cannot reproduce frequencies below ~50 Hz robustly — audible result will be device-dependent.
- Size claim: the repository aims for a small footprint; do not rely on a hard-coded "~19 KB" size without measuring the actual distribution (wheel, zip, or minified script). Update this number after building the actual package.

Wireless distribution & verification
- Create a package (zip/wheel) and publish or host in a release.
- Provide SHA-256 checksums for each release artifact and include verification instructions.
- Example verification:
```bash
# compute and verify checksum
sha256sum zlaps-<version>.zip
```

Troubleshooting
- NumPy import error: `pip install numpy`
- Audio playback failure: ensure your OS has an audio output device or use save_audio() to write a WAV file and play it externally
- Termux permissions: Termux may require additional setup for audio; consider using WAV export if direct playback is unsupported
- Checksum mismatch: re-download the artifact and re-run checksum verification

Security & integrity
- Sign or provide checksums for releases
- Prefer secure channels for distributing sensitive builds; include version tracking in the package metadata

Contributing
Contributions welcome. Suggested workflow:
1. Fork the repository
2. Create a feature branch (git checkout -b feat/your-feature)
3. Add tests and update docs
4. Open a pull request describing your changes

Please add a CONTRIBUTING.md and CODE_OF_CONDUCT.md if you accept community contributions.

License
MIT — see LICENSE for full text.

Support & contact
- Repo: https://github.com/askforkris90/zlaps
- Issues: https://github.com/askforkris90/zlaps/issues

Acknowledgements
- Designed for educational and experimental use in community and low-bandwidth scenarios.
