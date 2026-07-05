#!/usr/bin/env python3
"""
ZLAPS Desktop Display Application
Displays the ZLAPS communication system with a GUI interface on your desktop
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from datetime import datetime
from communication_core import CommunicationCore
from wireless_download import WirelessDownloadManager

class ZLAPSDesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZLAPS - Phone Communication System")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a2e")
        
        # Initialize communication
        self.comm = CommunicationCore(user_id="Desktop User", low_sound_mode=True)
        self.download_manager = WirelessDownloadManager()
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        """Create the main GUI widgets"""
        
        # Header
        header_frame = tk.Frame(self.root, bg="#0f3460", height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame, 
            text="🌊 ZLAPS - Frequency Phone Communication System 🌊",
            font=("Arial", 16, "bold"),
            bg="#0f3460",
            fg="#00dcff"
        )
        title_label.pack(pady=10)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_frame, bg="#1a1a2e")
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
        
        # Recipient input
        tk.Label(left_panel, text="Recipient:", font=("Arial", 10, "bold"), bg="#1a1a2e", fg="#00dcff").pack(pady=5)
        self.recipient_entry = tk.Entry(left_panel, width=20, font=("Arial", 10))
        self.recipient_entry.insert(0, "loretta")
        self.recipient_entry.pack(pady=5)
        
        # Phone number input
        tk.Label(left_panel, text="Phone Number:", font=("Arial", 10, "bold"), bg="#1a1a2e", fg="#00dcff").pack(pady=5)
        self.phone_entry = tk.Entry(left_panel, width=20, font=("Arial", 10))
        self.phone_entry.insert(0, "555-1234")
        self.phone_entry.pack(pady=5)
        
        # Message input
        tk.Label(left_panel, text="Message:", font=("Arial", 10, "bold"), bg="#1a1a2e", fg="#00dcff").pack(pady=5)
        self.message_entry = scrolledtext.ScrolledText(left_panel, width=25, height=6, font=("Arial", 9))
        self.message_entry.pack(pady=5)
        
        # Buttons frame
        button_frame = tk.Frame(left_panel, bg="#1a1a2e")
        button_frame.pack(pady=10)
        
        # Dial button
        dial_btn = tk.Button(
            button_frame,
            text="📞 Dial Out",
            command=self.dial_out,
            bg="#00dcff",
            fg="#000",
            font=("Arial", 10, "bold"),
            width=15
        )
        dial_btn.pack(pady=5)
        
        # Send text button
        send_btn = tk.Button(
            button_frame,
            text="💬 Send Text",
            command=self.send_text,
            bg="#00dcff",
            fg="#000",
            font=("Arial", 10, "bold"),
            width=15
        )
        send_btn.pack(pady=5)
        
        # Hybrid button
        hybrid_btn = tk.Button(
            button_frame,
            text="📡 Send Hybrid",
            command=self.send_hybrid,
            bg="#ff6400",
            fg="#fff",
            font=("Arial", 10, "bold"),
            width=15
        )
        hybrid_btn.pack(pady=5)
        
        # Download button
        download_btn = tk.Button(
            button_frame,
            text="📥 Wireless Download",
            command=self.show_download_info,
            bg="#4caf50",
            fg="#fff",
            font=("Arial", 10, "bold"),
            width=15
        )
        download_btn.pack(pady=5)
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="🗑️  Clear",
            command=self.clear_output,
            bg="#666",
            fg="#fff",
            font=("Arial", 10, "bold"),
            width=15
        )
        clear_btn.pack(pady=5)
        
        # Right panel - Output
        right_panel = tk.Frame(main_frame, bg="#1a1a2e")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(right_panel, text="Communication Log:", font=("Arial", 11, "bold"), bg="#1a1a2e", fg="#00dcff").pack(anchor=tk.W, pady=5)
        
        # Output display
        self.output_display = scrolledtext.ScrolledText(
            right_panel,
            width=50,
            height=30,
            font=("Courier", 9),
            bg="#0f3460",
            fg="#00ff00",
            insertbackground="#00dcff"
        )
        self.output_display.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Configure text tags for styling
        self.output_display.tag_config("header", foreground="#ff6400", font=("Courier", 10, "bold"))
        self.output_display.tag_config("success", foreground="#4caf50")
        self.output_display.tag_config("error", foreground="#ff4444")
        self.output_display.tag_config("info", foreground="#00dcff")
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#0f3460", height=40)
        footer_frame.pack(fill=tk.X)
        
        footer_label = tk.Label(
            footer_frame,
            text="✓ ZLAPS Ready | Frequency Range: 20-120 Hz (Low-Sound Mode)",
            font=("Arial", 9),
            bg="#0f3460",
            fg="#00dcff"
        )
        footer_label.pack(pady=8)
        
        # Log initial message
        self.log_message("ZLAPS Desktop Application Started", "header")
        self.log_message(f"User ID: {self.comm.user_id}", "info")
        self.log_message("Ready to communicate!", "success")
    
    def log_message(self, message, tag="info"):
        """Add message to output display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        self.output_display.insert(tk.END, full_message, tag)
        self.output_display.see(tk.END)
        self.root.update()
    
    def dial_out(self):
        """Handle dial out"""
        recipient = self.recipient_entry.get()
        phone = self.phone_entry.get()
        
        if not recipient or not phone:
            messagebox.showwarning("Input Error", "Please enter recipient and phone number")
            return
        
        try:
            self.log_message(f"Dialing {phone} to {recipient}...", "header")
            result = self.comm.dial_out(recipient=recipient, number_sequence=phone)
            
            self.log_message(f"Status: {result['status']}", "success")
            self.log_message(f"Signal Length: {result['signal_length']} samples", "info")
            self.log_message(f"Frequencies: {result['frequencies']}", "info")
        except Exception as e:
            self.log_message(f"Error: {str(e)}", "error")
    
    def send_text(self):
        """Handle send text"""
        recipient = self.recipient_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()
        
        if not recipient or not message:
            messagebox.showwarning("Input Error", "Please enter recipient and message")
            return
        
        try:
            self.log_message(f"Sending text to {recipient}...", "header")
            result = self.comm.send_text(recipient=recipient, message_content=message)
            
            self.log_message(f"Status: {result['status']}", "success")
            self.log_message(f"Message: {result['message']}", "info")
            self.log_message(f"Timestamp: {result['timestamp']}", "info")
        except Exception as e:
            self.log_message(f"Error: {str(e)}", "error")
    
    def send_hybrid(self):
        """Handle hybrid communication"""
        recipient = self.recipient_entry.get()
        phone = self.phone_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()
        
        if not recipient or not phone or not message:
            messagebox.showwarning("Input Error", "Please enter recipient, phone, and message")
            return
        
        try:
            self.log_message(f"Sending hybrid transmission to {recipient}...", "header")
            result = self.comm.send_hybrid(recipient=recipient, number=phone, text=message)
            
            self.log_message(f"Status: {result['status']}", "success")
            self.log_message(f"Dial Status: {result['dial_status']}", "info")
            self.log_message(f"Message: {result['message_content']}", "info")
        except Exception as e:
            self.log_message(f"Error: {str(e)}", "error")
    
    def show_download_info(self):
        """Show wireless download information"""
        try:
            self.log_message("Creating wireless package...", "header")
            pkg = self.download_manager.create_wireless_package()
            
            self.log_message(f"Package ID: {pkg['package_id']}", "success")
            self.log_message(f"Total Size: {pkg['total_size_kb']} KB", "info")
            self.log_message(f"Checksum: {pkg['checksum'][:16]}...", "info")
            
            # Show download links
            self.log_message("\n--- Download Links ---", "header")
            
            for device in ["android", "linux", "raspberry_pi"]:
                info = self.download_manager.get_download_link(device)
                self.log_message(f"\n{device.upper()}:", "info")
                self.log_message(f"  URL: {info['download_url']}", "info")
                self.log_message(f"  Time: {info['estimated_download_time_sec']:.2f}s", "info")
                
        except Exception as e:
            self.log_message(f"Error: {str(e)}", "error")
    
    def clear_output(self):
        """Clear the output display"""
        self.output_display.delete("1.0", tk.END)
        self.log_message("Output cleared", "info")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = ZLAPSDesktopApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
