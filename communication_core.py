"""
Communication Core Module - Main orchestration combining frequency dialing and text messaging.
Provides unified interface for phone communication via frequency signals and text.
"""

from typing import Dict, List, Tuple
from frequency_dialer import FrequencyDialer, FrequencyConfig
from text_handler import TextHandler
import numpy as np


class CommunicationCore:
    """
    Main communication system that coordinates:
    - Frequency-based dialing
    - Text messaging
    - Two-way communication patterns
    - Hybrid communication (frequency + text)
    """
    
    def __init__(self, user_id: str, low_sound_mode: bool = True):
        """
        Initialize communication core
        
        Args:
            user_id: Identifier for this communication endpoint
            low_sound_mode: Use low frequency range (20-120 Hz) or full range (20-250 Hz)
        """
        self.user_id = user_id
        self.low_sound_mode = low_sound_mode
        
        # Initialize components
        freq_config = FrequencyConfig()
        self.frequency_dialer = FrequencyDialer(freq_config, low_sound_mode=low_sound_mode)
        self.text_handler = TextHandler(user_id)
        
        self.active_connection = None
    
    def dial_out(self, recipient: str, number_sequence: str) -> Dict:
        """
        Dial out to recipient using frequency signals
        
        Args:
            recipient: Recipient identifier
            number_sequence: Phone number to dial (e.g., "555-1234")
        
        Returns:
            Dictionary with dialing info and audio signal
        """
        result = self.frequency_dialer.dial_out(number_sequence)
        self.active_connection = recipient
        
        return {
            "status": result['status'],
            "from": self.user_id,
            "to": recipient,
            "number": number_sequence,
            "signal": result.get('signal'),
            "signal_length": result.get('signal_length', 0),
            "frequencies": result.get('frequencies', [])
        }
    
    def send_text(self, recipient: str, message_content: str) -> Dict:
        """
        Send a text message
        
        Args:
            recipient: Recipient identifier
            message_content: Text content to send
        
        Returns:
            Dictionary with message info
        """
        result = self.text_handler.create_message(recipient, message_content)
        
        return {
            "status": result['status'],
            "from": self.user_id,
            "to": recipient,
            "message": message_content,
            "message_count": result.get('message_count', 1),
            "timestamp": result.get('timestamp', '')
        }
    
    def receive_text(self, sender: str, message_content: str) -> Dict:
        """
        Receive an inbound text message
        
        Args:
            sender: Sender identifier
            message_content: Message text received
        
        Returns:
            Dictionary with received message info
        """
        result = self.text_handler.receive_message(sender, message_content)
        
        return {
            "status": result['status'],
            "from": sender,
            "to": self.user_id,
            "message": message_content,
            "message_count": result.get('message_count', 1),
            "timestamp": result.get('timestamp', '')
        }
    
    def send_hybrid(self, recipient: str, number: str, text: str) -> Dict:
        """
        Send both frequency dial and text message simultaneously
        
        Args:
            recipient: Recipient identifier
            number: Frequency dial sequence (e.g., "555-5678")
            text: Text message to send
        
        Returns:
            Dictionary with combined communication info
        """
        dial_result = self.dial_out(recipient, number)
        text_result = self.send_text(recipient, text)
        
        return {
            "status": "hybrid_transmission",
            "from": self.user_id,
            "to": recipient,
            "dial_status": dial_result['status'],
            "message_content": text,
            "signal_length": dial_result['signal_length'],
            "frequencies": dial_result['frequencies']
        }
    
    def get_conversation_history(self, contact: str) -> Dict:
        """
        Get formatted conversation history with a contact
        
        Args:
            contact: Contact identifier
        
        Returns:
            Dictionary with conversation history
        """
        conversation = self.text_handler.get_conversation(contact)
        
        if conversation is None:
            return {
                'status': 'no_conversation',
                'contact': contact,
                'messages': []
            }
        
        return {
            'status': 'success',
            'contact': contact,
            'message_count': conversation['message_count'],
            'messages': conversation['messages'],
            'created_at': conversation['created_at']
        }
    
    def back_and_forth(self, recipient: str, exchange_pairs: List[Tuple[bool, str]]) -> Dict:
        """
        Simulate back-and-forth communication (send/receive pairs)
        
        Args:
            recipient: Communication partner
            exchange_pairs: List of tuples (is_outbound: bool, message: str)
                           is_outbound=True means send, False means receive
        
        Returns:
            Dictionary with complete exchange
        """
        exchanges = []
        
        for is_outbound, message_content in exchange_pairs:
            if is_outbound:
                result = self.send_text(recipient, message_content)
                exchanges.append({
                    'direction': 'outbound',
                    **result
                })
            else:
                result = self.receive_text(recipient, message_content)
                exchanges.append({
                    'direction': 'inbound',
                    **result
                })
        
        history = self.get_conversation_history(recipient)
        
        return {
            "status": "conversation_complete",
            "participants": [self.user_id, recipient],
            "exchange_count": len(exchanges),
            "exchanges": exchanges,
            "history": history['messages'] if history['status'] == 'success' else []
        }
