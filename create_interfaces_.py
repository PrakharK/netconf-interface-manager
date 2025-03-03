from ncclient import manager

#Device Details (Cisco DevNet Sandbox)
host = "devnetsandboxiosxe.cisco.com"
port = 830
username = input( " Please mention the username as per Sandbox")
password = input( " Please Enter the Password !  ")

# Define the Loop back Interface Configuration 
loopback_interface = "Looopback100"
loopback_ip = "10.100.100.1"
loopback_mask = "255.255.255.0"
loopback_description = " Created via NETCONF"


# XML Configuration Template
loopback_config = loopback_config = f"""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback100</name>
            <description>Created via NETCONF</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                ianaift:softwareLoopback
            </type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>10.100.100.1</ip>
                    <netmask>255.255.255.0</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""


try:
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False
    ) as m:
        # Send NETCONF Edit-Config RPC to create the Loopback interface
        response = m.edit_config(target="running", config=loopback_config)
        print("✅ Loopback Interface Created Successfully!")
        print(response)

except Exception as e:
    print(f"❌ Error: {e}")


