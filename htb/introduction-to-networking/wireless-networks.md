Wireless Networks
- Wireless networks are computer networks that use wireless data connection between network nodes
- These networks allow devices such as laptops, smartphones, and tablets to communicate with each other and the Internet without needing physical connections such as cables
- Wireless networks use radio frequency (RF) technology to transmit data between devices
- Each device on a wireless network has a wireless adapter that converts data into RF signals and sends them over the air
- Other devices on the network receive these signals with their own wireless adapters, and the data is then converted back into a usable form
- Those can operate over various ranges, depending on the technology used
- A wireless wide area network (WWAN) might use mobile telecommunication technology such as cellular data, which can cover a much larger area, such as an entire city or region
- To connect to a wireless network, a device must be within range of the network and configured with the correct network settings, such as the network name and password
- Once connected, devices can communicate with each other and the Internet allowing users to access online resources and exchange data
- Communication between devices occurs over RF in the 2.4 GHz and 5 GHz bands in a Wi-Fi network
- When a device, like a laptop, wants to send data over the network, it first communicates with the Wireless Access Point (WAP) to request permission to transmit
- The WAP is a central device, like a router, that connects the wireless network to a wired network and controls access to the network
- Once the WAP grants permission, the transmitting device sends the data as RF signals, which are received by the wireless adapters of other devices on the network
- The data is then converted back into a usable form and passed on to the appropriate application or system
- The strength of the RF signal and the distance it can travel are influenced by factors such as the transmitter's power, the presence of obstacles, and the density of RF noise in the environment
Wi-Fi Connection
- The device must also be configured with the correct network settings, such as the network name / Service Set Identifier (SSID) and password
- So, to connect to the router, the laptop uses a wireless networking protocol called IEEE 802.11
- This protocol defines the technical details of how wireless devices communicate with each other and with WAPs
- When a device wants to join a Wi-Fi network, it sends a request to the WAP to initiate a connection process
- This request is known as a connection request frame or association request and is sent using the IEEE 802.11 wireless networking protocol
- The device then uses this information to configure its wireless adapter and connect to the WAP
- Once the connection is establishes, the device can communicate with the WAP and other network devices
- It can also access the Internet and other online resources through the WAP, which acts as a gateway to the wired network
- However, the SSID can be hidden by disabling broadcasting
- That means that devices that search for that specific WAP will not be able to identify its SSID
- In addition to the IEEE 802.11 protocol, other networking protocols and technologies may also be used, like TCP/IP, DHCP, and WPA2, in a Wi-Fi network to perform tasks such as assigning IP addresses to devices, routing traffic between devices, and providing security
WEP Challenge-Response Handshake
- The challenge-response handshake is a process to establish a secure connection between a WAP and a client in a wireless network that uses the WEP security protocol
- This involves exchanging packets between the WAP and the client device to authenticate the device and establish a secure connection
- Nevertheless, some packets can get lost, so the so-called CRC checksum has been integrated
- Cyclic Redundancy Check (CRC) is a error-detection mechanism used in the WEP protocol to protect against data corruption in wireless communications
- A CRC value is calculated for each packet transmitted over the wireless network based on the packet's data
- When the destination device receives the packet, the CRC value is recalculated and compared to the original value
- If the values match, the data has been transmitted successfully without any errors
Security Features
- Wi-Fi networks have several security features to protect against unauthorized access and ensure the privacy and integrity of data transmitted over the network
Encryption
- We can use various encryption algorithms to protect the confidentiality of data transmitted over wireless networks
- The most common encryption algorithms in Wi-Fi are Wired Equivalent Privacy (WEP), Wi-Fi Protected Access 2 (WPA2) and Wi-Fi Protected Access 3 (WPA3)
Access Control
- Wi-Fi networks are configured by default to allow unauthorized devices to join the network using specific authentication methods
- However, these methods can be changed by requiring a password or a unique identifier to identify authorized devices
Firewall
- A firewall is a security system that controls incoming and outgoing network traffic based on predetermined security rules
Encryption Protocols
- WEP and WPA are encryption protocols that secure data over a Wi-Fi network
- WPA can use different encryption algorithms, including Advanced Encryption Standard (AES)
WEP
- WEP uses a 40-bit or 104-bit key to encrypt data, while WPA using AES uses a 128-bit key
- Longer keys provide more robust encryption and are more resistant to attacks
- However, it is vulnerable to various attacks that can allow an attacker to decrypt data transmitted over the network
- In addition, WEP is not compatible with newer devices and operating systems and is generally no longer considered secure
- WEP uses the RC4 cipher encryption algorithm, which makes it vulnerable to attacks
- However, WEP uses a shared key for authentication, which means the same key is used for encryption and authentication
- WEP-40, also known as WEP-64, uses a 40-bit key, while WEP-104 uses a 104-bit key
- The key is divided into an Initialization Vector (IV) and a secret key
- The IV is a small value included in the packet header along with encrypted data and is used to create the key for both WEP-40 and WEP-104 and is included to ensure that each key is unique
- The secret key is a series of random bits used to encrypt the data
- The WEP-104 has a 80-bit long secret key
- Since the IV in WEP is relatively small, we can brute force it, and determine the correct value
- Afterward, we can use it to decrypt the data in the packet
WPA
- WPA provides the highest level of security and is not susceptible to the same types of attacks as WEP
- In addition, WPA uses more secure authentication methods, such as Pre-Shared Key (PSK) or an 802.1X authentication server, which provides stronger protection against unauthorized access
- Although older devices may not support WPA, WPA is compatible with most devices and operating systems
- All wireless networks, especially in critical infrastructure like offices, should generally implement at least WPA2 or even WPA3 encryption
Authentication Protocols
- Lightweight Extensible Authentication Protocol (LEAP) and Protected Extensible Authentication Protocol (PEAP) are authentication protocols used to secure wireless networks to provide a secure method for authenticating devices on wireless networks and often used in conjunction with WEP or WPA to provide an additional layer of security
- LEAP and PEAP are both based on the Extensible Authentication Protocol (EAP), a framework for authentication used in various networking contexts
- LEAP uses a shared key for authentication, which means that the same key is used for encryption 
- PEAP uses a more secure authentication method called tunneled Transport Layer Security (TLS)
- This method establishes a secure connection between the device and the WAP using a digital certificate, and an unencrypted tunnel protects the authentication process
- This provides more robust protection against unauthorized access and is more resistant to attacks
TACACS+
- In a wireless network, when a wireless access point (WAP) sends an authentication request to a Terminal Access Controller Access-Control System Plus (TACACS+) server, it is likely that the ensure request packet will be encrypted will be protected to protect the confidentiality and integrity of the request
- TACACS+ is a protocol used to authenticate and authorize users accessing network devices, such as routers and switches
- When a WAP sends an authentication request to a TACACS+ server, the request typically includes the user's credentials and other information about the session
- Encrypting the authentication request helps to ensure that this sensitive information is not visible to unauthorized parties who may be able to intercept the request
- It also helps prevent tampering with the request ore replacing it with a malicious request of their own
- Several encryption methods may be used to encrypt the authentication request, such as SSL/TLS or IPSec
- The specific encryption method used may depend on the configuration of the TACACS+server and the capabilities of the WAP
Disassociation Attack
- A Disassociation Attack is a type of all wireless network attack that aims to disrupt the communication between a WAP and its clients by sending disassociation frames to one or more clients
- The WAP uses disassociation frames to disconnect a client from the network
- When a WAP sends a disassociation frame to a client, the client will disconnect from the network and have to reconnect to continue using the network
- We can launch the attack from within or outside the network depending on our location and network security measures
- The purpose of this attack is to disrupt the communication between the WAP and its clients, causing the clients to disconnect and possibly causing inconvenience or disruption to the users
- We can also use it as a precursor to other attacks, such as a MITM attack, by forcing the clients to reconnect to the network and potentially exposing them to further attacks
Wireless Hardening
- There are many different ways to protect wireless networks
    - Disabling broadcasting
    - WiFi Protected Access
    - MAC Filtering
    - Deploying EAP-TLS
Disabling Broadcasting
- Disabling the broadcasting of the SSID is a security measure that can help harden a WAP by making it more difficult to discover and connect to the network
- When the SSID is broadcasted, it is include din beacon frames regularly transmitted by the WAP to advertise the availability of the network
- By disabling the broadcasting of the SSID, the WAP will not transmit beacon frames, and the network will not be visible to devices that are not already connected to the network
WPA
- WPA provides strong encryption and authentication for wireless communications, helping protect against unauthorized network access and sensitive data interception
- WPA includes two main versions:
    - WPA-Personal
    - WPA-Enterprise
- WPA-Personal, designed for home and small business networks, and WPA-Enterprise designed for larger organisations and uses a centralized authentication server to verify the identity of clients
MAC Filtering
- MAC filtering is a security measure that allows WAP to accept or reject connections from specific devices based on their MAC addresses
- By configuring the WAP to accept connections only from devices with approved MAC addresses, it is possible to prevent unauthorized devices from connecting to the network
Deploying EAP-TLS
- EAP-TLS is a security protocol used to authenticate and encrypt wireless communications
- It uses digital certificates and PKI to verify the identity of clients and establish secure connections
- Deploying EAP-TLS can help to harden a WAP by providing strong authentication and encryption for wireless communications, which can protect against unauthorized access to the network and the interception of sensitive data
