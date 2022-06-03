# DNS-server-Python
DNS Server in Python programming language

What is DNS?

The DNS is a system of records of domain names and IP addresses that allows browsers to find the right IP address that corresponds to a hostname URL entered into it. When we try to access a website, we generally type in their domain names, like cdnetworks.com or wired.com or nytimes.com, into the web browser. Web browsers however need to know the exact IP addresses to load content for the website. The DNS is what translates the domain names to the IP addresses so that the resources can be loaded from the website’s server.

Sometimes, websites can have numerous IP addresses corresponding to a single domain name. For example, large sites like Google will have users querying a server from distant parts of the world. The server that a computer from Singapore tries to query will likely be different from the one a different computer from say Toronto will try to reach, even if the site name entered in the browser is the same. This is where DNS caching comes in.

How Does a DNS Work?

The DNS is responsible for converting the hostname, what we commonly refer to as the website or web page name, to the IP address. The act of entering the domain name is referred to as a DNS query and the process of finding the corresponding IP address is known as DNS resolution.

DNS queries can be of three types: recursive query, iterative query or non-recursive query.

    Recursive query – These are queries where a DNS server has to respond with the requested resource record. If a record cannot be found, the DNS client has to be shown an error message.
    Iterative query – These are queries for which the DNS client will continue to request a response from multiple DNS servers until the best response is found, or an error or timeout occurs. If the DNS server is unable to find a match for the query, it will refer to a DNS server authoritative for a lower level of the domain namespace. This referral address is then queried by the DNS client and this process continues with additional DNS servers.
    Non-recursive query – these are queries which are resolved by a DNS resolver when the requested resource is available, either due to the server being authoritative or because the resource is already stored in cache.
