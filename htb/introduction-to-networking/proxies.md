Proxies
- A proxy is when a device or service sits in the middle of a connection and acts as a mediator
- The mediator is the critical piece of information because it means the device in the middle must be able to inspect the contents of the traffic
- Without the ability to be a mediator, the device is technically a gateway, not a proxy
Dedicated Proxy / Forward Proxy
- A Forward Proxy is when a client makes a request to a computer, and that computer carries out the request
Reverse Proxy
- A reverse proxy, is the reverse of a forward proxy
- Instead of being designed to filter outgoing requests, it filters incoming ones
- The most common goal of a reverse proxy is to listen on an address and forward it to a closed-off network
(Non-) Transparent Proxy
- All these proxy services act either transparently or non-transparently
- With a transparent proxy, the client doesn't know about its existence
- The transparent proxy intercepts the client's communication requests to the Internet and acts as a substitute instance
- If it is a non-transparent proxy, we must be informed about its existence
- For this purpose, we and the software we want to use are given a special proxy configuration that ensure that traffic to the Internet is first addressed to the proxy

