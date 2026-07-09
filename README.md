# 🔎 Google Dork Automation Tool

A lightweight Python utility that automates **Google Dork** queries for **OSINT, reconnaissance, and defensive security research**. Instead of manually crafting dozens of search operators, simply choose a search category, enter your target, and let the tool generate and launch a curated collection of advanced Google searches.

Designed for **security researchers, bug bounty hunters, penetration testers, CTF players, and OSINT investigators** who want to speed up public information gathering.

---

## 🚀 Features

* 👤 Username investigation
* 📧 Email footprint discovery
* 📱 Phone number searches
* 🧑 Name-based OSINT
* 🏢 Company document discovery
* 🏛 Government file searches
* 🌐 Website & domain reconnaissance
* 🗄 Database & backup exposure discovery
* 🖥 IP address intelligence
* 🛡 Vulnerability & CVE research
* 🕰 Internet Archive lookups
* 📡 DNS record lookup
* ✅ Quick URL reputation checking

---

## 📋 Search Categories

| Option               | Description                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Username**         | Search usernames across popular platforms, public mentions, profiles, and indexed content.                                   |
| **Phone**            | Discover publicly indexed phone numbers, contact information, messaging accounts, and documents.                             |
| **Name**             | Search people, resumes, portfolios, online profiles, documents, and public mentions.                                         |
| **Company Files**    | Locate indexed PDFs, Office documents, backups, portals, dashboards, APIs, configuration files, and other exposed resources. |
| **Email**            | Search for public references, accounts, documents, leaks, and mentions associated with an email address.                     |
| **Gov Files**        | Search publicly indexed government documents, spreadsheets, datasets, and reports.                                           |
| **URL Recon**        | Enumerate indexed pages, login portals, APIs, JavaScript files, backups, exposed assets, and infrastructure.                 |
| **IP**               | Gather publicly available information related to an IP address using search engines and reputation services.                 |
| **DBS**              | Locate exposed database backups, dumps, connection strings, configuration files, and related resources.                      |
| **Vuln**             | Search for public vulnerability reports, CVEs, exploits, security advisories, and scan reports.                              |
| **Internet Archive** | Open archived snapshots of websites using the Wayback Machine.                                                               |
| **DNS Lookup**       | View public DNS records including A, MX, TXT, NS, and other domain information.                                              |
| **Quick URL Check**  | Quickly inspect a domain's reputation using VirusTotal.                                                                      |

---

## ⚡ Requirements

* Python 3.x
* Internet connection
* Any modern web browser

**No third-party libraries are required.**

---

## ▶️ Usage

```bash
python dork.py
```

Select one of the available search categories, provide the requested input, and the tool will automatically launch multiple Google Dork queries in your default browser.

---

## 🔍 Google Operators Used

The tool makes extensive use of advanced Google search operators, including:

* `site:`
* `inurl:`
* `intext:`
* `intitle:`
* `filetype:`
* `ext:`

These operators help identify publicly indexed content more efficiently and reduce manual query creation.

---

## 🧰 Integrated Resources

The toolkit also provides quick access to several public security and OSINT resources, including:

* Google Search
* VirusTotal
* URLScan.io
* Cisco Talos Intelligence
* Internet Archive (Wayback Machine)
* NSLookup.io

---

## 🎯 Intended Use

This project is useful for:

* 🛡 Defensive Security Research
* 🔎 Open Source Intelligence (OSINT)
* 🐞 Bug Bounty Reconnaissance
* 🔐 Authorized Penetration Testing
* 🏴 Capture The Flag (CTF) Challenges
* 🌐 Asset Discovery
* 📚 Cybersecurity Education

---

## ⚠️ Disclaimer

This tool **does not exploit vulnerabilities, bypass authentication, or access non-public systems**. It simply automates searches against **publicly indexed information** using Google search operators and well-known OSINT resources.

Use this tool **only on systems you own or are explicitly authorized to assess**. You are solely responsible for complying with applicable laws, regulations, and the terms of service of any platforms or services you use. The author assumes no responsibility for misuse.

---

## ⭐ Contributing

Contributions, bug reports, feature requests, and pull requests are always welcome.

If you find this project useful, consider giving it a **⭐ Star** to support future development.
