#PLATFORM "[Unix,Linux,Windows,Mac,Dos]" #KOFEIT#
#PACKAGE "HACA" #KOFEIT#
#TYPE "[Hacking,Cracking]" #KOFEIT#
#VERSION "1" #KOFEIT#
#LANGUAGE "Python" #KOFEIT#
#AUTHOR "Sinoce" #KOFEIT#
#TYPE_RUN "Remote"  #KOFEIT#
#USY 6 #KOFEIT#
from Kofeit import *
import hashlib,time

class KOFEIT():

    def __init__(self) -> None:
        self.accept = False
        self.hash_types = {
            'md5':hashlib.md5,
            'sha1':hashlib.md5,
            'sha224':hashlib.sha224,
            'sha384':hashlib.sha384,
            'sha512':hashlib.sha512,
            'blake2b':hashlib.blake2b,
            'blake2s':hashlib.blake2s,
            'sha3_224':hashlib.sha3_224,
            'sha3_256':hashlib.sha3_256,
            'sha3_384':hashlib.sha3_384,
            'sha3_512':hashlib.sha3_512,
            'shake_128':hashlib.shake_128,
            'shake_256':hashlib.shake_256}
        self.module_info = {
            "module_type":{
                "APT":False,
                "Hacking":True,
                "Pentest":True,
                "Cracking":True,
                "SessionHijacking":False,
            },
            "platform_target":"""
            Windows":"Supported
            Linux:Supported
            Dos:Supported
            Mac:Supported
            Android: Termux(Simulator Terminal Linux) & Pydroid3 (Python3 On Android +4)""",
            "module_language":"Python",
            "ctime":"2024/19/4 12:45",
            "version":1
        }
        self.module_name = "HACA #KOFEIT#"
        self.option_types = {
            "hash":"<class 'str'>",
            "hash_type":"<class 'str'>",
            "passwordlist":"<class 'str'>",
        }
        self.options = {
            "hash":"",
            "hash_type":"",
            "passwordlist":"wordlists\\wordlist_hash.txt",
        }
        self.author = "Sinoce-HSC"
        self.description = "Tools For Crack Only Hashes (md5, sha1, sha224, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256)"
    
    def info(self):
        language = self.module_info["module_language"]
        platform = self.module_info["platform_target"]
        ctime = self.module_info['ctime']
        version  = self.module_info['version']
        print_status("#6[#2*#6] #0" + f"Module-Name:{self.module_name}\nLanguage-Module:{language}\nPlatform-Supported:\n[\n{platform}\n]\nDescription:{self.description}\nAuthor:{self.author}\nTime-Created:{ctime}\nVersion:{version}", True)
    
    def check_variable(self,var):
        if var:return True
        else:return False

    def show_options(self):
        print_status(f"""
Key		             Value
======================================
hash           :           {self.options['hash']}
hash_type      :           {self.options['hash_type']}
passwordlist   :           {self.options['passwordlist']}""",True)

    def set_value(self, key, value):
        if key in self.options:
            if self.option_types[key] == "<class 'list'>"  and str(type(value)) == "<class 'str'>":
                value = value.split(",")
                self.options[key] = value
                value_str = '[ ' + " | ".join(value) + ' ]'
                print_status("#6[#2*#6] #0" + f"#1{key} #3=#2>#66 {value_str}#0",True)
            elif self.option_types[key] == "<class 'str'>" and str(type(value)) == "<class 'str'>":
                self.options[key] = value
                print_status("#6[#2*#6] #0" + f"#1{key} #3=#2>#66 {value}#0",True)
            else:
                print_no(f"#4Type#2 {key}#3 Is #1{self.option_types[key]} #2can't #22set #5 > #22{str(type(value))}#0",True)
        else:
            print_no(f"#1{key}#22 Invalid #66(#1{key}#66) #4Not#3 Found #2!#0",True)

    def help(self):
        print_status(f"""
#2info #3ARGS#5[#22None#5] #6(#55Show info Module #11{self.module_name.split(" ")[0]}#6)
#2set #3/ #2set_value #3ARGS#5[#2<#1KEY#2> #2<#1VALUE#2>#5] #6(#55Set A Key To Value#6)
#2show options #3/ #2show_options #3ARGS#5[#22None#5] #6(#55Show the options Module #11{self.module_name.split(" ")[0]}#6)
#2check #3ARGS#5[#22None#5] #6(#55Check Options Seted and Module #11{self.module_name.split(" ")[0]}#6)
#2exploit #3/ #2run #3ARGS#5[#22None#5] #6(#55run the module #11{self.module_name.split(" ")[0]}#6)
#33Values:\n\tType:[rans / virus / rce / worm / rkit]\n\tRisk:[1 / 2 / 3]\n\tOutput:[Filename Save]""",True)
    
    def check(self):
        if self.check_variable(self.options['hash']):
            print_ok("#1Hash #1Verifyed #5.#0",True)

            if self.options['hash_type'] in self.hash_types:
                self.hash_creator = self.hash_types[self.options['hash_type']]
                print_ok("#Hash_Type #1Verifyed #5.#0",True)
            
                if self.check_variable(self.options['passwordlist']):

                    if os.path.isfile(self.options['passwordlist']):
                        rdata = open(self.options['passwordlist']).read().splitlines()

                        if self.check_variable(rdata):
                            print_ok("#2PasswordList #1Verifyed #5.#0",True)
                            self.accept = True
                        else:
                            print_status("#2Please Enter #22Passwordlist #22Not #1Empty #5!#0", True)

                    else:
                        print_status("#2Please Enter #22Passwordlist #1Valid #5!#0", True)

                else:
                    print_status("#2Please Enter #22Passwordlist #3File #5!#0", True)

            else:
                print_status("#2Please Enter #22Valid #3hash_type #5!#0", True)
        
        else:
            print_status("#2Please #22Enter #4Hash #1Input#5 !#0", True)
    
    def ch(self, n, o):
        nh,nm,ns = n.split(":")
        oh,om,os = o.split(":")
        final_time = F"{int(oh)-int(nh)}:{int(om)-int(nh)}:{int(os)-int(ns)}"
        return final_time

    def exploit(self):
        if self.accept:
            try:
                passwordlist = open(self.options['passwordlist']).read().splitlines()
                xnum = 1
                start_time = time.strftime('%H:%M:%S')
                for password in passwordlist:
                    hash_encode = self.hash_creator(password.encode()).hexdigest()
                    if hash_encode == self.options['hash']:
                        end_time = time.strftime('%H:%M:%S')
                        print_ok(f"\n#22Hash #3Cracked #4Input#5:#11{password} #66Hash#5:#11{self.options['hash']} Time : {self.ch(start_time,end_time)}", True)
                        break
                    else:
                        print_flush(f"#44Testing #2Input #5:#6 {password} #2Hash #5:#3 {hash_encode} [{xnum} / {len(passwordlist)}]",False)
                        xnum += 1
            except KeyboardInterrupt:
                print_star("#22Canceled #3By #4User#5 !#0",True)
        else:
            print_status("#2 Please#3 Type check to check and again back #5!#0", True)