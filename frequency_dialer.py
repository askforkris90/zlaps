"""
Frequency Dialer Module - Generates audio frequency signals for phone dialing.
Uses audio frequencies (20-250 Hz) for communication instead of traditional signals.
"""

import numpy as np
from typing import List, Tuple, Dict


class FrequencyConfig:
    """Configuration for frequency generation."""
    
    def __init__(self):
        self.sample_rate = 44100  # Hz
        self.low_freq_range = (20, 250)  # Hz range for standard mode
        self.low_sound_mode_range = (20, 120)  # Hz range for low-sound mode
        self.amplitude = 0.7  # Normalized amplitude
        self.tone_duration = 1.0  # seconds per digit
        self.audio_format = "WAV"  # mono, 16-bit
        
    def get_frequency_range(self, low_sound_mode: bool = False) -> Tuple[int, int]:
        """Get the appropriate frequency range."""
        if low_sound_mode:
            return self.low_sound_mode_range
        return self.low_freq_range


class FrequencyDialer:
    """Main frequency signal generator for phone dialing."""
    
    def __init__(self, config: FrequencyConfig = None, low_sound_mode: bool = False):
        self.config = config or FrequencyConfig()
        self.low_sound_mode = low_sound_mode
        self.dial_frequencies = {
            '0': 40, '1': 50, '2': 60, '3': 70, '4': 80,
            '5': 90, '6': 100, '7': 110, '8': 120, '9': 130,
            '*': 140, '#': 150
        }
        
    def generate_tone(self, frequency: float, duration: float = None) -> np.ndarray:
        """Create a single tone at specified frequency."""
        if duration is None:
            duration = self.config.tone_duration
            
        t = np.linspace(0, duration, int(self.config.sample_rate * duration))
        signal = self.config.amplitude * np.sin(2 * np.pi * frequency * t)
        return signal.astype(np.float32)
    
    def dial_sequence(self, frequencies: List[float]) -> np.ndarray:
        """Create sequence of tones from frequency list."""
        signals = []
        for freq in frequencies:
            signals.append(self.generate_tone(freq))
            # Add small silence between tones
            silence = np.zeros(int(0.1 * self.config.sample_rate))
            signals.append(silence)
        
        return np.concatenate(signals)
    
    def dial_out(self, number_sequence: str) -> Dict:
        """Convert number to frequencies and generate signal."""
        frequencies = []
        for digit in number_sequence:
            if digit in self.dial_frequencies:
                frequencies.append(self.dial_frequencies[digit])
        
        if not frequencies:
            return {
                'status': 'failed',
                'error': 'No valid digits in sequence',
                'signal_length': 0
            }
        
        signal = self.dial_sequence(frequencies)
        
        return {
            'status': 'success',
            'number': number_sequence,
            'signal': signal,
            'signal_length': len(signal),
            'frequency_count': len(frequencies),
            'frequencies': frequencies
        }
    
    def save_audio(self, signal: np.ndarray, filename: str) -> Dict:
        """Export signal to WAV file."""
        try:
            import wave
            import struct
            
            # Convert float32 to int16
            signal_int = np.int16(signal * 32767)
            
            with wave.open(filename, 'wb') as wav_file:
                wav_file.setnchannels(1)  # mono
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(self.config.sample_rate)
                wav_file.writeframes(signal_int.tobytes())
            
            return {
                'status': 'success',
                'filename': filename,
                'format': 'WAV',
                'channels': 1,
                'sample_rate': self.config.sample_rate
            }
        except Exception as e:
            return {
                'status': 'failed',
                'error': str(e)
            }
    
    def get_dial_map(self) -> Dict:
        """Return the digit to frequency mapping."""
        return self.dial_frequencies.copy()
