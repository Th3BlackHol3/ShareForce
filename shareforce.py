#!/bin/python3

import sys
import requests

print('''

  ██████  ██░ ██  ▄▄▄       ██▀███  ▓█████   █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▒░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░    ░    ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
      ░   ░  ░  ░      ░  ░   ░        ░  ░           ░ ░     ░     ░ ░ v1.7    ░  ░
                                                                    ░               
Windows Sharepoint Directory Audit Tool | Sharepoint-Exploit: CVE-2019-0504 & CVE-2022-22005

Developed by Th3 BlackHol3
https://twitter.com/Th3BlackHol3_
https://www.linkedin.com/in/th3blackhol3/

Disclaimer: Use responsibly and only on authorized systems; the author assumes no liability for any misuse or illegal activities.
''')

directories = [
    "_vti_bin/_vti_adm/admin.dll",
    "_vti_bin/_vti_aut/author.dll",
    "_vti_bin/shtml.dll",
    "vti_bin",
    "_vti_bin/_vti_aut",
    "_vti_bin/_vti_adm",
    "_vti_pvt",
    "_vti_cnf",
    "_vti_txt",
    "_vti_log",
    "front_bin",
    "_vti_inf.html",
    "_vti_inf.html",
    "_vti_bin/shtml.dll/_vti_rpc",
    "_vti_bin/owssvr.dll",
    "_vti_bin/_vti_adm/admin.dll",
    "_vti_bin/_vti_adm/admin.exe",
    "_vti_bin/_vti_aut/author.exe",
    "_vti_bin/_vti_aut/WS_FTP.log",
    "_vti_bin/_vti_aut/ws_ftp.log",
    "_vti_bin/shtml.exe/_vti_rpc",
    "_vti_bin/_vti_aut/author.dll",
    "_vti_bin/Admin.asmx",
    "_vti_bin/alerts.asmx",
    "_vti_bin/dspsts.asmx",
    "_vti_bin/forms.asmx",
    "_vti_bin/Lists.asmx",
    "_vti_bin/people.asmx",
    "_vti_bin/Permissions.asmx",
    "_vti_bin/search.asmx",
    "_vti_bin/UserGroup.asmx",
    "_vti_bin/versions.asmx",
    "_vti_bin/Views.asmx",
    "_vti_bin/webpartpages.asmx",
    "_vti_bin/webs.asmx",
    "_vti_bin/spsdisco.aspx",
    "_vti_bin/AreaService.asmx",
    "_vti_bin/BusinessDataCatalog.asmx",
    "_vti_bin/ExcelService.asmx",
    "_vti_bin/SharepointEmailWS.asmx",
    "_vti_bin/spscrawl.asmx",
    "_vti_bin/spsearch.asmx",
    "_vti_bin/UserProfileService.asmx",
    "_vti_bin/WebPartPages.asmx",
    "_vti_pvt/authors.pwd",
    "_vti_pvt/administrators.pwd",
    "_vti_pvt/users.pwd",
    "_vti_pvt/service.pwd",
    "_vti_pvt/service.grp",
    "_vti_pvt/bots.cnf",
    "_vti_pvt/service.cnf",
    "_vti_pvt/access.cnf",
    "_vti_pvt/writeto.cnf",
    "_vti_pvt/botsinf.cnf",
    "_vti_pvt/doctodep.btr",
    "_vti_pvt/deptodoc.btr",
    "_vti_pvt/linkinfo.cnf",
    "_vti_pvt/services.org",
    "_vti_pvt/structure.cnf",
    "_vti_pvt/svcacl.cnf",
    "_vti_pvt/uniqperm.cnf",
    "_vti_pvt/service/lck",
    "_vti_pvt/frontpg.lck",
    "_vti_pvt/",
    "_vti_bin/",
    "_vti_log/",
    "_vti_cnf/",
    "_vti_bot",
    "_vti_bin/_vti_adm",
    "_vti_bin/_vti_aut",
    "_vti_txt",
    "_layouts/aclinv.aspx",
    "_layouts/addrole.aspx",
    "_layouts/AdminRecycleBin.aspx",
    "_layouts/AreaNavigationSettings.aspx",
    "_layouts/AreaTemplateSettings.aspx",
    "_layouts/AreaWelcomePage.aspx",
    "_layouts/associatedgroups.aspx",
    "_layouts/bpcf.aspx",
    "_layouts/ChangeSiteMasterPage.aspx",
    "_layouts/create.aspx",
    "_layouts/editgrp.aspx",
    "_layouts/editprms.aspx",
    "_layouts/groups.aspx",
    "_layouts/help.aspx",
    "_layouts/images/",
    "_layouts/listedit.aspx",
    "_layouts/ManageFeatures.aspx",
    "_layouts/mcontent.aspx",
    "_layouts/mngctype.aspx",
    "_layouts/mngfield.aspx",
    "_layouts/mngsiteadmin.aspx",
    "_layouts/mngsubwebs.aspx",
    "_layouts/mngsubwebs.aspx?view=sites",
    "_layouts/mobile/mbllists.aspx",
    "_layouts/MyInfo.aspx",
    "_layouts/MyPage.aspx",
    "_layouts/MyTasks.aspx",
    "_layouts/navoptions.aspx",
    "_layouts/NewDwp.aspx",
    "_layouts/newgrp.aspx",
    "_layouts/newsbweb.aspx",
    "_layouts/PageSettings.aspx",
    "_layouts/people.aspx",
    "_layouts/people.aspx?MembershipGroupId=0",
    "_layouts/permsetup.aspx",
    "_layouts/picker.aspx",
    "_layouts/policy.aspx",
    "_layouts/policyconfig.aspx",
    "_layouts/policycts.aspx",
    "_layouts/Policylist.aspx",
    "_layouts/prjsetng.aspx",
    "_layouts/quiklnch.aspx",
    "_layouts/recyclebin.aspx",
    "_layouts/RedirectPage.aspx",
    "_layouts/role.aspx",
    "_layouts/settings.aspx",
    "_layouts/SiteDirectorySettings.aspx",
    "_layouts/sitemanager.aspx",
    "_layouts/SiteManager.aspx?lro=all",
    "_layouts/spcf.aspx",
    "_layouts/storman.aspx",
    "_layouts/themeweb.aspx",
    "_layouts/topnav.aspx",
    "_layouts/user.aspx",
    "_layouts/userdisp.aspx",
    "_layouts/userdisp.aspx?ID=1",
    "_layouts/useredit.aspx",
    "_layouts/useredit.aspx?ID=1",
    "_layouts/viewgrouppermissions.aspx",
    "_layouts/viewlsts.aspx",
    "_layouts/vsubwebs.aspx",
    "_layouts/WPPrevw.aspx?ID=247",
    "_layouts/wrkmng.aspx",
    "Forms/DispForm.aspx",
    "Forms/DispForm.aspx?ID=1",
    "Forms/EditForm.aspx",
    "Forms/EditForm.aspx?ID=1",
    "Forms/Forms/AllItems.aspx",
    "Forms/MyItems.aspx",
    "Forms/NewForm.aspx",
    "Pages/default.aspx",
    "Pages/Forms/AllItems.aspx",
    "_catalogs/masterpage/Forms/AllItems.aspx",
    "_catalogs/wp/Forms/AllItems.aspx",
    "about/_vti_pvt/service.pwd.",
    "about/_vti_pvt/service.pwd",
    "service.pwd",
    "about/_vti_pvt/administrators.pwd",
    "about/_vti_pvt/administrators.pwd.",
    "administrators.pwd",
    "about/_vti_pvt/authors.pwd",
    "about/_vti_pvt/authors.pwd.",
    "_catalogs/wp/Forms/AllItems.aspx",
    "authors.pwdFrontPage",
]

def check_directories(base_url):
    for directory in directories:
        url = f"{base_url}/{directory}"
        response = requests.get(url)
        status_code = response.status_code
        print(f"{url} - Status Code: {status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python web_directory_brute_force.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
    check_directories(target_url)

