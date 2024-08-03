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
        # Add installation command for the specific tool here
        if tool == 'nmap':
            subprocess.run(['pkg', 'install', '-y', 'nmap'])
        elif tool == 'aircrack-ng':
            subprocess.run(['pkg', 'install', '-y', 'aircrack-ng'])
        elif tool == 'john':
            subprocess.run(['pkg', 'install', '-y', 'john'])
        elif tool == 'tshark':
            subprocess.run(['pkg', 'install', '-y', 'wireshark'])
        elif tool == 'hashcat':
            subprocess.run(['pkg', 'install', '-y', 'hashcat'])
        elif tool == 'crunch':
            subprocess.run(['pkg', 'install', '-y', 'crunch'])
        elif tool == 'adb':
            subprocess.run(['pkg', 'install', '-y', 'adb'])
        elif tool == 'apktool':
            subprocess.run(['pkg', 'install', '-y', 'apktool'])
        elif tool == 'curl':
            subprocess.run(['pkg', 'install', '-y', 'curl'])
        elif tool == 'openssh':
            subprocess.run(['pkg', 'install', '-y', 'openssh'])
        elif tool == 'openvpn':
            subprocess.run(['pkg', 'install', '-y', 'openvpn'])
        elif tool == 'frida':
            subprocess.run(['pip3', 'install', 'frida'])
        else:
            print(f"Tool {tool} not recognized or installation method not provided.")
