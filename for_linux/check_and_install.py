import subprocess
import sys

def check_and_install(package):
    try:
        __import__(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_tool(tool):
    result = subprocess.run(['which', tool], capture_output=True)
    if result.returncode != 0:
        print(f"{tool} is not installed. Installing...")
        if tool == 'nmap':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nmap'])
        elif tool == 'aircrack-ng':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'aircrack-ng'])
        elif tool == 'john':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'john'])
        elif tool == 'tshark':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'wireshark'])
        elif tool == 'hashcat':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'hashcat'])
        elif tool == 'crunch':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'crunch'])
        elif tool == 'nessus':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nessus'])
        elif tool == 'nikto':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nikto'])
        elif tool == 'kismet':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'kismet'])
        elif tool == 'adb':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'adb'])
        elif tool == 'apktool':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'apktool'])
        elif tool == 'objection':
            subprocess.run(['pip3', 'install', 'objection'])
        elif tool == 'frida':
            subprocess.run(['pip3', 'install', 'frida'])
        elif tool == 'curl':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'curl'])
        elif tool == 'openssh-client':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'openssh-client'])
        elif tool == 'openvpn':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'openvpn'])
        elif tool == 'kali-tweaks':
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'kali-tweaks'])
        else:
            print(f"No installation command for {tool}. Please install it manually.")

