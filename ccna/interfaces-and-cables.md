Ethernet
- Ethernet is a collection of network protocols/standards
- For the purpose of this lesson, we will focus on types of cabling as defined by Ethernet standards
- In future lessons, we will learn other aspects of Ethernet
Bits and Bytes
- 0 or a 1
- 8 bits = 1 byte
- Speed is measured in bits per second, not bytes per second
- Data on a hard drive is measured in bytes
Ethernet Standards
- Defined in the IEEE 802.3 standard in 1983
- IEEE = Institute of Electrical and Electronics Engineers
UTP Cables
- Unshielded Twisted Pair
- Twisted helps protect against EMI (Electromagnetic Interference)
PC to Switch Connection
- Transmit (TX) are pins 1 and 2 on the PC
- Receive (RX) are pins 1 and 2 on the Switch
- Transmit (TX) are pins 3 and 6 on the Switch
- Receive (RX) are pins 3 and 6 on the PC
- Allows Full-Duplex transmission
Router to Switch Connection
- Switch
    - Pins 1 and 2 Receive
    - Pins 3 and 6 Transmit
- Router
    - Same as PC
- Straight-through cable works with this
Same device connection
- RX and TX pins end up being the same which means they can't transmit
- Answer to the problem is a different type of cable (Crossover cable)
- Pairs are reversed on each end
    - 3 Connects to 1
    - 6 Connects to 2
    - 1 Connects to 3
    - 2 Connects to 6 
- TX and RX pins per device
    - Router, Firewall, PC
        - TX (1,2) and RX (3,6)
        - TX (3,6) and RX (1,2) 
- Most modern devices don't have to worry about cross-over cables
    - Auto MDI-X
Fiber-Optic Connections
- Copper UTP cables can be used for up to 100 meters
- Connect an SFP transmitter (Small Form-Factor Pluggable)
Structure of a Fiber-Optic Connection
- Fiberglass Core
- Cladding that reflects light
- Protective buffer
- Outer jacket of the cable
- Two types of fiber
    - Single mode and multi mode
Types of fiber optic
- Multi mode
    - Core diameter is wider than single-mode fiber
    - Allows multiple angles of light waves to enter the fiberglass core
    - Allows longer cables than UTP, but shorter cables than single-mode fiber
    - Cheaper than single-mode fiber (often cheaper LED-based SFP transmitter)
- Single mode
    - Core diameter is narrower than multi-mode fiber
    - Light enters at a single angle from a laser-based transmitter
    - Allows longer cables than both UTP and multi-mode fiber
    - More expensive than multi-mode fiber (due to more expensive laser based SFP transmitters)
UTP vs Fiber-Optic Cabling
- UTP
    - Lower cost than fiber-optic
    - Shorter maximum distance than fiber-optic
    - Can be vulnerable to EMI
    - RJ45 ports used with UTP are cheaper than SFP ports
    - Emit a faint signal outside of the cable, which can be copied
- Fiber-Optic
    - Higher cost than UTP 
    - Longer maximum distance than UTP
    - No vulnerability to EMI
    - SFP ports are more expensive than RJ45 ports
    - Does not emit any signal outside of the cable
