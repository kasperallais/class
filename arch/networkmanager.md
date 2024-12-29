Usage
- Network Manager comes with nmcli and nmtui
List Nearby Wi-Fi Networks
- 'nmcli device wifi list'
Connect to a Wi-Fi Network
- 'nmcli device wifi connect SSID_or_BSSI password password'
Connect to a Wi-Fi on the wlan0 interface
- 'nmcli device wifi connect SSID_or_BSSI password password ifname wlan1 profile_name'
Disconnect an interface
- 'nmcli device disconnect ifname eth0'
