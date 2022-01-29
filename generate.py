import json

import yaml
from jinja2 import Template

with open("template.html") as template_file:
    template = Template(template_file.read())

with open("peers.yml", "r") as peers_file:
    peers = yaml.safe_load(peers_file)

# Generate emails
emails = set()
for peer in peers["peers"]:
    emails.add(peer["email"])

with open("web/index.html", "w") as index_file:
    index_file.write(template.render(peers=peers["peers"]))

with open("web/ixf.json", "w") as ixf_file:
    ixf_peers = []
    for peer in peers["peers"]:
        ixf_peers.append({
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

        ixf_file.write(json.dumps({
        "version": "1.0",
        "ixp_list": [
            {
                "shortname": "ARIX",
                "name": "Amateur Radio Internet Exchange",
                "country": "US",
                "url": "arix.dev",
                "peeringdb_id": 3069,
                "support_email": "noc@arix.dev",
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
                        "manufacturer": "Cisco",
                        "model": "Unknown",
                        "software": "Unknown"
                    }
                ]
            }
        ],
        "member_list": ixf_peers
    }))
