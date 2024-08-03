import subprocess
from check_and_install import check_and_install, check_and_install_tool

class CyberSecurityAI:
    def __init__(self):
        # Check and install necessary tools and packages upon initialization
        self.check_and_install_dependencies()

    def check_and_install_dependencies(self):
        # Checking and installing required Python packages
        required_packages = ['nmap', 'metasploit.msfrpc']
        for package in required_packages:
            check_and_install(package)

        # Checking and installing required tools
        required_tools = [
            'nmap', 'aircrack-ng', 'john', 'tshark', 'hashcat', 'crunch', 'nessus', 'nikto', 'kismet',
            'adb', 'apktool', 'objection', 'frida', 'curl', 'openssh-client', 'openvpn', 'kali-tweaks'
        ]

        for tool in required_tools:
            check_and_install_tool(tool)

    def run_tool(self, tool_name, *args):
        tool_functions = {
            'nmap': self.run_nmap_scan,
            'metasploit': self.exploit_with_metasploit,
            'aircrack-ng': self.crack_wifi_with_aircrack,
            'john': self.crack_password_with_john,
            'wireshark': self.analyze_pcap_with_wireshark,
            'hashcat': self.crack_hash_with_hashcat,
            'crunch': self.generate_wordlist_with_crunch,
            'nessus': self.scan_with_nessus,
            'nikto': self.scan_with_nikto,
            'kismet': self.scan_with_kismet,
            'adb': self.run_adb_command,
            'apktool': self.decompile_with_apktool,
            'curl': self.run_curl,
            'kali-tweaks': self.run_kali_tweaks
        }
        
        if tool_name in tool_functions:
            return tool_functions[tool_name](*args)
        else:
            print(f"Tool {tool_name} is not recognized.")

    def run_nmap_scan(self, *args):
        result = subprocess.run(['nmap'] + list(args), capture_output=True)
        return result.stdout.decode()

    def exploit_with_metasploit(self, *args):
        # Assuming metasploit is called with msfconsole -x
        result = subprocess.run(['msfconsole', '-x'] + list(args), capture_output=True)
        return result.stdout.decode()

    def crack_wifi_with_aircrack(self, *args):
        result = subprocess.run(['aircrack-ng'] + list(args), capture_output=True)
        return result.stdout.decode()

    def crack_password_with_john(self, *args):
        result = subprocess.run(['john'] + list(args), capture_output=True)
        return result.stdout.decode()

    def analyze_pcap_with_wireshark(self, *args):
        result = subprocess.run(['tshark'] + list(args), capture_output=True)
        return result.stdout.decode()

    def crack_hash_with_hashcat(self, *args):
        result = subprocess.run(['hashcat'] + list(args), capture_output=True)
        return result.stdout.decode()

    def generate_wordlist_with_crunch(self, *args):
        result = subprocess.run(['crunch'] + list(args), capture_output=True)
        return result.stdout.decode()

    def scan_with_nessus(self, *args):
        # Command for Nessus scan
        pass

    def scan_with_nikto(self, *args):
        result = subprocess.run(['nikto'] + list(args), capture_output=True)
        return result.stdout.decode()

    def scan_with_kismet(self, *args):
        result = subprocess.run(['kismet'] + list(args), capture_output=True)
        return result.stdout.decode()

    def run_adb_command(self, *args):
        result = subprocess.run(['adb'] + list(args), capture_output=True)
        return result.stdout.decode()

    def decompile_with_apktool(self, *args):
        result = subprocess.run(['apktool'] + list(args), capture_output=True)
        return result.stdout.decode()

    def run_curl(self, *args):
        result = subprocess.run(['curl'] + list(args), capture_output=True)
        return result.stdout.decode()

    def run_kali_tweaks(self, *args):
        result = subprocess.run(['kali-tweaks'] + list(args), capture_output=True)
        return result.stdout.decode()
