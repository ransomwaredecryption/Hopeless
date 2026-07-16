# Hopeless (WannaCry v2 Simulation)

[![Python Version](https://shields.io)](https://python.org)
[![Platform](https://shields.io)](https://microsoft.com)
[![License](https://shields.io)](#disclaimer)

A high-fidelity Python-based simulation designed to replicate the behavioral patterns, evasion tactics, and destructive mechanisms of sophisticated ransomware strains like WannaCry. 

This repository serves strictly as a **behavioral blueprint** for malware analysts, security researchers, and blue team engineers studying endpoint detection, indicator of compromise (IoC) generation, and modern Endpoint Detection and Response (EDR) testing.

---

## ⚠️ Important Disclaimer

> [!CAUTION]
> **ONLY FOR PEOPLE THAT HAS MONEY.**  
> Running or modifying this software without proper isolation will cause **permanent, irreversible data loss and operating system corruption**. The authors and contributors assume no liability for damages caused by the misuse of this code. Always execute inside a dedicated, non-networked malware analysis sandbox or hypervisor.

---

## 🔍 Behavioral Features

This script simulates the complete life cycle of an advanced threat actor on an endpoint:

* **Security Evasion & Persistence:** Automatically attempts to bypass real-time monitoring by disabling Windows Defender configurations via PowerShell and enforces process single-instancing via an OS-level named mutex (`Global\WannaCryV2Mutex`).
* **Recovery Inhibition:** Executes standard native utility manipulation to purge Volume Shadow Copies (`vssadmin`) and alters the Windows Boot Configuration Data (`bcdedit`) to prevent automated system repairs.
* **Cryptographic Payload:** Scans local paths and network drive arrays (`A-Z:\`) for sensitive extension targets, applying authenticated AES-256 GCM encryption before severing the original files.
* **Worm-like Lateral Movement:** Replicates historical SMB exploits by multi-threading subnet enumeration sweeps and mapping remote system triggers via hidden scheduled tasks (`schtasks`).
* **Anti-Analysis Defenses:** Contains an aggressive, multi-tiered destruction protocol that triggers an explicit Blue Screen of Death (BSOD) and destroys the Master Boot Record (MBR) if system validation criteria fail.

---

## 🛠️ Repository Structure

```text
├── hopeless.py          # Main malware simulation core engine
└── README.md            # Repository documentation and safety protocols
```

---

## 📋 Prerequisites & Architecture

The script relies heavily on native Windows APIs accessed through Python wrappers. The following environment constraints apply:

### Supported Operating Systems
* Windows 10 / 11 (Architecture validation is strictly enforced for NT systems).

### Python Dependencies
Install the required low-level cryptographic and system tracking dependencies:
```bash
pip install pycryptodome psutil pywin32 pillow
```

---

## 🔬 Indicators of Compromise (IoCs)

When testing this script within an isolated SIEM/EDR engineering lab, look for the following default artifacts:

| Artifact Type | Value / Signature | Description |
| :--- | :--- | :--- |
| **File Extension** | `.WCRY2` | Appended to all encrypted payloads |
| **Mutex Signature** | `Global\WannaCryV2Mutex` | Used to prevent process collision |
| **Dropped Files** | `README_WANNA_CRY.txt` | Generated ransom note documentation |
| **Registry Key Modification** | `HKLM\SYSTEM\...\Control\SafeBoot` | Altered to break safe boot pathways |
