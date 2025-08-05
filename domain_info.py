#version 1.0 - fix the output to display in json format. 7/30/25
#version 1.1 - added json output. 8/4/25
import dns.resolver
import json
import pyfiglet

def get_dns_info(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT', 'SOA', 'SRV', 'CAA', 'HINFO', 'CERT']
    dns_info = {}

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            dns_info[record] = [rdata.to_text() for rdata in answers]
        except Exception as e:
            dns_info[record] = f"Error: {e}"

    return dns_info
banner = pyfiglet.figlet_format("SITE DNS INFO")
print(banner)
site = input('Enter the site: ')

web_site = get_dns_info(site)
formatted_out = json.dumps(web_site, indent=4)

print(formatted_out)