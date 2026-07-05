"""
Examples - Demonstration of ZLAPS functionality.
Shows basic usage of frequency dialing, text messaging, and wireless distribution.
"""

from communication_core import CommunicationCore
from wireless_download import WirelessDownloadManager


def example_1_basic_frequency_dialing():
    """Example 1: Basic Frequency Dialing"""
    print("\n=== Example 1: Basic Frequency Dialing ===")
    
    comm = CommunicationCore(user_id="user1", low_sound_mode=True)
    
    # Dial out
    result = comm.dial_out(recipient="loretta", number_sequence="555-1234")
    print(f"Status: {result['status']}")
    print(f"Signal length: {result['signal_length']} samples")
    print(f"Frequencies used: {result['frequencies']}")


def example_2_send_receive_text():
    """Example 2: Send & Receive Text"""
    print("\n=== Example 2: Send & Receive Text ===")
    
    comm = CommunicationCore(user_id="user1", low_sound_mode=True)
    
    # Send text
    send_result = comm.send_text(recipient="loretta", message_content="Hello Loretta!")
    print(f"Sent: {send_result['message']}")
    
    # Receive text
    recv_result = comm.receive_text(sender="loretta", message_content="Hi there!")
    print(f"Received: {recv_result['message']}")


def example_3_hybrid_communication():
    """Example 3: Hybrid Communication"""
    print("\n=== Example 3: Hybrid Communication ===")
    
    comm = CommunicationCore(user_id="user1", low_sound_mode=True)
    
    # Send frequency dial + text simultaneously
    result = comm.send_hybrid(
        recipient="loretta",
        number="555-5678",
        text="Calling with backup text"
    )
    print(f"Hybrid status: {result['dial_status']}")
    print(f"Message: {result['message_content']}")


def example_4_back_and_forth_conversation():
    """Example 4: Back-and-Forth Conversation"""
    print("\n=== Example 4: Back-and-Forth Conversation ===")
    
    comm = CommunicationCore(user_id="alice", low_sound_mode=True)
    
    exchange = comm.back_and_forth(
        recipient="bob",
        exchange_pairs=[
            (True, "Are you there?"),
            (False, "Yes, I'm here!"),
            (True, "Great, let's talk"),
            (False, "Perfect!")
        ]
    )
    
    print("Conversation History:")
    print(exchange['history'])


def example_5_conversation_history():
    """Example 5: Conversation History"""
    print("\n=== Example 5: Conversation History ===")
    
    comm = CommunicationCore(user_id="user1", low_sound_mode=True)
    
    # Send and receive some messages
    comm.send_text(recipient="alice", message_content="Hey Alice!")
    comm.receive_text(sender="alice", message_content="Hi! How are you?")
    comm.send_text(recipient="alice", message_content="I'm doing great!")
    
    # View conversation
    history = comm.get_conversation_history("alice")
    print("Full conversation:")
    for entry in history['messages']:
        print(f"  [{entry['timestamp']}] {entry['sender']}: {entry['content']}")


def example_6_wireless_download():
    """Example 6: Wireless Download for Mobile"""
    print("\n=== Example 6: Wireless Download for Mobile ===")
    
    manager = WirelessDownloadManager()
    
    # Create package
    pkg_result = manager.create_wireless_package()
    print(f"Package created: {pkg_result['package_id']}")
    print(f"Total size: {pkg_result['total_size_kb']} KB")
    
    # Get download link for Android
    android_info = manager.get_download_link(device_type="android")
    print(f"\nAndroid Download:")
    print(f"  Download URL: {android_info['download_url']}")
    print(f"  File Size: {android_info['file_size']}")
    print(f"  Checksum: {android_info['checksum']}")
    print(f"  Est. time: {android_info['estimated_download_time_sec']:.2f}s")
    
    # Get download link for Raspberry Pi
    pi_info = manager.get_download_link(device_type="raspberry_pi")
    print(f"\nRaspberry Pi Download:")
    print(f"  Download URL: {pi_info['download_url']}")
    print(f"  Compression: {pi_info['optimization']['compression']}")
    
    # Log downloads
    manager.log_download("android", pkg_result['package_id'])
    manager.log_download("raspberry_pi", pkg_result['package_id'])
    
    # Statistics
    stats = manager.get_download_statistics()
    print(f"\nDownload Statistics:")
    print(f"  Total: {stats['total_downloads']}")
    print(f"  By device: {stats['by_device']}")


def example_7_full_workflow():
    """Example 7: Full Workflow - Complete Communication"""
    print("\n=== Example 7: Full Workflow ===")
    
    # Initialize communication
    comm = CommunicationCore(user_id="alice", low_sound_mode=True)
    
    print("1. Dialing...")
    dial = comm.dial_out(recipient="bob", number_sequence="555-9999")
    print(f"   Dial status: {dial['status']}")
    
    print("\n2. Sending text...")
    msg = comm.send_text(recipient="bob", message_content="Bob, can you hear me?")
    print(f"   Message sent at: {msg['timestamp']}")
    
    print("\n3. Receiving response...")
    resp = comm.receive_text(sender="bob", message_content="Yes! Loud and clear!")
    print(f"   Response: {resp['message']}")
    
    print("\n4. Viewing conversation...")
    history = comm.get_conversation_history("bob")
    print(f"   Total messages: {history['message_count']}")
    for msg in history['messages']:
        print(f"   - {msg['sender']}: {msg['content']}")


def run_all_examples():
    """Run all examples."""
    print("=" * 60)
    print("ZLAPS - Phone Communication System Examples")
    print("=" * 60)
    
    try:
        example_1_basic_frequency_dialing()
        example_2_send_receive_text()
        example_3_hybrid_communication()
        example_4_back_and_forth_conversation()
        example_5_conversation_history()
        example_6_wireless_download()
        example_7_full_workflow()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_examples()
