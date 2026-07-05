"""
Wireless Download Module - Package and distribute to wireless/mobile devices.
Handles packaging, distribution, and verification for mobile devices.
"""

import hashlib
import json
from typing import Dict, List, Optional
from datetime import datetime


class WirelessPackage:
    """Downloadable package container."""
    
    def __init__(self, package_id: str, version: str = "1.0.0"):
        self.package_id = package_id
        self.version = version
        self.modules = []
        self.total_size = 0
        self.checksum = None
        self.created_at = datetime.now()
    
    def add_module(self, module_name: str, size_kb: float) -> Dict:
        """Add module to package."""
        self.modules.append({
            'name': module_name,
            'size_kb': size_kb,
            'added_at': datetime.now().isoformat()
        })
        self.total_size += size_kb
        
        return {
            'status': 'added',
            'module': module_name,
            'total_size_kb': self.total_size
        }
    
    def calculate_checksum(self) -> str:
        """Calculate SHA-256 checksum for package."""
        package_data = json.dumps({
            'id': self.package_id,
            'version': self.version,
            'modules': self.modules,
            'size': self.total_size
        }).encode()
        
        self.checksum = hashlib.sha256(package_data).hexdigest()
        return self.checksum
    
    def get_package_info(self) -> Dict:
        """Get package information."""
        return {
            'id': self.package_id,
            'version': self.version,
            'modules': self.modules,
            'total_size_kb': self.total_size,
            'checksum': self.checksum,
            'created_at': self.created_at.isoformat()
        }


class MobileOptimizer:
    """Transmission optimization for mobile devices."""
    
    @staticmethod
    def optimize_for_device(device_type: str) -> Dict:
        """Get optimization parameters for device type."""
        optimizations = {
            'android': {
                'compression': 'gzip',
                'max_chunk_size': 512,  # KB
                'timeout': 30,  # seconds
                'retries': 3
            },
            'linux': {
                'compression': 'gzip',
                'max_chunk_size': 1024,
                'timeout': 60,
                'retries': 2
            },
            'raspberry_pi': {
                'compression': 'bzip2',
                'max_chunk_size': 256,
                'timeout': 45,
                'retries': 3
            },
            'ios': {
                'compression': 'gzip',
                'max_chunk_size': 512,
                'timeout': 30,
                'retries': 2
            },
            'custom': {
                'compression': 'gzip',
                'max_chunk_size': 512,
                'timeout': 30,
                'retries': 2
            }
        }
        
        return optimizations.get(device_type.lower(), optimizations['custom'])
    
    @staticmethod
    def estimate_download_time(size_kb: float, bandwidth_mbps: float = 5.0) -> float:
        """Estimate download time in seconds."""
        size_megabits = (size_kb * 8) / 1024
        return size_megabits / bandwidth_mbps


class WirelessDownloadManager:
    """Distribution manager."""
    
    def __init__(self):
        self.packages: Dict[str, WirelessPackage] = {}
        self.download_log: List[Dict] = []
        self.supported_devices = ['android', 'linux', 'raspberry_pi', 'ios', 'custom']
    
    def create_wireless_package(self) -> Dict:
        """Build package for wireless distribution."""
        package_id = f"zlaps_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        package = WirelessPackage(package_id)
        
        # Add standard modules
        modules = [
            ('frequency_dialer.py', 5),
            ('text_handler.py', 3),
            ('communication_core.py', 5),
            ('wireless_download.py', 6)
        ]
        
        for module, size in modules:
            package.add_module(module, size)
        
        package.calculate_checksum()
        self.packages[package_id] = package
        
        return {
            'status': 'created',
            'package_id': package_id,
            'total_size_kb': package.total_size,
            'module_count': len(package.modules),
            'checksum': package.checksum
        }
    
    def get_download_link(self, device_type: str = 'mobile') -> Dict:
        """Get download info for device type."""
        # Map common device names
        device_map = {
            'mobile': 'android',
            'phone': 'android',
            'raspberry': 'raspberry_pi',
            'pi': 'raspberry_pi'
        }
        
        actual_device = device_map.get(device_type.lower(), device_type.lower())
        
        if actual_device not in self.supported_devices:
            return {
                'status': 'failed',
                'error': f'Unsupported device type: {device_type}',
                'supported_devices': self.supported_devices
            }
        
        # Get latest package
        if not self.packages:
            self.create_wireless_package()
        
        latest_package_id = max(self.packages.keys())
        package = self.packages[latest_package_id]
        
        optimizer = MobileOptimizer.optimize_for_device(actual_device)
        est_time = MobileOptimizer.estimate_download_time(package.total_size_kb)
        
        return {
            'status': 'success',
            'device_type': actual_device,
            'package_id': latest_package_id,
            'download_url': f'https://github.com/askforkris90/zlaps/releases/download/{latest_package_id}',
            'file_size': f'{package.total_size_kb} KB',
            'checksum': package.checksum,
            'device_types': [actual_device],
            'optimization': optimizer,
            'estimated_download_time_sec': est_time,
            'modules': [m['name'] for m in package.modules]
        }
    
    def verify_download(self, package_id: str, checksum: str) -> Dict:
        """Check integrity of downloaded package."""
        if package_id not in self.packages:
            return {
                'status': 'failed',
                'error': f'Package {package_id} not found'
            }
        
        package = self.packages[package_id]
        
        if package.checksum != checksum:
            return {
                'status': 'failed',
                'valid': False,
                'error': 'Checksum mismatch',
                'expected': package.checksum,
                'received': checksum
            }
        
        return {
            'status': 'success',
            'valid': True,
            'package_id': package_id,
            'checksum': checksum,
            'verified_at': datetime.now().isoformat()
        }
    
    def log_download(self, device_type: str, package_id: str, success: bool = True) -> Dict:
        """Track download attempt."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'device_type': device_type,
            'package_id': package_id,
            'success': success
        }
        
        self.download_log.append(log_entry)
        
        return {
            'status': 'logged',
            'total_downloads': len(self.download_log),
            'entry': log_entry
        }
    
    def get_download_statistics(self) -> Dict:
        """Get download statistics."""
        total = len(self.download_log)
        successful = sum(1 for log in self.download_log if log['success'])
        failed = total - successful
        
        device_stats = {}
        for log in self.download_log:
            device = log['device_type']
            if device not in device_stats:
                device_stats[device] = 0
            device_stats[device] += 1
        
        return {
            'total_downloads': total,
            'successful': successful,
            'failed': failed,
            'by_device': device_stats
        }
