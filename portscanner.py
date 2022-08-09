import socket

def scan(target, ports=100):
	print('\n' + "Scanning port for " + target)
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ip_addr, port):
	try:
		sock = socket.socket()
		sock.connect((ip_addr, port))
		print("[+] Port Opened "+ str(port))
	except:
		pass

targets = input("[*] Enter Targets To Scan(split by comma): ")
ports =int(input("[*] Enter the number of ports to scan: "))

if ',' in targets:
	print("[*] Multiple targets being scanned")
	for target in targets.split(','):
		scan(target.strip(' '), ports)
else:
	scan(targets,ports)



# try to get banner from open port where you can extract version
# Add counter to let you know how what is being scanned and how many port found closed
