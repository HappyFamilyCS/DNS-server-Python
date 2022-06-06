import dns.resolver
import sys
import webbrowser


#it is code that we can directly access the web page  by ip Address that is Receved by DNS Server
domain_name=input("Enter Domain name --> ")
# there we check for errors
try: 
    answer = dns.resolver.resolve(domain_name, 'A')
    print(f'\nA is used for IP addresses')
    print('-' * 30)
    ip=''
    for server in answer:
        print(server.to_text())
        ip+=str(server)
# when the domain name that we entered is not mach and not find we print the below massege
except dns.resolver.NoNameservers:
    print(f"there is no maching IP address to {domain_name} ")
# this is for TTL when time out occure 
except dns.resolver.LifetimeTimeout:
    print("Life Time --> Time out")
# when there is no file in record
except dns.resolver.NoAnswer:
    pass
# when domain name not founded or exist in record
except dns.resolver.NXDOMAIN:
    print(f'{domain} does not exist.')
    quit()
# it is for kebaord interupt when we push some thing in keyboard
except KeyboardInterrupt:
    print('Quitting.')
    quit()

finally:
    webbrowser.open("https://www.google.com/search?q=" + ip)
    # webbrowser.open("https://www.google.com/search?q=" + domain_name)
