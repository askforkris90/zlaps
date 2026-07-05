# ZLAPS Installation Guide

Complete setup instructions for different platforms.

## Quick Start (All Platforms)

```bash
# Clone repository
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip install -r requirements.txt

# Verify installation
python examples.py
```

## Platform-Specific Installation

### Windows

```bash
# Install Python 3.7+
# Download from https://www.python.org/

# Clone and setup
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip install -r requirements.txt

# Run examples
python examples.py
```

### macOS

```bash
# Using Homebrew (recommended)
brew install python3

# Clone and setup
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip3 install -r requirements.txt

# Run examples
python3 examples.py
```

### Linux (Ubuntu/Debian)

```bash
# Install Python 3.7+
sudo apt-get install python3 python3-pip

# Clone and setup
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip3 install -r requirements.txt

# Run examples
python3 examples.py
```

### Raspberry Pi

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install Python and pip
sudo apt-get install python3 python3-pip

# Clone and setup
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip3 install -r requirements.txt

# Run examples
python3 examples.py
```

### Android (Termux)

```bash
# Install Termux from Play Store

# In Termux:
pkg update
pkg install python3 python3-pip

# Clone and setup
git clone https://github.com/askforkris90/zlaps.git
cd zlaps

# Install dependencies
pip install -r requirements.txt

# Run examples
python examples.py
```

## Wireless Download Installation

### Method 1: Direct Download

1. Download the latest release from GitHub
2. Extract the files
3. Run `pip install -r requirements.txt`
4. Execute `python examples.py`

### Method 2: Package Manager

```bash
pip install zlaps
```

### Method 3: Development Install

```bash
git clone https://github.com/askforkris90/zlaps.git
cd zlaps
pip install -e .
```

## Troubleshooting

### Issue: `pip: command not found`

**Solution:** Use `pip3` instead on Linux/macOS:
```bash
pip3 install -r requirements.txt
```

### Issue: `No module named 'numpy'`

**Solution:** Install NumPy:
```bash
pip install numpy
```

### Issue: `ModuleNotFoundError: No module named 'communication_core'`

**Solution:** Ensure all `.py` files are in the same directory:
```bash
ls *.py
# Should show: communication_core.py, frequency_dialer.py, text_handler.py, wireless_download.py
```

### Issue: Audio output not playing

**Solution:** Export to WAV file instead:
```python
from frequency_dialer import FrequencyDialer

dialer = FrequencyDialer()
result = dialer.dial_out("555-1234")
dialer.save_audio(result['signal'], "output.wav")
```

### Issue: Slow wireless download

**Solution:** Use the minified version (50-70% smaller):
```bash
python -m compileall .
```

### Issue: Checksum mismatch

**Solution:** Re-download and verify:
```bash
rm requirements.txt
git pull origin main
pip install -r requirements.txt
```

## Verifying Installation

```bash
# Test basic import
python -c "from communication_core import CommunicationCore; print('OK')"

# Run full test suite
python examples.py

# Check version
python -c "import sys; print(f'Python {sys.version}')"
python -c "import numpy; print(f'NumPy {numpy.__version__}')"
```

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.7 | 3.9+ |
| NumPy | 1.19.0 | Latest |
| RAM | 256 MB | 512 MB+ |
| Disk | 50 MB | 100 MB |

## Support

- **Issues:** https://github.com/askforkris90/zlaps/issues
- **Documentation:** See README.md
- **Examples:** Run `python examples.py`
