# Route Servers

The ARIX route servers use AS47192 on the following addresses:
- 44.190.42.253
- 2602:801:30ff::253
- 44.190.42.254
- 2602:801:30ff::254

The route servers run [BIRD](https://bird.network.cz) and [Pathvector](https://pathvector.io) and enforce strict IRR, RPKI, max-prefix, and Tier 1 ASN filtering.

Please keep your PeeringDB page up to date, as configuration profiles are built automatically.

## BGP Communities

All routes are tagged with 47192,1 and 47192:0:PEER_ASN where PEER_ASN is the ASN the route was learned from. To exclude
a route from being announced to all peers, add 47192,0. To exclude a route from being announced to a specific peer, add
47192:0:PEER_ASN (47192,PEER_ASN will work too if the peer's ASN fits in a 16-bit integer).

The route servers pass along all communities to peers (NO_EXPORT for example).

### Info

| Community   | Large Community | Description                |
|:------------|:----------------|:---------------------------|
| 47192:47192 | 47192:1:47192   | Added to all routes        |
|             | 47192:2:x       | Learned from ASx           |

### Action

| Community | Large Community | Description                |
|:----------|:----------------|:---------------------------|
| 47192:0   | 47192:0:0       | Don't announce to any peer |
| 47192:x   | 47192:0:x       | Don't announce to ASx      |
| 65535:666 | 47192:666:0     | Blackhole (set nexthop to .251/::251) |
