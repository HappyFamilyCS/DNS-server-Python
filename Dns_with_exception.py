import dns.resolver     # importing DNS resolver
import sys
record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']  # list of DNS records
try:
    domain = sys.argv[1]    # gitting domain from terminal(system)
except IndexError:
    print('Syntax error - python3 dnsenum.py domainname')

for records in record_types:
    try:# it check for errors
        answer = dns.resolver.resolve(domain, records)
        print(f'\n{records} Records')
        print('-' * 30)
        for server in answer:
            print(server.to_text())

    except dns.resolver.NoAnswer:#wheb no answer found
        pass
    except dns.resolver.NXDOMAIN:# when the domain name is wrong or not exist
        print(f'{domain} does not exist.')
        quit()
        
    except KeyboardInterrupt:#keyboard interups
        print('Quitting.')
        quit()
