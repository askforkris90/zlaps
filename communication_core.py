"""
Communication Core Module
Orchestrates frequency dialing and text messaging
"""

from typing import Optional
from frequency_dialer import FrequencyDialer, FrequencyConfig
from text_handler import TextHandler, MessageType
import numpy as np


class CommunicationCore:
    """
    Main communication system that coordinates:
    - Frequency-based dialing
    - Text messaging
    - Two-way communication patterns
    """
    
    def __init__(self, user_id: str, low_sound_mode: bool = True):
        """
        Initialize communication core
        
        Args:
            user_id: Identifier for this communication endpoint
            low_sound_mode: Use low frequency range (True) or full range (False)
        """
        self.user_id = user_id
        self.low_sound_mode = low_sound_mode
        
        # Initialize components
        freq_config = FrequencyConfig()
        if low_sound_mode:
            freq_config.low_freq_range = (20, 120)  # Even lower range for "low sound friend"
        
        self.frequency_dialer = FrequencyDialer(freq_config)
        self.text_handler = TextHandler()
        
        self.active_connection = None
    
    def dial_out(self, recipient: str, number_sequence: str) -> dict:
        """
        Dial out to recipient using frequency signals
        
        Args:
            recipient: Recipient identifier
            number_sequence: Phone number to dial
        
        Returns:
            Dictionary with dialing info and audio signal
        """
        audio_signal = self.frequency_dialer.dial_out(
            number_sequence,
            low_sound=self.low_sound_mode
        )
        
        self.active_connection = recipient
        
        return {
            "status": "dialing",
            "from": self.user_id,
            "to": recipient,
            "number": number_sequence,
            "audio_signal": audio_signal,
            "signal_length": len(audio_signal)
        }
    
    def send_text(self, recipient: str, message_content: str) -> dict:
        """
        Send a text message
        
        Args:
            recipient: Recipient identifier
            message_content: Text content
        
        Returns:
            Dictionary with message info
        """
        message = self.text_handler.create_message(
            content=message_content,
            recipient=recipient,
            sender=self.user_id,
            message_type=MessageType.TEXT
        )
        
        return {
            "status": "sent",
            "from": self.user_id,
            "to": recipient,
            "message": message_content,
            "timestamp": message.timestamp.isoformat()
        }
    
    def send_hybrid(self, recipient: str, number: str, text: str) -> dict:
        """
        Send both frequency dial and text message simultaneously
        
        Args:
            recipient: Recipient identifier
            number: Frequency dial sequence
            text: Text message
        
        Returns:
            Dictionary with combined communication info
        """
        dial_result = self.dial_out(recipient, number)
        text_result = self.send_text(recipient, text)
        
        return {
            "status": "hybrid_transmission",
            "from": self.user_id,
            "to": recipient,
            "frequency_dial": dial_result,
            "text_message": text_result
        }
    
    def receive_text(self, sender: str, message_content: str) -> dict:
        """
        Receive an inbound text message
        
        Args:
            sender: Sender identifier
            message_content: Message text
        
        Returns:
            Dictionary with received message info
        """
        message = self.text_handler.receive_message(
            content=message_content,
            sender=sender,
            recipient=self.user_id
        )
        
        return {
            "status": "received",
            "from": sender,
            "to": self.user_id,
            "message": message_content,
            "timestamp": message.timestamp.isoformat()
        }
    
    def get_conversation_history(self, contact: str) -> str:
        """
        Get formatted conversation history with a contact
        
        Args:
            contact: Contact identifier
        
        Returns:
            Formatted conversation string
        """
        return self.text_handler.format_conversation(self.user_id, contact)
    
    def back_and_forth(self, recipient: str, exchange_pairs: list) -> dict:
        """
        Simulate back-and-forth communication (send/receive pairs)
        
        Args:
            recipient: Communication partner
            exchange_pairs: List of tuples (is_outbound: bool, message: str)
        
        Returns:
            Dictionary with complete exchange
        """
        exchanges = []
        
        for is_outbound, message_content in exchange_pairs:
            if is_outbound:
                result = self.send_text(recipient, message_content)
            else:
                result = self.receive_text(recipient, message_content)
            
            exchanges.append(result)
        
        return {
            "status": "conversation_complete",
            "participants": [self.user_id, recipient],
            "exchanges": exchanges,
            "history": self.get_conversation_history(recipient)
        }
