import time
import psutil # Install with 'pip install psutil'
from pyembedded.raspberry_pi_tools.raspberrypi import PI # Install with 'pip install pyembedded'
pi = PI()

def get_cpu_temp():
	""" Récupérer la température du processeur """
	raw = psutil.sensors_temperatures().get("cpu_thermal")
	if raw is None:
		return 'Inconnu'
	else:
		return raw[0].current

def get_cpu_load():
	""" Récupérer la charge du processeur """
	# return pi.get_cpu_usage()
	return psutil.cpu_percent()

def get_ram_usage():
	""" Récupérer la charge du processeur """
	# return pi.get_ram_info()
	return psutil.virtual_memory().percent

def get_disk_usage():
	""" Récupérer la charge du processeur """
	return pi.get_disk_space()[3]

def get_network_usage(interface="eth0"):
	""" Utilisation du réseau """
	net_stat = psutil.net_io_counters(pernic=True, nowrap=True).get(interface)
	if net_stat is not None:
		net_in_1 = net_stat.bytes_recv
		net_out_1 = net_stat.bytes_sent
		time.sleep(1)
		net_stat = psutil.net_io_counters(pernic=True, nowrap=True).get(interface)
		net_in_2 = net_stat.bytes_recv
		net_out_2 = net_stat.bytes_sent
		return {'in': str(round((net_in_2 - net_in_1) / 1024 / 1024, 3)) + " MB/s", "out": str(round((net_out_2 - net_out_1) / 1024 / 1024, 3)) + " MB/s"}
	else:
		return {'in': "Inconnu (vérifiez le nom de l'interface utilisée)", 'out': ""}