import pyperclip, re


def ParseSwitch(switch_run_config,switchfile,switchname,tableinfo):

	#switchRegex = re.compile(r'interface(\s)*ethernet(\s)*[a-z0-9]*(\s)*',re.VERBOSE|re.IGNORECASE)
	#switchRegex = re.compile(r'interface.ethernet.(\d/\d){1}.description (.*) lagi',re.VERBOSE|re.IGNORECASE|re.DOTALL)
	#switchRegex = re.compile(r'ethernet\s?(\d/\d+){1}\s+description [A-Za-z0-9:-]*',re.IGNORECASE|re.VERBOSE)
	switchRegex = re.compile(r'''
	ethernet\s?(\d/\d+){1}?\s*
	(description\s+[A-Za-z0-9:\-_. ]*)?\s*
	(no\s+cdp\s+enable)?\s*
	(switchport\s+mode\s+trunk)?\s*
	(switchport\s+trunk\s+native\s+vlan\s+(\d)+)?\s*
	(switchport\s+trunk\s+allowed\s+vlan\s+([\d+,-])+)?\s*
	(spanning-tree\s+port\s+type\s+normal)?\s*
	(spanning\-tree\s+bpduguard\s+disable)?\s*
	(spanning-tree\s+port\s+type\s+edge\s+trunk)?\s*
	(no\s+snmp\s+trap\s+link-status)?\s*
	(channel-group\s+(\d+)?\s+mode\s+active)?\s*
	(no)?\s+shutdown
	''',re.IGNORECASE | re.VERBOSE|re.DOTALL)
	#(switchport mode trunk)?\s+
	#(switchport trunk native vlan (\d\d\d\d)+)?\s+
	#''',re.IGNORECASE|re.VERBOSE)

	#switchRegex = re.compile(r'''interface ethernet \d/(\d)+ # interface ethernet 1/5
	#(\s)?(description)?														 # description bookz1_s6p1_hyper_tdnh1
	#''',re.IGNORECASE|re.VERBOSE)
	#result=switchRegex.search('interface ethernet 1/30 description BIRDIE lagi')
	#result=switchRegex.search(switch_run_config)
	result=switchRegex.findall(switch_run_config)
	print "Switch " + switchfile
	print "=============================\n"
	
	for res in result:
		#debug print ('result in g0 :' + res[0]+ ' g1 ' + res[1] + ' g2 ' + res[2] + ' g3 ' + res[3] + ' g4 ' + res[4] + ' g5 ' + res[5] + ' g6 ' + res[6] + ' g7 ' + res[7] + ' g8 '+ res[8] + '\n' )
		#print ('result' + res[0])
		#print ('result' + res[1])
		listinfo=[switchname,res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8]]
		#print ' '.join(listinfo)
		tableinfo[switchname+res[0]]=listinfo
	#print('switc run ' + switch_run_config)
	#print ('result in group :' + result.group(0)+ ' group1 ' + result.group(1) + 'group2 '+result.group(2))
	#print ('result in group :' + result.group(0)+ ' group1 ' + result.group(1))
    #listinfo=[res[0],res[1],res[2]] 
	#print('result '+ result.group(0))
	#print('sini')	
	#test=re.compile(r'Last: (.*) sama (\d/\d) lagi description')
	#mo=test.search('First: Al Last:   Swiegart sama 1/3 lagi description BIRDIEZ switchport')
	#print ('mo group 0 '+mo.group(0)+ ' group 1 ' + mo.group(1) + ' group 2 ' + mo.group(2))
    
	
def ReadSwitchConfigFromFile(Filename):
	readfile=open(Filename,'r')
	result=readfile.read()
	return result
	

switch_run_config='''
	interface Ethernet1/1
	description C::HZL-COLO-CORE-RTA1
	switchport mode trunk
	switchport trunk native vlan 2046
	switchport trunk allowed vlan 2046,2200-2249,2298-2299
	spanning-tree port type normal
	spanning-tree bpduguard disable
	channel-group 714 mode active
	no shutdown

	interface Ethernet1/2
	description Foruplinkexpansiontodist2-2
	no shutdown
  
	'''
switch_run_config1='''
	interface Ethernet1/2
	description Foruplinkexpansiontodist2-2
	no shutdown
	'''
#ParseSwitch(switch_run_config)
#ParseSwitch()
#ParseSwitch(switch_run_config1)

switchNameRegex = re.compile(r'(HZL.*[1-9])', re.IGNORECASE)

	
#SwitchConfig=['C:\Python27\mine\HZL-COLO-PRODTDNDH2-SWA1.txt','C:\Python27\mine\HZL-COLO-PRODTDNDH2-SWA2.txt']
#tableinfo = {}
#for Switchfile in SwitchConfig:
#	SwitchName=switchNameRegex.search(Switchfile).group(0)
#	print('Switch Name :' +  SwitchName )
#	Res=ReadSwitchConfigFromFile(Switchfile)
#	ParseSwitch(Res,Switchfile,SwitchName,tableinfo)
