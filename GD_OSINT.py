import webbrowser
import time

_original_open = webbrowser.open

def delayed_open(url, *args, **kwargs):
    result = _original_open(url, *args, **kwargs)
    time.sleep(0.4)
    return result

webbrowser.open = delayed_open

sites=["instagram.com","twitter.com","tiktok.com","pinterest.com","github.com","linkedin.com","reddit.com"]
print("       Use a vpn and proxies to stay safe and ensure you're not getting tracked. You are solely responsible for your actions!  ALSO, open your preffered browser first." \
"")
while True:
    q = input("""Enter a number
[1]username
[2]phone
[3]name
[4]company files
[5]email
[6]gov files
[7]url recon
[8]ip
[9]dbs
[10]vuln
[11]internet archive
[12]Domain DNS lookup
[13]Quick URL checking
[14]info
[15]exit: """)

    if q=="15":
        print("Byeeeeeeeee")
        break

    elif q=="1":
        user=input("Enter username: ")
        for s in sites:
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+intext:"{user}"')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"+("profile"+OR+"account"+OR+"member")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"')
        webbrowser.open(f'https://www.google.Domain DNS lookupcom/search?q=inurl:{user}')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("leak"+OR+"paste"+OR+"dump")')

    elif q=="2":
        user=input("Enter phone number: ")
        for s in sites:
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+intext:"{user}"')
        webbrowser.open(f'https://www.google.com/search?q="{user}"')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("contact"+OR+"phone"+OR+"whatsapp")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("telegram"+OR+"signal"+OR+"viber")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+(filetype:pdf+OR+filetype:docx+OR+filetype:xlsx)')

    elif q=="3":
        user=input("Enter name and surname: ")
        user2=input("Enter keyword: ")
        user3=input("Enter a filetype? if not, press enter: ")
        if user3:
            webbrowser.open(f'https://www.google.com/search?q="{user}"+filetype:{user3}+intext:{user2}')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+intext:{user2}')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("email"+OR+"phone"+OR+"contact")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("resume"+OR+"cv"+OR+"portfolio")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("username"+OR+"profile"+OR+"account")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("leak"+OR+"paste"+OR+"dump")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("discord"+OR+"telegram"+OR+"github")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+(filetype:pdf+OR+filetype:docx+OR+filetype:xlsx+OR+filetype:csv)')
        for s in sites:
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"+"{user2}"')

    elif q=="4":
        user=input("Enter site: ")
        user2=input("Enter keyword: ")
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+filetype:pdf+intext:{user2}')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("confidential"+OR+"internal"+OR+"private"+OR+"restricted")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("employee+handbook"+OR+"onboarding"+OR+"vpn")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("sharepoint"+OR+"drive.google.com")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+intitle:"index+of"')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:admin+OR+inurl:login+OR+inurl:dashboard+OR+inurl:portal)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:jenkins+OR+inurl:grafana+OR+inurl:kibana)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:jira+OR+inurl:confluence)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:dev+OR+inurl:test+OR+inurl:staging)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("mysql+error"+OR+"Fatal+error"+OR+"Warning:"+OR+"stack+trace")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("exception"+OR+"debug"+OR+"failed")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(ext:bak+OR+ext:old+OR+ext:backup+OR+ext:zip+OR+ext:gz)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(filetype:pdf+OR+filetype:docx+OR+filetype:xlsx+OR+filetype:csv)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(filetype:log+OR+filetype:txt+OR+filetype:json+OR+filetype:xml)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+filetype:js')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+filetype:map')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(swagger+OR+"api-docs"+OR+"openapi")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:api+OR+inurl:v1+OR+inurl:v2)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+inurl:.git')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(".env"+OR+"config.php"+OR+"wp-config.php"+OR+"settings.py")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(".gitlab-ci.yml"+OR+"docker-compose.yml"+OR+"kubeconfig")')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"api+key"')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"token"')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"secret"')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("firebaseio.com"+OR+"amazonaws.com"+OR+"storage.googleapis.com")')

    elif q=="5":
        user=input("Enter email: ")
        for s in sites:
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+intext:"{user}"')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"+("profile"+OR+"account"+OR+"member")')
            webbrowser.open(f'https://www.google.com/search?q=site:{s}+"{user}"+("paste"+OR+"leak"+OR+"dump")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"')
        webbrowser.open(f'https://www.google.com/search?q=intext:"{user}"')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("contact"+OR+"about"+OR+"support")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("discord"+OR+"telegram"+OR+"github")')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+(filetype:pdf+OR+filetype:docx+OR+filetype:xlsx+OR+filetype:csv)')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("forum"+OR+"account"+OR+"member")')

    elif q=="6":
        user=input("Enter what file you want to see: ")
        user2=input("Enter keyword: ")
        user3=input("Enter title context: ")
        webbrowser.open(f'https://www.google.com/search?q=site:gov.gr+filetype:pdf+"{user}"+intext:{user2}+intitle:{user3}')
        webbrowser.open(f'https://www.google.com/search?q=site:gov.gr+(filetype:xlsx+OR+filetype:csv+OR+filetype:docx)+{user2}')
        webbrowser.open(f'https://www.google.com/search?q=site:gov.gr+("internal"+OR+"confidential")')

    elif q=="7":
        user=input("Enter site (example=recipes.com) : ")
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+-www+-mail')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:admin+OR+inurl:login+OR+inurl:dashboard+OR+inurl:portal)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+intitle:"index+of"')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:jenkins+OR+inurl:grafana+OR+inurl:kibana)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:jira+OR+inurl:confluence)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:staging+OR+inurl:dev+OR+inurl:test)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(".env"+OR+"config.php"+OR+"wp-config.php"+OR+"settings.py")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(".gitlab-ci.yml"+OR+"docker-compose.yml"+OR+"kubeconfig")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(filetype:sql+OR+filetype:log+OR+filetype:json+OR+filetype:xml+OR+filetype:txt+OR+filetype:bak)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(ext:bak+OR+ext:old+OR+ext:backup+OR+ext:zip+OR+ext:gz)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("mysql+error"+OR+"syntax+error"+OR+"Fatal+error"+OR+"Warning:")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("stack+trace"+OR+"exception"+OR+"debug")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+filetype:js')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+filetype:map')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(swagger+OR+"api-docs"+OR+"openapi")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:api+OR+inurl:v1+OR+inurl:v2)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+inurl:.git')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"api+key"')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"secret"')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"token"')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(filetype:pdf+OR+filetype:docx+OR+filetype:xlsx+OR+filetype:csv)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("firebaseio.com"+OR+"amazonaws.com"+OR+"storage.googleapis.com")')
        webbrowser.open(f'https://urlscan.io/search/#domain%3A{user}')
        webbrowser.open(f"https://www.virustotal.com/gui/domain/{user}")
        webbrowser.open(f"https://talosintelligence.com/reputation_center/lookup?search={user}")


    elif q=="8":
        user=input("Enter IP address: ")
        webbrowser.open(f'https://www.google.com/search?q="{user}"+intext:phone')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+intext:device')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+intitle:webcam')
        webbrowser.open(f'https://www.google.com/search?q="{user}"+("router"+OR+"camera"+OR+"iot")')
        webbrowser.open(f'https://urlscan.io/search/#*ip%3A{user}')
        webbrowser.open(f"https://www.virustotal.com/gui/ip-address/{user}")
        webbrowser.open(f"https://https://www.abuseipdb.com/check/{user}")

    elif q=="9":
        user=input("Enter site: ")
        user2=input("What do you want to see: ")
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+allintext:{user2}+(filetype:sql+OR+filetype:log+OR+filetype:txt+OR+filetype:csv)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(".env"+OR+"config.php"+OR+"wp-config.php"+OR+"settings.py")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(ext:sql+OR+ext:db+OR+ext:sqlite+OR+ext:mdb+OR+ext:bak)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(ext:zip+OR+ext:tar+OR+ext:gz+OR+ext:7z+OR+ext:rar)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("mysql+error"+OR+"sql+syntax"+OR+"PDOException"+OR+"Fatal+error")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("jdbc:mysql"+OR+"mongodb://"+OR+"postgres://")')
        webbrowser.open(f'https://www.google.com/search?q=site:github.com+"{user}"+"DATABASE_URL"')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("firebaseio.com"+OR+"mongodb.net"+OR+"rds.amazonaws.com")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(inurl:phpmyadmin+OR+inurl:adminer+OR+inurl:mysql+OR+inurl:db)')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+(filetype:xlsx+OR+filetype:csv)+("user"+OR+"email")')

    elif q=="10":
        user=input("Enter site: ")
        webbrowser.open(f'https://www.google.com/search?q=intext:{user}+intitle:"report"+("qualys"+OR+"acunetix"+OR+"nessus"+OR+"netsparker"+OR+"nmap")+filetype:pdf')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("CVE"+OR+"vulnerability"+OR+"exploit")')
        webbrowser.open(f'https://www.google.com/search?q=site:{user}+("outdated"+OR+"deprecated")')
        webbrowser.open(f"https://www.virustotal.com/gui/domain/{user}")

    elif q=="11":
        user=input("Enter full site URL:")
        webbrowser.open(f'https://web.archive.org/web/*/{user}')

    elif q=="12":
        user=input("Enter domain (exmaple=recipes.com) :")
        webbrowser.open(f"https://www.nslookup.io/domains/{user}/dns-records/")

    elif q=="13":
        user=input("Enter the full site URL:")
        webbrowser.open(f"https://www.virustotal.com/gui/domain/{user}")

    elif q=="14":
        print("""
[1] Username          - Searches websites and Google for usernames, profiles, leaks, mentions.
[2] Phone             - Finds phone numbers across websites, documents, contacts, messaging platforms.
[3] Name              - Searches people, documents, profiles, resumes, accounts, and mentions.
[4] Company Files     - Finds indexed company documents, portals, backups, configurations, exposures.
[5] Email             - Searches public references, accounts, leaks, documents containing email.
[6] Gov Files         - Finds government documents, spreadsheets, records, and public files.
[7] URL Recon         - Maps website assets, portals, files, APIs, infrastructure exposure.
[8] IP                - Searches public information associated with specific IP addresses.
[9] DBS               - Finds exposed databases, backups, connection strings, database resources.
[10] Vuln             - Searches vulnerability reports, CVEs, exploits, security-related information.
[11] Internet Archive - Views historical website snapshots and previously archived content.
[12]Domain DNS lookup - Displays public DNS records, mail servers, nameservers, TXT records, and domain configuration.
[13]Quick URL checking- Displays if a website contains malicious content
""")

    else:
        print("Enter a number brahhhhh :)")