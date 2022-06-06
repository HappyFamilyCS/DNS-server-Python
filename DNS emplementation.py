import dns.resolver     # importing DNS resolver
import sys
record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']  # list of DNS records
domain = sys.argv[1]    # gitting domain from terminal(system)
for records in record_types:
    answer = dns.resolver.resolve(domain, records)
    print(f'\n{records} Records')
    print('-' * 30)
    for server in answer:
        print(server.to_text())
