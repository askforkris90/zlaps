"""
Text Handler Module - Manages text messaging and conversation tracking.
Provides messaging system with conversation history.
"""

from typing import List, Dict, Optional
from datetime import datetime


class Message:
    """Individual message representation."""
    
    def __init__(self, sender: str, recipient: str, content: str, message_type: str = 'text'):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.message_type = message_type
        self.timestamp = datetime.now()
        self.id = f"{sender}_{recipient}_{int(self.timestamp.timestamp())}"
    
    def to_dict(self) -> Dict:
        """Convert message to dictionary."""
        return {
            'id': self.id,
            'sender': self.sender,
            'recipient': self.recipient,
            'content': self.content,
            'type': self.message_type,
            'timestamp': self.timestamp.isoformat()
        }
    
    def __str__(self) -> str:
        return f"{self.sender} → {self.recipient}: {self.content}"


class Conversation:
    """Represents a conversation between two users."""
    
    def __init__(self, user1: str, user2: str):
        self.user1 = user1
        self.user2 = user2
        self.messages: List[Message] = []
        self.created_at = datetime.now()
    
    def add_message(self, message: Message) -> Dict:
        """Add message to conversation."""
        self.messages.append(message)
        return {
            'status': 'success',
            'message_count': len(self.messages),
            'message_id': message.id
        }
    
    def get_messages(self) -> List[Dict]:
        """Get all messages in conversation."""
        return [msg.to_dict() for msg in self.messages]
    
    def get_message_count(self) -> int:
        """Get total message count."""
        return len(self.messages)
    
    def format_conversation(self) -> str:
        """Format conversation as readable text."""
        lines = []
        for msg in self.messages:
            timestamp = msg.timestamp.strftime("%H:%M:%S")
            lines.append(f"[{timestamp}] {msg.sender}: {msg.content}")
        return "\n".join(lines)


class TextHandler:
    """Messaging system manager."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.conversations: Dict[str, Conversation] = {}
        self.message_log: List[Message] = []
    
    def _get_conversation_key(self, other_user: str) -> str:
        """Get unique key for conversation."""
        users = sorted([self.user_id, other_user])
        return f"{users[0]}_{users[1]}"
    
    def create_message(self, recipient: str, content: str) -> Dict:
        """Send message."""
        message = Message(self.user_id, recipient, content)
        
        conv_key = self._get_conversation_key(recipient)
        if conv_key not in self.conversations:
            self.conversations[conv_key] = Conversation(self.user_id, recipient)
        
        result = self.conversations[conv_key].add_message(message)
        self.message_log.append(message)
        
        return {
            'status': 'success',
            'from': self.user_id,
            'to': recipient,
            'message': content,
            'timestamp': message.timestamp.isoformat(),
            **result
        }
    
    def receive_message(self, sender: str, content: str) -> Dict:
        """Record inbound message."""
        message = Message(sender, self.user_id, content)
        
        conv_key = self._get_conversation_key(sender)
        if conv_key not in self.conversations:
            self.conversations[conv_key] = Conversation(sender, self.user_id)
        
        result = self.conversations[conv_key].add_message(message)
        self.message_log.append(message)
        
        return {
            'status': 'success',
            'from': sender,
            'to': self.user_id,
            'message': content,
            'timestamp': message.timestamp.isoformat(),
            **result
        }
    
    def get_conversation(self, other_user: str) -> Optional[Dict]:
        """Retrieve conversation history."""
        conv_key = self._get_conversation_key(other_user)
        
        if conv_key not in self.conversations:
            return None
        
        conversation = self.conversations[conv_key]
        return {
            'participants': [self.user_id, other_user],
            'message_count': conversation.get_message_count(),
            'created_at': conversation.created_at.isoformat(),
            'messages': conversation.get_messages()
        }
    
    def format_conversation(self, other_user: str) -> str:
        """Display formatted conversation."""
        conv_key = self._get_conversation_key(other_user)
        
        if conv_key not in self.conversations:
            return f"No conversation with {other_user}"
        
        return self.conversations[conv_key].format_conversation()
    
    def get_all_conversations(self) -> Dict:
        """Get all conversations."""
        result = {}
        for conv_key, conversation in self.conversations.items():
            result[conv_key] = {
                'message_count': conversation.get_message_count(),
                'messages': conversation.get_messages()
            }
        return result
    
    def get_conversation_summary(self) -> Dict:
        """Get summary of all conversations."""
        return {
            'user': self.user_id,
            'total_conversations': len(self.conversations),
            'total_messages': len(self.message_log),
            'conversations': list(self.conversations.keys())
        }
