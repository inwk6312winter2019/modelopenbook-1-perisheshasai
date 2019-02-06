fin=open("running-config.cfg","r")
term="nameif"
term1="ip address"
d=dict()
def ip():
	for line in fin:
		line.strip.split('/n')
		if term in line:
			line_nameif=line_nameif.strip()
			print(line_nameif)
		if term1 in line:
			line_ip_sddress=line_ip_address.strip()
			print(line_ip_address)
			dict.update({line_nameif:line_ip_address})
ip()
print(d)
fin.close()
