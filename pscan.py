#PLATFORM "[ANDROID,LINUX,Windows,Dos,Mac]" #KOFEIT#
#PACKAGE "PortScanner-1" #KOFEIT#
#TYPE "[Hacking,Pentest]" #KOFEIT#
#VERSION "1.0" #KOFEIT#
#LANGUAGE "Python" #KOFEIT#
#AUTHOR "SINOCE" #KOFEIT#
#TYPE_RUN "REMOTE"  #KOFEIT#
#USY 3 #KOFEIT#
from Kofeit import *
import socket,os

class KOFEIT():

    def __init__(self) -> None:
        self.module_info = {
            "module_type":{
                "Hacking":True,
                "Cracking":False,
                "PenTest":True,
                "SessionHijacking":False,
                "CSRF":False,
                "APT":False
            },

        "platform_target":{
                """
    Android:Supported(Termux & Pydroid3)
    Linux:Supported
    Windows":"Supported
    Dos:Supported
    Mac:Supported
                """,
            },
            "module_language":"Python",
            "ctime":"1402/12/25 14:12",
            "version":1.0
            }
        self.module_name = "PortScan-1 #KOFEIT#"
        self.options_types = {
            "PortRange":"<class 'str'>",
            "PortList":"<class 'str'>",
            "HostName":"<class 'str'>",
            "HostList":"<class 'str'>",
            "Domain":"<class 'str'>",
            "ScanType":"<class 'str'>",
        }
        self.options = {
            "PortRange":"",
            "PortList":"",
            "HostName":"",
            "HostList":"",
            "Domain":"",
            # "DomainList":"",
            "ScanType":"DEFAULT",
        }
        self.rq = {}
        self.author = "Sinoce-HSC"
        self.description = "Only PortScanner Easy ."
    def info(self):
        language = self.module_info["module-language"]
        platform = self.module_info["platform_target"]
        ctime = self.module_info['ctime']
        version  = self.module_info['version']
        print_status("#6[#2*#6] #0" + f"Module-Name:{self.module_name}\nLanguage-Module:{language}\nPlatform-Supported:\n[\n{platform}\n]\nDescription:{self.description}\nAuthor:{self.author_module}\nTime-Created:{ctime}\nVersion:{version}", True)
    def check_variable(self,var):
        if var:return True
        else:return False
    def show_options(self):
        PortRange:str=self.options["PortRange"]
        PortList:str=self.options["PortList"]
        HostName:str=self.options["HostName"]
        HostList:str=self.options["HostList"]
        ScanType:str=self.options["ScanType"]
        print_status("-"*5 +f"LIST Options:" + "-"*5+f"""\nKey        Value\nPortList : {self.options['PortList']} [{self.check_variable(self.options['PortList'])}]\nHostList : {self.options['HostList']} [{self.check_variable(self.options['HostList'])}]\n""" +"-"*5+"String Options:" + "-"*5+f"""\nHostName : {self.options['HostName']} [{self.check_variable(self.options['HostName'])}]\nPortRange:{self.options['PortRange']} [{self.check_variable(self.options['PortRange'])}]\nDomain : {self.options['Domain']} [{self.check_variable(self.options['Domain'])}]\nScanType:{self.options['ScanType']} [{self.check_variable(self.options['ScanType'])}]\n""", True)
    def create_client(self,typec:str="UDP"):
        if typec == "TCP":
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif typec == "UDP":
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif typec == "DEFAULT":
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def set_value(self,key,value):
        if key in self.options:
            if self.options_types[key] == "<class 'list'>"  and str(type(value)) == "<class 'str'>":
                value = value.split(",")
                self.options[key] = value
                value_str = '[ ' + " | ".join(value) + ' ]'
                print_status("#6[#2*#6] #0" + f"#1{key} #3=#2>#66 {value_str}#0",True)
            elif self.options_types[key] == "<class 'str'>" and str(type(value)) == "<class 'str'>":
                self.options[key] = value
                print_status("#6[#2*#6] #0" + f"#1{key} #3=#2>#66 {value}#0",True)
            else:
                print_no(f"#4Type#2 {key}#3 Is #1{self.options_types[key]} #2can't #22set #5 > #22{str(type(value))}#0",True)
        else:
            print_no(f"#1{key}#22 Invalid #66(#1{key}#66) #4Not#3 Found #2!#0",True)
    def help(self):
        print_status(f"""
#2info #3ARGS#5[#22None#5] #6(#55Show info Module #11{self.module_name.split(" ")[0]}#6)
#2set #3/ #2set_value #3ARGS#5[#2<#1KEY#2> #2<#1VALUE#2>#5] #6(#55Set A Key To Value#6)
#2show options #3/ #2show_options #3ARGS#5[#22None#5] #6(#55Show the options Module #11{self.module_name.split(" ")[0]}#6)
#2check #3ARGS#5[#22None#5] #6(#55Check Options Seted and Module #11{self.module_name.split(" ")[0]}#6)
#2exploit #3/ #2run #3ARGS#5[#22None#5] #6(#55run the module #11{self.module_name.split(" ")[0]}#6)""",True)
    def check(self):
        if self.check_variable(self.options['PortRange']):
            self.rq['PORT'] = self.options['PortRange']
            print_ok("#2PortRange#1 Verifyed #5.#0",True)
        elif self.check_variable(self.options['PortList']):
            if os.path.isfile(self.options['PortList']):
                PortList = open(self.options['PortList']).read().splitlines()
                if len(PortList) > 0 and PortList:
                    self.rq["PORT"] = PortList
                    print_ok("#2PortList #1Verifyed #5.#0",True)
        else:
            print_no("#66[#1PortRange#3/#1PortList#66] #2Is #4 Required #2!#0")
        if self.check_variable(self.options['HostName']):
            self.rq['IP_ADDR'] = self.options['HostName']
            print_ok("#33IP_ADDR #2=#55>#22 HostName #1Verifyed #5.#0",True)
        elif self.check_variable(self.options['HostList']):
            if os.path.isfile(self.options['HostList']):
                HostList = open(self.options['HostList']).read().splitlines()
                if len(HostList) > 0 and HostList:
                    self.rq['IP_ADDR'] = HostList
                    print_ok("#33IP_ADDR #2=#55>#22 HostList #1Verifyed #5.#0",True)
        else:
            if self.check_variable(self.options['Domain']):
                try:
                    ADDR_DOMAIN = socket.gethostbyname(self.options['Domain'])
                    self.rq['IP_ADDR'] = ADDR_DOMAIN
                    print_ok("#33IP_ADDR #2=#55>#22 Domain #1Verifyed #5.#0",True)
                except socket.gaierror:
                    print_no("#1D#2N#3S#4(#1Domain Name Server#3)#2 Invalid #5!#0")
                except TimeoutError:
                    print_no("#1Time#2Out #22Error #5!#0")
            else:
                print_no("#66[#1 IP Address Target#66] #2Is #4 Required #2!#0")


        if self.check_variable(self.options['ScanType']):
            ScanType = self.options['ScanType']
            if ScanType.upper() == "UDP":
                print_ok(f"#2ScanType #44[#66{ScanType}#44] #1Verifyed#5 .#0",True)
            elif ScanType.upper() == "TCP":
                print_ok(f"#2ScanTypee #44[#66{ScanType}#44] #1Verifyed#5 .#0",True)
            elif ScanType.upper() == "DEFAULT":
                print_star("#2ScanType #1Default#3=#44[#66TCP#44]#0 .",True)
            else:
                print_no("#1ScanType#2 Is #22not #4Defined #5!#0")


    def exploit(self):
        IP_ADDR = self.rq["IP_ADDR"]
        PORT = self.rq["PORT"]
        OPEN_PORT = []
        print_ok("#11Please #66Wait #1.#2.#3.#0",True)
        print_ok(f"#1IP #22Address #4:#5 (#66{IP_ADDR}#5) #0",True)
        if type(PORT) == str:
            StartRange,EndRange = self.options['PortRange'].split("-")
            client = self.create_client(self.options['ScanType'])
            client.settimeout(1.5)
            for PORT in range(int(StartRange), int(EndRange) + 1):
                try:
                    client.connect((IP_ADDR, PORT))
                except socket.gaierror:
                    print_no("#1D#2N#3S#4(#1Domain Name Server#3)#2 Invalid #5!#0",True)
                    break
                except TimeoutError:
                    print_no(f"#1Time#2Out #22Error #1On #2Port#4:#5(#66{PORT}#5) #5!#0",True)
                except:
                    ...
                else:
                    OPEN_PORT.append(int(PORT))
                print_status("\r"+f"#6[#2*#6] #1Proccessing #2Port#3:#4(#66{PORT}#4) #0",end=False)
                open(f"Scan-{IP_ADDR}.scan",'ab+').write(str("\nOPEN-PORT".join(OPEN_PORT)).encode())
            print_ok(f"#11Scan Done#4 Result #2Saved On #3(#1Scan-{IP_ADDR}.scan#3)#0",True)
        else:
            PORTS = [PORTS.append(P) for P in PORT]
            self.rq['CLIENT'].settimeout(2)
            for PORT in PORTS:
                try:
                    self.rq['CLIENT'].connect((IP_ADDR, int(PORT)))
                except socket.gaierror:
                    print_no("#1D#2N#3S#4(#1Domain Name Server#3)#2 Invalid #5!#0",True)
                    break
                except TimeoutError:
                    print_no("#1Time#2Out #22Error #5!#0",True)
                else:
                    OPEN_PORT.append(int(PORT))
                print_status("\r"+f"#6[#2*#6] #1Proccessing #2Port#3:#4(#66{PORT}#4) #0",end=False)
            open(f"Scan-{IP_ADDR}.scan",'ab+').write(str("\nOPEN-PORT".join(OPEN_PORT)).encode())
            print_ok(f"#11Scan Done#4 Result #2Saved On #3(#1Scan-{IP_ADDR}.scan#3)#0",True)