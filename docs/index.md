![ARIX Logo](https://arix.dev/logo.png)

# Amateur Radio Internet Exchange

Welcome to the Amateur Radio Internet Exchange. ARIX is an internet exchange point for licensed amateur radio
operators for the use of networking research, development, and education.

## Connectivity

- 2.4GHz 802.11n - Portland, OR
- 2.4GHz/5GHz 802.11n - Flagstaff, AZ
- SMF 1G-LX / 10G-LR or RJ45 (1G) - Hurricane Electric FMT2, Fremont, CA
- Virtual Machine - contact us for more information

## Contact

The ARIX team can be contacted by email at info@arix.dev, or join #arix on libera.chat for general discussion.

## Policy

If an ARIX member cause issues for the exchange, other members, or the internet at large, intentionally or
unintentionally, the offending port may be brought down until the issue is corrected.

- Only announce IP space that you're authorized to announce.
- Only IPv4, ARP, IPv6, and NDP L2 protocols are permitted.
- Only one MAC address per port without prior authorization.

## Route Servers

ARIX operates route servers to aid members in their peering endeavours. See the members table above for peering
information. The route servers run Pathvector and enforce strict IRR, RPKI, max-prefix, and Tier 1 ASN filtering. Please
keep your PeeringDB page up to date, as configuration is automatically built from PeeringDB.

## BGP Communities

All routes are tagged with 47192,1 and 47192:0:PEER_ASN where PEER_ASN is the ASN the route was learned from. To exclude
a route from being announced to all peers, add 47192,0. To exclude a route from being announced to a specific peer, add
47192:0:PEER_ASN (47192,PEER_ASN will work too if the peer's ASN fits in a 16-bit integer).
