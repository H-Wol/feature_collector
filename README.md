Collector
===

사용 API
---

>1. VirusTotal
> + File Hash(sha1, sha256, md5) -> https://www.virustotal.com/api/v3/files/{id}
>     + https://developers.virustotal.com/reference/file-info
> + URL -> https://www.virustotal.com/api/v3/urls/{id}
>     + https://developers.virustotal.com/reference/url-info
> + Domain -> https://www.virustotal.com/api/v3/domains/{domain}
>     + https://developers.virustotal.com/reference/domain-info
> + IPs -> https://www.virustotal.com/api/v3/ip_addresses/{ip}
>     + https://developers.virustotal.com/reference/ip-info
>
> 2. MalwareBazaar
> + File Hash(sha1, sha256, md5) -> https://mb-api.abuse.ch/api/v1/ (form-data -> query:get_info)
>     + https://bazaar.abuse.ch/api/#query_hash
>
> 3. URLhaus
>
> 4. OTX
> + https://otx.alienvault.com/assets/static/external_api.html#Home
> + File Hash(sha1, sha256, md5) -> https://otx.alienvault.com/api/v1/indicators/file/{file_hash}/{section}
>    + section
>         + general: General metadata about the file hash, and a list of the other sections currently available for this hash.
>         + analysis: dynamic and static analysis of this file (Cuckoo analysis, exiftool, etc.)
> + URL -> https://otx.alienvault.com/api/v1/indicators/url/{url}/{section}
>     + section
>         + general: Historical geographic info, any pulses this indicator is on, list of the other sections currently available for this URL.
>         + url_list: Full results (potentially multiple) from AlienVault Labs url analysis.
> + Domain -> https://otx.alienvault.com/api/v1/indicators/domain/{domain}/{section}
>     + section
>         + general: General information about the domain, including any pulses, and a list of the other sections currently available for this domain.
>         + geo: A more verbose listing of geographic data (Country code, coordinates, etc.)
>         + malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this domain.
>         + url_list: URLs analyzed by AlienVault Labs on this domain.
>         + passive_dns: Passive dns records observed by AlienVault Labs pointing to this domain.
>         + whois: Whois records for the domain.
>         + http_scans: Meta data for http(s) connections to the domain.
> + IPs(v4) -> https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/{section}
>     + section
>         + general: General information about the IP, such as geo data, and a list of the other sections currently available for this IP address.
>         + reputation: OTX data on malicious activity observed by AlienVault Labs (IP Reputation).
>         + geo: A more verbose listing of geographic data (Country code, coordinates, etc.)
>         + malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this IP address.
>         + url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this IP address.
>         + passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this IP address.
>         + http_scans: Meta data for http(s) connections to the IP.
> + IPs(v6) -> https://otx.alienvault.com/api/v1/indicators/IPv6/{ip}/{section}
>     + section
>         + general: General information about the IP, such as geo data, and a list of the other sections currently available for this IP address.
>         + reputation: OTX data on malicious activity observed by AlienVault Labs (IP Reputation).
>         + geo: A more verbose listing of geographic data (Country code, coordinates, etc.)
>         + malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this IP address.
>         + url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this IP address.
>         + passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this IP address.



