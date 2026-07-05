# ZLAPS - Frequency & Text Communication System

A custom phone communication system that combines frequency-based dialing with text messaging for metropolitan urban communities.

## Features

- **Frequency Dialing**: Dial out using audio frequency signals (no iOS similarities)
- **Low Sound Mode**: Optimized for low-frequency communication patterns
- **Text Messaging**: Send and receive text messages
- **Hybrid Communication**: Combine frequency dialing and text in single transmission
- **Back-and-Forth**: Simulate two-way conversations between participants
- **Conversation History**: Track all message exchanges

## Architecture

### Modules

1. **frequency_dialer.py** - Generates audio frequency signals for dialing
   - Tone generation
   - Sequence creation
   - WAV file export
   - Low-frequency optimized

2. **text_handler.py** - Manages text-based messaging
   - Message creation and reception
   - Conversation tracking
   - Message formatting
   - Support for inbound/outbound messages

3. **communication_core.py** - Orchestrates the system
   - Dial-out functionality
   - Text transmission
   - Hybrid communications
   - Conversation management

## Usage Examples

```python
from communication_core import CommunicationCore

# Create a low-sound communication endpoint
comm = CommunicationCore(user_id="user1", low_sound_mode=True)

# Dial out using frequency
result = comm.dial_out(recipient="loretta", number_sequence="555-1234")

# Send text message
text_result = comm.send_text(recipient="loretta", message_content="Hello!")

# Send both frequency dial and text
hybrid = comm.send_hybrid(recipient="loretta", number="555-1234", text="Calling now")

# Simulate back-and-forth conversation
exchange = comm.back_and_forth(
    recipient="loretta",
    exchange_pairs=[
        (True, "Hey, can you hear me?"),
        (False, "Yes, I can hear you!"),
        (True, "Great, let's talk"),
    ]
)

# View conversation history
history = comm.get_conversation_history("loretta")
print(history)
```

## Configuration

### Low Sound Mode
When `low_sound_mode=True`:
- Frequency range: 20-120 Hz (bass/low frequencies)
- Better for "low sound friend" communication patterns
- Ideal for low-frequency distraction patterns

### Frequency Mapping
Digits are mapped to frequency values:
- 0 → 100 Hz
- 1 → 110 Hz
- 2 → 120 Hz
- ... and so on

## File Structure

```
zlaps/
├── frequency_dialer.py      # Frequency generation and tone management
├── text_handler.py          # Text messaging system
├── communication_core.py    # Main orchestration
└── README.md               # This file
```

## Technical Specifications

- **Sample Rate**: 44,100 Hz (standard audio)
- **Tone Duration**: 1.0 second per digit
- **Amplitude**: 0.7 (normalized)
- **Audio Format**: WAV (mono, 16-bit)

## For Metropolitan Urban Communities

ZLAPS is designed for affordable phone communication in metropolitan areas, combining:
- Low-cost frequency-based signaling
- Text backup communication
- Flexible two-way messaging
- Custom communication patterns

---

**No iOS Integration** - This is a standalone communication system with no Apple platform dependencies.
