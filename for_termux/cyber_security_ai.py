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
            'nmap', 'aircrack-ng', 'john', 'tshark', 'hashcat', 'crunch', 'adb', 'apktool', 'curl', 'openssh', 'openvpn', 'frida'
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
            'adb': self.run_adb_command,
            'apktool': self.decompile_with_apktool,
            'curl': self.transfer_with_curl,
            'openssh': self.run_ssh_command,
            'openvpn': self.connect_with_openvpn,
            'frida': self.instrument_with_frida
        }
        
        if tool_name in tool_functions:
            return tool_functions[tool_name](*args)
        else:
            return "Tool not supported"
    
    def run_nmap_scan(self, target):
        import nmap
        nm = nmap.PortScanner()
        nm.scan(target, arguments='-sV')
        return nm.csv()
    
    def exploit_with_metasploit(self, exploit, payload, target):
        import metasploit.msfrpc as msfrpc
        client = msfrpc.Msfrpc({})
        client.login('msf', 'password')
        exploit_module = client.call('module.exploits', [exploit])
        payload_module = client.call('module.payloads', [payload])
        client.call('module.execute', [exploit_module, payload_module, target])
        return "Exploit executed"
    
    def crack_wifi_with_aircrack(self, cap_file, wordlist):
        result = subprocess.run(['aircrack-ng', cap_file, '-w', wordlist], capture_output=True)
        return result.stdout.decode()
    
    def crack_password_with_john(self, password_file, wordlist):
        result = subprocess.run(['john', '--wordlist=' + wordlist, password_file], capture_output=True)
        return result.stdout.decode()
    
    def analyze_pcap_with_wireshark(self, pcap_file):
        result = subprocess.run(['tshark', '-r', pcap_file], capture_output=True)
        return result.stdout.decode()
    
    def crack_hash_with_hashcat(self, hash_file, wordlist):
        result = subprocess.run(['hashcat', '-a', '0', '-m', '0', hash_file, wordlist], capture_output=True)
        return result.stdout.decode()
    
    def generate_wordlist_with_crunch(self, min_len, max_len, charset):
        result = subprocess.run(['crunch', min_len, max_len, charset], capture_output=True)
        return result.stdout.decode()
    
    def run_adb_command(self, command):
        result = subprocess.run(['adb', 'shell', command], capture_output=True)
        return result.stdout.decode()
    
    def decompile_with_apktool(self, apk_file):
        result = subprocess.run(['apktool', 'd', apk_file], capture_output=True)
        return result.stdout.decode()
    
    def transfer_with_curl(self, url):
        result = subprocess.run(['curl', url], capture_output=True)
        return result.stdout.decode()
    
    def run_ssh_command(self, command, host):
        result = subprocess.run(['ssh', host, command], capture_output=True)
        return result.stdout.decode()
    
    def connect_with_openvpn(self, config_file):
        result = subprocess.run(['openvpn', '--config', config_file], capture_output=True)
        return result.stdout.decode()
    
    def instrument_with_frida(self, script, target_app):
        result = subprocess.run(['frida', '-U', '-f', target_app, '-l', script, '--no-pause'], capture_output=True)
        return result.stdout.decode()
