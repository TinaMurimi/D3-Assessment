# WEB SERVICE SECURITY CONCEPTS
## Web Services Protocols
Web Services currently revolves around three important protocols: 

### SOAP (Simple Object Access Protocol)

An XML-based protocol for accessing web services over HTTP. It is platform independent and language independent.
Every programming language can understand the XML markup language. Hence, XML was used as the underlying medium for data exchange. But there are no standard specifications on use of XML across all programming languages for data exchange. That is where SOAP comes in. SOAP was designed to work with XML over HTTP and have some sort of specification which could be used across all applications.

SOAP vs REST
Instead of using XML to make a request, REST relies on a simple URL in many cases. In some situations you must provide additional information in special ways, but most Web services using REST rely exclusively on obtaining the needed information using the URL approach. REST can use four different HTTP 1.1 verbs (GET, POST, PUT, and DELETE) to perform tasks.

Unlike SOAP, REST doesn’t have to use XML to provide the response. You can find REST-based Web services that output the data in Command Separated Value (CSV), JavaScript Object Notation (JSON) and Really Simple Syndication (RSS). The point is that you can obtain the output you need in a form that’s easy to parse within the language you need for your application.

### WSDL (Web Services Description Language)
WSDL is an XML format for describing network services as a set of endpoints operating on messages containing either document-oriented or procedure-oriented information. A WSDL document defines services as collections of network endpoints, or ports.

In WSDL, the abstract definition of endpoints and messages is separated from their concrete network deployment or data format bindings. This allows the reuse of abstract definitions: messages, which are abstract descriptions of the data being exchanged, and port types which are abstract collections of operations. The concrete protocol and data format specifications for a particular port type constitutes a reusable binding. A port is defined by associating a network address with a reusable binding, and a collection of ports define a service.

### UDDI (Universal Description, Discovery, and Integration)

An XML-based standard for describing, publishing, and finding web services.


## Web Service Security

(i) Authentication: Verifying that the user is who she claims to be. A user's identity is verified based on the credentials presented by that user.
HTTP basic authentication uses a user name and password to authenticate a service client to a secure endpoint. A simple way to provide authentication data for the service client is to authenticate to the protected service endpoint to the HTTP basic authentication. The basic authentication is located in the HTTP header that carries the SOAP request. When the application server receives the HTTP request, the user name and password are retrieved and verified using the authentication mechanism specific to the server. Although the basic authentication data is base64-encoded, sending data over HTTPS is recommended. The integrity and confidentiality of the data can be protected by the Secure Sockets Layer (SSL) protocol. 

(ii) Authorization (or Access Control)— Granting access to specific resources based on an authenticated user's permissions. Authorization enables you to determine what operations authenticated clients can access.There are three basic approaches to authorization:

- **Role-based—Role:** based security is based on the notion that a set of identities, known as principals, can be grouped into roles, and then a policy can be applied to each of the roles.
- **Identity based:** Identity Model enables you to manage claims and policies in order to authorize clients. With this approach, you can verify claims contained within the authenticated users' credentials. These claims can be compared with the set of authorization policies for the WCF service. Depending on the claims provided by the client, the service can either grant or deny access to the operation or resources. Identity Model is useful for fine-grained authorization and is most beneficial when using issue token authentication.
- **Resource based:** Individual resources are secured by using Windows access control lists (ACLs).

(iii) Confidentiality, privacy— Keeping information secret. Accesses a message, for example a Web service request or an email, as well as the identity of the sending and receiving parties in a confidential manner. Confidentiality and privacy can be achieved by encrypting the content of a message and obfuscating the sending and receiving parties' identities.

(iv) Integrity, non repudiation— Making sure that a message remains unaltered during transit by having the sender digitally sign the message. A digital signature is used to validate the signature and provides non-repudiation. The timestamp in the signature prevents anyone from replaying this message after the expiration.

### Web Securuty Methods
There are two ways with which we can ensure security with Web Services:

#### Transport level security
Transport level security, such as HTTP Basic/Digest and SSL(Secure Sockets Layer), is the usual "first line of defence", as securing the transport mechanism itself makes Web services inherently secure.  The trade-off is transport dependency (Web services are more tightly coupled to the network transport layer). It secures the actual transport (i.e. the pipe) over which the message passes through from client to a service. For example it uses SSL (Secure Socket Layer) to ensure point-to-point protection. If a message needs to go through multiple points to reach its destination, each intermediate point must forward the message over a new SSL connection.

Transport level security is based on Secure Sockets Layer (SSL) or Transport Layer Security (TLS) that runs beneath HTTP. SSL and TLS provide security features including authentication, data protection, and cryptographic token support for secure HTTP connections. To run with HTTPS, the service endpoint address must be in the form https://. The integrity and confidentiality of transport data, including SOAP messages and HTTP basic authentication, is confirmed when you use SSL and TLS.

Implementing security at the transport level means, securing the network protocol a Web Service uses for communication. SSL provides endpoint authentication and communication privacy over the internet using cryptography. In this model, a Web Service client will use SSL to open a secure socket to a Web Service. The client then sends and receives SOAP messages over this secured socket using HTTPS. The SSL implementation takes care of ensuring privacy by encrypting all the network traffic on the socket. SSL can also authenticate the Web Service to the client using a digital certificate issued by a Certificate authority. SSL can be used in three modes:
    
    (i) No authentication: Neither the client nor the server authenticates itself to the other. No certificates are sent or exchanged. In this case, only confidentiality (encryption/decryption) is used.
    
    (ii) One-way authentication (or server authentication): Only the server authenticates itself to the client. The server sends the client a certificate verifying that the server is authentic. This is typically the approach used for Internet transactions such as online banking.
    
    (iii) Two-way authentication (or bilateral authentication): Both client and server authenticate themselves to each other by sending certificates to each other. This approach is necessary to prevent attacks from occurring between a proxy and a Web service endpoint.

SSL uses a combination of secret-key and public-key cryptography to secure communications. SSL traffic uses secret keys for encryption and decryption, and the exchange of public keys is used for mutual authentication of the parties involved in the communication.

HTTPS provides encryption, which ensures privacy and message integrity. HTTPS also authenticates through the use of certificates, which can be used on the server side, the client side, or both. HTTPS with server-side certificates is the most common configuration on the Web today. In this configuration, clients can authenticate servers, but servers cannot authenticate clients. However, HTTPS can also be used in conjunction with basic or digest authentication, which provides a weaker form of authentication for clients.

Advantages:
    
    (i) As Transport Level Security secures the network protocol, so no extra coding required.
    (ii) As client and service doesn’t need to understand WS-Security specification results support for interoperability.
    (iii) Improved performance can be achieved by using hardware accelerators.
Disadvantages:

    (i) Lacks support for intermediate systems because it’s point to point and protects the “pipe” between a single client and a service.
    (ii) Security options are comparatively less due to protocol security limitations.


#### Message level security
Message level security, such as WS-Security, SAML, XML Digital Signatures, and XML Encrypttion,  can be more effective and has the added flexibility that the message can be sent over any transport.
Message level security is an application layer service and facilitates the protection of message data between applications. Message protection encompasses two concepts, message confidentiality and message integrity.
SOAP based communications introduces the notion of Message Level Security. In  message level security, security information is contained within the SOAP message, which allows security information to travel along with the message. For example, a portion of the message may be signed by a sender and encrypted for a particular receiver. When the message is sent from the initial sender, it may pass through intermediate nodes before reaching its intended receiver. In this scenario, the encrypted portions continue to be opaque to any intermediate nodes and can only be decrypted by the intended receiver. For this reason, message-level security is also sometimes referred to as end-to-end security.

Advantages:

    (i) As the message is secured (signed and encrypted) while transmitting through the network, any intermediate hop in the network has no impact on security.
    (ii) Being transport-independent, it can support multiple transport options.
    (iii) Supports wide range of security options, even we can implement custom security. Secured message can be sent over many different protocols such as SMTP, FTP, and TCP without having to rely on the protocol for security.
    (iv) It is more flexible because parts of the message can be signed or encrypted rather than the entire message. This means that intermediaries are able to view parts of the message intended for them. An example of this is a Web service that routes SOAP message being able to inspect unencrypted parts of the message to determine where to send the message, while other parts of the message remain encrypted.
    (v) intermediaries can add their own headers to the message and sign them for the purpose of audit logging

Disadvantages:

    (i) Every individual Message is secured means there is a cost to encrypt a message at one side and decrypt on the other resulting in reduced performance.
    (ii) Lacks Interoperability. It demands both client and service should support WS-Security specification, so no support for applications developed in older technologies like ASMX.

#### Factor to Consider
1. Your application interacts directly with the Web service.
Transport Layer: Transport layer HTTPS provides full message protection.
Message Layer: Message layer message protection usually requires more work and overhead than transport layer.
2. Web services are hosted on a system that does not support integrated authentication.
Transport Layer: Basic over HTTPS could be implemented, however, it would require manipulation of message headers.
Message Layer: Authentication can be performed by passing credentials in the message.
3. Your company has a firewall in place between applications and Web services.
Transport Layer: Ports could be opened to support HTTPS.
Message Layer: Message layer security is not affected by standard firewalls.
4. You have non-repudiation requirements
Transport Layer: Does not support digital signatures.
Message Layer: Supports Digital signatures, which represents the standard approach for implementing non-repudiation.
5. A Web service request can pass through message queues or routing servers.
Transport Layer: The message data is not protected as it passes through the server, which leaves it vulnerable to attack.
Message Layer: Message data will be protected as it passes through intermediate servers.
6. The Web service you are designing will handle a high concurrent load.
Transport Layer: Hardware appliances can be used to improve performance with Transport Layer message protection such as SSL.
Message Layer: Security tokens can be used to establish a session, however, message protection has a high computational load.


### OWASP Application Security Verification Standard (ASVS)
OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development.

The primary aim of the OWASP Application Security Verification Standard (ASVS) Project is to normalize the range in the coverage and level of rigor available in the market when it comes to performing Web application security verification using a commercially-workable open standard. The standard provides a basis for testing application technical security controls, as well as any technical security controls in the environment, that are relied on to protect against vulnerabilities such as Cross-Site Scripting (XSS) and SQL injection. This standard can be used to establish a level of confidence in the security of Web applications. The requirements were developed with the following objectives in mind:
    
1. Use as a metric - Provide application developers and application owners with a yardstick with which to assess the degree of trust that can be placed in their Web applications,
2. Use as guidance - Provide guidance to security control developers as to what to build into security controls in order to satisfy application security requirements, and
3. Use during procurement - Provide a basis for specifying application security verification requirements in contracts.
The Application Security Verification Standard defines three security verification levels, with each level increasing
in depth.

- ASVS Level 1 is meant for all software.
- ASVS Level 2 is for applications that contain sensitive data, which requires protection.
- ASVS Level 3 is for the most critical applications - applications that perform high value transactions, contain sensitive medical data, or any application that requires the highest level of trust.

#### OWASP Top 10 Web Application Security Risks
1. Injection
Injection flaws, such as SQL injection, LDAP injection, and CRLF injection, occur when an attacker sends untrusted data to an interpreter that is executed as a command without proper authorization.

* Application security testing can easily detect injection flaws. Developers should use parameterized queries when coding to prevent injection flaws.
Injection attacks can be prevented by validating and/or sanitizing user-submitted data. (Validation means rejecting suspicious-looking data, while sanitization refers to cleaning up the suspicious-looking parts of the data.) In addition, a database admin can set controls to minimize the amount of information an injection attack can expose.

2. Broken Authentication and Session Management
Vulnerabilities in authentication (login) systems can give attackers access to user accounts and even the ability to compromise an entire system using an admin account. For example, an attacker can take a list containing thousands of known username/password combinations obtained during a data breach and use a script to try all those combinations on a login system to see if there are any that work.

Some strategies to mitigate authentication vulnerabilities are requiring 2-factor authentication (2FA) as well as limiting or delaying repeated login attempts using rate limiting.

3. Sensitive Data Exposure
If web applications don’t protect sensitive data such as financial information and passwords, attackers can gain access to that data and sellor utilize it for nefarious purposes. One popular method for stealing sensitive information is using a man-in-the-middle attack.

Data exposure risk can be minimized by encrypting all sensitive data as well as disabling the caching* of any sensitive information. Additionally, web application developers should take care to ensure that they are not unnecessarily storing any sensitive data.

*Caching is the practice of temporarily storing data for re-use. For example, web browsers will often cache webpages so that if a user revisits those pages within a fixed time span, the browser does not have to fetch the pages from the web.

4. XML External Entities (XEE)
This is an attack against a web application that parses XML* input. This input can reference an external entity, attempting to exploit a vulnerability in the parser. An ‘external entity’ in this context refers to a storage unit, such as a hard drive. An XML parser can be duped into sending data to an unauthorized external entity, which can pass sensitive data directly to an attacker.

The best ways to prevent XEE attacks are to have web applications accept a less complex type of data, such as JSON**, or at the very least to patch XML parsers and disable the use of external entities in an XML application.

*XML or Extensible Markup Language is a markup language intended to be both human-readable and machine-readable. Due to its complexity and security vulnerabilities, it is now being phased out of use in many web applications.

**JavaScript Object Notation (JSON) is a type of simple, human-readable notation often used to transmit data over the internet. Although it was originally created for JavaScript, JSON is language-agnostic and can be interpreted by many different programming languages.

5. Broken Access Control
Improperly configured or missing restrictions on authenticated users allow them to access unauthorized functionality or data, such as accessing other users’ accounts, viewing sensitive documents, and modifying data and access rights.

* Penetration testing is essential for detecting non-functional access controls; other testing methods only detect where access controls are missing.
Access controls can be secured by ensuring that a web application uses authorization tokens* and sets tight controls on them.

*Many services issue authorization tokens when users log in. Every privileged request that a user makes will require that the authorization token be present. This is a secure way to ensure that the user is who they say they are, without having to constantly enter their login credentials.

6. Security Misconfiguration
Security misconfiguration is the most common vulnerability on the list, and is often the result of using default configurations or displaying excessively verbose errors. For instance, an application could show a user overly-descriptive errors which may reveal vulnerabilities in the application. This can be mitigated by removing any unused features in the code and ensuring that error messages are more general.

* Dynamic application security testing (DAST) can detect misconfigurations, such as leaky APIs.

7. Cross-Site Scripting
Cross-site scripting vulnerabilities occur when web applications allow users to add custom code into a url path or onto a website that will be seen by other users. This vulnerability can be exploited to run malicious JavaScript code on a victim’s browser. For example, an attacker could send an email to a victim that appears to be from a trusted bank, with a link to that bank’s website. This link could have some malicious JavaScript code tagged onto the end of the url. If the bank’s site is not properly protected against cross-site scripting, then that malicious code will be run in the victim’s web browser when they click on the link.

Mitigation strategies for cross-site scripting include escaping untrusted HTTP requests as well as validating and/or sanitizing user-generated content. Using modern web development frameworks like ReactJS and Ruby on Rails also provides some built-in cross-site scripting protection.

* Developer training complements security testing to help programmers prevent cross-site scripting with best coding best practices, such as encoding data and input validation.

8. Insecure deserialization
Insecure deserialization flaws can enable an attacker to execute code in the application remotely, tamper or delete serialized (written to disk) objects, conduct injection attacks, and elevate privileges. This threat targets the many web applications which frequently serialize and deserialize data. Serialization means taking objects from the application code and converting them into a format that can be used for another purpose, such as storing the data to disk or streaming it. Deserialization is just the opposite: converting serialized data back into objects the application can use

* Application security tools can detect deserialization flaws but penetration testing is frequently needed to validate the problem.
An insecure deserialization exploit is the result of deserializing data from untrusted sources, and can result in serious consequences like DDoS attacks and remote code execution attacks. While steps can be taken to try and catch attackers, such as monitoring deserialization and implementing type checks, the only sure way to protect against insecure deserialization attacks is to prohibit the deserialization of data from untrusted sources.

9. Using Components With Known Vulnerabilities
Many modern web developers use components such as libraries and frameworks in their web applications. These components are pieces of software that help developers avoid redundant work and provide needed functionality; common example include front-end frameworks like React and smaller libraries that used to add share icons or a/b testing. Some attackers look for vulnerabilities in these components which they can then use to orchestrate attacks. Some of the more popular components are used on hundreds of thousands of websites; an attacker finding a security hole in one of these components could leave hundreds of thousands of sites vulnerable to exploit.

Component developers often offer security patches and updates to plug up known vulnerabilities, but web application developers don’t always have the patched or most-recent versions of components running on their applications. To minimize the risk of running components with known vulnerabilities, developers should remove unused components from their projects, as well as ensuring that they are receiving components from a trusted source and ensuring they are up to date.

* Software composition analysis conducted at the same time as static analysis can identify insecure versions of components.

10. Insufficient Logging and Monitoring
The time to detect a breach is frequently measured in weeks or months. Insufficient logging and ineffective integration with security incident response systems allow attackers to pivot to other systems and maintain persistent threats.
Many web applications are not taking enough steps to detect data breaches. The average discovery time for a breach is around 200 days after it has happened. This gives attackers a lot of time to cause damage before there is any response. OWASP recommends that web developers should implement logging and monitoring as well as incident response plans to ensure that they are made aware of attacks on their applications

* Think like an attacker and use pen testing to find out if you have sufficient monitoring; examine your logs after pen testing.



