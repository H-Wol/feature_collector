# Collector

## 사용 API

> 1.  VirusTotal
>
> - File Hash(sha1, sha256, md5) -> https://www.virustotal.com/api/v3/files/{id}
>   - https://developers.virustotal.com/reference/file-info
> - URL -> https://www.virustotal.com/api/v3/urls/{id}
>   - https://developers.virustotal.com/reference/url-info
> - Domain -> https://www.virustotal.com/api/v3/domains/{domain}
>   - https://developers.virustotal.com/reference/domain-info
> - IPs -> https://www.virustotal.com/api/v3/ip_addresses/{ip}
>   - https://developers.virustotal.com/reference/ip-info
>
> 2. MalwareBazaar
>
> - File Hash(sha1, sha256, md5) -> https://mb-api.abuse.ch/api/v1/ (form-data -> query:get_info, hash:hash)
>   - https://bazaar.abuse.ch/api/#query_hash
>
> 3. URLhaus
>
> - File Hash(sha256, md5) -> https://urlhaus-api.abuse.ch/v1/payload/ (form-data->md5_hash:md5 / sha256_hash:sha256)
>   - https://urlhaus-api.abuse.ch/#payloadinfo
> - URL ->https://urlhaus-api.abuse.ch/v1/url/ (form-data -> url:url)
>   - https://urlhaus-api.abuse.ch/#urlinfo
> - Domain/IPs -> https://urlhaus-api.abuse.ch/v1/host/ (form-data -> host:Domain/IPs)
>   - https://urlhaus-api.abuse.ch/#hostinfo

> 4. OTX
>
> - https://otx.alienvault.com/assets/static/external_api.html#Home
> - File Hash(sha1, sha256, md5) -> https://otx.alienvault.com/api/v1/indicators/file/{file_hash}/{section}
>   - section
>     - general: General metadata about the file hash, and a list of the other sections currently available for this hash.
>     - analysis: dynamic and static analysis of this file (Cuckoo analysis, exiftool, etc.)
> - URL -> https://otx.alienvault.com/api/v1/indicators/url/{url}/{section}
>   - section
>     - general: Historical geographic info, any pulses this indicator is on, list of the other sections currently available for this URL.
>     - url_list: Full results (potentially multiple) from AlienVault Labs url analysis.
> - Domain -> https://otx.alienvault.com/api/v1/indicators/domain/{domain}/{section}
>   - section
>     - general: General information about the domain, including any pulses, and a list of the other sections currently available for this domain.
>     - geo: A more verbose listing of geographic data (Country code, coordinates, etc.)
>     - malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this domain.
>     - url_list: URLs analyzed by AlienVault Labs on this domain.
>     - passive_dns: Passive dns records observed by AlienVault Labs pointing to this domain.
>     - whois: Whois records for the domain.
>     - http_scans: Meta data for http(s) connections to the domain.
> - IPs(v4) -> https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/{section}
>   - section
>     - general: General information about the IP, such as geo data, and a list of the other sections currently available for this IP address.
>     - reputation: OTX data on malicious activity observed by AlienVault Labs (IP Reputation).
>     - geo: A more verbose listing of geographic data (Country code, coordinates, etc.)
>     - malware: Malware samples analyzed by AlienVault Labs which have been observed connecting to this IP address.
>     - url_list: URLs analyzed by AlienVault Labs which point to or are somehow associated with this IP address.
>     - passive_dns: passive dns information about hostnames/domains observed by AlienVault Labs pointing to this IP address.
>     - http_scans: Meta data for http(s) connections to the IP.

## 초기 설정

> 1.

## 사용 방법

> 1. python {ioc/file} -gn {공격 그룹 명(option)}
>    > 단일 ioc의 경우 입력한 공격 그룹명이 없을 경우 공격 그룹명이 etc로 저장
>    >
>    > 파일의 경우 파일명으로 공격 그룹명이 지정됨

> 2. 해당 요청은 실행 경로의 KISA/{공격 그룹명}/{ioc*요청API*세부API}.json로 저장
>    > 단일 ioc의 경우 공격 그룹명이 없을 경우 etc 폴더로 저장
>    >
>    > 동일 공격 그룹의 동일 ioc의 경우 덮어씌워짐
>    >
>    > 요청 실패의 경우 빈 파일로 저장
>    >
>    > VirusTotal의 경우 하루 500건 이상은 요청되지 않음 (시도한 당일 요청 횟수는 feature_collector/feature_collector/api/config/config.ini 에 표기)

## 쉘 사용방법

> 1. KISA {ioc/file} -gn {공격 그룹 명(option)}
>    > 단일 ioc의 경우 입력한 공격 그룹명이 없을 경우 공격 그룹명이 etc로 저장
>    >
>    > 파일의 경우 파일명으로 공격 그룹명이 지정됨

> 2. 해당 요청은 요청경로의 KISA/{공격 그룹명}/{ioc*요청API*세부API}.json로 저장
>    > 단일 ioc의 경우 공격 그룹명이 없을 경우 etc 폴더로 저장
>    >
>    > 동일 공격 그룹의 동일 ioc의 경우 덮어씌워짐
>    >
>    > 요청 실패의 경우 빈 파일로 저장
>    >
>    > VirusTotal의 경우 하루 500건 이상은 요청되지 않음 (시도한 당일 요청 횟수는 feature_collector/feature_collector/api/config/config.ini 에 표기)
