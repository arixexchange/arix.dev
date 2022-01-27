"""
parse.py builds the ixf.json and members.md files
"""

import json
import yaml

with open("peers.yml", "r") as peers_file:
    peers = yaml.safe_load(peers_file)

emails = set()
for peer in peers["peers"]:
    emails.add(peer["email"])
print(",".join(emails))

peers_table = """| Name | ASN | Callsign | Connection | IPs |
| ---- | -------- | --- | ---------- | --- |
"""

ixf_members = []
for peer in peers["peers"]:
    ixf_members.append({
        "asnum": peer["asn"],
        "url": peer["website"],
        "name": peer["name"],
        "connection_list": [
            {
                "ixp_id": 1,
                "state": "active",
                "if_list": [
                    {
                        "if_speed": peer["speed"],
                        "switch_id": peer["switch"]
                    }
                ],
                "vlan_list": [
                    {
                        "vlan_id": 1,
                        "ipv4": {
                            "address": peer["ipv4"],
                            "routeserver": True
                        },
                        "ipv6": {
                            "address": peer["ipv6"],
                            "routeserver": True
                        }
                    }
                ]
            }
        ]
    })
    peers_table += f"| [{peer['name']}]({peer['website']}) | [{peer['asn']}](https://peeringdb.com/asn/{peer['asn']}) | {peer['callsign']} | {peer['pop']} SW{peer['switch']} | {peer['ipv4']} {peer['ipv6']} |\n"

peers_table = f"# Members\n\nThere are {len(ixf_members)} members on the exchange.\n\n"+peers_table
with open("docs/members.md", "w") as members_file:
    members_file.write(peers_table)

# Write IXF JSON file
with open("docs/ixf.json", "w") as ixf_file:
    ixf = {
        "version": "1.0",
        "ixp_list": [
            {
                "shortname": "ARIX",
                "name": "Amateur Radio Internet Exchange",
                "country": "US",
                "url": "arix.dev",
                "peeringdb_id": 3069,
                "support_email": "peering@arix.dev",
                "ixp_id": 1,
                "ixf_id": 913,
                "vlan": [
                    {
                        "id": 1,
                        "name": "ARIX",
                        "ipv4": {
                            "prefix": "44.190.42.0",
                            "mask_length": 24,
                            "looking_glass_urls": []
                        },
                        "ipv6": {
                            "prefix": "2602:801:30ff::",
                            "mask_length": 64,
                            "looking_glass_urls": []
                        }
                    }
                ],
                "switch": [
                    {
                        "id": 1,
                        "name": "sw1.fmt.arix.dev",
                        "colo": "Hurricane Electric Fremont 2",
                        "city": "Fremont",
                        "country": "USA",
                        "pdb_facility_id": 547,
                        "manufacturer": "Arista Networks",
                        "model": "Unknown",
                        "software": "Unknown"
                    }, {
                        "id": 2,
                        "name": "sw2.fmt.arix.dev",
                        "colo": "Hurricane Electric Fremont 2",
                        "city": "Fremont",
                        "country": "USA",
                        "pdb_facility_id": 547,
                        "manufacturer": "Arista Networks",
                        "model": "Unknown",
                        "software": "Unknown"
                    }
                ]
            }
        ],
        "member_list": ixf_members
    }

    ixf_file.write(json.dumps(ixf))
