from ncclient import manager

# Device details
host = "devnetsandboxiosxe.cisco.com"
port = 830
username = "admin"
password = "C1sco12345"

# Corrected NETCONF Filter
filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>
'''

try:
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False
    ) as m:
        response = m.get(filter)
        print("✅ Retrieved Interface Details:")
        print(response.xml)

        # Save output
        with open("interfaces.xml", "w") as f:
            f.write(response.xml)

except Exception as e:
    print(f"❌ Error: {e}")
