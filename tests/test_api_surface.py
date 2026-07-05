# tests/test_api_surface.py
import importlib

MODULES_AND_EXPECTED = {
    "frequency_dialer": {
        "classes": ["FrequencyConfig", "FrequencyDialer"],
        "methods_on_frequency_dialer": ["generate_tone", "dial_sequence", "dial_out", "save_audio"],
    },
    "text_handler": {
        "classes": ["Message", "TextHandler"],
        "methods_on_text_handler": ["create_message", "receive_message", "get_conversation", "format_conversation"],
    },
    "communication_core": {
        "classes": ["CommunicationCore"],
        "methods_on_communication_core": ["dial_out", "send_text", "send_hybrid", "receive_text", "back_and_forth", "get_conversation_history"],
    },
    "wireless_download": {
        "classes": ["WirelessDownloadManager", "WirelessPackage", "MobileOptimizer"],
        "methods_on_wireless_download_manager": ["create_wireless_package", "get_download_link", "verify_download", "log_download"],
    },
}


def _import_or_fail(module_name):
    try:
        return importlib.import_module(module_name)
    except Exception as e:
        raise AssertionError(f"Failed to import module '{module_name}': {e}")


def test_modules_and_classes_exist():
    for module_name, spec in MODULES_AND_EXPECTED.items():
        module = _import_or_fail(module_name)
        # check classes
        for cls_name in spec.get("classes", []):
            assert hasattr(module, cls_name), f"Module '{module_name}' missing class '{cls_name}'"


def test_frequency_dialer_methods_exist():
    module = _import_or_fail("frequency_dialer")
    FD = getattr(module, "FrequencyDialer")
    for method in MODULES_AND_EXPECTED["frequency_dialer"]["methods_on_frequency_dialer"]:
        assert hasattr(FD, method), f"FrequencyDialer missing method '{method}'"


def test_text_handler_methods_exist():
    module = _import_or_fail("text_handler")
    TH = getattr(module, "TextHandler")
    for method in MODULES_AND_EXPECTED["text_handler"]["methods_on_text_handler"]:
        assert hasattr(TH, method), f"TextHandler missing method '{method}'"


def test_communication_core_methods_exist():
    module = _import_or_fail("communication_core")
    CC = getattr(module, "CommunicationCore")
    for method in MODULES_AND_EXPECTED["communication_core"]["methods_on_communication_core"]:
        assert hasattr(CC, method), f"CommunicationCore missing method '{method}'"


def test_wireless_download_manager_methods_exist():
    module = _import_or_fail("wireless_download")
    WDM = getattr(module, "WirelessDownloadManager")
    for method in MODULES_AND_EXPECTED["wireless_download"]["methods_on_wireless_download_manager"]:
        assert hasattr(WDM, method), f"WirelessDownloadManager missing method '{method}'"
