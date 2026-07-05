# ZLAPS - Phone Communication System for Metropolitan Urban Communities

[![Repository](https://img.shields.io/badge/repo-askforkris90%2Fzlaps-blue)](https://github.com/askforkris90/zlaps)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)

Affordable phone communication system combining frequency-based dialing with text messaging. Designed for metropolitan urban communities with wireless download support for mobile devices.

## 🎯 Features

- **Frequency-Based Dialing** - Uses audio frequencies (20-250 Hz) instead of traditional signals
- **Text Messaging** - Full messaging with conversation history tracking
- **Low-Sound Mode** - Optimized for low-frequency communication patterns
- **Hybrid Communication** - Combine frequency dialing and text simultaneously
- **Back-and-Forth Conversations** - Simulate multi-turn communication exchanges
- **Wireless Download** - Download to mobile/wireless devices
- **Mobile Optimization** - Android, Linux, custom device support
- **Minimal Footprint** - ~19 KB total size for wireless distribution
- **No iOS Dependencies** - Completely independent, no Apple platform requirements

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- NumPy library

### Quick Install

```bash
# Clone repository
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip install -r requirements.txt

# Verify installation
python examples.py
```

### Wireless Download for Mobile Devices

**Android (via Termux):**
```bash
pkg install python3 python3-pip
pip install numpy
git clone https://github.com/askforkris90/zlaps.git
cd zlaps
python3 communication_core.py
```

**Linux/Raspberry Pi:**
```bash
python3 -m pip install -r requirements.txt
python3 communication_core.py
```

See [INSTALL.md](INSTALL.md) for detailed setup instructions.

## 🚀 Quick Start

```python
from communication_core import CommunicationCore

# Create communication endpoint
comm = CommunicationCore(user_id="yourname", low_sound_mode=True)

# Dial out using frequency signals
comm.dial_out(recipient="loretta", number_sequence="555-1234")

# Send text message
comm.send_text(recipient="loretta", message_content="Hey, can you hear me?")

# Receive message
comm.receive_text(sender="loretta", message_content="Yes, loud and clear!")

# View conversation
print(comm.get_conversation_history("loretta"))
```

## 📚 Usage Examples

### Example 1: Basic Frequency Dialing

```python
from communication_core import CommunicationCore

comm = CommunicationCore(user_id="user1", low_sound_mode=True)

# Dial out
result = comm.dial_out(recipient="loretta", number_sequence="555-1234")
print(f"Status: {result['status']}")
print(f"Signal length: {result['signal_length']} samples")
```

### Example 2: Send & Receive Text

```python
# Send text
comm.send_text(recipient="loretta", message_content="Hello Loretta!")

# Receive text
comm.receive_text(sender="loretta", message_content="Hi there!")
```

### Example 3: Hybrid Communication

```python
# Send frequency dial + text simultaneously
comm.send_hybrid(
    recipient="loretta",
    number="555-5678",
    text="Calling with backup text"
)
```

### Example 4: Back-and-Forth Conversation

```python
exchange = comm.back_and_forth(
    recipient="loretta",
    exchange_pairs=[
        (True, "Are you there?"),
        (False, "Yes, I'm here!"),
        (True, "Great, let's talk"),
        (False, "Perfect!")
    ]
)
print(exchange['history'])
```

### Example 5: Wireless Download for Mobile

```python
from wireless_download import WirelessDownloadManager

manager = WirelessDownloadManager()
info = manager.get_download_link(device_type="mobile")

print(f"Download URL: {info['download_url']}")
print(f"File Size: {info['file_size']}")
print(f"Compatible Devices: {info['device_types']}")
```

## 📖 Module Documentation

### frequency_dialer.py
Generates audio frequency signals for phone dialing.

**Key Classes:**
- `FrequencyConfig` - Configuration for frequency generation
- `FrequencyDialer` - Main frequency signal generator

**Key Methods:**
- `generate_tone(frequency)` - Create single tone
- `dial_sequence(frequencies)` - Create sequence
- `dial_out(number_sequence)` - Convert number to frequencies
- `save_audio(signal, filename)` - Export to WAV

### text_handler.py
Manages text messaging and conversation tracking.

**Key Classes:**
- `Message` - Individual message representation
- `TextHandler` - Messaging system manager

**Key Methods:**
- `create_message()` - Send message
- `receive_message()` - Record inbound
- `get_conversation()` - Retrieve history
- `format_conversation()` - Display conversation

### communication_core.py
Main orchestration combining frequency dialing and text messaging.

**Key Class:**
- `CommunicationCore` - Main communication coordinator

**Key Methods:**
- `dial_out()` - Frequency dial
- `send_text()` - Send message
- `send_hybrid()` - Both simultaneously
- `receive_text()` - Get message
- `back_and_forth()` - Multi-turn conversation
- `get_conversation_history()` - View history

### wireless_download.py
Package and distribute to wireless/mobile devices.

**Key Classes:**
- `WirelessPackage` - Downloadable package container
- `WirelessDownloadManager` - Distribution manager
- `MobileOptimizer` - Transmission optimization

**Key Methods:**
- `create_wireless_package()` - Build package
- `get_download_link()` - Get download info
- `verify_download()` - Check integrity
- `log_download()` - Track downloads

## 🔧 Technical Specifications

| Spec | Value |
|------|-------|
| Sample Rate | 44,100 Hz |
| Frequency Range | 20-250 Hz |
| Low-Sound Mode | 20-120 Hz |
| Tone Duration | 1.0 second per digit |
| Amplitude | 0.7 (normalized) |
| Audio Format | WAV (mono, 16-bit) |
| Total Package Size | ~19 KB |
| Python Version | 3.7+ |
| Dependencies | NumPy |

## 📱 Wireless Distribution

ZLAPS supports wireless download to:
- **Android** (Termux, Python IDE, custom apps)
- **Linux** (Desktop, Raspberry Pi, BeagleBone)
- **Custom Wireless Devices** (Any with Python 3.7+)
- **IoT Devices** (Edge computing platforms)

### Download Process

1. Get package: `https://github.com/askforkris90/zlaps/releases`
2. Verify checksum for integrity
3. Extract modules
4. Install NumPy dependency
5. Initialize CommunicationCore

### File Sizes (Wireless Optimized)
- frequency_dialer.py: ~5 KB
- text_handler.py: ~3 KB
- communication_core.py: ~5 KB
- wireless_download.py: ~6 KB
- **Total: ~19 KB**

## 🔒 Security & Integrity

Each wireless package includes:
- SHA-256 checksum for integrity verification
- Device compatibility checking
- Version tracking
- Download logging

```python
# Verify downloaded package
manager = WirelessDownloadManager()
is_valid = manager.verify_download(package_id, checksum)
```

## 🎨 Use Cases

- **Metropolitan Urban Communication** - Affordable phone connectivity
- **Low-Bandwidth Networks** - Minimal data footprint
- **Emergency Communication** - Backup messaging system
- **Community Networks** - Local frequency-based communication
- **IoT Communication** - Device-to-device messaging
- **Educational** - Learning frequency modulation and networking

## 📝 Configuration

### Low-Sound Mode
```python
# Enable for "low sound friends" - uses 20-120 Hz range
comm = CommunicationCore(user_id="me", low_sound_mode=True)
```

### Custom Frequency Range
```python
from frequency_dialer import FrequencyConfig, FrequencyDialer

config = FrequencyConfig()
config.low_freq_range = (50, 150)  # Custom range
dialer = FrequencyDialer(config)
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| NumPy not found | `pip install numpy` |
| Can't import modules | Ensure all .py files in same directory |
| Audio not playing | Use `save_audio()` to export WAV |
| Wireless download slow | Use minified version (50-70% smaller) |
| Checksum mismatch | Re-download and verify integrity |

## 📋 Requirements

See `requirements.txt`:
```
numpy>=1.19.0
```

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Submit pull request

## 📞 Support

- **Repository**: https://github.com/askforkris90/zlaps
- **Issues**: https://github.com/askforkris90/zlaps/issues
- **Documentation**: See INSTALL.md and README.md

## 🌍 Community

Designed for metropolitan urban communities. ZLAPS provides affordable, low-bandwidth communication for communities worldwide.

---

**No iOS Dependencies** | **Mobile Optimized** | **Urban Focused** | **Open Source**
