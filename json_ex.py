import json
with open('data.json', 'r') as f:
    data = json.load(f)
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "------", "------")

# Loop through only the first 3 interfaces
for item in data["imdata"][:3]:   # <- only first three items
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))