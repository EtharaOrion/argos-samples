
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Get:1 http://deb.debian.org/debian trixie InRelease [140 kB]
Get:2 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]
Get:3 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]
Get:4 http://deb.debian.org/debian trixie/main arm64 Packages [9607 kB]
Get:5 http://deb.debian.org/debian trixie-updates/main arm64 Packages [4424 B]
Get:6 http://deb.debian.org/debian-security trixie-security/main arm64 Packages [252 kB]
Fetched 10.1 MB in 1s (12.7 MB/s)
Reading package lists...
Building dependency tree...
Reading state information...
18 packages can be upgraded. Run 'apt list --upgradable' to see them.

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
patch is already the newest version (2.8-2).
patch set to manually installed.
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 18
━ UTScapy - Scapy adaa923d - 3.9.25
 └ Loaded config file ./test/configs/linux.utsc
 └ Non-root mode
 └ Booting scapy...
 └ Discovering tests files...
[32m━ Loading: test/tls/tests_tls_netaccess.uts[0m
Campaign CRC=80D1C372 in 000.00s SHA=00398E12905B8F85E932821C74EA75C220F661BC
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/answering_machines.uts[0m
[34m[1mpassed[0m A920212C 000.03s Generic answering machine mocker
[34m[1mpassed[0m E96DD2B7 000.00s BOOT_am
[34m[1mpassed[0m 7AE7679E 000.01s DHCP_am
[34m[1mpassed[0m E85516A9 000.00s ARP_am
[34m[1mpassed[0m 680FF64F 000.00s DNS_am
[34m[1mpassed[0m 1E25B757 000.00s WiFi_am
Campaign CRC=FC25EE9B in 000.06s SHA=3E6E8F4B1D12DA7BB018A4FA1CB0F8628BD2A098
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/cert.uts[0m
[34m[1mpassed[0m 7467C9D5 000.00s PKCS os2ip basic tests
[34m[1mpassed[0m 7CDE63E1 000.00s PKCS i2osp basic tests
[31m[1mfailed[0m B28AF781 000.00s PubKey class : Importing PEM-encoded RSA public key
[31m[1mfailed[0m DEB7954B 000.00s PubKey class : Verifying PEM key format
[31m[1mfailed[0m 1C9EB2F5 000.00s PubKey class : Importing DER-encoded RSA Key
[31m[1mfailed[0m 756D80F5 000.00s PubKey class : Verifying DER key format
[31m[1mfailed[0m D99A77ED 000.00s PubKey class : Checking modulus value
[31m[1mfailed[0m B1A9D1E6 000.00s PubKey class : Checking public exponent value
[34m[1mpassed[0m 74A3AA7E 000.00s PubKey class : Importing PEM-encoded ECDSA public key
[31m[1mfailed[0m 712AE41F 000.00s PubKey class : Checking curve
[31m[1mfailed[0m AC355F33 000.00s PubKey class : Checking point value
[31m[1mfailed[0m 4E636BE1 000.00s PubKeyRSA class : Generate without modulus
[31m[1mfailed[0m 8C0EE682 000.00s PrivKey class : Importing PEM-encoded RSA private key
[31m[1mfailed[0m BBABEEBD 000.00s PrivKey class : Checking public attributes
[31m[1mfailed[0m C522A6B2 000.00s PrivKey class : Checking private attributes
[34m[1mpassed[0m 59BEC5F0 000.00s PrivKey class : Importing PEM-encoded ECDSA private key
[31m[1mfailed[0m 4105D581 000.00s PrivKey class : Importing DER-encoded RSA private key
[31m[1mfailed[0m 3816E9A8 000.00s PrivKey class : Checking public attributes
[31m[1mfailed[0m AC272088 000.00s PrivKey class : Checking private attributes
[31m[1mfailed[0m A2AE99D4 000.01s PrivKey class : sign tbs cert
[31m[1mfailed[0m 19E68023 000.00s PrivKey/PubKey classes : Signing/Verifying with MD5_SHA1 hash
[31m[1mfailed[0m E280E220 000.00s PrivKey/PubKey classes : Signing/Verifying with MD5_SHA1 hash with legacy support
[31m[1mfailed[0m 3F2C417F 000.01s Cert class : Importing PEM-encoded X.509 Certificate
[31m[1mfailed[0m D5B0F293 000.00s Cert class : Checking version
[31m[1mfailed[0m FC12B8BB 000.00s Cert class : Checking certificate serial number extraction
[31m[1mfailed[0m AFA16673 000.00s Cert class : Checking signature algorithm
[31m[1mfailed[0m 9B8F7229 000.00s Cert class : Checking issuer extraction in basic format (/C=FR ...)
[31m[1mfailed[0m 2ADF05A7 000.00s Cert class : Checking subject extraction in basic format (/C=FR ...)
[31m[1mfailed[0m DE4DF378 000.00s Cert class : Checking start date extraction in simple and tuple formats
[31m[1mfailed[0m B2215E79 000.00s Cert class : Checking end date extraction in simple and tuple formats
[31m[1mfailed[0m 5F4A083B 000.00s Cert class : test remainingDays
[31m[1mfailed[0m 72F683BC 000.00s Cert class : Checking RSA public key
[31m[1mfailed[0m 8850F39D 000.00s Cert class : Checking extensions
[31m[1mfailed[0m 1173B95C 000.00s Cert class : encrypt
[31m[1mfailed[0m 3FD1B423 000.00s Cert class : export
[31m[1mfailed[0m 57C7A0AD 000.00s Cert class : isIssuerCert
[34m[1mpassed[0m DA1699AD 000.01s Cert class : Importing another PEM-encoded X.509 Certificate
[31m[1mfailed[0m BD33B64D 000.00s Cert class : Checking ECDSA public key
[34m[1mpassed[0m A77D322B 000.00s Cert class : Checking ECDSA signature
[34m[1mpassed[0m C7650354 000.00s Cert class : Test show
[34m[1mpassed[0m 3B08B684 000.00s Cert: Check split_pem on chained certs with missing end \n
[34m[1mpassed[0m F710A869 000.00s CRL class : Importing PEM-encoded CRL
[34m[1mpassed[0m 3BBE93BF 000.00s CRL class : Checking version
[34m[1mpassed[0m 9FEEDBE5 000.00s CRL class : Checking issuer extraction in basic format (/C=FR ...)
[34m[1mpassed[0m 9C7206C7 000.00s CRL class : Checking lastUpdate date extraction in tuple format
[34m[1mpassed[0m AFB28660 000.00s CRL class : Checking nextUpdate date extraction in tuple format
[34m[1mpassed[0m 3148A0F7 000.00s CRL class : Checking number of revoked certificates
[34m[1mpassed[0m F5F73161 000.00s CRL class : Checking presence of one revoked certificate
[31m[1mfailed[0m 4BBE171F 000.01s Cert/CRL class : Checking isRevoked
[34m[1mpassed[0m 1F2AFF67 000.00s CRL class : Test show
[31m[1mfailed[0m 29ED0F21 000.01s Cert class : Checking isIssuerCert()
[31m[1mfailed[0m ECE33A81 000.00s Cert class : Checking isSelfSigned()
[31m[1mfailed[0m ADD2C36B 000.00s PubKey class : Checking verifyCert()
[31m[1mfailed[0m DB119917 000.00s Chain class : Checking chain construction
[31m[1mfailed[0m 676CE307 000.00s Chain class : repr
[31m[1mfailed[0m 4AA5853F 000.00s Chain class : Checking chain verification
[31m[1mfailed[0m A4A6ED7D 000.00s Chain class: Checking chain verification with file
[34m[1mpassed[0m B95F31AC 000.00s Clear files
[31m[1mfailed[0m 4D9EB4B7 000.00s Test __repr__
[31m[1mfailed[0m 249C4366 000.00s Test GeneralizedTime
Campaign CRC=2A29939B in 000.08s SHA=18C66F0E0C26385336A965ED731164C24A3B1222
[31m[1mPASSED=17 FAILED=43[0m
[32m━ Loading: test/fields.uts[0m
[34m[1mpassed[0m 49EC0DD3 000.01s ConditionnalField class
[34m[1mpassed[0m C10B7C25 000.00s Simple tests
[34m[1mpassed[0m A1FC55E3 000.00s MACField class
[34m[1mpassed[0m 1AE4144B 000.00s SourceMACField
[34m[1mpassed[0m A8B908D5 000.00s IPField class
[34m[1mpassed[0m 5A43B1E5 000.00s SourceIPField
[34m[1mpassed[0m 9F9545D2 000.00s ThreeBytesField
[34m[1mpassed[0m 59075674 000.00s NBytesField
[34m[1mpassed[0m 37550C07 000.00s StrField
[34m[1mpassed[0m F8D6E66A 000.00s StrFieldUtf16
[34m[1mpassed[0m DE45793B 000.00s StrFieldUtf16
[34m[1mpassed[0m FC687874 000.00s Creation of a layer with ActionField
[34m[1mpassed[0m C18AA531 000.00s Triggering action
[34m[1mpassed[0m 648CCA2E 000.00s Creation of a layer with FieldLenField
[34m[1mpassed[0m FD69822A 000.00s Assembly of an empty packet
[34m[1mpassed[0m 418F18DF 000.00s Assembly of non empty packet
[34m[1mpassed[0m D70A4723 000.00s Disassembly
[34m[1mpassed[0m AB742CDB 000.00s BitFieldLenField test
[34m[1mpassed[0m DDF60244 000.00s Creation of a layer
[34m[1mpassed[0m BBDF976B 000.00s Assembly of an empty packet
[34m[1mpassed[0m 10BFFBF0 000.00s Assembly of a non-empty packet
[34m[1mpassed[0m 271331C3 000.00s Disassemble
[34m[1mpassed[0m C7F07619 000.00s Manipulate
[34m[1mpassed[0m E54B8BB1 000.00s Test mutability of the default values
[34m[1mpassed[0m 68DB9CF4 000.00s Create a layer
[34m[1mpassed[0m BE210CA7 000.00s Test the PacketListField assembly
[34m[1mpassed[0m 4A105497 000.00s Test the PacketListField assembly 2
[34m[1mpassed[0m D7560C6C 000.00s Test disassembly
[34m[1mpassed[0m 8EC9F5F9 000.00s Nested PacketListField
[34m[1mpassed[0m F0F8088A 000.00s Create a layer
[34m[1mpassed[0m BE210CA7 000.00s Test the PacketListField assembly
[34m[1mpassed[0m 4A105497 000.00s Test the PacketListField assembly 2
[34m[1mpassed[0m D7560C6C 000.00s Test disassembly
[34m[1mpassed[0m 8EC9F5F9 000.00s Nested PacketListField
[34m[1mpassed[0m 5C773132 000.01s Complex packet
[34m[1mpassed[0m 952B8BB0 000.00s Test calls on TCPOptionsField.getfield
[34m[1mpassed[0m F0F8088A 000.00s Create a layer
[34m[1mpassed[0m BE210CA7 000.00s Test the PacketListField assembly
[34m[1mpassed[0m 4A105497 000.00s Test the PacketListField assembly 2
[34m[1mpassed[0m D7560C6C 000.00s Test disassembly
[34m[1mpassed[0m 8EC9F5F9 000.00s Nested PacketListField
[34m[1mpassed[0m 79CF4B32 000.01s Complex packet
[34m[1mpassed[0m EBD4DC4F 000.00s Create layers for heterogeneous PacketListField
[34m[1mpassed[0m EA657C90 000.00s Test heterogeneous PacketListField
[34m[1mpassed[0m A7CDB158 000.00s Create layers for heterogeneous PacketListField with memory
[34m[1mpassed[0m 39388F3E 000.00s Test heterogeneous PacketListField with memory
[34m[1mpassed[0m E574C4A9 000.00s Test calls on MultiFlagsField.any2i
[34m[1mpassed[0m D4255D03 000.00s Test calls on MultiFlagsField.i2m
[34m[1mpassed[0m 0D183FDA 000.00s Test calls on MultiFlagsField.m2i
[34m[1mpassed[0m BF13311E 000.00s Test calls on MultiFlagsField.i2repr
[34m[1mpassed[0m 8DE519CD 000.00s EnumField tests initialization
[34m[1mpassed[0m 5153B133 000.00s EnumField.any2i_one
[34m[1mpassed[0m 717CDA12 000.00s EnumField.any2i
[34m[1mpassed[0m 36CF7260 000.00s EnumField.i2repr_one
[34m[1mpassed[0m 28FE6765 000.00s EnumField.i2repr
[34m[1mpassed[0m 1597D3EA 000.00s Building expect_exception handler
[34m[1mpassed[0m D688FCD5 000.00s CharEnumField tests initialization
[34m[1mpassed[0m E1F03FE9 000.00s CharEnumField.any2i_one
[34m[1mpassed[0m 1597D3EA 000.00s Building expect_exception handler
[34m[1mpassed[0m B7B39436 000.00s XByteEnumField tests initialization
[34m[1mpassed[0m 95B4EBD9 000.00s XByteEnumField.i2repr_one
[34m[1mpassed[0m 384257A1 000.00s XByteEnumField update tests initialization
[34m[1mpassed[0m F9AD73AB 000.00s XByteEnumField.i2repr_one with update
[34m[1mpassed[0m 1597D3EA 000.00s Building expect_exception handler
[34m[1mpassed[0m 1DA6EA64 000.00s XShortEnumField tests initialization
[34m[1mpassed[0m 95B4EBD9 000.00s XShortEnumField.i2repr_one
[34m[1mpassed[0m 0D59ADD1 000.00s XShortEnumField update tests initialization
[34m[1mpassed[0m F9AD73AB 000.00s XShortEnumField.i2repr_one with update
[34m[1mpassed[0m 4428B855 000.00s Raise exception - test data
[34m[1mpassed[0m 10ABFD9E 000.00s default usage
[34m[1mpassed[0m B0091A9D 000.00s inverted yes - no (scalar config)
[34m[1mpassed[0m F93CFB59 000.00s inverted yes - no (range config)
[34m[1mpassed[0m 89ADCBD1 000.00s yes - no (using sets)
[34m[1mpassed[0m B73E29D0 000.00s yes, no and invalid
[34m[1mpassed[0m 470FA2B0 000.00s invalid scalar spec
[34m[1mpassed[0m A74F4C1B 000.00s invalid range spec - invalid length
[34m[1mpassed[0m BBEDDB92 000.00s invalid range spec - invalid value
[34m[1mpassed[0m 1473586E 000.00s invalid set spec - invalid value
[34m[1mpassed[0m FD5682F6 000.00s FlasgField - Python incompatible name
[34m[1mpassed[0m 7ABC2B56 000.00s Test initialization order
[34m[1mpassed[0m D8E6560B 000.00s Default order
[34m[1mpassed[0m 39AC5ACF 000.00s Reversed order
[34m[1mpassed[0m 99D0148A 000.00s Test default values auto-update
[34m[1mpassed[0m E8107B46 000.00s MultipleTypeField - syntax error
[34m[1mpassed[0m 91DF4F1E 000.00s Test Flags Field Iterator
[34m[1mpassed[0m 9E7F4CB7 000.00s Test upper nibble
[34m[1mpassed[0m 1B04A4FD 000.00s Test lower nibble
[34m[1mpassed[0m 7D3838E6 000.00s Test single flag 1
[34m[1mpassed[0m 571CAF9B 000.00s Test single flag 2
[34m[1mpassed[0m 6A1EFD0B 000.00s Test single flag 0x80
[34m[1mpassed[0m CDAC6203 000.00s Test pattern 0x55
[34m[1mpassed[0m 890D9CEB 000.00s Test pattern 0xAA
[34m[1mpassed[0m 15FCB607 000.00s Test pattern 0x00
[34m[1mpassed[0m 567E8BE8 000.00s Test pattern 0xFF
[34m[1mpassed[0m BF2749BA 000.00s FlagsField with str
[34m[1mpassed[0m 0C4F6B6D 000.00s FlagsField with dict
[34m[1mpassed[0m 44B19AAB 000.00s ScalingField Test default behaviour
[34m[1mpassed[0m A231573C 000.00s ScalingField Test string assignment
[34m[1mpassed[0m D18D7CEF 000.00s ScalingField Test scaling
[34m[1mpassed[0m B56FEC5C 000.00s ScalingField Test scaling signed
[34m[1mpassed[0m 5884C0E1 000.00s ScalingField Test scaling signed offset
[34m[1mpassed[0m 3C241A76 000.00s ScalingField Test scaling offset
[34m[1mpassed[0m AD7F3300 000.00s ScalingField Test unit
[34m[1mpassed[0m B4122C4B 000.00s ScalingField Test unit and ndigits
[34m[1mpassed[0m 100B2821 000.00s ScalingField Test unit and ndigits 2
[34m[1mpassed[0m FDA807AC 000.00s ScalingField Test unit and ndigits 3
[34m[1mpassed[0m E16F5885 000.00s ScalingField randval byte
[34m[1mpassed[0m F67EC324 000.00s ScalingField randval byte 2
[34m[1mpassed[0m 0A84E725 000.00s ScalingField signed randval byte
[34m[1mpassed[0m B8218E92 000.00s ScalingField signed randval byte 2
[34m[1mpassed[0m 620F1A7F 000.00s ScalingField signed randval short
[34m[1mpassed[0m 2C1E2061 000.00s ScalingField signed randval int
[34m[1mpassed[0m A3E507E5 000.00s ScalingField signed randval long
[34m[1mpassed[0m 15384BF6 000.00s ScalingField signed randval long
[34m[1mpassed[0m 17614262 000.00s BitExtendedField: simple test
[34m[1mpassed[0m 11E7CD87 000.00s BitExtendedField i2m: corner values
[34m[1mpassed[0m FA8C776E 000.00s BitExtendedField i2m: field expansion
[34m[1mpassed[0m 63380967 000.00s BitExtendedField i2m: test all FX bit positions
[34m[1mpassed[0m 23EB3DD7 000.00s BitExtendedField m2i: test all FX bit positions
[34m[1mpassed[0m 025CA863 000.00s BitExtendedField m2i: stop at FX zero
[34m[1mpassed[0m 8B69666F 000.00s BitExtendedField m2i: multiple bytes
[34m[1mpassed[0m DC0CB84A 000.00s BitExtendedField m2i: invalid field with no stopping bit
[34m[1mpassed[0m 81347E2B 000.00s LSBExtendedField
[34m[1mpassed[0m 86B97D0E 000.00s MSBExtendedField
[34m[1mpassed[0m C8DF1936 000.00s Field Deprecation test
[34m[1mpassed[0m 824FE140 000.00s FCSField: basic test
[34m[1mpassed[0m 9722690D 000.00s PacketField: randval()
[34m[1mpassed[0m C4C85BD3 000.00s PacketField: randval(), PacketField in PacketField
Campaign CRC=D01E7B57 in 000.15s SHA=1C89C4F7267378A134F4912C4EC7B3E7D47A1377
[34m[1mPASSED=128 FAILED=0[0m
[32m━ Loading: test/imports.uts[0m
[34m[1mpassed[0m 37B9EBD3 000.01s Prepare importing all scapy files
[34m[1mpassed[0m 816770EE 001.07s Try importing all core separately
[34m[1mpassed[0m 1D3DC2E3 003.00s Try importing all layers separately
[34m[1mpassed[0m B57BFE53 003.25s Try importing all contribs separately
Campaign CRC=28239D7B in 007.34s SHA=F2D25F17A0AA5976C19379B8E754F06FEC0A77C5
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/linux.uts[0m
[34m[1mpassed[0m 6C1F3DEA 000.00s IPv6 link-local address selection
[34m[1mpassed[0m BDB9A714 000.00s IPv6
[34m[1mpassed[0m C586475C 000.00s Routing table, interface with no names
[34m[1mpassed[0m FE81D5D6 000.00s Reload interfaces & routes
Campaign CRC=4AA14A75 in 000.01s SHA=148E14999C9FFCBEBD8A6F199B95D74A98FE81B1
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/nmap.uts[0m
[34m[1mpassed[0m D4B85D3C 000.00s Module loading
[34m[1mpassed[0m D4A566B0 000.00s Test functions
[34m[1mpassed[0m 1E5242C9 000.30s Fetch database
[34m[1mpassed[0m 445BCB55 000.04s Database loading
[34m[1mpassed[0m 1E3CA419 000.00s Nmap base not available
[34m[1mpassed[0m 3230DA5F 000.00s Clear temp files
Campaign CRC=5255FC16 in 000.34s SHA=99D1D67A6188DEC77DEBC8726D2887C90321F9A8
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/p0f.uts[0m
[34m[1mpassed[0m FDBDA0E1 000.01s Module loading
[34m[1mpassed[0m 08581CC6 000.27s Fetch database
[34m[1mpassed[0m AEE5211D 000.00s Test TCP p0f, SYN - Windows
[34m[1mpassed[0m D3DDF7DC 000.00s Test TCP p0f, SYN - Linux
[34m[1mpassed[0m 6D3D3134 000.00s Test TCP p0f, SYN - IPv6 FreeBSD
[34m[1mpassed[0m D3DAB7CC 000.00s Test TCP p0f, SYN-ACK - Linux
[34m[1mpassed[0m 25E0D8BE 000.00s Test HTTP p0f, request - wget
[34m[1mpassed[0m A8B31707 000.00s Test HTTP p0f, response - nginx
[34m[1mpassed[0m B470B9E2 000.00s Test MTU p0f
[34m[1mpassed[0m 57328C93 000.00s Check that the impersonated packet is properly detected by p0f
[34m[1mpassed[0m 51FF2E2E 000.00s Check incidence of MSS value on linux version detection
[34m[1mpassed[0m 061C7EE9 000.00s Impersonate when window size must be multiple of some integer
[34m[1mpassed[0m 0734A2D0 000.00s Impersonate when window size must be multiple of mss
[34m[1mpassed[0m 86005C3B 000.00s Impersonate when the following quirks are present: seq-,ack-,pushf+,urgf+
[34m[1mpassed[0m E5AAFFD8 000.00s Use valid option values from original packet
[34m[1mpassed[0m 13B8F121 000.00s Discard invalid options values
[34m[1mpassed[0m 9BA73FDB 000.00s Remove fp files
Campaign CRC=5F92BAA3 in 000.29s SHA=3FE27B3DC58E23C336CA83E42AE82C3C5F7C13BD
[34m[1mPASSED=17 FAILED=0[0m
[32m━ Loading: test/p0fv2.uts[0m
[34m[1mpassed[0m 2BDF8058 000.00s Module loading
[34m[1mpassed[0m 1CAA2D63 001.11s Fetch database
[34m[1mpassed[0m B64E3887 000.00s Test p0f
[34m[1mpassed[0m 080CB4AC 000.00s Test prnp0f
[34m[1mpassed[0m D1A1144A 000.00s Impersonate when window size must be multiple of some integer
[34m[1mpassed[0m E1ED9C6C 000.00s Handle unusual flags ("F") quirk
[34m[1mpassed[0m AE160304 000.00s Use valid option values from original packet
[34m[1mpassed[0m 02854DEE 000.00s Use valid option values when multiples required
[34m[1mpassed[0m 2129AF15 000.00s Discard non-multiple option values when multiples required
[34m[1mpassed[0m 1FC59A60 000.00s Discard bad timestamp values
[34m[1mpassed[0m E2259EB3 000.00s Discard 2nd timestamp of 0 if "T" quirk is present
[34m[1mpassed[0m 101E107E 000.00s Remove fp files
Campaign CRC=95AAC95C in 001.12s SHA=11DFD4A9BB388BC56C63D658EA3702080FCF6ABE
[34m[1mPASSED=12 FAILED=0[0m
[32m━ Loading: test/pipetool.uts[0m
[34m[1mpassed[0m 5C9C4D1E 003.01s Test default test case
[34m[1mpassed[0m 10405756 000.00s Test add_pipe
[34m[1mpassed[0m F205E1DE 000.00s Test exhausted source
[34m[1mpassed[0m DF905DB3 000.00s Test add_pipe on running instance
[34m[1mpassed[0m 04395C32 000.00s Test Operators
[34m[1mpassed[0m 03E71414 000.00s Test doc
[34m[1mpassed[0m 6FD12EEC 000.00s Test RawConsoleSink with CLIFeeder
[34m[1mpassed[0m 5993C5A6 000.00s Test QueueSink with CLIFeeder
[34m[1mpassed[0m 78AB5F06 000.00s Test UpDrain
[34m[1mpassed[0m F37DF15D 000.00s Test DownDrain
[34m[1mpassed[0m B4648AEB 000.00s Test PeriodicSource exhaustion
[34m[1mpassed[0m DBD8B864 000.00s Test SniffSource
[34m[1mpassed[0m 00D6F2A1 000.00s Test SniffSource with socket
[34m[1mpassed[0m E9142AC6 000.00s Test SniffSource with invalid args
[34m[1mpassed[0m A218CCDB 000.00s Test exhausted AutoSource and SniffSource
[34m[1mpassed[0m FE839E4F 000.00s Test WiresharkSink
[34m[1mpassed[0m C17A9E30 000.00s Test WiresharkSink with linktype
[34m[1mpassed[0m 3DDEACF7 000.00s Test WiresharkSink with args
[34m[1mpassed[0m 29727A4D 000.00s Test RdpcapSource and WrpcapSink
[34m[1mpassed[0m 5253C3FC 000.00s TriggerDrain and TriggeredValve with CLIFeeder
[34m[1mpassed[0m 38B83B94 000.00s TriggerDrain and TriggeredValve with CLIHighFeeder
[34m[1mpassed[0m 5253C3FC 000.00s TriggerDrain and TriggeredQueueingValve with CLIFeeder
[34m[1mpassed[0m BDD3E66C 000.00s TriggerDrain and TriggeredSwitch with CLIFeeder on high channel
[34m[1mpassed[0m 046C140A 000.00s TriggerDrain and TriggeredSwitch with CLIHighFeeder on low channel
[34m[1mpassed[0m 1C0C74BE 000.00s TriggerDrain and TriggeredMessage
[34m[1mpassed[0m 4B4F8A83 000.00s TriggerDrain and TriggeredQueueingValve on low channel
[34m[1mpassed[0m 0B3A37E0 000.00s TriggerDrain and TriggeredQueueingValve on high channel
[34m[1mpassed[0m 50B65DF1 000.00s UDPDrain
[34m[1mpassed[0m B242EE60 000.00s FDSourceSink on a ObjectPipe object
Campaign CRC=67F600F3 in 003.06s SHA=D49B9FB418001D0DFCB00A20E7CAF9E9DC005162
[34m[1mPASSED=29 FAILED=0[0m
[32m━ Loading: test/random.uts[0m
[34m[1mpassed[0m FB8E29C4 000.00s RandomEnumeration
[34m[1mpassed[0m 0AA4C4C9 000.00s RandIP6
[34m[1mpassed[0m BA1D742D 000.00s RandMAC
[34m[1mpassed[0m 4FF6687B 000.00s RandOID
[34m[1mpassed[0m F8199EF8 000.00s RandRegExp
[34m[1mpassed[0m 1FFB52B1 000.00s Corrupted(Bytes|Bits)
[34m[1mpassed[0m 5595C82C 000.00s RandEnumKeys
[34m[1mpassed[0m 934A8248 000.00s RandSingNum
[34m[1mpassed[0m 32930193 000.00s Rand*
[34m[1mpassed[0m B54D1038 000.00s RandInt (test __bool__)
[34m[1mpassed[0m 95FC464A 000.00s Various volatiles
Campaign CRC=1BBB5BA3 in 000.01s SHA=D3582E2DA067A2C39CD8BA9A82340C95ADF5A403
[34m[1mPASSED=11 FAILED=0[0m
[32m━ Loading: test/regression.uts[0m
[34m[1mpassed[0m DA599690 000.00s Setup
[34m[1mpassed[0m D18177CF 000.00s Get conf
[34m[1mpassed[0m C7B4EFF2 000.00s Test module version detection
[34m[1mpassed[0m 19EC7768 000.00s List layers
[34m[1mpassed[0m FE0F029B 000.00s List layers - advanced
[34m[1mpassed[0m CA149C8C 000.00s List packet fields - ls
[34m[1mpassed[0m B614219C 000.00s List commands
[34m[1mpassed[0m AD124E63 000.01s List contribs
[34m[1mpassed[0m B7884B09 000.00s Test automatic doc generation
[34m[1mpassed[0m DE8CCBA1 000.00s Check that all contrib modules are well-configured
[34m[1mpassed[0m 0A631592 000.00s Configuration
[34m[1mpassed[0m 3F6538B8 000.00s Configuration conf.use_* LINUX
[34m[1mpassed[0m 37C97003 000.02s Configuration conf.use_pcap
[34m[1mpassed[0m A123BCF3 000.01s Test layer filtering
[34m[1mpassed[0m 970EB61E 000.00s UTscapy route check
[34m[1mpassed[0m BEBF10F5 000.00s Interface related functions
[34m[1mpassed[0m 18F1F0C5 000.00s More Interfaces related functions
[34m[1mpassed[0m FC3E1AC8 000.00s Test conf.ifaces
[34m[1mpassed[0m 009779EA 000.00s Test read_routes6() - default output
[34m[1mpassed[0m 874739C6 000.00s Test read_routes6() - check mandatory routes
[34m[1mpassed[0m 41EBC767 000.00s Test ifchange()
[34m[1mpassed[0m DB13F153 000.00s Packet.route()
[34m[1mpassed[0m 6820815F 000.00s plain_str test
[34m[1mpassed[0m 16835536 000.00s test bytes_hex/hex_bytes
[34m[1mpassed[0m 6288D049 000.00s test gzip_decompress/gzip_compress
[34m[1mpassed[0m 451B4F17 000.00s orb/chb
[34m[1mpassed[0m 630DC34D 000.00s Pickle and unpickle a packet
[34m[1mpassed[0m 29EB7522 000.00s Usage test
[34m[1mpassed[0m 047BBDD9 000.00s Session test
[34m[1mpassed[0m 358903D2 000.00s Session test with fname
[34m[1mpassed[0m 77972341 000.00s Clear session files
[34m[1mpassed[0m 26B0188A 000.00s Test temporary file creation
[34m[1mpassed[0m F3CA4AF5 000.01s Emulate interact()
[34m[1mpassed[0m ADB2A4AB 000.01s Test explore() with GUI mode
[34m[1mpassed[0m 0BA85D98 000.00s Test explore() with non-GUI mode
[34m[1mpassed[0m E528FB12 000.01s Test load_contrib overwrite
[34m[1mpassed[0m E0AD57DF 000.00s Test load_contrib failure
[34m[1mpassed[0m B97A8D27 000.00s Test sane function
[34m[1mpassed[0m 0F048235 000.00s Test lhex function
[34m[1mpassed[0m EFAA494A 000.01s Test restart function
[34m[1mpassed[0m 709E8D59 000.00s Test linehexdump function
[34m[1mpassed[0m 84F60AFB 000.00s Test chexdump function
[34m[1mpassed[0m 77D2AF54 000.00s Test repr_hex function
[34m[1mpassed[0m 18D9F734 000.00s Test hexstr function
[34m[1mpassed[0m AD979794 000.00s Test fletcher16 functions
[34m[1mpassed[0m 4F2BCB69 000.44s Test hexdiff function
[34m[1mpassed[0m 5412F8DD 000.00s Test mysummary functions - Ether
[34m[1mpassed[0m 438CB37E 000.00s Test zerofree_randstring function
[34m[1mpassed[0m F663F014 000.00s Test strand function
[34m[1mpassed[0m AE5CA56C 000.00s Test export_object and import_object functions
[34m[1mpassed[0m 15EB18BA 000.00s Test tex_escape function
[34m[1mpassed[0m 264A2A33 000.00s Test colgen function
[34m[1mpassed[0m C05BFAC1 000.00s Test incremental_label function
[34m[1mpassed[0m 92E11F43 000.00s Test corrupt_* functions
[34m[1mpassed[0m B3149865 000.00s Test save_object and load_object functions
[34m[1mpassed[0m 8000B16F 000.26s Test whois function
[31m[1mfailed[0m BB02F984 000.00s Test manuf DB methods
[34m[1mpassed[0m 55C51765 000.00s Test multiple wireshark's manuf formats
[34m[1mpassed[0m D22D73D8 000.00s Test load_services
[34m[1mpassed[0m 94FFDA87 000.32s Test utility functions - network related
[34m[1mpassed[0m E4205DC0 000.00s Test autorun functions
Running as user "root" and group "root". This could be dangerous.
Running as user "root" and group "root". This could be dangerous.
Running as user "root" and group "root". This could be dangerous.
*[34m[1mpassed[0m 1CDEA5CA 000.00s Test autorun with logging
[34m[1mpassed[0m 33DA38EA 000.00s Test utility TEX functions
[34m[1mpassed[0m 27B33D76 000.00s Test config file functions
[34m[1mpassed[0m ACF8754F 000.00s Test config file functions failures
[34m[1mpassed[0m 79DA91B5 000.00s Test CacheInstance repr
[34m[1mpassed[0m BB1482F9 000.00s Test pyx detection functions
[34m[1mpassed[0m 0F68215F 000.00s Test matplotlib detection functions
[34m[1mpassed[0m AD8592A5 000.00s Packet class methods
[34m[1mpassed[0m 7019404B 000.00s hide_defaults
[34m[1mpassed[0m C871CB89 000.00s split_layers
[34m[1mpassed[0m 3635E2A7 000.00s fuzz
[34m[1mpassed[0m FE9D1A24 000.00s fuzz a Packet with MultipleTypeField
[34m[1mpassed[0m 48E1CA2A 000.00s fuzz on packets with advanced RandNum
[34m[1mpassed[0m 52407322 000.00s fuzz on packets with FlagsField
[34m[1mpassed[0m 6CABED80 000.00s Building some packets
[34m[1mpassed[0m 8A5DFB7D 000.00s Manipulating some packets
[34m[1mpassed[0m 836BF8D1 000.00s Bind string array as payload
[34m[1mpassed[0m 4E09A425 000.00s Checking overloads
[34m[1mpassed[0m 3E36F166 000.00s sprintf() function
[34m[1mpassed[0m 5D99FA28 000.00s sprintf() function
[34m[1mpassed[0m F24A9F91 000.00s haslayer function
[34m[1mpassed[0m 7B185480 000.00s getlayer function
[34m[1mpassed[0m 3F096904 000.00s getlayer / haslayer with name
[34m[1mpassed[0m EB905B84 000.00s getlayer with a filter
[34m[1mpassed[0m 1751C560 000.00s specific haslayer and getlayer implementations for EAP
[34m[1mpassed[0m 69995C65 000.00s specific haslayer and getlayer implementations for RadiusAttribute
[34m[1mpassed[0m 7F8D0DEC 000.00s equality
[34m[1mpassed[0m 8C9734CF 000.00s answers
[34m[1mpassed[0m FA97BD89 000.00s answers - Net
[34m[1mpassed[0m 82B9D32E 000.00s conf.checkIPsrc
[34m[1mpassed[0m 5921AF76 000.00s Padding assembly
[34m[1mpassed[0m A9AF49AF 000.00s Padding and length computation
[34m[1mpassed[0m 2814B0C5 000.00s PadField test
[34m[1mpassed[0m 15BD6ED7 000.00s ReversePadField
[34m[1mpassed[0m CBAAEDAF 000.00s Creation of an IPv3 class from IP class with different default values
[34m[1mpassed[0m 0E3B8822 000.00s Test of IPv3 class
[34m[1mpassed[0m 078501B1 000.00s ASN1 - ASN1_Object
[34m[1mpassed[0m A5976424 000.00s ASN1 - RandASN1Object
[34m[1mpassed[0m 7EA44FC4 000.00s ASN1 - ASN1_BIT_STRING
[34m[1mpassed[0m 5CF0AB92 000.00s ASN1 - ASN1_SEQUENCE
[34m[1mpassed[0m 3AA85782 000.00s ASN1 - ASN1_DECODING_ERROR
[34m[1mpassed[0m DD7EF478 000.00s ASN1 - ASN1_INTEGER
[34m[1mpassed[0m 0613C657 000.00s ASN1 - ASN1_OID
[34m[1mpassed[0m 7E6A9D70 000.00s RandASN1Object(), specific crashes
[34m[1mpassed[0m 01E62F5E 000.00s SSID is parsed properly even with the presence of RSN Information
[34m[1mpassed[0m D5631F8D 000.27s Whois request
[34m[1mpassed[0m 2FB8BF66 003.89s AS resolvers
[34m[1mpassed[0m C8EED631 000.68s AS resolver - IPv6
[34m[1mpassed[0m 0FA8EBD5 000.00s AS resolver - socket error
[34m[1mpassed[0m A0F4B95B 000.01s sendpfast
[34m[1mpassed[0m 6E277EB6 000.00s Implicit logic 1
[34m[1mpassed[0m 4C656AED 000.00s Implicit logic 2
[34m[1mpassed[0m 65799897 000.00s Implicit logic 3
[34m[1mpassed[0m 3D53515F 000.00s Test SuperSocket.select
[34m[1mpassed[0m 6746E7CA 000.00s __repr__
[34m[1mpassed[0m 1583A3C8 000.00s check _resolve_MAC
[34m[1mpassed[0m 2C2CF3CF 000.00s Variable creations
[34m[1mpassed[0m 4F9FD49A 000.00s Read a pcap file
[34m[1mpassed[0m 2B295E32 000.00s Read a pcapng file
[34m[1mpassed[0m 9B99CFB9 000.00s Read a pcap file with nanosecond precision
[34m[1mpassed[0m 6B69CA4B 000.00s Read a pcapng file with nanosecond precision and default tsresol
[34m[1mpassed[0m 99487D9B 000.00s Read a pcapng with little-endian SHB
[34m[1mpassed[0m B86EA77D 000.00s Read a pcap file with wirelen != captured len
[34m[1mpassed[0m 1A36F5AE 000.00s Check all packet lists are the same
[34m[1mpassed[0m B2AE1B2E 000.00s Check packets from pcap file
[34m[1mpassed[0m 81B3996C 000.00s Check wirelen value from pcap file
[34m[1mpassed[0m 3B142116 000.00s Check wrpcap() then rdpcap() with wirelen
[34m[1mpassed[0m 160D8ACD 000.00s Check wrpcap() then rdpcap() with sent_time on SndRcvList
[34m[1mpassed[0m E20CA410 000.00s Check wrpcap()
[34m[1mpassed[0m C18FCEC3 000.00s Check offline sniff() (by PacketList)
[34m[1mpassed[0m 5DB7D967 000.00s Check offline sniff() (by filename)
[34m[1mpassed[0m 2F421D82 000.00s Check offline sniff() (by file object)
[31m[1mfailed[0m 3C94713B 000.01s Check offline sniff() with a filter (by filename)
[31m[1mfailed[0m FA2B2E6F 000.00s Check offline sniff() with a filter (by file object)
[31m[1mfailed[0m 9F9CD740 000.01s Check offline sniff() with a PcapNg file and a filter (by file object)
[31m[1mfailed[0m ED0A048B 000.00s Check offline sniff() with Packets and tcpdump
[34m[1mpassed[0m 3BF7ACD4 000.00s Check offline sniff() with Packets, tcpdump and a bad filter
[34m[1mpassed[0m E8881540 000.00s Check offline sniff with lfilter
[34m[1mpassed[0m C4425291 000.00s Check offline sniff() without a tcpdump binary
[34m[1mpassed[0m B8A9D336 000.00s Check wrpcap(nano=True)
[34m[1mpassed[0m 8C272C25 000.00s Check PcapNg with nanosecond precision using obsolete packet block
[34m[1mpassed[0m 44D28963 000.00s Check PcapNg using Simple Packet Block
[34m[1mpassed[0m 9B9AA394 000.00s Invalid pcapng files
[34m[1mpassed[0m 9948C982 000.00s Check PcapWriter on null write
[34m[1mpassed[0m 238CECEE 000.00s Check PcapWriter sets correct linktype after null write
[34m[1mpassed[0m 30CD1304 000.00s Check RawPcapReader on pcap
[34m[1mpassed[0m BBF8DDD9 000.00s Check RawPcapWriter
[31m[1mfailed[0m BFEC162C 000.00s Check tcpdump()
[34m[1mpassed[0m 12CFDB8E 000.00s Check tcpdump() command with linktype
[34m[1mpassed[0m 06544347 000.00s Check tcpdump() command with linktype and args
[31m[1mfailed[0m 15AD5567 000.01s Check sniff() offline with linktype & 802.11 filter
[34m[1mpassed[0m 03178F06 000.00s Check tcpdump() command rejects non-string input for prog
[34m[1mpassed[0m A1537C4A 000.11s Check tcpdump() command with tshark
[34m[1mpassed[0m 206EA769 000.25s Check tdecode command directly for tshark
[34m[1mpassed[0m 4B70552F 000.10s Check tdecode with linktype
[34m[1mpassed[0m 4384A0D9 000.00s Check wireshark()
[34m[1mpassed[0m 81CC510A 000.00s Check Raw IP pcap files
[34m[1mpassed[0m C465B88B 000.00s Check wrpcap() with no packet
[34m[1mpassed[0m A03B785B 000.00s Check wrpcap() with SndRcvList
[34m[1mpassed[0m 0756A969 000.00s Check wrpcap() with different packets types
[34m[1mpassed[0m 7F49B1DD 000.01s Truncated netstat -rn output on OS X
[34m[1mpassed[0m 34304D0C 000.01s macOS 10.13
[34m[1mpassed[0m 036E8133 000.01s macOS 10.15
[34m[1mpassed[0m 2995D7BF 000.01s OpenBSD 6.3
[34m[1mpassed[0m A5E84ED4 000.01s Solaris 11.1
[34m[1mpassed[0m 3F3EA2A4 000.00s Test mocked _parse_tcpreplay_result
[34m[1mpassed[0m A449085C 000.00s Test more recent version with flows
[34m[1mpassed[0m 7E87495F 000.00s Preliminary definitions
[34m[1mpassed[0m B5FCB7EF 000.01s Mac OS X 10.9.5
[34m[1mpassed[0m 2CE5D0CA 000.01s Mac OS X 10.9.5 with global IPv6 connectivity
[34m[1mpassed[0m 9AD01A8D 000.00s Mac OS X 10.10.4
[34m[1mpassed[0m DB273570 000.01s FreeBSD 10.2
[34m[1mpassed[0m FE5A0B20 000.01s FreeBSD 13.0
[34m[1mpassed[0m 07695D00 000.01s OpenBSD 5.5
[34m[1mpassed[0m 3DB372CE 000.01s NetBSD 7.0
[34m[1mpassed[0m A689E46C 000.01s Mocked IPv4 routes calls
[34m[1mpassed[0m E7AB1032 000.01s Mocked IPv6 routes calls
[34m[1mpassed[0m E9342B72 000.00s Find a link-local address when conf.iface does not support IPv6
[34m[1mpassed[0m 2255E1EB 000.00s Windows: reset routes properly
[34m[1mpassed[0m 57B42A03 000.01s Test with DNS over TCP
[34m[1mpassed[0m EC7AE892 000.00s Test with recv() calls that return exact packet-length rawings
[34m[1mpassed[0m DA9BE4E7 000.00s Test with recv() calls that return twice as much data as the exact packet-length
[34m[1mpassed[0m 3382073D 000.00s Test with recv() calls that return not enough data
[34m[1mpassed[0m 7F5F6D30 000.00s IPv6 bin to rawing conversion
[34m[1mpassed[0m 7F1C114E 000.00s IPv6 bin to rawing conversion - Zero-block of length 1
[34m[1mpassed[0m B043B4EE 000.00s IPv6 bin to rawing conversion - Illegal sizes
[34m[1mpassed[0m F8B22202 000.00s Net
[34m[1mpassed[0m 0999A1C4 000.00s Net using name
[34m[1mpassed[0m 5B4904DD 000.00s Multiple IP addresses test
[34m[1mpassed[0m 2609BE5E 000.00s OID
[34m[1mpassed[0m AD4A8CE3 000.00s Net6
[34m[1mpassed[0m E5893D82 000.00s Test repr on Net
[34m[1mpassed[0m F878CD1A 000.00s in6_getLocalUniquePrefix()
[34m[1mpassed[0m 4E154B45 000.00s Misc addresses manipulation functions
[34m[1mpassed[0m 9B356652 000.00s in6_getscope()
[34m[1mpassed[0m 158E29B1 000.00s construct_source_candidate_set()
[34m[1mpassed[0m 8F99F845 000.00s inet_pton()
[34m[1mpassed[0m 3E6AD142 000.00s make_route()
[34m[1mpassed[0m 7C251239 000.00s add() & delt()
[34m[1mpassed[0m C132633E 000.00s ifchange()
[34m[1mpassed[0m 163CE9C0 000.00s ifdel()
[34m[1mpassed[0m DB35A643 000.00s ifadd() & get_if_bcast()
[34m[1mpassed[0m AB5C26EE 000.00s IP flags
[34m[1mpassed[0m F79BD7F8 000.00s TCP flags
[34m[1mpassed[0m E2D16013 000.00s Flag values mutation with .raw_packet_cache
[34m[1mpassed[0m B29AD6EA 000.00s Operations on flag values
[34m[1mpassed[0m 09859BDA 000.00s Test detection
[34m[1mpassed[0m AD2D7A3C 000.00s MIB
[34m[1mpassed[0m 54015052 000.03s MIB - graph
[34m[1mpassed[0m 80453ECF 000.00s MIB - test aliases
[34m[1mpassed[0m 13DE7129 000.00s DADict tests
[34m[1mpassed[0m 0F3147E1 000.00s Test ETHER_TYPES
[34m[1mpassed[0m 741D539A 000.00s BER tests
[34m[1mpassed[0m 902D8DDD 000.00s BER trigger failures
[34m[1mpassed[0m A32AA0D6 000.00s FieldLenField with BitField
[34m[1mpassed[0m 717AED56 000.00s PacketListField
[34m[1mpassed[0m 8C5199F1 000.00s Test PacketListField deepcopy
[34m[1mpassed[0m EE5096F6 000.00s PacketField
[34m[1mpassed[0m FA8512FC 000.00s Parsing a human-readable UUID
[34m[1mpassed[0m 20F8FDCC 000.00s Parsing a machine-encoded UUID
[34m[1mpassed[0m 6D66DB8E 000.00s Parsing a tuple of values
[34m[1mpassed[0m 43FF993A 000.00s Handle None values
[34m[1mpassed[0m 84F5FFBA 000.00s Get a UUID for dissection
[34m[1mpassed[0m E2A34AC6 000.00s Verify little endian UUIDField
[34m[1mpassed[0m 814A1D27 000.00s Verify reversed UUIDField
[34m[1mpassed[0m 84A2B964 000.00s RandUUID setup
[34m[1mpassed[0m 54DEBA8F 000.00s RandUUID default behaviour
[34m[1mpassed[0m F3EF8632 000.00s RandUUID incorrect implicit args
[34m[1mpassed[0m FDED75F1 000.00s RandUUID v4 UUID (correct args)
[34m[1mpassed[0m EC5945DF 000.00s RandUUID v4 UUID (incorrect args)
[34m[1mpassed[0m 5C0AB483 000.00s RandUUID v1 UUID
[34m[1mpassed[0m ECECDA5B 000.00s RandUUID v1 UUID (implicit version)
[34m[1mpassed[0m 3060B0FE 000.00s RandUUID v1 UUID (incorrect args)
[34m[1mpassed[0m 568DB606 000.00s RandUUID v5 UUID
[34m[1mpassed[0m 367129C0 000.00s RandUUID v5 UUID (incorrect args)
[34m[1mpassed[0m 3454E097 000.00s RandUUID v3 UUID
[34m[1mpassed[0m 367129C0 000.00s RandUUID v3 UUID (incorrect args)
[34m[1mpassed[0m 650D0FCF 000.00s RandUUID looks like a UUID with str
[34m[1mpassed[0m F110F700 000.00s RandUUID with a static part
[34m[1mpassed[0m B1A68738 000.00s RandUUID with a range part
[34m[1mpassed[0m 64ED434C 000.00s MPLS - build/dissection
[34m[1mpassed[0m B37C9BC5 000.00s MPLS encapsulated Ethernet with CW - build/dissection
[34m[1mpassed[0m 90BFA850 000.00s MPLS encapsulated Ethernet without CW - build/dissection
[34m[1mpassed[0m F5E6E24B 000.00s MPLS encapsulated IP - build/dissection
[34m[1mpassed[0m 176FDD85 000.00s sr()
[34m[1mpassed[0m 1E6ADEC5 000.00s pickle test
[34m[1mpassed[0m 85668C29 000.00s plot()
[34m[1mpassed[0m 791AD790 000.00s diffplot()
[34m[1mpassed[0m F8DDA873 000.00s multiplot()
[34m[1mpassed[0m 1F8ED2D6 000.00s rawhexdump()
[34m[1mpassed[0m D5AE450E 000.00s hexraw()
[34m[1mpassed[0m 8CE8F6CC 000.00s hexdump()
[34m[1mpassed[0m DB8A3CCD 000.00s import_hexcap()
[34m[1mpassed[0m 418D2AC7 000.00s import_hexcap(input_string)
[34m[1mpassed[0m B738C569 000.00s padding()
[34m[1mpassed[0m 19C50702 000.00s nzpadding()
[34m[1mpassed[0m 3C28DA66 000.01s conversations()
[34m[1mpassed[0m 0665A5AB 000.00s sessions()
[34m[1mpassed[0m 6EDE7474 000.00s afterglow()
[34m[1mpassed[0m 94B7A8FE 000.00s psdump()
[34m[1mpassed[0m 21DA85E5 000.00s pdfdump()
[34m[1mpassed[0m 3F79992C 000.00s svgdump()
[34m[1mpassed[0m 99F51C1E 000.00s __getstate__ / __setstate__ (used by pickle)
[34m[1mpassed[0m 52CFA6F8 000.08s _version()
[34m[1mpassed[0m 7E1C8D9B 000.00s UTscapy HTML output
[34m[1mpassed[0m 7B4709F1 000.00s test get_temp_dir
[34m[1mpassed[0m 6ECAAD5D 000.01s test fragleak functions
Campaign CRC=54067941 in 006.96s SHA=1D6443BFCD67B514681890FD99775E3FFB6B29E8
[31m[1mPASSED=261 FAILED=7[0m
[32m━ Loading: test/sendsniff.uts[0m
Campaign CRC=7AFEEBF7 in 000.00s SHA=8487302C6C12460EAB9B53870F28C411F5206A94
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/sslv2.uts[0m
[34m[1mpassed[0m 8A6657FE 000.00s Reading SSLv2 session - Loading unparsed SSLv2 records
[34m[1mpassed[0m 146D9669 000.00s Reading SSLv2 session - SSLv2 parsing does not raise any error
[34m[1mpassed[0m 1E319EB4 000.00s Reading SSLv2 session - Record with cleartext
[34m[1mpassed[0m 6802D577 000.00s Reading SSLv2 session - Record __getitem__
[34m[1mpassed[0m EA38711E 000.00s Reading SSLv2 session - ClientHello
[31m[1mfailed[0m F508F1C7 000.01s Reading SSLv2 session - ServerHello
[31m[1mfailed[0m FEB3285E 000.00s Reading SSLv2 session - ClientMasterKey with unknown server key
[34m[1mpassed[0m 4AB8636B 000.00s Reading SSLv2 session - Importing server compromised key
[31m[1mfailed[0m B672832B 000.00s Reading SSLv2 session - ClientMasterKey with compromised server key
[31m[1mfailed[0m 23E3A78B 000.00s Reading SSLv2 session - Checking session secrets
[31m[1mfailed[0m 86A5B458 000.00s Reading SSLv2 session - Record with ciphertext
[31m[1mfailed[0m D40CC003 000.00s Reading SSLv2 session - ServerVerify
[31m[1mfailed[0m 9524473A 000.00s Reading SSLv2 session - ClientFinished
[31m[1mfailed[0m 07FEBDE6 000.00s Reading SSLv2 session - RequestCertificate
[31m[1mfailed[0m 746B2B50 000.00s Reading SSLv2 session - ClientCertificate
[31m[1mfailed[0m 84FCDE31 000.00s Reading SSLv2 session - ServerFinished
[31m[1mfailed[0m BC3A7EF4 000.00s Reading SSLv2 session - Application data
[31m[1mfailed[0m C64B02EC 000.00s Reading SSLv2 session - Checking final sequence numbers
[31m[1mfailed[0m 23F24CE3 000.00s Check TLS-related scapy internals - Checking raw() harmlessness (with RC4)
[31m[1mfailed[0m DC436DCC 000.00s Check TLS-related scapy internals - Checking show2() harmlessness (with RC4)
[31m[1mfailed[0m 8C36E060 000.02s Check TLS-related scapy internals - Checking show2() harmlessness (with 3DES)
[34m[1mpassed[0m C92A29DD 000.03s Check TLS-related scapy internals - Checking tls_session freeze during show2()
[34m[1mpassed[0m 4D6AB548 000.00s Check TLS-related scapy internals - Checking SSLv2 cast from TLS class
[31m[1mfailed[0m 6F807B3A 000.00s Building SSLv2 packets - Various default messages
[34m[1mpassed[0m 3C3264EF 000.00s Building SSLv2 packets - Error within clear record
[34m[1mpassed[0m 3B4095F3 000.00s Building SSLv2 packets - ClientHello with automatic length computation
[31m[1mfailed[0m E7B2C5B9 000.00s Building SSLv2 packets - ClientMasterKey context linking
Campaign CRC=8B018C63 in 000.07s SHA=CB74DF4DA7E403226B569CDB6B1DA103544906E4
[31m[1mPASSED=10 FAILED=17[0m
[32m━ Loading: test/tftp.uts[0m
[34m[1mpassed[0m CBBFDA20 000.00s Test answers
[34m[1mpassed[0m D559286B 000.00s Utilities
[34m[1mpassed[0m F88AFFD0 000.00s TFTP_read() automaton
[34m[1mpassed[0m A974A974 000.00s TFTP_read() automaton error
[34m[1mpassed[0m C8958E7A 000.00s TFTP_write() automaton
[34m[1mpassed[0m 46A32A1B 000.00s TFTP_write() automaton error
[34m[1mpassed[0m 34A6D0CC 000.00s TFTP_WRQ_server() automaton
[34m[1mpassed[0m 4C0A9FCA 000.00s TFTP_WRQ_server() automaton with options
[34m[1mpassed[0m 4FF55CC4 000.01s TFTP_RRQ_server() automaton
Campaign CRC=913D7EA5 in 000.03s SHA=3A46E0AF5C478AAD6EA6C1B0822E5EEC7DC92353
[34m[1mPASSED=9 FAILED=0[0m
[32m━ Loading: test/tls.uts[0m
[34m[1mpassed[0m B0887572 000.00s Crypto - Hmac_MD5 instantiation, parameter check
[34m[1mpassed[0m 6AED9608 000.00s Crypto - Hmac_MD5 behavior on test vectors from RFC 2202 (+ errata)
[34m[1mpassed[0m 0297B3F0 000.00s Crypto - Hmac_SHA instantiation, parameter check
[34m[1mpassed[0m 23EB1663 000.00s Crypto - Hmac_SHA behavior on test vectors from RFC 2202 (+ errata)
[34m[1mpassed[0m C1256CD4 000.02s Crypto - Hmac_SHA2 behavior on test vectors from RFC 4231
[34m[1mpassed[0m 28378727 000.00s Crypto - _tls_P_MD5 behavior on test vectors borrowed from RFC 2202 (+ errata)
[34m[1mpassed[0m 37B323C2 000.00s Crypto - _tls_P_SHA1 behavior on test vectors borrowed from RFC 2202 (+ errata)
[34m[1mpassed[0m 127C32D6 000.00s Crypto - _tls_PRF behavior on test vectors borrowed from RFC 2202 (+ errata)
[34m[1mpassed[0m A2CBB7AF 000.00s Crypto - _ssl_PRF behavior on test vectors
[34m[1mpassed[0m 9A46A7F3 000.00s Crypto - _tls12_*_PRF behavior, using SHA-256, SHA-384 and SHA-512
[34m[1mpassed[0m F292F15D 000.00s Crypto - compute_master_secret() in SSL mode
[34m[1mpassed[0m B776A9FB 000.00s Crypto - derive_key_block() in SSL mode
[34m[1mpassed[0m B48D9F3D 000.00s Crypto - compute_master_secret() in TLS 1.0 mode
[34m[1mpassed[0m 425B2666 000.00s Crypto - derive_key_block() in TLS 1.0 mode
[31m[1mfailed[0m CB4B0C0B 000.00s Crypto - RC4 stream cipher, encryption/decryption checks from RFC 6229
[34m[1mpassed[0m E2591B36 000.00s Crypto - RC2 block cipher, encryption/decryption checks from RFC 2268
[31m[1mfailed[0m 4ADC4444 000.00s Crypto - DES cipher in CBC mode, check from FIPS PUB 81
[31m[1mfailed[0m 3EBDCB1A 000.00s Crypto - AES cipher in CBC mode, checks from RFC 3602
[31m[1mfailed[0m ECF05A71 000.01s Crypto - AES cipher in GCM mode, auth_encrypt() and auth_decrypt() checks
[31m[1mfailed[0m 302EEB44 000.00s Crypto - Camellia cipher, encryption/decryption checks
[34m[1mpassed[0m E4AAFE42 000.00s Reading test session - Loading unparsed TLS records
[31m[1mfailed[0m A7134BD9 000.02s Reading TLS test session - TLS parsing (no encryption) does not throw any error
[34m[1mpassed[0m CA71F728 000.00s Reading TLS test session - TLS Record header
[34m[1mpassed[0m 49773585 000.00s Reading TLS test session - TLS Record __getitem__
[34m[1mpassed[0m 2845C9AD 000.00s Reading TLS test session - ClientHello
[34m[1mpassed[0m 56983416 000.00s Reading TLS test session - ClientHello extensions
[34m[1mpassed[0m F0DB34E1 000.00s Reading TLS test session - ServerHello
[31m[1mfailed[0m 7452ADA2 000.00s Reading TLS test session - Certificate
[31m[1mfailed[0m F6B2FD5D 000.00s Reading TLS test session - Multiple TLS layers
[31m[1mfailed[0m 8387A8AE 000.00s Reading TLS test session - CertificateStatus
[31m[1mfailed[0m 5238E3FE 000.00s Reading TLS test session - ServerKeyExchange
[31m[1mfailed[0m 4C78696F 000.00s Reading TLS test session - ServerHelloDone
[31m[1mfailed[0m C68603B3 000.00s Reading TLS test session - Context checks after 1st RTT
[31m[1mfailed[0m 01CE4161 000.00s Reading TLS test session - TLS parsing (with encryption) does not throw any error
[31m[1mfailed[0m 6D5B39A2 000.00s Reading TLS test session - ClientKeyExchange
[31m[1mfailed[0m 929C3324 000.00s Reading TLS test session - ChangeCipherSpec
[31m[1mfailed[0m B048FB5B 000.00s Reading TLS test session - Finished
[31m[1mfailed[0m DB611497 000.00s Reading TLS test session - Ticket, CCS & Finished
[31m[1mfailed[0m 3CC6736C 000.03s Building x25519 ecdh_Yc
[31m[1mfailed[0m 19B2F607 000.01s Reading TLS test session - Extended master secret
[31m[1mfailed[0m 65A38C52 000.01s Reading TLS test session - Encrypt-then-MAC extension
[34m[1mpassed[0m 523B0943 000.01s Reading TLS test session - Full TLSNewSessionTicket captured
[31m[1mfailed[0m 9BFD9BEA 000.00s Reading TLS test session - ApplicationData
[34m[1mpassed[0m E16C3CFB 000.00s Reading TLS msg dissect - Packet too small
[34m[1mpassed[0m 98A06F75 000.00s Reading TLS msg dissect - Wrong data
[34m[1mpassed[0m 1186A8BE 000.00s Test x25519 dissection in ServerKeyExchange
[34m[1mpassed[0m 5AC0E4EC 000.00s Reading test session - Loading unparsed TLS records
[31m[1mfailed[0m 5F629369 000.02s Reading TLS test session
[31m[1mfailed[0m ED9B3F77 000.00s Verify TLSClientKeyExchange
[31m[1mfailed[0m 4315CF82 000.00s Verify TLSChangeCipherSpec
[31m[1mfailed[0m 0987A23C 000.00s Verify TLSFinished
[31m[1mfailed[0m 7129D1EC 000.00s Verify MAC - TLSFinished record
[31m[1mfailed[0m 217FD24E 000.00s Reading TLS vulnerable session - Decrypt data from using a compromised server key
[31m[1mfailed[0m B61F8BD0 000.25s Auto provide the session
[34m[1mpassed[0m F2E4303D 000.00s Building packets - Various default records
[34m[1mpassed[0m E1D73B3A 000.01s Building packets - ClientHello with automatic length computation
[31m[1mfailed[0m 5F9959B8 000.00s Building packets - application data with Encrypt-then-MAC
[31m[1mfailed[0m F348CBB9 000.00s Building packets - ServerHello context linking
[34m[1mpassed[0m D9A9BEAF 000.00s Building packets - ChangeCipherSpec with forged, forbidden field values
[34m[1mpassed[0m 432509F2 000.00s Building packets - TLS record with bad data
[34m[1mpassed[0m 2F9A29BF 000.00s Building packets - _CipherSuitesField with no cipher
[34m[1mpassed[0m DDE4A240 000.00s Building packets - TLSClientKeyExchange with bad data
[34m[1mpassed[0m 6D689D9A 000.00s Building packets - Perform dummy session update
[34m[1mpassed[0m 86FD1BCD 000.01s Cryptography module is unavailable
[34m[1mpassed[0m B4DE5629 000.00s Truncated TCP segment
[34m[1mpassed[0m 92FED23E 000.00s Test tlsSession
[34m[1mpassed[0m F3D78A5B 000.00s Test connState
[31m[1mfailed[0m 968E928A 000.06s Test tls.tools
[34m[1mpassed[0m 2CDF5401 000.00s Dissect TLSCertificateVerify
[31m[1mfailed[0m 47862E1B 000.01s Test complex TLSServerKeyExchange dissection & build
[34m[1mpassed[0m 45A1F7E4 000.00s Issue 2763
[31m[1mfailed[0m E8F97B8C 000.02s Test TLS TCP defragmentation
[31m[1mfailed[0m 0BBC7C36 000.00s Issue 2527
[34m[1mpassed[0m 05A72F45 000.01s Issue 2778
[34m[1mpassed[0m 7768B96B 000.00s PR/Issue 3295
[31m[1mfailed[0m 6600E46D 000.00s Issue 3324 - FFDH support
[31m[1mfailed[0m 0F34B22E 000.01s OCSP: payload after OCSP - GH3291
[31m[1mfailed[0m 4AD94D0E 000.01s pcap file & external TLS Key Log file
[31m[1mfailed[0m 7E2B7CF5 000.02s pcapng file with a Decryption Secrets Block
Campaign CRC=D31219F9 in 000.60s SHA=5BA9DCB5C29167A36743185946A1A8310F4BB81E
[31m[1mPASSED=41 FAILED=38[0m
[32m━ Loading: test/tls13.uts[0m
[34m[1mpassed[0m 7BE14281 000.00s Reading test session - Loading unparsed TLS 1.3 records
[31m[1mfailed[0m BDAF6302 000.00s Reading TLS 1.3 session - TLS parsing (no encryption) does not throw any error
[34m[1mpassed[0m 3A61BBB2 000.00s Reading TLS 1.3 session - TLS Record header
[34m[1mpassed[0m 49773585 000.00s Reading TLS 1.3 session - TLS Record __getitem__
[34m[1mpassed[0m 8853DDEE 000.00s Reading TLS 1.3 session - ClientHello
[34m[1mpassed[0m 682B4C02 000.00s Reading TLS 1.3 session - ClientHello extensions
[31m[1mfailed[0m F2DB7FF0 000.00s Reading TLS 1.3 session - ServerHello
[31m[1mfailed[0m 134D533F 000.00s Reading TLS 1.3 session - TLS parsing (with encryption) does not throw any error
[31m[1mfailed[0m E97E0673 000.00s Reading TLS 1.3 session - TLS13 Record header
[31m[1mfailed[0m 38EC62C5 000.00s Reading TLS 1.3 session - TLS13 Record __getitem__
[31m[1mfailed[0m 2E2010FD 000.00s Reading TLS 1.3 session - TLS13 ApplicationData
[34m[1mpassed[0m 2828899B 000.00s Decrypt a TLS 1.3 session with a retry - Parse first ClientHello
[31m[1mfailed[0m ACDABE4F 000.00s Decrypt a TLS 1.3 session with a retry - Parse ServerHelloRetryRequest
[34m[1mpassed[0m 2F2E5949 000.01s Decrypt a TLS 1.3 session with a retry - Parse second ClientHello
[31m[1mfailed[0m 49A93428 000.00s Decrypt a TLS 1.3 session with a retry - Parse ServerHello
[31m[1mfailed[0m 4791488A 000.00s Decrypt a TLS 1.3 session with a retry - Handshake traffic secret derivation
[31m[1mfailed[0m 24EED56A 000.00s Decrypt a TLS 1.3 session with a retry - Server handshake traffic key calculation
[31m[1mfailed[0m D73D4ABC 000.00s Decrypt a TLS 1.3 session with a retry - Decrypt and parse server handshake
[31m[1mfailed[0m 14A74342 000.00s Decrypt a TLS 1.3 session with a retry - Client handshake traffic key calculation
[31m[1mfailed[0m 7DD21E98 000.00s Decrypt a TLS 1.3 session with a retry - Decrypt and parse client finished
[31m[1mfailed[0m 8A2FC06A 000.00s Decrypt a TLS 1.3 session with a retry - Application traffic secret derivation
[31m[1mfailed[0m 238E8C38 000.00s Decrypt a TLS 1.3 session with a retry - Application traffic keys calculation
[31m[1mfailed[0m 49496441 000.00s Decrypt a TLS 1.3 session with a retry - Decrypt and parse client Alert
[31m[1mfailed[0m 514DAAED 000.00s Decrypt a TLS 1.3 session with a retry - Decrypt and parse server Alert
Campaign CRC=F90C7E39 in 000.03s SHA=FFB0C12E56D9CAE59298F4287E5AB8843A61AC7A
[31m[1mPASSED=7 FAILED=17[0m
[32m━ Loading: test/tuntap.uts[0m
[34m[1mpassed[0m 2120E469 000.00s Linux-specific protocol headers
[34m[1mpassed[0m FE81D5D6 000.00s Cleanup
Campaign CRC=EB0A8A81 in 000.00s SHA=9F19AFC44A269AC679CCFEEBCBCD141362B726A2
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/scapy/layers/asn1.uts[0m
[34m[1mpassed[0m D95C6143 000.00s short HH
[34m[1mpassed[0m 4E127845 000.00s short HH (invalid)
[34m[1mpassed[0m 11A165F1 000.00s short HHMM
[34m[1mpassed[0m 3DDCEF2A 000.00s short HHMM (invalid)
[34m[1mpassed[0m 10A0D165 000.00s full
[34m[1mpassed[0m BA309686 000.00s full (invalid)
[34m[1mpassed[0m 1F34F644 000.00s with microseconds
[34m[1mpassed[0m E6F47C1D 000.00s with microseconds (invalid)
[34m[1mpassed[0m 97A83935 000.00s Z short HH
[34m[1mpassed[0m 4F42A5D4 000.00s Z short HHMM
[34m[1mpassed[0m 26C55C28 000.00s Z full
[34m[1mpassed[0m 7766A817 000.00s Z with microseconds
[34m[1mpassed[0m 613CB9BD 000.00s offset short HH
[34m[1mpassed[0m 7C82C5EE 000.00s offset short HHMM
[34m[1mpassed[0m 83BBD361 000.00s offset full
[34m[1mpassed[0m 14F5D1B3 000.00s offset with microseconds
[34m[1mpassed[0m 48ABFD3F 000.00s offset negative
[34m[1mpassed[0m 34FCBEF9 000.00s offset invalid (offset >= 24h)
[34m[1mpassed[0m 503D7C59 000.00s UTC short HHMM
[34m[1mpassed[0m 2E838E84 000.00s UTC short HHMM (no Z)
[34m[1mpassed[0m 1D91B1AF 000.00s UTC short HHMM (invalid)
[34m[1mpassed[0m 57E7CF21 000.00s UTC full
[34m[1mpassed[0m 9C4E3B7F 000.00s UTC full (no Z)
[34m[1mpassed[0m 7017A636 000.00s UTC full (invalid)
[34m[1mpassed[0m 3656A400 000.00s prepare
[34m[1mpassed[0m 4FD5C4D9 000.00s short HH datetime
[34m[1mpassed[0m 940DD4D6 000.00s short HHMM datetime
[34m[1mpassed[0m 2EC32DF0 000.00s full datetime
[34m[1mpassed[0m E702C9DB 000.00s datetime assignment
[34m[1mpassed[0m 5842960D 000.00s datetime construction
[34m[1mpassed[0m FA47C6CF 000.00s datetime construction (UTC)
[34m[1mpassed[0m 1D5906A5 000.00s datetime construction (offset)
[34m[1mpassed[0m 0F9574FF 000.00s UTC datetime construction
[34m[1mpassed[0m ED1A0631 000.00s UTC datetime construction (Z)
[34m[1mpassed[0m 92B6E418 000.00s UTC datetime construction (offset)
Campaign CRC=8974D427 in 000.01s SHA=B688DF96C5A71D6A268BE9BF9BE704BF84FFABE1
[34m[1mPASSED=35 FAILED=0[0m
[32m━ Loading: test/scapy/layers/bluetooth.uts[0m
[34m[1mpassed[0m D839BB51 000.02s HCI layers
[34m[1mpassed[0m 34B7B7FD 000.00s Test HCI_PHDR_Hdr
[34m[1mpassed[0m 52821345 000.00s LE Create Connection
[34m[1mpassed[0m 77DF2342 000.00s LE Create Connection Cancel
[34m[1mpassed[0m 8509CB33 000.00s Disconnect
[34m[1mpassed[0m 2D63D45A 000.00s LE Connection Update Command
[34m[1mpassed[0m A1973A92 000.00s LE Connection Update Event
[34m[1mpassed[0m 05B671BB 000.00s Parse EIR_Flags, EIR_CompleteList16BitServiceUUIDs, EIR_CompleteLocalName and EIR_TX_Power_Level
[34m[1mpassed[0m D3CFA490 000.00s Parse EIR_Manufacturer_Specific_Data
[34m[1mpassed[0m 75E9A69D 000.00s Parse EIR_Manufacturer_Specific_Data with magic
[34m[1mpassed[0m D5066B69 000.00s Parse EIR_ServiceData16BitUUID
[34m[1mpassed[0m FAD81431 000.00s Basic L2CAP dissect
[34m[1mpassed[0m E17CFC16 000.00s Basic HCI_ACL_Hdr build & dissect
[34m[1mpassed[0m E06C4A06 000.00s Complex HCI - L2CAP build
[34m[1mpassed[0m 30734F0C 000.00s Complex HCI - L2CAP dissect
[34m[1mpassed[0m A86E9865 000.00s Answers
[34m[1mpassed[0m 6A7A605D 000.00s EIR_Hdr - HCI_LE_Meta_Advertising_Report (single report)
[34m[1mpassed[0m FE8DE930 000.01s EIR_Hdr - HCI_LE_Meta_Advertising_Report (duplicate reports)
[34m[1mpassed[0m 8AE37F5F 000.00s ATT_Hdr - misc
[34m[1mpassed[0m 15EAADC4 000.00s ATT Read_By_Type_Response
[34m[1mpassed[0m 0B7C4E8D 000.00s L2CAP layers
[34m[1mpassed[0m 1B61265D 000.00s SM_Public_Key() tests
[34m[1mpassed[0m 3B7175FE 000.00s SM_DHKey_Check() tests
Campaign CRC=B722F4FD in 000.06s SHA=3FBF06ABDCD159DA244AA24D311848DAA9C2C886
[34m[1mPASSED=23 FAILED=0[0m
[32m━ Loading: test/scapy/layers/bluetooth4LE.uts[0m
[34m[1mpassed[0m 9984EE5A 000.00s Default build
[34m[1mpassed[0m 20EEB610 000.00s Basic dissection
[34m[1mpassed[0m D470A3B4 000.00s BTLE_DATA build
[34m[1mpassed[0m 9ECB5866 000.00s Longer BTLE_ADV
[34m[1mpassed[0m A782E4AD 000.00s BTLE_DATA + EIR_ShortenedLocalName
[34m[1mpassed[0m 5499128D 000.00s LL_CONNECTION_UPDATE_IND
[34m[1mpassed[0m 78F80AEE 000.00s LL_CHANNEL_MAP_IND
[34m[1mpassed[0m A9A5DC61 000.00s LL_TERMINATE_IND
[34m[1mpassed[0m FB368406 000.00s LL_ENC_REQ
[34m[1mpassed[0m 08337861 000.00s LL_ENC_RSP
[34m[1mpassed[0m 48F7FD44 000.00s LL_START_ENC_REQ
[34m[1mpassed[0m 14E88AAC 000.00s LL_START_ENC_RSP
[34m[1mpassed[0m 3D51D732 000.00s LL_UNKNOWN_RSP
[34m[1mpassed[0m 97B66FDC 000.00s LL_FEATURE_REQ
[34m[1mpassed[0m 0E184B84 000.00s LL_FEATURE_RSP
[34m[1mpassed[0m D102B049 000.00s LL_PAUSE_ENC_REQ
[34m[1mpassed[0m 23A5A621 000.00s LL_PAUSE_ENC_RSP
[34m[1mpassed[0m 6485E439 000.00s LL_VERSION_IND
[34m[1mpassed[0m 9BB04ED5 000.00s LL_REJECT_IND
[34m[1mpassed[0m 50577846 000.00s LL_SLAVE_FEATURE_REQ
[34m[1mpassed[0m E47BD306 000.00s LL_CONNECTION_PARAM_REQ
[34m[1mpassed[0m 0740BDA8 000.00s LL_CONNECTION_PARAM_RSP
[34m[1mpassed[0m CDC0A9ED 000.00s LL_REJECT_EXT_IND
[34m[1mpassed[0m FF3A5E4B 000.00s LL_PING_REQ
[34m[1mpassed[0m 0D9D4823 000.00s LL_PING_RSP
[34m[1mpassed[0m 2E009C5A 000.00s LL_LENGTH_REQ
[34m[1mpassed[0m 13EE388C 000.00s LL_LENGTH_RSP
[34m[1mpassed[0m FF72160E 000.00s LL_PHY_REQ
[34m[1mpassed[0m E6D76118 000.00s LL_PHY_RSP
[34m[1mpassed[0m 7A13C253 000.00s LL_PHY_UPDATE_IND
[34m[1mpassed[0m 9AB7FD6C 000.00s BTLE_DATA + BTLE_EMPTY_PDU
[34m[1mpassed[0m A21263DF 000.00s BTLE_DATA + ATT_PrepareWriteReq
[34m[1mpassed[0m F0D2F433 000.00s BTLE layers
[34m[1mpassed[0m 8BF33286 000.00s BTLE_RF link
[34m[1mpassed[0m 9E7FFC52 000.00s DLT_USER0 with PPI
[34m[1mpassed[0m 0F3537E5 000.00s DLT_BLUETOOTH_LE_LL with PPI
[34m[1mpassed[0m 00356CCF 000.00s DLT_BLUETOOTH_LE_LL without PPI
Campaign CRC=92DC5CAA in 000.04s SHA=D1BE662975E12AB675D13D01FCB3E32BD056D9A5
[34m[1mPASSED=37 FAILED=0[0m
[32m━ Loading: test/scapy/layers/can.uts[0m
[34m[1mpassed[0m 337E8646 000.00s Load module
[34m[1mpassed[0m BF15F873 000.00s Build a packet
[34m[1mpassed[0m E055F517 000.00s Dissect & parse
[34m[1mpassed[0m D0813640 000.00s Check flags values
[34m[1mpassed[0m 967F2D9F 000.00s Read PCAP file
[34m[1mpassed[0m C1A6EB8B 000.00s Check if parsing worked: each packet has a CAN layer
[34m[1mpassed[0m E40575B5 000.00s Check if parsing worked: no packet has a Raw or Padding layer
[34m[1mpassed[0m 76311047 000.00s Identifiers
[34m[1mpassed[0m EF39590C 000.00s Flags
[34m[1mpassed[0m BC62DA16 000.00s Data length
[34m[1mpassed[0m 29FDCD48 000.00s read PCAP of a CookedLinux/SocketCAN capture (CAN standard and extended)
[34m[1mpassed[0m DD95CBA8 000.00s check CAN is detected over CookedLinux (each packet has both layers)
[34m[1mpassed[0m E40575B5 000.00s Check if parsing worked: no packet has a Raw or Padding layer
[34m[1mpassed[0m 95A2D6C1 000.00s Check byte swap for dissection
[34m[1mpassed[0m FF99CC4C 000.00s Check byte swap-back for building
[34m[1mpassed[0m A09B1357 000.00s Check building CAN packet with not padded data field
[34m[1mpassed[0m 09C67D30 000.00s Check rdcandump default
[34m[1mpassed[0m 9D56BC7D 000.00s Check rdcandump_iterable default
[34m[1mpassed[0m EFC00941 000.00s Check rdcandump filter
[34m[1mpassed[0m 40FA135E 000.00s interface not log file format
[34m[1mpassed[0m BB9D3F2D 000.00s interface not log file format filtered 1
[34m[1mpassed[0m E2835480 000.00s interface not log file format filtered 2
[34m[1mpassed[0m 23D70CAA 000.00s interface not log file format filtered 2 count 1
[34m[1mpassed[0m E04C11E0 000.00s interface not log file format filtered 2 count 2
[34m[1mpassed[0m 62BD1BB3 000.00s default reading
[34m[1mpassed[0m C35E8CF6 000.00s default reading
[34m[1mpassed[0m 83C56D45 000.00s interface not log file format
[34m[1mpassed[0m D748BFF8 000.00s Test invalid fields_desc
[34m[1mpassed[0m 37ECFE8D 000.00s Test invalid fields_desc with ConditionalField
[34m[1mpassed[0m FBB1EC76 000.01s Motorola byte order (Big Endian) dissect test
[34m[1mpassed[0m 299CE32F 000.00s Motorola byte order (Big Endian) build test
[34m[1mpassed[0m 738149B8 000.01s Motorola byte order (Big Endian) dissect test with mixed field order
[34m[1mpassed[0m 1A9ED9BD 000.01s Motorola byte order (Big Endian) build test with mixed field order
[34m[1mpassed[0m 8C8E3C8A 000.01s Intel byte order (Little Endian) dissect test
[34m[1mpassed[0m 0AB215A0 000.00s Intel byte order (Little Endian) build test
[34m[1mpassed[0m C4E18912 000.01s Intel byte order (Little Endian) build test with mixed field order
[34m[1mpassed[0m 99ADA4DE 000.00s Intel byte order (Little Endian) build test with short package
[34m[1mpassed[0m 090EC7E7 000.00s Packet with mixed endianness fields build test
[34m[1mpassed[0m F41DFA9D 000.00s Muxed Packet with mixed endianness fields build test
[34m[1mpassed[0m 764AE80B 000.00s Muxed Packet build test
[34m[1mpassed[0m 33B8634D 000.00s SignalHeader Muxed Packet build test
[34m[1mpassed[0m FEE5D5D7 000.01s Intel byte order (Little Endian) SignalPacket dissect test
[34m[1mpassed[0m D06AB3A7 000.00s Intel byte order (Little Endian) short SignalPacket dissect test
[34m[1mpassed[0m A97DBA7D 000.00s Intel byte order (Little Endian) short SignalPacket dissect test mixed field order
[34m[1mpassed[0m 090EC7E7 000.00s Packet with mixed endianness fields build test
[34m[1mpassed[0m D856826B 000.00s Packet with mixed endianness fields build test, mixed field order
[34m[1mpassed[0m 155DA1AC 000.00s Packet with mixed endianness fields dissect test, mixed field order
[34m[1mpassed[0m 94ECA0C2 000.00s Packet with mixed endianness fields dissect test, mixed field order and scaling
[34m[1mpassed[0m 94ECA0C2 000.00s Packet with mixed endianness fields dissect test, mixed field order and scaling
[34m[1mpassed[0m 3AA461CB 000.00s Packet with mixed endianness fields dissect test, mixed field order and scaling and offset
[34m[1mpassed[0m AE88B971 000.00s Packet with mixed endianness fields dissect test, mixed field order and scaling and offset
[34m[1mpassed[0m 9B2587C8 000.00s Packet with mixed endianness fields dissect test, mixed field order and scaling with signed values
[34m[1mpassed[0m 45D3C7E8 000.00s Packet with mixed endianness fields dissect test, mixed field order and scaling with signed values
[34m[1mpassed[0m 1D12D05F 000.01s Packet with big endianness signals
[34m[1mpassed[0m 373FF5DF 000.01s Packet with little endianness signals
[34m[1mpassed[0m 47174EEF 000.00s Packet with float signals build test
[34m[1mpassed[0m B142439C 000.00s Packet with float signals dissect test
[34m[1mpassed[0m 2B4A2A85 000.00s Packet with float signals build test 2
[34m[1mpassed[0m B142439C 000.00s Packet with float signals dissect test 2
[34m[1mpassed[0m 66AC128B 000.00s Packet with float signals randval
[34m[1mpassed[0m 5C3B739B 000.00s Packet with float signals fuzz
[34m[1mpassed[0m AF9620A5 000.14s Test signal fuzzing offset 1
[34m[1mpassed[0m BAB8DA21 000.14s Test signal fuzzing offset 2 and scaling
[34m[1mpassed[0m CFF360AC 000.14s Test signal fuzzing offset 3
[34m[1mpassed[0m 1732949E 000.14s Test signal fuzzing offset 4 and scaling
[34m[1mpassed[0m 89FE5A16 000.14s Test signal fuzzing offset 5 and scaling
[34m[1mpassed[0m A9DC7F3D 000.52s Test FloatSignal fuzzing 1
Campaign CRC=4CFB56E0 in 001.33s SHA=AA054253AD6BC2298EC1E564B26584F7CDF2CE4E
[34m[1mPASSED=67 FAILED=0[0m
[32m━ Loading: test/scapy/layers/dhcp.uts[0m
[34m[1mpassed[0m E40548DD 000.00s BOOTP - misc
[34m[1mpassed[0m E3D749AC 000.00s DHCPOptionsField
[34m[1mpassed[0m 3DFDA3FE 000.00s DHCP - build
[34m[1mpassed[0m C67043CC 000.00s DHCP - dissection
[34m[1mpassed[0m B1A86CEC 000.00s DHCPOptions
[31m[1mfailed[0m 6694DB0D 000.00s Check that the dhcpd alias is properly defined and documented
Campaign CRC=FDBC694B in 000.01s SHA=603DFA93D72A649F5C08492802358886F52F0AC9
[31m[1mPASSED=5 FAILED=1[0m
[32m━ Loading: test/scapy/layers/dhcp6.uts[0m
[34m[1mpassed[0m C79D9319 000.00s DUID_LLT basic instantiation
[34m[1mpassed[0m 573F6218 000.00s DUID_LLT basic build
[34m[1mpassed[0m 126A2667 000.00s DUID_LLT build with specific values
[34m[1mpassed[0m 77E99B3D 000.00s DUID_LLT basic dissection
[34m[1mpassed[0m 643AC523 000.00s DUID_LLT dissection with specific values
[34m[1mpassed[0m CF5040FC 000.00s DUID_EN basic instantiation
[34m[1mpassed[0m 69C01E88 000.00s DUID_EN basic build
[34m[1mpassed[0m ACC4AB6F 000.00s DUID_EN build with specific values
[34m[1mpassed[0m 160378C7 000.00s DUID_EN basic dissection
[34m[1mpassed[0m 6582ABBC 000.00s DUID_EN dissection with specific values
[34m[1mpassed[0m B1DCDB18 000.00s DUID_LL basic instantiation
[34m[1mpassed[0m 0A128751 000.00s DUID_LL basic build
[34m[1mpassed[0m FF3E4251 000.00s DUID_LL build with specific values
[34m[1mpassed[0m F3F48399 000.00s DUID_LL basic dissection
[34m[1mpassed[0m 5F3C7367 000.00s DUID_LL with specific values
[34m[1mpassed[0m 47906855 000.00s DUID_UUID basic instantiation
[34m[1mpassed[0m E1F2A3BA 000.00s DUID_UUID basic build
[34m[1mpassed[0m 28EAD2EC 000.00s DUID_UUID build with specific values
[34m[1mpassed[0m 8B0D92F1 000.00s DUID_UUID basic dissection
[34m[1mpassed[0m BBC16669 000.00s DUID_UUID with specific values
[34m[1mpassed[0m 7BAA0C6D 000.00s DHCP6 Opt Unknown basic instantiation
[34m[1mpassed[0m 2B585C11 000.00s DHCP6 Opt Unknown basic build (default values)
[34m[1mpassed[0m 35654E89 000.00s DHCP6 Opt Unknown - len computation test
[34m[1mpassed[0m 362E31B1 000.00s DHCP6OptClientId basic instantiation
[34m[1mpassed[0m FF2048D7 000.00s DHCP6OptClientId basic build
[34m[1mpassed[0m EB8F837C 000.00s DHCP6OptClientId instantiation with specific values
[34m[1mpassed[0m 90E0BE87 000.00s DHCP6OptClientId instantiation with DUID_LL
[34m[1mpassed[0m E251CCE9 000.00s DHCP6OptClientId instantiation with DUID_LLT
[34m[1mpassed[0m EF3404CD 000.00s DHCP6OptClientId instantiation with DUID_EN
[34m[1mpassed[0m 770629E3 000.00s DHCP6OptClientId instantiation with specified length
[34m[1mpassed[0m 4D7691F7 000.00s DHCP6OptClientId basic dissection
[34m[1mpassed[0m 770629E3 000.00s DHCP6OptClientId instantiation with specified length
[34m[1mpassed[0m 4D7691F7 000.00s DHCP6OptClientId basic dissection
[34m[1mpassed[0m 02025171 000.00s DHCP6OptClientId dissection with specific duid value
[34m[1mpassed[0m 4BF9A59A 000.00s DHCP6OptClientId dissection with specific DUID_LL as duid value
[34m[1mpassed[0m 7335375D 000.00s DHCP6OptClientId dissection with specific DUID_LLT as duid value
[34m[1mpassed[0m 96FDC4D3 000.00s DHCP6OptClientId dissection with specific DUID_EN as duid value
[34m[1mpassed[0m 2F43A84F 000.00s DHCP6OptServerId basic instantiation
[34m[1mpassed[0m 4C04F6BC 000.00s DHCP6OptServerId basic build
[34m[1mpassed[0m AD40A748 000.00s DHCP6OptServerId basic build with specific values
[34m[1mpassed[0m C8B4C371 000.00s DHCP6OptServerId instantiation with DUID_LL
[34m[1mpassed[0m B34DB4DA 000.00s DHCP6OptServerId instantiation with DUID_LLT
[34m[1mpassed[0m F24A4510 000.00s DHCP6OptServerId instantiation with DUID_EN
[34m[1mpassed[0m 2ACA0AC9 000.00s DHCP6OptServerId instantiation with specified length
[34m[1mpassed[0m 0E4510ED 000.00s DHCP6OptServerId basic dissection
[34m[1mpassed[0m 25088EF1 000.00s DHCP6OptServerId dissection with specific duid value
[34m[1mpassed[0m FCEA3AAD 000.00s DHCP6OptServerId dissection with specific DUID_LL as duid value
[34m[1mpassed[0m 17596198 000.00s DHCP6OptServerId dissection with specific DUID_LLT as duid value
[34m[1mpassed[0m 02BDF3DF 000.00s DHCP6OptServerId dissection with specific DUID_EN as duid value
[34m[1mpassed[0m 8E5AF373 000.00s DHCP6OptIAAddress - Basic Instantiation
[34m[1mpassed[0m 50C9AB86 000.00s DHCP6OptIAAddress - Basic Dissection
[34m[1mpassed[0m 5C745AE2 000.00s DHCP6OptIAAddress - Instantiation with specific values
[34m[1mpassed[0m 180DE904 000.00s DHCP6OptIAAddress - Instantiation with specific values (default optlen computation)
[34m[1mpassed[0m 5304CAF8 000.00s DHCP6OptIAAddress - Dissection with specific values
[34m[1mpassed[0m 77B71ADD 000.00s DHCP6OptIA_NA - Basic Instantiation
[34m[1mpassed[0m FA5B1DB5 000.00s DHCP6OptIA_NA - Basic Dissection
[34m[1mpassed[0m 124509AF 000.00s DHCP6OptIA_NA - Instantiation with specific values (keep automatic length computation)
[34m[1mpassed[0m 35BE0F11 000.00s DHCP6OptIA_NA - Instantiation with specific values (forced optlen)
[34m[1mpassed[0m 2BF7A72A 000.00s DHCP6OptIA_NA - Instantiation with a list of IA Addresses (optlen automatic computation)
[34m[1mpassed[0m CC90E33C 000.00s DHCP6OptIA_NA - Dissection with specific values
[34m[1mpassed[0m C90EBD9B 000.00s DHCP6OptIA_NA - Instantiation with a list of different opts: IA Address and Status Code (optlen automatic computation)
[34m[1mpassed[0m 2049AD1A 000.00s DHCP6OptIA_TA - Basic Instantiation
[34m[1mpassed[0m 3445CAE0 000.00s DHCP6OptIA_TA - Basic Dissection
[34m[1mpassed[0m C518AC84 000.00s DHCP6OptIA_TA - Instantiation with specific values
[34m[1mpassed[0m 758C776D 000.00s DHCP6OptIA_TA - Dissection with specific values
[34m[1mpassed[0m C5715683 000.00s DHCP6OptIA_TA - Instantiation with a list of different opts: IA Address and Status Code (optlen automatic computation)
[34m[1mpassed[0m 36705FC1 000.00s DHCP6OptOptReq - Basic Instantiation
[34m[1mpassed[0m 74BD65BF 000.00s DHCP6OptOptReq - optlen field computation
[34m[1mpassed[0m 1966E096 000.00s DHCP6OptOptReq - instantiation with empty list
[34m[1mpassed[0m 681B1127 000.00s DHCP6OptOptReq - Basic dissection
[34m[1mpassed[0m 2CEBB2FD 000.00s DHCP6OptOptReq - Dissection with specific value
[34m[1mpassed[0m EF01D128 000.00s DHCP6OptOptReq - repr
[34m[1mpassed[0m 83CD3B19 000.00s DHCP6OptPref - Basic instantiation
[34m[1mpassed[0m 9ABD2F75 000.00s DHCP6OptPref - Instantiation with specific values
[34m[1mpassed[0m A26ADA84 000.00s DHCP6OptPref - Basic Dissection
[34m[1mpassed[0m 5A11B8FB 000.00s DHCP6OptPref - Dissection with specific values
[34m[1mpassed[0m F99BAE27 000.00s DHCP6OptElapsedTime - Basic Instantiation
[34m[1mpassed[0m 3170EBDD 000.00s DHCP6OptElapsedTime - Instantiation with specific elapsedtime value
[34m[1mpassed[0m 01D564C9 000.00s DHCP6OptElapsedTime - Basic Dissection
[34m[1mpassed[0m A0FC2104 000.00s DHCP6OptElapsedTime - Dissection with specific values
[34m[1mpassed[0m EF01D128 000.00s DHCP6OptElapsedTime - Repr
[34m[1mpassed[0m 12093175 000.00s DHCP6OptServerUnicast - Basic Instantiation
[34m[1mpassed[0m B593271B 000.00s DHCP6OptServerUnicast - Instantiation with specific values (test 1)
[34m[1mpassed[0m AB1E0B0E 000.00s DHCP6OptServerUnicast - Instantiation with specific values (test 2)
[34m[1mpassed[0m E68815C3 000.00s DHCP6OptServerUnicast - Dissection with default values
[34m[1mpassed[0m 0A2A1DCB 000.00s DHCP6OptServerUnicast - Dissection with specific values (test 1)
[34m[1mpassed[0m ABCD8B8B 000.00s DHCP6OptServerUnicast - Dissection with specific values (test 2)
[34m[1mpassed[0m 483BB9D5 000.00s DHCP6OptStatusCode - Basic Instantiation
[34m[1mpassed[0m 59E4DBFE 000.00s DHCP6OptStatusCode - Instantiation with specific values
[34m[1mpassed[0m C973546A 000.00s DHCP6OptStatusCode - Automatic Length computation
[34m[1mpassed[0m C12FEA58 000.00s DHCP6OptRapidCommit - Basic Instantiation
[34m[1mpassed[0m 89359BEA 000.00s DHCP6OptRapidCommit - Basic Dissection
[34m[1mpassed[0m 21E9E578 000.00s DHCP6OptUserClass - Basic Instantiation
[34m[1mpassed[0m C728FB45 000.00s DHCP6OptUserClass - Basic Dissection
[34m[1mpassed[0m 4FFE3CEC 000.00s DHCP6OptUserClass - Instantiation with one user class data rawucture
[34m[1mpassed[0m 1397460A 000.00s DHCP6OptUserClass - Dissection with one user class data rawucture
[34m[1mpassed[0m 57A1E3CB 000.00s DHCP6OptUserClass - Instantiation with two user class data rawuctures
[34m[1mpassed[0m 1841DC70 000.00s DHCP6OptUserClass - Dissection with two user class data rawuctures
[34m[1mpassed[0m 42297BF6 000.00s DHCP6OptVendorClass - Basic Instantiation
[34m[1mpassed[0m 4CE36928 000.00s DHCP6OptVendorClass - Basic Dissection
[34m[1mpassed[0m 9B354873 000.00s DHCP6OptVendorClass - Instantiation with one vendor class data rawucture
[34m[1mpassed[0m 469486B5 000.00s DHCP6OptVendorClass - Dissection with one vendor class data rawucture
[34m[1mpassed[0m C023DF29 000.00s DHCP6OptVendorClass - Instantiation with two vendor class data rawuctures
[34m[1mpassed[0m 1D2D4C13 000.00s DHCP6OptVendorClass - Dissection with two vendor class data rawuctures
[34m[1mpassed[0m 6E1B3AF2 000.00s DHCP6OptVendorSpecificInfo - Basic Instantiation
[34m[1mpassed[0m C428A8A6 000.00s DHCP6OptVendorSpecificInfo - Basic Dissection
[34m[1mpassed[0m F67D2ACA 000.00s DHCP6OptVendorSpecificInfo - Instantiation with specific values (one option)
[34m[1mpassed[0m F5159739 000.00s DHCP6OptVendorSpecificInfo - Dissection with with specific values (one option)
[34m[1mpassed[0m 3BD3252A 000.00s DHCP6OptVendorSpecificInfo - Instantiation with specific values (two options)
[34m[1mpassed[0m D85C1FDC 000.00s DHCP6OptVendorSpecificInfo - Dissection with with specific values (two options)
[34m[1mpassed[0m AE0C4328 000.00s DHCP6OptIfaceId - Basic Instantiation
[34m[1mpassed[0m 54DD9335 000.00s DHCP6OptIfaceId - Basic Dissection
[34m[1mpassed[0m 9500371E 000.00s DHCP6OptIfaceId - Instantiation with specific value
[34m[1mpassed[0m 692CCF89 000.00s DHCP6OptIfaceId - Dissection with specific value
[34m[1mpassed[0m FE4BFB1C 000.00s DHCP6OptReconfMsg - Basic Instantiation
[34m[1mpassed[0m 97DE5AA0 000.00s DHCP6OptReconfMsg - Basic Dissection
[34m[1mpassed[0m 63C038DE 000.00s DHCP6OptReconfMsg - Instantiation with specific values
[34m[1mpassed[0m 223A58FB 000.00s DHCP6OptReconfMsg - Dissection with specific values
[34m[1mpassed[0m 7FE87B62 000.00s DHCP6OptReconfAccept - Basic Instantiation
[34m[1mpassed[0m CCE32A09 000.00s DHCP6OptReconfAccept - Basic Dissection
[34m[1mpassed[0m 6884B85A 000.00s DHCP6OptReconfAccept - Instantiation with specific values
[34m[1mpassed[0m 7E254112 000.00s DHCP6OptReconfAccept - Dssection with specific values
[34m[1mpassed[0m 6A0FEC94 000.00s DHCP6OptSIPDomains - Basic Instantiation
[34m[1mpassed[0m 5C613FC4 000.00s DHCP6OptSIPDomains - Basic Dissection
[34m[1mpassed[0m 222818B4 000.00s DHCP6OptSIPDomains - Instantiation with one domain
[34m[1mpassed[0m 1A45951B 000.00s DHCP6OptSIPDomains - Dissection with one domain
[34m[1mpassed[0m 1B52FA95 000.00s DHCP6OptSIPDomains - Instantiation with two domains
[34m[1mpassed[0m F9C93597 000.00s DHCP6OptSIPDomains - Dissection with two domains
[34m[1mpassed[0m AF257E77 000.00s DHCP6OptSIPDomains - Enforcing only one dot at end of domain
[34m[1mpassed[0m 9E523117 000.00s DHCP6OptSIPServers - Basic Instantiation
[34m[1mpassed[0m 759AFEC2 000.00s DHCP6OptSIPServers - Basic Dissection
[34m[1mpassed[0m EF893C3F 000.00s DHCP6OptSIPServers - Instantiation with specific values (1 address)
[34m[1mpassed[0m 8F637FA2 000.00s DHCP6OptSIPServers - Dissection with specific values (1 address)
[34m[1mpassed[0m 63D24C8F 000.00s DHCP6OptSIPServers - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m CDDCF6B2 000.00s DHCP6OptSIPServers - Dissection with specific values (2 addresses)
[34m[1mpassed[0m A2AE85FD 000.00s DHCP6OptDNSServers - Basic Instantiation
[34m[1mpassed[0m 58D8E580 000.00s DHCP6OptDNSServers - Basic Dissection
[34m[1mpassed[0m A9444EC5 000.00s DHCP6OptDNSServers - Instantiation with specific values (1 address)
[34m[1mpassed[0m BC746583 000.00s DHCP6OptDNSServers - Dissection with specific values (1 address)
[34m[1mpassed[0m ED35320B 000.00s DHCP6OptDNSServers - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m 952E3E66 000.00s DHCP6OptDNSServers - Dissection with specific values (2 addresses)
[34m[1mpassed[0m 4CCFB8F0 000.00s DHCP6OptDNSDomains - Basic Instantiation
[34m[1mpassed[0m E1F53152 000.00s DHCP6OptDNSDomains - Basic Dissection
[34m[1mpassed[0m 17CB7DD8 000.00s DHCP6OptDNSDomains - Instantiation with specific values (1 domain)
[34m[1mpassed[0m 5535AD9E 000.00s DHCP6OptDNSDomains - Dissection with specific values (1 domain)
[34m[1mpassed[0m 4AD4CE63 000.00s DHCP6OptDNSDomains - Instantiation with specific values (2 domains)
[34m[1mpassed[0m 9FB29EBC 000.00s DHCP6OptDNSDomains - Dissection with specific values (2 domains)
[34m[1mpassed[0m 6FC64603 000.00s DHCP6OptIAPrefix - Basic Instantiation
[34m[1mpassed[0m 8BC01797 000.00s DHCP6OptIAPrefix - Basic Dissection
[34m[1mpassed[0m 890662B7 000.00s DHCP6OptIAPrefix - Instantiation with specific values
[34m[1mpassed[0m 3CA899EB 000.00s DHCP6OptIAPrefix - Instantiation with specific values (default optlen computation)
[34m[1mpassed[0m 7F436536 000.00s DHCP6OptIAPrefix - Dissection with specific values
[34m[1mpassed[0m B851ABE7 000.00s DHCP6OptIA_PD - Basic Instantiation
[34m[1mpassed[0m 1ED94E0C 000.00s DHCP6OptIA_PD - Basic Dissection
[34m[1mpassed[0m 8CE67D52 000.00s DHCP6OptIA_PD - Instantiation with specific values (keep automatic length computation)
[34m[1mpassed[0m 67D8D9BC 000.00s DHCP6OptIA_PD - Instantiation with specific values (forced optlen)
[34m[1mpassed[0m 4065D7F8 000.00s DHCP6OptIA_PD - Instantiation with a list of IA Prefixes (optlen automatic computation)
[34m[1mpassed[0m 1D7BEA97 000.00s DHCP6OptIA_PD - Dissection with specific values
[34m[1mpassed[0m B4D0102A 000.00s DHCP6OptIA_PD - Instantiation with a list of different opts: IA Prefix and Status Code (optlen automatic computation)
[34m[1mpassed[0m 7FEABB0F 000.00s DHCP6OptNISServers - Basic Instantiation
[34m[1mpassed[0m 2D3E55AB 000.00s DHCP6OptNISServers - Basic Dissection
[34m[1mpassed[0m 8A415BEB 000.00s DHCP6OptNISServers - Instantiation with specific values (1 address)
[34m[1mpassed[0m A2FEE027 000.00s DHCP6OptNISServers - Dissection with specific values (1 address)
[34m[1mpassed[0m 7219CF98 000.00s DHCP6OptNISServers - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m 7F300088 000.00s DHCP6OptNISServers - Dissection with specific values (2 addresses)
[34m[1mpassed[0m 9F10D357 000.00s DHCP6OptNISPServers - Basic Instantiation
[34m[1mpassed[0m 7C52E80C 000.00s DHCP6OptNISPServers - Basic Dissection
[34m[1mpassed[0m DB9FD9BA 000.00s DHCP6OptNISPServers - Instantiation with specific values (1 address)
[34m[1mpassed[0m 132B557E 000.00s DHCP6OptNISPServers - Dissection with specific values (1 address)
[34m[1mpassed[0m 0B2A759C 000.00s DHCP6OptNISPServers - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m 0B95A772 000.00s DHCP6OptNISPServers - Dissection with specific values (2 addresses)
[34m[1mpassed[0m 35E92EE5 000.00s DHCP6OptNISDomain - Basic Instantiation
[34m[1mpassed[0m FC357773 000.00s DHCP6OptNISDomain - Basic Dissection
[34m[1mpassed[0m 771D2456 000.00s DHCP6OptNISDomain - Instantiation with one domain name
[34m[1mpassed[0m B60B8275 000.00s DHCP6OptNISDomain - Dissection with one domain name
[34m[1mpassed[0m E3058EF2 000.00s DHCP6OptNISDomain - Instantiation with one domain with trailing dot
[34m[1mpassed[0m E7939353 000.00s DHCP6OptNISPDomain - Basic Instantiation
[34m[1mpassed[0m EEDA00A7 000.00s DHCP6OptNISPDomain - Basic Dissection
[34m[1mpassed[0m 83274083 000.00s DHCP6OptNISPDomain - Instantiation with one domain name
[34m[1mpassed[0m 2E63DD48 000.00s DHCP6OptNISPDomain - Dissection with one domain name
[34m[1mpassed[0m 521B902B 000.00s DHCP6OptNISPDomain - Instantiation with one domain with trailing dot
[34m[1mpassed[0m 76F9E6A2 000.00s DHCP6OptSNTPServers - Basic Instantiation
[34m[1mpassed[0m A82BAC3C 000.00s DHCP6OptSNTPServers - Basic Dissection
[34m[1mpassed[0m C6B08BC2 000.00s DHCP6OptSNTPServers - Instantiation with specific values (1 address)
[34m[1mpassed[0m 1DA0E113 000.00s DHCP6OptSNTPServers - Dissection with specific values (1 address)
[34m[1mpassed[0m E6063C82 000.00s DHCP6OptSNTPServers - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m 1A9361CE 000.00s DHCP6OptSNTPServers - Dissection with specific values (2 addresses)
[34m[1mpassed[0m 32E1CE95 000.00s DHCP6OptInfoRefreshTime - Basic Instantiation
[34m[1mpassed[0m DB05D6F2 000.00s DHCP6OptInfoRefreshTime - Basic Dissction
[34m[1mpassed[0m 0C267524 000.00s DHCP6OptInfoRefreshTime - Instantiation with specific values
[34m[1mpassed[0m 4B176846 000.00s DHCP6OptBCMCSServers - Basic Instantiation
[34m[1mpassed[0m DB90931E 000.00s DHCP6OptBCMCSServers - Basic Dissection
[34m[1mpassed[0m D169C53A 000.00s DHCP6OptBCMCSServers - Instantiation with specific values (1 address)
[34m[1mpassed[0m 5E8A233D 000.00s DHCP6OptBCMCSServers - Dissection with specific values (1 address)
[34m[1mpassed[0m 8C4433DB 000.00s DHCP6OptBCMCSServers - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m B47B1DC0 000.00s DHCP6OptBCMCSServers - Dissection with specific values (2 addresses)
[34m[1mpassed[0m 6379536D 000.00s DHCP6OptBCMCSDomains - Basic Instantiation
[34m[1mpassed[0m E3180DCC 000.00s DHCP6OptBCMCSDomains - Basic Dissection
[34m[1mpassed[0m 3F135354 000.00s DHCP6OptBCMCSDomains - Instantiation with specific values (1 domain)
[34m[1mpassed[0m FF72EB2B 000.00s DHCP6OptBCMCSDomains - Dissection with specific values (1 domain)
[34m[1mpassed[0m 6D92A894 000.00s DHCP6OptBCMCSDomains - Instantiation with specific values (2 domains)
[34m[1mpassed[0m 477EE63F 000.00s DHCP6OptBCMCSDomains - Dissection with specific values (2 domains)
[34m[1mpassed[0m 8C71EC2F 000.00s DHCP6OptRemoteID - Basic Instantiation
[34m[1mpassed[0m 6B9A6137 000.00s DHCP6OptRemoteID - Basic Dissection
[34m[1mpassed[0m B03424CE 000.00s DHCP6OptRemoteID - Instantiation with specific values
[34m[1mpassed[0m D46CC6A3 000.00s DHCP6OptRemoteID - Dissection with specific values
[34m[1mpassed[0m DCD7B680 000.00s DHCP6OptSubscriberID - Basic Instantiation
[34m[1mpassed[0m 139DE428 000.00s DHCP6OptSubscriberID - Basic Dissection
[34m[1mpassed[0m CD2EC53A 000.00s DHCP6OptSubscriberID - Instantiation with specific values
[34m[1mpassed[0m A13CA093 000.00s DHCP6OptSubscriberID - Dissection with specific values
[34m[1mpassed[0m 3F74488E 000.00s DHCP6OptClientFQDN - Basic Instantiation
[34m[1mpassed[0m A84B7210 000.00s DHCP6OptClientFQDN - Basic Dissection
[34m[1mpassed[0m FDF061CC 000.00s DHCP6OptClientFQDN - Instantiation with various flags combinations
[34m[1mpassed[0m 1787A293 000.00s DHCP6OptClientFQDN - Instantiation with one fqdn
[34m[1mpassed[0m 3E86FB9D 000.00s DHCP6OptClientFQDN - Dissection with one fqdn
[34m[1mpassed[0m 6E81346C 000.00s DHCP6OptPanaAuthAgent - Basic Instantiation
[34m[1mpassed[0m 66B70519 000.00s DHCP6OptPanaAuthAgent - Basic Dissection
[34m[1mpassed[0m 270758CB 000.00s DHCP6OptPanaAuthAgent - Instantiation with specific values (1 address)
[34m[1mpassed[0m E7473B76 000.00s DHCP6OptPanaAuthAgent - Dissection with specific values (1 address)
[34m[1mpassed[0m EECF4952 000.00s DHCP6OptPanaAuthAgent - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m 49DD3BD5 000.00s DHCP6OptPanaAuthAgent - Dissection with specific values (2 addresses)
[34m[1mpassed[0m 83EC1F66 000.00s DHCP6OptNewPOSIXTimeZone - Basic Instantiation
[34m[1mpassed[0m 1A01D8C2 000.00s DHCP6OptNewPOSIXTimeZone - Basic Dissection
[34m[1mpassed[0m 32525614 000.00s DHCP6OptNewPOSIXTimeZone - Instantiation with specific values
[34m[1mpassed[0m B3E5F651 000.00s DHCP6OptNewPOSIXTimeZone - Dissection with specific values
[34m[1mpassed[0m F16DE64E 000.00s DHCP6OptNewTZDBTimeZone - Basic Instantiation
[34m[1mpassed[0m 35770912 000.00s DHCP6OptNewTZDBTimeZone - Basic Dissection
[34m[1mpassed[0m 91CBB7C3 000.00s DHCP6OptNewTZDBTimeZone - Instantiation with specific values
[34m[1mpassed[0m 68A1BDD3 000.00s DHCP6OptNewTZDBTimeZone - Dissection with specific values
[34m[1mpassed[0m C1BBFC50 000.00s DHCP6OptRelayAgentERO - Basic Instantiation
[34m[1mpassed[0m D87CE796 000.00s DHCP6OptRelayAgentERO - optlen field computation
[34m[1mpassed[0m 55C856B2 000.00s DHCP6OptRelayAgentERO - instantiation with empty list
[34m[1mpassed[0m 05BA5C72 000.00s DHCP6OptRelayAgentERO - Basic dissection
[34m[1mpassed[0m 5B368CD2 000.00s DHCP6OptRelayAgentERO - Dissection with specific value
[34m[1mpassed[0m 3B63A4EA 000.00s DHCP6OptLQClientLink - Basic Instantiation
[34m[1mpassed[0m A8B0154E 000.00s DHCP6OptLQClientLink - Basic Dissection
[34m[1mpassed[0m 2549610B 000.00s DHCP6OptLQClientLink - Instantiation with specific values (1 address)
[34m[1mpassed[0m EBE32745 000.00s DHCP6OptLQClientLink - Dissection with specific values (1 address)
[34m[1mpassed[0m 8B1EA20B 000.00s DHCP6OptLQClientLink - Instantiation with specific values (2 addresses)
[34m[1mpassed[0m A29C5ADB 000.00s DHCP6OptLQClientLink - Dissection with specific values (2 addresses)
[34m[1mpassed[0m BBC77F5A 000.00s DHCP6OptBootFileUrl - Basic Instantiation
[34m[1mpassed[0m BFB16E14 000.00s DHCP6OptBootFileUrl - Basic Dissection
[34m[1mpassed[0m B7F7EE32 000.00s DHCP6OptBootFileUrl - Instantiation with specific values
[34m[1mpassed[0m 26B38B0D 000.00s DHCP6OptBootFileUrl - Dissection with specific values
[34m[1mpassed[0m 76E07503 000.00s DHCP6OptClientArchType - Basic Instantiation
[34m[1mpassed[0m D35B9876 000.00s DHCP6OptClientArchType - Basic Dissection
[34m[1mpassed[0m 62F5E414 000.00s DHCP6OptClientArchType - Instantiation with specific value as just int
[34m[1mpassed[0m 5D2F43DD 000.00s DHCP6OptClientArchType - Instantiation with specific value as single item list of int
[34m[1mpassed[0m B12768B0 000.00s DHCP6OptClientArchType - Dissection with specific 1 value list
[34m[1mpassed[0m C97B6CE1 000.00s DHCP6OptClientArchType - Instantiation with specific value as 2 item list of int
[34m[1mpassed[0m C5832B1C 000.00s DHCP6OptClientArchType - Dissection with specific 2 values list
[34m[1mpassed[0m ADEB6593 000.00s DHCP6OptClientNetworkInterId - Basic Instantiation
[34m[1mpassed[0m B7D0A9A5 000.00s DHCP6OptClientNetworkInterId - Basic Dissection
[34m[1mpassed[0m A598FE2F 000.00s DHCP6OptClientNetworkInterId - Instantiation with specific values
[34m[1mpassed[0m 3D6C910C 000.00s DHCP6OptClientNetworkInterId - Dissection with specific values
[34m[1mpassed[0m BDDB4B3E 000.00s DHCP6OptERPDomain - Basic Instantiation
[34m[1mpassed[0m 1475A5B4 000.00s DHCP6OptERPDomain - Basic Dissection
[34m[1mpassed[0m 39AAB580 000.00s DHCP6OptERPDomain - Instantiation with specific values (1 domain)
[34m[1mpassed[0m E591D50C 000.00s DHCP6OptERPDomain - Dissection with specific values (1 domain)
[34m[1mpassed[0m 79350BF2 000.00s DHCP6OptERPDomain - Instantiation with specific values (2 domains)
[34m[1mpassed[0m 50E6BDC7 000.00s DHCP6OptERPDomain - Dissection with specific values (2 domains)
[34m[1mpassed[0m 7F12A31A 000.00s DHCP6OptRelaySuppliedOpt - Basic Instantiation
[34m[1mpassed[0m BB870D4D 000.00s DHCP6OptRelaySuppliedOpt - Basic Dissection
[34m[1mpassed[0m 9D40CF7E 000.00s DHCP6OptRelaySuppliedOpt - Instantiation with specific values
[34m[1mpassed[0m EDA0BF0C 000.00s DHCP6OptRelaySuppliedOpt - Dissection with specific values
[34m[1mpassed[0m 97778832 000.00s Basic build & dissect
[34m[1mpassed[0m 222CB7F5 000.00s Basic build & dissect
[34m[1mpassed[0m 4BCBEFEE 000.00s Basic build & dissect
[34m[1mpassed[0m 05ECD4D8 000.00s DHCP6_Solicit - Basic Instantiation
[34m[1mpassed[0m ACA2C22D 000.00s DHCP6_Solicit - Basic Dissection
[34m[1mpassed[0m B2FBFD0B 000.00s DHCP6_Solicit - Basic test of DHCP6_solicit.hashret()
[34m[1mpassed[0m 78A6A805 000.00s DHCP6_Solicit - Test of DHCP6_solicit.hashret() with specific values
[34m[1mpassed[0m 4037380B 000.00s DHCP6_Solicit - UDP ports overload
[34m[1mpassed[0m BEA9393A 000.00s DHCP6_Solicit - Dispatch based on UDP port
[34m[1mpassed[0m 49F7AC73 000.00s DHCP6_Advertise - Basic Instantiation
[34m[1mpassed[0m BA6768A7 000.00s DHCP6_Advertise - Basic test of DHCP6_solicit.hashret()
[34m[1mpassed[0m C5AEA977 000.00s DHCP6_Advertise - Test of DHCP6_Advertise.hashret() with specific values
[34m[1mpassed[0m DBEE0DCC 000.00s DHCP6_Advertise - Basic test of answers() with solicit message
[34m[1mpassed[0m F7C12A80 000.00s DHCP6_Advertise - Test of answers() with solicit message
[34m[1mpassed[0m 5A5E5880 000.00s DHCP6_Advertise - UDP ports overload
[34m[1mpassed[0m 987B8472 000.00s DHCP6_Request - Basic Instantiation
[34m[1mpassed[0m D7F0076D 000.00s DHCP6_Request - Basic Dissection
[34m[1mpassed[0m FE7E857E 000.00s DHCP6_Request - UDP ports overload
[34m[1mpassed[0m 4698F0F7 000.00s DHCP6_Confirm - Basic Instantiation
[34m[1mpassed[0m B145C8FA 000.00s DHCP6_Confirm - Basic Dissection
[34m[1mpassed[0m 94A6B80F 000.00s DHCP6_Confirm - UDP ports overload
[34m[1mpassed[0m 1BCB0635 000.00s DHCP6_Renew - Basic Instantiation
[34m[1mpassed[0m 8CD9AFA1 000.00s DHCP6_Renew - Basic Dissection
[34m[1mpassed[0m CD9AC729 000.00s DHCP6_Renew - UDP ports overload
[34m[1mpassed[0m A4C424A0 000.00s DHCP6_Rebind - Basic Instantiation
[34m[1mpassed[0m 3978B36A 000.00s DHCP6_Rebind - Basic Dissection
[34m[1mpassed[0m 2A50EFE4 000.00s DHCP6_Rebind - UDP ports overload
[34m[1mpassed[0m 3111C41E 000.00s DHCP6_Reply - Basic Instantiation
[34m[1mpassed[0m 7CB6CA69 000.00s DHCP6_Reply - Basic Dissection
[34m[1mpassed[0m DB5DDF19 000.00s DHCP6_Reply - UDP ports overload
[34m[1mpassed[0m C7904878 000.00s DHCP6_Reply - Answers
[34m[1mpassed[0m 6C00D155 000.00s DHCP6_Release - Basic Instantiation
[34m[1mpassed[0m 30BC1D29 000.00s DHCP6_Release - Basic Dissection
[34m[1mpassed[0m 80229F74 000.00s DHCP6_Release - UDP ports overload
[34m[1mpassed[0m 7A3B85FE 000.00s DHCP6_Decline - Basic Instantiation
[34m[1mpassed[0m B0CB486C 000.00s DHCP6_Confirm - Basic Dissection
[34m[1mpassed[0m A3A8FDD0 000.00s DHCP6_Decline - UDP ports overload
[34m[1mpassed[0m 5B7F3836 000.00s DHCP6_Reconf - Basic Instantiation
[34m[1mpassed[0m 81C7B54D 000.00s DHCP6_Reconf - Basic Dissection
[34m[1mpassed[0m 31A261BB 000.00s DHCP6_Reconf - UDP ports overload
[34m[1mpassed[0m 3373BDBE 000.00s DHCP6_InfoRequest - Basic Instantiation
[34m[1mpassed[0m 547C2E0D 000.00s DHCP6_InfoRequest - Basic Dissection
[34m[1mpassed[0m 9DD90FD6 000.00s DHCP6_InfoRequest - UDP ports overload
[34m[1mpassed[0m 2C4775D8 000.00s DHCP6_RelayForward - Basic Instantiation
[34m[1mpassed[0m 18D6F270 000.00s DHCP6_RelayForward - Basic Dissection
[34m[1mpassed[0m 897EEC87 000.00s DHCP6_RelayForward - Dissection with options
[34m[1mpassed[0m DB68DA15 000.00s DHCP6_RelayForward - Advanced dissection
[34m[1mpassed[0m 9508CE5B 000.00s DHCP6OptRelayMsg - Basic Instantiation
[34m[1mpassed[0m 5CC7ECC6 000.00s DHCP6OptRelayMsg - Basic Dissection
[34m[1mpassed[0m F14D078C 000.00s DHCP6OptRelayMsg - Embedded DHCP6 packet Instantiation
[34m[1mpassed[0m 0ACE3538 000.00s DHCP6OptRelayMsg - Embedded DHCP6 packet Dissection
[34m[1mpassed[0m 3B907575 000.00s DHCP6_RelayReply - Basic Instantiation
[34m[1mpassed[0m 607A1E6F 000.00s DHCP6_RelayReply - Basic Dissection
Campaign CRC=5A338202 in 000.10s SHA=60758BFE03F41A681471482066C5BD036B8C89C9
[34m[1mPASSED=318 FAILED=0[0m
[32m━ Loading: test/scapy/layers/dns.uts[0m
[34m[1mpassed[0m 28F440C5 000.00s DNS frame with advanced decompression
[34m[1mpassed[0m C7DDC889 000.00s DNS frame with DNSRRSRV
[34m[1mpassed[0m 16D6B2CC 000.00s DNS frame with decompression hidden args
[34m[1mpassed[0m A78542A3 000.00s DNS advanced building
[34m[1mpassed[0m 281A63F6 000.00s Basic DNS Compression
[34m[1mpassed[0m 5A52CC30 000.00s DNS frames with MX records
[34m[1mpassed[0m 707BC022 000.00s Advanced dns_get_str tests
[34m[1mpassed[0m 6CA1C298 000.00s Decompression loop in dns_get_str
[34m[1mpassed[0m A69B8918 000.00s Prematured end in dns_get_str
[34m[1mpassed[0m BC4423C3 000.00s Other decompression loop in dns_get_str
[34m[1mpassed[0m D57780E2 000.00s DNS record type 16 (TXT)
[34m[1mpassed[0m F02E5A0B 000.00s DNS - Malformed DNS over TCP message
[34m[1mpassed[0m 2D906D1D 000.00s DNS - dns_compress on decompressed packet
[34m[1mpassed[0m 99A86BAD 000.00s DNS - dns_compress on close indexes
[34m[1mpassed[0m 7B48D445 000.00s DNS - dns_encode edge cases
[34m[1mpassed[0m 6683AEB1 000.00s DNS - simple request
[34m[1mpassed[0m 7A9B6C2B 000.00s DNS - preserve rdlen when rdata is not a compressed DNS string
Campaign CRC=0F763BE0 in 000.03s SHA=51FFFE32D7918CDAFBB0D4F03588B7E1229589FC
[34m[1mPASSED=17 FAILED=0[0m
[32m━ Loading: test/scapy/layers/dns_dnssec.uts[0m
[34m[1mpassed[0m 01F134E9 000.00s example from RFC 4034
[34m[1mpassed[0m 95B7A220 000.00s [0]
[34m[1mpassed[0m 7AF543C7 000.00s [0,1,2,3,4,5,6,7]
[34m[1mpassed[0m E6640B6D 000.00s [256,512,4096,36864]
[34m[1mpassed[0m A63AF85B 000.00s [65535]
[34m[1mpassed[0m D0647AEE 000.00s example from RFC 4034
[34m[1mpassed[0m 0818D1B5 000.00s [0]
[34m[1mpassed[0m 6B6F484A 000.00s [0,1,2,3,4,5,6,7]
[34m[1mpassed[0m C34A7B08 000.00s [256,512,4096,36864]
[34m[1mpassed[0m BEACAC75 000.00s [65535]
[34m[1mpassed[0m EB8F00DF 000.00s DNSRRNSEC(), basic instantiation
[34m[1mpassed[0m 85F328F1 000.00s DNSRRRNSEC(), check parameters
[34m[1mpassed[0m 06D8E113 000.00s DNSRRNSEC3(), basic instantiation
[34m[1mpassed[0m 83835EFE 000.00s DNSRRRNSEC3(), check parameters
[34m[1mpassed[0m AB7DB468 000.00s DNSRRNSEC3PARAM(), basic instantiation
[34m[1mpassed[0m 7A5BA656 000.00s DNSRRRNSEC3PARAM(), check parameters
[34m[1mpassed[0m 79BF520A 000.00s DNSRRRSIG(), basic instantiation
[34m[1mpassed[0m B328C932 000.00s DNSRRRSIG(), check parameters
[34m[1mpassed[0m E86741B7 000.00s DNSRRRSIG(), dissection
[34m[1mpassed[0m 98DDC0CB 000.00s DNSRRDNSKEY(), basic instantiation
[34m[1mpassed[0m CBB44857 000.00s DNSRRDNSKEY(), check parameters
[34m[1mpassed[0m EEE416B6 000.00s DNSRRDNSKEY(), dissection
[34m[1mpassed[0m 2CF66A6D 000.00s DNSRRDS() and DNSRRDLV(), basic instancaition
[34m[1mpassed[0m CCA6DC1B 000.00s DNSRRDS(), check parameters
[34m[1mpassed[0m B94145A9 000.00s DNSRR(type="TXT") instantiation
[34m[1mpassed[0m E22D54A9 000.00s Build DNSRR
[34m[1mpassed[0m 4B145851 000.00s DNSRRR(), check parameters
[34m[1mpassed[0m 176E770E 000.00s DNSRRTSIG basic instantiation
[34m[1mpassed[0m 5730FB06 000.00s DNSRRTSIG(), check parameters
[34m[1mpassed[0m D16A5BDB 000.00s TimeField methods
Campaign CRC=054C888B in 000.01s SHA=315E5F8577E5D388EC0F05188B17D262AC4322B4
[34m[1mPASSED=30 FAILED=0[0m
[32m━ Loading: test/scapy/layers/dns_edns0.uts[0m
[34m[1mpassed[0m 41DCEAAC 000.00s EDNS0TLV(), basic instantiation
[34m[1mpassed[0m 1715585A 000.00s EDNS0TLV(), check parameters
[34m[1mpassed[0m 4D78447D 000.00s EDNS0TLV(), check computed optlen
[34m[1mpassed[0m 50A50DC2 000.00s EDNS0TLV(), dissection
[34m[1mpassed[0m 5F5E2642 000.00s DNSRROPT(), basic instantiation
[34m[1mpassed[0m 89FFB862 000.00s DNSRROPT(), check parameters
[34m[1mpassed[0m 8FBAF2A9 000.00s DNSRROPT() & EDN0TLV(), check parameters
[34m[1mpassed[0m 2BAF6684 000.00s DNSRROP(), dissection
[34m[1mpassed[0m A11CE60B 000.00s EDNS-PING - basic instantiation
[34m[1mpassed[0m A378306E 000.00s NSID- basic instantiation
Campaign CRC=7EA9C4CC in 000.00s SHA=2B415DDA2E3539CC75A325B567DE66B733E1FA4D
[34m[1mPASSED=10 FAILED=0[0m
[32m━ Loading: test/scapy/layers/dot11.uts[0m
[34m[1mpassed[0m 7232562B 000.00s 802.11 - misc
[34m[1mpassed[0m 5C51DE63 000.00s Dot11 - build
[34m[1mpassed[0m 4E6E6642 000.00s Dot11 - dissection
[34m[1mpassed[0m 92B10465 000.00s Dot11QoS - build
[34m[1mpassed[0m F133DC56 000.00s Dot11 - binary in SSID
[34m[1mpassed[0m C9A318DA 000.00s Dot11QoS - dissection
[34m[1mpassed[0m 899846BF 000.00s Dot11 - answers
[34m[1mpassed[0m 8C5E89D2 000.00s Dot11 - misc
[34m[1mpassed[0m 76EE9F2C 000.00s Multiple Dot11Elt layers
[31m[1mfailed[0m CB43C4CC 000.00s Dot11WEP - build
[34m[1mpassed[0m A30D532E 000.00s Dot11WEP - dissect
[34m[1mpassed[0m 331B5870 000.00s Dot11TKIP - dissection
[34m[1mpassed[0m C580C6A2 000.00s Dot11CCMP - dissection
[34m[1mpassed[0m 9E2EC45F 000.00s Dot11 - answers
[34m[1mpassed[0m 727C1186 000.00s Dot11Beacon network_stats()
[34m[1mpassed[0m 686ABE35 000.01s Dot11EltCountry dissection
[34m[1mpassed[0m 257388B5 000.00s RSNCipherSuite
[34m[1mpassed[0m DF857CAD 000.00s AKMSuite
[34m[1mpassed[0m AB60021B 000.00s PMKIDListPacket
[34m[1mpassed[0m 15C94D9C 000.01s Dot11EltRSN
[34m[1mpassed[0m B5747628 000.00s Dot11EltMicrosoftWPA
[34m[1mpassed[0m 0AAD6CC4 000.00s Dot11EltVendorSpecific
[34m[1mpassed[0m 1B4BA993 000.00s Beacon with RSN IE
[34m[1mpassed[0m 6629BBA9 000.00s Beacon with Microsoft WPA IE
[34m[1mpassed[0m CED7778E 000.00s HT Capabilities
[34m[1mpassed[0m 1D067C5A 000.00s HT Capabilities with fuzzed values
[34m[1mpassed[0m 0C2D8919 000.00s RadioTap - MCS weird padding
[34m[1mpassed[0m EC25B047 000.00s RadioTap MCS
[34m[1mpassed[0m 6699C361 000.00s Reassociation request
[34m[1mpassed[0m 39BC1BA4 000.00s Backward compatibility of Dot11Elt
[34m[1mpassed[0m 766077DC 000.00s Dot11FCS parent matching
[34m[1mpassed[0m 05126D7A 000.00s Dot11FCS - test FCS with FCSField
[34m[1mpassed[0m EA560CD5 000.00s Dot11FCS computation
[31m[1mfailed[0m ACF025FF 000.00s WEP tests
[34m[1mpassed[0m E13623A6 000.00s RadioTap - dissection & build
[34m[1mpassed[0m BB29AD86 000.00s RadioTap Big-Small endian dissection
[34m[1mpassed[0m 3806F42D 000.00s RadioTap MCS dissection
[34m[1mpassed[0m 74C25A1B 000.00s RadioTap RX/TX Flags dissection
[34m[1mpassed[0m F3BC4C13 000.00s RadioTap, other fields
[34m[1mpassed[0m 5651AA7E 000.00s RadioTap - Dissection - guess_payload_class() test
[34m[1mpassed[0m 820C6AFF 000.00s RadioTap - Dissection with Extended presence mask
[34m[1mpassed[0m DCC54F08 000.00s RadioTap - Build with Extended presence mask
[34m[1mpassed[0m FABBE3AC 000.00s RadioTap - dissect & build TLVs
[34m[1mpassed[0m 453205F1 000.00s fuzz() calls for Dot11Elt()
[34m[1mpassed[0m FD9379A5 000.00s PMKIDListPacket - Check computation of nb_pmkids
[34m[1mpassed[0m C797C178 000.01s Dot11EltRSN - Check computation of nb_pairwise_cipher_suites and nb_akm_suites
[34m[1mpassed[0m 5B830B66 000.00s Dot11EltMicrosoftWPA - Check computation of nb_pairwise_cipher_suites and nb_akm_suites
Campaign CRC=D47F8133 in 000.08s SHA=D2F285F95833E7674EA00986966986619A8A2464
[31m[1mPASSED=45 FAILED=2[0m
[32m━ Loading: test/scapy/layers/dot15d4.uts[0m
[34m[1mpassed[0m 02A90162 000.01s Dot15D4 layers
[34m[1mpassed[0m 6F6DE6FD 000.00s Dot15d4FCS parent matching
[34m[1mpassed[0m E6F99953 000.00s Dot15d4FCS - Beacon (without pending addresses)
[34m[1mpassed[0m A0A5F80D 000.00s Dot15d4FCS - Beacon (with pending addresses)
[34m[1mpassed[0m 87BAD503 000.00s Dot15d4FCS - Coordinator Realignment (without the channel page)
[34m[1mpassed[0m FFEF437E 000.00s Dot15d4FCS - Coordinator Realignment (with the channel page)
[34m[1mpassed[0m E42C06AC 000.00s Set SixLoWPAN
[34m[1mpassed[0m 102CC8AF 000.00s SixLoWPAN layers
[34m[1mpassed[0m 0719EC8F 000.00s Default dissection
[34m[1mpassed[0m A0F43B4C 000.00s Frag second dissection
[34m[1mpassed[0m F9570ED2 000.00s LoWPAN_IPHC dissections
[34m[1mpassed[0m E91D09A7 000.00s LoWPAN_IPHC - M=1, DAC=1, DAM=0
[34m[1mpassed[0m 45DAC9F2 000.00s LoWPAN_NHC - NHC_UDP
[34m[1mpassed[0m 7ED5CECB 000.00s LoWPAN_NHC - compute UDP NHC_UDP
[34m[1mpassed[0m 53D1B570 000.00s LoWPAN_NHC - NHC_IPv6Ext
[34m[1mpassed[0m ED77A2DA 000.00s LoWPAN_HC1 dissection & build
[34m[1mpassed[0m F6763E0E 000.00s LoWPAN_HC1 build from scratch
[34m[1mpassed[0m E73CE9DE 000.01s Advanced packets - dissection & FCS computation
[34m[1mpassed[0m F62E82C6 000.00s Dot15d4AuxSecurityHeader - build & dissect
[34m[1mpassed[0m 0CA0C1B8 000.00s Fragmentate packet & defragmentate
[34m[1mpassed[0m 00000000 000.00s Mesh Header.
[34m[1mpassed[0m 06E7450E 000.00s SixLoWPAN - Advanced 1
[34m[1mpassed[0m A815A33C 000.00s SixLoWPAN - Advanced 2
[34m[1mpassed[0m AD889D86 000.00s SixLoWPAN - Advanced 3
[34m[1mpassed[0m 3A2BFFAB 000.00s SixLoWPAN - Using ICMP
[34m[1mpassed[0m 8B03A86B 000.00s LoWPAN_IPHC - Extracted packet
[34m[1mpassed[0m 788652DA 000.01s LoWPAN_IPHC - Extracted packet 2
[34m[1mpassed[0m FDA7F30B 000.00s SixLoWPAN - Check Traffic Class and Flow Label when TF=0
[34m[1mpassed[0m CAC867F0 000.00s SixLoWPAN - Check Traffic Class and Flow Label when TF=1
[34m[1mpassed[0m 57EFE8B6 000.00s SixLoWPAN - Check Traffic Class and Flow Label when TF=2
[34m[1mpassed[0m 072CF461 000.01s SixLoWPAN - Checking the Hop Limit value in the IPv6 packet decompressed
[34m[1mpassed[0m 251FC4FE 000.00s SixLoWPAN - Check Source Address
[34m[1mpassed[0m 62040B9E 000.00s SixLoWPAN over Ethernet
[34m[1mpassed[0m 04477E01 000.00s Compressed SixLoWPAN - real packets with ZEP2
[34m[1mpassed[0m BCAF850C 000.00s SixLoWPAN - Using ETH
[34m[1mpassed[0m 3DCF0403 000.00s SixLoWPAN - Using ETH 2
[34m[1mpassed[0m 389AF3BB 000.00s SixLoWPAN - Using ETH 3
[34m[1mpassed[0m EB847AC1 000.00s Set zigbee
[34m[1mpassed[0m C6026C51 000.00s ZigbeeNWKStub - ZigbeeNWK dispatch_hook
[34m[1mpassed[0m 8E22AE0D 000.00s Zigbee - ZCLGeneralReadAttributesResponse
[34m[1mpassed[0m 7C78C9E6 000.00s Zigbee - ZigbeeAppDataPayload
[34m[1mpassed[0m BC86B4AF 000.01s Zigbee - advanced dissection
[34m[1mpassed[0m F6A5B810 000.00s Zigbee - skke_1 transport key
[34m[1mpassed[0m 26CF1774 000.00s Zigbee - Link Status
[34m[1mpassed[0m A0FBF41E 000.00s Zigbee - Network Report
[34m[1mpassed[0m F75E85D2 000.00s Zigbee - End Device Timeout Request
[34m[1mpassed[0m B26A7844 000.00s Zigbee - End Device Timeout Response
[34m[1mpassed[0m 6EE5003C 000.00s Zigbee - Transport Key
[34m[1mpassed[0m F905A9D3 000.00s Zigbee - Request Key
[34m[1mpassed[0m 950EECCE 000.00s Zigbee - Tunnel
[34m[1mpassed[0m C6D4F8D9 000.00s Zigbee - Verify Key
[34m[1mpassed[0m 5CBCDD40 000.00s Zigbee - Confirm Key
[34m[1mpassed[0m CA622A7A 000.00s Zigbee - APS acknowledgment (with the Acknowledgment Format enabled)
[34m[1mpassed[0m 9581C79B 000.00s Zigbee - APS acknowledgment (with the Acknowledgment Format disabled)
[34m[1mpassed[0m 04D8D369 000.00s Zigbee - ZDP command
[34m[1mpassed[0m F0F15001 000.00s Zigbee - ZDP command: Device_annce
[34m[1mpassed[0m 33B4CFEF 000.00s Zigbee - ZCL General command: Read Attributes
[34m[1mpassed[0m 4B07B502 000.00s Zigbee - ZCL General command: Read Attributes Response
[34m[1mpassed[0m 8E1F9454 000.00s Zigbee - ZCL IAS Zone command: Zone Enroll Response
Campaign CRC=7FF31545 in 000.11s SHA=0C7274164D280BFC3F499F31FB8DC82D6AA694A4
[34m[1mPASSED=59 FAILED=0[0m
[32m━ Loading: test/scapy/layers/eap.uts[0m
[34m[1mpassed[0m 5259CA59 000.00s EAPOL - Basic Instantiation
[34m[1mpassed[0m D337081E 000.00s EAPOL - Instantiation with specific values
[34m[1mpassed[0m 0B33D50B 000.00s EAPOL - Dissection (1)
[34m[1mpassed[0m B3B3D2C8 000.00s EAPOL - Dissection (2)
[34m[1mpassed[0m 870F76A2 000.00s EAPOL - Dissection (3)
[34m[1mpassed[0m 18748F1F 000.00s EAPOL - Dissection (4)
[34m[1mpassed[0m D29AE44C 000.00s EAPOL - Dissection (5)
[34m[1mpassed[0m 75FA0E16 000.00s EAPOL - Dissection (6)
[34m[1mpassed[0m 5C723E5C 000.00s EAPOL-MKA - With Basic parameter set - Dissection
[34m[1mpassed[0m E6B298E3 000.00s EAPOL-MKA - With Potential Peer List parameter set - Dissection
[34m[1mpassed[0m 1B777BA8 000.00s EAPOL-MKA - With Live Peer List parameter set - Dissection
[34m[1mpassed[0m 47B70661 000.00s EAPOL-MKA - With SAK Use parameter set - Dissection
[34m[1mpassed[0m AD793BE4 000.00s EAPOL-MKA - With Distributed SAK parameter set - Dissection
[34m[1mpassed[0m 8C5B5629 000.00s EAP - Basic Instantiation
[34m[1mpassed[0m 00852BB9 000.00s EAP - Instantiation with specific values
[34m[1mpassed[0m 7D59BE49 000.00s EAP - Instantiation - Multiple desired authentication types
[34m[1mpassed[0m E9D66340 000.00s EAP - Dissection (1)
[34m[1mpassed[0m F5EB25FD 000.00s EAP - Dissection (2)
[34m[1mpassed[0m 0D80AAC6 000.00s EAP - Dissection (3)
[34m[1mpassed[0m D82E5B28 000.00s EAP - Dissection (4)
[34m[1mpassed[0m A5ED0BD3 000.00s EAP - Dissection (5)
[34m[1mpassed[0m 42790080 000.00s EAP - Dissection (6)
[34m[1mpassed[0m 22EDE159 000.00s EAP - Dissection (7)
[34m[1mpassed[0m C559CDC6 000.00s EAP - Dissection (8)
[34m[1mpassed[0m 02A2E196 000.00s EAP - EAP_TLS - Basic Instantiation
[34m[1mpassed[0m ABC6CAE9 000.00s EAP - EAP_FAST - Basic Instantiation
[34m[1mpassed[0m D41E649B 000.00s EAP - EAP_TTLS - Basic Instantiation
[34m[1mpassed[0m 55E8207D 000.00s EAP - EAP_PEAP - Basic Instantiation
[34m[1mpassed[0m 8CB571E8 000.00s EAP - EAP_MD5 - Basic Instantiation
[34m[1mpassed[0m D74B3838 000.00s EAP - EAP_MD5 - Request - Dissection (8)
[34m[1mpassed[0m D77F99F7 000.00s EAP - EAP_MD5 - Response - Dissection (9)
[34m[1mpassed[0m 6D444E21 000.00s EAP - LEAP - Basic Instantiation
[34m[1mpassed[0m 5FB74C57 000.00s EAP - LEAP - Request - Dissection (10)
[34m[1mpassed[0m DC8BE016 000.00s EAP - LEAP - Response - Dissection (11)
[34m[1mpassed[0m 7C21F60D 000.00s EAP - PEAP - Request - Dissection
[34m[1mpassed[0m 495C6233 000.00s EAP - PEAP - Response - Dissection
[34m[1mpassed[0m 1A2740CC 000.00s EAP - Layers (1)
[34m[1mpassed[0m 53B693B0 000.00s EAP - Layers (2)
[34m[1mpassed[0m BC8A3153 000.00s EAP - sessions (1)
[34m[1mpassed[0m 147CEDA0 000.00s EAP - sessions (2)
Campaign CRC=19DF8773 in 000.02s SHA=45432D5C1D23F6BDAE074D8756F7A646CD8A5D36
[34m[1mPASSED=40 FAILED=0[0m
[32m━ Loading: test/scapy/layers/hsrp.uts[0m
[34m[1mpassed[0m C638A950 000.00s HSRP - build & dissection
Campaign CRC=27F64651 in 000.00s SHA=3F436271EF6352DD5DC95DC2E23E95E9762F52C7
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/scapy/layers/http.uts[0m
[34m[1mpassed[0m 53E033A3 000.02s TCPSession - dissect HTTP 1.0 chunked image
[34m[1mpassed[0m B6FCD3E5 000.01s TCPSession - dissect HTTP 1.0 html page with Content_Length
[34m[1mpassed[0m A3A5CE24 000.01s HTTP decompression (gzip)
[31m[1mfailed[0m 5E68D7C3 000.00s HTTP decompression (brotli)
[31m[1mfailed[0m FF26C0AD 000.00s HTTP decompression (zstd)
[34m[1mpassed[0m 8F68CFB2 000.01s HTTP PSH bug fix
[34m[1mpassed[0m 86606937 000.00s HTTP build
[34m[1mpassed[0m CB515FDC 000.02s HTTP 1.1 -> HTTP 2.0 Upgrade (h2c)
[34m[1mpassed[0m 9DE1F2E7 000.00s Test chunked with gzip
Campaign CRC=8EF086BB in 000.07s SHA=28B7F1F24F63D1909B56DBD0C7A64398478BD601
[31m[1mPASSED=7 FAILED=2[0m
[32m━ Loading: test/scapy/layers/inet.uts[0m
[34m[1mpassed[0m 4BA31281 000.00s IP options individual assembly
[34m[1mpassed[0m 9A8D64B8 000.00s IP options individual dissection
[34m[1mpassed[0m FD50E388 000.00s IP assembly and dissection with options
[34m[1mpassed[0m 17E9CA70 000.00s IPSession - dissect fragmented IP packets on-the-flow
[34m[1mpassed[0m 17096E2F 000.00s StringBuffer
[34m[1mpassed[0m 38D84225 000.00s fragment()
[34m[1mpassed[0m 2CBDD00C 000.00s fragment() and overloaded_fields
[34m[1mpassed[0m DFE594D6 000.00s fragment() already fragmented packets
[34m[1mpassed[0m 185E3CD1 000.00s fragment() with non-multiple-of-8 MTU
[34m[1mpassed[0m 38AA62AA 000.00s defrag()
[34m[1mpassed[0m 822DC623 000.00s defragment()
[34m[1mpassed[0m 2D66B8BF 000.01s defragment() uses timestamp of last fragment
[34m[1mpassed[0m CC47DF74 000.00s defragment() - Missing fragments
[34m[1mpassed[0m 1F6B1D73 000.01s defrag() / defragment() - Real DNS packets
[34m[1mpassed[0m 0BDBA2DA 000.00s Packet().fragment()
[34m[1mpassed[0m 5252347B 000.00s Packet().fragment() and overloaded_fields
[34m[1mpassed[0m E15B30B3 000.00s Packet().fragment() already fragmented packets
[34m[1mpassed[0m CF0C26C2 000.00s TCP options: UTO - basic build
[34m[1mpassed[0m 5A0D5D8D 000.00s TCP options: UTO - basic dissection
[34m[1mpassed[0m 20E9E9F9 000.00s TCP options: SAck - basic build
[34m[1mpassed[0m BCDB92DF 000.00s TCP options: SAck - basic dissection
[34m[1mpassed[0m 62A90792 000.00s TCP options: SAckOK - basic build
[34m[1mpassed[0m 64193152 000.00s TCP options: SAckOK - basic dissection
[34m[1mpassed[0m 62690F3F 000.00s TCP options: EOL - basic build
[34m[1mpassed[0m 83D3D900 000.00s TCP options: EOL - basic dissection
[34m[1mpassed[0m 96F1D377 000.00s TCP options: malformed - build
[34m[1mpassed[0m 4A34058C 000.00s TCP options: malformed - dissection
[34m[1mpassed[0m 2B2BCB4D 000.00s TCP options: wrong offset
[34m[1mpassed[0m F9C9B67E 000.00s TCP options: MPTCP - basic build using bytes
[34m[1mpassed[0m A3A21C0D 000.00s TCP options: invalid data offset
[34m[1mpassed[0m 73389405 000.00s TCP options: build oversized packet
[34m[1mpassed[0m 8B0C5B5A 000.00s TCP random options
[34m[1mpassed[0m FFF8CFB5 000.01s IP, TCP & UDP checksums (these tests highly depend on default values)
[34m[1mpassed[0m 6716D5EA 000.00s IP with forced-length 0
[34m[1mpassed[0m 6ADFBCF2 000.00s TCP payload with IP Total Length 0
[34m[1mpassed[0m 6EC93368 000.00s Layer binding
[34m[1mpassed[0m 35710318 000.00s IPv4 - ICMPTimeStampField
[34m[1mpassed[0m 1479098D 000.00s IPv4 - UDP null checksum
[34m[1mpassed[0m F6FC6EF6 000.01s IPv4 - (IP|UDP|TCP|ICMP)Error
[34m[1mpassed[0m 9193D025 000.00s IPv4 - mDNS
[34m[1mpassed[0m B3729FE3 000.00s IPv4 - utilities
[34m[1mpassed[0m A57EC9C5 000.03s IPv4 - traceroute utilities
[34m[1mpassed[0m 095AB3BC 000.01s IPv4 - reporting
[34m[1mpassed[0m AE1BA37F 000.00s IPv4 - Checksum computation with source routing
Campaign CRC=C6C61837 in 000.12s SHA=23C98CCCF8465A4DB1D313B7B384E58318DD545F
[34m[1mPASSED=44 FAILED=0[0m
[32m━ Loading: test/scapy/layers/inet6.uts[0m
[34m[1mpassed[0m D1CE7F15 000.00s IPv6 Class basic Instantiation
[34m[1mpassed[0m 47FE251A 000.00s IPv6 Class basic build (default values)
[34m[1mpassed[0m 2AFB2655 000.00s IPv6 Class basic dissection (default values)
[34m[1mpassed[0m 116A1D05 000.00s IPv6 Class with basic TCP stacked - build
[34m[1mpassed[0m E77B83DD 000.00s IPv6 Class with basic TCP stacked - dissection
[34m[1mpassed[0m F1924BC2 000.00s IPv6 Class with TCP and TCP data - build
[34m[1mpassed[0m D0C3C8D6 000.00s IPv6 Class with TCP and TCP data - dissection
[34m[1mpassed[0m F195E599 000.00s IPv6 Class binding with Ethernet - build
[34m[1mpassed[0m A0974624 000.00s IPv6 Class binding with Ethernet - dissection
[34m[1mpassed[0m FD44B31B 000.00s IPv6 Class - summary
[34m[1mpassed[0m DB6C92E4 000.00s IPv6 Class binding with GRE - build
[34m[1mpassed[0m FF2BFB92 000.00s IPv6 Class binding with GRE - dissection
[34m[1mpassed[0m D18B79CA 000.00s IPv6 ma_addr coverage on hashret
[34m[1mpassed[0m 11A76559 000.00s PseudoIPv6
[34m[1mpassed[0m 83A813B5 000.00s in6_chksum is computed on UDP or TCP build
[34m[1mpassed[0m 2D45AAC8 000.00s IPv6ExtHdrRouting Class - No address - build
[34m[1mpassed[0m 2FB49298 000.00s IPv6ExtHdrRouting Class - One address - build
[34m[1mpassed[0m 1398D3BC 000.00s IPv6ExtHdrRouting Class - Multiple Addresses - build
[34m[1mpassed[0m BFE608B1 000.00s IPv6ExtHdrRouting Class - Specific segleft (2->1) - build
[34m[1mpassed[0m 45FC49B8 000.00s IPv6ExtHdrRouting Class - Specific segleft (2->0) - build
[34m[1mpassed[0m 94E5198B 000.00s IPv6ExtHdrSegmentRouting Class - default - build & dissect
[34m[1mpassed[0m 345DF334 000.00s IPv6ExtHdrSegmentRouting Class - addresses list - build & dissect
[34m[1mpassed[0m E520764C 000.00s IPv6ExtHdrSegmentRouting Class - TLVs list - build & dissect
[34m[1mpassed[0m EB6DC194 000.00s IPv6ExtHdrSegmentRouting Class - both lists - build & dissect
[34m[1mpassed[0m 775ED580 000.00s IPv6ExtHdrSegmentRouting Class - UDP pseudo-header checksum - build & dissect
[34m[1mpassed[0m 64FF945F 000.00s Test in6_get6to4Prefix() - 0.0.0.0 address
[34m[1mpassed[0m D66F1EFB 000.00s Test in6_get6to4Prefix() - 255.255.255.255 address
[34m[1mpassed[0m 89A19ABC 000.00s Test in6_get6to4Prefix() - 1.1.1.1 address
[34m[1mpassed[0m C85A196A 000.00s Test in6_get6to4Prefix() - invalid address
[34m[1mpassed[0m A5258DE8 000.00s Test in6_6to4ExtractAddr() - 2002:: address
[34m[1mpassed[0m C1C5C579 000.00s Test in6_6to4ExtractAddr() - 255.255.255.255 address
[34m[1mpassed[0m 1856D118 000.00s Test in6_6to4ExtractAddr() - "2002:101:101::" address
[34m[1mpassed[0m FE84F001 000.00s Test in6_6to4ExtractAddr() - invalid address
[34m[1mpassed[0m 116945D2 000.00s in6_getLinkScopedMcastAddr() : default generation
[34m[1mpassed[0m 15A1164B 000.00s in6_getLinkScopedMcastAddr() : different valid scope values
[34m[1mpassed[0m 1B46F9F2 000.00s in6_getLinkScopedMcastAddr() : grpid in different formats
[34m[1mpassed[0m 9C7E1D83 000.00s in6_mactoifaceid() conversion function (test 1)
[34m[1mpassed[0m 86460033 000.00s in6_mactoifaceid() conversion function (test 2)
[34m[1mpassed[0m 18EDF6C2 000.00s in6_mactoifaceid() conversion function (test 3)
[34m[1mpassed[0m E27E1DC5 000.00s in6_mactoifaceid() conversion function (test 4)
[34m[1mpassed[0m 55DFF829 000.00s in6_mactoifaceid() conversion function (test 5)
[34m[1mpassed[0m 4FE7E599 000.00s in6_mactoifaceid() conversion function (test 6)
[34m[1mpassed[0m EC2EECAB 000.00s in6_mactoifaceid() conversion function (test 1)
[34m[1mpassed[0m DF0FDAFB 000.00s in6_mactoifaceid() conversion function (test 2)
[34m[1mpassed[0m B330D236 000.00s in6_mactoifaceid() conversion function (test 3)
[34m[1mpassed[0m FE0E4D6C 000.00s in6_mactoifaceid() conversion function (test 4)
[34m[1mpassed[0m 90033B9C 000.00s in6_mactoifaceid() conversion function (test 5)
[34m[1mpassed[0m A3220DCC 000.00s in6_mactoifaceid() conversion function (test 6)
[34m[1mpassed[0m 3089CFC8 000.00s in6_addrtomac() conversion function (test 1)
[34m[1mpassed[0m 03A8F998 000.00s in6_addrtomac() conversion function (test 2)
[34m[1mpassed[0m D7E362FE 000.00s in6_addrtomac() conversion function (test 3)
[34m[1mpassed[0m 9ADDFDA4 000.00s in6_addrtomac() conversion function (test 4)
[34m[1mpassed[0m 4CA418FF 000.00s in6_addrtomac() conversion function (test 5)
[34m[1mpassed[0m 7F852EAF 000.00s in6_addrtomac() conversion function (test 6)
[34m[1mpassed[0m 08767272 000.00s Test in6_getRandomizedIfaceId
[34m[1mpassed[0m 343ADC44 000.00s Test RFC 1924 function - in6_ctop() basic test
[34m[1mpassed[0m 6AF7CDC0 000.00s Test RFC 1924 function - in6_ctop() with character outside charset
[34m[1mpassed[0m C172E6F3 000.00s Test RFC 1924 function - in6_ctop() with bad length address
[34m[1mpassed[0m C4342A8E 000.00s Test RFC 1924 function - in6_ptoc() basic test
[34m[1mpassed[0m C4342A8E 000.00s Test RFC 1924 function - in6_ptoc() basic test
[34m[1mpassed[0m A4701435 000.00s Test RFC 1924 function - in6_ptoc() with bad input
[34m[1mpassed[0m FCEA333A 000.00s in6_getAddrType - 6to4 addresses
[34m[1mpassed[0m 131734E3 000.00s in6_getAddrType - Assignable Unicast global address
[34m[1mpassed[0m 8BDD9DB1 000.00s in6_getAddrType - Multicast global address
[34m[1mpassed[0m 213FCF86 000.00s in6_getAddrType - Multicast local address
[34m[1mpassed[0m 6CCACBE3 000.00s in6_getAddrType - Unicast Link-Local address
[34m[1mpassed[0m A8F9859D 000.00s in6_getAddrType - Loopback address
[34m[1mpassed[0m 1CC8CEFB 000.00s in6_getAddrType - Unspecified address
[34m[1mpassed[0m 9E620BFF 000.00s in6_getAddrType - Unassigned Global Unicast address
[34m[1mpassed[0m 2F5A3C1A 000.00s in6_getAddrType - Weird address (FE::1)
[34m[1mpassed[0m 1FCBAF51 000.00s in6_getAddrType - Weird address (FE8::1)
[34m[1mpassed[0m B929EB08 000.00s in6_getAddrType - Weird address (1::1)
[34m[1mpassed[0m 573C88CB 000.00s in6_getAddrType - Weird address (1000::1)
[34m[1mpassed[0m B0274B52 000.00s ICMPv6DestUnreach Class - Basic Build (no argument)
[34m[1mpassed[0m 7C20B0AE 000.00s ICMPv6DestUnreach Class - Basic Build over IPv6 (for cksum and overload)
[34m[1mpassed[0m 72B4D073 000.00s ICMPv6DestUnreach Class - Basic Build over IPv6 with some payload
[34m[1mpassed[0m 5DCED31E 000.00s ICMPv6DestUnreach Class - Dissection with default values and some payload
[34m[1mpassed[0m 61EBCF68 000.00s ICMPv6DestUnreach Class - Dissection with specific values
[34m[1mpassed[0m 6A099C52 000.00s ICMPv6DestUnreach Class - checksum computation related stuff
[34m[1mpassed[0m 92F17464 000.00s ICMPv6PacketTooBig Class - Basic Build (no argument)
[34m[1mpassed[0m 60E87C3A 000.00s ICMPv6PacketTooBig Class - Basic Build over IPv6 (for cksum and overload)
[34m[1mpassed[0m 0CA63B6C 000.00s ICMPv6PacketTooBig Class - Basic Build over IPv6 with some payload
[34m[1mpassed[0m 12D4F0B8 000.00s ICMPv6PacketTooBig Class - Dissection with default values and some payload
[34m[1mpassed[0m 03142868 000.00s ICMPv6PacketTooBig Class - Dissection with specific values
[34m[1mpassed[0m 1BB988F8 000.00s ICMPv6PacketTooBig Class - checksum computation related stuff
[34m[1mpassed[0m 8A3F901A 000.00s ICMPv6EchoRequest - Basic Instantiation
[34m[1mpassed[0m 699B15EE 000.00s ICMPv6EchoRequest - Instantiation with specific values
[34m[1mpassed[0m EA446DAE 000.00s ICMPv6EchoRequest - Basic dissection
[34m[1mpassed[0m E198A309 000.00s ICMPv6EchoRequest - Dissection with specific values
[34m[1mpassed[0m C8ABAED8 000.00s ICMPv6EchoRequest - Automatic checksum computation and field overloading (build)
[34m[1mpassed[0m D5DA8869 000.00s ICMPv6EchoRequest - Automatic checksum computation and field overloading (dissection)
[34m[1mpassed[0m 9B53C5BF 000.00s ICMPv6EchoReply - Basic Instantiation
[34m[1mpassed[0m 731C7145 000.00s ICMPv6EchoReply - Instantiation with specific values
[34m[1mpassed[0m 6D91D17E 000.00s ICMPv6EchoReply - Basic dissection
[34m[1mpassed[0m F842CDB8 000.00s ICMPv6EchoReply - Dissection with specific values
[34m[1mpassed[0m C7B5F6CD 000.00s ICMPv6EchoReply - Automatic checksum computation and field overloading (build)
[34m[1mpassed[0m D5DA8869 000.00s ICMPv6EchoReply - Automatic checksum computation and field overloading (dissection)
[34m[1mpassed[0m D877DBBC 000.00s ICMPv6EchoRequest and ICMPv6EchoReply - hashret() test 1
[34m[1mpassed[0m ED194425 000.00s ICMPv6EchoRequest and ICMPv6EchoReply - hashret() test 2
[34m[1mpassed[0m FCA0F5AC 000.00s ICMPv6EchoRequest and ICMPv6EchoReply - hashret() test 3
[34m[1mpassed[0m A74729F6 000.00s ICMPv6EchoRequest and ICMPv6EchoReply - hashret() test 4
[34m[1mpassed[0m 99E290FA 000.00s ICMPv6EchoRequest and ICMPv6EchoReply - answers() test 5
[34m[1mpassed[0m 6C09EBC2 000.00s ICMPv6EchoRequest and ICMPv6EchoReply - answers() test 6
[34m[1mpassed[0m 71108418 000.00s ICMPv6MRD_Advertisement - Basic instantiation
[34m[1mpassed[0m 8F8BA144 000.00s ICMPv6MRD_Advertisement - Instantiation with specific values
[34m[1mpassed[0m 9E6E21C9 000.00s ICMPv6MRD_Advertisement - Basic Dissection and overloading mechanisms
[34m[1mpassed[0m BE0C3CDF 000.00s ICMPv6MRD_Solicitation - Basic dissection
[34m[1mpassed[0m EE2B5EA7 000.00s ICMPv6MRD_Solicitation - Instantiation with specific values
[34m[1mpassed[0m 1547161E 000.00s ICMPv6MRD_Solicitation - Basic Dissection and overloading mechanisms
[34m[1mpassed[0m 8751A716 000.00s ICMPv6MRD_Termination Basic instantiation
[34m[1mpassed[0m F00B6415 000.00s ICMPv6MRD_Termination - Instantiation with specific values
[34m[1mpassed[0m EE51AADC 000.00s ICMPv6MRD_Termination - Basic Dissection and overloading mechanisms
[34m[1mpassed[0m B0AE1C85 000.00s HBHOptUnknown - Basic Instantiation
[34m[1mpassed[0m ACAF4AE9 000.00s HBHOptUnknown - Basic Dissection
[34m[1mpassed[0m 8BD4223D 000.00s HBHOptUnknown - Automatic optlen computation
[34m[1mpassed[0m 1149AE15 000.00s HBHOptUnknown - Instantiation with specific values
[34m[1mpassed[0m FEFDFEEE 000.00s HBHOptUnknown - Dissection with specific values
[34m[1mpassed[0m 11565441 000.00s Pad1 - Basic Instantiation
[34m[1mpassed[0m 518CEBB3 000.00s Pad1 - Basic Dissection
[34m[1mpassed[0m 61AB67F0 000.00s PadN - Basic Instantiation
[34m[1mpassed[0m 656980DD 000.00s PadN - Optlen Automatic computation
[34m[1mpassed[0m 17FC8495 000.00s PadN - Basic Dissection
[34m[1mpassed[0m C5CB0342 000.00s PadN - Dissection with specific values
[34m[1mpassed[0m D503B731 000.00s PadN - Instantiation with forced optlen
[34m[1mpassed[0m 1D8D7ADA 000.00s RouterAlert - Basic Instantiation
[34m[1mpassed[0m A54FE28F 000.00s RouterAlert - Basic Dissection
[34m[1mpassed[0m C7B9FB38 000.00s RouterAlert - Instantiation with specific values
[34m[1mpassed[0m F7186483 000.00s RouterAlert - Instantiation with specific values
[34m[1mpassed[0m F3FA9ADA 000.00s Jumbo - Basic Instantiation
[34m[1mpassed[0m 99EED01B 000.00s Jumbo - Basic Dissection
[34m[1mpassed[0m 91205FD6 000.00s Jumbo - Instantiation with specific values
[34m[1mpassed[0m E5FC9898 000.00s Jumbo - Dissection with specific values
[34m[1mpassed[0m 4CCEF5BF 000.00s HAO - Basic Instantiation
[34m[1mpassed[0m 4E0F867C 000.00s HAO - Basic Dissection
[34m[1mpassed[0m C418FF05 000.00s HAO - Instantiation with specific values
[34m[1mpassed[0m E7DC6D56 000.00s HAO - Dissection with specific values
[34m[1mpassed[0m EC3D2FE2 000.00s HAO - hashret
[34m[1mpassed[0m 233C6301 000.00s IPv6ExtHdrHopByHop - Basic Instantiation
[34m[1mpassed[0m 7B48FFB4 000.00s IPv6ExtHdrHopByHop - Instantiation with HAO option
[34m[1mpassed[0m FADA6FBC 000.00s IPv6ExtHdrHopByHop - Instantiation with RouterAlert option
[34m[1mpassed[0m 2C5CF83A 000.00s IPv6ExtHdrHopByHop - Instantiation with Jumbo option
[34m[1mpassed[0m D695A953 000.00s IPv6ExtHdrHopByHop - Complete dissection with Jumbo option
[34m[1mpassed[0m 4F45480A 000.00s IPv6ExtHdrHopByHop - Instantiation with Pad1 option
[34m[1mpassed[0m 4F45480A 000.00s IPv6ExtHdrHopByHop - Instantiation with PadN option
[34m[1mpassed[0m 5E80B26B 000.00s IPv6ExtHdrHopByHop - Instantiation with Jumbo, RouterAlert, HAO
[34m[1mpassed[0m A0AB0063 000.00s IPv6ExtHdrHopByHop - Instantiation with HAO, Jumbo, RouterAlert
[34m[1mpassed[0m 9B504E62 000.00s IPv6ExtHdrHopByHop - Instantiation with RouterAlert, HAO, Jumbo
[34m[1mpassed[0m A69E2AD2 000.00s IPv6ExtHdrHopByHop - Hashret
[34m[1mpassed[0m FECF1887 000.00s IPv6ExtHdrHopByHop - Basic Dissection
[34m[1mpassed[0m 4DDF99AE 000.00s ICMPv6ND_RS - Basic instantiation
[34m[1mpassed[0m D56894C6 000.00s ICMPv6ND_RS - Basic instantiation with empty dst in IPv6 underlayer
[34m[1mpassed[0m A90C1892 000.00s ICMPv6ND_RS - Basic dissection
[34m[1mpassed[0m EAC3B7DA 000.00s ICMPv6ND_RS - Basic instantiation with empty dst in IPv6 underlayer
[34m[1mpassed[0m 988340A1 000.00s ICMPv6ND_RA - Basic Instantiation
[34m[1mpassed[0m EAB9F5B1 000.00s ICMPv6ND_RA - Basic instantiation with empty dst in IPv6 underlayer
[34m[1mpassed[0m 854A2794 000.00s ICMPv6ND_RA - Basic dissection
[34m[1mpassed[0m 10B9F0CB 000.00s ICMPv6ND_RA - Basic instantiation with empty dst in IPv6 underlayer
[34m[1mpassed[0m 5F315605 000.00s ICMPv6ND_RA - Answers
[34m[1mpassed[0m 729ACF34 000.00s ICMPv6ND_RA - Summary Output
[34m[1mpassed[0m 4107B846 000.00s ICMPv6ND_NS - Basic Instantiation
[34m[1mpassed[0m BE7F71E1 000.00s ICMPv6ND_NS - Instantiation with specific values
[34m[1mpassed[0m 0E54D262 000.00s ICMPv6ND_NS - Basic Dissection
[34m[1mpassed[0m AE5264E2 000.00s ICMPv6ND_NS - Dissection with specific values
[34m[1mpassed[0m B8ED22A7 000.00s ICMPv6ND_NS - IPv6 layer fields overloading
[34m[1mpassed[0m 619885DF 000.00s ICMPv6ND_NA - Basic Instantiation
[34m[1mpassed[0m 223DB4FA 000.00s ICMPv6ND_NA - Instantiation with specific values
[34m[1mpassed[0m 4439E621 000.00s ICMPv6ND_NA - Basic Dissection
[34m[1mpassed[0m A2CDB8CB 000.00s ICMPv6ND_NA - Dissection with specific values
[34m[1mpassed[0m B8ED22A7 000.00s ICMPv6ND_NS - IPv6 layer fields overloading
[34m[1mpassed[0m AB86627F 000.00s ICMPv6ND_ND/ICMPv6ND_ND matching - test 1
[34m[1mpassed[0m 9A765EC0 000.00s ICMPv6NDOptUnknown - Basic Instantiation
[34m[1mpassed[0m 5A5D9618 000.00s ICMPv6NDOptUnknown - Instantiation with specific values
[34m[1mpassed[0m 3FE39940 000.00s ICMPv6NDOptUnknown - Basic Dissection
[34m[1mpassed[0m 13873292 000.00s ICMPv6NDOptUnknown - Dissection with specific values
[34m[1mpassed[0m 90AF5747 000.00s ICMPv6NDOptSrcLLAddr - Basic Instantiation
[34m[1mpassed[0m E6828AEF 000.00s ICMPv6NDOptSrcLLAddr - Instantiation with specific values
[34m[1mpassed[0m 17C13F23 000.00s ICMPv6NDOptSrcLLAddr - Basic Dissection
[34m[1mpassed[0m 68952992 000.00s ICMPv6NDOptSrcLLAddr - Instantiation with specific values
[34m[1mpassed[0m DC35A7E9 000.00s ICMPv6NDOptDstLLAddr - Basic Instantiation
[34m[1mpassed[0m 6AF98091 000.00s ICMPv6NDOptDstLLAddr - Instantiation with specific values
[34m[1mpassed[0m A222A5B1 000.00s ICMPv6NDOptDstLLAddr - Basic Dissection
[34m[1mpassed[0m 4F1DECB4 000.00s ICMPv6NDOptDstLLAddr - Instantiation with specific values
[34m[1mpassed[0m FF4E47BB 000.00s ICMPv6NDOptPrefixInfo - Basic Instantiation
[34m[1mpassed[0m 48915433 000.00s ICMPv6NDOptPrefixInfo - Instantiation with specific values
[34m[1mpassed[0m ACF9B9CF 000.00s ICMPv6NDOptPrefixInfo - Basic Dissection
[34m[1mpassed[0m 5CFA5B35 000.00s ICMPv6NDOptPrefixInfo - Instantiation with specific values
[34m[1mpassed[0m 406CE07A 000.00s ICMPv6NDOptRedirectedHdr - Basic Instantiation
[34m[1mpassed[0m D0348B15 000.00s ICMPv6NDOptRedirectedHdr - Instantiation with specific values
[34m[1mpassed[0m 2CEAD38E 000.00s ICMPv6NDOptRedirectedHdr - Instantiation with simple IPv6 packet (no upper layer)
[34m[1mpassed[0m 8EEC368B 000.00s ICMPv6NDOptRedirectedHdr - Basic Dissection
[34m[1mpassed[0m C1EB1E49 000.00s ICMPv6NDOptRedirectedHdr - Disssection with specific values
[34m[1mpassed[0m 825E4405 000.00s ICMPv6NDOptRedirectedHdr - Dissection with cut IPv6 Header
[34m[1mpassed[0m C3B0C13D 000.00s ICMPv6NDOptRedirectedHdr - Complete dissection
[34m[1mpassed[0m 12DB2C22 000.00s ICMPv6NDOptMTU - Basic Instantiation
[34m[1mpassed[0m 65770798 000.00s ICMPv6NDOptMTU - Instantiation with specific values
[34m[1mpassed[0m 83B871C6 000.00s ICMPv6NDOptMTU - Basic dissection
[34m[1mpassed[0m 17C89A45 000.00s ICMPv6NDOptMTU - Dissection with specific values
[34m[1mpassed[0m 23296DBD 000.00s ICMPv6NDOptMTU - Summary Output
[34m[1mpassed[0m 136EA017 000.00s ICMPv6NDOptShortcutLimit - Basic Instantiation
[34m[1mpassed[0m 559E7404 000.00s ICMPv6NDOptShortcutLimit - Instantiation with specific values
[34m[1mpassed[0m 0F220EAF 000.00s ICMPv6NDOptShortcutLimit - Basic Dissection
[34m[1mpassed[0m 73976BB0 000.00s ICMPv6NDOptShortcutLimit - Dissection with specific values
[34m[1mpassed[0m BF81F813 000.00s ICMPv6NDOptAdvInterval - Basic Instantiation
[34m[1mpassed[0m CA6C93CA 000.00s ICMPv6NDOptAdvInterval - Instantiation with specific values
[34m[1mpassed[0m E94BFFAE 000.00s ICMPv6NDOptAdvInterval - Basic dissection
[34m[1mpassed[0m BEF20018 000.00s ICMPv6NDOptAdvInterval - Dissection with specific values
[34m[1mpassed[0m C231587A 000.00s ICMPv6NDOptHAInfo - Basic Instantiation
[34m[1mpassed[0m 0B0C8DF5 000.00s ICMPv6NDOptHAInfo - Instantiation with specific values
[34m[1mpassed[0m CF87AC62 000.00s ICMPv6NDOptHAInfo - Basic dissection
[34m[1mpassed[0m 498F662C 000.00s ICMPv6NDOptHAInfo - Dissection with specific values
[34m[1mpassed[0m B69122C3 000.00s ICMPv6NDOptSrcAddrList - Basic Instantiation
[34m[1mpassed[0m DE7FE747 000.00s ICMPv6NDOptSrcAddrList - Instantiation with specific values (auto len)
[34m[1mpassed[0m B5B76D1F 000.00s ICMPv6NDOptSrcAddrList - Instantiation with specific values
[34m[1mpassed[0m 5267358D 000.00s ICMPv6NDOptSrcAddrList - Basic Dissection
[34m[1mpassed[0m C13C47A5 000.00s ICMPv6NDOptSrcAddrList - Dissection with specific values (auto len)
[34m[1mpassed[0m 0BDF3C1D 000.00s ICMPv6NDOptSrcAddrList - Dissection with specific values
[34m[1mpassed[0m C87ECDC7 000.00s ICMPv6NDOptTgtAddrList - Basic Instantiation
[34m[1mpassed[0m 8686FB8C 000.00s ICMPv6NDOptTgtAddrList - Instantiation with specific values (auto len)
[34m[1mpassed[0m 7E021A90 000.00s ICMPv6NDOptTgtAddrList - Instantiation with specific values
[34m[1mpassed[0m DF694DCF 000.00s ICMPv6NDOptTgtAddrList - Basic Dissection
[34m[1mpassed[0m 3B066EBB 000.00s ICMPv6NDOptTgtAddrList - Dissection with specific values (auto len)
[34m[1mpassed[0m C26E6D95 000.00s ICMPv6NDOptTgtAddrList - Instantiation with specific values
[34m[1mpassed[0m 7D59A368 000.00s ICMPv6NDOptIPAddr - Basic Instantiation
[34m[1mpassed[0m C1D1E7D5 000.00s ICMPv6NDOptIPAddr - Instantiation with specific values
[34m[1mpassed[0m 1A2F5C7F 000.00s ICMPv6NDOptIPAddr - Basic Dissection
[34m[1mpassed[0m 0B8C346B 000.00s ICMPv6NDOptIPAddr - Dissection with specific values
[34m[1mpassed[0m EFC6686C 000.00s ICMPv6NDOptNewRtrPrefix - Basic Instantiation
[34m[1mpassed[0m D9B46DE8 000.00s ICMPv6NDOptNewRtrPrefix - Instantiation with specific values
[34m[1mpassed[0m E7373FCC 000.00s ICMPv6NDOptNewRtrPrefix - Basic Dissection
[34m[1mpassed[0m 321A7BB0 000.00s ICMPv6NDOptNewRtrPrefix - Dissection with specific values
[34m[1mpassed[0m 8CA3631C 000.00s ICMPv6NDOptLLA - Basic Instantiation
[34m[1mpassed[0m 48526498 000.00s ICMPv6NDOptLLA - Instantiation with specific values
[34m[1mpassed[0m C536C823 000.00s ICMPv6NDOptLLA - Basic Dissection
[34m[1mpassed[0m 1DEC5413 000.00s ICMPv6NDOptLLA - Dissection with specific values
[34m[1mpassed[0m 8C3E3751 000.00s ICMPv6NDOptRouteInfo - Basic Instantiation
[34m[1mpassed[0m 44A42CE7 000.00s ICMPv6NDOptRouteInfo - Instantiation with forced prefix but no length
[34m[1mpassed[0m D30C6789 000.00s ICMPv6NDOptRouteInfo - Instantiation with forced length values (1/4)
[34m[1mpassed[0m 03213D9B 000.00s ICMPv6NDOptRouteInfo - Instantiation with forced length values (2/4)
[34m[1mpassed[0m D2034B7A 000.00s ICMPv6NDOptRouteInfo - Instantiation with forced length values (3/4)
[34m[1mpassed[0m 9B323128 000.00s ICMPv6NDOptRouteInfo - Instantiation with forced length values (4/4)
[34m[1mpassed[0m 0E899A78 000.00s ICMPv6NDOptRouteInfo - Instantiation with specific values
[34m[1mpassed[0m A9702412 000.00s ICMPv6NDOptRouteInfo - Basic dissection
[34m[1mpassed[0m BA32308F 000.00s ICMPv6NDOptRouteInfo - Dissection with specific values
[34m[1mpassed[0m 24C9726E 000.00s ICMPv6NDOptRouteInfo - Summary Output
[34m[1mpassed[0m 77F8890C 000.00s ICMPv6NDOptMAP - Basic Instantiation
[34m[1mpassed[0m 2FEE4C87 000.00s ICMPv6NDOptMAP - Instantiation with specific values
[34m[1mpassed[0m C6AAF0A2 000.00s ICMPv6NDOptMAP - Basic Dissection
[34m[1mpassed[0m 900763C7 000.00s ICMPv6NDOptMAP - Dissection with specific values
[34m[1mpassed[0m 4F509225 000.00s ICMPv6NDOptRDNSS - Basic Instantiation
[34m[1mpassed[0m 9CD0A8FB 000.00s ICMPv6NDOptRDNSS - Basic instantiation with 1 DNS address
[34m[1mpassed[0m C58A2B38 000.00s ICMPv6NDOptRDNSS - Basic instantiation with 2 DNS addresses
[34m[1mpassed[0m 43D6D077 000.00s ICMPv6NDOptRDNSS - Instantiation with specific values
[34m[1mpassed[0m DC2BFF23 000.00s ICMPv6NDOptRDNSS - Basic Dissection
[34m[1mpassed[0m 37BF7067 000.00s ICMPv6NDOptRDNSS - Dissection (with 1 DNS address)
[34m[1mpassed[0m 9D964AF3 000.00s ICMPv6NDOptRDNSS - Dissection (with 2 DNS addresses)
[34m[1mpassed[0m D07F3579 000.00s ICMPv6NDOptRDNSS - Summary Output
[34m[1mpassed[0m 043EECBA 000.00s ICMPv6NDOptDNSSL - Basic Instantiation
[34m[1mpassed[0m F6B0842F 000.00s ICMPv6NDOptDNSSL - Instantiation with 1 search domain, as seen in the wild
[34m[1mpassed[0m E914C420 000.00s ICMPv6NDOptDNSSL - Basic instantiation with 2 search domains
[34m[1mpassed[0m ECC9DE2E 000.00s ICMPv6NDOptDNSSL - Basic instantiation with 3 search domains
[34m[1mpassed[0m B1DC63A2 000.00s ICMPv6NDOptDNSSL - Basic Dissection
[34m[1mpassed[0m B96216D1 000.00s ICMPv6NDOptDNSSL - Basic Dissection with specific values
[34m[1mpassed[0m 0245ABBD 000.00s ICMPv6NDOptDNSSL - Summary Output
[34m[1mpassed[0m 3FDE1930 000.00s ICMPv6NDOptEFA - Basic Instantiation
[34m[1mpassed[0m C66DCEC4 000.00s ICMPv6NDOptEFA - Basic Dissection
[34m[1mpassed[0m 5A9CA3E4 000.00s ICMPv6NIQueryNOOP - Basic Instantiation
[34m[1mpassed[0m E7B5CD0E 000.00s ICMPv6NIQueryNOOP - Basic Dissection
[34m[1mpassed[0m 9E5885F0 000.00s ICMPv6NIQueryName - single label DNS name (internal)
[34m[1mpassed[0m 09349544 000.00s ICMPv6NIQueryName - single label DNS name
[34m[1mpassed[0m B5A1B89B 000.00s ICMPv6NIQueryName - fqdn (internal)
[34m[1mpassed[0m 0A731407 000.00s ICMPv6NIQueryName - fqdn
[34m[1mpassed[0m 700787CB 000.00s ICMPv6NIQueryName - IPv6 address (internal)
[34m[1mpassed[0m 118B9433 000.00s ICMPv6NIQueryName - IPv6 address
[34m[1mpassed[0m 646BF569 000.00s ICMPv6NIQueryName - IPv4 address (internal)
[34m[1mpassed[0m 12166AC6 000.00s ICMPv6NIQueryName - IPv4 address
[34m[1mpassed[0m 9E9ECE7E 000.00s ICMPv6NIQueryName - build & dissection
[34m[1mpassed[0m F32AF9E2 000.00s ICMPv6NIQueryName - dissection
[34m[1mpassed[0m DCE7145A 000.00s ICMPv6NIQueryIPv6 - single label DNS name (internal)
[34m[1mpassed[0m E1691DBD 000.00s ICMPv6NIQueryIPv6 - single label DNS name
[34m[1mpassed[0m EB6E8B1A 000.00s ICMPv6NIQueryIPv6 - fqdn (internal)
[34m[1mpassed[0m E22E9CFE 000.00s ICMPv6NIQueryIPv6 - fqdn
[34m[1mpassed[0m AB7F5D94 000.00s ICMPv6NIQueryIPv6 - IPv6 address (internal)
[34m[1mpassed[0m C1C61F21 000.00s ICMPv6NIQueryIPv6 - IPv6 address
[34m[1mpassed[0m FE8A89EC 000.00s ICMPv6NIQueryIPv6 - IPv4 address (internal)
[34m[1mpassed[0m 9CAA8473 000.00s ICMPv6NIQueryIPv6 - IPv4 address
[34m[1mpassed[0m 80D80DB7 000.00s ICMPv6NIQueryIPv4 - single label DNS name (internal)
[34m[1mpassed[0m 10F9B2D6 000.00s ICMPv6NIQueryIPv4 - single label DNS name
[34m[1mpassed[0m E9FA74CB 000.00s ICMPv6NIQueryIPv4 - fqdn (internal)
[34m[1mpassed[0m 13BE3395 000.00s ICMPv6NIQueryIPv4 - fqdn
[34m[1mpassed[0m 57710B44 000.00s ICMPv6NIQueryIPv4 - IPv6 address (internal)
[34m[1mpassed[0m 4FE1F2D7 000.00s ICMPv6NIQueryIPv4 - IPv6 address
[34m[1mpassed[0m 0F5CFF51 000.00s ICMPv6NIQueryIPv4 - IPv4 address (internal)
[34m[1mpassed[0m D3A66514 000.00s ICMPv6NIQueryIPv4 - IPv4 address
[34m[1mpassed[0m 90EE9B24 000.00s ICMPv6NIQueryIPv4 - dissection
[34m[1mpassed[0m FB14D0BC 000.00s ICMPv6NIQueryIPv4 - hashret()
[34m[1mpassed[0m 4FA1E638 000.00s ICMPv6NIQuery* - flags handling (Test 1)
[34m[1mpassed[0m 9DA8440B 000.00s ICMPv6NIQuery* - flags handling (Test 2)
[34m[1mpassed[0m 1DD2FCF9 000.00s ICMPv6NIReply* - flags handling (Test 1)
[34m[1mpassed[0m 04A33787 000.00s ICMPv6NIReply* - flags handling (Test 2)
[34m[1mpassed[0m 8ECA63FE 000.00s ICMPv6NIQuery* - Flags Default values
[34m[1mpassed[0m 7043A408 000.00s ICMPv6NIReply* - Flags Default values
[34m[1mpassed[0m 9DD5F86E 000.00s ICMPv6NIQueryIPv6 - dispatch with nothing in data
[34m[1mpassed[0m F03359A7 000.00s ICMPv6NIQueryIPv6 - dispatch with IPv6 address in data
[34m[1mpassed[0m A0C43FF6 000.00s ICMPv6NIQueryIPv6 - dispatch with IPv4 address in data
[34m[1mpassed[0m FE817D4D 000.00s ICMPv6NIQueryIPv6 - dispatch with name in data
[34m[1mpassed[0m 876BC56C 000.00s ICMPv6NIQueryName - dispatch with nothing in data
[34m[1mpassed[0m E48D9A5D 000.00s ICMPv6NIQueryName - dispatch with IPv6 address in data
[34m[1mpassed[0m 74621ABB 000.00s ICMPv6NIQueryName - dispatch with IPv4 address in data
[34m[1mpassed[0m 2E1A4B52 000.00s ICMPv6NIQueryName - dispatch with name in data
[34m[1mpassed[0m 9EB63E24 000.00s ICMPv6NIQueryIPv4 - dispatch with nothing in data
[34m[1mpassed[0m 21D154E9 000.00s ICMPv6NIQueryIPv4 - dispatch with IPv6 address in data
[34m[1mpassed[0m B13ED40F 000.00s ICMPv6NIQueryIPv4 - dispatch with IPv6 address in data
[34m[1mpassed[0m 7E7B6F19 000.00s ICMPv6NIQueryIPv4 - dispatch with name in data
[34m[1mpassed[0m CD3BE374 000.00s ICMPv6NIReplyName - dispatch
[34m[1mpassed[0m D785DE76 000.00s ICMPv6NIReplyIPv6 - dispatch
[34m[1mpassed[0m D4E6183C 000.00s ICMPv6NIReplyIPv4 - dispatch
[34m[1mpassed[0m 5A60D811 000.00s ICMPv6NIReplyRefuse - dispatch
[34m[1mpassed[0m D5BFCED9 000.00s ICMPv6NIReplyUnknown - dispatch
[34m[1mpassed[0m 7C332597 000.00s ICMPv6NIReplyNOOP - single DNS name without hint => understood as string (internal)
[34m[1mpassed[0m 3B9A395F 000.00s ICMPv6NIReplyNOOP - single DNS name without hint => understood as string
[34m[1mpassed[0m 3788EEC1 000.00s ICMPv6NIReplyNOOP - fqdn without hint => understood as string (internal)
[34m[1mpassed[0m A25145C0 000.00s ICMPv6NIReplyNOOP - fqdn without hint => understood as string
[34m[1mpassed[0m 999B2E68 000.00s ICMPv6NIReplyNOOP - IPv6 address without hint => understood as string (internal)
[34m[1mpassed[0m 0969548F 000.00s ICMPv6NIReplyNOOP - IPv6 address without hint => understood as string
[34m[1mpassed[0m BFD5487C 000.00s ICMPv6NIReplyNOOP - IPv4 address without hint => understood as string (internal)
[34m[1mpassed[0m C13935F3 000.00s ICMPv6NIReplyNOOP - IPv4 address without hint => understood as string
[34m[1mpassed[0m 0D81A049 000.00s ICMPv6NIReplyName - single label DNS name as a rawing (without ttl) (internal)
[34m[1mpassed[0m 3C53E327 000.00s ICMPv6NIReplyName - single label DNS name as a rawing (without ttl)
[34m[1mpassed[0m 609A42C2 000.00s ICMPv6NIReplyName - fqdn name as a rawing (without ttl) (internal)
[34m[1mpassed[0m 8A8C7EEE 000.00s ICMPv6NIReplyName - fqdn name as a rawing (without ttl)
[34m[1mpassed[0m D3374243 000.00s ICMPv6NIReplyName - list of 2 single label DNS names (without ttl) (internal)
[34m[1mpassed[0m 0D040755 000.00s ICMPv6NIReplyName - list of 2 single label DNS names (without ttl)
[34m[1mpassed[0m 91AFC664 000.00s ICMPv6NIReplyName - [ttl, single-label, single-label, fqdn] (internal)
[34m[1mpassed[0m F1959693 000.00s ICMPv6NIReplyName - [ttl, single-label, single-label, fqdn]
[34m[1mpassed[0m A62F555E 000.00s ICMPv6NIReplyName - dissection
[34m[1mpassed[0m 0327B8D1 000.00s ICMPv6NIReplyIPv6 - one IPv6 address without TTL (internal)
[34m[1mpassed[0m 5BE7931B 000.00s ICMPv6NIReplyIPv6 - one IPv6 address without TTL
[34m[1mpassed[0m F06FE01C 000.00s ICMPv6NIReplyIPv6 - one IPv6 address without TTL (as a list)  (internal)
[34m[1mpassed[0m 48D51A67 000.00s ICMPv6NIReplyIPv6 - one IPv6 address without TTL (as a list)
[34m[1mpassed[0m DF725CF6 000.00s ICMPv6NIReplyIPv6 - one IPv6 address with TTL  (internal)
[34m[1mpassed[0m C1D13295 000.00s ICMPv6NIReplyIPv6 - one IPv6 address with TTL
[34m[1mpassed[0m 5296D121 000.00s ICMPv6NIReplyIPv6 - two IPv6 addresses as a list of rawings (without TTL) (internal)
[34m[1mpassed[0m 888F2159 000.00s ICMPv6NIReplyIPv6 - two IPv6 addresses as a list of rawings (without TTL)
[34m[1mpassed[0m 92CA19B9 000.00s ICMPv6NIReplyIPv6 - two IPv6 addresses as a list (first with ttl, second without) (internal)
[34m[1mpassed[0m 9237D0A0 000.00s ICMPv6NIReplyIPv6 - two IPv6 addresses as a list (first with ttl, second without)
[34m[1mpassed[0m 9486E700 000.00s ICMPv6NIReplyIPv6 - build & dissection
[34m[1mpassed[0m 5955F7E0 000.00s ICMPv6NIReplyIPv4 - one IPv4 address without TTL (internal)
[34m[1mpassed[0m 0CAD9396 000.00s ICMPv6NIReplyIPv4 - one IPv4 address without TTL
[34m[1mpassed[0m 34759FE1 000.00s ICMPv6NIReplyIPv4 - one IPv4 address without TTL (as a list) (internal)
[34m[1mpassed[0m 9BB55A35 000.00s ICMPv6NIReplyIPv4 - one IPv4 address without TTL (as a list)
[34m[1mpassed[0m DC268620 000.00s ICMPv6NIReplyIPv4 - one IPv4 address with TTL (internal)
[34m[1mpassed[0m 6F083881 000.00s ICMPv6NIReplyIPv4 - one IPv4 address with TTL (internal)
[34m[1mpassed[0m 0ED8BCE7 000.00s ICMPv6NIReplyIPv4 - two IPv4 addresses as a list of rawings (without TTL)
[34m[1mpassed[0m 1D320704 000.00s ICMPv6NIReplyIPv4 - two IPv4 addresses as a list of rawings (without TTL) (internal)
[34m[1mpassed[0m 31813DFC 000.00s ICMPv6NIReplyIPv4 - two IPv4 addresses as a list (first with ttl, second without)
[34m[1mpassed[0m 2F24CF43 000.00s ICMPv6NIReplyIPv4 - two IPv4 addresses as a list (first with ttl, second without) (internal)
[34m[1mpassed[0m 446E1292 000.00s ICMPv6NIReplyIPv4 - build & dissection
[34m[1mpassed[0m 2E88C9E1 000.00s ICMPv6NIReplyRefuse - basic instantiation
[34m[1mpassed[0m 67DE51FE 000.00s ICMPv6NIReplyRefuse - basic dissection
[34m[1mpassed[0m C18313EC 000.00s ICMPv6NIReplyUnknown - basic instantiation
[34m[1mpassed[0m 2243DEBA 000.00s ICMPv6NIReplyRefuse - basic dissection
[34m[1mpassed[0m 25F69183 000.00s computeNIGroupAddr
[34m[1mpassed[0m 810CA877 000.00s IPv6ExtHdrFragment - Basic Instantiation
[34m[1mpassed[0m 3523504F 000.00s IPv6ExtHdrFragment - Instantiation with specific values
[34m[1mpassed[0m 50251AD8 000.00s IPv6ExtHdrFragment - Basic Dissection
[34m[1mpassed[0m D7C6213D 000.00s IPv6ExtHdrFragment - Instantiation with specific values
[34m[1mpassed[0m 28BC4D04 000.00s IPv6 - IPv6ExtHdrFragment hashret
[34m[1mpassed[0m 473F0D3F 000.01s fragment6 - test against a long TCP packet with a 1280 MTU
[34m[1mpassed[0m C13258B5 000.01s fragment6 - test against a long TCP packet with a 1280 MTU without fragment header
[34m[1mpassed[0m 4097E05C 000.01s defragment6 - test against a long TCP packet fragmented with a 1280 MTU
[34m[1mpassed[0m D4BF84B5 000.00s defragment6 - test against packets with L2 header
[34m[1mpassed[0m 77F618FA 000.01s defragment6 - test against a large TCP packet fragmented with a 1280 bytes MTU and missing fragments
[34m[1mpassed[0m 517315C1 000.00s defragment6 - test against a TCP packet fragmented with a 800 bytes MTU and missing fragments
[34m[1mpassed[0m 22E57892 000.00s defragment6 - test the packet length
[34m[1mpassed[0m B5119202 000.00s Fake interfaces
[34m[1mpassed[0m E2FA358D 000.00s Route6 - Route6 flushing
[34m[1mpassed[0m 3C829EE5 000.00s Route6 - Route6.route
[34m[1mpassed[0m 90A8DA51 000.00s Route6 - Route6.make_route
[34m[1mpassed[0m 90A05192 000.00s Route6 - Route6.add & Route6.delt
[34m[1mpassed[0m 6C7F3CCC 000.00s Route6 - Route6.ifadd & Route6.ifdel
[34m[1mpassed[0m C5760E37 000.00s IPv6 - utils
[34m[1mpassed[0m 92EB7429 000.00s IPv6 - IPerror6 & UDPerror & _ICMPv6Error
[34m[1mpassed[0m 2255E1EB 000.00s Windows: reset routes properly
[34m[1mpassed[0m 6A54B998 000.00s ICMPv6MLQuery - build & dissection
[34m[1mpassed[0m 8718938D 000.00s Check answers
[34m[1mpassed[0m 52CBEBEA 000.00s ICMPv6MLQuery2 - build & dissection
[34m[1mpassed[0m E2A0E7CE 000.00s ICMPv6MLReport2 - build & dissection
[34m[1mpassed[0m 3C9829B9 000.00s ICMPv6MLReport2 and ICMPv6MLDMultAddrRec - dissection
[34m[1mpassed[0m BEBE583F 000.00s Check answers
[34m[1mpassed[0m 676DD590 000.00s Define test utilities
[34m[1mpassed[0m 6A1F7A15 000.03s Test NDP_Attack_DAD_DoS_via_NS
[34m[1mpassed[0m 04CB506B 000.01s Test NDP_Attack_DAD_DoS_via_NA
[34m[1mpassed[0m 2B24994F 000.01s Test NDP_Attack_NA_Spoofing
[34m[1mpassed[0m FE484B43 000.01s Test NDP_Attack_Kill_Default_Router
[34m[1mpassed[0m F96FBC83 000.01s Test NDP_Attack_Fake_Router
[34m[1mpassed[0m A279F5A4 000.00s Test NDP_Attack_NS_Spoofing
[34m[1mpassed[0m E44AE85E 000.00s in6_getha()
[34m[1mpassed[0m 592778C9 000.00s ICMPv6HAADRequest - build/dissection
[34m[1mpassed[0m 18E6F441 000.00s ICMPv6HAADReply - build/dissection
[34m[1mpassed[0m 3B898003 000.00s ICMPv6HAADRequest / ICMPv6HAADReply - build/dissection
[34m[1mpassed[0m 703155C7 000.00s ICMPv6MPSol - build (default values)
[34m[1mpassed[0m 1F39B49A 000.00s ICMPv6MPSol - dissection (default values)
[34m[1mpassed[0m D5807B21 000.00s ICMPv6MPSol - build
[34m[1mpassed[0m 6C468680 000.00s ICMPv6MPSol - dissection
[34m[1mpassed[0m FF26D9A7 000.00s ICMPv6MPAdv - build (default values)
[34m[1mpassed[0m 9844767F 000.00s ICMPv6MPAdv - dissection (default values)
[34m[1mpassed[0m C8446CFB 000.00s ICMPv6MPAdv - build
[34m[1mpassed[0m A0A65698 000.00s ICMPv6MPAdv - dissection
[34m[1mpassed[0m C2DC6F17 000.00s IPv6ExtHdrRouting - type 2 - build/dissection
[34m[1mpassed[0m 693098A2 000.00s IPv6ExtHdrRouting - type 2 - hashret
[34m[1mpassed[0m BE18A6D5 000.00s MIP6OptBRAdvice - build (default values)
[34m[1mpassed[0m 1F838EDF 000.00s MIP6OptBRAdvice - dissection (default values)
[34m[1mpassed[0m E0633312 000.00s MIP6OptBRAdvice - build
[34m[1mpassed[0m D461A817 000.00s MIP6OptBRAdvice - dissection
[34m[1mpassed[0m 2D3EA9D1 000.00s MIP6OptAltCoA - build (default values)
[34m[1mpassed[0m B2D6DF37 000.00s MIP6OptAltCoA - dissection (default values)
[34m[1mpassed[0m 3FDF4DEF 000.00s MIP6OptAltCoA - build
[34m[1mpassed[0m A6FEC781 000.00s MIP6OptAltCoA - dissection
[34m[1mpassed[0m 9F63513F 000.00s MIP6OptNonceIndices - build (default values)
[34m[1mpassed[0m 62CFAA10 000.00s MIP6OptNonceIndices - dissection (default values)
[34m[1mpassed[0m 29F89A20 000.00s MIP6OptNonceIndices - build
[34m[1mpassed[0m 0A650149 000.00s MIP6OptNonceIndices - dissection
[34m[1mpassed[0m D8650078 000.00s MIP6OptBindingAuthData - build (default values)
[34m[1mpassed[0m D1DB4338 000.00s MIP6OptBindingAuthData - dissection (default values)
[34m[1mpassed[0m AD44FCBE 000.00s MIP6OptBindingAuthData - build
[34m[1mpassed[0m 626B98D7 000.00s MIP6OptBindingAuthData - dissection
[34m[1mpassed[0m 899430EC 000.00s MIP6OptMobNetPrefix - build (default values)
[34m[1mpassed[0m BF944CC7 000.00s MIP6OptMobNetPrefix - dissection (default values)
[34m[1mpassed[0m 4100796A 000.00s MIP6OptMobNetPrefix - build
[34m[1mpassed[0m CB86B6A7 000.00s MIP6OptMobNetPrefix - dissection
[34m[1mpassed[0m FAA9B32E 000.00s MIP6OptLLAddr - basic build
[34m[1mpassed[0m 57BD9C8D 000.00s MIP6OptLLAddr - basic dissection
[34m[1mpassed[0m D2B9FFA2 000.00s MIP6OptLLAddr - build with specific values
[34m[1mpassed[0m DED1F1CA 000.00s MIP6OptLLAddr - dissection with specific values
[34m[1mpassed[0m 3EB82B5B 000.00s MIP6OptMNID - basic build
[34m[1mpassed[0m 0BD909BB 000.00s MIP6OptMNID - basic dissection
[34m[1mpassed[0m BC66CE7D 000.00s MIP6OptMNID - build with specific values
[34m[1mpassed[0m 98E601DF 000.00s MIP6OptMNID - dissection with specific values
[34m[1mpassed[0m 2EA8576B 000.00s MIP6OptMsgAuth - basic build
[34m[1mpassed[0m 4E7DB72B 000.00s MIP6OptMsgAuth - basic dissection
[34m[1mpassed[0m AF7CEF39 000.00s MIP6OptMsgAuth - build with specific values
[34m[1mpassed[0m 8F9664D3 000.00s MIP6OptMsgAuth - dissection with specific values
[34m[1mpassed[0m 1366CFF5 000.00s MIP6OptReplayProtection - basic build
[34m[1mpassed[0m 4E5171DC 000.00s MIP6OptReplayProtection - basic dissection
[34m[1mpassed[0m 2160C672 000.00s MIP6OptReplayProtection - build with specific values
[34m[1mpassed[0m 808820E6 000.00s MIP6OptReplayProtection - dissection with specific values
[34m[1mpassed[0m 00000000 000.00s MIP6OptCGAParams
[34m[1mpassed[0m 00000000 000.00s MIP6OptSignature
[34m[1mpassed[0m 00000000 000.00s MIP6OptHomeKeygenToken
[34m[1mpassed[0m 00000000 000.00s MIP6OptCareOfTestInit
[34m[1mpassed[0m 00000000 000.00s MIP6OptCareOfTest
[34m[1mpassed[0m 6F90C841 000.00s Mobility Options - Automatic Padding - MIP6OptBRAdvice
[34m[1mpassed[0m 81BCBF42 000.00s Mobility Options - Automatic Padding - MIP6OptAltCoA
[34m[1mpassed[0m FB9089F0 000.00s Mobility Options - Automatic Padding - MIP6OptNonceIndices
[34m[1mpassed[0m C2A7CFBF 000.00s Mobility Options - Automatic Padding - MIP6OptBindingAuthData
[34m[1mpassed[0m 0099BB44 000.00s Mobility Options - Automatic Padding - MIP6OptMobNetPrefix
[34m[1mpassed[0m 8144EF0D 000.00s Mobility Options - Automatic Padding - MIP6OptLLAddr
[34m[1mpassed[0m 1907ADCE 000.00s Mobility Options - Automatic Padding - MIP6OptMNID
[34m[1mpassed[0m 085C2EB2 000.00s Mobility Options - Automatic Padding - MIP6OptMsgAuth
[34m[1mpassed[0m 0CFD6125 000.00s Mobility Options - Automatic Padding - MIP6OptReplayProtection
[34m[1mpassed[0m 7B1D075B 000.00s Mobility Options - Automatic Padding - MIP6OptCGAParamsReq
[34m[1mpassed[0m 0CB63ED5 000.00s Mobility Options - Automatic Padding - MIP6OptCGAParams
[34m[1mpassed[0m 55703FC9 000.00s Mobility Options - Automatic Padding - MIP6OptSignature
[34m[1mpassed[0m 8A64A6E7 000.00s Mobility Options - Automatic Padding - MIP6OptHomeKeygenToken
[34m[1mpassed[0m 2EF8FA78 000.00s Mobility Options - Automatic Padding - MIP6OptCareOfTestInit
[34m[1mpassed[0m EA424CA5 000.00s Mobility Options - Automatic Padding - MIP6OptCareOfTest
[34m[1mpassed[0m 343D67A9 000.00s MIP6MH_BRR - Build (default values)
[34m[1mpassed[0m FA10AAFE 000.00s MIP6MH_BRR - Build with specific values
[34m[1mpassed[0m CC0997F9 000.00s MIP6MH_BRR - Basic dissection
[34m[1mpassed[0m 3F85511F 000.00s MIP6MH_BRR - Dissection with specific values
[34m[1mpassed[0m 972AC425 000.00s MIP6MH_BRR / MIP6MH_BU / MIP6MH_BA hashret() and answers()
[34m[1mpassed[0m A074EB35 000.00s MIP6MH_HoTI - Build (default values)
[34m[1mpassed[0m 16F24C0F 000.00s MIP6MH_HoTI - Dissection (default values)
[34m[1mpassed[0m 008E3B60 000.00s MIP6MH_HoTI - Build (specific values)
[34m[1mpassed[0m A0A512FE 000.00s MIP6MH_HoTI - Dissection (specific values)
[34m[1mpassed[0m 1BB92C38 000.00s MIP6MH_CoTI - Build (default values)
[34m[1mpassed[0m 6C3D4668 000.00s MIP6MH_CoTI - Dissection (default values)
[34m[1mpassed[0m CBB62C95 000.00s MIP6MH_CoTI - Build (specific values)
[34m[1mpassed[0m 90C87043 000.00s MIP6MH_CoTI - Dissection (specific values)
[34m[1mpassed[0m 9805A2D8 000.00s MIP6MH_HoT - Build (default values)
[34m[1mpassed[0m 91A2B934 000.00s MIP6MH_HoT - Dissection (default values)
[34m[1mpassed[0m 527EC2C7 000.00s MIP6MH_HoT - Build (specific values)
[34m[1mpassed[0m 9ECE0115 000.00s MIP6MH_HoT - Dissection (specific values)
[34m[1mpassed[0m A78ACF94 000.00s MIP6MH_HoT answers
[34m[1mpassed[0m 10CB707C 000.00s MIP6MH_CoT - Build (default values)
[34m[1mpassed[0m 4103DE62 000.00s MIP6MH_CoT - Dissection (default values)
[34m[1mpassed[0m D1E23B94 000.00s MIP6MH_CoT - Build (specific values)
[34m[1mpassed[0m 9C96522A 000.00s MIP6MH_CoT - Dissection (specific values)
[34m[1mpassed[0m 7AC66C5F 000.00s MIP6MH_BU - build (default values)
[34m[1mpassed[0m CD3B0A32 000.00s MIP6MH_BU - dissection (default values)
[34m[1mpassed[0m F03F99F5 000.00s MIP6MH_BU - build
[34m[1mpassed[0m 48B7FAB6 000.00s MIP6MH_BU - dissection
[34m[1mpassed[0m 4E3A1E0B 000.00s MIP6MH_BA - build
[34m[1mpassed[0m B3EB0DA2 000.00s MIP6MH_BA - dissection
[34m[1mpassed[0m F1A9E8C2 000.00s MIP6MH_BE - build
[34m[1mpassed[0m 7760C958 000.00s MIP6MH_BE - dissection
[34m[1mpassed[0m 3C235418 000.01s get_trace()
[34m[1mpassed[0m 78F9C219 000.00s show()
[34m[1mpassed[0m 698AEC27 000.00s graph()
Campaign CRC=0A701896 in 000.38s SHA=0F500BCA0C6F69639F38534DE2027130394CDBAA
[34m[1mPASSED=499 FAILED=0[0m
[32m━ Loading: test/scapy/layers/ipsec.uts[0m
[34m[1mpassed[0m 24B4490D 000.00s IPv4 / ESP - Transport - NULL - NULL
[31m[1mfailed[0m 5DC0C9E5 000.00s IPv4 / ESP - Transport - DES - NULL
[31m[1mfailed[0m B698A88E 000.00s IPv4 / ESP - Transport - 3DES - NULL
[31m[1mfailed[0m 56DB1A50 000.00s IPv4 / ESP - Transport - AES-CBC - NULL
[31m[1mfailed[0m DDEDEB77 000.00s IPv4 / ESP - Transport - AES-CTR - NULL
[31m[1mfailed[0m C40766DC 000.00s IPv4 / ESP - Transport - Blowfish - NULL
[31m[1mfailed[0m 905CCE66 000.00s IPv4 / ESP - Transport - CAST - NULL
[34m[1mpassed[0m 7B6AF86D 000.00s IPv4 / ESP - Tunnel - NULL - NULL
[31m[1mfailed[0m 3E58B48B 000.00s IPv4 / ESP - Tunnel - DES - NULL
[31m[1mfailed[0m 1FCABAC5 000.00s IPv4 / ESP - Tunnel - 3DES - NULL
[31m[1mfailed[0m 0B7925C4 000.00s IPv4 / ESP - Tunnel - AES-CBC - NULL
[31m[1mfailed[0m F3D7794C 000.00s IPv4 / ESP - Tunnel - AES-CTR - NULL
[31m[1mfailed[0m 1821F9DB 000.00s IPv4 / ESP - Tunnel - Blowfish - NULL
[31m[1mfailed[0m 4E102D03 000.00s IPv4 / ESP - Tunnel - CAST - NULL
[31m[1mfailed[0m 1A66A883 000.00s IPv4 / ESP - Transport - NULL - HMAC-SHA1-96
[31m[1mfailed[0m EF619CD7 000.00s IPv4 / ESP - Transport - NULL - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m A6646F17 000.00s IPv4 / ESP - Transport - NULL - SHA2-256-128
[31m[1mfailed[0m 7DA3C611 000.00s IPv4 / ESP - Transport - NULL - SHA2-256-128 - altered packet
[31m[1mfailed[0m 5C2C2ED2 000.00s IPv4 / ESP - Transport - NULL - SHA2-384-192
[31m[1mfailed[0m 26777B52 000.00s IPv4 / ESP - Transport - NULL - SHA2-384-192 - altered packet
[31m[1mfailed[0m 7F8AFDD2 000.00s IPv4 / ESP - Transport - NULL - SHA2-512-256
[31m[1mfailed[0m DD540E4C 000.00s IPv4 / ESP - Transport - NULL - SHA2-512-256 - altered packet
[31m[1mfailed[0m 929272A1 000.00s IPv4 / ESP - Transport - NULL - HMAC-MD5-96
[31m[1mfailed[0m 1FCA70C6 000.00s IPv4 / ESP - Transport - NULL - HMAC-MD5-96 - altered packet
[31m[1mfailed[0m 92B66874 000.00s IPv4 / ESP - Transport - NULL - AES-CMAC-96
[31m[1mfailed[0m DD0CD0EC 000.00s IPv4 / ESP - Transport - NULL - AES-CMAC-96 - altered packet
[31m[1mfailed[0m 02D48B87 000.00s IPv4 / ESP - Tunnel - NULL - HMAC-SHA1-96
[31m[1mfailed[0m 8FFD2D8C 000.00s IPv4 / ESP - Tunnel - NULL - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 6C64D811 000.00s IPv4 / ESP - Tunnel - NULL - SHA2-256-128
[31m[1mfailed[0m 9F979F4B 000.00s IPv4 / ESP - Tunnel - NULL - SHA2-256-128 - altered packet
[31m[1mfailed[0m 6575E0FC 000.00s IPv4 / ESP - Tunnel - NULL - SHA2-384-192
[31m[1mfailed[0m 125056D6 000.00s IPv4 / ESP - Tunnel - NULL - SHA2-384-192 - altered packet
[31m[1mfailed[0m A0376B52 000.00s IPv4 / ESP - Tunnel - NULL - SHA2-512-256
[31m[1mfailed[0m 06831375 000.00s IPv4 / ESP - Tunnel - NULL - SHA2-512-256 - altered packet
[31m[1mfailed[0m D73E8D9B 000.00s IPv4 / ESP - Tunnel - NULL - HMAC-MD5-96
[31m[1mfailed[0m 1DA43F10 000.00s IPv4 / ESP - Tunnel - NULL - HMAC-MD5-96 - altered packet
[31m[1mfailed[0m 175BD7AD 000.00s IPv4 / ESP - Tunnel - NULL - AES-CMAC-96
[31m[1mfailed[0m 734C9DED 000.00s IPv4 / ESP - Tunnel - NULL - AES-CMAC-96 - altered packet
[31m[1mfailed[0m 4848AC05 000.00s IPv4 / ESP - Transport - AES-CBC - HMAC-SHA1-96
[31m[1mfailed[0m A21B6201 000.00s IPv4 / ESP - Transport - AES-CBC - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 75FADB28 000.00s IPv4 / ESP - Transport - AES-GCM - NULL
[31m[1mfailed[0m 07B06129 000.00s IPv4 / ESP - Transport - AES-GCM - NULL -- ESN
[31m[1mfailed[0m 42C1A67E 000.00s IPv4 / ESP - Transport - AES-GCM - NULL - altered packet
[31m[1mfailed[0m A6C17CD7 000.00s IPv4 / ESP - Transport - AES-GCM - NULL - altered packet -- ESN
[31m[1mfailed[0m 07693232 000.00s IPv4 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96
[31m[1mfailed[0m 2B8BF2A3 000.00s IPv4 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m ED13B1FA 000.00s IPv4 / ESP - Tunnel - AES-GCM - NULL
[31m[1mfailed[0m A2EC0094 000.00s IPv4 / ESP - Tunnel - AES-GCM - NULL -- ESN
[31m[1mfailed[0m 153E8605 000.00s IPv4 / ESP - Tunnel - AES-GCM - NULL - altered packet
[31m[1mfailed[0m 4E79BCA4 000.00s IPv4 / ESP - Tunnel - AES-GCM - NULL - altered packet - ESN
[31m[1mfailed[0m D86D8159 000.00s IPv4 / AH - Transport - HMAC-SHA1-96
[31m[1mfailed[0m 7D64CAF0 000.00s IPv4 / AH - Transport - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 78E6D38F 000.00s IPv4 / AH - Transport - SHA2-256-128
[31m[1mfailed[0m 77E1AC83 000.00s IPv4 / AH - Transport - SHA2-256-128 - altered packet
[31m[1mfailed[0m 49FC872C 000.00s IPv4 / AH - Transport - SHA2-384-192
[31m[1mfailed[0m 3BD8E906 000.00s IPv4 / AH - Transport - SHA2-384-192 - altered packet
[31m[1mfailed[0m 1588EE64 000.00s IPv4 / AH - Transport - SHA2-512-256
[31m[1mfailed[0m B855FF3C 000.00s IPv4 / AH - Transport - SHA2-512-256 - altered packet
[31m[1mfailed[0m 3A8EA8D8 000.00s IPv4 / AH - Transport - HMAC-MD5-96
[31m[1mfailed[0m 8A48C696 000.00s IPv4 / AH - Transport - HMAC-MD5-96 - altered packet
[31m[1mfailed[0m 1540D01D 000.00s IPv4 / AH - Transport - AES-CMAC-96
[31m[1mfailed[0m C911A71A 000.00s IPv4 / AH - Transport - AES-CMAC-96 - altered packet
[31m[1mfailed[0m F26E4BF1 000.00s IPv4 / AH - Transport - AES-CMAC-96 -- ESN
[31m[1mfailed[0m DC321F0D 000.00s IPv4 / AH - Transport - AES-CMAC-96 - altered packet -- ESN
[31m[1mfailed[0m 09A104C9 000.00s IPv4 / AH - Tunnel - HMAC-SHA1-96
[31m[1mfailed[0m 39E2E5B7 000.00s IPv4 / AH - Tunnel - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 28FF2E80 000.00s IPv4 / AH - Tunnel - SHA2-256-128
[31m[1mfailed[0m 6E37F1DE 000.00s IPv4 / AH - Tunnel - SHA2-256-128 - altered packet
[31m[1mfailed[0m 6E1D4A87 000.00s IPv4 / AH - Tunnel - SHA2-384-192
[31m[1mfailed[0m 7A43B237 000.00s IPv4 / AH - Tunnel - SHA2-384-192 - altered packet
[31m[1mfailed[0m BBEEA0A7 000.00s IPv4 / AH - Tunnel - SHA2-512-256
[31m[1mfailed[0m 7F997001 000.00s IPv4 / AH - Tunnel - SHA2-512-256 - altered packet
[31m[1mfailed[0m 6AB37C50 000.00s IPv4 / AH - Tunnel - HMAC-MD5-96
[31m[1mfailed[0m D9057270 000.00s IPv4 / AH - Tunnel - HMAC-MD5-96 - altered packet
[31m[1mfailed[0m 4242F820 000.00s IPv4 / AH - Tunnel - AES-CMAC-96
[31m[1mfailed[0m 91D9637D 000.00s IPv4 / AH - Tunnel - AES-CMAC-96 - altered packet
[31m[1mfailed[0m 8D59B720 000.00s IPv4 / AH - Tunnel - AES-CMAC-96 -- ESN
[31m[1mfailed[0m 43DEF47F 000.00s IPv4 / AH - Tunnel - AES-CMAC-96 - altered packet -- ESN
[34m[1mpassed[0m 249C7565 000.00s IPv6 / ESP - Transport - NULL - NULL
[31m[1mfailed[0m AA2CB292 000.00s IPv6 / ESP - Transport - AES-CBC - NULL
[31m[1mfailed[0m 907998DC 000.00s IPv6 / ESP - Transport - NULL - HMAC-SHA1-96
[31m[1mfailed[0m D0E4F3B8 000.00s IPv6 / ESP - Transport - NULL - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 26F073EB 000.00s IPv6 / ESP - Transport - AES-CBC - HMAC-SHA1-96
[31m[1mfailed[0m E7542481 000.00s IPv6 / ESP - Transport - AES-CBC - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 4D2FA934 000.00s IPv6 / ESP - Transport - AES-GCM - NULL
[31m[1mfailed[0m 084E3561 000.00s IPv6 / ESP - Transport - AES-GCM - NULL - altered packet
[34m[1mpassed[0m 1FB80F1E 000.00s IPv6 / ESP - Tunnel - NULL - NULL
[31m[1mfailed[0m E8AAAFDC 000.00s IPv6 / ESP - Tunnel - AES-CBC - NULL
[31m[1mfailed[0m B3D27143 000.00s IPv6 / ESP - Tunnel - NULL - HMAC-SHA1-96
[31m[1mfailed[0m A19E6E9B 000.00s IPv6 / ESP - Tunnel - NULL - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m DFE80438 000.00s IPv6 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96
[31m[1mfailed[0m F55880D0 000.00s IPv6 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m EB354950 000.00s IPv6 / ESP - Tunnel - AES-GCM - NULL
[31m[1mfailed[0m A202712C 000.00s IPv6 / ESP - Tunnel - AES-GCM - NULL - altered packet
[31m[1mfailed[0m FDA2E817 000.00s IPv6 / AH - Transport - HMAC-SHA1-96
[31m[1mfailed[0m F33DA747 000.00s IPv6 / AH - Transport - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 9225F982 000.00s IPv6 / AH - Transport - SHA2-256-128
[31m[1mfailed[0m D072995D 000.00s IPv6 / AH - Transport - SHA2-256-128 - altered packet
[31m[1mfailed[0m 01E20299 000.00s IPv6 / AH - Tunnel - HMAC-SHA1-96
[31m[1mfailed[0m 8AF6D12E 000.00s IPv6 / AH - Tunnel - HMAC-SHA1-96 - altered packet
[31m[1mfailed[0m 1571C4A6 000.00s IPv6 / AH - Tunnel - SHA2-256-128
[31m[1mfailed[0m DB37FA82 000.00s IPv6 / AH - Tunnel - SHA2-256-128 - altered packet
[31m[1mfailed[0m 4BE1DF5D 000.00s IPv6 + Extensions / AH - Transport
[31m[1mfailed[0m 7CD6E93E 000.00s IPv6 + Routing Header / AH - Transport
Campaign CRC=4549386E in 000.17s SHA=7B5FAD730D4ED9959593C6202F79018D7D8E4930
[31m[1mPASSED=4 FAILED=100[0m
[32m━ Loading: test/scapy/layers/isakmp.uts[0m
[34m[1mpassed[0m 0996C047 000.00s ISAKMP creation
[34m[1mpassed[0m 13E7F83A 000.00s ISAKMP manipulation
[34m[1mpassed[0m 75894D40 000.00s ISAKMP assembly
[34m[1mpassed[0m AAE066B0 000.00s ISAKMP disassembly
Campaign CRC=A5EC2298 in 000.01s SHA=ED978D58FA2269BB71187A1A98A5BE0C91807560
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/scapy/layers/l2.uts[0m
[31m[1mfailed[0m 36466FAA 000.00s Test ARPingResult output
[34m[1mpassed[0m 8D22216F 000.00s STP - Basic Instantiation
[34m[1mpassed[0m AA3BE87F 000.00s STP - Basic Dissection
[34m[1mpassed[0m 21257BAD 000.00s Simple Ether() / ARP() show
[34m[1mpassed[0m AFE513E9 000.00s ARP for IPv4
[34m[1mpassed[0m A8F2D976 000.00s ARP for IPv6
[34m[1mpassed[0m 5EEB24C2 000.00s Dummy ARP
Campaign CRC=FD7247D5 in 000.01s SHA=E020F39BF2BBF302A5F4C3FC6D9E2531F339E6DA
[31m[1mPASSED=6 FAILED=1[0m
[32m━ Loading: test/scapy/layers/l2tp.uts[0m
[34m[1mpassed[0m 2CF8D04B 000.00s L2TP - build
[34m[1mpassed[0m 6BDF4376 000.00s L2TP - dissection
Campaign CRC=143873BA in 000.00s SHA=A2C296DD67AB895478EDB7D966453A21B051AEF1
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/scapy/layers/ldap.uts[0m
[34m[1mpassed[0m D8C5FC33 000.00s Load LDAP
[34m[1mpassed[0m 02DBB16C 000.00s LDAP_UnbindRequest
[34m[1mpassed[0m 881EFE87 000.00s LDAP_BindRequest
[34m[1mpassed[0m B63B357B 000.00s LDAP_BindResponse
[34m[1mpassed[0m E8463FE4 000.00s LDAP_SearchRequest
[34m[1mpassed[0m 0FC4B2C6 000.01s LDAP_SearchResponse
[34m[1mpassed[0m 873E04C9 000.00s Basic CLDAP dissection & build test
[34m[1mpassed[0m 0EBD4BFC 000.00s More advanced CLDAP dissection & build test
Campaign CRC=BFDFB4C6 in 000.04s SHA=D289483528D9FA4777D96EA02BE596BF3A93A410
[34m[1mPASSED=8 FAILED=0[0m
[32m━ Loading: test/scapy/layers/llmnr.uts[0m
[34m[1mpassed[0m 6C984879 000.00s Simple packet dissection
[34m[1mpassed[0m 42549DE9 000.00s Packet build / dissection
[34m[1mpassed[0m 38C132CD 000.00s Answers - building
[34m[1mpassed[0m F1258B96 000.00s Answers - dissecting
Campaign CRC=7A069644 in 000.00s SHA=3B1FCDCDB388C22A08AA7AA652C06A717289DBC0
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/scapy/layers/lltd.uts[0m
[34m[1mpassed[0m 99984E6C 000.00s Simple packet dissection
[34m[1mpassed[0m 79D94FA3 000.00s Packet build / dissection
[34m[1mpassed[0m 077B6E6C 000.02s Attribute build / dissection
[34m[1mpassed[0m 8512CA50 000.00s Large TLV
Campaign CRC=D774E13F in 000.02s SHA=7ADF863D7496C08F7CFD17440862176919782D00
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/scapy/layers/mgcp.uts[0m
[34m[1mpassed[0m 5B4119BB 000.00s MGCP - build
[34m[1mpassed[0m A0ED03AF 000.00s MGCP - dissect
Campaign CRC=12D768A8 in 000.00s SHA=FFE6B99B6805F15DD4D36F390A3922C99BCFE604
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/scapy/layers/mobileip.uts[0m
[34m[1mpassed[0m E653E518 000.00s MobileIP - build
[34m[1mpassed[0m A735736A 000.00s MobileIP - dissect
Campaign CRC=84239F45 in 000.00s SHA=89D0098ABA1598654C50D3ACA3D0630C08B2C950
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/scapy/layers/netbios.uts[0m
[34m[1mpassed[0m 618A23C5 000.00s NBNSQueryRequest - build & dissect
[34m[1mpassed[0m 6245A284 000.00s NBNSQueryResponse - build & dissect
[34m[1mpassed[0m 872131DA 000.00s NBNSNodeStatusResponse - build & dissect
[34m[1mpassed[0m A3DD20CC 000.00s NBNSWackResponse - build & dissect
[34m[1mpassed[0m 741E538B 000.00s NBTSession
Campaign CRC=5C2365AF in 000.01s SHA=1E19C444F18C8AA0BEE89A8B71A73D7ABA1C6AEB
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/scapy/layers/netflow.uts[0m
[34m[1mpassed[0m FAA2CA0C 000.00s NetflowHeaderV5 - basic building
[34m[1mpassed[0m AA93666E 000.00s NetflowHeaderV5 - UDP bindings
[34m[1mpassed[0m 4C3D693B 000.00s NetflowHeaderV5 - basic dissection
[34m[1mpassed[0m 86E34794 000.01s NetflowV9 - advanced dissection
[34m[1mpassed[0m E3C15092 000.01s NetflowV9 - Multiple FlowSets in one packet
[34m[1mpassed[0m FF4E9241 000.01s NetflowV9 - build and dissection
[34m[1mpassed[0m 9FC287A9 000.01s NetflowV9 - advanced build
[34m[1mpassed[0m DC95D31B 000.00s NetflowV9 - padding #GH2257
[34m[1mpassed[0m 18BDF888 000.01s IPFix dissection
[34m[1mpassed[0m F0F3B7D8 000.00s NetflowV10/IPFIX - dissection without padding (GH3101)
[34m[1mpassed[0m 9B964405 000.01s NetflowV10/IPFIX - build
[34m[1mpassed[0m 69B9B08E 000.01s NetflowSession - dissect packet NetflowV9 packets on-the-flow
Campaign CRC=6DE6D4F2 in 000.06s SHA=1EB756C296CFE91C81984BA14A5CC86209561297
[34m[1mPASSED=12 FAILED=0[0m
[32m━ Loading: test/scapy/layers/ntp.uts[0m
[34m[1mpassed[0m B1C374EB 000.00s specific haslayer and getlayer implementations for NTP
[34m[1mpassed[0m F9C30AE6 000.00s NTP - Layers (1)
[34m[1mpassed[0m A688B3D2 000.00s NTP - Layers (2)
[34m[1mpassed[0m 54C8D404 000.00s NTP - sessions (1)
[34m[1mpassed[0m FC3E08F7 000.00s NTP - sessions (2)
[34m[1mpassed[0m D9DAEC57 000.00s NTPHeader - Basic checks
[34m[1mpassed[0m B3767822 000.00s NTPHeader - Dissection
[34m[1mpassed[0m D936F900 000.00s NTPHeader - High precision
[34m[1mpassed[0m 4041DAF6 000.00s NTPHeader - KoD
[34m[1mpassed[0m 6C1023E6 000.00s NTPHeader - Extension dissection test
[34m[1mpassed[0m 9BDAC2CB 000.00s NTPAuthenticator
[34m[1mpassed[0m 8E52EA3E 000.00s NTP Control (mode 6) - CTL_OP_READSTAT (1) - request
[34m[1mpassed[0m 00C5F27E 000.00s NTP Control (mode 6) - CTL_OP_READSTAT (2) - response
[34m[1mpassed[0m 1A0E91F0 000.00s NTP Control (mode 6) - CTL_OP_READVAR (1) - request
[34m[1mpassed[0m 9F829D49 000.00s NTP Control (mode 6) - CTL_OP_READVAR (2) - response (1st packet)
[34m[1mpassed[0m BF408546 000.00s NTP Control (mode 6) - CTL_OP_READVAR (3) - response (2nd packet)
[34m[1mpassed[0m 1EFDEFC7 000.00s NTP Control (mode 6) - CTL_OP_READVAR (4) - request
[34m[1mpassed[0m F2B0A946 000.00s NTP Control (mode 6) - CTL_OP_READVAR (5) - response
[34m[1mpassed[0m 97E33559 000.00s NTP Control (mode 6) - CTL_OP_WRITEVAR (1) - request
[34m[1mpassed[0m 2BFD342E 000.00s NTP Control (mode 6) - CTL_OP_WRITEVAR (2) - response
[34m[1mpassed[0m FE2E8C22 000.00s NTP Control (mode 6) - CTL_OP_CONFIGURE (1) - request
[34m[1mpassed[0m 62421E0C 000.00s NTP Control (mode 6) - CTL_OP_CONFIGURE (2) - response
[34m[1mpassed[0m B445626A 000.00s NTP Control (mode 6) - CTL_OP_SAVECONFIG (1) - request
[34m[1mpassed[0m 6815F357 000.00s NTP Control (mode 6) - CTL_OP_SAVECONFIG (2) - response
[34m[1mpassed[0m C2B02B28 000.00s NTP Control (mode 6) - CTL_OP_REQ_NONCE (1) - request
[34m[1mpassed[0m DA8FF895 000.00s NTP Control (mode 6) - CTL_OP_REQ_NONCE (2) - response
[34m[1mpassed[0m 0163F7D3 000.00s NTP Control (mode 6) - CTL_OP_READ_MRU (1) - request
[34m[1mpassed[0m 9B6D8557 000.00s NTP Control (mode 6) - CTL_OP_READ_MRU (2) - response
[34m[1mpassed[0m 56372637 000.00s NTP Private (mode 7) - error - Dissection
[34m[1mpassed[0m 247F5CDB 000.00s NTP Private (mode 7) - REQ_PEER_LIST (1) - request
[34m[1mpassed[0m 78D0747A 000.00s NTP Private (mode 7) - REQ_PEER_LIST (2) - response
[34m[1mpassed[0m 0840EF23 000.00s NTP Private (mode 7) - REQ_PEER_INFO (1) - request
[34m[1mpassed[0m 710D4E41 000.00s NTP Private (mode 7) - REQ_PEER_INFO (2) - response
[34m[1mpassed[0m CD02FB1C 000.00s NTP Private (mode 7) - REQ_PEER_LIST_SUM (1) - request
[34m[1mpassed[0m 5BCA7296 000.00s NTP Private (mode 7) - REQ_PEER_LIST_SUM (2) - response (1st packet)
[34m[1mpassed[0m DF4F17DE 000.00s NTP Private (mode 7) - REQ_PEER_LIST_SUM (3) - response (2nd packet)
[34m[1mpassed[0m CA8435DE 000.00s NTP Private (mode 7) - REQ_PEER_LIST_SUM (3) - response (3rd packet)
[34m[1mpassed[0m 88B90085 000.00s NTP Private (mode 7) - REQ_PEER_STATS (1) - request
[34m[1mpassed[0m 5619343D 000.00s NTP Private (mode 7) - REQ_PEER_STATS (2) - response
[34m[1mpassed[0m 1BB8ADED 000.00s NTP Private (mode 7) - REQ_SYS_INFO (1) - request
[34m[1mpassed[0m 81BDD772 000.00s NTP Private (mode 7) - REQ_SYS_INFO (2) - response
[34m[1mpassed[0m 74F9EA12 000.00s NTP Private (mode 7) - REQ_SYS_STATS (1) - request
[34m[1mpassed[0m 031514A6 000.00s NTP Private (mode 7) - REQ_SYS_STATS (2) - response
[34m[1mpassed[0m 562473ED 000.00s NTP Private (mode 7) - REQ_IO_STATS (1) - request
[34m[1mpassed[0m F270BB43 000.00s NTP Private (mode 7) - REQ_IO_STATS (2) - response
[34m[1mpassed[0m 486F04B8 000.00s NTP Private (mode 7) - REQ_MEM_STATS (1) - request
[34m[1mpassed[0m 7CEB692C 000.00s NTP Private (mode 7) - REQ_MEM_STATS (2) - response
[34m[1mpassed[0m E1C4FABB 000.00s NTP Private (mode 7) - REQ_LOOP_INFO (1) - request
[34m[1mpassed[0m CF9B748D 000.00s NTP Private (mode 7) - REQ_LOOP_INFO (2) - response
[34m[1mpassed[0m 4A245500 000.00s NTP Private (mode 7) - REQ_TIMER_STATS (1) - request
[34m[1mpassed[0m 7DA66EB9 000.00s NTP Private (mode 7) - REQ_TIMER_STATS (2) - response
[34m[1mpassed[0m B1F55138 000.00s NTP Private (mode 7) - REQ_CONFIG (1) - request
[34m[1mpassed[0m 39838024 000.00s NTP Private (mode 7) - REQ_CONFIG (2) - response
[34m[1mpassed[0m 349B6287 000.00s NTP Private (mode 7) - REQ_UNCONFIG (1) - request
[34m[1mpassed[0m E7CE6E6B 000.00s NTP Private (mode 7) - REQ_UNCONFIG (2) - response
[34m[1mpassed[0m 0734495C 000.00s NTP Private (mode 7) - REQ_RESADDFLAGS (1) - request
[34m[1mpassed[0m 43F73610 000.00s NTP Private (mode 7) - REQ_RESSUBFLAGS (1) - request
[34m[1mpassed[0m 88CD283B 000.00s NTP Private (mode 7) - REQ_RESET_PEER (1) - request
[34m[1mpassed[0m 0D0E240E 000.00s NTP Private (mode 7) - REQ_AUTHINFO (1) - response
[34m[1mpassed[0m F3253F1E 000.00s NTP Private (mode 7) - REQ_ADD_TRAP (1) - request
[34m[1mpassed[0m 5A94C7DE 000.00s NTP Private (mode 7) - REQ_ADD_TRAP (2) - response
[34m[1mpassed[0m DAC730B1 000.00s NTP Private (mode 7) - REQ_CLR_TRAP (1) - request
[34m[1mpassed[0m 2EE09A3B 000.00s NTP Private (mode 7) - REQ_CLR_TRAP (2) - response
[34m[1mpassed[0m 42FB635C 000.00s NTP Private (mode 7) - REQ_GET_CTLSTATS - response
[34m[1mpassed[0m 454A0EA1 000.00s NTP Private (mode 7) - REQ_GET_KERNEL (1) - request
[34m[1mpassed[0m 92E8D12C 000.00s NTP Private (mode 7) - REQ_GET_KERNEL (2) - response
[34m[1mpassed[0m CB98A241 000.00s NTP Private (mode 7) - REQ_MON_GETLIST_1 (1) - request
[34m[1mpassed[0m FBFE67FA 000.00s NTP Private (mode 7) - REQ_MON_GETLIST_1 (2) - response
[34m[1mpassed[0m 210E7FC1 000.00s NTP Private (mode 7) - REQ_IF_STATS (1) - request
[34m[1mpassed[0m 27051134 000.00s NTP Private (mode 7) - REQ_IF_STATS (2) - response
[34m[1mpassed[0m 52D78B89 000.00s NTP Private (mode 7) - REQ_IF_STATS (3) - response
[34m[1mpassed[0m B23BD302 000.00s NTP Private (mode 7) - REQ_IF_RELOAD (1) - request
[34m[1mpassed[0m F61C4A71 000.00s NTP Private (mode 7) - REQ_IF_RELOAD (2) - response
Campaign CRC=588D7E9F in 000.06s SHA=B8937ACE9ED2D6269CAF6F1407B6930F750D9E14
[34m[1mPASSED=73 FAILED=0[0m
[32m━ Loading: test/scapy/layers/pflog.uts[0m
[34m[1mpassed[0m 70336DF9 000.00s Load module
[34m[1mpassed[0m 0732D6A0 000.00s Dissect PFLog packet of a IP()/TCP() dropped packet
[34m[1mpassed[0m 02CFE070 000.00s Dissect PFLog packet of a IP()/UDP() dropped packet
[34m[1mpassed[0m 8DE73CBE 000.00s Dissect PFLog packet of a IP()/ICMP() echo-request dropped packet
[34m[1mpassed[0m 1FFCF54E 000.00s Dissect PFLog packet of a IPv6()/TCP() dropped packet
[34m[1mpassed[0m D956AB2B 000.00s Dissect PFLog packet of a IPv6()/TCP() passed packet
[34m[1mpassed[0m 4D0D9924 000.00s Dissect PFLog packet of a IPv6()/UDP() dropped packet
[34m[1mpassed[0m E8E8A910 000.00s Dissect PFLog packet of a IPv6()/ICMP6() dropped packet
[34m[1mpassed[0m BBA64F63 000.00s Dissect PFLog packet of a IPv6()/ICMP6() passed packet
Campaign CRC=885A30E9 in 000.01s SHA=B414BC6A90B3FF72B9A753ECE93D46F08B1F2793
[34m[1mPASSED=9 FAILED=0[0m
[32m━ Loading: test/scapy/layers/ppp.uts[0m
[34m[1mpassed[0m 6851222B 000.00s PPPoE
[34m[1mpassed[0m B6A5A382 000.00s PPPoE with padding
[34m[1mpassed[0m CD4992FF 000.00s PPP/HDLC
[34m[1mpassed[0m 53649A26 000.00s PPP IPCP
[34m[1mpassed[0m D6E5EC61 000.00s PPP ECP
[34m[1mpassed[0m 6C69C2E0 000.00s PPP with only one byte for protocol
Campaign CRC=0881A166 in 000.01s SHA=4B66EBE31CE395637CC8C758B6B7123ACD83D978
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/scapy/layers/pptp.uts[0m
[34m[1mpassed[0m 6EFF2540 000.00s Test IP/GRE v0 decoding
[34m[1mpassed[0m 9E2D0288 000.00s Test IP/GRE v1 decoding with PPP LCP
[34m[1mpassed[0m 1D85559C 000.00s Test IP/GRE v1 encoding/decoding with PPP LCP Echo
[34m[1mpassed[0m A9CFFD76 000.00s Test LCP Echo Request / Reply
[34m[1mpassed[0m 6755A821 000.00s Test LCP Configure Request
[34m[1mpassed[0m 625ED6EB 000.00s Test LCP Configure Ack
[34m[1mpassed[0m 2A150CEB 000.00s Test LCP Configure Nak
[34m[1mpassed[0m F5665338 000.00s Test LCP Configure Reject
[34m[1mpassed[0m C66ED592 000.00s Test LCP Configure options
[34m[1mpassed[0m 1FAB0BB1 000.00s Test LCP Auth option
[34m[1mpassed[0m D8825501 000.00s Test LCP Code-Reject
[34m[1mpassed[0m 78DFBBA4 000.00s Test LCP Protocol-Reject
[34m[1mpassed[0m 870294C7 000.00s Test LCP Discard Request
[34m[1mpassed[0m 584C7AE1 000.00s Test LCP Terminate-Request/Terminate-Ack
[34m[1mpassed[0m D9FED231 000.00s Test PPP PAP Request
[34m[1mpassed[0m 36B756A4 000.00s Test PPP PAP Authenticate-Ack
[34m[1mpassed[0m C0AFFCCE 000.00s Test PPP PAP Authenticate-Nak
[34m[1mpassed[0m D8483E17 000.00s Test PPP CHAP Challenge
[34m[1mpassed[0m 0F6EEE34 000.00s Test PPP CHAP Response
[34m[1mpassed[0m 0B028577 000.00s Test PPP CHAP Success
[34m[1mpassed[0m 2594D84E 000.00s Test PPP CHAP Failure
[34m[1mpassed[0m B44E36D2 000.00s Test PPTP Start-Control-Connection-Request
[34m[1mpassed[0m ADA50819 000.00s Test PPTP Start-Control-Connection-Reply
[34m[1mpassed[0m DE3D1768 000.00s Test PPTP Stop-Control-Connection-Request
[34m[1mpassed[0m 0CD7142B 000.00s Test PPTP Stop-Control-Connection-Reply
[34m[1mpassed[0m 06FAA0BD 000.00s Test PPTP Echo-Request
[34m[1mpassed[0m 80AF2CB5 000.00s Test PPTP Echo-Reply
[34m[1mpassed[0m 4AD76384 000.00s Test PPTP Outgoing-Call-Request
[34m[1mpassed[0m 71E948C8 000.00s Test PPTP Outgoing-Call-Reply
[34m[1mpassed[0m B2E32729 000.00s Test PPTP Incoming-Call-Request
[34m[1mpassed[0m 5E58E216 000.00s Test PPTP Incoming-Call-Reply
[34m[1mpassed[0m 81441A17 000.00s Test PPTP Incoming-Call-Connected
[34m[1mpassed[0m 13FF9ECF 000.00s Test PPTP Call-Clear-Request
[34m[1mpassed[0m DE4636EE 000.00s Test PPTP Call-Disconnect-Notify
[34m[1mpassed[0m 2018BB75 000.00s Test PPTP WAN-Error-Notify
[34m[1mpassed[0m 27E04195 000.00s Test PPTP Set-Link-Info
Campaign CRC=04CFAAD5 in 000.04s SHA=7C9BC886B5AE3E57327FFE58535CA4FB1797FD5F
[34m[1mPASSED=36 FAILED=0[0m
[32m━ Loading: test/scapy/layers/radius.uts[0m
[34m[1mpassed[0m 124121DB 000.00s IP/UDP/RADIUS - Build
[34m[1mpassed[0m 5444466F 000.00s IP/UDP/RADIUS - Dissection
[34m[1mpassed[0m 2717B4CB 000.00s RADIUS - Access-Request - Dissection (1)
[34m[1mpassed[0m 9550873D 000.00s RADIUS - compute_message_authenticator()
[34m[1mpassed[0m 5406EA6B 000.00s RADIUS - Access-Challenge - Dissection (2)
[34m[1mpassed[0m 54541CB1 000.00s RADIUS - Access-Request - Dissection (3)
[34m[1mpassed[0m D68CDF3D 000.00s RADIUS - Access-Challenge - Dissection (4)
[34m[1mpassed[0m E5F41CCF 000.00s RADIUS - Response Authenticator computation
[34m[1mpassed[0m D3563405 000.00s RADIUS - Layers (1)
[34m[1mpassed[0m DE55C66A 000.00s RADIUS - sessions (1)
[34m[1mpassed[0m 11C5BF97 000.00s RADIUS - sessions (2)
[34m[1mpassed[0m F08473B8 000.00s Issue GH#1407
[34m[1mpassed[0m D4D6BA76 000.00s RADIUS - attributes with IPv4 addresses
[34m[1mpassed[0m 6465787F 000.00s Radius - fragmented EAP - GH2832
[34m[1mpassed[0m A6A57568 000.00s RadiusAttr_User_Password
Campaign CRC=045727F1 in 000.02s SHA=A2654B9C48E68E089AE54F86934FCB5C8C82AA9B
[34m[1mPASSED=15 FAILED=0[0m
[32m━ Loading: test/scapy/layers/rip.uts[0m
[34m[1mpassed[0m 3A6A3B66 000.00s RIP - build
[34m[1mpassed[0m 34293B14 000.00s RIP - UDP bindings
[34m[1mpassed[0m E6AB8522 000.00s RIP - dissection
Campaign CRC=37F63DB6 in 000.00s SHA=2FF376083CD35FF6304A39EF36883E7F6A138E87
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/scapy/layers/rtp.uts[0m
[34m[1mpassed[0m 324C5C42 000.00s test rtp with extension header
[34m[1mpassed[0m 909F8468 000.00s test layer creation
[34m[1mpassed[0m 1FF3ADC0 000.00s test RTP without extension
Campaign CRC=BB198A8B in 000.00s SHA=BCB203F54B868CDF9727AF5FF0A1A2C849F966CA
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/scapy/layers/sctp.uts[0m
[34m[1mpassed[0m D987AE51 000.00s SCTP - Chunk Init - build
[34m[1mpassed[0m 1F806BCF 000.00s SCTP - Chunk Init - dissection
[34m[1mpassed[0m 56F2812B 000.00s SCTP - SCTPChunkSACK - build
[34m[1mpassed[0m B85A0B9D 000.00s SCTP - SCTPChunkSACK - dissection
[34m[1mpassed[0m 6FDB8476 000.00s SCTP - answers
[34m[1mpassed[0m 4E020F3E 000.00s SCTP basic header - Dissection
[34m[1mpassed[0m 393C051D 000.00s basic SCTPChunkData - Dissection
[34m[1mpassed[0m 70F05259 000.00s basic SCTPChunkInit - Dissection
[34m[1mpassed[0m 68276168 000.00s SCTPChunkInit multiple valid parameters - Dissection
[34m[1mpassed[0m 211E0DAF 000.00s basic SCTPChunkInitAck - Dissection
[34m[1mpassed[0m 3BF3CCEF 000.00s SCTPChunkInitAck with state cookie - Dissection
[34m[1mpassed[0m A2FC3292 000.00s basic SCTPChunkSACK - Dissection
[34m[1mpassed[0m 5A0FB4F7 000.00s basic SCTPChunkHeartbeatReq - Dissection
[34m[1mpassed[0m 6D5A80EB 000.00s basic SCTPChunkHeartbeatAck - Dissection
[34m[1mpassed[0m 66CE6C9F 000.00s basic SCTPChunkAbort - Dissection
[34m[1mpassed[0m 203A3683 000.00s basic SCTPChunkShutDown - Dissection
[34m[1mpassed[0m B772C61E 000.00s basic SCTPChunkShutDownAck - Dissection
[34m[1mpassed[0m 26E82AFC 000.00s basic SCTPChunkError - Dissection
[34m[1mpassed[0m FE9FE83D 000.00s basic SCTPChunkCookieEcho - Dissection
[34m[1mpassed[0m 5D04F492 000.00s basic SCTPChunkCookieAck - Dissection
[34m[1mpassed[0m CB4F2EA6 000.00s basic SCTPChunkShutdownComplete - Dissection
[34m[1mpassed[0m 451C596A 000.00s basic SCTPChunkAuthentication - Dissection
[34m[1mpassed[0m 2EC45041 000.00s basic SCTPChunkAddressConf - Dissection
[34m[1mpassed[0m 43BEC18D 000.00s basic SCTPChunkAddressConfAck - Dissection
[34m[1mpassed[0m 3B64297F 000.00s SCTPChunkParamRandom - Consecutive calls
Campaign CRC=34F415FA in 000.02s SHA=AD17983AE4DF8C86BAD6DDEBC53FEAD264FB9DAB
[34m[1mPASSED=25 FAILED=0[0m
[32m━ Loading: test/scapy/layers/skinny.uts[0m
[34m[1mpassed[0m 385F025C 000.00s Skinny - build & dissection
Campaign CRC=E78E7A9C in 000.00s SHA=C31E75483864D629BF18B199608D0681784E1A43
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/scapy/layers/smb.uts[0m
[34m[1mpassed[0m 5C8041A4 000.00s Import
[34m[1mpassed[0m CF752C94 000.00s test SMB Negociate Header - dissect
[34m[1mpassed[0m E9C5A9D3 000.00s test SMB Negociate Header - assemble
[34m[1mpassed[0m 3A069BCC 000.00s SMB Negotiate Request
[34m[1mpassed[0m 7991E7F4 000.00s SMB Negotiate Response Extended Security
[34m[1mpassed[0m 9FD00AC0 000.00s SMB Setup AndX Request (ES)
[34m[1mpassed[0m B9D2D5A5 000.00s SMB Setup AndX Response (ES)
[34m[1mpassed[0m 6D99F794 000.00s SMB Setup AndX Request - accept incomplete (ES)
[34m[1mpassed[0m 1459BECB 000.00s SMB Setup AndX Response - accept complete (ES)
Campaign CRC=F55341DC in 000.02s SHA=AB24888C5DB985FB994BFD1A2AEA051D5EC7466D
[34m[1mPASSED=9 FAILED=0[0m
[32m━ Loading: test/scapy/layers/smb2.uts[0m
[34m[1mpassed[0m A7DC099D 000.00s SMB2 Header dissecting
[34m[1mpassed[0m 52B9C30B 000.00s SMB2 Header assembling
[34m[1mpassed[0m EDB4B9C3 000.00s Common fields in header
[34m[1mpassed[0m 6FBF8DCE 000.00s SMB2 Negotiate Context in Request - type PREAUTH - disassemble
[34m[1mpassed[0m 943A2FBE 000.00s SMB2 Negotiate Context in Request - type ENCRYPTION disassemble
[34m[1mpassed[0m 91C4C51A 000.00s SMB2 Negotiate Context in Request - type COMPRESSION
[34m[1mpassed[0m BEF52211 000.00s SMB2 Negotiate Context in Request - type NETNAME NEGOCIATE
[34m[1mpassed[0m D504D49F 000.00s test SMB2 Negotiate Protocol Request Header - assembling
[34m[1mpassed[0m 915A12B2 000.00s Request with no 0x0311 in dialects
[34m[1mpassed[0m F5AC9391 000.00s Common fields in header
[34m[1mpassed[0m 582ED60C 000.00s SMB2 Negotiate Context in Response - Type PREAUTH
[34m[1mpassed[0m FED4301A 000.00s SMB2 Negotiate Context in Response - Type ENCRYPTION
[34m[1mpassed[0m 4023C12C 000.00s SMB2 Negotiate Context in Response - Type COMPRESSION
[34m[1mpassed[0m B3385EB3 000.00s SMB2 Negotiate Protocol Response Header assembling
[34m[1mpassed[0m 27240E6F 000.00s Response with dialect different from 0x0311
[34m[1mpassed[0m 7FA84DE7 000.00s Common fields in header
[34m[1mpassed[0m 6FBF8DCE 000.00s SMB2 Negotiate Context in Request - type PREAUTH - disassemble
[34m[1mpassed[0m 943A2FBE 000.00s SMB2 Negotiate Context in Request - type ENCRYPTION disassemble
[34m[1mpassed[0m 91C4C51A 000.00s SMB2 Negotiate Context in Request - type COMPRESSION
[34m[1mpassed[0m BEF52211 000.00s SMB2 Negotiate Context in Request - type NETNAME NEGOCIATE
[34m[1mpassed[0m 5865979B 000.00s Default DialectCount
[34m[1mpassed[0m C3B50C27 000.00s Default NegotiateCount
[34m[1mpassed[0m 46099F1D 000.00s SMB2 Negotiate Context in Request - type PREAUTH - disassemble
[34m[1mpassed[0m 01C05841 000.00s SMB2 Negotiate Context in Request - type ENCRYPTION disassemble
[34m[1mpassed[0m 93280C7C 000.00s SMB2 Negotiate Context in Request - type COMPRESSION
[34m[1mpassed[0m 7AC4A6A0 000.00s SMB2 Negotiate Context in Request - type NETNAME NEGOCIATE
[34m[1mpassed[0m CDB157A5 000.00s Setup Session Request
[34m[1mpassed[0m F3FCAA93 000.00s Setup Session Response
Campaign CRC=6FABC698 in 000.03s SHA=1D27D2F3183301AA08D1AB6C1B342FE860DC739A
[34m[1mPASSED=28 FAILED=0[0m
[32m━ Loading: test/scapy/layers/snmp.uts[0m
[34m[1mpassed[0m 7704A111 000.00s SNMP assembling
[34m[1mpassed[0m 89437673 000.00s SNMP disassembling
[34m[1mpassed[0m F7F25C3B 000.00s Basic UDP/SNMP bindings
[34m[1mpassed[0m 8056B27B 000.00s Basic SNMPvarbind build
[34m[1mpassed[0m EEFD9C31 000.00s Failing SNMPvarbind dissection
Campaign CRC=1F42BF5C in 000.01s SHA=257D361A66673D1D32F94A94D96BFDB64883CE81
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/scapy/layers/tftp.uts[0m
[34m[1mpassed[0m 7E3D9D4C 000.00s TFTP Options
Campaign CRC=7A97BF9C in 000.00s SHA=DCAF420360DF837ABA9DB39C03F0E57530D5A9BC
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/scapy/layers/usb.uts[0m
[34m[1mpassed[0m C6F5BE0E 000.00s load module
[34m[1mpassed[0m 79A72499 000.00s linklayer test
[34m[1mpassed[0m 8988CA4B 000.00s USBpcapTransferIsochronous
[34m[1mpassed[0m BDD15E91 000.00s USBpcapTransferInterrupt
[34m[1mpassed[0m C71FC4AD 000.00s USBpcapTransferControl
Campaign CRC=1818C060 in 000.00s SHA=850EFF426F0181528E702317E02DF6923278427D
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/scapy/layers/vrrp.uts[0m
[34m[1mpassed[0m 06543355 000.00s VRRP - build
[34m[1mpassed[0m A6C6FAE1 000.00s VRRP - dissection
[34m[1mpassed[0m 3C60EE28 000.00s VRRP IPv6 - build
[34m[1mpassed[0m 2F81CF0A 000.00s VRRP IPv6 - dissection
[34m[1mpassed[0m BFEBF0CA 000.00s VRRP - chksums
[34m[1mpassed[0m 084C98E6 000.00s VRRP IPv6 - chksums
Campaign CRC=D9FC87DC in 000.00s SHA=65DAD9483920530B092948C25FF3853DA3B1B2C9
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/scapy/layers/vxlan.uts[0m
[34m[1mpassed[0m 1DB45413 000.00s Build a VXLAN packet with VNI of 42
[34m[1mpassed[0m 4D21BD51 000.00s Verify VXLAN Ethernet Binding
[34m[1mpassed[0m 08979818 000.00s Verify UDP dport overloading
[34m[1mpassed[0m 5004880C 000.00s Build a VXLAN packet with next protocol field
[34m[1mpassed[0m 8614DF8C 000.00s Build a VXLAN packet with no group policy ID
[34m[1mpassed[0m 76A01301 000.00s Build a VXLAN packet with group policy ID = 42
[34m[1mpassed[0m 4FFB3E90 000.01s Build a VXLAN packet followed by and IP or IPv6 layer
[34m[1mpassed[0m EFED39DA 000.00s Dissect VXLAN with no NextProtocol
Campaign CRC=177DB210 in 000.02s SHA=D93D44CFF014ADA2A3850107B4A78B9EBE8C0759
[34m[1mPASSED=8 FAILED=0[0m
[32m━ Loading: test/scapy/layers/x509.uts[0m
[34m[1mpassed[0m 815A2A6F 000.00s Decoding an ASN.1 SEQUENCE with an unknown, high-tag identifier
[34m[1mpassed[0m A0410715 000.00s Key class : Importing DER encoded RSA private key
[34m[1mpassed[0m 156EF5A0 000.00s Key class : key version
[34m[1mpassed[0m 6FB0E92E 000.00s Key class : key modulus
[34m[1mpassed[0m 04D67681 000.00s Key class : key public exponent
[34m[1mpassed[0m CE3F420E 000.00s Key class : key private exponent
[34m[1mpassed[0m 9C1E1F5D 000.00s Key class : key prime1
[34m[1mpassed[0m ADA3892D 000.00s Key class : key prime2
[34m[1mpassed[0m 061180BE 000.00s Key class : key exponent1
[34m[1mpassed[0m 4C22B5AF 000.00s Key class : key exponent2
[34m[1mpassed[0m 2A1EAC96 000.00s Key class : key coefficient
[34m[1mpassed[0m CA5C6209 000.01s Cert class : Importing DER encoded X.509 Certificate with RSA public key
[34m[1mpassed[0m 1C954526 000.01s Cert class : Rebuild certificate
[34m[1mpassed[0m 6519AA69 000.00s Cert class : Version
[34m[1mpassed[0m 5F89792E 000.00s Cert class : Serial
[34m[1mpassed[0m 96069759 000.00s Cert class : Signature algorithm (as advertised by TBSCertificate)
[34m[1mpassed[0m 2B54E823 000.00s Cert class : Issuer structure
[34m[1mpassed[0m 9A359EB2 000.00s Cert class : Issuer first attribute
[34m[1mpassed[0m BCD8E63C 000.00s Cert class : Issuer string
[34m[1mpassed[0m C41B9CFF 000.00s Cert class : Validity
[34m[1mpassed[0m 49247FAF 000.00s Cert class : Subject structure
[34m[1mpassed[0m 67529256 000.00s Cert class : Subject last attribute
[34m[1mpassed[0m B8A26A10 000.00s Cert class : Subject string
[34m[1mpassed[0m F1749DC0 000.00s Cert class : SubjectPublicKey algorithm
[34m[1mpassed[0m 57564CB0 000.00s Cert class : SubjectPublicKey value
[34m[1mpassed[0m 605143AE 000.00s Cert class : Extensions structure
[34m[1mpassed[0m E39175B6 000.00s Cert class : Subject key identifier extension info
[34m[1mpassed[0m AAA70103 000.00s Cert class : Subject key identifier extension value
[34m[1mpassed[0m E12DA65D 000.00s Cert class : Signature algorithm
[34m[1mpassed[0m 78AD39E7 000.00s Cert class : Signature value
[34m[1mpassed[0m 68047BAF 000.01s Cert class : Default X509_Cert from scratch
[34m[1mpassed[0m FB1213A9 000.00s Cert class : Error
[34m[1mpassed[0m D9A3D2B4 000.00s CRL class : Importing DER encoded X.509 CRL
[34m[1mpassed[0m 1C954526 000.00s CRL class : Rebuild crl
[34m[1mpassed[0m B1A3384E 000.00s CRL class : Version
[34m[1mpassed[0m 37D33E06 000.00s CRL class : Signature algorithm (as advertised by TBSCertList)
[34m[1mpassed[0m 181DA09D 000.00s CRL class : Issuer structure
[34m[1mpassed[0m D95B0CF4 000.00s CRL class : Issuer first attribute
[34m[1mpassed[0m 16D18A47 000.00s CRL class : Issuer string
[34m[1mpassed[0m 29C49A61 000.00s CRL class : This update
[34m[1mpassed[0m D4495358 000.00s CRL class : Optional next update
[34m[1mpassed[0m 5F33E02C 000.00s CRL class : Optional revoked_certificates structure
[34m[1mpassed[0m D77CB718 000.00s CRL class : Revoked_certificates first attribute
[34m[1mpassed[0m C42F3BD5 000.00s CRL class : Extensions structure
[34m[1mpassed[0m F0DF9A48 000.00s CRL class : Signature algorithm
[34m[1mpassed[0m 44713053 000.00s CRL class : Signature value
[34m[1mpassed[0m 77266656 000.00s CRL class : Default X509_CRL from scratch
[34m[1mpassed[0m B539127D 000.00s Randval tests : ASN1F_SEQUENCE_OF
[34m[1mpassed[0m 87053B16 000.00s Randval tests : ASN1F_PACKET
[34m[1mpassed[0m CB31C001 000.00s OCSP class : OCSP Response import
[34m[1mpassed[0m B1F0C1FD 000.00s OCSP class : OCSP Response global checks
[34m[1mpassed[0m 7082595B 000.00s OCSP class : OCSP ResponseData checks
[34m[1mpassed[0m D5519085 000.00s OCSP class : OCSP SingleResponse checks
[34m[1mpassed[0m 5318D377 000.00s OCSP class : OCSP Response reconstruction
Campaign CRC=0C1AC101 in 000.05s SHA=6408F55B823CEE6E3AA87CC99D07D112FB4D8DF5
[34m[1mPASSED=54 FAILED=0[0m
[32m━ Loading: test/contrib/altbeacon.uts[0m
[34m[1mpassed[0m 926B11EA 000.00s Setup
[34m[1mpassed[0m 22A5CF54 000.00s Presence check
[34m[1mpassed[0m AC58CE7B 000.00s AltBeaconParserTest.testRecognizeBeacon
[34m[1mpassed[0m 158A8B84 000.00s AltBeaconParserTest.testDetectsDaveMHardwareBeacon
[34m[1mpassed[0m 2EDFFF30 000.00s AltBeaconParserTest.testParseWrongFormatReturnsNothing
[34m[1mpassed[0m 9B2F4F51 000.00s AltBeaconParserTest.testParsesBeaconMissingDataField
[34m[1mpassed[0m 3B802940 000.00s Build EIR
Campaign CRC=D7C58309 in 000.00s SHA=C4B462CDA469C88108018EC4507E166AA17D9062
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/aoe.uts[0m
[34m[1mpassed[0m CCFE2482 000.00s Build - Check Ethertype
[34m[1mpassed[0m A3B2AA30 000.00s Build - Check default
[34m[1mpassed[0m 7C934B6D 000.00s Build - Check Issue ATA command
[34m[1mpassed[0m 3C71B50C 000.00s Build - Check Query Config Information
[34m[1mpassed[0m 8EEC2B12 000.00s Build - Check Mac Mask List
[34m[1mpassed[0m DFD25640 000.00s Build - Check ReserveRelease
Campaign CRC=C807C2CC in 000.00s SHA=E606DA710C370788108DC8319AA830F2B3AF5CFA
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/avs.uts[0m
[34m[1mpassed[0m 72BCD676 000.00s Default build, storage and dissection
Campaign CRC=53E97EF6 in 000.00s SHA=DCC4C84EFB41726311A6F926B86AC0605DD8C652
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/bfd.uts[0m
[34m[1mpassed[0m 9C31AA5A 000.00s BFD, basic instantiation
[34m[1mpassed[0m 4CC71667 000.00s BFD - dissection
Campaign CRC=359A5341 in 000.00s SHA=FA44EB8C49B02B064400CC0F8F0C6AE18BE6D0A9
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/contrib/bgp.uts[0m
[34m[1mpassed[0m 07BFF945 000.00s OLD speaker (see RFC 6793)
[34m[1mpassed[0m 0229FEEF 000.00s BGPNLRI_IPv4 - Instantiation
[34m[1mpassed[0m 29E43CFF 000.00s BGPNLRI_IPv4 - Instantiation with specific values (1)
[34m[1mpassed[0m 082A88BB 000.00s BGPNLRI_IPv4 - Instantiation with specific values (2)
[34m[1mpassed[0m 41BB2952 000.00s BGPNLRI_IPv4 - Instantiation with specific values (3)
[34m[1mpassed[0m 0A43D94D 000.00s BGPNLRI_IPv4 - Basic dissection
[34m[1mpassed[0m B45FD533 000.00s BGPNLRI_IPv4 - Dissection with specific values
[34m[1mpassed[0m AAAF4F7E 000.00s BGPNLRI_IPv6 - Instantiation
[34m[1mpassed[0m 62CCF2AB 000.00s BGPNLRI_IPv6 - Instantiation with specific values (1)
[34m[1mpassed[0m 299621DF 000.00s BGPNLRI_IPv6 - Instantiation with specific values (2)
[34m[1mpassed[0m 21AD29D7 000.00s BGPNLRI_IPv6 - Basic dissection
[34m[1mpassed[0m D9C4B77F 000.00s BGPNLRI_IPv6 - Dissection with specific values
[34m[1mpassed[0m E8AA5C39 000.00s BGP - Instantiation (Should be a KEEPALIVE)
[34m[1mpassed[0m 76C8E862 000.00s BGP - Instantiation with specific values (1)
[34m[1mpassed[0m F567EB49 000.00s BGP - Instantiation with specific values (2)
[34m[1mpassed[0m AAE7E875 000.00s BGP - Instantiation with specific values (3)
[34m[1mpassed[0m 2948EB5E 000.00s BGP - Instantiation with specific values (4)
[34m[1mpassed[0m 15E7EE0D 000.00s BGP - Instantiation with specific values (5)
[34m[1mpassed[0m 9648ED26 000.00s BGP - Instantiation with specific values (6)
[34m[1mpassed[0m 202E2F3A 000.00s BGP - Basic dissection
[34m[1mpassed[0m E74F5BBD 000.00s BGP - Dissection with specific values
[34m[1mpassed[0m 60A52550 000.00s BGPKeepAlive - Instantiation (by default, should be a "generic" capability)
[34m[1mpassed[0m D3477ECF 000.00s BGPKeepAlive - Swallowing tests: combined BGPKeepAlive
[34m[1mpassed[0m 64EBE4C1 000.00s BGPCapability - Instantiation (by default, should be a "generic" capability)
[34m[1mpassed[0m DAAE28BB 000.00s BGPCapability - Instantiation with specific values (1)
[34m[1mpassed[0m 31134FB2 000.00s BGPCapability - Check exception
[34m[1mpassed[0m 88058EA7 000.00s BGPCapability - Test haslayer()
[34m[1mpassed[0m DDFDA567 000.00s BGPCapability - Test getlayer()
[34m[1mpassed[0m 50A4B026 000.00s BGPCapability - sessions (1)
[34m[1mpassed[0m 14ACB555 000.00s BGPCapability - sessions (2)
[34m[1mpassed[0m 86F484D1 000.00s BGPCapMultiprotocol - Inheritance
[34m[1mpassed[0m 42CDA112 000.00s BGPCapMultiprotocol - Instantiation
[34m[1mpassed[0m 476FB63E 000.00s BGPCapMultiprotocol - Instantiation with specific values (1)
[34m[1mpassed[0m D220459B 000.00s BGPCapMultiprotocol - Instantiation with specific values (2)
[34m[1mpassed[0m 6D475273 000.00s BGPCapMultiprotocol - Dissection with specific values
[34m[1mpassed[0m 01EF1D8E 000.00s BGPCapORFBlock - Instantiation
[34m[1mpassed[0m C751ECD7 000.00s BGPCapORFBlock - Instantiation with specific values (1)
[34m[1mpassed[0m 918C7984 000.00s BGPCapORFBlock - Instantiation with specific values (2)
[34m[1mpassed[0m 61364530 000.00s BGPCapORFBlock - Basic dissection
[34m[1mpassed[0m 129854A6 000.00s BGPCapORFBlock - Dissection with specific values
[34m[1mpassed[0m 1B4E2F73 000.00s BGPCapORFBlock.ORF - Instantiation
[34m[1mpassed[0m 8D1AFE28 000.00s BGPCapORFBlock.ORF - Instantiation with specific values (1)
[34m[1mpassed[0m 205F3379 000.00s BGPCapORFBlock.ORF - Basic dissection
[34m[1mpassed[0m C70B7C0B 000.00s BGPCapORFBlock.ORF - Dissection with specific values
[34m[1mpassed[0m 78A5F944 000.00s BGPCapORF - Inheritance
[34m[1mpassed[0m 2CA9FCE5 000.00s BGPCapORF - Instantiation
[34m[1mpassed[0m 47A53510 000.00s BGPCapORF - Instantiation with specific values (1)
[34m[1mpassed[0m D60E2926 000.00s BGPCapORF - Instantiation with specific values (2)
[34m[1mpassed[0m 07C12A5A 000.00s BGPCapORF - Basic dissection
[34m[1mpassed[0m 24CEF50D 000.00s BGPCapORF - Dissection with specific values
[34m[1mpassed[0m E1299071 000.00s BGPCapORF - Dissection
[34m[1mpassed[0m 0ABB001C 000.00s BGPCapGracefulRestart.GRTuple - Instantiation
[34m[1mpassed[0m 41E8E696 000.00s BGPCapGracefulRestart.GRTuple - Instantiation with specific values
[34m[1mpassed[0m 1C972EA5 000.00s BGPCapGracefulRestart.GRTuple - Basic dissection
[34m[1mpassed[0m E6049A2B 000.00s BGPCapGracefulRestart.GRTuple - Dissection with specific values
[34m[1mpassed[0m C2DCD0BB 000.00s BGPCapGracefulRestart - Inheritance
[34m[1mpassed[0m 99542362 000.00s BGPCapGracefulRestart - Instantiation
[34m[1mpassed[0m 497F3315 000.00s BGPCapGracefulRestart - Instantiation with specific values (1)
[34m[1mpassed[0m 497F3315 000.00s BGPCapGracefulRestart - Instantiation with specific values (2)
[34m[1mpassed[0m 459A6615 000.00s BGPCapGracefulRestart - Instantiation with specific values (3)
[34m[1mpassed[0m E8D413AF 000.00s BGPCapGracefulRestart - Instantiation with specific values (4)
[34m[1mpassed[0m 38D93AA6 000.00s BGPCapGracefulRestart - Basic dissection
[34m[1mpassed[0m F18ADBA4 000.00s BGPCapGracefulRestart - Dissection with specific values
[34m[1mpassed[0m 42281A97 000.00s BGPCapFourBytesASN - Inheritance
[34m[1mpassed[0m 46FF9C1A 000.00s BGPCapFourBytesASN - Instantiation
[34m[1mpassed[0m C14EFBFB 000.00s BGPCapFourBytesASN - Instantiation with specific values (1)
[34m[1mpassed[0m 3121ECD5 000.00s BGPCapFourBytesASN - Instantiation with specific values (2)
[34m[1mpassed[0m 098AC2F5 000.00s BGPCapFourBytesASN - Basic dissection
[34m[1mpassed[0m FBDB56E6 000.00s BGPCapFourBytesASN - Dissection with specific values
[34m[1mpassed[0m FF88C5E7 000.00s BGPAuthenticationInformation - Instantiation
[34m[1mpassed[0m FD583316 000.00s BGPAuthenticationInformation - Basic dissection
[34m[1mpassed[0m 05EA8A12 000.00s BGPOptParam - Instantiation
[34m[1mpassed[0m D386D9DF 000.00s BGPOptParam - Instantiation with specific values (1)
[34m[1mpassed[0m 1A641406 000.00s BGPOptParam - Instantiation with specific values (2)
[34m[1mpassed[0m 6D95491A 000.00s BGPOptParam - Instantiation with specific values (3)
[34m[1mpassed[0m B6F52980 000.00s BGPOptParam - Instantiation with specific values (4)
[34m[1mpassed[0m 4F4E653E 000.00s BGPOptParam - Instantiation with specific values (5)
[34m[1mpassed[0m E56A5E37 000.00s BGPOptParam - Basic dissection
[34m[1mpassed[0m E50D663F 000.00s BGPOptParam - Dissection with specific values
[34m[1mpassed[0m 83239751 000.00s BGPOpen - Instantiation
[34m[1mpassed[0m C836D805 000.00s BGPOpen - Instantiation with specific values (1)
[34m[1mpassed[0m 5CF74E6A 000.00s BGPOpen - Instantiation with specific values (2)
[34m[1mpassed[0m D09D6275 000.00s BGPOpen - Instantiation with specific values (3)
[34m[1mpassed[0m C7797F0D 000.00s BGPOpen - Dissection with specific values (1)
[34m[1mpassed[0m 52870FB9 000.00s BGPOpen - Dissection with specific values (2) (followed by a KEEPALIVE)
[34m[1mpassed[0m C8D33BE7 000.00s BGPOpen - Dissection with specific values (3)
[34m[1mpassed[0m A7C386FE 000.00s BGPOpen - Dissection with specific values (4)
[34m[1mpassed[0m F2D8F7BA 000.00s BGPPAOrigin - Instantiation
[34m[1mpassed[0m 68537B70 000.00s BGPPAOrigin - Instantiation with specific values
[34m[1mpassed[0m 11183844 000.00s BGPPAOrigin - Dissection
[34m[1mpassed[0m EED71F8B 000.00s BGPPAASPath - Instantiation
[34m[1mpassed[0m A3305EF3 000.00s BGPPAASPath - Instantiation with specific values (1)
[34m[1mpassed[0m ED1106E9 000.00s BGPPAASPath - Instantiation with specific values (2)
[34m[1mpassed[0m F3BD198D 000.00s BGPPAASPath - Instantiation with specific values (3)
[34m[1mpassed[0m A21B6BF6 000.00s BGPPAASPath - Dissection (1)
[34m[1mpassed[0m 9A86FE81 000.00s BGPPAASPath - Dissection (2)
[34m[1mpassed[0m 03D97582 000.00s BGPPANextHop - Instantiation
[34m[1mpassed[0m C26055D0 000.00s BGPPANextHop - Instantiation with specific values
[34m[1mpassed[0m DAD41E11 000.00s BGPPANextHop - Basic dissection
[34m[1mpassed[0m 556C05B0 000.00s BGPPANextHop - Dissection with specific values
[34m[1mpassed[0m 9F45F93B 000.00s BGPPAMultiExitDisc - Instantiation
[34m[1mpassed[0m 48224459 000.00s BGPPAMultiExitDisc - Instantiation with specific values (1)
[34m[1mpassed[0m 77DCD29D 000.00s BGPPAMultiExitDisc - Basic dissection
[34m[1mpassed[0m 87FFD4F4 000.00s BGPPALocalPref - Instantiation
[34m[1mpassed[0m 7A55497B 000.00s BGPPALocalPref - Instantiation with specific values (1)
[34m[1mpassed[0m 05E27331 000.00s BGPPALocalPref - Basic dissection
[34m[1mpassed[0m FB012004 000.00s BGPPAAggregator - Instantiation
[34m[1mpassed[0m 2950DB38 000.00s BGPPAAggregator - Instantiation with specific values (1)
[34m[1mpassed[0m 5BD7C6C5 000.00s BGPPAAggregator - Dissection
[34m[1mpassed[0m 68D4D2E6 000.00s BGPPACommunity - Basic instantiation
[34m[1mpassed[0m 7F7A17FA 000.00s BGPPACommunity - Instantiation with specific value
[34m[1mpassed[0m 32C58406 000.00s BGPPACommunity - Dissection
[34m[1mpassed[0m A266901E 000.00s BGPPAOriginatorID - Basic instantiation
[34m[1mpassed[0m D73AEF2D 000.00s BGPPAOriginatorID - Instantiation with specific value
[34m[1mpassed[0m 509395F0 000.00s BGPPAOriginatorID - Dissection
[34m[1mpassed[0m 11A478B5 000.00s BGPPAClusterList - Basic instantiation
[34m[1mpassed[0m 8212CFC0 000.00s BGPPAClusterList - Instantiation with specific values
[34m[1mpassed[0m 5B3E8545 000.00s BGPPAClusterList - Dissection
[34m[1mpassed[0m 6EA947E7 000.00s BGPPAMPReachNLRI - Instantiation
[34m[1mpassed[0m A88197FD 000.00s BGPPAMPReachNLRI - Instantiation with specific values (1)
[34m[1mpassed[0m 653E29AD 000.00s BGPPAMPReachNLRI - Dissection (1)
[34m[1mpassed[0m 56C5AE58 000.00s BGPPAMPReachNLRI - Dissection (2)
[34m[1mpassed[0m 7DEB0C24 000.00s BGPPAMPUnreachNLRI - Instantiation
[34m[1mpassed[0m 4599F738 000.00s BGPPAMPUnreachNLRI - Instantiation with specific values (1)
[34m[1mpassed[0m 0B9322D2 000.00s BGPPAMPUnreachNLRI - Instantiation with specific values (2)
[34m[1mpassed[0m 74F2B8C8 000.00s BGPPAMPUnreachNLRI - Dissection (1)
[34m[1mpassed[0m A4A58112 000.00s BGPPAMPUnreachNLRI - Dissection (2)
[34m[1mpassed[0m DB4F77B6 000.00s BGPPAAS4Aggregator - Instantiation
[34m[1mpassed[0m B2B5DC38 000.00s BGPPAAS4Aggregator - Instantiation with specific values
[34m[1mpassed[0m EB7D67FC 000.00s BGPPAAS4Aggregator - Dissection
[34m[1mpassed[0m 1FC9CE93 000.00s BGPPathAttr - Instantiation
[34m[1mpassed[0m 67E21AB6 000.00s BGPPathAttr - Instantiation with specific values (1)
[34m[1mpassed[0m 45F50955 000.00s BGPPathAttr - Instantiation with specific values (2)
[34m[1mpassed[0m 4F19949B 000.00s BGPPathAttr - Instantiation with specific values (3)
[34m[1mpassed[0m A86275A9 000.00s BGPPathAttr - Dissection (1)
[34m[1mpassed[0m 4EC9D25B 000.00s BGPPathAttr - advanced
[34m[1mpassed[0m 0759C998 000.00s BGPUpdate - Instantiation
[34m[1mpassed[0m 7CA1D159 000.00s BGPUpdate - Dissection (1)
[34m[1mpassed[0m 1E13C6AA 000.00s BGPUpdate - Behave like a NEW speaker (RFC 6793) - Dissection (2)
[34m[1mpassed[0m 23E2553A 000.01s BGPUpdate - Dissection (MP_REACH_NLRI)
[34m[1mpassed[0m 8C0348D6 000.01s BGPUpdate - Dissection (MP_UNREACH_NLRI)
[34m[1mpassed[0m F2B10FFC 000.00s BGPUpdate - Dissection (with BGP Additional Path)
[34m[1mpassed[0m E7485576 000.00s BGPUpdate - with BGPHeader
[34m[1mpassed[0m C21E3DC0 000.00s BGPNotification - Instantiation
[34m[1mpassed[0m BDF81469 000.00s BGPNotification - Dissection (Administratively Reset)
[34m[1mpassed[0m 1257F644 000.00s BGPNotification - Dissection (Bad Peer AS)
[34m[1mpassed[0m 9AD30AE2 000.00s BGPNotification - Dissection (Attribute Flags Error)
[34m[1mpassed[0m 7E73D740 000.00s BGPRouteRefresh - Instantiation
[34m[1mpassed[0m 30082B60 000.00s BGPRouteRefresh - Instantiation with specific values
[34m[1mpassed[0m 72B1BB61 000.00s BGPRouteRefresh - Dissection (1)
[34m[1mpassed[0m 6F53DDFF 000.00s BGPRouteRefresh - Dissection (2) - With ORFs
[34m[1mpassed[0m 1CB6F65E 000.00s BGPRouteRefresh - Dissection (3) - bad ORFS (GH3345)
[34m[1mpassed[0m E589A6C8 000.00s BGPCapGeneric fuzz()
Campaign CRC=E3539014 in 000.09s SHA=14E548895942C154A1313020ABCD51CD7D508EBC
[34m[1mPASSED=153 FAILED=0[0m
[32m━ Loading: test/contrib/bier.uts[0m
[34m[1mpassed[0m C7966420 000.00s BIER - build/dissection
Campaign CRC=E0D33815 in 000.00s SHA=0E3491751EAB95087105FB85F9237507FBAA5494
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/bp.uts[0m
[34m[1mpassed[0m 0500B6C5 000.00s Build packets & dissect
Campaign CRC=8E924623 in 000.00s SHA=4740F127FD09D6DA41EBFB5E387E9E2E06994C98
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/cansocket.uts[0m
Campaign CRC=D2D14014 in 000.00s SHA=8BE92D9B60A281AD88C83FF5F660466316A9849B
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/contrib/cansocket_native.uts[0m
Campaign CRC=47E759E9 in 000.00s SHA=F94CA2F395F7B874E06600C62646B26987984B06
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/contrib/cansocket_python_can.uts[0m
Campaign CRC=32FC9882 in 000.00s SHA=2587DE49D1D1203DB3C3FB9153447F4CA62EB4AE
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/contrib/carp.uts[0m
[34m[1mpassed[0m 2DDCDC64 000.00s Build
Campaign CRC=F0A45F01 in 000.00s SHA=7029CC4050D66575932CBB17BD4BAF6C47388FA6
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/cdp.uts[0m
[34m[1mpassed[0m E385210B 000.00s CDPv2 - Dissection (1)
[34m[1mpassed[0m 5896E63B 000.00s CDPv2 - Rebuild (1)
[34m[1mpassed[0m 6CE77812 000.00s CDPv2 - Dissection (2)
[34m[1mpassed[0m F8FE3D06 000.00s CDPv2 - Rebuild (2)
[34m[1mpassed[0m 42955EC8 000.00s CDPv2 - Complex Packet
[34m[1mpassed[0m DCDF175D 000.00s CDPChecksum - packet with odd length
[34m[1mpassed[0m 708ADF8E 000.00s CDPv2 - CDPMsgAddr Packet
Campaign CRC=A3D9CCFF in 000.01s SHA=408937DB349546F0DD90AED47CD93260FEAE1974
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/chdlc.uts[0m
[34m[1mpassed[0m DBBEE11D 000.00s Default build, storage and dissection
[34m[1mpassed[0m 898D52EA 000.00s Build request
[34m[1mpassed[0m D2D3DF2C 000.00s Build keepalive
Campaign CRC=45717F20 in 000.00s SHA=CB08CB6476F7D7F6C187D990E414DC641E8E94CD
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/contrib/coap.uts[0m
[34m[1mpassed[0m 2A01A5DD 000.00s Import the CoAP layer
[34m[1mpassed[0m F3420745 000.00s CoAP default values
[34m[1mpassed[0m 866B41E5 000.00s Token length calculation
[34m[1mpassed[0m 36FFB16B 000.00s CON GET dissect
[34m[1mpassed[0m C56B530B 000.00s Extended option delta
[34m[1mpassed[0m 3A6976AC 000.00s Extended option length
[34m[1mpassed[0m B6086FF0 000.00s Options should be ordered by option number
[34m[1mpassed[0m 955A5EBB 000.00s Options of the same type should not be reordered
[34m[1mpassed[0m C6C67A92 000.00s Destination port
[34m[1mpassed[0m 7481DB92 000.00s Source port
[34m[1mpassed[0m 9549A0DE 000.00s building with a text/plain payload
[34m[1mpassed[0m FD8769CA 000.00s dissection with a text/plain payload
Campaign CRC=8E8F201E in 000.01s SHA=17F7A2210EBFD8B725A954D46D57D70BC1D5ADB9
[34m[1mPASSED=12 FAILED=0[0m
[32m━ Loading: test/contrib/concox.uts[0m
[34m[1mpassed[0m 8AFBFC0A 000.00s Basic tests
Campaign CRC=A90E25CF in 000.00s SHA=F37F73E687CE02951DE7D512CA1095A2E69E8FBB
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/dce_rpc.uts[0m
[34m[1mpassed[0m 22FDB774 000.00s Import the DCE/RPC layer
[34m[1mpassed[0m F9F9757C 000.00s Little Endian IntField getfield
[34m[1mpassed[0m FECC3148 000.00s Little Endian IntField addfield
[34m[1mpassed[0m 0D424B4B 000.00s Big Endian IntField getfield
[34m[1mpassed[0m 6DF20DE4 000.00s Big Endian IntField addfield
[34m[1mpassed[0m 00F1595F 000.00s Little Endian StrField getfield
[34m[1mpassed[0m DEA8F3D5 000.00s Little Endian StrField addfield
[34m[1mpassed[0m 31A4FD97 000.00s Big Endian StrField getfield
[34m[1mpassed[0m E582D47B 000.00s Big Endian StrField addfield
[34m[1mpassed[0m 31CEEC81 000.00s Little Endian UUIDField getfield
[34m[1mpassed[0m CB324544 000.00s Little Endian UUIDField addfield
[34m[1mpassed[0m 5AD58BC4 000.00s Big Endian UUIDField getfield
[34m[1mpassed[0m 4773038D 000.00s Big Endian UUIDField addfield
[34m[1mpassed[0m F0740964 000.00s DCE/RPC default values
[34m[1mpassed[0m F6C222CE 000.00s DCE/RPC payload length computation
[34m[1mpassed[0m E119BDBD 000.00s DCE/RPC Guess payload class fallback with no possible payload
[34m[1mpassed[0m C39CE92E 000.00s DCE/RPC Guess payload class to a registered heuristic payload
[34m[1mpassed[0m E119BDBD 000.00s DCE/RPC Guess payload class fallback with possible payload classes
[34m[1mpassed[0m BE9E59DD 000.00s DCE/RPC little-endian build
[34m[1mpassed[0m 96C1BD05 000.00s DCE/RPC little-endian dissection
Campaign CRC=21DB8CE8 in 000.01s SHA=EB1509B3173D20075712B5499DF0756D04061B97
[34m[1mPASSED=20 FAILED=0[0m
[32m━ Loading: test/contrib/diameter.uts[0m
[34m[1mpassed[0m 15B2973F 000.00s AVP identified by full name
[34m[1mpassed[0m 3DFE6124 000.00s Same AVP identified by the beginning of the name
[34m[1mpassed[0m 52D158E2 000.00s Same AVP identified by its code
[34m[1mpassed[0m 454AFB4E 000.00s The Session-Id AVP (with some padding added)
[34m[1mpassed[0m A626FBBA 000.00s An enumerated AVP
[34m[1mpassed[0m 812ACDC4 000.00s An address AVP
[34m[1mpassed[0m 3A08DACF 000.00s A time AVP
[34m[1mpassed[0m 9832FFA4 000.00s An empty Auth App ID AVP
[34m[1mpassed[0m 89807E0C 000.00s An ISDN AVP
[34m[1mpassed[0m 11CED972 000.00s Some OctetString AVPs
[34m[1mpassed[0m A3E7CAD1 000.00s Unknown AVP identifier
[34m[1mpassed[0m A6E75EC2 000.00s Vendor AVP identified by full name
[34m[1mpassed[0m 6CF51C41 000.00s Same AVP identified by its code and vendor ID
[34m[1mpassed[0m FFD46D3C 000.00s Altering the flags of the Origin-Host AVP
[34m[1mpassed[0m 61803652 000.00s Altering the length of the Destination-Realm AVP
[34m[1mpassed[0m 4D429E79 000.00s Altering the vendor of the Public-Identity AVP, and hence the flags ...
[34m[1mpassed[0m 623E1F2A 000.00s The Supported-Features AVP (with vendor)
[34m[1mpassed[0m 53CBCF82 000.00s The same AVP created more simply
[34m[1mpassed[0m 13737913 000.00s (re)Building the previous AVP from scratch
[34m[1mpassed[0m 5FE274AE 000.00s Another (dummy) grouped AVP
[34m[1mpassed[0m B7718836 000.00s A grouped AVP inside another grouped AVP
[34m[1mpassed[0m 6924C8F6 000.00s A big grouped AVP
[34m[1mpassed[0m 109BBBCF 000.00s Dissect grouped AVP
[34m[1mpassed[0m EB7943C8 000.00s A simple request identified by its name
[34m[1mpassed[0m D0CD98F9 000.00s Unknown request by its name
[34m[1mpassed[0m 893DDEA5 000.00s The same one identified by its code
[34m[1mpassed[0m BB89C6D5 000.00s Unknown request by its code
[34m[1mpassed[0m 88882CF0 000.00s The same one identified by its abbreviation
[34m[1mpassed[0m 7E16A921 000.00s Altering the request default fields
[34m[1mpassed[0m 0A6DF884 000.00s Altering the default request fields with string
[34m[1mpassed[0m 503F45A2 000.00s Altering the default request fields with invalid string
[34m[1mpassed[0m B4710BF6 000.00s A simple answer identified by its name
[34m[1mpassed[0m 7A6B57AF 000.00s Same answer identified by its code or abbreviation
[34m[1mpassed[0m 3C704AEA 000.00s Altering the answer default fields
[34m[1mpassed[0m 5A516C3B 000.01s A dummy Multimedia-Auth request (identified by only a portion of its name)
[34m[1mpassed[0m 3D84D971 000.01s The same request built from scratch
Campaign CRC=1F80F4E8 in 000.05s SHA=903CD50307C07BD4636F466CDC2FD1CB6DD30104
[34m[1mPASSED=36 FAILED=0[0m
[32m━ Loading: test/contrib/dtp.uts[0m
[34m[1mpassed[0m D979EB4F 000.00s Basic DTP build
[34m[1mpassed[0m F3CC7A19 000.00s Basic DTP dissection
[34m[1mpassed[0m 592C91AF 000.00s Test negotiate_trunk
Campaign CRC=7EB88161 in 000.00s SHA=0E5A7FA3453F79BD5C4727F6A68EEAAE4E8DDBA0
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/contrib/eddystone.uts[0m
[34m[1mpassed[0m DA599690 000.00s Setup
[34m[1mpassed[0m B6F4E7AF 000.00s Eddystone URL (decode EIR)
[34m[1mpassed[0m 0AC00106 000.00s Eddystone URL (decode LE Set Advertising Data)
[34m[1mpassed[0m FDCE20FD 000.00s Eddystone URL (encode frames)
[34m[1mpassed[0m 63CAE18E 000.00s Eddystone URL (encode unsupported scheme)
[34m[1mpassed[0m 9D81C503 000.00s Eddystone URL (encode advertising report)
Campaign CRC=F728C163 in 000.00s SHA=195216E8467334700D9F8B1D79A7190A388A6723
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/eigrp.uts[0m
[34m[1mpassed[0m 78FA3B53 000.00s EIGRP IPv4 Binding
[34m[1mpassed[0m 67878E5F 000.00s EIGRP IPv6 Binding
[34m[1mpassed[0m B4FCE0EC 000.00s EIGRP checksum field
[34m[1mpassed[0m 12A5766B 000.00s ShortVersionField nice representation
[34m[1mpassed[0m FEE00658 000.00s ShortVersionField h2i function
[34m[1mpassed[0m 5578EDC6 000.00s ShortVersionField error
[34m[1mpassed[0m 10C647EB 000.00s EigrpIPField length with prefix length of 8 bit
[34m[1mpassed[0m 8A6461F8 000.00s EigrpIPField length with prefix length of 12 bit
[34m[1mpassed[0m 237D0CF7 000.00s EigrpIPField length with prefix length of 24 bit
[34m[1mpassed[0m 715FAA89 000.00s EigrpIPField length with prefix length of 28 bit
[34m[1mpassed[0m 81C42B2C 000.00s EigrpIPField randval
[34m[1mpassed[0m 1B6EC14B 000.00s EigrpIP6Field length with prefix length of 8 bit
[34m[1mpassed[0m F3EDDA80 000.00s EigrpIP6Field length with prefix length of 99 bit
[34m[1mpassed[0m 01FCB71F 000.00s EigrpIP6Field length with prefix length of 128 bit
[34m[1mpassed[0m 73845B1C 000.00s EigrpIP6Field randval
[34m[1mpassed[0m 24F73F59 000.00s EIGRPGuessPayloadClass function: Return Parameters TLV
[34m[1mpassed[0m 4B6B26FE 000.00s EIGRPGuessPayloadClass function: Return Authentication Data TLV
[34m[1mpassed[0m 8455A2CA 000.00s EIGRPGuessPayloadClass function: Return Sequence TLV
[34m[1mpassed[0m B4133706 000.00s EIGRPGuessPayloadClass function: Return Software Version TLV
[34m[1mpassed[0m E2C15504 000.00s EIGRPGuessPayloadClass function: Return Next Multicast Sequence TLV
[34m[1mpassed[0m 2423B98E 000.00s EIGRPGuessPayloadClass function: Return Stub Router TLV
[34m[1mpassed[0m E2F67C5D 000.00s EIGRPGuessPayloadClass function: Return Internal Route TLV
[34m[1mpassed[0m 69F437BD 000.00s EIGRPGuessPayloadClass function: Return External Route TLV
[34m[1mpassed[0m 53019AF8 000.00s EIGRPGuessPayloadClass function: Return IPv6 Internal Route TLV
[34m[1mpassed[0m 903BD2DE 000.00s EIGRPGuessPayloadClass function: Return IPv6 External Route TLV
[34m[1mpassed[0m 00A57195 000.00s EIGRPGuessPayloadClass function: Return EIGRPGeneric
[34m[1mpassed[0m 3C51BAD4 000.00s EIGRP parameters and software version
[34m[1mpassed[0m F16ABBD0 000.00s EIGRP Sequence
[34m[1mpassed[0m 5252C2A0 000.00s EIGRP Generic
[34m[1mpassed[0m 411A85A1 000.00s EIGRP internal route length field
[34m[1mpassed[0m 2ED5A7C0 000.00s EIGRP external route length field
[34m[1mpassed[0m 870DB3D0 000.00s EIGRPv6 internal route length field
[34m[1mpassed[0m 1484F8DF 000.00s EIGRPv6 external route length field
[34m[1mpassed[0m 4896B499 000.00s Receive-Only
[34m[1mpassed[0m 33F0B308 000.00s Connected
[34m[1mpassed[0m D054D189 000.00s Static
[34m[1mpassed[0m 4B6029AC 000.00s Summary
[34m[1mpassed[0m B45D1F34 000.00s Connected, Summary
[34m[1mpassed[0m 6491FAB3 000.00s Static, Summary
[34m[1mpassed[0m CF5286B4 000.00s Redistributed, Connected
[34m[1mpassed[0m CAECAE79 000.00s Redistributed, Static
[34m[1mpassed[0m 621116E6 000.00s Redistributed, Static, Connected
[34m[1mpassed[0m EE1E38B9 000.00s Redistributed, Summary
[34m[1mpassed[0m E09601EF 000.00s Redistributed, Connected, Summary
[34m[1mpassed[0m E6378EC7 000.00s Connected, Redistributed, Static, Summary
[34m[1mpassed[0m 5872906A 000.00s Leak-Map
[34m[1mpassed[0m 9E1F107B 000.00s Connected, Leak-Map
[34m[1mpassed[0m F6E7F059 000.00s External route flag external
[34m[1mpassed[0m 3C4BE7CE 000.00s External route flag candidate-default route
[34m[1mpassed[0m 08F27350 000.00s Multiple internal routing updates
[34m[1mpassed[0m F95592D8 000.00s Multiple external routing updates
[34m[1mpassed[0m A6294872 000.00s Verify keysize calculation
[34m[1mpassed[0m 10EEAB89 000.00s Verify length calculation
Campaign CRC=238308E8 in 000.02s SHA=2FF9D3C89BF08A0EE08C026797375B863DC23114
[34m[1mPASSED=53 FAILED=0[0m
[32m━ Loading: test/contrib/enipTCP.uts[0m
[34m[1mpassed[0m AEC1ECE6 000.00s Import the enip layer
[34m[1mpassed[0m 6844A936 000.00s Encapsulation Header Default Values
[34m[1mpassed[0m 78B7D966 000.00s ENIP List Services Reply Command ID
[34m[1mpassed[0m 7519B59A 000.00s ENIP List Services Reply Default Values
[34m[1mpassed[0m 1296DA72 000.00s ENIP List Services Reply Items Default Values
[34m[1mpassed[0m D6F624F7 000.00s ENIP List Identity Reply Command ID
[34m[1mpassed[0m 4874B7AD 000.00s ENIP List Identity Reply Default Values
[34m[1mpassed[0m 40588C18 000.00s ENIP List Identity Reply Items Default Values
[34m[1mpassed[0m B1002807 000.00s ENIP List Interfaces Reply Command ID
[34m[1mpassed[0m 01BC03D4 000.00s ENIP List Interfaces Reply Default Values
[34m[1mpassed[0m 91633E9E 000.00s ENIP List Interfaces Reply Items Default Values
[34m[1mpassed[0m A6FCF197 000.00s ENIP Register Session Command ID
[34m[1mpassed[0m D8828F58 000.00s ENIP Register Session Default Values
[34m[1mpassed[0m 22CF95D8 000.00s ENIP Register Session Request
[34m[1mpassed[0m 01103FBC 000.00s ENIP Register Session Reply
[34m[1mpassed[0m C52473A1 000.00s ENIP Send RR Data Command ID
[34m[1mpassed[0m 5C22F43C 000.00s ENIP Send RR Data Default Values
[34m[1mpassed[0m 0C6F787C 000.00s ENIP Send RR Data Request
[34m[1mpassed[0m 17463BBF 000.00s ENIP Send RR Data Reply
[34m[1mpassed[0m 1EEB21DA 000.00s ENIP Send Unit Data Command ID
[34m[1mpassed[0m B00750CB 000.00s ENIP Send Unit Data Default Values
[34m[1mpassed[0m 4DFEC256 000.00s ENIP Send Unit Data
Campaign CRC=70E9D88D in 000.01s SHA=8B9076006B736D557A3404EF777E0C86F375CE22
[34m[1mPASSED=22 FAILED=0[0m
[32m━ Loading: test/contrib/erspan.uts[0m
[34m[1mpassed[0m 496221D2 000.00s Build & dissect ERSPAN 1
[34m[1mpassed[0m E19CD6C5 000.00s Build ERSPAN II
[34m[1mpassed[0m EEAF284B 000.00s Dissect ERSPAN II
[34m[1mpassed[0m 8301BF27 000.00s Build & dissect ERSPAN III with platform specific
[34m[1mpassed[0m 5AC3D4BA 000.00s Build & dissect ERSPAN III without platform specific
Campaign CRC=05CE5439 in 000.00s SHA=D25411FE6DF1642D0545A3E446FDB0323A0E3B23
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/ethercat.uts[0m
[34m[1mpassed[0m 8F754A9F 000.01s regression test
[34m[1mpassed[0m 61A99FE8 000.00s Avoid mix of LEBitFields and BitFields
[34m[1mpassed[0m EFBD1827 000.00s EtherCat and padding
[34m[1mpassed[0m 6DCD6B6D 000.00s EtherCat and RawPayload
[34m[1mpassed[0m 77EA7D54 000.01s EtherCat - test invalid length detection
[34m[1mpassed[0m 86AD1CBA 000.01s EtherCat and Type12 DLPDU layers
[34m[1mpassed[0m 4B999277 000.00s EtherCat and Type12 DLPDU layer using structure used for physical and broadcast addressing
[34m[1mpassed[0m A363BE31 000.00s EtherCat and Type12 DLPDU layer using structure used for logical addressing
[34m[1mpassed[0m C5C6582C 000.04s EtherCat and randomly stacked Type12 DLPDU layers
Campaign CRC=0087D228 in 000.09s SHA=D22A162133008F9FE0A25CC36427C59F284B7082
[34m[1mPASSED=9 FAILED=0[0m
[32m━ Loading: test/contrib/etherip.uts[0m
[34m[1mpassed[0m 4C61684B 000.00s Basic EtherIP test
Campaign CRC=EE8184BE in 000.00s SHA=888260DB9DEAC82D4AE223663755A8264C0E6FC8
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/exposure_notification.uts[0m
[34m[1mpassed[0m 926B11EA 000.00s Setup
[34m[1mpassed[0m E6FEE8FE 000.00s Presence check
[34m[1mpassed[0m 452E240E 000.00s Raw payload copied from BluetoothExplorer.app
[34m[1mpassed[0m 442049EB 000.00s Raw captured payload
Campaign CRC=9E782A77 in 000.00s SHA=C608CF534C76F4AF7CF15041004ECF9F5D6941DC
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/contrib/geneve.uts[0m
[34m[1mpassed[0m CCAF5194 000.00s Build & dissect - GENEVE encapsulates Ether
[34m[1mpassed[0m 5F273E52 000.00s Build & dissect - GENEVE with options encapsulates Ether
[34m[1mpassed[0m D60BB061 000.00s Build & dissect - GENEVE encapsulates IPv4
[34m[1mpassed[0m 3F8CCDF3 000.00s Build & dissect - GENEVE encapsulates IPv6
[34m[1mpassed[0m F6A7525C 000.00s GENEVE - Answers
[34m[1mpassed[0m 035999B0 000.00s GENEVE - Summary
Campaign CRC=253E009E in 000.01s SHA=B0D652EAFA08D5DCC454638793C16FD28CE813AF
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/gtp.uts[0m
[34m[1mpassed[0m 3D059091 000.00s GTPHeader, basic instantiation
[34m[1mpassed[0m 912A0032 000.00s GTP_U_Header detection
[34m[1mpassed[0m A58ACA8F 000.00s GTP_U_Header with PDU Session Container
[34m[1mpassed[0m 24CDE0AD 000.00s GTP_U_Header with PDU Session Container with QFI/PPI
[34m[1mpassed[0m 10FB55CF 000.00s GTP_U_Header sub layers
[34m[1mpassed[0m 525D312B 000.00s GTPPDUSessionContainer(), dissect
[34m[1mpassed[0m 954DF898 000.00s GTPPDUSessionContainer with padding
[34m[1mpassed[0m 60522119 000.00s GTPEchoResponse matches GTPEchoRequest by seq
[34m[1mpassed[0m 478FC514 000.00s GTPCreatePDPContextRequest(), basic instantiation
[34m[1mpassed[0m 31D513AD 000.00s GTPCreatePDPContextRequest(), basic dissection
[34m[1mpassed[0m C653E88F 000.00s GTPV1UpdatePDPContextRequest(), dissect
[34m[1mpassed[0m 3E9021BC 000.00s GTPV1UpdatePDPContextResponse(), dissect
[34m[1mpassed[0m 8556D319 000.00s IE_Cause(), dissect
[34m[1mpassed[0m 368F2ABB 000.00s IE_Cause(), basic instantiation
[34m[1mpassed[0m AE66E195 000.00s IE_IMSI(), dissect
[34m[1mpassed[0m A1535328 000.00s IE_IMSI(), basic instantiation
[34m[1mpassed[0m A1C1CE8E 000.00s IE_Routing(), dissect
[34m[1mpassed[0m 2B37B2B9 000.00s IE_Routing(), basic instantiation
[34m[1mpassed[0m DDA4A54D 000.00s IE_Recovery(), dissect
[34m[1mpassed[0m 29AFEDB6 000.00s IE_Recovery(), basic instantiation
[34m[1mpassed[0m 48095B23 000.00s IE_SelectionMode(), dissect
[34m[1mpassed[0m 2C1E956E 000.00s IE_SelectionMode(), basic instantiation
[34m[1mpassed[0m DD6B1417 000.00s IE_TEIDI(), dissect
[34m[1mpassed[0m F27515FA 000.00s IE_TEIDI(), basic instantiation
[34m[1mpassed[0m 34F95BAC 000.00s IE_TEICP(), dissect
[34m[1mpassed[0m 275BDFF4 000.00s IE_TEICP(), basic instantiation
[34m[1mpassed[0m AFCABAFA 000.00s IE_Teardown(), dissect
[34m[1mpassed[0m 24D46469 000.00s IE_Teardown(), basic instantiation
[34m[1mpassed[0m 86600E86 000.00s IE_NSAPI(), dissect
[34m[1mpassed[0m 6C60D96F 000.00s IE_NSAPI(), basic instantiation
[34m[1mpassed[0m 2B78370E 000.00s IE_ChargingCharacteristics(), dissect
[34m[1mpassed[0m D63BB6F1 000.00s IE_ChargingCharacteristics(), basic instantiation
[34m[1mpassed[0m 95F7A62E 000.00s IE_TraceReference(), basic instantiation
[34m[1mpassed[0m 00049528 000.00s IE_TraceType(), basic instantiation
[34m[1mpassed[0m B7F158BD 000.00s IE_ChargingId(), dissect
[34m[1mpassed[0m CBA1A6E5 000.00s IE_ChargingId(), basic instantiation
[34m[1mpassed[0m C39051A0 000.00s IE_EndUserAddress(), dissect
[34m[1mpassed[0m C8050E2C 000.00s IE_EndUserAddress(), IPv4/IPv6 dissect
[34m[1mpassed[0m 80F42488 000.00s IE_EndUserAddress(), basic instantiation IPv4
[34m[1mpassed[0m BCFDA151 000.00s IE_EndUserAddress(), basic instantiation IPv6
[34m[1mpassed[0m 44082C08 000.00s IE_EndUserAddress(), basic instantiation IPv4/IPv6
[34m[1mpassed[0m 606AB699 000.00s IE_AccessPointName(), dissect
[34m[1mpassed[0m 725C4839 000.00s IE_AccessPointName(), basic instantiation
[34m[1mpassed[0m 677396CC 000.00s IE_ProtocolConfigurationOptions(), dissect
[34m[1mpassed[0m 8E99F144 000.00s IE_ProtocolConfigurationOptions(), basic instantiation
[34m[1mpassed[0m EB356BEF 000.00s IE_GSNAddress(), simple build/dissect IPv4
[34m[1mpassed[0m D098E676 000.00s IE_GSNAddress(), simple build/dissect IPv6
[34m[1mpassed[0m 69494BE7 000.00s IE_GSNAddress(), dissect IPv4
[34m[1mpassed[0m 57FB23F0 000.00s IE_GSNAddress(), dissect IPv6
[34m[1mpassed[0m 7F8A6F3E 000.00s IE_GSNAddress(), basic instantiation IPv4
[34m[1mpassed[0m 4387C3EF 000.00s IE_GSNAddress(), basic instantiation IPv6
[34m[1mpassed[0m 0E17D08D 000.00s IE_MSInternationalNumber(), dissect
[34m[1mpassed[0m 2A4B0903 000.00s IE_MSInternationalNumber(), basic instantiation
[34m[1mpassed[0m 4AB81EF1 000.00s IE_QoS(), dissect
[34m[1mpassed[0m 9B09660B 000.00s IE_QoS(), basic instantiation
[34m[1mpassed[0m 2CCD1282 000.00s IE_CommonFlags(), dissect
[34m[1mpassed[0m F3F3A428 000.00s IE_CommonFlags(), basic instantiation
[34m[1mpassed[0m 08E68797 000.00s IE_APNRestriction(), basic instantiation
[34m[1mpassed[0m 030E0728 000.00s IE_RATType(), dissect
[34m[1mpassed[0m C0F48FD4 000.00s IE_RATType(), basic instantiation
[34m[1mpassed[0m A72CCB60 000.00s IE_UserLocationInformation(), dissect
[34m[1mpassed[0m 4225880F 000.00s IE_UserLocationInformation(), basic instantiation
[34m[1mpassed[0m 709A5518 000.00s IE_MSTimeZone(), dissect
[34m[1mpassed[0m 24638A44 000.00s IE_MSTimeZone(), basic instantiation
[34m[1mpassed[0m 5D87975F 000.00s IE_IMEI(), dissect
[34m[1mpassed[0m AD8D5C2A 000.00s IE_IMEI(), basic instantiation
[34m[1mpassed[0m 5CC0EDE2 000.00s IE_MSInfoChangeReportingAction(), basic instantiation
[34m[1mpassed[0m F2BE9E37 000.00s IE_DirectTunnelFlags(), dissect
[34m[1mpassed[0m CE3A9C36 000.00s IE_DirectTunnelFlags(), basic instantiation
[34m[1mpassed[0m 1DF96849 000.00s IE_BearerControlMode(), basic instantiation
[34m[1mpassed[0m CD92FCDD 000.00s IE_EvolvedAllocationRetentionPriority(), basic instantiation
[34m[1mpassed[0m 639DC57B 000.00s IE_CharginGatewayAddress(), basic instantiation
[34m[1mpassed[0m 02B19167 000.00s IE_PrivateExtension(), basic instantiation
Campaign CRC=EDFB0990 in 000.07s SHA=ADCCF29DF1A6AEFD3F4B29340FC1CD6023BE7BF9
[34m[1mPASSED=73 FAILED=0[0m
[32m━ Loading: test/contrib/gtp_v2.uts[0m
[34m[1mpassed[0m 5CCFC8E4 000.00s GTPHeader v2, basic instantiation
[34m[1mpassed[0m 65EBE70E 000.00s GTPV2EchoRequest, basic instantiation
[34m[1mpassed[0m AA51C76B 000.00s GTPV2CreateSessionRequest, basic instantiation
[34m[1mpassed[0m F9C6810E 000.00s GTPV2EchoRequest, dissection
[34m[1mpassed[0m 429B7CBE 000.00s GTPV2EchoResponse, dissection
[34m[1mpassed[0m 9CFECF19 000.00s GTPV2ModifyBearerRequest, dissection
[34m[1mpassed[0m 4A51BF5A 000.00s IE_IMSI, dissection
[34m[1mpassed[0m D4FEA35D 000.00s IE_IMSI, basic instantiation
[34m[1mpassed[0m E52DB4DC 000.00s IE_Cause, dissection
[34m[1mpassed[0m 0F5CA9D1 000.00s IE_Cause, basic instantiation
[34m[1mpassed[0m EBD4DDA0 000.00s IE_Cause, basic instantiation 2
[34m[1mpassed[0m 50F8C5D1 000.00s IE_Cause, basic instantiation 3
[34m[1mpassed[0m 19654406 000.00s IE_RecoveryRestart, dissection
[34m[1mpassed[0m 7A57FDB7 000.00s IE_RecoveryRestart, basic instantiation
[34m[1mpassed[0m 94FE45CE 000.00s IE_APN, dissection
[34m[1mpassed[0m 1EAA5031 000.00s IE_APN, basic instantiation
[34m[1mpassed[0m DD2D2887 000.00s IE_AMBR, dissection
[34m[1mpassed[0m 45FA5ED0 000.00s IE_AMBR, basic instantiation
[34m[1mpassed[0m FCEB3271 000.00s IE_EPSBearerID, dissection
[34m[1mpassed[0m 53FF4499 000.00s IE_EPSBearerID, basic instantiation
[34m[1mpassed[0m 58247B94 000.00s IE_IP_Address, dissection
[34m[1mpassed[0m 55B60F96 000.00s IE_IP_Address, basic instantiation
[34m[1mpassed[0m 79564039 000.00s IE_MEI, dissection
[34m[1mpassed[0m 02F592A8 000.00s IE_MEI, basic instantiation
[34m[1mpassed[0m EA549337 000.00s IE_MSISDN, dissection
[34m[1mpassed[0m 167FBE48 000.00s IE_MSISDN, basic instantiation
[34m[1mpassed[0m C296EE54 000.00s IE_Indication, dissection
[34m[1mpassed[0m 752AF271 000.00s IE_Indication, basic instantiation
[34m[1mpassed[0m 5F4A2709 000.00s IE_Indication, basic instantiation 2
[34m[1mpassed[0m E5AD13E3 000.00s IE_PCO, dissection
[34m[1mpassed[0m 087BE85E 000.00s IE_PCO, basic instantiation
[34m[1mpassed[0m 3F8EFB99 000.00s IE_EPCO, dissection
[34m[1mpassed[0m 80FD0022 000.00s IE_EPCO, basic instantiation
[34m[1mpassed[0m 907E8EA6 000.00s IE_APCO, dissection
[34m[1mpassed[0m F2B3BFA4 000.00s IE_APCO, basic instantiation
[34m[1mpassed[0m EBB152A7 000.00s IE_MMContext_EPS, dissection
[34m[1mpassed[0m 4D4DDF00 000.00s IE_MMContext_EPS, basic instantiation
[34m[1mpassed[0m D3DCE265 000.00s IE_PDNConnection, IE_FQDN, dissection
[34m[1mpassed[0m 12494A7C 000.00s IE_PDNConnection, IE_FQDN, basic instantiation
[34m[1mpassed[0m 60740CB5 000.00s IE_PAA, dissection
[34m[1mpassed[0m 90342883 000.00s IE_PAA, basic instantiation
[34m[1mpassed[0m CD8834C2 000.00s IE_Bearer_QoS, dissection
[34m[1mpassed[0m 2668574E 000.00s IE_Bearer_QoS, basic instantiation
[34m[1mpassed[0m 0551DF73 000.00s IE_RAT, dissection
[34m[1mpassed[0m 0B681092 000.00s IE_RAT, basic instantiation
[34m[1mpassed[0m 0AE4B86B 000.00s IE_ServingNetwork, dissection
[34m[1mpassed[0m 4DD7450E 000.00s IE_ServingNetwork, basic instantiation
[34m[1mpassed[0m DFB109BF 000.00s IE_ULI, dissection
[34m[1mpassed[0m A6A6BEEB 000.00s IE_ULI, basic instantiation
[34m[1mpassed[0m 57C935DB 000.00s IE_UCI, dissection
[34m[1mpassed[0m D16659BC 000.00s IE_UCI, basic instantiation
[34m[1mpassed[0m 70288695 000.00s IE_BearerFlags, dissection
[34m[1mpassed[0m 9147A6DC 000.00s IE_BearerFlags, basic instantiation
[34m[1mpassed[0m EE2DE0CC 000.00s IE_UPF_SelInd_Flags, dissection
[34m[1mpassed[0m E8EB2AB8 000.00s IE_UPF_SelInd_Flags, basic instantiation
[34m[1mpassed[0m 639E1D21 000.00s IE_Ran_Nas_Cause, dissection
[34m[1mpassed[0m 53A513C0 000.00s IE_Ran_Nas_Cause, basic instantiation
[34m[1mpassed[0m 389D0AF5 000.00s IE_FQCSID, dissection
[34m[1mpassed[0m 6C94DDB9 000.00s IE_FQCSID, basic instantiation
[34m[1mpassed[0m AB6DF1DB 000.00s IE_FTEID, dissection
[34m[1mpassed[0m 90D049F4 000.00s IE_FTEID, basic instantiation
[34m[1mpassed[0m 112E74BF 000.00s IE_BearerContext, dissection
[34m[1mpassed[0m CEF65F3B 000.00s IE_BearerContext, basic instantiation
[34m[1mpassed[0m 667A4D73 000.00s IE_ChargingID, dissection
[34m[1mpassed[0m A1535DB0 000.00s IE_ChargingID, basic instantiation
[34m[1mpassed[0m 07429366 000.00s IE_ChargingCharacteristics, dissection
[34m[1mpassed[0m D0A5FE91 000.00s IE_ChargingCharacteristics, basic instantiation
[34m[1mpassed[0m CF5A04A3 000.00s IE_PDN_type, dissection
[34m[1mpassed[0m F69821FB 000.00s IE_PDN_type, basic instantiation
[34m[1mpassed[0m A65C02FB 000.00s IE_UE_Timezone, dissection
[34m[1mpassed[0m 8CDCCEFC 000.00s IE_UE_Timezone, basic instantiation
[34m[1mpassed[0m E3712C0E 000.00s IE_UE_Timezone, basic instantiation
[34m[1mpassed[0m F03C04DA 000.00s IE_Port_Number, dissection
[34m[1mpassed[0m 2B7EC740 000.00s IE_Port_Number, basic instantiation
[34m[1mpassed[0m 0C09C023 000.00s IE_APN_Restriction, dissection
[34m[1mpassed[0m 46E822D5 000.00s IE_APN_Restriction, basic instantiation
[34m[1mpassed[0m 59382080 000.00s IE_SelectionMode, dissection
[34m[1mpassed[0m 56548512 000.00s IE_SelectionMode, basic instantiation
[34m[1mpassed[0m 896BAB27 000.01s IE_MMBR, dissection
[34m[1mpassed[0m AFF3EE0B 000.00s IE_MMBR, basic instantiation
[34m[1mpassed[0m 713402DB 000.00s GTPHeader isn't an answer to not GTPHeader instance
[34m[1mpassed[0m ED69846D 000.00s GTPHeader is an answer to a message with the same sequence number
[34m[1mpassed[0m C40F65BD 000.00s GTPHeader isn't an answer to a message with a different sequence number
[34m[1mpassed[0m 062A35E1 000.00s GTPV2EchoResponse answers
[34m[1mpassed[0m B553F724 000.00s GTPHeader post_build
[34m[1mpassed[0m 041FCA99 000.00s GTPHeader hashret
[34m[1mpassed[0m 1A5D25DB 000.00s IE_NotImplementedTLV
[34m[1mpassed[0m 93FE8D3D 000.00s IE_PrivateExtension, dissection
[34m[1mpassed[0m 4F4A99C0 000.00s IE_PrivateExtension, basic instantiation
Campaign CRC=EB7454CB in 000.11s SHA=B125C7BE42FD2AFB33B05843625F8093CF80A351
[34m[1mPASSED=89 FAILED=0[0m
[32m━ Loading: test/contrib/homeplugav.uts[0m
[34m[1mpassed[0m 1A00500C 000.00s Import the homeplugav layer
[34m[1mpassed[0m E23A002D 000.01s Building packets packet
[34m[1mpassed[0m 9FE0C04A 000.00s Some important manipulations
[34m[1mpassed[0m AEE5B61F 000.00s Some important fields parsing
[34m[1mpassed[0m 695F7898 000.00s Testing length and checksum on a generated Write Module Data Request
Campaign CRC=A3924A8E in 000.01s SHA=41D382EF5080D9543B8317817DA464661CAD82BF
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/homepluggp.uts[0m
[34m[1mpassed[0m A12E0547 000.00s Import the homeplugg layer
[34m[1mpassed[0m C2E5546D 000.00s Most important packet to intrude a HPGP network
[34m[1mpassed[0m F5E6FD82 000.00s Some other important parsing tests
[34m[1mpassed[0m 2373DC0F 000.00s Some important manipulations
Campaign CRC=3D3F2009 in 000.01s SHA=ABC6953DAA11A7D760B915D1F4A408A028F284CA
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/contrib/homeplugsg.uts[0m
[34m[1mpassed[0m EC8AE509 000.00s Import the homepluggq layer
[34m[1mpassed[0m 3DFAADF8 000.00s Some important manipulations
Campaign CRC=AD6BFBF2 in 000.00s SHA=C92EC446E21CBDC84E5EB2973C88286AED826382
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/contrib/http2.uts[0m
[34m[1mpassed[0m 6B7BBCB3 000.00s Configuring Scapy
[34m[1mpassed[0m 0084545B 000.00s HTTP/2 UVarIntField.any2i
[34m[1mpassed[0m AAD8F448 000.00s HTTP/2 UVarIntField.m2i on full byte
[34m[1mpassed[0m E77AC891 000.00s HTTP/2 UVarIntField.m2i on partial byte
[34m[1mpassed[0m CB7BDA87 000.00s HTTP/2 UVarIntField.getfield on full byte
[34m[1mpassed[0m 5C20EAB4 000.00s HTTP/2 UVarIntField.getfield on partial byte
[34m[1mpassed[0m E4774FEF 000.00s HTTP/2 UVarIntField.i2m on full byte
[34m[1mpassed[0m 051AB17A 000.00s HTTP/2 UVarIntField.i2m on partial byte
[34m[1mpassed[0m 89B443A3 000.00s HTTP/2 UVarIntField.addfield on full byte
[34m[1mpassed[0m 782FA12F 000.00s HTTP/2 UVarIntField.addfield on partial byte
[34m[1mpassed[0m 93538457 000.00s HTTP/2 UVarIntField.i2len on full byte
[34m[1mpassed[0m B6356041 000.00s HTTP/2 UVarIntField.i2len on partial byte
[34m[1mpassed[0m 646474E2 000.00s HTTP/2 FieldUVarLenField.i2m without adjustment
[34m[1mpassed[0m 7342AD49 000.00s HTTP/2 FieldUVarLenField.i2m with adjustment
[34m[1mpassed[0m 2A637692 001.00s HTTP/2 HPackZString Compression
[34m[1mpassed[0m AD35637E 001.89s HTTP/2 HPackZString Decompression
[34m[1mpassed[0m 6EE5C7E1 000.00s HTTP/2 HPackStrLenField.m2i
[34m[1mpassed[0m 1AFBF34B 000.00s HTTP/2 HPackStrLenField.any2i
[34m[1mpassed[0m B5F98BFA 000.00s HTTP/2 HPackStrLenField.i2m
[34m[1mpassed[0m BFC1E0CC 000.00s HTTP/2 HPackStrLenField.addfield
[34m[1mpassed[0m 73AECC2C 000.00s HTTP/2 HPackStrLenField.getfield
[34m[1mpassed[0m EBD6D752 000.00s HTTP/2 HPackStrLenField.i2h / i2repr
[34m[1mpassed[0m 0A9863C4 000.00s HTTP/2 HPackStrLenField.i2len
[34m[1mpassed[0m 33BFAEEE 000.00s HTTP/2 HPackMagicBitField.addfield
[34m[1mpassed[0m 3889AC5F 000.00s HTTP/2 HPackMagicBitField.getfield
[34m[1mpassed[0m 59DA2D0D 000.00s HTTP/2 HPackMagicBitField.h2i
[34m[1mpassed[0m EA8BC26E 000.00s HTTP/2 HPackMagicBitField.m2i
[34m[1mpassed[0m 4A4210DB 000.00s HTTP/2 HPackMagicBitField.i2m
[34m[1mpassed[0m 8470FE1C 000.00s HTTP/2 HPackMagicBitField.any2i
[34m[1mpassed[0m 2C9CC23B 000.00s HTTP/2 Dissect HPackHdrString
[34m[1mpassed[0m E42DE3AA 000.00s HTTP/2 Build HPackHdrString
[34m[1mpassed[0m 5FB1F8D6 000.00s HTTP/2 Dissect HPackIndexedHdr
[34m[1mpassed[0m 787EE8DD 000.00s HTTP/2 Build HPackIndexedHdr
[34m[1mpassed[0m 4878E38D 000.00s HTTP/2 Dissect HPackLitHdrFldWithIncrIndexing without indexed name
[34m[1mpassed[0m D0429681 000.00s HTTP/2 Dissect HPackLitHdrFldWithIncrIndexing with indexed name
[34m[1mpassed[0m FD305AF3 000.00s HTTP/2 Build HPackLitHdrFldWithIncrIndexing without indexed name
[34m[1mpassed[0m FB963641 000.00s HTTP/2 Build HPackLitHdrFldWithIncrIndexing with indexed name
[34m[1mpassed[0m 47A74E32 000.00s HTTP/2 Dissect HPackLitHdrFldWithoutIndexing : don't index and no index
[34m[1mpassed[0m DCDC3553 000.00s HTTP/2 Dissect HPackLitHdrFldWithoutIndexing : never index index and no index
[34m[1mpassed[0m 17D77A57 000.00s HTTP/2 Dissect HPackLitHdrFldWithoutIndexing : never index and indexed name
[34m[1mpassed[0m 0DCD0D40 000.00s HTTP/2 Build HPackLitHdrFldWithoutIndexing : don't index and no index
[34m[1mpassed[0m 7720EEEB 000.00s HTTP/2 Build HPackLitHdrFldWithoutIndexing : never index index and no index
[34m[1mpassed[0m F157972A 000.00s HTTP/2 Build HPackLitHdrFldWithoutIndexing : never index and indexed name
[34m[1mpassed[0m 7559F70C 000.00s HTTP/2 Dissect HPackDynamicSizeUpdate
[34m[1mpassed[0m B92657C9 000.00s HTTP/2 Build HPackDynamicSizeUpdate
[34m[1mpassed[0m 46A6ECBA 000.00s HTTP/2 Dissect Data Frame: Simple data frame
[34m[1mpassed[0m 145C703F 000.00s HTTP/2 Build Data Frame: Simple data frame
[34m[1mpassed[0m E539EE66 000.00s HTTP/2 Dissect Data Frame: Simple data frame with padding
[34m[1mpassed[0m F1C755FC 000.00s HTTP/2 Build Data Frame: Simple data frame with padding
[34m[1mpassed[0m 3321AC43 000.00s HTTP/2 Dissect Data Frame: Simple data frame with padding and end stream flag
[34m[1mpassed[0m 2CF9336A 000.00s HTTP/2 Build Data Frame: Simple data frame with padding and end stream flag
[34m[1mpassed[0m 8340F4B3 000.00s HTTP/2 Dissect Headers Frame: Simple header frame
[34m[1mpassed[0m 30A88B6B 000.00s HTTP/2 Build Headers Frame: Simple header frame
[34m[1mpassed[0m AD930112 000.00s HTTP/2 Dissect Headers Frame: Header frame with padding
[34m[1mpassed[0m 04CB4E6D 000.00s HTTP/2 Build Headers Frame: Header frame with padding
[34m[1mpassed[0m 733029A8 000.00s HTTP/2 Dissect Headers Frame: Header frame with priority
[34m[1mpassed[0m DE420A3F 000.00s HTTP/2 Build Headers Frame: Header frame with priority
[34m[1mpassed[0m EC6D06AF 000.00s HTTP/2 Dissect Headers Frame: Header frame with priority and padding and flags
[34m[1mpassed[0m 3219C62B 000.00s HTTP/2 Build Headers Frame: Header frame with priority and padding and flags
[34m[1mpassed[0m 1254FD87 000.00s HTTP/2 Dissect Priority Frame
[34m[1mpassed[0m 635777FE 000.00s HTTP/2 Build Priority Frame
[34m[1mpassed[0m 1A462781 000.00s HTTP/2 Dissect Reset Stream Frame: Protocol Error
[34m[1mpassed[0m 9FCF810F 000.00s HTTP/2 Build Reset Stream Frame: Protocol Error
[34m[1mpassed[0m DCE3FA2F 000.00s HTTP/2 Dissect Reset Stream Frame: Raw 123456 error
[34m[1mpassed[0m 16EAB2CE 000.00s HTTP/2 Dissect Reset Stream Frame: Raw 123456 error
[34m[1mpassed[0m D235EB3C 000.00s HTTP/2 Dissect Settings Frame: Settings Frame
[34m[1mpassed[0m F403C17E 000.00s HTTP/2 Build Settings Frame: Settings Frame
[34m[1mpassed[0m B13CCB81 000.00s HTTP/2 Dissect Settings Frame: Incomplete Settings Frame
[34m[1mpassed[0m 000222A2 000.00s HTTP/2 Dissect Settings Frame: Settings Frame acknowledgement
[34m[1mpassed[0m 51886635 000.00s HTTP/2 Build Settings Frame: Settings Frame acknowledgement
[34m[1mpassed[0m 256F1BFD 000.00s HTTP/2 Dissect Push Promise Frame: no flag & headers with compression and hdr_name
[34m[1mpassed[0m 47DFE052 000.00s HTTP/2 Build Push Promise Frame: no flag & headers with compression and hdr_name
[34m[1mpassed[0m 4A095BC9 000.00s HTTP/2 Dissect Push Promise Frame: with padding, the flag END_Header & headers with compression and hdr_name
[34m[1mpassed[0m A73348B2 000.00s HTTP/2 Build Push Promise Frame: with padding, the flag END_Header & headers with compression and hdr_name
[34m[1mpassed[0m D3D38CB7 000.00s HTTP/2 Dissect Ping Frame: Ping frame
[34m[1mpassed[0m 33FDC369 000.00s HTTP/2 Build Ping Frame: Ping frame
[34m[1mpassed[0m FCE3DB2F 000.00s HTTP/2 Dissect Ping Frame: Pong frame
[34m[1mpassed[0m 208275B1 000.00s HTTP/2 Dissect Ping Frame: Pong frame
[34m[1mpassed[0m B18DEC9F 000.00s HTTP/2 Dissect Go Away Frame: No error
[34m[1mpassed[0m 137B5DF2 000.00s HTTP/2 Build Go Away Frame: No error
[34m[1mpassed[0m 4DFC6C79 000.00s HTTP/2 Dissect Go Away Frame: Arbitrary error with additional data
[34m[1mpassed[0m C4A63A1E 000.00s HTTP/2 Build Go Away Frame: Arbitrary error with additional data
[34m[1mpassed[0m 71ED5774 000.00s HTTP/2 Dissect Window Update Frame: global
[34m[1mpassed[0m 4D311332 000.00s HTTP/2 Build Window Update Frame: global
[34m[1mpassed[0m 4C188615 000.00s HTTP/2 Dissect Window Update Frame: a stream
[34m[1mpassed[0m E699A466 000.00s HTTP/2 Build Window Update Frame: a stream
[34m[1mpassed[0m A4E7C3AC 000.00s HTTP/2 Dissect Continuation Frame: no flag & headers with compression and hdr_name
[34m[1mpassed[0m D865CC25 000.00s HTTP/2 Build Continuation Frame: no flag & headers with compression and hdr_name
[34m[1mpassed[0m 1B508D78 000.00s HTTP/2 Dissect Continuation Frame: flag END_Header & headers with compression, sensitive flag and hdr_name
[34m[1mpassed[0m 958B5419 000.00s HTTP/2 Build Continuation Frame: flag END_Header & headers with compression, sensitive flag and hdr_name
[34m[1mpassed[0m 3882CC1B 000.00s HTTP/2 HPackHdrEntry Tests
[34m[1mpassed[0m 3C90CDA0 000.00s HTTP/2 HPackHdrTable : Querying Static Entries
[34m[1mpassed[0m 1EE9F5CB 000.00s HTTP/2 HPackHdrTable : Addind Dynamic Entries without overflowing the table
[34m[1mpassed[0m FCA16C62 000.00s HTTP/2 HPackHdrTable : Querying Dynamic Entries
[34m[1mpassed[0m 462AFCB0 000.00s HTTP/2 HPackHdrTable : Addind already registered Dynamic Entries without overflowing the table
[34m[1mpassed[0m E73DBFAF 000.00s HTTP/2 HPackHdrTable : Addind Dynamic Entries and overflowing the table
[34m[1mpassed[0m 7752F90C 000.00s HTTP/2 HPackHdrTable : Resizing
[34m[1mpassed[0m 5DDDD80E 000.00s HTTP/2 HPackHdrTable : Recapping
[34m[1mpassed[0m 88CCF4F7 000.00s HTTP/2 HPackHdrTable : Generating Textual Representation
[34m[1mpassed[0m 0A71588B 000.01s HTTP/2 HPackHdrTable : Parsing Textual Representation
[34m[1mpassed[0m 034C8733 000.00s HTTP/2 HPackHdrTable : Parsing Textual Representation without body
[34m[1mpassed[0m BB422161 000.00s HTTP/2 HPackHdrTable : Parsing Textual Representation with too small max frame
[34m[1mpassed[0m C974AAF3 000.02s HTTP/2 HPackHdrTable : Parsing Textual Representation with very large header and a large authorized frame size
[34m[1mpassed[0m B9705DFD 000.03s HTTP/2 HPackHdrTable : Parsing Textual Representation with two very large headers and a large authorized frame size
[34m[1mpassed[0m D70C37B6 000.03s HTTP/2 HPackHdrTable : Parsing Textual Representation with two very large headers, a large authorized frame size and a "small" max header list size
[34m[1mpassed[0m 77D581F3 000.04s HTTP/2 HPackHdrTable : Parsing Textual Representation with sensitive headers and non-indexable ones
Campaign CRC=9D548D9B in 003.11s SHA=A54F417EC15FC32124CEAE24E2CEB785B4587A39
[34m[1mPASSED=106 FAILED=0[0m
[32m━ Loading: test/contrib/ibeacon.uts[0m
[34m[1mpassed[0m EBEB2C8D 000.00s Presence check
[34m[1mpassed[0m E7B72D0B 000.00s Apple multiple submessages
[34m[1mpassed[0m B938C12B 000.00s iBeacon (decode LE Set Advertising Data)
[34m[1mpassed[0m 129046D6 000.00s iBeacon (encode LE Set Advertising Data)
[34m[1mpassed[0m 3F3C166E 000.00s iBeacon (decode advertising frame)
[34m[1mpassed[0m 02432768 000.00s Basic overflow area packet
Campaign CRC=5DDDAEDD in 000.01s SHA=008D0B340628E36FC5B6E420D4EA7852F72D741F
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/icmp_extensions.uts[0m
[34m[1mpassed[0m 0A4809C7 000.00s Basic build
Campaign CRC=91F31A0F in 000.00s SHA=3CF87CDEC75A950AD992B9FF7F629E8DA68A7899
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/iec104.uts[0m
[34m[1mpassed[0m 68FECEC8 000.02s load the iec104 layer
[34m[1mpassed[0m 0B83A20A 000.00s class attribute generator
[34m[1mpassed[0m 10C67704 000.00s IEC60870_5_4_NormalizedFixPoint
[34m[1mpassed[0m 68961233 000.00s Iec104SequenceNumber field
[34m[1mpassed[0m D1F062EE 000.00s IEC104_U_Message
[34m[1mpassed[0m 9A39A014 000.00s IEC104_S_Message
[34m[1mpassed[0m B2724FDD 000.00s IEC104_I_Message_SeqIOA
[34m[1mpassed[0m 49CC6CF6 000.00s IEC104_I_Message_SingleIOA
[34m[1mpassed[0m 3CED541D 000.00s single IEC104 S Message
[34m[1mpassed[0m 748B02AF 000.00s double IEC104 S Message (test layer binding)
[34m[1mpassed[0m 28851C37 000.00s single IEC104 U Message
[34m[1mpassed[0m FCC4D6A4 000.00s double IEC104 U Message
[34m[1mpassed[0m 12139F91 000.07s Sequence IOA, single IO - information object types dissection
[34m[1mpassed[0m B5928067 000.07s Single IOA, single IO - information object types dissection
[34m[1mpassed[0m AB7BA36D 000.00s Sequence IOA, multiple IOs - information object types dissection
[34m[1mpassed[0m 9B41A81C 000.00s Single IOA, multiple IOs - information object types dissection
[34m[1mpassed[0m CB528B22 000.00s Sequence IOA, multiple  APDUs
[34m[1mpassed[0m C55726BD 000.00s Single IOA, multiple  APDUs
[34m[1mpassed[0m C3243803 000.01s Mixed Single and Sequence IOA, multiple APDU
[34m[1mpassed[0m D9A37AB2 000.00s I/U/S Message sequence (mixed APDUs)
[34m[1mpassed[0m 0EA27F04 000.00s ASDU allowed in given standard (examples)
[34m[1mpassed[0m 7300A3ED 000.00s BCR - binary counter reading / IEC104_IO_M_IT_NA_1 - integrated totals
[34m[1mpassed[0m E7C52ECF 000.00s DIQ - double-point information with quality descriptor / IEC104_IO_M_DP_NA_1 - double-point information without time tag
[34m[1mpassed[0m 9A35BD31 000.00s VTI - value with transient state indication / IEC104_IO_M_ST_NA_1 - step position information
[34m[1mpassed[0m 74E730A0 000.00s IEC104_IO_C_RD_NA_1 - read command (zero byte field)
Campaign CRC=24592363 in 000.22s SHA=AA01F11459DE9929A32C3885B84CD15546EEE396
[34m[1mPASSED=25 FAILED=0[0m
[32m━ Loading: test/contrib/ife.uts[0m
[34m[1mpassed[0m 3AA5B21C 000.00s build basic IFE frames
[34m[1mpassed[0m 3C057263 000.00s add padding if required
[34m[1mpassed[0m 4904C70B 000.00s variable payload
Campaign CRC=6CFB947F in 000.00s SHA=2B975AD82D9B67B320BACF3773FDCE9B11E91815
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/contrib/igmp.uts[0m
[34m[1mpassed[0m 3F4B46C6 000.00s Build IGMP - Basic
[34m[1mpassed[0m 9C7AB618 000.00s Build IGMP - Custom membership
[34m[1mpassed[0m D3B41484 000.00s Build IGMP - LG
[34m[1mpassed[0m 132D95F2 000.00s Change IGMP params
[34m[1mpassed[0m C5A19B8E 000.00s Test mysummary
[34m[1mpassed[0m 28057230 000.00s IGMP - misc
Campaign CRC=F33D0F47 in 000.01s SHA=B394C86F609BA29AC67A8D4B99562DD2E9C67F31
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/igmpv3.uts[0m
[34m[1mpassed[0m 004129E3 000.00s Build IGMPv3 - Basic
[34m[1mpassed[0m D737EF7B 000.00s Build IGMPv3 - igmpize
[34m[1mpassed[0m 9A9846E5 000.00s Dissect IGMPv3 - IGMPv3mq
[34m[1mpassed[0m 6C1A57EC 000.00s Dissect IGMPv3 - IGMPv3mr
[34m[1mpassed[0m 51FD4FC3 000.00s Dissect IGMPv3 - IGMPv3mra
[34m[1mpassed[0m 8256AC81 000.00s IGMP vs IVMPv3 tests
[34m[1mpassed[0m D087DB52 000.00s IGMPv3 - summaries
Campaign CRC=FFFC55B4 in 000.01s SHA=B6A3553EECDA3171CE1F2975E917FD437E791199
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/ikev2.uts[0m
[34m[1mpassed[0m 8BF05290 000.00s Ikev2 build
[34m[1mpassed[0m 9C8C7707 000.00s Ikev2 dissection
[34m[1mpassed[0m AEA1CD44 000.00s Build Ikev2 SA request packet
[34m[1mpassed[0m 97FD9F60 000.00s Build advanced IKEv2
[34m[1mpassed[0m BE61A8A9 000.00s Dissect Initiator Request
[34m[1mpassed[0m CC4CBBA8 000.00s Dissect Responder Response
[34m[1mpassed[0m 87DD53AE 000.00s Dissect Encrypted Inititor Request
[34m[1mpassed[0m C0795CDB 000.00s Dissect Encrypted Responder Response
[34m[1mpassed[0m 69F3050A 000.02s Test Certs detection
[34m[1mpassed[0m 47339FB5 000.02s Test Certs length calculations
[34m[1mpassed[0m 430ECD13 000.00s Test TrafficSelector detection
[34m[1mpassed[0m 5F56A739 000.00s Test TSi with multiple TrafficSelector dissection
[34m[1mpassed[0m 6DF81A28 000.00s Test automatic calculation of number_of_TSs field
[34m[1mpassed[0m C324D073 000.00s IKEv2_payload_Encrypted_Fragment, simple tests
Campaign CRC=68968918 in 000.05s SHA=F6F70C9C828E678B23C6C229716978E48614DC75
[34m[1mPASSED=14 FAILED=0[0m
[32m━ Loading: test/contrib/isis.uts[0m
[34m[1mpassed[0m 48B839C0 000.00s Import the isis layer
[34m[1mpassed[0m C6881BFB 000.00s Layer Binding
[34m[1mpassed[0m 23A30FEE 000.00s P2P Hello
[34m[1mpassed[0m 0F5E9E6B 000.02s LSP
[34m[1mpassed[0m BFB3DC11 000.09s LSP with Sub-TLVs
Campaign CRC=7CD3D2A9 in 000.11s SHA=A5578B4E4972329B5D8763FF57229B87E99565E7
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/isotp_message_builder.uts[0m
[34m[1mpassed[0m 1F431143 000.00s Definition of utility functions
[34m[1mpassed[0m 488D7E38 000.02s Import isotp
[34m[1mpassed[0m F6960BC4 000.00s Create ISOTPMessageBuilder
[34m[1mpassed[0m 58CA1293 000.00s Feed packets to machine
[34m[1mpassed[0m C6D997D0 000.00s Verify there is a ready message in the machine
[34m[1mpassed[0m 8DE75BC5 000.00s Extract the message from the machine
[34m[1mpassed[0m 7E213004 000.00s Verify that no error happens when there is not enough data
[34m[1mpassed[0m 2040AA9F 000.00s Verify that no error happens when there is no data
[34m[1mpassed[0m 65398DD3 000.00s Verify a single frame without EA
[34m[1mpassed[0m 4EDEEF08 000.00s Single frame without EA, with excessive bytes in CAN frame
[34m[1mpassed[0m 6B86C209 000.00s Verify a single frame with EA
[34m[1mpassed[0m B3B2A1A0 000.00s Single CAN frame that has 2 valid interpretations
[34m[1mpassed[0m 7E714495 000.00s Verify multiple frames with EA
[34m[1mpassed[0m 44CC60DF 000.00s Verify multiple frames with EA 2
[34m[1mpassed[0m AFE4859A 000.00s Verify that an EA starting with 1 will still work
[34m[1mpassed[0m 741292F7 000.00s Verify that an EA of 07 will still work
[34m[1mpassed[0m 308230AD 000.00s Verify that three interleaved messages can be sniffed simultaneously on the same identifier and extended address (very unrealistic)
[34m[1mpassed[0m 5C372A83 000.00s Verify multiple frames with EA from list
[34m[1mpassed[0m 7F87CC28 000.00s Verify multiple frames with EA from list and iterator
[34m[1mpassed[0m D6FDA5AA 000.00s Verify a single frame without EA and different basecls
Campaign CRC=6437C879 in 000.04s SHA=249575A7FDD1B700FE294FFB4FC572B3FE7ACA38
[34m[1mPASSED=20 FAILED=0[0m
[32m━ Loading: test/contrib/isotp_native_socket.uts[0m
[31m[1mfailed[0m 68248430 000.01s Imports
[34m[1mpassed[0m 1F431143 000.00s Definition of constants, utility functions and mock classes
[31m[1mfailed[0m 26485E40 000.00s Compatibility with isotpsend
[31m[1mfailed[0m 36667A49 000.00s Compatibility with isotpsend - extended addresses
[31m[1mfailed[0m B886C062 000.00s Compatibility with isotprecv
[31m[1mfailed[0m 347AD227 000.00s Compatibility with isotprecv - extended addresses
[31m[1mfailed[0m CEE5A9CA 000.00s Create ISOTP socket
[31m[1mfailed[0m 1EC041CE 000.00s Send single frame ISOTP message
[31m[1mfailed[0m BEE44263 000.00s Send single frame ISOTP message Test init with CANSocket
[31m[1mfailed[0m 09D3505B 000.00s Test init with wrong type
[31m[1mfailed[0m 8E0A236F 000.00s Send two-frame ISOTP message
[31m[1mfailed[0m 86A45491 000.00s Send a single frame ISOTP message with padding
[31m[1mfailed[0m A112FA69 000.00s Send a two-frame ISOTP message with padding
[31m[1mfailed[0m 182113F0 000.00s Receive a padded single frame ISOTP message with padding disabled
[31m[1mfailed[0m 57FCD3BA 000.00s Receive a padded single frame ISOTP message with padding enabled
[31m[1mfailed[0m F66DCEB9 000.00s Receive a non-padded single frame ISOTP message with padding enabled
[31m[1mfailed[0m 5ED38388 000.00s Receive a padded two-frame ISOTP message with padding enabled
[31m[1mfailed[0m BF4FEFAF 000.00s Receive a padded two-frame ISOTP message with padding disabled
[31m[1mfailed[0m 22BAF48E 000.00s Receive a single frame ISOTP message
[31m[1mfailed[0m 42D81F48 000.00s Receive a single frame ISOTP message, with extended addressing
[31m[1mfailed[0m 169718A8 000.00s Receive a two-frame ISOTP message
[31m[1mfailed[0m F02357BA 000.00s Receive a two-frame ISOTP message and test python with statement
[31m[1mfailed[0m FF736300 000.00s ISOTP Socket sr1 test
[31m[1mfailed[0m C1CECEE4 000.00s ISOTP Socket sr1 and ISOTP test
[31m[1mfailed[0m 566E30A1 000.00s ISOTP Socket sr1 and ISOTP test vice versa
[31m[1mfailed[0m 8C1E9735 000.00s ISOTP Socket sniff
[34m[1mpassed[0m 0F833B1C 000.00s Cleanup reference to ISOTPSoftSocket to let the thread end
[31m[1mfailed[0m F073FC1C 000.00s Delete vcan interfaces
Campaign CRC=C27D0795 in 000.02s SHA=33BF75ACD3EAD2BA1377421E10A0005613287188
[31m[1mPASSED=2 FAILED=26[0m
[32m━ Loading: test/contrib/isotp_packet.uts[0m
[34m[1mpassed[0m E7099BD6 000.00s Import isotp
[34m[1mpassed[0m 1F431143 000.00s Define helpers
[34m[1mpassed[0m 849B0308 000.00s Creation of an empty ISOTP packet
[34m[1mpassed[0m 73245074 000.00s Creation of a simple ISOTP packet with tx_id
[34m[1mpassed[0m 420BF219 000.00s Creation of a simple ISOTP packet with ext_address
[34m[1mpassed[0m 69BA6E57 000.00s Creation of a simple ISOTP packet with rx_id
[34m[1mpassed[0m BFD2C078 000.00s Creation of a simple ISOTP packet with rx_ext_address
[34m[1mpassed[0m 5205AB0F 000.00s Creation of a simple ISOTP packet with tx_id, rx_id, ext_address, rx_ext_address
[34m[1mpassed[0m FFFE5ECD 000.00s ISOTP answers test
[34m[1mpassed[0m 00A75466 000.00s Creation of a simple ISOTP packet with tx_id validation error
[34m[1mpassed[0m D603ED0A 000.00s Creation of a simple ISOTP packet with rx_id validation error
[34m[1mpassed[0m 80923917 000.00s Creation of a simple ISOTP packet with ext_address validation error
[34m[1mpassed[0m 6A02A9B9 000.00s Creation of a simple ISOTP packet with rx_ext_address validation error
[34m[1mpassed[0m F39C167D 000.00s Build a packet with extended addressing
[34m[1mpassed[0m B8805F0B 000.00s Build a packet with normal addressing
[34m[1mpassed[0m 6EA88CCB 000.00s Compare both isotp payloads
[34m[1mpassed[0m 7069A3CD 000.00s Dissect multiple packets
[34m[1mpassed[0m 84DBBF9E 000.00s Build SF frame with constructor, check for correct length assignments
[34m[1mpassed[0m F84EFFA9 000.00s Build SF frame EA with constructor, check for correct length assignments
[34m[1mpassed[0m 11C197FB 000.00s Build FF frame with constructor, check for correct length assignments
[34m[1mpassed[0m 3F3D703C 000.00s Build FF frame EA with constructor, check for correct length assignments
[34m[1mpassed[0m D79DA369 000.00s Build FF frame EA, extended size, with constructor, check for correct length assignments
[34m[1mpassed[0m 6EE663A3 000.00s Build FF frame, extended size, with constructor, check for correct length assignments
[34m[1mpassed[0m E9F4AC99 000.00s Build CF frame with constructor, check for correct length assignments
[34m[1mpassed[0m 95355E36 000.00s Build CF frame EA with constructor, check for correct length assignments
[34m[1mpassed[0m 2E8D73F7 000.00s Build FC frame EA with constructor, check for correct length assignments
[34m[1mpassed[0m FF37ADDF 000.00s Build FC frame with constructor, check for correct length assignments
[34m[1mpassed[0m B3FB3016 000.00s Construct some single frames
[34m[1mpassed[0m 9BF1BC49 000.00s Construct some single frames EA
[34m[1mpassed[0m 072033A4 000.00s Construct ISOTP_packet with extended can frame
[34m[1mpassed[0m DE26FD4E 000.00s Construct ISOTPEA_Packet with extended can frame
[34m[1mpassed[0m EB257C3B 000.00s Fragment an empty ISOTP message
[34m[1mpassed[0m 513C5830 000.00s Fragment another empty ISOTP message
[34m[1mpassed[0m A3F523CC 000.00s Fragment a 4 bytes long ISOTP message
[34m[1mpassed[0m 5B115042 000.00s Fragment a 4 bytes long ISOTP message extended
[34m[1mpassed[0m A14C6FE8 000.00s Fragment a 8 bytes long ISOTP message extended
[34m[1mpassed[0m BFE83FBB 000.00s Fragment a 7 bytes long ISOTP message
[34m[1mpassed[0m 55BB0ACC 000.00s Fragment a 8 bytes long ISOTP message
[34m[1mpassed[0m 98A6931E 000.00s Fragment an ISOTP message with extended addressing
[34m[1mpassed[0m D4C5D288 000.00s Fragment a 7 bytes ISOTP message with destination identifier
[34m[1mpassed[0m 48B48945 000.00s Fragment a 16 bytes ISOTP message with extended addressing
[34m[1mpassed[0m 26BE3E40 000.01s Fragment a huge ISOTP message, 4997 bytes long
[34m[1mpassed[0m CD680A75 000.00s Defragment a single-frame ISOTP message
[34m[1mpassed[0m 2A854F8A 000.00s Defragment non ISOTP message
[34m[1mpassed[0m 0734BF26 000.00s Defragment ISOTP message with warning
[34m[1mpassed[0m F9959005 000.00s Defragment exception
[34m[1mpassed[0m 4CCF5A19 001.17s Fragment exception
[34m[1mpassed[0m 2C0DDA77 000.00s Defragment an ISOTP message composed of multiple CAN frames
[34m[1mpassed[0m FB1A1DD4 000.02s Check if fragmenting a message and defragmenting it back yields the original message
[34m[1mpassed[0m DBBFC033 000.00s Defragment an ambiguous CAN frame
Campaign CRC=628ADFD4 in 001.23s SHA=E36EC4DE2BE7A1878DD417D4EB559DC4858D7F56
[34m[1mPASSED=50 FAILED=0[0m
[32m━ Loading: test/contrib/isotp_soft_socket.uts[0m
[34m[1mpassed[0m 440F6D95 000.00s Imports
[34m[1mpassed[0m 987BF108 000.00s Redirect logging
[34m[1mpassed[0m 1F431143 000.00s Definition of utility functions
[34m[1mpassed[0m AAB25AA8 000.00s Test sniffer with multiple frames
[34m[1mpassed[0m 4F963715 000.01s Single-frame receive
[34m[1mpassed[0m 63E17D40 000.01s Single-frame send
[34m[1mpassed[0m F5EFDD67 000.01s Two frame receive
[34m[1mpassed[0m 27AEC363 000.33s 20000 bytes receive
[34m[1mpassed[0m F8131715 000.55s 20000 bytes send
[34m[1mpassed[0m 468C4F4C 000.00s Close ISOTPSoftSocket
[34m[1mpassed[0m 181F2B14 000.00s Test on_recv function with single frame
[34m[1mpassed[0m 1302D3C9 000.00s Test on_recv function with empty frame
[34m[1mpassed[0m 5E84F436 000.00s Test on_recv function with single frame and extended addressing
[34m[1mpassed[0m 1F4EE6EF 000.00s CF is sent when first frame is received
[34m[1mpassed[0m FC8F2029 000.00s Verify that packets are not lost if they arrive before the sniff() is called
[34m[1mpassed[0m 71F17150 000.01s Send single frame ISOTP message, using send
[34m[1mpassed[0m 610D2417 000.52s Send many single frame ISOTP messages, using send
[34m[1mpassed[0m 4FCFA469 000.01s Send two-frame ISOTP message, using send
[34m[1mpassed[0m 21D6E41E 000.01s Send single frame ISOTP message
[34m[1mpassed[0m EDD1481D 000.02s Send two-frame ISOTP message
[34m[1mpassed[0m AC4DA037 000.02s Send two-frame ISOTP message with bs
[34m[1mpassed[0m 5CBC5154 000.04s Send two-frame ISOTP message with ST
[34m[1mpassed[0m B6487EEA 000.01s Receive a single frame ISOTP message
[34m[1mpassed[0m 024DC193 000.01s Receive a single frame ISOTP message, with extended addressing
[34m[1mpassed[0m 9DC6C54F 000.01s Receive frames from CandumpReader
[34m[1mpassed[0m 426B948A 001.00s Receive frames from CandumpReader with ISOTPSniffer without extended addressing
[34m[1mpassed[0m F887197D 001.00s Receive frames from CandumpReader with ISOTPSniffer
[34m[1mpassed[0m C4E3FAFD 000.00s Receive frames from CandumpReader with ISOTPSniffer and count
[34m[1mpassed[0m 714E9534 000.00s ISOTPSession tests
[34m[1mpassed[0m 0A854DA4 000.01s Receive a two-frame ISOTP message
[34m[1mpassed[0m 7EF9A0B9 000.00s Check what happens when a CAN frame with wrong identifier gets received
[34m[1mpassed[0m 4B85C9FC 000.10s Check if not sending the last CF will make the socket timeout
[34m[1mpassed[0m 60771DFC 000.10s Check if not sending the first CF will make the socket timeout
[34m[1mpassed[0m 6BB0DF79 001.30s Check if not sending the first FC will make the socket timeout
[34m[1mpassed[0m F78E352C 001.30s Check if not sending the second FC will make the socket timeout
[34m[1mpassed[0m 6054E6E7 001.30s Check if reception of an overflow FC will make a send fail
[34m[1mpassed[0m C9364F88 000.02s ISOTPSoftSocket sr1
[34m[1mpassed[0m FF1253B6 000.06s ISOTPSoftSocket sniff
[34m[1mpassed[0m E143A0C1 000.02s bridge and sniff with isotp soft sockets set up vcan0 and vcan1 for package forwarding vcan1
[34m[1mpassed[0m CE3A3513 000.05s bridge and sniff with isotp soft sockets and multiple long packets
[34m[1mpassed[0m A37AE1B8 000.02s bridge and sniff with isotp soft sockets set up vcan0 and vcan1 for package change vcan1
[34m[1mpassed[0m 6772E596 000.02s Two ISOTPSoftSockets at the same time, sending and receiving
[34m[1mpassed[0m F4F9DD1B 000.03s Two ISOTPSoftSockets at the same time, sending and receiving with tx_gap
[34m[1mpassed[0m 2C30A55E 000.08s Two ISOTPSoftSockets at the same time, multiple sends/receives
[34m[1mpassed[0m 27FE13B7 000.01s Send a single frame ISOTP message with padding
[34m[1mpassed[0m 4378C5BB 000.01s Send a two-frame ISOTP message with padding
[34m[1mpassed[0m C84F4F00 000.01s Receive a padded single frame ISOTP message with padding disabled
[34m[1mpassed[0m 15DD7950 000.01s Receive a padded single frame ISOTP message with padding enabled
[34m[1mpassed[0m A74F4586 000.01s Receive a non-padded single frame ISOTP message with padding enabled
[34m[1mpassed[0m 908BBB43 000.01s Receive a padded two-frame ISOTP message with padding enabled
[34m[1mpassed[0m C1F7BEAE 000.01s Receive a padded two-frame ISOTP message with padding disabled
[34m[1mpassed[0m 1063FA94 000.00s Delete testsockets
Campaign CRC=BCE3B8B0 in 008.05s SHA=141A663FDFB49CFDDA3F69F4D73D854C5B45AD33
[34m[1mPASSED=52 FAILED=0[0m
[32m━ Loading: test/contrib/isotpscan.uts[0m
Campaign CRC=8E0BE5A1 in 000.00s SHA=449482E66B9F6155399759931CE136CE4E182908
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/contrib/knx.uts[0m
[34m[1mpassed[0m 081615E0 000.00s Import the knx layer
[34m[1mpassed[0m 9719E962 000.00s Header default values
[34m[1mpassed[0m 9BC0B4D9 000.00s KNX Header payload length calculation
[34m[1mpassed[0m 862C696E 000.00s KNX Header Guess Payload KNXSearchRequest
[34m[1mpassed[0m 0A51A595 000.00s KNX Header Guess Payload KNXSearchResponse
[34m[1mpassed[0m 1CC5C01D 000.00s KNX Header Guess Payload KNXDescriptionRequest
[34m[1mpassed[0m EE16C354 000.00s KNX Header Guess Payload KNXDescriptionResponse
[34m[1mpassed[0m 15DE2884 000.00s KNX Header Guess Payload KNXConnectRequest
[34m[1mpassed[0m 6ECD3EB6 000.00s KNX Header Guess Payload KNXConnectResponse
[34m[1mpassed[0m CBB821E4 000.00s KNX Header Guess Payload KNXConnectionstateRequest
[34m[1mpassed[0m 5642D4E4 000.00s KNX Header Guess Payload KNXConnectionstateResponse
[34m[1mpassed[0m 1846D879 000.00s KNX Header Guess Payload KNXDisconnectRequest
[34m[1mpassed[0m 1DD3CC46 000.00s KNX Header Guess Payload KNXDisconnectResponse
[34m[1mpassed[0m D0E1B3EA 000.00s KNX Header Guess Payload KNXConfigurationRequest
[34m[1mpassed[0m D31D43AA 000.00s KNX Header Guess Payload KNXConfigurationACK
[34m[1mpassed[0m 12475378 000.00s KNX Header Guess Payload KNXTunnelingRequest
[34m[1mpassed[0m 27DCF38B 000.00s KNX Header Guess Payload KNXTunnelingACK
[34m[1mpassed[0m 00000000 000.00s Destination port
Campaign CRC=495EC73D in 000.01s SHA=5B54B35B877C6EB22168CA88DA5B36DD50F6D48E
[34m[1mPASSED=18 FAILED=0[0m
[32m━ Loading: test/contrib/lacp.uts[0m
[34m[1mpassed[0m 66461E2C 000.00s Build & dissect LACP
[34m[1mpassed[0m AA98A824 000.00s Marker sanity
Campaign CRC=05C07EAE in 000.00s SHA=2C34784435DD00471CDC445023C2019A7E2A87C5
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/contrib/ldp.uts[0m
[34m[1mpassed[0m 8FD77C79 000.01s Default build
[34m[1mpassed[0m 3EBF265F 000.00s Basic dissection
[34m[1mpassed[0m 81543C2A 000.00s Build advanced LDPInit()
[34m[1mpassed[0m BCFE6B24 000.00s Build advanced LDPAddress() with LDPLabelMM()
[34m[1mpassed[0m 9EEB302F 000.00s Advanced dissection - complex LDP
Campaign CRC=A83FD8A3 in 000.01s SHA=D234A80818103B831F407E5E8F989012BA86218B
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/lldp.uts[0m
[34m[1mpassed[0m A39ADFC2 000.00s build basic LLDP frames
[34m[1mpassed[0m 9540793D 000.00s build: check length calculation (#GH3107)
[34m[1mpassed[0m 17D3CC70 000.01s add padding if required
[34m[1mpassed[0m F921276E 000.00s Dissection: PtopoChassisIdType == chasIdPtopoGenAddr(5)
[34m[1mpassed[0m C9184D02 000.00s Advanced test: check definitions and length of complex IDs
[34m[1mpassed[0m 983B526E 000.01s basic frame structure
[34m[1mpassed[0m DE7F62CC 000.01s basic frame structure
[34m[1mpassed[0m BFA091E9 000.01s length fields / value sizes checks
[34m[1mpassed[0m 73A58140 000.01s test attribute values
[34m[1mpassed[0m 0370BB45 000.00s ThreeBytesEnumField tests
[34m[1mpassed[0m C9664E44 000.00s LLDPDUGenericOrganisationSpecific tests
Campaign CRC=F473A995 in 000.05s SHA=D8AC5C38BFAD41137046E454C340EE53CB6998AA
[34m[1mPASSED=11 FAILED=0[0m
[32m━ Loading: test/contrib/loraphy2wan.uts[0m
[34m[1mpassed[0m 5894C60C 000.00s Import the loraphy2wan layer
[34m[1mpassed[0m 68D39E3B 000.00s Packet decoding
[34m[1mpassed[0m 61C8C460 000.00s Decoding an encrypted JA packet
[34m[1mpassed[0m C6C1A38B 000.00s Packet crafting: generating an unencrypted JA frame
[34m[1mpassed[0m E4E49337 000.00s Generating an unencrypted LoRa JA packet
[34m[1mpassed[0m EA188F0E 000.00s Parsing Piggy back commands
Campaign CRC=43B7CC6F in 000.00s SHA=A28A99A05118E894171521FA1A85DEC7553E268A
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/ltp.uts[0m
[34m[1mpassed[0m 03233B00 000.01s Build packets & dissect
Campaign CRC=A3340398 in 000.01s SHA=8287C0969F0DB08AF6F59BC2873E88CD4172796D
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/mac_control.uts[0m
[34m[1mpassed[0m D726B2C9 000.00s pause frame
[34m[1mpassed[0m F7601BED 000.00s gate frame
[34m[1mpassed[0m 543F0919 000.00s report frame
[34m[1mpassed[0m AAF219CE 000.00s report frame flags (generic for all other register frame types)
[34m[1mpassed[0m AA4BD65F 000.00s register_req frame
[34m[1mpassed[0m 4564BE5E 000.00s register frame
[34m[1mpassed[0m 4E10B3F9 000.00s register_ack frame
[34m[1mpassed[0m F8908B5C 000.00s class based flow control frame
[34m[1mpassed[0m CBF9EE83 000.00s naked frame
[34m[1mpassed[0m 7665EC39 000.00s single vlan tag
[34m[1mpassed[0m FC5D175F 000.00s QinQ
[34m[1mpassed[0m 43C0F5E7 000.00s hand craftet payload (disabled auto padding)
Campaign CRC=E4BF936B in 000.01s SHA=9FC9B795BEA7B091E5F929B0618F25A5BD5024BF
[34m[1mPASSED=12 FAILED=0[0m
[32m━ Loading: test/contrib/macsec.uts[0m
[34m[1mpassed[0m 2B3A721B 000.00s MACsec - basic encap - encrypted
[31m[1mfailed[0m 196D93C5 000.00s MACsec - basic encryption - encrypted
[31m[1mfailed[0m 5C23C2F1 000.00s MACsec - basic decryption - encrypted
[31m[1mfailed[0m E4B190BA 000.00s MACsec - basic decap - decrypted
[34m[1mpassed[0m 399DE717 000.00s MACsec - basic encap - integrity only
[31m[1mfailed[0m C019E0DC 000.00s MACsec - basic encryption - integrity only
[31m[1mfailed[0m B7992A7C 000.00s MACsec - basic decryption - integrity only
[31m[1mfailed[0m 4C24A304 000.00s MACsec - basic decap - integrity only
[34m[1mpassed[0m E690E944 000.00s MACsec - encap - shortlen 2
[34m[1mpassed[0m AADF6437 000.00s MACsec - encap - shortlen 10
[34m[1mpassed[0m EB048049 000.00s MACsec - encap - shortlen 18
[34m[1mpassed[0m DEEC66D4 000.00s MACsec - encap - shortlen 32
[34m[1mpassed[0m F92EA610 000.00s MACsec - encap - shortlen 40
[34m[1mpassed[0m BA2CC9A8 000.00s MACsec - encap - shortlen 47
[34m[1mpassed[0m 661F45FC 000.00s MACsec - encap - shortlen 0 (48)
[34m[1mpassed[0m 3821B35B 000.00s MACsec - encap - shortlen 2/nosci
[34m[1mpassed[0m F432DC4F 000.00s MACsec - encap - shortlen 32/nosci
[34m[1mpassed[0m 90F27333 000.00s MACsec - encap - shortlen 47/nosci
[31m[1mfailed[0m A70C387E 000.00s MACsec - authenticate
[34m[1mpassed[0m 5E7C7F0B 000.00s MACsec - authenticate - invalid packet
[31m[1mfailed[0m 4D4CEA0F 000.00s MACsec - decrypt
[34m[1mpassed[0m 629E0231 000.00s MACsec - decrypt - invalid packet
[34m[1mpassed[0m 942F9D63 000.00s MACsec - decap - non-Ethernet
[34m[1mpassed[0m 25C2737D 000.00s MACsec - decap - non-MACsec
[34m[1mpassed[0m 15DB0FB2 000.00s MACsec - encap - non-Ethernet
[31m[1mfailed[0m 6E4A4EB9 000.00s MACsec - Standard Test Vectors - C.1.1 GCM-AES-128 (54-octet frame integrity protection)
[31m[1mfailed[0m D1E3F5E2 000.00s MACsec - Standard Test Vectors - C.1.2 GCM-AES-256 (54-octet frame integrity protection)
[31m[1mfailed[0m 0251EACF 000.00s MACsec - Standard Test Vectors - C.1.3 GCM-AES-XPN-128 (54-octet frame integrity protection)
[31m[1mfailed[0m 8641353C 000.00s MACsec - Standard Test Vectors - C.1.4 GCM-AES-XPN-256 (54-octet frame integrity protection)
[31m[1mfailed[0m 05078ADE 000.00s MACsec - Standard Test Vectors - C.5.1 GCM-AES-128 (54-octet frame confidentiality protection)
[31m[1mfailed[0m C4FC6762 000.00s MACsec - Standard Test Vectors - C.5.2 GCM-AES-256 (54-octet frame confidentiality protection)
[31m[1mfailed[0m F2E67BBB 000.00s MACsec - Standard Test Vectors - C.5.3 GCM-AES-XPN-128 (54-octet frame confidentiality protection)
[31m[1mfailed[0m 72EC7FAC 000.00s MACsec - Standard Test Vectors - C.5.4 GCM-AES-XPN-256 (54-octet frame confidentiality protection)
Campaign CRC=080ECE71 in 000.05s SHA=1481F4900258E65922FF222CA1C8DDE7CB5BF9CC
[31m[1mPASSED=17 FAILED=16[0m
[32m━ Loading: test/contrib/modbus.uts[0m
[34m[1mpassed[0m 32BE9D8F 000.00s Import the modbus layer
[34m[1mpassed[0m B1B57563 000.00s MBAP default values
[34m[1mpassed[0m 78F0EDAC 000.00s MBAP payload length calculation
[34m[1mpassed[0m 4EBDBD01 000.00s MBAP Guess Payload ModbusPDU01ReadCoilsRequest (simple case)
[34m[1mpassed[0m 6169E561 000.00s MBAP Guess Payload ModbusPDU01ReadCoilsResponse
[34m[1mpassed[0m D8C79702 000.00s MBAP Guess Payload ModbusPDU01ReadCoilsError
[34m[1mpassed[0m A706009B 000.00s MBAP Guess Payload ModbusPDU02ReadDiscreteInputsRequest
[34m[1mpassed[0m FC3432A9 000.00s MBAP Guess Payload ModbusPDU02ReadDiscreteInputsResponse
[34m[1mpassed[0m 9F5CF2DD 000.00s MBAP Guess Payload ModbusPDU02ReadDiscreteInputsError
[34m[1mpassed[0m 01014F44 000.00s MBAP Guess Payload ModbusPDU03ReadHoldingRegistersRequest
[34m[1mpassed[0m BB2F0D69 000.00s MBAP Guess Payload ModbusPDU03ReadHoldingRegistersResponse
[34m[1mpassed[0m 5A93C66E 000.00s MBAP Guess Payload ModbusPDU03ReadHoldingRegistersError
[34m[1mpassed[0m 7C3BA4DF 000.00s MBAP Guess Payload ModbusPDU04ReadInputRegistersRequest
[34m[1mpassed[0m EA6F020B 000.00s MBAP Guess Payload ModbusPDU04ReadInputRegistersResponse
[34m[1mpassed[0m 452205EC 000.00s MBAP Guess Payload ModbusPDU04ReadInputRegistersError
[34m[1mpassed[0m 2FA6F717 000.00s MBAP Guess Payload ModbusPDU05WriteSingleCoilRequest
[34m[1mpassed[0m C63C8C96 000.00s MBAP Guess Payload ModbusPDU05WriteSingleCoilResponse
[34m[1mpassed[0m 0DB51706 000.00s MBAP Guess Payload ModbusPDU05WriteSingleCoilError
[34m[1mpassed[0m 328D4E6A 000.00s MBAP Guess Payload ModbusPDU06WriteSingleRegisterRequest
[34m[1mpassed[0m F2342CFC 000.00s MBAP Guess Payload ModbusPDU06WriteSingleRegisterResponse
[34m[1mpassed[0m 62CFC502 000.00s MBAP Guess Payload ModbusPDU06WriteSingleRegisterError
[34m[1mpassed[0m A4F8FD95 000.00s MBAP Guess Payload ModbusPDU07ReadExceptionStatusRequest
[34m[1mpassed[0m 952C567E 000.00s MBAP Guess Payload ModbusPDU07ReadExceptionStatusResponse
[34m[1mpassed[0m FA1C86D0 000.00s MBAP Guess Payload ModbusPDU07ReadExceptionStatusError
[34m[1mpassed[0m 8A82D576 000.00s MBAP Guess Payload ModbusPDU08DiagnosticsRequest
[34m[1mpassed[0m 90BEBDE1 000.00s MBAP Guess Payload ModbusPDU08DiagnosticsResponse
[34m[1mpassed[0m 82B0B168 000.00s MBAP Guess Payload ModbusPDU08DiagnosticsError
[34m[1mpassed[0m 426D07CD 000.00s MBAP Guess Payload ModbusPDU0BGetCommEventCounterRequest
[34m[1mpassed[0m AB9F6B2E 000.00s MBAP Guess Payload ModbusPDU0BGetCommEventCounterResponse
[34m[1mpassed[0m 12365CC5 000.00s MBAP Guess Payload ModbusPDU0BGetCommEventCounterError
[34m[1mpassed[0m AE733A06 000.00s MBAP Guess Payload ModbusPDU0CGetCommEventLogRequest
[34m[1mpassed[0m 905D4900 000.00s MBAP Guess Payload ModbusPDU0CGetCommEventLogResponse
[34m[1mpassed[0m 854BACF6 000.00s MBAP Guess Payload ModbusPDU0CGetCommEventLogError
[34m[1mpassed[0m DC6EA838 000.00s MBAP Guess Payload ModbusPDU0FWriteMultipleCoilsRequest
[34m[1mpassed[0m 9EA3AF3C 000.00s MBAP Guess Payload ModbusPDU0FWriteMultipleCoilsResponse
[34m[1mpassed[0m 78B1FA51 000.00s MBAP Guess Payload ModbusPDU0FWriteMultipleCoilsError
[34m[1mpassed[0m D997A166 000.00s MBAP Guess Payload ModbusPDU10WriteMultipleRegistersRequest
[34m[1mpassed[0m ED17D6AF 000.00s MBAP Guess Payload ModbusPDU10WriteMultipleRegistersResponse
[34m[1mpassed[0m BD9FD047 000.00s MBAP Guess Payload ModbusPDU10WriteMultipleRegistersError
[34m[1mpassed[0m 1C6D3E22 000.00s MBAP Guess Payload ModbusPDU11ReportSlaveIdRequest
[34m[1mpassed[0m D1F210FF 000.00s MBAP Guess Payload ModbusPDU11ReportSlaveIdResponse
[34m[1mpassed[0m 2C8000A8 000.00s MBAP Guess Payload ModbusPDU11ReportSlaveIdError
[34m[1mpassed[0m E249690D 000.00s MBAP Guess Payload ModbusPDU14ReadFileRecordRequest
[34m[1mpassed[0m 5C1FDAB0 000.00s MBAP Guess Payload ModbusPDU14ReadFileRecordResponse
[34m[1mpassed[0m 2C8000A8 000.00s MBAP Guess Payload ModbusPDU14ReadFileRecordError
[34m[1mpassed[0m 0623EA37 000.00s MBAP Guess Payload ModbusPDU15WriteFileRecordRequest
[34m[1mpassed[0m 66063DDD 000.00s MBAP Guess Payload ModbusPDU15WriteFileRecordResponse
[34m[1mpassed[0m 7ACD0555 000.00s MBAP Guess Payload ModbusPDU15WriteFileRecordError
[34m[1mpassed[0m 2B3C6059 000.00s MBAP Guess Payload ModbusPDU16MaskWriteRegisterRequest
[34m[1mpassed[0m 36C0A639 000.00s MBAP Guess Payload ModbusPDU16MaskWriteRegisterResponse
[34m[1mpassed[0m 8C813A12 000.00s MBAP Guess Payload ModbusPDU16MaskWriteRegisterError
[34m[1mpassed[0m 2B3C6059 000.00s MBAP Guess Payload ModbusPDU16MaskWriteRegisterRequest
[34m[1mpassed[0m 36C0A639 000.00s MBAP Guess Payload ModbusPDU16MaskWriteRegisterResponse
[34m[1mpassed[0m 8C813A12 000.00s MBAP Guess Payload ModbusPDU16MaskWriteRegisterError
[34m[1mpassed[0m 6139355D 000.00s MBAP Guess Payload ModbusPDU17ReadWriteMultipleRegistersRequest
[34m[1mpassed[0m 98F0C200 000.00s MBAP Guess Payload ModbusPDU17ReadWriteMultipleRegistersResponse
[34m[1mpassed[0m 1C428D4D 000.00s MBAP Guess Payload ModbusPDU17ReadWriteMultipleRegistersError
[34m[1mpassed[0m DAA3962C 000.00s MBAP Guess Payload ModbusPDU18ReadFIFOQueueRequest
[34m[1mpassed[0m B473EE25 000.00s MBAP Guess Payload ModbusPDU18ReadFIFOQueueResponse
[34m[1mpassed[0m 68A1EDCD 000.00s MBAP Guess Payload ModbusPDU18ReadFIFOQueueError
[34m[1mpassed[0m D82D7FD2 000.00s MBAP Guess Payload ModbusPDU2B0EReadDeviceIdentificationRequest (2 level test)
[34m[1mpassed[0m 9CE8C8C9 000.00s MBAP Guess Payload ModbusPDU2B0EReadDeviceIdentificationResponse
[34m[1mpassed[0m 9C15531D 000.00s MBAP Guess Payload ModbusPDU2B0EReadDeviceIdentificationError
[34m[1mpassed[0m 221F237A 000.00s MBAP Guess Payload Reserved Function Request (Invalid payload)
[34m[1mpassed[0m AB7BB8D2 000.00s MBAP Guess Payload Reserved Function Response (Invalid payload)
[34m[1mpassed[0m 46C8556F 000.00s MBAP Guess Payload Reserved Function Error (Invalid payload)
[34m[1mpassed[0m 2483B7E0 000.00s MBAP Guess Payload ModbusPDU02ReadDiscreteInputsResponse
[34m[1mpassed[0m 0E664921 000.00s MBAP Guess Payload ModbusPDU02ReadDiscreteInputsResponse minimal parameters
[34m[1mpassed[0m AE03A9C9 000.00s MBAP Guess Payload ModbusPDU02ReadDiscreteInputsRequest dissection
[34m[1mpassed[0m 91E4F659 000.00s ModbusPDU02ReadDiscreteInputsError
[34m[1mpassed[0m A79B9D7F 000.00s MBAP Guess Payload User-Defined Function Request (Invalid payload)
[34m[1mpassed[0m FD679E5A 000.00s MBAP Guess Payload User-Defined Function Response (Invalid payload)
[34m[1mpassed[0m 952A10FB 000.00s MBAP Guess Payload User-Defined Function Error (Invalid payload)
[34m[1mpassed[0m 482FD5FE 000.00s Destination port
[34m[1mpassed[0m 721D2226 000.00s Source port
[34m[1mpassed[0m 4A483178 000.00s ModbusPDU01ReadCoilsRequest
[34m[1mpassed[0m BB8921B2 000.00s ModbusPDU01ReadCoilsRequest minimal parameters
[34m[1mpassed[0m A8F07100 000.00s ModbusPDU01ReadCoilsRequest dissection
[34m[1mpassed[0m 9D9C7E63 000.00s ModbusPDU01ReadCoilsResponse
[34m[1mpassed[0m 5E0C08F6 000.00s ModbusPDU01ReadCoilsResponse minimal parameters
[34m[1mpassed[0m 6F1CE4DE 000.00s ModbusPDU01ReadCoilsResponse dissection
[34m[1mpassed[0m 7B4F222E 000.00s ModbusPDU01ReadCoilsError
[34m[1mpassed[0m D8F18522 000.00s ModbusPDU81ReadCoilsError minimal parameters
[34m[1mpassed[0m 92F3CECE 000.00s ModbusPDU81ReadCoilsError dissection
[34m[1mpassed[0m 25622B90 000.00s ModbusPDU02ReadDiscreteInputsRequest
[34m[1mpassed[0m A01E957B 000.00s ModbusPDU02ReadDiscreteInputsRequest minimal parameters
[34m[1mpassed[0m D53416E9 000.00s ModbusPDU02ReadDiscreteInputsResponse
[34m[1mpassed[0m BA1B4A4A 000.00s ModbusPDU02ReadDiscreteInputsResponse minimal parameters
[34m[1mpassed[0m F0FEE8FA 000.00s ModbusPDU02ReadDiscreteInputsRequest dissection
[34m[1mpassed[0m 91E4F659 000.00s ModbusPDU02ReadDiscreteInputsError
[34m[1mpassed[0m AC130A38 000.00s ModbusPDU03ReadHoldingRegistersRequest
[34m[1mpassed[0m 4EBCCD40 000.00s ModbusPDU03ReadHoldingRegistersRequest minimal parameters
[34m[1mpassed[0m 8A69ADED 000.00s ModbusPDU03ReadHoldingRegistersResponse
[34m[1mpassed[0m 7E567E9F 000.00s ModbusPDU03ReadHoldingRegistersResponse minimal parameters
[34m[1mpassed[0m 710AF2E5 000.00s ModbusPDU03ReadHoldingRegistersResponse dissection
[34m[1mpassed[0m 839F15C6 000.00s ModbusPDU03ReadHoldingRegistersError
[34m[1mpassed[0m B8F8749E 000.00s ModbusPDU04ReadInputRegistersRequest
[34m[1mpassed[0m B8D7D1A3 000.00s ModbusPDU04ReadInputRegistersResponse
[34m[1mpassed[0m C913DEA2 000.00s ModbusPDU04ReadInputRegistersResponse minimal parameters
[34m[1mpassed[0m FAA41DCF 000.00s ModbusPDU04ReadInputRegistersError
[34m[1mpassed[0m AB7F35DC 000.00s ModbusPDU05WriteSingleCoilRequest
[34m[1mpassed[0m C7615EED 000.00s ModbusPDU05WriteSingleCoilResponse
[34m[1mpassed[0m 6C3944EF 000.00s ModbusPDU05WriteSingleCoilError
[34m[1mpassed[0m BB64897F 000.00s ModbusPDU06WriteSingleRegisterRequest
[34m[1mpassed[0m C17EECC8 000.00s ModbusPDU06WriteSingleRegisterResponse
[34m[1mpassed[0m 365A2997 000.00s ModbusPDU06WriteSingleRegisterError
[34m[1mpassed[0m 26600BBC 000.00s ModbusPDU07ReadExceptionStatusRequest
[34m[1mpassed[0m 009378D8 000.00s ModbusPDU07ReadExceptionStatusResponse
[34m[1mpassed[0m 40F48DBE 000.00s ModbusPDU07ReadExceptionStatusError
[34m[1mpassed[0m 645A5188 000.00s ModbusPDU08DiagnosticsRequest
[34m[1mpassed[0m 66252494 000.00s ModbusPDU08DiagnosticsRequest minimal parameters
[34m[1mpassed[0m F6225DF1 000.00s ModbusPDU08DiagnosticsResponse
[34m[1mpassed[0m 280C5A48 000.00s ModbusPDU08DiagnosticsResponse minimal parameters
[34m[1mpassed[0m D9A12BD4 000.00s ModbusPDU08DiagnosticsError
[34m[1mpassed[0m 7B2F46E1 000.00s ModbusPDU0BGetCommEventCounterRequest
[34m[1mpassed[0m 4576CE8F 000.00s ModbusPDU0BGetCommEventCounterResponse
[34m[1mpassed[0m E71CA811 000.00s ModbusPDU0BGetCommEventCounterError
[34m[1mpassed[0m 0652C55C 000.00s ModbusPDU0CGetCommEventLogRequest
[34m[1mpassed[0m A8CDCD0A 000.00s ModbusPDU0CGetCommEventLogResponse
[34m[1mpassed[0m B12663C3 000.00s ModbusPDU0CGetCommEventLogError
[34m[1mpassed[0m 3EAA5D20 000.00s ModbusPDU0FWriteMultipleCoilsRequest
[34m[1mpassed[0m 82778E64 000.00s ModbusPDU0FWriteMultipleCoilsRequest minimal parameters
[34m[1mpassed[0m CCD867D6 000.00s ModbusPDU0FWriteMultipleCoilsResponse
[34m[1mpassed[0m 84CDC3B0 000.00s ModbusPDU0FWriteMultipleCoilsError
[34m[1mpassed[0m 30A10866 000.00s ModbusPDU10WriteMultipleRegistersRequest
[34m[1mpassed[0m 975FDCB2 000.00s ModbusPDU10WriteMultipleRegistersRequest minimal parameters
[34m[1mpassed[0m 849F09B1 000.00s ModbusPDU10WriteMultipleRegistersResponse
[34m[1mpassed[0m 959E349D 000.00s ModbusPDU10WriteMultipleRegistersError
[34m[1mpassed[0m BA1E1F4B 000.00s ModbusPDU11ReportSlaveIdRequest
[34m[1mpassed[0m B659D6E2 000.00s ModbusPDU11ReportSlaveIdResponse minimal parameters
[34m[1mpassed[0m 69F62C02 000.00s ModbusPDU11ReportSlaveIdError
[34m[1mpassed[0m AD2CDEFD 000.00s ModbusPDU14ReadFileRecordRequest len parameters
[34m[1mpassed[0m F169AC11 000.00s ModbusPDU14ReadFileRecordRequest minimal parameters
[34m[1mpassed[0m 8F7E67A0 000.00s ModbusPDU14ReadFileRecordRequest dissection
[34m[1mpassed[0m F758F52D 000.00s ModbusPDU14ReadFileRecordResponse minimal parameters
[34m[1mpassed[0m 51720E6A 000.00s ModbusPDU14ReadFileRecordResponse dissection
[34m[1mpassed[0m 2207F055 000.00s ModbusPDU14ReadFileRecordError
[34m[1mpassed[0m FCC974B1 000.00s ModbusPDU15WriteFileRecordRequest minimal parameters
[34m[1mpassed[0m E1946343 000.00s ModbusPDU15WriteFileRecordRequest dissection
[34m[1mpassed[0m E1D2EB0D 000.00s ModbusPDU15WriteFileRecordResponse minimal parameters
[34m[1mpassed[0m 55506789 000.00s ModbusPDU15WriteFileRecordResponse dissection
[34m[1mpassed[0m 7477F6C8 000.00s ModbusPDU15WriteFileRecordError
[34m[1mpassed[0m 6DCF542E 000.00s ModbusPDU16MaskWriteRegisterRequest
[34m[1mpassed[0m 5D609073 000.00s ModbusPDU16MaskWriteRegisterResponse
[34m[1mpassed[0m AF78D1CF 000.00s ModbusPDU16MaskWriteRegisterError
[34m[1mpassed[0m F465E947 000.00s ModbusPDU17ReadWriteMultipleRegistersRequest
[34m[1mpassed[0m 037AA11B 000.00s ModbusPDU17ReadWriteMultipleRegistersRequest minimal parameters
[34m[1mpassed[0m B8F5706E 000.00s ModbusPDU17ReadWriteMultipleRegistersRequest dissection
[34m[1mpassed[0m 8B6C5B87 000.00s ModbusPDU17ReadWriteMultipleRegistersResponse
[34m[1mpassed[0m 51556AFA 000.00s ModbusPDU17ReadWriteMultipleRegistersResponse minimal parameters
[34m[1mpassed[0m 87E68255 000.00s ModbusPDU17ReadWriteMultipleRegistersResponse dissection
[34m[1mpassed[0m 714F5721 000.00s ModbusPDU17ReadWriteMultipleRegistersError
[34m[1mpassed[0m 0EFA2E1B 000.00s ModbusPDU18ReadFIFOQueueRequest
[34m[1mpassed[0m 00000000 000.00s ModbusPDU18ReadFIFOQueueResponse
[34m[1mpassed[0m E22EFD87 000.00s ModbusPDU18ReadFIFOQueueResponse
[34m[1mpassed[0m 4CA603B3 000.00s ModbusPDU18ReadFIFOQueueResponse minimal parameters
[34m[1mpassed[0m 654D68D4 000.00s ModbusPDU18ReadFIFOQueueResponse dissection
[34m[1mpassed[0m 378424E8 000.00s ModbusPDU18ReadFIFOQueueError
[34m[1mpassed[0m 2D2C2945 000.00s ModbusPDU2B0EReadDeviceIdentificationRequest
[34m[1mpassed[0m 4CF42812 000.00s ModbusPDU2B0EReadDeviceIdentificationResponse
[34m[1mpassed[0m 8F0DF808 000.00s ModbusPDU2B0EReadDeviceIdentificationResponse complete response
[34m[1mpassed[0m 82AC94C8 000.00s ModbusPDU2B0EReadDeviceIdentificationResponse dissection
[34m[1mpassed[0m 3FC872EC 000.00s ModbusPDU2B0EReadDeviceIdentificationError
Campaign CRC=745047FB in 000.05s SHA=2CA69F4D6E959A8868436DE35C6797308D4A74BE
[34m[1mPASSED=163 FAILED=0[0m
[32m━ Loading: test/contrib/mount.uts[0m
[34m[1mpassed[0m 60C96CF4 000.00s Create subpackets
[34m[1mpassed[0m DE44A0ED 000.00s Create Mount Calls
[34m[1mpassed[0m 2D0E8CA2 000.00s Create Successful Mount Replies
[34m[1mpassed[0m 3415BDE3 000.00s Create Failed Mount Replies
[34m[1mpassed[0m 85AC3302 000.01s Layer Bindings for Mount Calls
[34m[1mpassed[0m D03BF1C9 000.00s Layer Bindings for Mount Replies
[34m[1mpassed[0m 936582FF 000.00s Mount calls vs Raw strings
[34m[1mpassed[0m 7EC99D5B 000.00s Mount replies vs Raw Strings
Campaign CRC=804BD996 in 000.01s SHA=D52DFE30163BE1AF45F838816E55F7C80B12FE3B
[34m[1mPASSED=8 FAILED=0[0m
[32m━ Loading: test/contrib/mpls.uts[0m
[34m[1mpassed[0m 4FC8C629 000.00s Build & dissect - IPv4
[34m[1mpassed[0m 46CE1359 000.00s Build & dissect - IPv6
[34m[1mpassed[0m 9D054B8B 000.00s Association on IP and IPv6
Campaign CRC=B0EE5F33 in 000.00s SHA=84A1B4EAD927E3A64F7A0FBD4108882FE454AFC0
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/contrib/mqtt.uts[0m
[34m[1mpassed[0m E3845F7C 000.00s Import the MQTT layer
[34m[1mpassed[0m 7014339A 000.00s MQTTPublish, packet instantiation
[34m[1mpassed[0m F41A15D4 000.00s Fixed header and MQTTPublish, packet dissection
[34m[1mpassed[0m DD633F54 000.00s MQTTConnect, packet instantiation
[34m[1mpassed[0m C064A0B6 000.00s MQTTConnect, packet dissection
[34m[1mpassed[0m 9FE8B0D1 000.00s MQTTDisconnect
[34m[1mpassed[0m 9D1347CA 000.00s MQTTConnack, packet instantiation
[34m[1mpassed[0m 53F68D7F 000.00s MQTTConnack, packet dissection
[34m[1mpassed[0m 53FD606C 000.00s MQTTSubscribe, packet instantiation
[34m[1mpassed[0m B46AC9B7 000.00s MQTTSubscribe, packet dissection
[34m[1mpassed[0m A6E45705 000.00s MQTTSuback, packet instantiation
[34m[1mpassed[0m 2E1FA9E9 000.00s MQTTSuback, packet dissection
[34m[1mpassed[0m E5C2B2BE 000.00s MQTTUnsubscribe, packet instantiation
[34m[1mpassed[0m CC6554DE 000.00s MQTTUnsubscribe, packet dissection
[34m[1mpassed[0m 0487FC86 000.00s MQTTUnsuback, packet instantiation
[34m[1mpassed[0m 98019A1C 000.00s MQTTUnsuback, packet dissection
[34m[1mpassed[0m B4E1A02F 000.00s MQTTPubrec, packet instantiation
[34m[1mpassed[0m 84C3D298 000.00s MQTTPubrec packet dissection
[34m[1mpassed[0m 448B506A 000.00s MQTTPublish, long value
[34m[1mpassed[0m B5A28756 000.00s MQTT without payload
[34m[1mpassed[0m D294A5AD 000.00s MQTT RandVariableFieldLen
[34m[1mpassed[0m 15774812 000.00s MQTTUnsubscribe
[34m[1mpassed[0m 4CA8B2AB 000.00s MQTTSubscribe
Campaign CRC=22A6CC47 in 000.01s SHA=DA03617BF472BF3D739798D61C52A79214B283E0
[34m[1mPASSED=23 FAILED=0[0m
[32m━ Loading: test/contrib/mqttsn.uts[0m
[34m[1mpassed[0m F250DABE 000.00s Import the MQTT-SN layer
[34m[1mpassed[0m D3022D2C 000.00s MQTTSN + MQTTSNAdvertise, packet instantiation and len field adjust
[34m[1mpassed[0m 1C7B4B54 000.00s MQTTSNAdvertise, packet dissection
[34m[1mpassed[0m 2FDF474D 000.00s MQTTSNSearchGW, packet instantiation
[34m[1mpassed[0m FF682F91 000.00s MQTTSNSearchGW, packet dissection
[34m[1mpassed[0m C0EBC887 000.00s MQTTSNGwInfo, packet instantiation
[34m[1mpassed[0m ABFB947A 000.00s MQTTSN + MQTTSNGwInfo, packet instantiation and len field adjust
[34m[1mpassed[0m 5C25B52F 000.00s MQTTSNGwInfo, packet dissection
[34m[1mpassed[0m C774191D 000.00s MQTTSNGwInfo, packet dissection - invalid length
[34m[1mpassed[0m 9B6FC50E 000.00s MQTTSNConnect, packet instantiation
[34m[1mpassed[0m 89701047 000.00s MQTTSNConnect, packet dissection
[34m[1mpassed[0m 86808A7E 000.00s MQTTSNConnack, packet instantiation
[34m[1mpassed[0m 3581A384 000.00s MQTTSNConnack, packet dissection
[34m[1mpassed[0m BA1DF8C5 000.00s MQTTSNWillTopicReq, packet instantiation
[34m[1mpassed[0m 2E71D2D8 000.00s MQTTSNWillTopicReq, packet dissection
[34m[1mpassed[0m 6D3B0FEF 000.00s MQTTSNWillTopic, packet instantiation
[34m[1mpassed[0m 47F7F922 000.00s MQTTSNWillTopic, packet dissection
[34m[1mpassed[0m BC1565D9 000.00s MQTTSNWillMsgReq, packet instantiation
[34m[1mpassed[0m 2194512C 000.00s MQTTSNWillMsgReq, packet dissection
[34m[1mpassed[0m 43FADA03 000.00s MQTTSNWillMsg, packet instantiation
[34m[1mpassed[0m CFA0AB01 000.00s MQTTSNWillMsg, packet dissection
[34m[1mpassed[0m 0A802316 000.00s MQTTSNRegister, packet instantiation
[34m[1mpassed[0m 051ACC71 000.00s MQTTSNRegister, packet dissection
[34m[1mpassed[0m A941F579 000.00s MQTTSNRegack, packet instantiation
[34m[1mpassed[0m BCC82EAD 000.00s MQTTSNRegack, packet dissection
[34m[1mpassed[0m ED2A6E97 000.00s MQTTSNPublish, packet instantiation
[34m[1mpassed[0m F47C70F0 000.00s MQTTSNPublish, packet instantiation - long data
[34m[1mpassed[0m 8D698D98 000.00s MQTTSNPublish, packet dissection
[34m[1mpassed[0m FF5B7C12 000.00s MQTTSNPublish, packet dissection - long data
[34m[1mpassed[0m 68873341 000.00s MQTTSNPuback, packet instantiation
[34m[1mpassed[0m 0E9C0776 000.00s MQTTSNPuback, packet dissection
[34m[1mpassed[0m D9FE066B 000.00s MQTTSNPubcomp, packet instantiation
[34m[1mpassed[0m 449D0C6D 000.00s MQTTSNPubcomp, packet dissection
[34m[1mpassed[0m C1E6953E 000.00s MQTTSNPubrec, packet instantiation
[34m[1mpassed[0m 29739270 000.00s MQTTSNPubrec, packet dissection
[34m[1mpassed[0m E7E4D552 000.00s MQTTSNPubrel, packet instantiation
[34m[1mpassed[0m 53ADF49F 000.00s MQTTSNPubrel, packet dissection
[34m[1mpassed[0m 435E8700 000.00s MQTTSNSubscribe, packet instantiation - topic name
[34m[1mpassed[0m 8B05B65E 000.00s MQTTSNSubscribe, packet instantiation - predefined topic ID
[34m[1mpassed[0m 8381B387 000.00s MQTTSNSubscribe, packet instantiation - short topic
[34m[1mpassed[0m BC40725B 000.00s MQTTSNSubscribe, packet dissection - topic name
[34m[1mpassed[0m FE013D00 000.00s MQTTSNSubscribe, packet dissection - short topic
[34m[1mpassed[0m 4C29B267 000.00s MQTTSNSubscribe, packet dissection - predefined topic ID
[34m[1mpassed[0m DE35563A 000.00s MQTTSNSuback, packet instantiation
[34m[1mpassed[0m B9FEB304 000.00s MQTTSNSuback, packet dissection
[34m[1mpassed[0m 51A7F80C 000.00s MQTTSNUnsubscribe, packet instantiation - topic name
[34m[1mpassed[0m 7E15D043 000.00s MQTTSNUnsubscribe, packet instantiation - predefined topic ID
[34m[1mpassed[0m 7C416C40 000.00s MQTTSNUnsubscribe, packet instantiation - short topic
[34m[1mpassed[0m 3FC198C6 000.00s MQTTSNUnsubscribe, packet dissection - topic name
[34m[1mpassed[0m 16DDA911 000.00s MQTTSNUnsubscribe, packet dissection - short topic
[34m[1mpassed[0m 7058717A 000.00s MQTTSNUnsubscribe, packet dissection - predefined topic ID
[34m[1mpassed[0m 39AA9FE6 000.00s MQTTSNUnsuback, packet instantiation
[34m[1mpassed[0m 477240CE 000.00s MQTTSNUnsuback, packet dissection
[34m[1mpassed[0m 3C165855 000.00s MQTTSNPingReq, packet instantiation - no client ID
[34m[1mpassed[0m EBFF8117 000.00s MQTTSNPingReq, packet instantiation - with client ID
[34m[1mpassed[0m ED2F5F2B 000.00s MQTTSNPingReq, packet dissection
[34m[1mpassed[0m 20D2595B 000.00s MQTTSNPingResp, packet instantiation
[34m[1mpassed[0m CB1E8642 000.00s MQTTSNPingResp, packet dissection
[34m[1mpassed[0m D2E77CBA 000.00s MQTTSNDisconnect, packet instantiation and len field adjust - w/o duration
[34m[1mpassed[0m 2BB625AD 000.00s MQTTSNDisconnect, packet instantiation and len field adjust - w duration
[34m[1mpassed[0m 7984093B 000.00s MQTTSNDisconnect, packet dissection - w/o duration
[34m[1mpassed[0m 662A4C5F 000.00s MQTTSNDisconnect, packet dissection - w duration
[34m[1mpassed[0m EC244345 000.00s MQTTSNWillTopicUpd, packet instantiation
[34m[1mpassed[0m BF931796 000.00s MQTTSNWillTopicUpd, packet dissection
[34m[1mpassed[0m AB935B9A 000.00s MQTTSNWillTopicResp, packet instantiation
[34m[1mpassed[0m 9861FADD 000.00s MQTTSNWillTopicResp, packet dissection
[34m[1mpassed[0m 3F363EC5 000.00s MQTTSNWillMsgUpd, packet instantiation
[34m[1mpassed[0m 40FB19D0 000.00s MQTTSNWillMsgUpd, packet dissection
[34m[1mpassed[0m 78242D07 000.00s MQTTSNWillMsgResp, packet instantiation
[34m[1mpassed[0m 19A47237 000.00s MQTTSNWillMsgResp, packet dissection
[34m[1mpassed[0m 92D880D0 000.00s MQTTSNEncaps, packet instantiation
[34m[1mpassed[0m 9424AD47 000.00s MQTTSNEncaps, packet dissection
[34m[1mpassed[0m 965841FD 000.00s MQTTSNEncaps, packet dissection -- long payload
[34m[1mpassed[0m 8C45CF61 000.00s MQTTSN without payload
[34m[1mpassed[0m D768B275 000.00s MQTTSN without payload -- invalid lengths
[34m[1mpassed[0m 7C1C82BB 000.00s MQTT-SN RandVariableFieldLen
[34m[1mpassed[0m CD9F57F7 000.00s Disect full IPv6 packages
[34m[1mpassed[0m 6C88BAFF 000.00s UDP packet instantiation
Campaign CRC=82623D61 in 000.04s SHA=81969D56C6DB8501E2B0CC9D4AF837FC330F0747
[34m[1mPASSED=78 FAILED=0[0m
[32m━ Loading: test/contrib/nfs.uts[0m
[34m[1mpassed[0m 459DE1A4 000.00s Create subpackets
[34m[1mpassed[0m 33528A2D 000.00s Create NFS Calls
[34m[1mpassed[0m 99511DDD 000.00s Create NFS Successful replies
[34m[1mpassed[0m 162DA228 000.00s Create NFS Failed replies
[34m[1mpassed[0m 8A24391F 000.04s Layer Bindings for NFS Calls
[34m[1mpassed[0m 739C96BC 000.02s Layer Bindings for NFS Replies
[34m[1mpassed[0m 9BF1D735 000.03s Built NFS Calls vs Raw Strings
[34m[1mpassed[0m DF54C926 000.17s Built NFS Replies vs Raw Strings
Campaign CRC=98547F7E in 000.27s SHA=3AE9509BC78CAD876D73B080A56D4E4A78625F4F
[34m[1mPASSED=8 FAILED=0[0m
[32m━ Loading: test/contrib/nlm.uts[0m
[34m[1mpassed[0m 7C8F99D8 000.00s Create subpackets
[34m[1mpassed[0m 9F310C0E 000.00s Create nlm Calls
[34m[1mpassed[0m D69E10A3 000.00s Create nlm Replies
[34m[1mpassed[0m F56B404F 000.02s RPC Layer Bindings for NLM Calls
[34m[1mpassed[0m A9991254 000.01s RPC Layer Bindings for NLM Replies
[34m[1mpassed[0m 93B4FF93 000.03s Built NLM Calls vs Raw Strings
[34m[1mpassed[0m 28123A2E 000.00s NLM Replies vs Raw Strings
Campaign CRC=0D9B568A in 000.06s SHA=65617E334A5290CE502B06652C75D36285C1CEF3
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/nsh.uts[0m
[34m[1mpassed[0m AD690F56 000.00s Build a NSH over NSH packet with SPI=42, and SI=1
[34m[1mpassed[0m 64BB8051 000.00s Build a NSH with Fixed context headers
[34m[1mpassed[0m FAC78318 000.00s Build a Ethernet over NSH over Ethernet packet (NSH over Ethernet encapsulating the original packet) and verify Ethernet Bindings
[34m[1mpassed[0m 7499C9BF 000.00s Build a NSH over GRE packet, and verify GRE Bindings
[34m[1mpassed[0m F80F9EF0 000.00s 0 length variable length context header NSH
Campaign CRC=D921926D in 000.00s SHA=8F0C79A6930561A2BEFCB5757CDA63C911443C3D
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/oncrpc.uts[0m
[34m[1mpassed[0m AAD283E1 000.00s Create subpackets
[34m[1mpassed[0m C3E79625 000.00s Create ONC RPC Packets
[34m[1mpassed[0m CC49E3B8 000.00s RPC Message type
[34m[1mpassed[0m 4F70B5F3 000.01s Test Built Packets vs Raw Strings
Campaign CRC=8F681607 in 000.02s SHA=6C0FD7F658AD62970BCB07E2549EE661B3F56DA3
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/contrib/opc_da.uts[0m
[34m[1mpassed[0m 8293FDFF 000.00s OpcDaRequest
[34m[1mpassed[0m D96BF855 000.00s OpcDaRequestLE
[34m[1mpassed[0m 52F11ED4 000.00s OpcDaPing
[34m[1mpassed[0m 9835CD50 000.00s OpcDaResponse
[34m[1mpassed[0m B4DD394B 000.00s OpcDaResponseLE
[34m[1mpassed[0m A98BC079 000.00s OpcDaAlter_context
[34m[1mpassed[0m 6A2108AE 000.00s OpcDaAlter_contextLE
[34m[1mpassed[0m 00000000 000.00s OpcDaAlter_Context_Resp
[34m[1mpassed[0m 00000000 000.00s OpcDaAlter_Context_RespLE
Campaign CRC=B0683B02 in 000.01s SHA=0239F595D360E1496FE6C1E90D20FA7F2B90D8DB
[34m[1mPASSED=9 FAILED=0[0m
[32m━ Loading: test/contrib/openflow.uts[0m
[34m[1mpassed[0m 38F59B18 000.00s Be sure we have loaded OpenFlow v1
[34m[1mpassed[0m 09089A41 000.00s OFPTHello(), simple hello message
[34m[1mpassed[0m E934B3E1 000.00s OFPTEchoRequest(), echo request
[34m[1mpassed[0m 9D4580CA 000.00s OFPMatch(), check wildcard completion
[34m[1mpassed[0m C1D4D70D 000.00s OpenFlow(), generic method test with OFPTEchoRequest()
[34m[1mpassed[0m 9A19F238 000.00s OFPTFlowMod(), check codes and defaults values
[34m[1mpassed[0m A9990DBC 000.00s OFPTFlowMod(), complex flow_mod
[34m[1mpassed[0m E0F434BF 000.00s OFPETBadRequest() containing a flow_mod with wrong table_id
[34m[1mpassed[0m CD18D72C 000.00s OFPTPacketIn() containing an Ethernet frame
[34m[1mpassed[0m D9DBCA8A 000.00s OFPTStatsReplyFlow()
[34m[1mpassed[0m 51E50F0F 000.00s OFPTQueueGetConfigReply()
[34m[1mpassed[0m 03DC3BDD 000.00s OFPETHelloFailed()
[34m[1mpassed[0m 7FE6AAEE 000.00s TCP()/OFPTStatsRequestDesc(), check default sport
[34m[1mpassed[0m AD9BFE50 000.00s TCP()/OFPETHelloFailed(), check default dport
[34m[1mpassed[0m BB313B6A 000.00s TCP()/OFPTHello() dissection, check new TCP.guess_payload_class
[34m[1mpassed[0m B30648DD 000.00s complete Ether()/IP()/TCP()/OFPTFeaturesRequest()
Campaign CRC=E2F8034F in 000.01s SHA=43257405EBE3FCC68E3A8A583F6303AD3618F79D
[34m[1mPASSED=16 FAILED=0[0m
[32m━ Loading: test/contrib/openflow3.uts[0m
[34m[1mpassed[0m 7DF40AA0 000.00s Be sure we have loaded OpenFlow v3
[34m[1mpassed[0m C4EBF569 000.00s OFPTHello(), hello without version bitmap
[34m[1mpassed[0m 24D7DCC9 000.00s OFPTEchoRequest(), echo request
[34m[1mpassed[0m A3043291 000.00s OFPMatch(), check padding
[34m[1mpassed[0m 894B8B11 000.00s OpenFlow3(), generic method test with OFPTEchoRequest()
[34m[1mpassed[0m 503ED3B6 000.00s OFPTFlowMod(), check codes and defaults values
[34m[1mpassed[0m 07E71BF3 000.00s OFBIPv6ExtHdrHMID(), check creation of last OXM classes
[34m[1mpassed[0m 796168B6 000.00s OFPTFlowMod(), complex flow_mod
[34m[1mpassed[0m 94C163FD 000.00s OFPTFlowMod(), complex flow_mod - Dissection
[34m[1mpassed[0m FF10CD36 000.00s OFPFlowStats()
[34m[1mpassed[0m 0FBFA4E2 000.00s OFPETBadRequest() containing a flow_mod with wrong table_id
[34m[1mpassed[0m 1DE2694F 000.00s OFPTFPTInstructions()
[34m[1mpassed[0m CD18D72C 000.00s OFPTPacketIn() containing an Ethernet frame
[34m[1mpassed[0m 446E1A4E 000.00s OFPTGroupMod()
[34m[1mpassed[0m 749F7B44 000.00s OFPTQueueGetConfigReply()
[34m[1mpassed[0m BBB1183C 000.00s OFPMPReplyMeter()
[34m[1mpassed[0m 51006E68 000.00s OFPMPReplyMeterConfig()
[34m[1mpassed[0m 1F32C3B7 000.00s TCP()/OFPMPRequestDesc(), check default sport
[34m[1mpassed[0m AD9BFE50 000.00s TCP()/OFPETHelloFailed(), check default dport
[34m[1mpassed[0m F96A838F 000.00s TCP()/OFPTHello() dissection, check new TCP.guess_payload_class
[34m[1mpassed[0m CAD92DD3 000.00s Advanced TCP()/OFPTHello() built, with OFPHETVersionBitmap
[34m[1mpassed[0m 64078F57 000.00s complete Ether()/IP()/TCP()/OFPTFeaturesRequest()
[34m[1mpassed[0m E6B7D3F0 000.00s OFPMPRequestTableFeatures() with OFPTFPTMatch() OXMIDPacketListField tests
[34m[1mpassed[0m C7A73B48 000.00s Test OFBTCPSrc Autocompletion
Campaign CRC=2AF48F74 in 000.03s SHA=B8E52728E14E506577CB741A8CB80582BA94A795
[34m[1mPASSED=24 FAILED=0[0m
[32m━ Loading: test/contrib/ospf.uts[0m
[34m[1mpassed[0m 7200AD67 000.00s OSPF, basic instantiation
[34m[1mpassed[0m C300B5AC 000.00s OSPF - build
[34m[1mpassed[0m CD86E34A 000.00s OSPF - answers
[34m[1mpassed[0m 6DFBA085 000.00s OSPFv3 - build
[34m[1mpassed[0m 74D95569 000.00s OSPFv2 Opaque lsa
Campaign CRC=8E511AC7 in 000.01s SHA=B89032A4554203C4ABE4B8DD7815017AC602784C
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/pcom.uts[0m
[34m[1mpassed[0m 4A63DE6E 000.00s Import the pcom layer
[34m[1mpassed[0m C8239D59 000.00s PCOM/TCP Default values
[34m[1mpassed[0m 68EEB390 000.00s PCOM/TCP Len
[34m[1mpassed[0m 72382A67 000.00s PCOM/TCP Guess Payload Class
[34m[1mpassed[0m BD79F7A4 000.00s PCOM/ASCII Default values
[34m[1mpassed[0m D481B6A3 000.00s PCOM/ASCII Checksum
[34m[1mpassed[0m 8ECE6890 000.00s PCOM/ASCII Known Codes
[34m[1mpassed[0m 5FAD638C 000.00s PCOM/Binary Default values
[34m[1mpassed[0m 6825B648 000.00s PCOM/Binary Checksum
[34m[1mpassed[0m C7C76307 000.00s PCOM/Binary Known Codes
Campaign CRC=4BA4A9AD in 000.01s SHA=E4E003D5F2E99E673949A81ABFDED072DAAC29F3
[34m[1mPASSED=10 FAILED=0[0m
[32m━ Loading: test/contrib/pfcp.uts[0m
[34m[1mpassed[0m CAEAB396 000.02s Verify IEs
[34m[1mpassed[0m BB029506 001.24s Verify PCAPs
[34m[1mpassed[0m 026ED2E3 000.00s Build and dissect PFCP Association Setup Request
[34m[1mpassed[0m 8B912A8E 000.34s Build and dissect PFCP Association Setup Response
[34m[1mpassed[0m EC0B31BD 000.00s Build and dissect PFCP Session Establishment Response
[34m[1mpassed[0m C15FB1AE 000.02s Build and dissect PFCP Heartbeat Request
[34m[1mpassed[0m 2907CA1C 000.00s Build and dissect PFCP Session Report Response
[34m[1mpassed[0m 2A3A160B 000.00s Build and dissect PFCP Session Modification Request
[34m[1mpassed[0m B68ADF1B 000.01s Build and dissect PFCP Session Modification Response
[34m[1mpassed[0m 542930A5 000.01s Verify IEs
Campaign CRC=8D5EAD41 in 001.65s SHA=918D54BD63F2C7680397E0E417A074B3DBF20309
[34m[1mPASSED=10 FAILED=0[0m
[32m━ Loading: test/contrib/pim.uts[0m
[34m[1mpassed[0m AE9CA871 000.00s PIMv2 Hello - instantiation
[34m[1mpassed[0m 5DCF1417 000.00s PIMv2 Join/Prune - instantiation
[34m[1mpassed[0m 8C55EFD7 000.00s PIMv2 Hello - build
[34m[1mpassed[0m C423515F 000.01s PIMv2 Join/Prune - build
Campaign CRC=FB4EC91F in 000.02s SHA=C8D719D3AEBFA5ED8AEA58EC59B89CAA7246CD8F
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/contrib/pnio.uts[0m
[34m[1mpassed[0m 41E2EF04 000.00s Import the ProfinetIO layer
[34m[1mpassed[0m 01540E9D 000.00s ProfinetIO default values
[34m[1mpassed[0m 4C4287D4 000.00s ProfinetIO overloads Ethertype
[34m[1mpassed[0m B1E30FC3 000.00s ProfinetIO overloads UDP dport
[34m[1mpassed[0m B6D3A0AA 000.00s Ether guesses ProfinetIO as payload class
[34m[1mpassed[0m 5255596B 000.00s UDP guesses ProfinetIO as payload class
[34m[1mpassed[0m 460CF0DE 000.00s ProfinetIO PNIORealTime_IOxS parsing of a single status
[34m[1mpassed[0m 1C3D8482 000.00s ProfinetIO PNIORealTime_IOxS building of a single status
[34m[1mpassed[0m C5A58567 000.00s ProfinetIO PNIORealTime_IOxS parsing with multiple statuses
[34m[1mpassed[0m 7B72A01F 000.00s ProfinetIO RTC PDU parsing without configuration
[34m[1mpassed[0m 73AAB4A5 000.00s ProfinetIO RTC PDU building
[34m[1mpassed[0m D4D9C1C6 000.00s ProfinetIO RTC PDU parsing with config
[34m[1mpassed[0m 3B750454 000.00s PROFIsafe parsing (query with F_CRC_SEED=0)
[34m[1mpassed[0m 3F71CDDE 000.00s PROFIsafe parsing (query with F_CRC_SEED=1)
[34m[1mpassed[0m A0DDFA92 000.00s PROFIsafe parsing (response with F_CRC_SEED=0)
[34m[1mpassed[0m 879F88A7 000.00s PROFIsafe parsing (response with F_CRC_SEED=1)
[34m[1mpassed[0m 4EAA6A00 000.00s PROFIsafe building (query with F_CRC_SEED=0)
[34m[1mpassed[0m 6D25A268 000.00s PROFIsafe building (query with F_CRC_SEED=1)
[34m[1mpassed[0m 344B90D3 000.00s PROFIsafe building (response with F_CRC_SEED=0)
[34m[1mpassed[0m 705653EB 000.00s PROFIsafe building (response with F_CRC_SEED=1)
Campaign CRC=66A2AC2C in 000.02s SHA=32032CF60E4657932CEA43F1AE2462F418B29B69
[34m[1mPASSED=20 FAILED=0[0m
[32m━ Loading: test/contrib/pnio_dcp.uts[0m
[34m[1mpassed[0m 0441052D 000.00s Import the ProfinetIO layer
[34m[1mpassed[0m EDB59E8E 000.00s DCP Identify All Request parsing
[34m[1mpassed[0m 641136A6 000.00s DCP Set Request parsing
[34m[1mpassed[0m F8A42C76 000.00s DCP Identify Response parsing
[34m[1mpassed[0m D111413F 000.00s DCP Identify Response parsing with new DCP packages (DCPOEMIDBlock, DCPDeviceInitiativeBlock)
[34m[1mpassed[0m 15D62D28 000.00s DCP Set Request parsing
[34m[1mpassed[0m BD83DE1E 000.00s DCP Set Full IP Suite Request parsing
[34m[1mpassed[0m E7A5F1CC 000.00s DCP Identify All Request crafting
[34m[1mpassed[0m 42C5431C 000.00s DCP Set Name Request with specified name crafting
[34m[1mpassed[0m 8B1037BD 000.00s DCP Identify Response crafting
[34m[1mpassed[0m 353F3992 000.00s DCP Set Full IP Suite Request crafting
Campaign CRC=D416DAAB in 000.02s SHA=48B5C65132653787194696C7C2924761A7437AA2
[34m[1mPASSED=11 FAILED=0[0m
[32m━ Loading: test/contrib/pnio_rpc.uts[0m
[34m[1mpassed[0m 27AED0BF 000.00s Import the PNIO RPC layer
[34m[1mpassed[0m 7F8C76AB 000.00s Check that we have UUIDs
[34m[1mpassed[0m 37273DA1 000.00s Block default values
[34m[1mpassed[0m 4723B00E 000.00s Block basic example
[34m[1mpassed[0m 3AAA60BA 000.00s Block has no payload (only padding)
[34m[1mpassed[0m A0A1EB5A 000.00s IODControlReq default values
[34m[1mpassed[0m 405DDD2F 000.00s IODControlReq basic example (IODControlReq PrmEnd control)
[34m[1mpassed[0m BD8ECAAC 000.00s IODControlReq dissection
[34m[1mpassed[0m B0B37950 000.00s IODControlReq response
[34m[1mpassed[0m 1DD38C47 000.00s IODControlRes default values
[34m[1mpassed[0m 285842AE 000.00s IODControlRes basic example (IODControlRes PrmEnd control)
[34m[1mpassed[0m 91129611 000.00s IODControlRes dissection
[34m[1mpassed[0m 5F9A45BD 000.00s IODWriteReq default values
[34m[1mpassed[0m D2FA6368 000.00s IODWriteReq basic example
[34m[1mpassed[0m D0D77079 000.00s IODWriteReq dissection
[34m[1mpassed[0m 76F22EC9 000.00s IODWriteReq response
[34m[1mpassed[0m AA507192 000.00s IODWriteRes default values
[34m[1mpassed[0m 74785215 000.00s IODWriteRes basic example
[34m[1mpassed[0m 8F2302B3 000.00s IODWriteRes dissection
[34m[1mpassed[0m 0EF727C9 000.00s IODWriteMultipleReq default values
[34m[1mpassed[0m D384B63C 000.00s IODWriteMultipleReq basic example
[34m[1mpassed[0m 12765E4B 000.00s IODWriteMultipleReq dissection
[34m[1mpassed[0m 4D3C5823 000.00s IODWriteMultipleReq response
[34m[1mpassed[0m FB3D13E6 000.00s IODWriteMultipleRes default values
[34m[1mpassed[0m AEA91BD8 000.00s IODWriteMultipleRes basic example
[34m[1mpassed[0m F267BAAA 000.00s IODWriteMultipleRes dissection
[34m[1mpassed[0m B27FCC5C 000.00s IM0Block default values
[34m[1mpassed[0m E214B85E 000.00s IM0Block basic example
[34m[1mpassed[0m 3E1413D0 000.00s IM1Block default values
[34m[1mpassed[0m 5360F960 000.00s IM2Block default values
[34m[1mpassed[0m FDDEEC44 000.00s IM3Block default values
[34m[1mpassed[0m 03159573 000.00s IM4Block default values
[34m[1mpassed[0m B67FB6F3 000.00s ARBlockReq default values
[34m[1mpassed[0m E6A827AC 000.00s ARBlockReq basic example
[34m[1mpassed[0m 28DD4874 000.00s ARBlockReq dissection
[34m[1mpassed[0m 23C192CD 000.00s ARBlockReq response
[34m[1mpassed[0m 758652F8 000.00s ARBlockRes default values
[34m[1mpassed[0m 61F5C03B 000.00s ARBlockRes basic example
[34m[1mpassed[0m 0DCE1E48 000.00s ARBlockRes dissection
[34m[1mpassed[0m F0792407 000.00s IOCRBlockReq default values
[34m[1mpassed[0m 6E9E299C 000.00s IOCRAPI default values
[34m[1mpassed[0m 6786E049 000.00s IOCRAPIObject default values
[34m[1mpassed[0m 84040401 000.01s IOCRBlockReq basic example
[34m[1mpassed[0m 9276F521 000.01s IOCRBlockReq dissection
[34m[1mpassed[0m F2906F33 000.00s IOCRBlockReq response
[34m[1mpassed[0m B0A2519C 000.00s IOCRBlockRes default values
[34m[1mpassed[0m 0E505CD4 000.00s IOCRBlockRes basic example
[34m[1mpassed[0m 180F2289 000.00s IOCRBlockRes dissection
[34m[1mpassed[0m 83C4268C 000.00s ExpectedSubmoduleBlockReq default values
[34m[1mpassed[0m 3A5C3BE1 000.00s ExpectedSubmoduleAPI default values
[34m[1mpassed[0m 872F0837 000.00s ExpectedSubmodule default values
[34m[1mpassed[0m A78AAB69 000.00s ExpectedSubmoduleDataDescription default values
[34m[1mpassed[0m 5E5B4840 000.01s ExpectedSubmoduleBlockReq basic example
[34m[1mpassed[0m B9911D1A 000.01s ExpectedSubmoduleBlockReq dissection
[34m[1mpassed[0m 00CE5DE0 000.00s AlarmCRBlockReq default values
[34m[1mpassed[0m 5A4F19EA 000.00s AlarmCRBlockReq with transport
[34m[1mpassed[0m 69527F4B 000.00s AlarmCRBlockReq dissection
[34m[1mpassed[0m 4C8A23D4 000.00s AlarmCRBlockReq response
[34m[1mpassed[0m 5A05CE23 000.00s AlarmCRBlockRes default values
[34m[1mpassed[0m 498D9AAD 000.00s AlarmCRBlockRes dissection
[34m[1mpassed[0m 273B0EBF 000.00s PNIOServiceReqPDU basic example
[34m[1mpassed[0m 449CD09B 000.00s PNIOServiceReqPDU dissection
[34m[1mpassed[0m 03A7AE39 000.00s PNIOServiceResPDU basic example
[34m[1mpassed[0m 45C44084 000.00s PNIOServiceResPDU dissection
[34m[1mpassed[0m F58456F4 000.06s A PNIO RPC Connect Request
[34m[1mpassed[0m BCCB38CE 000.01s A PNIO RPC Write Request
[34m[1mpassed[0m D6DF22DB 000.00s A PNIO RPC PrmEnd Control Request
[34m[1mpassed[0m 428EBDEE 000.00s A PNIO RPC PrmEnd Control Request
[34m[1mpassed[0m 21861984 000.00s PNIO Alarm decoding (Alarm_Low)
[34m[1mpassed[0m 00726839 000.00s PNIO Alarm decoding (Alarm_High)
[34m[1mpassed[0m 06B0394F 000.00s PNIO Alarm DiagnosisItem
[34m[1mpassed[0m 3F55B3D1 000.00s PNIO Alarm UploadRetrievalItem
[34m[1mpassed[0m 3F46EC61 000.00s PNIO Alarm iParameterItem
[34m[1mpassed[0m B332E18E 000.00s PNIO Alarm RS_AlarmItem
[34m[1mpassed[0m 39DF1886 000.00s PNIO Alarm PRAL_AlarmItem
Campaign CRC=3422EA43 in 000.15s SHA=C2C7A01A4EFCC1FDE868C83A6D1A7A3C84945C98
[34m[1mPASSED=75 FAILED=0[0m
[32m━ Loading: test/contrib/portmap.uts[0m
[34m[1mpassed[0m 99BDD700 000.00s Create subpackets
[34m[1mpassed[0m F149786B 000.00s Create Portmap Packets
[34m[1mpassed[0m F9A09BB1 000.01s RPC Layer Bindings for Portmap calls
[34m[1mpassed[0m FEF6B9AB 000.00s RPC Layer Bindings for Portmap replies
[34m[1mpassed[0m E6755A5F 000.00s Portmap calls vs Raw Strings
[34m[1mpassed[0m CBB44E6C 000.00s Portmap replies vs Raw Strings
Campaign CRC=D3F407CD in 000.01s SHA=A09BDBB73AA5DC56F5402240CAD4931D319C3D6B
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/ppi_cace.uts[0m
[34m[1mpassed[0m 6EDC347A 000.03s Define test suite
[34m[1mpassed[0m F364CECB 000.00s Pkt_10_1
[34m[1mpassed[0m 605C6D34 000.01s Pkt_10_2
[34m[1mpassed[0m BA3ED86E 000.01s Pkt_10_3
[34m[1mpassed[0m CE5D1D05 000.01s Pkt_10_4
[34m[1mpassed[0m 94E89A66 000.01s Pkt_10_5
[34m[1mpassed[0m E7B3C0FA 000.01s Pkt_10_6
[34m[1mpassed[0m 0F1BA25D 000.01s Pkt_10_7
[34m[1mpassed[0m 7DF4AE9D 000.02s Pkt_10_8
[34m[1mpassed[0m 2B124076 000.01s Pkt_10_9
[34m[1mpassed[0m D86C63ED 000.01s Pkt_10_10
[34m[1mpassed[0m 17A20932 000.00s All-in-one packet
[34m[1mpassed[0m F56EA2C6 000.01s All-wrong-data packet
Campaign CRC=A1BC686C in 000.15s SHA=EB033ECB43C222EDCD74CEE78F1EF20E3AD57ED5
[34m[1mPASSED=13 FAILED=0[0m
[32m━ Loading: test/contrib/ppi_geotag.uts[0m
[34m[1mpassed[0m E21B2CC0 000.00s Import PPI Geotag
[34m[1mpassed[0m 0A4E973C 000.00s Test GPS dissection
[34m[1mpassed[0m 02AD4A2A 000.00s Test Vector dissection
[34m[1mpassed[0m DF6E6057 000.00s Test Sensor dissection
[34m[1mpassed[0m CE7DB03B 000.00s Test Antenna dissection
[34m[1mpassed[0m 13719EF7 000.00s Test GPSTime_Field time handling
Campaign CRC=DBC51777 in 000.00s SHA=36547F14F76B7DB87740277116A95F972B2D6AAC
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/ripng.uts[0m
[34m[1mpassed[0m 321BA0AB 000.00s Basic RIPng build
Campaign CRC=9489CFC3 in 000.00s SHA=AF5EDFF6B2B085C95304A2DA1E3CEF4438573E3F
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/roce.uts[0m
[34m[1mpassed[0m A8D115E7 000.00s RoCE layer
[34m[1mpassed[0m EC0E25D0 000.00s RoCE CNP packet
[34m[1mpassed[0m D130951A 000.00s RoCE CNP captured on ConnectX-4 Lx
[34m[1mpassed[0m E06AD740 000.00s RoCE v1 RC RDMA WRITE ONLY
[34m[1mpassed[0m BF01FEFA 000.00s RoCE v1 RC ACKNOWLEDGE
Campaign CRC=9DDDD55C in 000.01s SHA=537F00D47DB8462088CE6F033E58FBEC86A02F99
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/rpl.uts[0m
[34m[1mpassed[0m BC46C220 000.00s Import the RPL layer
[34m[1mpassed[0m 0F76260A 000.01s RPL Base Objects construction
[34m[1mpassed[0m 7F6944CE 000.00s RPL Base Objects dissection
[34m[1mpassed[0m 18CDDA0C 000.00s RPL Control Options construction
Campaign CRC=032178A4 in 000.02s SHA=F321ECA2B4F0599D019BC06F2230BAF61797AADA
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/contrib/rsvp.uts[0m
[34m[1mpassed[0m 9505AC9E 000.00s Default build
[34m[1mpassed[0m 785C0CC5 000.00s Master dissection
Campaign CRC=05745A6E in 000.00s SHA=75BEC13CE035AA4E07C01AAE17F5EF2F7B296491
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/contrib/rtcp.uts[0m
[34m[1mpassed[0m E0ACAFFF 000.00s test sender report parse
[31m[1mfailed[0m 709782AB 000.00s test receiver report parse
[34m[1mpassed[0m DE715DBB 000.00s test source description report parse
[34m[1mpassed[0m 1AF9FCC6 000.00s test parse SR and SDES stacked
Campaign CRC=DB2965FE in 000.00s SHA=2EFE2895067A050C9572850CC393C4A08154506E
[31m[1mPASSED=3 FAILED=1[0m
[32m━ Loading: test/contrib/rtr.uts[0m
[34m[1mpassed[0m 8754D4E8 000.00s default instantiation
[34m[1mpassed[0m 70508ABF 000.00s default values build
[34m[1mpassed[0m CCBE4003 000.00s filled values build
[34m[1mpassed[0m 1126113D 000.00s dissection
[34m[1mpassed[0m 26161311 000.00s default instantiation
[34m[1mpassed[0m B62E5E04 000.00s default values build
[34m[1mpassed[0m 2B913C64 000.00s filled values build
[34m[1mpassed[0m EAC9A283 000.00s dissection
[34m[1mpassed[0m 58720595 000.00s default instantiation
[34m[1mpassed[0m 232AA1C5 000.00s default values build
[34m[1mpassed[0m 3C22E6E3 000.00s dissection
[34m[1mpassed[0m 9CE218B8 000.00s default instantiation
[34m[1mpassed[0m 6220307F 000.00s default values build
[34m[1mpassed[0m A9EBBAD4 000.00s filled values build
[34m[1mpassed[0m 536B46BD 000.00s dissection
[34m[1mpassed[0m 5257E1A4 000.00s default instantiation
[34m[1mpassed[0m 78B3C912 000.00s default values build
[34m[1mpassed[0m E4B7C7F5 000.00s filled values build
[34m[1mpassed[0m 4AA022EB 000.00s dissection
[34m[1mpassed[0m 30F19569 000.00s default instantiation
[34m[1mpassed[0m 8FDA3D3C 000.00s default value build
[34m[1mpassed[0m 55F9A0FA 000.00s filled values build
[34m[1mpassed[0m 192EF04D 000.00s dissection
[34m[1mpassed[0m 3E5E466A 000.00s default instantiation
[34m[1mpassed[0m 2B3C391B 000.00s default values build
[34m[1mpassed[0m 773C950F 000.00s filled values build
[34m[1mpassed[0m 0C8A02FB 000.00s dissection
[34m[1mpassed[0m 099CB01B 000.00s default instantiation
[34m[1mpassed[0m 90FD3F7C 000.00s default values build
[34m[1mpassed[0m 8FE15847 000.00s filled values build
[34m[1mpassed[0m BD38DC7F 000.00s dissection
[34m[1mpassed[0m D6CBDEE9 000.00s default instantiation
[34m[1mpassed[0m CDF64D7F 000.00s default values build
[34m[1mpassed[0m 1A5A7AD3 000.00s dissection
[34m[1mpassed[0m 4B04F49D 000.00s default instantiation
[34m[1mpassed[0m 14CC05CA 000.00s default values build
[34m[1mpassed[0m EEF4F14C 000.00s filled values build
[34m[1mpassed[0m 185DE318 000.00s dissection
[34m[1mpassed[0m CDF25908 000.00s default instantiation
[34m[1mpassed[0m C7C955B6 000.00s default values build
[34m[1mpassed[0m AAF68B53 000.00s filled values build
[34m[1mpassed[0m E68E8333 000.00s dissection
Campaign CRC=009CEF0A in 000.03s SHA=418CE0F83D228514D2DE61FFDF959C1E16ACE9AA
[34m[1mPASSED=42 FAILED=0[0m
[32m━ Loading: test/contrib/sdnv.uts[0m
[34m[1mpassed[0m CB795B07 000.00s Load SDNVUtil
[34m[1mpassed[0m C76A0037 000.00s Define utils
[34m[1mpassed[0m 742A6435 000.00s Vector tests: small ints
[34m[1mpassed[0m 4D5A593E 000.00s Vector tests: big ints
[34m[1mpassed[0m 42A58814 000.00s 100 random vector tests
[34m[1mpassed[0m E6DC3580 000.00s SDVN tests
Campaign CRC=BABF4761 in 000.01s SHA=3D7710F2AA0B0D60751806C9B8AFA489B288943A
[34m[1mPASSED=6 FAILED=0[0m
[32m━ Loading: test/contrib/sebek.uts[0m
[34m[1mpassed[0m E27179EA 000.00s Layer binding 1
[34m[1mpassed[0m 82547110 000.00s Packet dissection 1
[34m[1mpassed[0m C399EA2F 000.00s Layer binding 2
[34m[1mpassed[0m 8E7EDB2F 000.00s Packet dissection 2
[34m[1mpassed[0m 4C1B29F4 000.00s Layer binding 3
[34m[1mpassed[0m 952B87E1 000.00s Packet dissection 3
[34m[1mpassed[0m 94996C54 000.00s Nonsense summaries
Campaign CRC=455F8891 in 000.01s SHA=AA237F2E761BD5CA6E98DECB0F25475C884B7849
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/send.uts[0m
[34m[1mpassed[0m 878CEAEB 000.00s ICMPv6NDOptRsaSig build and dissection
[34m[1mpassed[0m 8E4AD660 000.00s ICMPv6NDOptCGA build and dissection
[34m[1mpassed[0m E0159ADE 000.00s ICMPv6NDOptTmstp build and dissection
[34m[1mpassed[0m 9185CAFD 000.00s ICMPv6NDOptNonce build and dissection
Campaign CRC=06722B7D in 000.01s SHA=F356DADC8E4A48DF616A3B938375F6206FCBB5A8
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/contrib/socks.uts[0m
[34m[1mpassed[0m CBDF4CAE 000.01s Basic build and dissection - test version dispatch
[34m[1mpassed[0m 4E191715 000.00s SOCKS5Request build and dissection
[34m[1mpassed[0m 8AD93DD1 000.00s Test SOCKSv5 over UDP
Campaign CRC=07A94E58 in 000.01s SHA=7414E397D9F7E3C6592C8E405A3AFB6488A0BCAD
[34m[1mPASSED=3 FAILED=0[0m
[32m━ Loading: test/contrib/spbm.uts[0m
[34m[1mpassed[0m 9E2FA55C 000.00s Test build and dissection
Campaign CRC=FB4F1B77 in 000.00s SHA=84E7E450DBF23A86193132C6C448DC99EA910548
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/tacacs.uts[0m
[34m[1mpassed[0m 75EB00FD 000.00s default instantiation
[34m[1mpassed[0m 0943AD4E 000.00s default values build
[34m[1mpassed[0m AD68E9A7 000.00s filled values build
[34m[1mpassed[0m 5AF9DD09 000.00s dissection
[34m[1mpassed[0m 1E866A37 000.00s default instantiation
[34m[1mpassed[0m 85B4E84B 000.00s default values build
[34m[1mpassed[0m 3635289B 000.00s filled values build -- SSH connection sample use scapy, secret = test
[34m[1mpassed[0m 09C0E2C4 000.00s dissection
[34m[1mpassed[0m 5F709645 000.00s default instantiation
[34m[1mpassed[0m 320D7FF9 000.00s default values build
[34m[1mpassed[0m 459F1222 000.00s filled values build -- SSH connection sample use scapy, secret = test
[34m[1mpassed[0m 004C9B89 000.00s dissection
[34m[1mpassed[0m 6A3D48EC 000.00s default instantiation
[34m[1mpassed[0m 230DBAE9 000.00s default values build
[34m[1mpassed[0m 30EE0DF8 000.00s filled values build -- SSH connection sample secret = test, password = pass
[34m[1mpassed[0m 8041A0A9 000.00s dissection
[34m[1mpassed[0m 4EEF9F5F 000.00s default instantiation
[34m[1mpassed[0m 3F5AAE02 000.00s default values build
[34m[1mpassed[0m 624503E4 000.00s filled values build -- SSH connection sample secret = test
[34m[1mpassed[0m BEF43CF5 000.00s dissection
[34m[1mpassed[0m 1A9BC264 000.00s default instantiation
[34m[1mpassed[0m B04D9EB1 000.00s default values build
[34m[1mpassed[0m C9A6C6C1 000.00s filled values build -- SSH connection sample secret = test
[34m[1mpassed[0m 00D74EBC 000.00s dissection
[34m[1mpassed[0m 8879699E 000.00s default instantiation
[34m[1mpassed[0m 4CB86C87 000.00s default value build
[34m[1mpassed[0m 1BAF4C3E 000.00s filled values build -- SSH connection sample secret = test
[34m[1mpassed[0m C8946887 000.00s dissection
[34m[1mpassed[0m 0DE37339 000.00s default instantiation
[34m[1mpassed[0m 4B162CFE 000.00s default values build
[34m[1mpassed[0m 42E888C6 000.00s filled values build  -- SSH connection sample secret = test
[34m[1mpassed[0m 09E59968 000.00s dissection
[34m[1mpassed[0m CB046580 000.00s instantiation
[34m[1mpassed[0m 75DD83FF 000.00s dissection
Campaign CRC=F3094D45 in 000.03s SHA=15325D4C510BD718C6B46D501348049E7FC712C5
[34m[1mPASSED=34 FAILED=0[0m
[32m━ Loading: test/contrib/tzsp.uts[0m
[34m[1mpassed[0m 00000000 000.00s build basic TZSP frames
[34m[1mpassed[0m AFD712FD 000.00s = basic TZSP header - keepalive
[34m[1mpassed[0m 40E6670F 000.00s = basic TZSP header - keepalive + ignored end tag
[34m[1mpassed[0m 82D93C33 000.00s = basic TZSP header with RX Packet and EndTag
[34m[1mpassed[0m 26828AF3 000.00s = basic TZSP header with RX Packet and Padding
[34m[1mpassed[0m F9A3BD27 000.00s = basic TZSP header with RX Packet and RAWRSSI (byte, short)
[34m[1mpassed[0m E5E06C95 000.00s = basic TZSP header with RX Packet and SNR (byte, short)
[34m[1mpassed[0m 194AE3C0 000.00s = basic TZSP header with RX Packet and DATA Rate
[34m[1mpassed[0m 810AC76E 000.00s = basic TZSP header with RX Packet and Timestamp
[34m[1mpassed[0m 5337557A 000.00s = basic TZSP header with RX Packet and ContentionFree
[34m[1mpassed[0m 2B201513 000.00s = basic TZSP header with RX Packet and Decrypted
[34m[1mpassed[0m 9DFCC65C 000.00s = basic TZSP header with RX Packet and FCS error
[34m[1mpassed[0m C87B42D0 000.00s = basic TZSP header with RX Packet and RXChannel
[34m[1mpassed[0m D20D259A 000.00s = basic TZSP header with RX Packet and Packet count
[34m[1mpassed[0m F6165D78 000.00s = basic TZSP header with RX Packet and RXFrameLength
[34m[1mpassed[0m 149EDF2C 000.00s = basic TZSP header with RX Packet and WLAN RADIO HDR SERIAL
[34m[1mpassed[0m F013D4A9 000.00s = handling of unknown tag
[34m[1mpassed[0m 996306A2 000.01s all layers stacked
[34m[1mpassed[0m 00000000 000.00s state tags value range
[34m[1mpassed[0m 37ED00E2 000.00s = TZSPTagContentionFree
[34m[1mpassed[0m 82BA0183 000.00s = TZSPTagError
[34m[1mpassed[0m 184E7B78 000.00s = missing TZSP header before end tag
[34m[1mpassed[0m 46DAED79 000.00s = invalid length field for given tag
[34m[1mpassed[0m 849FC3E8 000.00s = handling of unknown tag - payload to short
[34m[1mpassed[0m 7400232A 000.00s = handling of unknown tag - no payload after tag type
Campaign CRC=1321DB3F in 000.08s SHA=2E9C58F8D3ED039D5870DBC2A548728963036F9D
[34m[1mPASSED=25 FAILED=0[0m
[32m━ Loading: test/contrib/vqp.uts[0m
[34m[1mpassed[0m 7C39558A 000.00s Build VQP
[34m[1mpassed[0m 2F8C1252 000.00s Dissect VQP
Campaign CRC=244CE7E2 in 000.00s SHA=771D39B82984D237C674EF3A5F8729A9920F6C98
[34m[1mPASSED=2 FAILED=0[0m
[32m━ Loading: test/contrib/vtp.uts[0m
[34m[1mpassed[0m 4AE022D0 000.00s VTP, basic instantiation
Campaign CRC=FA6F7035 in 000.00s SHA=16702CB0A2404E9328FB2F41D29489124A791D92
[34m[1mPASSED=1 FAILED=0[0m
[32m━ Loading: test/contrib/wireguard.uts[0m
[34m[1mpassed[0m 9581C596 000.00s Build and dissect Transport
[34m[1mpassed[0m 03D99456 000.00s Build and dissect Init
[34m[1mpassed[0m 1E37F451 000.00s Build and dissect Response
[34m[1mpassed[0m B97863E3 000.00s Build and dissect Cookie Response
Campaign CRC=ECB2C085 in 000.00s SHA=5D8CB067E83BB4C8A33EA68C45166C7BA69D3BAB
[34m[1mPASSED=4 FAILED=0[0m
[32m━ Loading: test/tools/isotpscanner.uts[0m
Campaign CRC=0F09B64B in 000.00s SHA=EFF45D37D4C64265E1A06035FE02CC2DA6298E0A
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/tools/obdscanner.uts[0m
Campaign CRC=8910FA88 in 000.00s SHA=E5765853C9AA0E879951968ACB5ACACAE7A2A222
[34m[1mPASSED=0 FAILED=0[0m
[32m━ Loading: test/tools/xcpscanner.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m CEBB6F0B 000.01s modules
[34m[1mpassed[0m 5B137CEE 001.51s xcp can scanner broadcast ID-Range
[34m[1mpassed[0m 332F8156 001.51s xcp can scanner connect ID-range
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=BF33674E in 003.03s SHA=EC80C8E732DFB607CBBE014F199F1671DE075F6F
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/ccp.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m 6E7FD8EF 000.00s Load module
[34m[1mpassed[0m 01ACCD17 000.00s Build CRO CONNECT
[34m[1mpassed[0m 2723B0E1 000.00s Dissect DTO CONNECT
[34m[1mpassed[0m BDE7D3AF 000.00s Build CRO EXCHANGE_ID
[34m[1mpassed[0m A5AAA275 000.00s Dissect DTO EXCHANGE_ID
[34m[1mpassed[0m 5073C77B 000.00s Build CRO GET_SEED
[34m[1mpassed[0m 4ED49A77 000.00s Dissect DTO GET_SEED
[34m[1mpassed[0m A2961640 000.00s Build CRO UNLOCK
[34m[1mpassed[0m CEC63166 000.00s Dissect DTO UNLOCK
[34m[1mpassed[0m 43FE4B94 000.00s Build CRO SET_MTA
[34m[1mpassed[0m 69A9DBFF 000.00s Dissect DTO SET_MTA
[34m[1mpassed[0m EC4963C8 000.00s Build CRO DNLOAD
[34m[1mpassed[0m AE3AFDC2 000.00s Dissect DTO DNLOAD
[34m[1mpassed[0m FE93D8D5 000.00s Build CRO DNLOAD_6
[34m[1mpassed[0m AD0C9387 000.00s Dissect DTO DNLOAD_6
[34m[1mpassed[0m 34D2904A 000.00s Build CRO UPLOAD
[34m[1mpassed[0m DA87703B 000.00s Dissect DTO UPLOAD
[34m[1mpassed[0m 6693B5D7 000.00s Build CRO SHORT_UP
[34m[1mpassed[0m 4A26ED2F 000.00s Dissect DTO SHORT_UP
[34m[1mpassed[0m 1A82DCFF 000.00s Build CRO SELECT_CAL_PAGE
[34m[1mpassed[0m C888133D 000.00s Dissect DTO SELECT_CAL_PAGE
[34m[1mpassed[0m EE28D247 000.00s Build CRO GET_DAQ_SIZE
[34m[1mpassed[0m 644CD9D4 000.00s Dissect DTO GET_DAQ_SIZE
[34m[1mpassed[0m B3C3CA60 000.00s Build CRO SET_DAQ_PTR
[34m[1mpassed[0m CF0622CF 000.00s Dissect DTO SET_DAQ_PTR
[34m[1mpassed[0m AE492DCC 000.00s Build CRO WRITE_DAQ
[34m[1mpassed[0m 34F2C1A6 000.00s Dissect DTO WRITE_DAQ
[34m[1mpassed[0m E431CBB9 000.00s Build CRO START_STOP
[34m[1mpassed[0m 3E8D42A3 000.00s Dissect DTO START_STOP
[34m[1mpassed[0m FF631624 000.00s Build CRO DISCONNECT
[34m[1mpassed[0m B66D7442 000.00s Dissect DTO DISCONNECT
[34m[1mpassed[0m 0CF965D6 000.00s Build CRO SET_S_STATUS
[34m[1mpassed[0m BC12F747 000.00s Dissect DTO SET_S_STATUS
[34m[1mpassed[0m 9B5C796F 000.00s Build CRO GET_S_STATUS
[34m[1mpassed[0m F2B489DD 000.00s Dissect DTO GET_S_STATUS
[34m[1mpassed[0m 6F135ED7 000.00s Build CRO BUILD_CHKSUM
[34m[1mpassed[0m B7028478 000.00s Dissect DTO BUILD_CHKSUM
[34m[1mpassed[0m 490E780B 000.00s Dissect DTO BUILD_CHKSUM2
[34m[1mpassed[0m B8D9348A 000.00s Build CRO CLEAR_MEMORY
[34m[1mpassed[0m 93A365BD 000.00s Dissect DTO CLEAR_MEMORY
[34m[1mpassed[0m DEF52552 000.00s Build CRO PROGRAM
[34m[1mpassed[0m 2CE179CC 000.00s Dissect DTO PROGRAM
[34m[1mpassed[0m BFEC674A 000.00s Build CRO PROGRAM_6
[34m[1mpassed[0m C1695B8D 000.00s Dissect DTO PROGRAM_6
[34m[1mpassed[0m F207C003 000.00s Build CRO MOVE
[34m[1mpassed[0m 65AD84BD 000.00s Dissect DTO MOVE
[34m[1mpassed[0m EDD8EECA 000.00s Build CRO DIAG_SERVICE
[34m[1mpassed[0m 44D6F227 000.00s Dissect DTO DIAG_SERVICE
[34m[1mpassed[0m 6E4365D9 000.00s Build CRO ACTION_SERVICE
[34m[1mpassed[0m D9E9F267 000.00s Dissect DTO ACTION_SERVICE
[34m[1mpassed[0m 76BFFD16 000.00s Build CRO TEST
[34m[1mpassed[0m 81030CFF 000.00s Dissect DTO TEST
[34m[1mpassed[0m 288A263D 000.00s Build CRO START_STOP_ALL
[34m[1mpassed[0m 8B7C8FFA 000.00s Dissect DTO START_STOP_ALL
[34m[1mpassed[0m D97CE162 000.00s Build CRO GET_ACTIVE_CAL_PAGE
[34m[1mpassed[0m B40AD718 000.00s Dissect DTO GET_ACTIVE_CAL_PAGE
[34m[1mpassed[0m ABDE4FED 000.00s Build CRO GET_CCP_VERSION
[34m[1mpassed[0m 590B3C64 000.00s Dissect DTO GET_CCP_VERSION
[34m[1mpassed[0m F0F047E9 000.00s CAN Socket sr1 with dto.ansers(cro) == True
[34m[1mpassed[0m C5358F08 000.10s CAN Socket sr1 with dto.ansers(cro) == False
[34m[1mpassed[0m 1D7A86D4 000.00s CAN Socket sr1 with error code
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=DAACC357 in 000.16s SHA=61A78B5C2677B002F8648E380346A157AD33EEF7
[34m[1mPASSED=63 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/doip.uts[0m
[34m[1mpassed[0m F04B2408 000.01s Load Contrib Layer
[34m[1mpassed[0m FCC821F0 000.00s Defaults test
[34m[1mpassed[0m C01319D3 000.00s Build test 0
[34m[1mpassed[0m 10585C8E 000.00s Build test 1
[34m[1mpassed[0m 341DE1EB 000.00s Build test 2
[34m[1mpassed[0m 262743CF 000.00s Build test 3
[34m[1mpassed[0m 8E7078C3 000.00s Build test 4
[34m[1mpassed[0m 28443B36 000.00s Build test 5
[34m[1mpassed[0m CA6B6500 000.00s Build test 6
[34m[1mpassed[0m 513BC711 000.00s Build test 7
[34m[1mpassed[0m A546C7A2 000.00s Build test 8
[34m[1mpassed[0m 8DFA8109 000.00s Build test 4001
[34m[1mpassed[0m 54C734B7 000.00s Build test 4002
[34m[1mpassed[0m 58600A19 000.00s Build test 4003
[34m[1mpassed[0m 8BC8D4B1 000.00s Build test 4004
[34m[1mpassed[0m 7CD90A8D 000.00s Build test 8001
[34m[1mpassed[0m 0AE7C61C 000.00s Build test 8002
[34m[1mpassed[0m EC8758CD 000.00s Build test 8003
[34m[1mpassed[0m DF1C113E 000.05s read pcap file
[34m[1mpassed[0m E0C5527D 000.00s dissect test of routing activation pkts req
[34m[1mpassed[0m 21D2B028 000.00s dissect test of routing activation pkts resp
[34m[1mpassed[0m A26E986C 000.00s answers test of routing activation pkts
[34m[1mpassed[0m EF791612 000.00s dissect diagnostic message
Campaign CRC=175FB2D4 in 000.07s SHA=3A8A40B347AD408732C8CBCAFC96FCB35D859DC1
[34m[1mPASSED=23 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/ecu.uts[0m
[34m[1mpassed[0m 97256202 000.05s Load modules
[34m[1mpassed[0m 92D193FF 000.01s Load Ecu module
[34m[1mpassed[0m 52B1B986 000.00s Check EcuState basic functionality
[34m[1mpassed[0m C40E072F 000.00s More complex tests
[34m[1mpassed[0m 6FE6FE4A 000.00s Even more complex tests
[34m[1mpassed[0m 77D2454B 000.00s Delete Attribute Test
[34m[1mpassed[0m 189316FA 000.00s Copy tests
[34m[1mpassed[0m A50DEA07 000.00s Move tests
[34m[1mpassed[0m E13D1E66 000.00s equal tests
[34m[1mpassed[0m 52ACD926 000.00s hash tests
[34m[1mpassed[0m 8C1DCDD8 000.00s command tests
[34m[1mpassed[0m 0A0042C2 000.00s less than tests
[34m[1mpassed[0m 59157FBD 000.00s less than tests 2
[34m[1mpassed[0m A10F49C5 000.00s less than tests 3
[34m[1mpassed[0m 477A16ED 000.00s less than tests 4
[34m[1mpassed[0m 1ECFB640 000.00s less than tests 5
[34m[1mpassed[0m 6A056E04 000.00s less than tests 6
[34m[1mpassed[0m B64FE510 000.00s contains test
[34m[1mpassed[0m 65C448FC 000.00s Basic definitions for tests
[34m[1mpassed[0m D6767FE8 000.00s Basic checks
[34m[1mpassed[0m 199FEF57 000.00s Command checks
[34m[1mpassed[0m DF81228B 000.00s Command checks 2
[34m[1mpassed[0m 4D8CF3D3 000.00s Compare check
[34m[1mpassed[0m 724132E3 000.00s Key response check
[34m[1mpassed[0m 600E00ED 000.00s Log all commands applied to an Ecu
[34m[1mpassed[0m 7C72DF5F 000.00s Trace all commands applied to an Ecu
[34m[1mpassed[0m 5B9C2046 000.00s Generate supported responses of an Ecu
[34m[1mpassed[0m D7C9A135 000.02s Analyze multiple UDS messages
[34m[1mpassed[0m 79A76007 000.02s Analyze on the fly with EcuSession
[34m[1mpassed[0m 3DF43827 000.04s Analyze on the fly with EcuSession GMLAN1
[34m[1mpassed[0m 4E173277 000.08s Analyze on the fly with EcuSession GMLAN logging test
Campaign CRC=79024063 in 000.24s SHA=87E22A504A1759A26E3BBCA6768C8411EDFF3490
[34m[1mPASSED=31 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/ecu_am.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m 19B0D527 000.00s Load contribution layer
[34m[1mpassed[0m D2D3C534 000.01s Simple check with RDBI and Negative Response
[34m[1mpassed[0m 86000BD2 000.02s Simple check with different Sessions
[34m[1mpassed[0m 8263A7BD 000.05s Simple check with different Sessions and diagnosticSessionControl
[34m[1mpassed[0m A93C9EDD 000.05s Simple check with different Sessions and diagnosticSessionControl and answers hook
[34m[1mpassed[0m B12D5794 000.01s Simple check with security access and answers hook
[34m[1mpassed[0m F0EF20A5 000.85s Simple check with security access and answers hook and request-correctly-received message
[34m[1mpassed[0m 724037B1 000.82s Simple check with security access and answers hook and request-correctly-received message 2
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=C2683823 in 001.81s SHA=354D127EF0D7B008654C89C2C9D298758C306582
[34m[1mPASSED=10 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/kwp.uts[0m
[34m[1mpassed[0m DD2B38E9 000.01s Load module
[34m[1mpassed[0m B7A8A0F2 000.00s Check if positive response answers
[34m[1mpassed[0m 4FF2C0C6 000.00s Check hashret
[34m[1mpassed[0m BDEEDFD9 000.00s Check if negative response answers
[34m[1mpassed[0m 94EBFE4D 000.00s CHECK hashret NEG
[34m[1mpassed[0m 855A269C 000.00s Check if negative response answers
[34m[1mpassed[0m 94EBFE4D 000.00s CHECK hashret NEG
[34m[1mpassed[0m 27430AD9 000.00s Check if negative response answers not
[34m[1mpassed[0m 171C8A52 000.00s Check if positive response answers not
[34m[1mpassed[0m 757FFD7A 000.00s Check KWP_SDS
[34m[1mpassed[0m 9A8F6308 000.00s Check KWP_SDS
[34m[1mpassed[0m 81306650 000.00s Check KWP_SDSPR
[34m[1mpassed[0m 78CA8729 000.00s Check KWP_SDSPR
[34m[1mpassed[0m 9A8F6308 000.00s Check KWP_SDS
[34m[1mpassed[0m 78CA8729 000.00s Check KWP_SDSPR
[34m[1mpassed[0m 950DED2B 000.00s Check KWP_ER
[34m[1mpassed[0m 52E9868B 000.00s Check KWP_ER
[34m[1mpassed[0m B74CE32D 000.00s Check KWP_ERPR
[34m[1mpassed[0m 80886A28 000.00s Check KWP_SA
[34m[1mpassed[0m F856E57B 000.00s Check KWP_SAPR
[34m[1mpassed[0m F9BAC9C3 000.00s Check KWP_SA
[34m[1mpassed[0m FFE9B30C 000.00s Check KWP_SAPR
[34m[1mpassed[0m 80886A28 000.00s Check KWP_SA
[34m[1mpassed[0m 9237BD4F 000.00s Check KWP_SA
[34m[1mpassed[0m 13889602 000.00s Check KWP_SAPR
[34m[1mpassed[0m 340BA94F 000.00s Check KWP_DNT
[34m[1mpassed[0m 30F05E53 000.00s Check KWP_DNMTPR
[34m[1mpassed[0m 88FBE546 000.00s Check KWP_DNMTPR
[34m[1mpassed[0m 51C91A0A 000.00s Check KWP_TP
[34m[1mpassed[0m 7A4C0604 000.00s Check KWP_TPPR
[34m[1mpassed[0m 39D1C80E 000.00s Check KWP_CDTCS
[34m[1mpassed[0m 8F022E4B 000.00s Check KWP_CDTCSPR
[34m[1mpassed[0m FD7C3D91 000.00s Check KWP_ROE
[34m[1mpassed[0m A6676627 000.00s Check KWP_ROEPR
[34m[1mpassed[0m A31E3853 000.00s Check KWP_RDBI
[34m[1mpassed[0m EF900EA2 000.00s Build KWP_RDBI
[34m[1mpassed[0m F3A82B1C 000.00s Check KWP_RDBI2
[34m[1mpassed[0m DDA85DC5 000.00s Build KWP_RDBI2
[34m[1mpassed[0m F93737A2 000.00s Test observable dict used in KWP_RDBI, setter
[34m[1mpassed[0m F6033BB1 000.00s Test observable dict used in KWP_RDBI, deleter
[34m[1mpassed[0m CF27B844 000.00s Check KWP_RDBIPR
[34m[1mpassed[0m F9C99843 000.00s Check KWP_RMBA
[34m[1mpassed[0m 034F81E3 000.00s Check KWP_RMBAPR
[34m[1mpassed[0m 8F700FF5 000.00s Check KWP_DDLI
[34m[1mpassed[0m E6A345C4 000.00s Check KWP_DDLIPR
[34m[1mpassed[0m FDAA7D04 000.00s Check KWP_WDBI
[34m[1mpassed[0m 5B4F1973 000.00s Build KWP_WDBI
[34m[1mpassed[0m 57A528B7 000.00s Check KWP_WDBI
[34m[1mpassed[0m 3BFC1047 000.00s Check KWP_WDBIPR
[34m[1mpassed[0m C51ACE49 000.00s Check KWP_WMBA
[34m[1mpassed[0m EE0E9818 000.00s Check KWP_WMBAPR
[34m[1mpassed[0m E3FE2EFA 000.00s Check KWP_CDI
[34m[1mpassed[0m E7021100 000.00s Check KWP_RC
[34m[1mpassed[0m E7021100 000.00s Check KWP_RC
[34m[1mpassed[0m 4F0D28F1 000.00s Check KWP_RCPR
[34m[1mpassed[0m 2B4FBBAE 000.00s Check KWP_RD
[34m[1mpassed[0m 47747A7E 000.00s Check KWP_RDPR
[34m[1mpassed[0m 8D3AEDFE 000.00s Check KWP_RU
[34m[1mpassed[0m F09D26C0 000.00s Check KWP_RUPR
[34m[1mpassed[0m 1DB4FE15 000.00s Check KWP_TD
[34m[1mpassed[0m 890E798A 000.00s Check KWP_TDPR
[34m[1mpassed[0m 1E14D304 000.00s Check KWP_RTE
[34m[1mpassed[0m 8F36BA62 000.00s Check KWP_RTEPR
[34m[1mpassed[0m 49BCFD2D 000.00s Check KWP_IOCBI
[34m[1mpassed[0m 023F9058 000.00s Check KWP_IOCBIPR
[34m[1mpassed[0m 49B5091D 000.00s Check KWP_NRC
Campaign CRC=956BDA4F in 000.04s SHA=3D0240FDED2B6D69E8D22A7181034B9ACD942927
[34m[1mPASSED=66 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/someip.uts[0m
[34m[1mpassed[0m D3DDC383 000.00s Load module
[34m[1mpassed[0m 9F7F1DE8 000.00s Basic build
[34m[1mpassed[0m 85C2D0FD 000.00s Build with empty payload
[34m[1mpassed[0m 44B10351 000.00s Build with non-empty payload
[34m[1mpassed[0m CD7BD1C4 000.00s Dissect EVENT_ID packet
[34m[1mpassed[0m 751D3E26 000.00s Dissect METHOD_ID packet
[34m[1mpassed[0m 5BA2DF92 000.00s Build TP
[34m[1mpassed[0m F00608CC 000.00s Dissect TP
[34m[1mpassed[0m EC9AC64D 000.00s Build TP fragmented
[34m[1mpassed[0m 3D0DE85D 000.00s Check packet length on empty build
[34m[1mpassed[0m 23B9E896 000.00s Build 1
[34m[1mpassed[0m 4A219B67 000.00s Build 2
[34m[1mpassed[0m BE543121 000.00s Dissect
[34m[1mpassed[0m 1D607AAB 000.00s Check packet length on empty build
[34m[1mpassed[0m 23BFBA7C 000.00s Build
[34m[1mpassed[0m E73BD8DE 000.00s Dissect
[34m[1mpassed[0m 3A5F7423 000.00s Build and check flags
[34m[1mpassed[0m E67BB9DF 000.00s Build empty
[34m[1mpassed[0m 5BA6823C 000.00s Verify constants against spec TR_SOMEIP_00250
[34m[1mpassed[0m 09528163 000.00s check that values are bound
[34m[1mpassed[0m 17F4A12E 000.00s Check length of package without entries nor options
[34m[1mpassed[0m A7D8F449 000.00s Check entries to array and size check
[34m[1mpassed[0m B00F92E2 000.00s Check Options to array and size check
[34m[1mpassed[0m FB16610C 000.00s Check Entries & Options to array and size check
[34m[1mpassed[0m FDDCCF78 000.00s Single SD entry
[34m[1mpassed[0m 93716621 000.00s Double SD entry
[34m[1mpassed[0m 65453A67 000.00s Flipped double SD entry
[34m[1mpassed[0m B6C3BA4F 000.00s Verifying constants against spec
[34m[1mpassed[0m CA54E07C 000.00s SDOption_Config: Verify make_string() method from dict
[34m[1mpassed[0m 01E27F57 000.00s SDOption_Config: Verify make_string() method from list
[34m[1mpassed[0m 1FAA1C5F 000.00s SDOption_Config: Build and dissect empty
[34m[1mpassed[0m 1F38FB15 000.00s SDOption_Config: Build and dissect spec example
[34m[1mpassed[0m D0DDF213 000.00s SDOption_Config: Build and dissect fully populated
[34m[1mpassed[0m 0FA53950 000.00s SDOption_LoadBalance: Build and dissect empty
[34m[1mpassed[0m 50E16D5D 000.00s SDOption_LoadBalance: Build and dissect example
[34m[1mpassed[0m 6D6DA1FA 000.00s SDOption_LoadBalance: Build and dissect fully populated
[34m[1mpassed[0m 89A730E1 000.00s SDOption_IP4_EndPoint: Build and dissect empty
[34m[1mpassed[0m 3446D911 000.00s SDOption_IP4_EndPoint: Build and dissect example
[34m[1mpassed[0m 8BF142B2 000.00s SDOption_IP4_EndPoint: Build and dissect fully populated
[34m[1mpassed[0m 3F74F4FD 000.00s SDOption_IP4_Multicast: Build and dissect empty
[34m[1mpassed[0m 5C5E5477 000.00s SDOption_IP4_Multicast: Build and dissect example
[34m[1mpassed[0m E8B8C6A8 000.00s SDOption_IP4_Multicast: Build and dissect fully populated
[34m[1mpassed[0m 28402935 000.00s SDOption_IP4_SD_EndPoint: Build and dissect empty
[34m[1mpassed[0m F9B58D5E 000.00s SDOption_IP4_SD_EndPoint: Build and dissect example
[34m[1mpassed[0m 9EFA7947 000.00s SDOption_IP4_SD_EndPoint: Build and dissect fully populated
[34m[1mpassed[0m 10C4953C 000.00s SDOption_IP6_EndPoint: Build and dissect empty
[34m[1mpassed[0m 2B2DCBFB 000.00s SDOption_IP6_EndPoint: Build and dissect example
[34m[1mpassed[0m 9B227F72 000.00s SDOption_IP6_EndPoint: Build and dissect fully populated
[34m[1mpassed[0m AF80E2B8 000.00s SDOption_IP6_Multicast: Build and dissect empty
[34m[1mpassed[0m 4B622046 000.00s SDOption_IP6_Multicast: Build and dissect example
[34m[1mpassed[0m 8B8E6ACD 000.00s SDOption_IP6_Multicast: Build and dissect fully populated
[34m[1mpassed[0m 3AFD11DD 000.00s SDOption_IP6_SD_EndPoint: Build and dissect empty
[34m[1mpassed[0m AE42DD86 000.00s SDOption_IP6_SD_EndPoint: Build and dissect example
[34m[1mpassed[0m CA067E6A 000.00s SDOption_IP6_SD_EndPoint: Build and dissect fully populated
[34m[1mpassed[0m 1407B303 000.02s verify building and parsing of multiple SDOptions
Campaign CRC=C9237659 in 000.06s SHA=0A2F086CC67D03D65ABC1EC14E58D9A0096253D4
[34m[1mPASSED=55 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/testsocket.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m E0324C0D 000.00s Create Dummy Packet
[34m[1mpassed[0m 4C3D063D 000.00s Create Sockets
[34m[1mpassed[0m FDD6F60D 000.24s Simple ping pong
[34m[1mpassed[0m 11C2B631 000.08s Simple ping pong with sr with packet generator 500
[34m[1mpassed[0m CC06CAB8 000.18s Simple ping pong with sr with generated packets
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=F0CF66D5 in 000.50s SHA=01BA4BD2248677E1DF0BCB747C4FF4C41BCC1776
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/uds.uts[0m
[34m[1mpassed[0m ACD47BA2 000.00s Load module
[34m[1mpassed[0m C7D2AC0C 000.00s Check if positive response answers
[34m[1mpassed[0m 340037BC 000.00s Check hashret
[34m[1mpassed[0m 7FE78139 000.00s Check if negative response answers
[34m[1mpassed[0m 3ED43E1F 000.00s CHECK hashret NEG
[34m[1mpassed[0m 7A0200E5 000.00s Check if negative response answers not
[34m[1mpassed[0m FAC3603E 000.00s Check if positive response answers not
[34m[1mpassed[0m 372D2CC3 000.00s Check UDS_DSC
[34m[1mpassed[0m 87E8A7A5 000.00s Check UDS_DSC
[34m[1mpassed[0m 8DA1C985 000.00s Check UDS_DSCPR
[34m[1mpassed[0m 9F718B9E 000.00s Check UDS_DSCPR
[34m[1mpassed[0m 87E8A7A5 000.00s Check UDS_DSC
[34m[1mpassed[0m 9F718B9E 000.00s Check UDS_DSCPR
[34m[1mpassed[0m EE48C792 000.00s Check UDS_DSC modifies ecu state
[34m[1mpassed[0m 0071A548 000.00s Check UDS_DSCPR modifies ecu state
[34m[1mpassed[0m 660C0D62 000.00s Check UDS_ER
[34m[1mpassed[0m 7D2A53B6 000.00s Check UDS_ER
[34m[1mpassed[0m 6EA462B3 000.00s Check UDS_ERPR
[34m[1mpassed[0m 78D15F31 000.00s Check UDS_ERPR
[34m[1mpassed[0m 7C40B3A1 000.00s Check UDS_ERPR modifies ecu state
[34m[1mpassed[0m 1D333CB9 000.00s Check UDS_SA
[34m[1mpassed[0m 05D89D30 000.00s Check UDS_SAPR
[34m[1mpassed[0m 532C308A 000.00s Check UDS_SA
[34m[1mpassed[0m DFA23D54 000.00s Check UDS_SAPR
[34m[1mpassed[0m 2C3B44E6 000.00s Check UDS_SA
[34m[1mpassed[0m 4A098C15 000.00s Check UDS_SAPR modifies ecu state
[34m[1mpassed[0m 532C308A 000.00s Check UDS_SA
[34m[1mpassed[0m B8E69FD0 000.00s Check UDS_SAPR
[34m[1mpassed[0m 3997C1BD 000.00s Check UDS_CC
[34m[1mpassed[0m E2B733EB 000.00s Check UDS_CCPR
[34m[1mpassed[0m 969D0D4B 000.00s Check UDS_CCPR modifies ecu state
[34m[1mpassed[0m 92248607 000.00s Check UDS_AUTH
[34m[1mpassed[0m 2F27C96A 000.00s Build UDS_AUTH
[34m[1mpassed[0m 2B06843E 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m 65A024C2 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m F5F146A2 000.00s Check UDS_AUTH
[34m[1mpassed[0m 57BEB85C 000.00s Build UDS_AUTH
[34m[1mpassed[0m F7DA5182 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m 3F4A5CD5 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m 5E808F4E 000.00s Check UDS_AUTH
[34m[1mpassed[0m 4A17C2D0 000.00s Build UDS_AUTH
[34m[1mpassed[0m D4CC6314 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m 720B7D53 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m 18E95B16 000.00s Check UDS_AUTH
[34m[1mpassed[0m 7C2D9304 000.00s Build UDS_AUTH
[34m[1mpassed[0m 58AAB578 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m B80AB61C 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m B6031973 000.00s Check UDS_AUTH
[34m[1mpassed[0m 4A77E05F 000.00s Build UDS_AUTH
[34m[1mpassed[0m 9C5EC70E 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m FC1C89F3 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m FA8D340B 000.00s Check UDS_AUTH
[34m[1mpassed[0m 092DF1CC 000.00s Build UDS_AUTH
[34m[1mpassed[0m AAADDAD3 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m A498F9AF 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m 5EB6CB48 000.00s Check UDS_AUTH
[34m[1mpassed[0m 85370993 000.00s Build UDS_AUTH
[34m[1mpassed[0m AC0748F2 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m 3FCDAD93 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m E2C96FDB 000.00s Check UDS_AUTH
[34m[1mpassed[0m 581F431F 000.00s Build UDS_AUTH
[34m[1mpassed[0m AC086813 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m 8A49B5D1 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m 2C771E72 000.00s Check UDS_AUTH
[34m[1mpassed[0m 26BCFDDD 000.00s Build UDS_AUTH
[34m[1mpassed[0m 9EC7041F 000.00s Check UDS_AUTHPR
[34m[1mpassed[0m 596B1E97 000.00s Build UDS_AUTHPR
[34m[1mpassed[0m DDD94981 000.00s Check UDS_TP
[34m[1mpassed[0m F07B90A6 000.00s Check UDS_TPPR
[34m[1mpassed[0m 97F78D2C 000.00s Check UDS_ATP
[34m[1mpassed[0m 85E3F3A1 000.00s Check UDS_ATPPR
[34m[1mpassed[0m B54B225A 000.00s Check UDS_ATP
[34m[1mpassed[0m 21F8D3E8 000.00s Check UDS_ATPPR
[34m[1mpassed[0m 544E32BE 000.00s Check UDS_SDT
[34m[1mpassed[0m E4DB7501 000.00s Build UDS_SDT
[34m[1mpassed[0m 12B13532 000.00s Check UDS_SDTPR
[34m[1mpassed[0m E2420EAF 000.00s Check UDS_CDTCS
[34m[1mpassed[0m 4E7460D1 000.00s Check UDS_CDTCSPR
[34m[1mpassed[0m 6A13F6E2 000.00s Check UDS_ROE
[34m[1mpassed[0m 8D73CF44 000.00s Check UDS_ROEPR
[34m[1mpassed[0m 8878F8B9 000.00s Check UDS_LC
[34m[1mpassed[0m 14D50855 000.00s Check UDS_LCPR
[34m[1mpassed[0m 2D869102 000.00s Check UDS_LC
[34m[1mpassed[0m B7D682C6 000.00s Check UDS_RDBI
[34m[1mpassed[0m 818A9F12 000.00s Build UDS_RDBI
[34m[1mpassed[0m 172207C8 000.00s Check UDS_RDBI2
[34m[1mpassed[0m DD2B8093 000.00s Build UDS_RDBI2
[34m[1mpassed[0m 4CA6FC9B 000.00s Test observable dict used in UDS_RDBI, setter
[34m[1mpassed[0m 443FFCD7 000.00s Test observable dict used in UDS_RDBI, deleter
[34m[1mpassed[0m E5814EC8 000.00s Check UDS_RDBIPR
[34m[1mpassed[0m 9DD68265 000.00s Check UDS_RMBA
[34m[1mpassed[0m F1907B0D 000.00s Check UDS_RMBA
[34m[1mpassed[0m 84F6FA60 000.00s Check UDS_RMBA
[34m[1mpassed[0m 0D2479F2 000.00s Check UDS_RMBA
[34m[1mpassed[0m B441AEC5 000.00s Check UDS_RMBAPR
[34m[1mpassed[0m 4846774A 000.00s Check UDS_RSDBI
[34m[1mpassed[0m 704CCE5E 000.00s Check UDS_RSDBIPR
[34m[1mpassed[0m 3B1AE612 000.00s Check UDS_RSDBPI
[34m[1mpassed[0m CECD6BC7 000.00s Check UDS_RSDBPIPR
[34m[1mpassed[0m DD7FF8CE 000.00s Check UDS_RSDBPIPR
[34m[1mpassed[0m 7AD6277D 000.00s Check UDS_DDDI
[34m[1mpassed[0m B9494CED 000.00s Check UDS_DDDIPR
[34m[1mpassed[0m F85A34AA 000.00s Check UDS_WDBI
[34m[1mpassed[0m 2115A330 000.00s Build UDS_WDBI
[34m[1mpassed[0m 5CD87E17 000.00s Check UDS_WDBI
[34m[1mpassed[0m AE3CBFCE 000.00s Check UDS_WDBIPR
[34m[1mpassed[0m 636A651D 000.00s Check UDS_WMBA
[34m[1mpassed[0m 8697B783 000.00s Check UDS_WMBAPR
[34m[1mpassed[0m B346F7D4 000.00s Check UDS_WMBA
[34m[1mpassed[0m E5C1AB9D 000.00s Check UDS_WMBAPR
[34m[1mpassed[0m 05B27007 000.00s Check UDS_WMBA
[34m[1mpassed[0m 910979C5 000.00s Check UDS_WMBA
[34m[1mpassed[0m 86E7BBC9 000.00s Check UDS_WMBAPR
[34m[1mpassed[0m 69F5D3CE 000.00s Check UDS_WMBAPR
[34m[1mpassed[0m A48F6457 000.00s Check UDS_CDTCI
[34m[1mpassed[0m C5B2900D 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 444B5FE2 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 86A2FE15 000.00s Check UDS_RDTCIPR
[34m[1mpassed[0m 39C75A41 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 268596E7 000.00s Check UDS_RDTCI
[34m[1mpassed[0m C8058810 000.00s Check UDS_RDTCI
[34m[1mpassed[0m B5898DB3 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 28228CED 000.00s Check UDS_RDTCI
[34m[1mpassed[0m A9449724 000.00s Check UDS_RDTCI
[34m[1mpassed[0m B9E1DEAD 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 9FDA439B 000.00s Check UDS_RDTCI
[34m[1mpassed[0m C681773F 000.00s Check UDS_RDTCI
[34m[1mpassed[0m A5A8E72E 000.00s Check UDS_RDTCI
[34m[1mpassed[0m C334C3A9 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 794A3A6E 000.00s Check UDS_RDTCI
[34m[1mpassed[0m 0A76CAAC 000.00s Check UDS_RDTCI
[34m[1mpassed[0m AC8D243B 000.00s Check UDS_RDTCIPR
[34m[1mpassed[0m 6A7CAADB 000.00s Check UDS_RDTCIPR
[34m[1mpassed[0m CA677F72 000.00s Check UDS_RC
[34m[1mpassed[0m CA677F72 000.00s Check UDS_RC
[34m[1mpassed[0m E07A4854 000.00s Check UDS_RCPR
[34m[1mpassed[0m A0E9FD10 000.00s Check UDS_RD
[34m[1mpassed[0m 8BD92731 000.00s Check UDS_RD
[34m[1mpassed[0m 1585E341 000.00s Check UDS_RD
[34m[1mpassed[0m C9371D4B 000.00s Check UDS_RD
[34m[1mpassed[0m 76505115 000.00s Check UDS_RDPR
[34m[1mpassed[0m 44842A6C 000.00s Check UDS_RU
[34m[1mpassed[0m CA8C839D 000.00s Check UDS_RU
[34m[1mpassed[0m 164DFDDB 000.00s Check UDS_RU
[34m[1mpassed[0m C7160390 000.00s Check UDS_RU
[34m[1mpassed[0m 01E9A645 000.00s Check UDS_RUPR
[34m[1mpassed[0m 802F6373 000.00s Check UDS_TD
[34m[1mpassed[0m 802F6373 000.00s Check UDS_TD
[34m[1mpassed[0m 40A5D5FF 000.00s Check UDS_TDPR
[34m[1mpassed[0m B53AFA45 000.00s Check UDS_RTE
[34m[1mpassed[0m 1E26FA61 000.00s Check UDS_RTEPR
[34m[1mpassed[0m 992F4435 000.00s Check UDS_IOCBI
[34m[1mpassed[0m EF0034A3 000.00s Check UDS_RFT
[34m[1mpassed[0m 9B9A78F4 000.00s Build UDS_RFT
[34m[1mpassed[0m F2DE154C 000.00s Check UDS_RFTPR
[34m[1mpassed[0m F22BC6DC 000.00s Build UDS_RFTPR
[34m[1mpassed[0m 347BF383 000.00s Check UDS_NRC
Campaign CRC=4C71D3FF in 000.08s SHA=9F6803E014455F7C878B1C222F56192984A4646E
[34m[1mPASSED=157 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/obd/obd.uts[0m
[34m[1mpassed[0m 86B3692B 000.03s Load module
[34m[1mpassed[0m 09631DE9 000.00s Check if positive response answers
[34m[1mpassed[0m 99E8D9F9 000.00s Check hashret
[34m[1mpassed[0m C86B7A3A 000.00s Check if negative response answers
[34m[1mpassed[0m E06C458E 000.00s Check if negative response request_correctly_received_response_pending answers not
[34m[1mpassed[0m 08F48011 000.00s Check if negative response request_correctly_received_response_pending answers
[34m[1mpassed[0m 99E8D9F9 000.00s Check hashret
[34m[1mpassed[0m EFA2CB3C 000.00s Check hashret for Service 0x40
[34m[1mpassed[0m 2215B603 000.00s Check hashret for Service 0x51
[34m[1mpassed[0m 028A2E01 000.00s Check dissecting a request for Service 01 PID 00
[34m[1mpassed[0m 8B5551B7 000.00s Check dissecting a request for Service 01 PID 75
[34m[1mpassed[0m 18EFCB98 000.00s Check dissecting a request for Service 01 PID 78
[34m[1mpassed[0m 2F686BCD 000.00s Check dissecting a request for Service 01 PID 7F
[34m[1mpassed[0m 62E182C0 000.00s Check dissecting a request for Service 01 PID 89
[34m[1mpassed[0m 70BB9AA7 000.00s Check dissecting a request for Service 02 PID 00
[34m[1mpassed[0m 29D68AD8 000.00s Check dissecting a request for Service 02 PID 75
[34m[1mpassed[0m F2BBD2A0 000.00s Check dissecting a request for Service 02 PID 78
[34m[1mpassed[0m 6FF03E8E 000.00s Check dissecting a request for Service 02 PID 7F
[34m[1mpassed[0m 76693B81 000.00s Check dissecting a request for Service 02 PID 89
[34m[1mpassed[0m 2F992FEB 000.00s Check dissecting a request for Service 03
[34m[1mpassed[0m 53B22920 000.00s Check dissecting a request for Service 06
[34m[1mpassed[0m 4D79E5BB 000.00s Check dissecting a request for Service 06 MID 00
[34m[1mpassed[0m 544688DB 000.00s Check dissecting a request for Service 06 MID 00,01,02,03,04
[34m[1mpassed[0m 416D7934 000.00s Check dissecting a response for Service 06 MID 00
[34m[1mpassed[0m 2D22B64B 000.00s Check dissecting a response for Service 06 MID 00 and MID 20
[34m[1mpassed[0m 5E82023D 000.00s Check dissecting a response for Service 06 MID 00, 20, 40, 60, 80, A0
[34m[1mpassed[0m 4F23256B 000.00s Check dissecting a response for Service 06 MID 01
[34m[1mpassed[0m E13A3385 000.00s Check dissecting a response for Service 06 MID 21
[34m[1mpassed[0m 0ACDE022 000.00s Check dissecting a request for Service 09 IID 00
[34m[1mpassed[0m 375A7914 000.00s Check dissecting a request for Service 09 IID 02
[34m[1mpassed[0m 71E2D24E 000.00s Check dissecting a request for Service 09 IID 04
[34m[1mpassed[0m FFCD39F1 000.00s Check dissecting a request for Service 09 IID 00 and IID 02 and IID 04
[34m[1mpassed[0m 9367436E 000.00s Check dissecting a request for Service 09 IID 0A
[34m[1mpassed[0m 30090832 000.00s Check dissecting a response for Service 01 PID 75
[34m[1mpassed[0m 12A9A014 000.00s Check dissecting a response for Service 01 PID 00 and PID 20
[34m[1mpassed[0m 35060A7A 000.00s Check dissecting a response for Service 01 PID 05,01,15,0C,03
[34m[1mpassed[0m 3A660814 000.00s Check dissecting a response for Service 01 PID 78
[34m[1mpassed[0m 6D79E9B2 000.00s Check dissecting a response for Service 01 PID 7F
[34m[1mpassed[0m AA5662FA 000.00s Check dissecting a response for Service 01 PID 89
[34m[1mpassed[0m 9D159259 000.00s Check dissecting a response for Service 02 PID 75
[34m[1mpassed[0m B5650350 000.00s Check dissecting a response for Service 02 PID 78
[34m[1mpassed[0m 1412DC4D 000.00s Check dissecting a response for Service 02 PID 7F
[34m[1mpassed[0m FB164C22 000.00s Check dissecting a response for Service 02 PID 89
[34m[1mpassed[0m 3D21C643 000.00s Check dissecting a response for Service 02 PID 0C, 05, 04
[34m[1mpassed[0m E3BFFB8D 000.00s Check dissecting a response for Service 03
[34m[1mpassed[0m 29E7ACFA 000.00s Check dissecting a response for Service 07
[34m[1mpassed[0m 7E4975EA 000.00s Check dissecting a response for Service 08 Tid 00
[34m[1mpassed[0m 9991DC14 000.00s Check dissecting a response for Service 08 Tid 01
[34m[1mpassed[0m 66EA0DD4 000.00s Check dissecting a response for Service 08 Tid 05
[34m[1mpassed[0m 1BB19F97 000.00s Check dissecting a response for Service 08 Tid 09
[34m[1mpassed[0m 098B43D5 000.00s Check dissecting a response for Service 09 IID 00
[34m[1mpassed[0m 00068ABA 000.00s Check dissecting a response for Service 09 IID 02 with one VIN
[34m[1mpassed[0m 29317CB3 000.00s Check dissecting a response for Service 09 IID 02 with two VINs
[34m[1mpassed[0m B2393F06 000.00s Check dissecting a response for Service 09 IID 04 with one CID
[34m[1mpassed[0m A5656F3E 000.00s Check dissecting a response for Service 09 IID 04 with two CID
[34m[1mpassed[0m 10FA3EF2 000.00s Check dissecting a response for Service 09 IID 06
[34m[1mpassed[0m 3BF4C16B 000.00s Check dissecting a response for Service 09 IID 08
[34m[1mpassed[0m A1025ABB 000.00s Check dissecting a response for Service 09 IID 0A
[34m[1mpassed[0m 0F7E79AC 000.00s Check dissecting a response for Service 09 IID 0B
[34m[1mpassed[0m 900FC324 000.00s Check dissecting a response for Service 09 IID 02 and IID 04
[34m[1mpassed[0m 33F470F1 000.00s Check building a request for Service 01 PID 00
[34m[1mpassed[0m 83F1C490 000.00s Check building a request for Service 01 PID 75
[34m[1mpassed[0m 04FB2BD6 000.00s Check building a request for Service 01 PID 78
[34m[1mpassed[0m 2C15104C 000.00s Check building a request for Service 01 PID 7F
[34m[1mpassed[0m 9265286B 000.00s Check building a request for Service 01 PID 89
[34m[1mpassed[0m EA4A98EC 000.00s Check building a request for Service 02 PID 00
[34m[1mpassed[0m 5AE576C3 000.00s Check building a request for Service 02 PID 75
[34m[1mpassed[0m 4FFDAFCD 000.00s Check building a request for Service 02 PID 78
[34m[1mpassed[0m F0871DD4 000.00s Check building a request for Service 02 PID 7F
[34m[1mpassed[0m D44AF663 000.00s Check building a request for Service 02 PID 89
[34m[1mpassed[0m 103D9166 000.00s Check building a request for Service 03
[34m[1mpassed[0m F0871DD4 000.00s Check building a request for Service 02 PID 7F
[34m[1mpassed[0m 98D0779A 000.00s Check building a request for Service 09 IID 00
[34m[1mpassed[0m 7043B695 000.00s Check building a request for Service 09 IID 02
[34m[1mpassed[0m 9286F3C5 000.00s Check building a request for Service 09 IID 04
[34m[1mpassed[0m 7C644169 000.00s Check building a request for Service 09 IID 00 and IID 02 and IID 04
[34m[1mpassed[0m DFA76249 000.00s Check building a request for Service 09 IID 0A
[34m[1mpassed[0m 9057F79F 000.00s Check building a response for Service 03
[34m[1mpassed[0m 24983FA6 000.00s Check building a default response for Service 03
[34m[1mpassed[0m B809EBAA 000.00s Check building a response for Service 07
[34m[1mpassed[0m 2DF1F17D 000.00s Check building a default response for Service 07
[34m[1mpassed[0m 4B6D2A63 000.00s Check building a response for Service 0A
[34m[1mpassed[0m 3704F777 000.00s Check building a default response for Service 0A
[34m[1mpassed[0m 1191C579 000.00s Check building a response for Service 09 IID 00
[34m[1mpassed[0m EAB7FC32 000.00s Check building a response for Service 09 IID 02 with one VIN
[34m[1mpassed[0m 0AE26D94 000.00s Check building a response for Service 09 IID 02 with two VINs
[34m[1mpassed[0m B46615E7 000.00s Check building a response for Service 09 IID 04 with one CID
[34m[1mpassed[0m 694755B4 000.00s Check building a response for Service 09 IID 04 with two CID
[34m[1mpassed[0m 8A260EFB 000.00s Check building a response for Service 09 IID 0A
[34m[1mpassed[0m 0B4324F3 000.00s Check building a response for Service 09 IID 02 and IID 04
Campaign CRC=16DDA680 in 000.10s SHA=0478438E8085402AEA6505C6350C2727FD5DB8EC
[34m[1mPASSED=90 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/obd/scanner.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m 172A0B3E 000.01s Load contribution layer
[34m[1mpassed[0m 508FD752 000.00s Create sockets
[34m[1mpassed[0m 09196AB1 000.28s Create answers
[34m[1mpassed[0m 7B5CF409 000.17s Run scanner with real world responses short scan
[34m[1mpassed[0m 0B2124AF 001.35s Run scanner with real world responses full scan
[34m[1mpassed[0m 8D747CD7 000.04s Run scanner only for Service 01 real world responses
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=407EFEFE in 001.85s SHA=174482FD3AADF8FA78787FA43396895872C694EE
[34m[1mPASSED=8 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/scanner/configuration.uts[0m
[34m[1mpassed[0m 09267931 000.00s Load contribution layer
[34m[1mpassed[0m 60ABD021 000.00s Definition of Test classes
[34m[1mpassed[0m 9F723DD0 000.00s creation of config with classes
[34m[1mpassed[0m 8AFD9038 000.00s creation of config with instances
[34m[1mpassed[0m B468D37E 000.00s creation of config with instances and classes
[34m[1mpassed[0m A9BD3A34 000.00s creation of config with instances and classes and global configuration and local configuration
[34m[1mpassed[0m C0F660F6 000.00s creation of config with stages
[34m[1mpassed[0m DDE0A351 000.00s creation of config with stages class
Campaign CRC=3F068150 in 000.01s SHA=4F369ADA7D1A306964E13E11D150BC183CB11F5A
[34m[1mPASSED=8 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/scanner/enumerator.uts[0m
[34m[1mpassed[0m BF9EC181 000.00s Load contribution layer
[34m[1mpassed[0m 274208C7 000.01s ServiceEnumerator basecls checks
[34m[1mpassed[0m C9D0A14B 000.00s ServiceEnumerator not completed check
[34m[1mpassed[0m F8EBACA1 000.00s ServiceEnumerator completed
[34m[1mpassed[0m 01F4D2F4 000.00s ServiceEnumerator stats check
[34m[1mpassed[0m CEB1EC55 000.00s ServiceEnumerator scanned states
[34m[1mpassed[0m 67CE1DDE 000.00s ServiceEnumerator scanned results
[34m[1mpassed[0m 57330AE1 000.00s ServiceEnumerator get_label
[34m[1mpassed[0m 0563CC73 000.00s ServiceEnumerator show
[34m[1mpassed[0m A953C35E 000.00s ServiceEnumerator filtered results before show
[34m[1mpassed[0m 58DB2D48 000.00s ServiceEnumerator show filtered
[34m[1mpassed[0m E7659DBF 000.00s ServiceEnumerator filtered results after show
[34m[1mpassed[0m E8C489BD 000.00s ServiceEnumerator supported responses
[34m[1mpassed[0m 0C2AD14A 000.00s ServiceEnumerator evaluate response
[34m[1mpassed[0m 4F11368C 000.13s ServiceEnumerator execute
[34m[1mpassed[0m 1CBD89F1 000.00s Test negative response code service not supported
[34m[1mpassed[0m 5566C139 000.09s Test negative response code retry if busy
[34m[1mpassed[0m B1D752EB 000.09s Test negative response code don't retry if busy
[34m[1mpassed[0m EA161969 000.00s Test execution time
[34m[1mpassed[0m 083DE3A7 000.00s Definitions
[34m[1mpassed[0m C290DE65 000.00s Basic tests
[34m[1mpassed[0m E0AD11E6 000.00s Basic tests with default values
[34m[1mpassed[0m 29AA20A0 000.00s Basic test with stages
[34m[1mpassed[0m D05D211D 000.00s Basic tests with two stages
[34m[1mpassed[0m 30B776C3 000.00s Reset Handler tests
[34m[1mpassed[0m 0E74913D 000.00s Reset Handler tests 2
[34m[1mpassed[0m D4AE2482 000.00s Reconnect Handler tests
[34m[1mpassed[0m 8BB67759 000.00s Reconnect Handler tests 2
[34m[1mpassed[0m 4716493D 000.01s TestCase execute
[34m[1mpassed[0m 09E11BD7 000.00s TestCase execute StateGenerator
[34m[1mpassed[0m EAC6CF3A 000.00s TestCase execute StateGenerator no edge
[34m[1mpassed[0m C8F7EA09 000.00s TestCase execute StateGenerator with cleanupfunc
[34m[1mpassed[0m 8B94E799 000.00s TestCase execute StateGenerator with not callable cleanupfunc
[34m[1mpassed[0m 6DEC725C 000.00s TestCase execute StateGenerator with cleanupfunc negative return
[34m[1mpassed[0m 02AECA94 000.01s TestCase execute StateGenerator with cleanupfunc and path
[34m[1mpassed[0m 060AECAF 000.00s Test downrate edge
[34m[1mpassed[0m 23C3F1AE 000.00s TestCase execute TestCaseGenerator
[34m[1mpassed[0m BA959E75 000.00s TestCase scan timeout
[34m[1mpassed[0m CEFE4823 000.00s TestCase scan
[34m[1mpassed[0m 0CC2ADEF 000.01s Test supported responses
[34m[1mpassed[0m B6AAF471 000.01s Test show testcases
[34m[1mpassed[0m 921B020F 000.00s Test StateGeneratingServiceEnumerator
Campaign CRC=E485736D in 000.40s SHA=FD6356FC6B4E0C79DE370A6E4E2C703043FDD4A0
[34m[1mPASSED=42 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/scanner/graph.uts[0m
[34m[1mpassed[0m 8A70A10D 000.00s Load contribution layer
[34m[1mpassed[0m 656E2A91 000.00s Basic test
[34m[1mpassed[0m 8B545210 000.00s Shortest path test
[34m[1mpassed[0m 283DF909 000.00s graph add transition function
[34m[1mpassed[0m 39D6684B 000.00s graph pickle
Campaign CRC=5809081D in 000.00s SHA=CA81534DAD431B57C43DAB947137F4C4C37E9221
[34m[1mPASSED=5 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/scanner/staged_test_case.uts[0m
[34m[1mpassed[0m 8524E5AE 000.00s Load contribution layer
[34m[1mpassed[0m B8CA1B31 000.00s Definition of Test classes
[34m[1mpassed[0m 965F3D5B 000.00s Create instance of stage test
[34m[1mpassed[0m DA7DE0BE 000.00s Check completion
[34m[1mpassed[0m 6211ADC8 000.00s Check completion 2
[34m[1mpassed[0m 0C8DA98B 000.00s Check supported responses
[34m[1mpassed[0m CE10140E 000.00s Check connector
[34m[1mpassed[0m BA45360F 000.00s Check show
[34m[1mpassed[0m 930865F9 000.00s Check len
[34m[1mpassed[0m A32FAA08 000.00s Check generator functions
Campaign CRC=F67EAA6D in 000.01s SHA=B30E4175582797B7436F14A56A33E8991824FB8D
[34m[1mPASSED=10 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/scanner/test_case.uts[0m
[34m[1mpassed[0m A7876863 000.00s Load contribution layer
[34m[1mpassed[0m C3103B29 000.00s Definition of Test class
[34m[1mpassed[0m 7E43CEFF 000.00s Create instance of test class
[34m[1mpassed[0m E00C367A 000.00s Tests of has_completed
[34m[1mpassed[0m E903E00B 000.00s Tests of has_completed with new state
[34m[1mpassed[0m 420DE033 000.00s Tests of completed
[34m[1mpassed[0m 75E17155 000.00s Test of show
Campaign CRC=B56D6FEF in 000.00s SHA=9EA32A68BF6D1FD93BD09F4695F16F3979893D20
[34m[1mPASSED=7 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/scanner/uds_scanner.uts[0m
[34m[1mpassed[0m C682A522 000.00s Imports
[34m[1mpassed[0m 00527800 000.01s Load contribution layer
[34m[1mpassed[0m 77CDDC97 000.01s Define Testfunction
[34m[1mpassed[0m 60E862A5 000.37s Load packets from pcap
[34m[1mpassed[0m 5A2CCBD4 000.35s Create UDS messages from packets
[34m[1mpassed[0m 0E29EEEC 001.12s Create ECU-Clone from packets
[34m[1mpassed[0m 62A05109 000.00s Test UDS_SAEnumerator evaluate_response
[34m[1mpassed[0m DA963438 007.81s Simulate ECU and run Scanner
[34m[1mpassed[0m 5541ACD7 002.80s UDS_RDBIEnumerator
[34m[1mpassed[0m B7D3060A 003.61s UDS_RDBISelectiveEnumerator
[34m[1mpassed[0m F273617A 002.97s UDS_WDBIEnumerator
[34m[1mpassed[0m DCE2398C 002.97s UDS_WDBIEnumerator 2
[34m[1mpassed[0m 74EBED5E 000.05s UDS_TPEnumerator
[34m[1mpassed[0m 1727E99E 002.73s UDS_EREnumerator
[34m[1mpassed[0m 15FCF291 002.95s UDS_CCEnumerator
[34m[1mpassed[0m 1E1154F0 002.86s UDS_RDBPIEnumerator
[34m[1mpassed[0m 4ADB5AE7 000.58s UDS_RCEnumerator
[34m[1mpassed[0m 0F3684FC 006.44s UDS_RCSelectiveEnumerator
[34m[1mpassed[0m F8FD1DA1 002.82s UDS_IOCBIEnumerator
[34m[1mpassed[0m ED36D59D 006.84s UDS_RDEnumerator
[34m[1mpassed[0m 4E764564 002.75s UDS_TDEnumerator
[34m[1mpassed[0m D0993902 002.96s BMW_DevJobEnumerator
[34m[1mpassed[0m AE223815 000.00s Delete testsockets
Campaign CRC=635BB180 in 052.99s SHA=1CBDA2EE901B32F84AF3E0D69F130CBD54E2B988
[34m[1mPASSED=23 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/gm/gmlan.uts[0m
[34m[1mpassed[0m C8FCC42A 000.00s Load gmlan layer
[34m[1mpassed[0m 4D1A1B99 000.00s Set GMLAN ECU AddressingScheme
[34m[1mpassed[0m 58F0CBC4 000.00s Craft Packet
[34m[1mpassed[0m D92AF7EC 000.00s Craft VIN Packet
[34m[1mpassed[0m C8931BD6 000.00s Test Packet with ECU AddressingScheme2
[34m[1mpassed[0m E5D4D950 000.00s Test Packet GMLAN_RMBAPR with ECU AddressingScheme2
[34m[1mpassed[0m C375A45A 000.00s Craft Packet with ECU AddressingScheme2
[34m[1mpassed[0m 21ACA3EA 000.00s Test Packet with ECU AddressingScheme3
[34m[1mpassed[0m E810E48C 000.00s Test Packet GMLAN_RMBAPR with ECU AddressingScheme3
[34m[1mpassed[0m 54A48BFE 000.00s Craft Packet with ECU AddressingScheme3
[34m[1mpassed[0m 82D1A4EE 000.00s Test Packet with ECU AddressingScheme4
[34m[1mpassed[0m F800B37E 000.00s Test Packet GMLAN_RMBAPR with ECU AddressingScheme4
[34m[1mpassed[0m 15E9D55D 000.00s Craft Packet with ECU AddressingScheme4
[34m[1mpassed[0m EA7690DA 000.00s Craft Packet for RequestDownload2
[34m[1mpassed[0m F94CF433 000.00s Craft Packet for RequestDownload3
[34m[1mpassed[0m C2F663A2 000.00s Craft Packet for RequestDownload4
[34m[1mpassed[0m 1858C378 000.00s Craft Packet for RFRD1
[34m[1mpassed[0m 582B5F1C 000.00s Craft Packet for RFRD2
[34m[1mpassed[0m 52510EA6 000.00s Craft Packet for RFRDPR_RFRI
[34m[1mpassed[0m 674C2FDB 000.00s Craft Packet for RFRDPR_RFRI
[34m[1mpassed[0m A274DB37 000.00s Craft Packet for RFRDPR_RFRP
[34m[1mpassed[0m CF6A5524 000.00s Craft Packet for RDBI
[34m[1mpassed[0m 99982932 000.00s Craft Packet for RDBIPR
[34m[1mpassed[0m 11EA7370 000.00s Craft Packet for RDBPI
[34m[1mpassed[0m 4C9F050E 000.00s Craft Packet for RDBPIPR
[34m[1mpassed[0m E6A9A0C7 000.00s Craft Packet for GMLAN_RDBPKTI1
[34m[1mpassed[0m FD51D8D0 000.00s Craft Packet for GMLAN_RDBPKTI3
[34m[1mpassed[0m 42D6F2E2 000.00s Craft Packet for GMLAN_RDBPKTI4
[34m[1mpassed[0m 3EC8A404 000.00s Craft Packet for GMLAN_RDBPKTI2
[34m[1mpassed[0m F7D21E89 000.00s Build GMLAN_RDBPKTI1
[34m[1mpassed[0m F58F36FB 000.00s Craft Packet for GMLAN_SA1
[34m[1mpassed[0m 6D5011C4 000.00s Craft Packet for GMLAN_SA2
[34m[1mpassed[0m 4877ED60 000.00s Craft Packet for GMLAN_SAPR1
[34m[1mpassed[0m D4C21FEB 000.00s Craft Packet for GMLAN_SAPR2
[34m[1mpassed[0m CEAE6C69 000.00s Craft Packet for GMLAN_DDM
[34m[1mpassed[0m F62D03B2 000.00s Craft Packet for GMLAN_DDMPR
[34m[1mpassed[0m 12265B47 000.00s Craft Packet for GMLAN_DPBA1
[34m[1mpassed[0m 905A8B6A 000.00s Craft Packet for GMLAN_DPBA2
[34m[1mpassed[0m AB9D1930 000.00s Craft Packet for GMLAN_DPBA3
[34m[1mpassed[0m 8ACD8C5B 000.00s Craft Packet for GMLAN_DPBAPR
[34m[1mpassed[0m 25A90E0D 000.00s Craft Packet for GMLAN_RD1
[34m[1mpassed[0m 5335EE99 000.00s Craft Packet for GMLAN_RD2
[34m[1mpassed[0m DEDA4E18 000.00s Craft Packet for GMLAN_RD3
[34m[1mpassed[0m 267CDEFC 000.00s Craft Packet for GMLAN_TD1
[34m[1mpassed[0m 9956234D 000.00s Craft Packet for GMLAN_TD2
[34m[1mpassed[0m CA3253DF 000.00s Craft Packet for GMLAN_TD3
[34m[1mpassed[0m 362FCE5A 000.00s Craft Packet for WDBI
[34m[1mpassed[0m E95808D4 000.00s Craft Packet for WDBIPR
[34m[1mpassed[0m 6944176B 000.00s Craft Packet for RPSPR
[34m[1mpassed[0m 98AAF4AF 000.00s Craft Packet for PM
[34m[1mpassed[0m 1BF06A65 000.00s Craft Packet for RDI
[34m[1mpassed[0m E3E3E68B 000.00s Craft Packet for RDI_BN
[34m[1mpassed[0m DCAF0B43 000.00s Craft Packet for RDI_BM1
[34m[1mpassed[0m 5C79D869 000.00s Craft Packet for RDI_BM2
[34m[1mpassed[0m 8A3A66FD 000.00s Craft Packet for NR
[34m[1mpassed[0m A5641895 000.00s Check not answers
[34m[1mpassed[0m 4B65CCE6 000.00s Check answers 1
[34m[1mpassed[0m 68DFC885 000.00s Set treat-response-pending-as-answer
[34m[1mpassed[0m 6AF7A292 000.00s Check response-pending is not considered as answer
[34m[1mpassed[0m 78C00978 000.00s Check response-pending is considered as answer
[34m[1mpassed[0m F8517E36 000.00s Check hashret 1
[34m[1mpassed[0m 315E92A3 000.00s Check answers 2
[34m[1mpassed[0m 4140D313 000.00s Check hashret 2
[34m[1mpassed[0m 096744DC 000.00s Check modifies ecu state
[34m[1mpassed[0m D8735CF1 000.00s Craft GMLAN_DC
[34m[1mpassed[0m 1658184D 000.00s Dissect test GMLAN_DC
Campaign CRC=232D0DBB in 000.04s SHA=EA3AADB20F35D23E4993F90A10E8ED313DBAAE7F
[34m[1mPASSED=66 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/gm/gmlanutils.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m DEE00C33 000.00s Load contribution layer
[34m[1mpassed[0m 14A578DB 000.00s Define test sockets
[34m[1mpassed[0m FFE739B8 000.01s Positive, immediate positive response
[34m[1mpassed[0m 65609F35 000.01s Negative, immediate negative response
[34m[1mpassed[0m 9C284252 001.00s Negative, timeout
[34m[1mpassed[0m 3A977BB5 000.01s Positive, after response pending
[34m[1mpassed[0m 48DE0071 000.41s Positive, hold response pending for several messages
[34m[1mpassed[0m 89D42400 000.01s Negative, negative response after response pending
[34m[1mpassed[0m 3D434589 000.31s Negative, timeout after response pending
[34m[1mpassed[0m 283C16AA 000.31s Positive, pending message from different service interferes while pending
[34m[1mpassed[0m 1051232C 000.31s Positive, negative response from different service interferes while pending
[34m[1mpassed[0m 4B2F39E1 000.02s Positive, first: immediate negative response, retry: Positive
[34m[1mpassed[0m 6718EBAD 000.01s Positive, short payload, scheme = 4
[34m[1mpassed[0m 391D6742 000.01s Positive, short payload, scheme = 3
[34m[1mpassed[0m 007D71CB 000.01s Positive, short payload, scheme = 2
[34m[1mpassed[0m CDFD0CF3 000.01s Negative, short payload
[34m[1mpassed[0m E5695686 001.00s Negative, timeout
[34m[1mpassed[0m 0BBCC730 000.02s Positive, long payload
[34m[1mpassed[0m C1E6C74A 000.12s Positive, first part of payload succeeds, second pending, then fails, retry succeeds
[34m[1mpassed[0m A292FAEC 000.22s Positive, maxmsglen length check -> message is split automatically
[34m[1mpassed[0m CE47E9BE 000.01s Positive, highest possible address for scheme
[34m[1mpassed[0m CE3B4098 001.01s Negative, invalid address (too large for addressing scheme)
[34m[1mpassed[0m 140D6BF3 000.01s Positive, address zero
[34m[1mpassed[0m 6F6A3E10 001.01s Negative, negative address
[34m[1mpassed[0m 5B373FA1 000.22s Positive, short payload
[34m[1mpassed[0m 5474AFAF 000.00s KeyFunction
[34m[1mpassed[0m 634E015E 000.30s Positive scenario, level 1, tests if keyfunction applied properly
[34m[1mpassed[0m 5B550631 000.22s Positive scenario, level 3
[34m[1mpassed[0m 69E14CE1 000.22s Negative scenario, invalid password
[34m[1mpassed[0m E1A03DF3 000.00s invalid level (not an odd number)
[34m[1mpassed[0m 9A5903F9 000.11s zero seed
[34m[1mpassed[0m 0B213984 001.22s Positive scenario, request timeout, retry works
[34m[1mpassed[0m 3159E656 001.32s Positive scenario, keysend timeout, retry works
[34m[1mpassed[0m 20C901D4 000.32s Positive scenario, request error, retry works
[34m[1mpassed[0m BDE80CC2 000.42s sequence of the correct messages
[34m[1mpassed[0m CE89EF51 000.12s sequence of the correct messages, disablenormalcommunication as broadcast
[34m[1mpassed[0m 6541C9DC 001.01s timeout DisableNormalCommunication
[34m[1mpassed[0m 9E649697 001.07s timeout ReportProgrammedState
[34m[1mpassed[0m 06233226 001.07s timeout ProgrammingMode requestProgramming
[34m[1mpassed[0m 5AB55218 000.01s timeout DisableNormalCommunication
[34m[1mpassed[0m 70D3480B 000.12s sequence of the correct messages, retry set
[34m[1mpassed[0m 4BA2079D 001.01s negative response, make sure no retries are made
[34m[1mpassed[0m 5A8C448F 000.12s first fail at DisableNormalCommunication, then sequence of the correct messages
[34m[1mpassed[0m 65C0A06A 000.17s first fail at ReportProgrammedState, then sequence of the correct messages
[34m[1mpassed[0m CDF13784 000.17s first fail at ProgrammingMode requestProgramming, then sequence of the correct messages
[34m[1mpassed[0m A54275D2 001.01s fail twice
[34m[1mpassed[0m CF7E3A53 000.01s Positive, short length, scheme = 4
[34m[1mpassed[0m 8A4EEC02 000.01s Negative, negative response
[34m[1mpassed[0m 44EB6592 001.00s Negative, timeout
[34m[1mpassed[0m E8CE8783 000.01s Positive, negative response, retry succeeds
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=9531A2A1 in 017.14s SHA=19BC88C3D197F3006484716D644F588BA036046B
[34m[1mPASSED=52 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/gm/scanner.uts[0m
[34m[1mpassed[0m 2FC6B503 000.00s Imports
[34m[1mpassed[0m AE2C40A6 000.00s Load contribution layer
[34m[1mpassed[0m 9323681C 000.01s Define Testfunction
[34m[1mpassed[0m 8928C40D 000.12s Load packets from candump
[34m[1mpassed[0m B1148D1E 000.15s Create GMLAN messages from packets
[34m[1mpassed[0m 0E29EEEC 000.63s Create ECU-Clone from packets
[34m[1mpassed[0m C6B3AB0A 000.00s Test GMLAN_SAEnumerator evaluate_response
[34m[1mpassed[0m 6D52A2D9 005.56s Simulate ECU and run Scanner
[34m[1mpassed[0m E48DEC6F 000.32s Simulate ECU and test GMLAN_WDBIEnumerator
[34m[1mpassed[0m 7F49B4F5 000.36s Simulate ECU and test GMLAN_RDBPIEnumerator
[34m[1mpassed[0m 3949EF90 000.05s Simulate ECU and test GMLAN_TPEnumerator
[34m[1mpassed[0m 133F87E2 000.20s Simulate ECU and test GMLAN_DCEnumerator
[34m[1mpassed[0m 7756080E 000.47s Simulate ECU and test GMLAN_TDEnumerator
[34m[1mpassed[0m F6B35925 002.79s Simulate ECU and test GMLAN_RMBAEnumerator 1
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=81873933 in 010.65s SHA=94953A26F42527C39FA3747BEEC1DBBCDAF321FA
[34m[1mPASSED=15 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/bmw/hsfz.uts[0m
[34m[1mpassed[0m C56FF620 000.00s Load Contrib Layer
[34m[1mpassed[0m A588909F 000.00s Basic Test 1
[34m[1mpassed[0m ADF00B08 000.00s Basic Test 2
[34m[1mpassed[0m 1AE1112D 000.00s Basic Dissect Test
[34m[1mpassed[0m 0696C065 000.00s Build Test
[34m[1mpassed[0m C30FD3A0 000.00s Dissect Test
[34m[1mpassed[0m 33DC1E88 000.00s Dissect Test with padding
[34m[1mpassed[0m 5148ADAE 000.00s Dissect Test to short packet
[34m[1mpassed[0m C3862BC2 000.00s Dissect Test very long packet
Campaign CRC=F0D92AC7 in 000.01s SHA=2FCEB9F01C814ADFB2C73353E0B43B6CEB69BD69
[34m[1mPASSED=9 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/xcp/xcp.uts[0m
[34m[1mpassed[0m 0B97782B 000.00s Load module
[34m[1mpassed[0m DBB392DA 000.00s Test padding
[34m[1mpassed[0m 45448FEE 000.00s test_get_com_mode_info
[34m[1mpassed[0m EDF7DB7F 000.00s test_get_status
[34m[1mpassed[0m FE341520 000.00s test_get_seed
[34m[1mpassed[0m D3B7DB05 000.00s test_unlock
[34m[1mpassed[0m FAB931CD 000.00s test_get_id
[34m[1mpassed[0m E5981158 000.00s test_upload
[34m[1mpassed[0m 8CD1E8E0 000.00s test_cal_page
[34m[1mpassed[0m 20706642 000.00s test_set_mta
[34m[1mpassed[0m 1D7538F5 000.00s test_build_checksum
[34m[1mpassed[0m 165AF40F 000.00s test_download
[34m[1mpassed[0m 03986164 000.00s test_short_upload
[34m[1mpassed[0m CA56518F 000.00s test_copy_cal_page
[34m[1mpassed[0m A3F18ED4 000.00s test_get_daq_processor_info
[34m[1mpassed[0m 3445BBF8 000.00s test_daq_resolution_info
[34m[1mpassed[0m 27B66598 000.00s test_daq_event_info
[34m[1mpassed[0m 7B83627E 000.00s test_daq_list_info
[34m[1mpassed[0m 4C749C30 000.00s test_clear_daq_list
[34m[1mpassed[0m C04ADA41 000.00s test_alloc_daq
[34m[1mpassed[0m 1DDCFCBF 000.00s test_alloc_odt
[34m[1mpassed[0m 73768A65 000.00s test_alloc_odt_entry
[34m[1mpassed[0m 8B8CAFFA 000.00s test_set_daq_ptr
[34m[1mpassed[0m A730FB8F 000.00s test_write_daq
[34m[1mpassed[0m 253EF870 000.00s test_set_daq_list_mode(self):
[34m[1mpassed[0m BDEC536D 000.00s test_start_stop_daq_list
[34m[1mpassed[0m 16B49412 000.00s test_get_daq_clock
[34m[1mpassed[0m 695AF59B 000.00s Test negative response
[34m[1mpassed[0m 41EBF4BE 000.00s test_start_stop_synch
[34m[1mpassed[0m 9BA5999E 000.00s test_program_start
[34m[1mpassed[0m 03269835 000.00s test_program_clear(self):
[34m[1mpassed[0m 2ED18FDC 000.00s test_program
[34m[1mpassed[0m CF332C97 000.00s CONNECT
[34m[1mpassed[0m 92A14FDF 000.00s CONNECT 2
[34m[1mpassed[0m 16C06A7F 000.00s XCPOnUDP post build length
[34m[1mpassed[0m 1DCFE9DE 000.00s CONNECT
[34m[1mpassed[0m 957B3F9A 000.00s XCPOnTCP post build length
Campaign CRC=BA6962F1 in 000.05s SHA=DEA4819A236C13BA1AABBC3D66BAE1DB85BA5E56
[34m[1mPASSED=37 FAILED=0[0m
[32m━ Loading: test/contrib/automotive/xcp/xcp_comm.uts[0m
[34m[1mpassed[0m BF957852 000.00s Imports
[34m[1mpassed[0m 5F32A26A 000.00s Load module
[34m[1mpassed[0m 13E4C18D 000.01s Connect
[34m[1mpassed[0m 4E9238B9 000.00s Endianness test for ConnectPositiveResponse
[34m[1mpassed[0m D51AEF60 000.00s Wrong answer
[34m[1mpassed[0m AE223815 000.00s Delete TestSockets
Campaign CRC=772EC1BB in 000.01s SHA=0A4E911D382CBA327A9CF58E351213997ECB62E4
[34m[1mPASSED=6 FAILED=0[0m
✓ All campaigns executed. Writing output...
[32m
TLS session establishment tests
[0m━ Run at 12:48:41 from [test/tls/tests_tls_netaccess.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Regression tests for Scapy Answering Machines
[0m━ Run at 12:48:41 from [test/answering_machines.uts] by UTscapy in 0.0578455924987793
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:48:41 from [test/cert.uts] by UTscapy in 0.08452439308166504
[34m[1m └ Passed=17
[0m[31m[1m └ Failed=43
[0m
######
## PubKey class tests
######


###(002)=[failed] PubKey class : Importing PEM-encoded RSA public key

[34m[1m>>> [0mx = PubKey("""
... -----BEGIN PUBLIC KEY-----
... MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmFdqP+nTEZukS0lLP+yj
... 1gNImsEIf7P2ySTunceYxwkm4VE5QReDbb2L5/HLA9pPmIeQLSq/BgO1meOcbOSJ
... 2YVHQ28MQ56+8Crb6n28iycX4hp0H3AxRAjh0edX+q3yilvYJ4W9/NnIb/wAZwS0
... oJif/tTkVF77HybAfJde5Eqbp+bCKIvMWnambh9DRUyjrBBZo5dA1o32zpuFBrJd
... I8dmUpw9gtf0F0Ba8lGZm8Uqc0GyXeXOJUE2u7CiMu3M77BM6ZLLTcow5+bQImkm
... TL1SGhzwfinME1e6p3Hm//pDjuJvFaY22k05LgLuyqc59vFiB3Toldz8+AbMNjvz
... AwIDAQAB
... -----END PUBLIC KEY-----
... """)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\x98Wj?\xe9\xd3\x11\x9b\xa4KIK?\xec\xa3\xd6\x03H\x9a\xc1\x08\x7f\xb3\xf6\xc9$\xee\x9d\xc7\x98\xc7\t&\xe1Q9A\x17\x83m\xbd\x8b\xe7\xf1\xcb\x03\xdaO\x98\x87\x90-*\xbf\x06\x03\xb5\x99\xe3\x9cl\xe4\x89\xd9\x85GCo\x0cC\x9e\xbe\xf0*\xdb\xea}\xbc\x8b\'\x17\xe2\x1at\x1fp1D\x08\xe1\xd1\xe7W\xfa\xad\xf2\x8a[\xd8\'\x85\xbd\xfc\xd9\xc8o\xfc\x00g\x04\xb4\xa0\x98\x9f\xfe\xd4\xe4T^\xfb\x1f&\xc0|\x97^\xe4J\x9b\xa7\xe6\xc2(\x8b\xccZv\xa6n\x1fCEL\xa3\xac\x10Y\xa3\x97@\xd6\x8d\xf6\xce\x9b\x85\x06\xb2]#\xc7fR\x9c=\x82\xd7\xf4\x17@Z\xf2Q\x99\x9b\xc5*sA\xb2]\xe5\xce%A6\xbb\xb0\xa22\xed\xcc\xef\xb0L\xe9\x92\xcbM\xca0\xe7\xe6\xd0"i&L\xbdR\x1a\x1c\xf0~)\xcc\x13W\xba\xa7q\xe6\xff\xfaC\x8e\xe2o\x15\xa66\xdaM9.\x02\xee\xca\xa79\xf6\xf1b\x07t\xe8\x95\xdc\xfc\xf8\x06\xcc6;\xf3\x03\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(003)=[failed] PubKey class : Verifying PEM key format

[34m[1m>>> [0mx.frmt == "PEM"
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'x' is not defined


###(004)=[failed] PubKey class : Importing DER-encoded RSA Key

[34m[1m>>> [0my = PubKey(b'0\x82\x01\"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\x98Wj?\xe9\xd3\x11\x9b\xa4KIK?\xec\xa3\xd6\x03H\x9a\xc1\x08\x7f\xb3\xf6\xc9$\xee\x9d\xc7\x98\xc7\t&\xe1Q9A\x17\x83m\xbd\x8b\xe7\xf1\xcb\x03\xdaO\x98\x87\x90-*\xbf\x06\x03\xb5\x99\xe3\x9cl\xe4\x89\xd9\x85GCo\x0cC\x9e\xbe\xf0*\xdb\xea}\xbc\x8b\'\x17\xe2\x1at\x1fp1D\x08\xe1\xd1\xe7W\xfa\xad\xf2\x8a[\xd8\'\x85\xbd\xfc\xd9\xc8o\xfc\x00g\x04\xb4\xa0\x98\x9f\xfe\xd4\xe4T^\xfb\x1f&\xc0|\x97^\xe4J\x9b\xa7\xe6\xc2(\x8b\xccZv\xa6n\x1fCEL\xa3\xac\x10Y\xa3\x97@\xd6\x8d\xf6\xce\x9b\x85\x06\xb2]#\xc7fR\x9c=\x82\xd7\xf4\x17@Z\xf2Q\x99\x9b\xc5*sA\xb2]\xe5\xce%A6\xbb\xb0\xa22\xed\xcc\xef\xb0L\xe9\x92\xcbM\xca0\xe7\xe6\xd0\"i&L\xbdR\x1a\x1c\xf0~)\xcc\x13W\xba\xa7q\xe6\xff\xfaC\x8e\xe2o\x15\xa66\xdaM9.\x02\xee\xca\xa79\xf6\xf1b\x07t\xe8\x95\xdc\xfc\xf8\x06\xcc6;\xf3\x03\x02\x03\x01\x00\x01')
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\x98Wj?\xe9\xd3\x11\x9b\xa4KIK?\xec\xa3\xd6\x03H\x9a\xc1\x08\x7f\xb3\xf6\xc9$\xee\x9d\xc7\x98\xc7\t&\xe1Q9A\x17\x83m\xbd\x8b\xe7\xf1\xcb\x03\xdaO\x98\x87\x90-*\xbf\x06\x03\xb5\x99\xe3\x9cl\xe4\x89\xd9\x85GCo\x0cC\x9e\xbe\xf0*\xdb\xea}\xbc\x8b\'\x17\xe2\x1at\x1fp1D\x08\xe1\xd1\xe7W\xfa\xad\xf2\x8a[\xd8\'\x85\xbd\xfc\xd9\xc8o\xfc\x00g\x04\xb4\xa0\x98\x9f\xfe\xd4\xe4T^\xfb\x1f&\xc0|\x97^\xe4J\x9b\xa7\xe6\xc2(\x8b\xccZv\xa6n\x1fCEL\xa3\xac\x10Y\xa3\x97@\xd6\x8d\xf6\xce\x9b\x85\x06\xb2]#\xc7fR\x9c=\x82\xd7\xf4\x17@Z\xf2Q\x99\x9b\xc5*sA\xb2]\xe5\xce%A6\xbb\xb0\xa22\xed\xcc\xef\xb0L\xe9\x92\xcbM\xca0\xe7\xe6\xd0"i&L\xbdR\x1a\x1c\xf0~)\xcc\x13W\xba\xa7q\xe6\xff\xfaC\x8e\xe2o\x15\xa66\xdaM9.\x02\xee\xca\xa79\xf6\xf1b\x07t\xe8\x95\xdc\xfc\xf8\x06\xcc6;\xf3\x03\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(005)=[failed] PubKey class : Verifying DER key format

[34m[1m>>> [0my.frmt == "DER"
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'y' is not defined


###(006)=[failed] PubKey class : Checking modulus value

[34m[1m>>> [0mx_pubNum.n == y_pubNum.n and x_pubNum.n == 19231328316532061413420367242571475005688288081144416166988378525696075445024135424022026378563116068168327239354659928492979285632474448448624869172454076124150405352043642781483254546569202103296262513098482624188672299255268092629150366527784294463900039290024710152521604731213565912934889752122898104556895316819303096201441834849255370122572613047779766933573375974464479123135292080801384304131606933504677232323037116557327478512106367095125103346134248056463878553619525193565824925835325216545121044922690971718737998420984924512388011040969150550056783451476150234324593710633552558175109683813482739004163
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'x_pubNum' is not defined


###(007)=[failed] PubKey class : Checking public exponent value

[34m[1m>>> [0mx_pubNum.e == y_pubNum.e and x_pubNum.e == 65537
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'x_pubNum' is not defined


###(009)=[failed] PubKey class : Checking curve

[34m[1m>>> [0mz.pubkey.curve.name == "secp256k1"
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PubKeyECDSA' object has no attribute 'pubkey'


###(010)=[failed] PubKey class : Checking point value

[34m[1m>>> [0mz.pubkey.public_numbers().x == 104748656174769496952370005421566518252704263000192720134585149244759951661467
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PubKeyECDSA' object has no attribute 'pubkey'


###(011)=[failed] PubKeyRSA class : Generate without modulus

[34m[1m>>> [0mt = PubKeyRSA()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 198, in __call__
    obj.fill_and_store()
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


######
## PrivKey class tests
######


###(012)=[failed] PrivKey class : Importing PEM-encoded RSA private key

[34m[1m>>> [0mx = PrivKey("""
... -----BEGIN RSA PRIVATE KEY-----
... MIIEowIBAAKCAQEAmFdqP+nTEZukS0lLP+yj1gNImsEIf7P2ySTunceYxwkm4VE5
... QReDbb2L5/HLA9pPmIeQLSq/BgO1meOcbOSJ2YVHQ28MQ56+8Crb6n28iycX4hp0
... H3AxRAjh0edX+q3yilvYJ4W9/NnIb/wAZwS0oJif/tTkVF77HybAfJde5Eqbp+bC
... KIvMWnambh9DRUyjrBBZo5dA1o32zpuFBrJdI8dmUpw9gtf0F0Ba8lGZm8Uqc0Gy
... XeXOJUE2u7CiMu3M77BM6ZLLTcow5+bQImkmTL1SGhzwfinME1e6p3Hm//pDjuJv
... FaY22k05LgLuyqc59vFiB3Toldz8+AbMNjvzAwIDAQABAoIBAH3KeJZL2hhI/1GX
... NMaU/PfDgFkgmYbxMA8JKusnm/SFjxAwBGnGI6UjBXpBgpQs2Nqm3ZseF9u8hmCK
... vGiCEX2GesCo2mSfmSQxD6RBrMTuQ99UXpxzBIscFnM/Zrs8lPBARGzmF2nI3qPx
... Xtex4ABX5o0Cd4NfZlZjpj96skUoO8+bd3I4OPUFYFFFuv81LoSQ6Hew0a8xtJXt
... KkDp9h1jTGGUOc189WACNoBLH0MGeVoSUfc1++RcC3cypUZ8fNP1OO6GBfv06f5o
... XES4ZbxGYpa+nCfNwb6V2gWbkvaYm7aFn0KWGNZXS1P3OcWv6IWdOmg2CI7MMBLJ
... 0LyWVCECgYEAyMJYw195mvHl8VyxJ3HkxeQaaozWL4qhNQ0Kaw+mzD+jYdkbHb3a
... BYghsgEDZjnyOVblC7I+4smvAZJLWJaf6sZ5HAw3zmj1ibCkXx7deoRc/QVcOikl
... 3dE/ymO0KGJNiGzJZmxbRS3hTokmVPuxSWW4p5oSiMupFHKa18Uv8DECgYEAwkJ7
... iTOUL6b4e3lQuHQnJbsiQpd+P/bsIPP7kaaHObewfHpfOOtIdtN4asxVFf/PgW5u
... WmBllqAHZYR14DEYIdL+hdLrdvk5nYQ3YfhOnp+haHUPCdEiXrRZuGXjmMA4V0hL
... 3HPF5ZM8H80fLnN8Pgn2rIC7CZQ46y4PnoV1nXMCgYBBwCUCF8rkDEWa/ximKo8a
... oNJmAypC98xEa7j1x3KBgnYoHcrbusok9ajTe7F5UZEbZnItmnsuG4/Nm/RBV1OY
... uNgBb573YzjHl6q93IX9EkzCMXc7NS7JrzaNOopOj6OFAtwTR3m89oHMDu8W9jfi
... KgaIHdXkJ4+AuugrstE4gQKBgFK0d1/8g7SeA+Cdz84YNaqMt5NeaDPXbsTA23Qx
... UBU0rYDxoKTdFybv9a6SfA83sCLM31K/A8FTNJL2CDGA9WNBL3fOSs2GYg88AVBG
... pUJHeDK+0748OcPUSPaG+pVIETSn5RRgffq16r0nWYUvSdAn8cuTqw3y+yC1pZS6
... AU8dAoGBAL5QCi0dTWKN3kf3cXaCAnYiWe4Qg2S+SgLE+F1U4Xws2rqAuSvIiuT5
... i5+Mqk9ZCGdoReVbAovJFoRqe7Fj9yWM+b1awGjL0bOTtnqx0iljob6uFyhpl1xg
... W3a3ICJ/ZYLvkgb4IBEteOwWpp37fX57vzhW8EmUV2UX7ve1uNRI
... -----END RSA PRIVATE KEY-----
... """)
[34m[1m>>> [0mx_privNum = x.key.private_numbers()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'key'


###(013)=[failed] PrivKey class : Checking public attributes

[34m[1m>>> [0massert(x_pubNum.n == 19231328316532061413420367242571475005688288081144416166988378525696075445024135424022026378563116068168327239354659928492979285632474448448624869172454076124150405352043642781483254546569202103296262513098482624188672299255268092629150366527784294463900039290024710152521604731213565912934889752122898104556895316819303096201441834849255370122572613047779766933573375974464479123135292080801384304131606933504677232323037116557327478512106367095125103346134248056463878553619525193565824925835325216545121044922690971718737998420984924512388011040969150550056783451476150234324593710633552558175109683813482739004163)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'x_pubNum' is not defined


###(014)=[failed] PrivKey class : Checking private attributes

[34m[1m>>> [0massert(x_privNum.p == 140977881300857803928857666115326329496639762170623218602431133528876162476487960230341078724702018316260690172014674492782486113504117653531825010840338251572887403113276393351318549036549656895326851872473595350667293402676143426484331639796163189182788306480699144107905869179435145810212051656274284113969)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'x_privNum' is not defined


###(018)=[failed] PrivKey class : Importing DER-encoded RSA private key

[34m[1m>>> [0ma = PrivKeyRSA(b'0\x82\x04\xa3\x02\x01\x00\x02\x82\x01\x01\x00\x98Wj?\xe9\xd3\x11\x9b\xa4KIK?\xec\xa3\xd6\x03H\x9a\xc1\x08\x7f\xb3\xf6\xc9$\xee\x9d\xc7\x98\xc7\t&\xe1Q9A\x17\x83m\xbd\x8b\xe7\xf1\xcb\x03\xdaO\x98\x87\x90-*\xbf\x06\x03\xb5\x99\xe3\x9cl\xe4\x89\xd9\x85GCo\x0cC\x9e\xbe\xf0*\xdb\xea}\xbc\x8b\'\x17\xe2\x1at\x1fp1D\x08\xe1\xd1\xe7W\xfa\xad\xf2\x8a[\xd8\'\x85\xbd\xfc\xd9\xc8o\xfc\x00g\x04\xb4\xa0\x98\x9f\xfe\xd4\xe4T^\xfb\x1f&\xc0|\x97^\xe4J\x9b\xa7\xe6\xc2(\x8b\xccZv\xa6n\x1fCEL\xa3\xac\x10Y\xa3\x97@\xd6\x8d\xf6\xce\x9b\x85\x06\xb2]#\xc7fR\x9c=\x82\xd7\xf4\x17@Z\xf2Q\x99\x9b\xc5*sA\xb2]\xe5\xce%A6\xbb\xb0\xa22\xed\xcc\xef\xb0L\xe9\x92\xcbM\xca0\xe7\xe6\xd0"i&L\xbdR\x1a\x1c\xf0~)\xcc\x13W\xba\xa7q\xe6\xff\xfaC\x8e\xe2o\x15\xa66\xdaM9.\x02\xee\xca\xa79\xf6\xf1b\x07t\xe8\x95\xdc\xfc\xf8\x06\xcc6;\xf3\x03\x02\x03\x01\x00\x01\x02\x82\x01\x00}\xcax\x96K\xda\x18H\xffQ\x974\xc6\x94\xfc\xf7\xc3\x80Y \x99\x86\xf10\x0f\t*\xeb\'\x9b\xf4\x85\x8f\x100\x04i\xc6#\xa5#\x05zA\x82\x94,\xd8\xda\xa6\xdd\x9b\x1e\x17\xdb\xbc\x86`\x8a\xbch\x82\x11}\x86z\xc0\xa8\xdad\x9f\x99$1\x0f\xa4A\xac\xc4\xeeC\xdfT^\x9cs\x04\x8b\x1c\x16s?f\xbb<\x94\xf0@Dl\xe6\x17i\xc8\xde\xa3\xf1^\xd7\xb1\xe0\x00W\xe6\x8d\x02w\x83_fVc\xa6?z\xb2E(;\xcf\x9bwr88\xf5\x05`QE\xba\xff5.\x84\x90\xe8w\xb0\xd1\xaf1\xb4\x95\xed*@\xe9\xf6\x1dcLa\x949\xcd|\xf5`\x026\x80K\x1fC\x06yZ\x12Q\xf75\xfb\xe4\\\x0bw2\xa5F||\xd3\xf58\xee\x86\x05\xfb\xf4\xe9\xfeh\\D\xb8e\xbcFb\x96\xbe\x9c\'\xcd\xc1\xbe\x95\xda\x05\x9b\x92\xf6\x98\x9b\xb6\x85\x9fB\x96\x18\xd6WKS\xf79\xc5\xaf\xe8\x85\x9d:h6\x08\x8e\xcc0\x12\xc9\xd0\xbc\x96T!\x02\x81\x81\x00\xc8\xc2X\xc3_y\x9a\xf1\xe5\xf1\\\xb1\'q\xe4\xc5\xe4\x1aj\x8c\xd6/\x8a\xa15\r\nk\x0f\xa6\xcc?\xa3a\xd9\x1b\x1d\xbd\xda\x05\x88!\xb2\x01\x03f9\xf29V\xe5\x0b\xb2>\xe2\xc9\xaf\x01\x92KX\x96\x9f\xea\xc6y\x1c\x0c7\xceh\xf5\x89\xb0\xa4_\x1e\xddz\x84\\\xfd\x05\\:)%\xdd\xd1?\xcac\xb4(bM\x88l\xc9fl[E-\xe1N\x89&T\xfb\xb1Ie\xb8\xa7\x9a\x12\x88\xcb\xa9\x14r\x9a\xd7\xc5/\xf01\x02\x81\x81\x00\xc2B{\x893\x94/\xa6\xf8{yP\xb8t\'%\xbb"B\x97~?\xf6\xec \xf3\xfb\x91\xa6\x879\xb7\xb0|z_8\xebHv\xd3xj\xccU\x15\xff\xcf\x81nnZ`e\x96\xa0\x07e\x84u\xe01\x18!\xd2\xfe\x85\xd2\xebv\xf99\x9d\x847a\xf8N\x9e\x9f\xa1hu\x0f\t\xd1"^\xb4Y\xb8e\xe3\x98\xc08WHK\xdcs\xc5\xe5\x93<\x1f\xcd\x1f.s|>\t\xf6\xac\x80\xbb\t\x948\xeb.\x0f\x9e\x85u\x9ds\x02\x81\x80A\xc0%\x02\x17\xca\xe4\x0cE\x9a\xff\x18\xa6*\x8f\x1a\xa0\xd2f\x03*B\xf7\xccDk\xb8\xf5\xc7r\x81\x82v(\x1d\xca\xdb\xba\xca$\xf5\xa8\xd3{\xb1yQ\x91\x1bfr-\x9a{.\x1b\x8f\xcd\x9b\xf4AWS\x98\xb8\xd8\x01o\x9e\xf7c8\xc7\x97\xaa\xbd\xdc\x85\xfd\x12L\xc21w;5.\xc9\xaf6\x8d:\x8aN\x8f\xa3\x85\x02\xdc\x13Gy\xbc\xf6\x81\xcc\x0e\xef\x16\xf67\xe2*\x06\x88\x1d\xd5\xe4\'\x8f\x80\xba\xe8+\xb2\xd18\x81\x02\x81\x80R\xb4w_\xfc\x83\xb4\x9e\x03\xe0\x9d\xcf\xce\x185\xaa\x8c\xb7\x93^h3\xd7n\xc4\xc0\xdbt1P\x154\xad\x80\xf1\xa0\xa4\xdd\x17&\xef\xf5\xae\x92|\x0f7\xb0"\xcc\xdfR\xbf\x03\xc1S4\x92\xf6\x081\x80\xf5cA/w\xceJ\xcd\x86b\x0f<\x01PF\xa5BGx2\xbe\xd3\xbe<9\xc3\xd4H\xf6\x86\xfa\x95H\x114\xa7\xe5\x14`}\xfa\xb5\xea\xbd\'Y\x85/I\xd0\'\xf1\xcb\x93\xab\r\xf2\xfb \xb5\xa5\x94\xba\x01O\x1d\x02\x81\x81\x00\xbeP\n-\x1dMb\x8d\xdeG\xf7qv\x82\x02v"Y\xee\x10\x83d\xbeJ\x02\xc4\xf8]T\xe1|,\xda\xba\x80\xb9+\xc8\x8a\xe4\xf9\x8b\x9f\x8c\xaaOY\x08ghE\xe5[\x02\x8b\xc9\x16\x84j{\xb1c\xf7%\x8c\xf9\xbdZ\xc0h\xcb\xd1\xb3\x93\xb6z\xb1\xd2)c\xa1\xbe\xae\x17(i\x97\\`[v\xb7 "\x7fe\x82\xef\x92\x06\xf8 \x11-x\xec\x16\xa6\x9d\xfb}~{\xbf8V\xf0I\x94We\x17\xee\xf7\xb5\xb8\xd4H')
[34m[1m>>> [0ma_privNum = a.key.private_numbers()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'key'


###(019)=[failed] PrivKey class : Checking public attributes

[34m[1m>>> [0massert(y.key.curve.name == "secp256k1")
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyECDSA' object has no attribute 'key'


###(020)=[failed] PrivKey class : Checking private attributes

[34m[1m>>> [0my.key.private_numbers().private_value == 90719786431263082134670936670180839782031078050773732489701961692235185651857
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyECDSA' object has no attribute 'key'


######
## PrivKey/Pubkey test signatures
######


###(021)=[failed] PrivKey class : sign tbs cert

[34m[1m>>> [0mpkey_sign = PrivKey("""
... -----BEGIN RSA PRIVATE KEY-----
... MIIEowIBAAKCAQEA1L8KacejlbFJ18bvAz5/W9mF+0GglJs6qyv8pAPPiX1mWaLZ
... Y42Kf/axHYrxUPXEqitRG3VkOy1HONAZhl90rY0jVUyYps94om4S98NECbY3eiVc
... 02ZqQng5HyzBYJQeTh+EYrDaxPUXcVXjthmrt/6vbUHI1Kgk/gok8IBFMSzilxeO
... ZMJJ+dQigeDiaJGwHb3U5KzOm+hFb/IbwjdXJm3CG/58bCQp0rp6RD2qI/D6Xtvj
... pc/ms6q7vfBVpquSLeEIt4Jq2XC9RKGR7TGHaVe8vmU5rb/Y36ReYCw5+fMJqcP4
... fFlC6iexBDhgy1sqV0o0tu4TzJodn8n3SFResQIDAQABAoIBAHcXEe8w0AOloJ5n
... P7hjLcvusi96BzfoxSi4kM4HTA+84KRgoqw1uUf0giT1eCxHx3Uylk52okr2B55n
... 70HnAVt9XEANho4qKW9Tis6iwd1l4RxA+ftkoyrePauT1BQKFgTJY8QTGAOU5zCM
... UdHIAPYYXX8dihxwm3SRnSf7xb/GSRkj5sMr0ioiBOZ91fwzbtOEbVXE58DyPNJm
... w/tBCFbibpr4iCU/6US8OyCxR/X4heRyKCcANXlHyE/eUO6TY8J2RaKbSQi+c3/y
... Y11ypSboyM3cGJ/URS5wRd0oQMQMANck4w+MlNU5jxsfN9wF32HWII8wq/6n3hHR
... M+H+3YECgYEA79nc8BLzFPrzuJud9JvCFEh0pNb0gLRb/MvIsaVUT7ac8/89tfvQ
... 6qxWgP81ldJ7S+d/uh80CKg0lVwaxF4sQ6yNn/cvebW8tCCm0RkD8q3R9kxOd3Q/
... kLNeeBS/gPzh2xOmVuTE0ruv7ovYowU8WfJG2z20lv7WNsrN/Jm526kCgYEA4xH+
... EBVqoPYxzKoa0LNxSPfVOBO7wT19pS5Ny7yjI9oy724cNXn39H5KaCHC3ZnR0mII
... 0znf7cbtbFHLSkR2MNzy1MC1VhIxFQ5yHLRCjZcKkjd+gZuJp0tCgY/r2dNYsBCR
... 7W1vMz/wNsbufkOhi/DqC0Ru7onFbouGBdpID8kCgYEAjamr6NAIarfeA4dGQBdP
... BhPVcRbUyr+8JQ9ntiTkK0C8axCyLi5RMooffYk+6QKseCR/ODr9zK8sf5sq5BiL
... JF1iOL0SeVxx3CH85TtVLZykikh/f+ZVNO38OghnI5Q5AeAVOvVbmuvn+Yj3pzGM
... d8O1PgCwDQ7vDuWxzCQvtiECgYAGWA9YFbEX9CjqBeqf4BOPLVVorqx1NqmW/tcv
... lQKd0s/Pfq0NFW5HB2w+woq2NED3dsO2WwyVkRQ7DYH3fjgrH1EtfoDSecmjQ/cO
... ND8Tw5+I/EHtjxHmeaTPB91YBZ6ZtKzPDFqp/ORSM3agUnVl+oIfdHcA9Rpt/zns
... We/feQKBgGimvdIrurKPTrV49ltAKdkHmglpYeCaDr6aZKwWMcsrLmTZ6a4uRPFF
... TdK+rCyGyjmibTVRjdg5+7KXshSlBleNR3v+AySAxzpjwySVhTfRirCogHRFHrnK
... kXqy5xUkg11ETv6v91n3u5NVBlXVN4iwFRGSKsecw0qxSgKjbP4n
... -----END RSA PRIVATE KEY-----
... """)
[34m[1m>>> [0m
[34m[1m>>> [0mc_tosign = Cert("""
... -----BEGIN CERTIFICATE-----
... MIIC/TCCAeWgAwIBAgIJALkQBZa7rCRFMA0GCSqGSIb3DQEBBQUAMBUxEzARBgNV
... BAMMCnNlY2Rldi5vcmcwHhcNMTgwMjI3MTY1NjIyWhcNMjgwMjI1MTY1NjIyWjAV
... MRMwEQYDVQQDDApzZWNkZXYub3JnMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
... CgKCAQEA1L8KacejlbFJ18bvAz5/W9mF+0GglJs6qyv8pAPPiX1mWaLZY42Kf/ax
... HYrxUPXEqitRG3VkOy1HONAZhl90rY0jVUyYps94om4S98NECbY3eiVc02ZqQng5
... HyzBYJQeTh+EYrDaxPUXcVXjthmrt/6vbUHI1Kgk/gok8IBFMSzilxeOZMJJ+dQi
... geDiaJGwHb3U5KzOm+hFb/IbwjdXJm3CG/58bCQp0rp6RD2qI/D6Xtvjpc/ms6q7
... vfBVpquSLeEIt4Jq2XC9RKGR7TGHaVe8vmU5rb/Y36ReYCw5+fMJqcP4fFlC6iex
... BDhgy1sqV0o0tu4TzJodn8n3SFResQIDAQABo1AwTjAdBgNVHQ4EFgQUf98kGOpM
... CVBFdHxFb8DaL6tPe+8wHwYDVR0jBBgwFoAUf98kGOpMCVBFdHxFb8DaL6tPe+8w
... DAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOCAQEAmw0lTyEVH8YfytbVS9AW
... rTJ1wWhDGf+9jHHEjX/OIq5ii0Ks38WyybhD7cMQNfkZCgIjrutrLHN/m/wn9aDx
... y9vuubWvrcbqhur82YZbVnlvEiqEEyY/ULqCaW2X7UC2K/2NAy14oF6bClLX8LBq
... 3G/lc6GUOToN6i4OuKeB9xxvJaBxsVIdnUW9IqesHatqV4yIhH1/flhqWM47LjHP
... a/uIGboyhl8p5bt3aVbXFwm/NeqsOVPDcQsBdWGldCN6loLE7b4eJDhjHbsuR2C3
... aomWcyGW1mRxNJUI0GQ5EHB5Vvy4mcxKG1DMYxG/rGf/EHk+xPJXpITIugbispbm
... uA==
... -----END CERTIFICATE-----
... """)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xd4\xbf\ni\xc7\xa3\x95\xb1I\xd7\xc6\xef\x03>\x7f[\xd9\x85\xfbA\xa0\x94\x9b:\xab+\xfc\xa4\x03\xcf\x89}fY\xa2\xd9c\x8d\x8a\x7f\xf6\xb1\x1d\x8a\xf1P\xf5\xc4\xaa+Q\x1bud;-G8\xd0\x19\x86_t\xad\x8d#UL\x98\xa6\xcfx\xa2n\x12\xf7\xc3D\t\xb67z%\\\xd3fjBx9\x1f,\xc1`\x94\x1eN\x1f\x84b\xb0\xda\xc4\xf5\x17qU\xe3\xb6\x19\xab\xb7\xfe\xafmA\xc8\xd4\xa8$\xfe\n$\xf0\x80E1,\xe2\x97\x17\x8ed\xc2I\xf9\xd4"\x81\xe0\xe2h\x91\xb0\x1d\xbd\xd4\xe4\xac\xce\x9b\xe8Eo\xf2\x1b\xc27W&m\xc2\x1b\xfe|l$)\xd2\xbazD=\xaa#\xf0\xfa^\xdb\xe3\xa5\xcf\xe6\xb3\xaa\xbb\xbd\xf0U\xa6\xab\x92-\xe1\x08\xb7\x82j\xd9p\xbdD\xa1\x91\xed1\x87iW\xbc\xbee9\xad\xbf\xd8\xdf\xa4^`,9\xf9\xf3\t\xa9\xc3\xf8|YB\xea\'\xb1\x048`\xcb[*WJ4\xb6\xee\x13\xcc\x9a\x1d\x9f\xc9\xf7HT^\xb1\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


######
## PubKey/PrivKey classes crypto tests
######


###(022)=[failed] PrivKey/PubKey classes : Signing/Verifying with MD5_SHA1 hash

[34m[1m>>> [0mm = "Testing our PKCS #1 legacy methods"    # ignore this string
[34m[1m>>> [0ms = x.sign(m, t="pkcs", h="md5-sha1")
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 518, in sign
    return _DecryptAndSignRSA.sign(self, data, t=t, h=h, mgf=mgf, L=L)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


###(023)=[failed] PrivKey/PubKey classes : Signing/Verifying with MD5_SHA1 hash with legacy support

[34m[1m>>> [0mm = "Testing our PKCS #1 legacy methods"
[34m[1m>>> [0ms = x._legacy_sign_md5_sha1(m)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/crypto/pkcs1.py", line 212, in _legacy_sign_md5_sha1
    k = self._modulusLen // 8
AttributeError: 'PrivKeyRSA' object has no attribute '_modulusLen'


######
## Cert class tests
######


###(024)=[failed] Cert class : Importing PEM-encoded X.509 Certificate

[34m[1m>>> [0mx = Cert("""
... -----BEGIN CERTIFICATE-----
... MIIFEjCCA/qgAwIBAgIJALRecEPnCQtxMA0GCSqGSIb3DQEBBQUAMIG2MQswCQYD
... VQQGEwJGUjEOMAwGA1UECBMFUGFyaXMxDjAMBgNVBAcTBVBhcmlzMRcwFQYDVQQK
... Ew5NdXNocm9vbSBDb3JwLjEeMBwGA1UECxMVTXVzaHJvb20gVlBOIFNlcnZpY2Vz
... MSUwIwYDVQQDExxJS0V2MiBYLjUwOSBUZXN0IGNlcnRpZmljYXRlMScwJQYJKoZI
... hvcNAQkBFhhpa2V2Mi10ZXN0QG11c2hyb29tLmNvcnAwHhcNMDYwNzEzMDczODU5
... WhcNMjYwMzMwMDczODU5WjCBtjELMAkGA1UEBhMCRlIxDjAMBgNVBAgTBVBhcmlz
... MQ4wDAYDVQQHEwVQYXJpczEXMBUGA1UEChMOTXVzaHJvb20gQ29ycC4xHjAcBgNV
... BAsTFU11c2hyb29tIFZQTiBTZXJ2aWNlczElMCMGA1UEAxMcSUtFdjIgWC41MDkg
... VGVzdCBjZXJ0aWZpY2F0ZTEnMCUGCSqGSIb3DQEJARYYaWtldjItdGVzdEBtdXNo
... cm9vbS5jb3JwMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmFdqP+nT
... EZukS0lLP+yj1gNImsEIf7P2ySTunceYxwkm4VE5QReDbb2L5/HLA9pPmIeQLSq/
... BgO1meOcbOSJ2YVHQ28MQ56+8Crb6n28iycX4hp0H3AxRAjh0edX+q3yilvYJ4W9
... /NnIb/wAZwS0oJif/tTkVF77HybAfJde5Eqbp+bCKIvMWnambh9DRUyjrBBZo5dA
... 1o32zpuFBrJdI8dmUpw9gtf0F0Ba8lGZm8Uqc0GyXeXOJUE2u7CiMu3M77BM6ZLL
... Tcow5+bQImkmTL1SGhzwfinME1e6p3Hm//pDjuJvFaY22k05LgLuyqc59vFiB3To
... ldz8+AbMNjvzAwIDAQABo4IBHzCCARswHQYDVR0OBBYEFPPYTt6Q9+Zd0s4zzVxW
... jG+XFDFLMIHrBgNVHSMEgeMwgeCAFPPYTt6Q9+Zd0s4zzVxWjG+XFDFLoYG8pIG5
... MIG2MQswCQYDVQQGEwJGUjEOMAwGA1UECBMFUGFyaXMxDjAMBgNVBAcTBVBhcmlz
... MRcwFQYDVQQKEw5NdXNocm9vbSBDb3JwLjEeMBwGA1UECxMVTXVzaHJvb20gVlBO
... IFNlcnZpY2VzMSUwIwYDVQQDExxJS0V2MiBYLjUwOSBUZXN0IGNlcnRpZmljYXRl
... MScwJQYJKoZIhvcNAQkBFhhpa2V2Mi10ZXN0QG11c2hyb29tLmNvcnCCCQC0XnBD
... 5wkLcTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQA2zt0BvXofiVvH
... MWlftZCstQaawej1SmxrAfDB4NUM24NsG+UZI88XA5XM6QolmfyKnNromMLC1+6C
... aFxjq3jC/qdS7ifalFLQVo7ik/te0z6Olo0RkBNgyagWPX2LR5kHe9RvSDuoPIsb
... SHMmJA98AZwatbvEhmzMINJNUoHVzhPeHZnIaBgUBg02XULk/ElidO51Rf3gh8dR
... /kgFQSQT687vs1x9TWD00z0Q2bs2UF3Ob3+NYkEGEo5F9RePQm0mY94CT2xs6WpH
... o060Fo7fVpAFktMWx1vpu+wsEbQAhgGqV0fCR2QwKDIbTrPW/p9HJtJDYVjYdAFx
... r3s7V77y
... -----END CERTIFICATE-----
... """)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\x98Wj?\xe9\xd3\x11\x9b\xa4KIK?\xec\xa3\xd6\x03H\x9a\xc1\x08\x7f\xb3\xf6\xc9$\xee\x9d\xc7\x98\xc7\t&\xe1Q9A\x17\x83m\xbd\x8b\xe7\xf1\xcb\x03\xdaO\x98\x87\x90-*\xbf\x06\x03\xb5\x99\xe3\x9cl\xe4\x89\xd9\x85GCo\x0cC\x9e\xbe\xf0*\xdb\xea}\xbc\x8b\'\x17\xe2\x1at\x1fp1D\x08\xe1\xd1\xe7W\xfa\xad\xf2\x8a[\xd8\'\x85\xbd\xfc\xd9\xc8o\xfc\x00g\x04\xb4\xa0\x98\x9f\xfe\xd4\xe4T^\xfb\x1f&\xc0|\x97^\xe4J\x9b\xa7\xe6\xc2(\x8b\xccZv\xa6n\x1fCEL\xa3\xac\x10Y\xa3\x97@\xd6\x8d\xf6\xce\x9b\x85\x06\xb2]#\xc7fR\x9c=\x82\xd7\xf4\x17@Z\xf2Q\x99\x9b\xc5*sA\xb2]\xe5\xce%A6\xbb\xb0\xa22\xed\xcc\xef\xb0L\xe9\x92\xcbM\xca0\xe7\xe6\xd0"i&L\xbdR\x1a\x1c\xf0~)\xcc\x13W\xba\xa7q\xe6\xff\xfaC\x8e\xe2o\x15\xa66\xdaM9.\x02\xee\xca\xa79\xf6\xf1b\x07t\xe8\x95\xdc\xfc\xf8\x06\xcc6;\xf3\x03\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(025)=[failed] Cert class : Checking version

[34m[1m>>> [0mx.version == 3
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'version'


###(026)=[failed] Cert class : Checking certificate serial number extraction

[34m[1m>>> [0mx.serial == 0xB45E7043E7090B71
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'serial'


###(027)=[failed] Cert class : Checking signature algorithm

[34m[1m>>> [0mx.sigAlg == 'sha1-with-rsa-signature'
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'sigAlg'


###(028)=[failed] Cert class : Checking issuer extraction in basic format (/C=FR ...)

[34m[1m>>> [0mx.issuer_str == '/C=FR/ST=Paris/L=Paris/O=Mushroom Corp./OU=Mushroom VPN Services/CN=IKEv2 X.509 Test certificate/emailAddress=ikev2-test@mushroom.corp'
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'issuer_str'


###(029)=[failed] Cert class : Checking subject extraction in basic format (/C=FR ...)

[34m[1m>>> [0mx.subject_str == '/C=FR/ST=Paris/L=Paris/O=Mushroom Corp./OU=Mushroom VPN Services/CN=IKEv2 X.509 Test certificate/emailAddress=ikev2-test@mushroom.corp'
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'subject_str'


###(030)=[failed] Cert class : Checking start date extraction in simple and tuple formats

[34m[1m>>> [0massert(x.notBefore_str_simple == '07/13/06')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'notBefore_str_simple'


###(031)=[failed] Cert class : Checking end date extraction in simple and tuple formats

[34m[1m>>> [0massert(x.notAfter_str_simple == '03/30/26')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'notAfter_str_simple'


###(032)=[failed] Cert class : test remainingDays

[34m[1m>>> [0massert abs(x.remainingDays("02/12/11")) > 5000
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'remainingDays'


###(033)=[failed] Cert class : Checking RSA public key

[34m[1m>>> [0massert(type(x.pubKey) is PubKeyRSA)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'pubKey'


###(034)=[failed] Cert class : Checking extensions

[34m[1m>>> [0mx.show()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'show'


###(035)=[failed] Cert class : encrypt

[34m[1m>>> [0massert len(x.encrypt(b"Scapy")) == 256
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


###(036)=[failed] Cert class : export

[34m[1m>>> [0mimport tempfile, os
[34m[1m>>> [0mfilename = tempfile.mktemp()
[34m[1m>>> [0mx.export(filename)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'export'


###(037)=[failed] Cert class : isIssuerCert

[34m[1m>>> [0massert x.isIssuerCert(x)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PrivKeyRSA' object has no attribute 'isIssuerCert'


###(039)=[failed] Cert class : Checking ECDSA public key

[34m[1m>>> [0massert(type(y.pubKey) is PubKeyECDSA)
[34m[1m>>> [0mpubkey = y.pubKey.pubkey
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'PubKeyECDSA' object has no attribute 'pubkey'


######
## CRL class tests
######


###(050)=[failed] Cert/CRL class : Checking isRevoked

[34m[1m>>> [0mcx = X509_Cert()
[34m[1m>>> [0mcx.tbsCertificate.serialNumber.val = 59577943160751197113872490992424857032
[34m[1m>>> [0mcx.tbsCertificate.issuer = x.x509CRL.tbsCertList.issuer
[34m[1m>>> [0mcx = Cert(raw(cx))
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\t\x000\x06\x02\x01\n\x02\x01\x03'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(052)=[failed] Cert class : Checking isIssuerCert()

[34m[1m>>> [0mc0 = Cert("""
... -----BEGIN CERTIFICATE-----
... MIIFVjCCBD6gAwIBAgIJAJmDv7HOC+iUMA0GCSqGSIb3DQEBCwUAMIHGMQswCQYD
... VQQGEwJVUzEQMA4GA1UECBMHQXJpem9uYTETMBEGA1UEBxMKU2NvdHRzZGFsZTEl
... MCMGA1UEChMcU3RhcmZpZWxkIFRlY2hub2xvZ2llcywgSW5jLjEzMDEGA1UECxMq
... aHR0cDovL2NlcnRzLnN0YXJmaWVsZHRlY2guY29tL3JlcG9zaXRvcnkvMTQwMgYD
... VQQDEytTdGFyZmllbGQgU2VjdXJlIENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcy
... MB4XDTE1MTAxMzE2NDIzOFoXDTE2MTEzMDIzMzQxOVowPjEhMB8GA1UECxMYRG9t
... YWluIENvbnRyb2wgVmFsaWRhdGVkMRkwFwYDVQQDDBAqLnRvb2xzLmlldGYub3Jn
... MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAseE36OuC1on62/XCS3fw
... LErecm4+E2DRqGYexK09MmDl8Jm19Hp6SFUh7g45EvnODcr1aWHHBO1uDx07HlCI
... eToOMUEW8bECZGilzfVKCsqZljUIw34nXdCpz/PnKK832LZ73fN+rm6Xf/fKaU7M
... 0AbfXSebOxLn5v4Ia1J7ghF8crNG68HoeLgPy+HrvQZEWNyDULKgYlvcgbg24558
... ebKpU4rgC8lKKhM5MRO9LM+ocM+MjT0Bo4iuEgA2HR4kK9152FMBJu0oT8mGlINO
... yOEULoWzr9Ru3WlGr0ElDnqti/KSynnZezJP93fo+bRPI1zUXAOu2Ks6yhNfXV1d
... oQIDAQABo4IBzDCCAcgwDAYDVR0TAQH/BAIwADAdBgNVHSUEFjAUBggrBgEFBQcD
... AQYIKwYBBQUHAwIwDgYDVR0PAQH/BAQDAgWgMDwGA1UdHwQ1MDMwMaAvoC2GK2h0
... dHA6Ly9jcmwuc3RhcmZpZWxkdGVjaC5jb20vc2ZpZzJzMS0xNy5jcmwwWQYDVR0g
... BFIwUDBOBgtghkgBhv1uAQcXATA/MD0GCCsGAQUFBwIBFjFodHRwOi8vY2VydGlm
... aWNhdGVzLnN0YXJmaWVsZHRlY2guY29tL3JlcG9zaXRvcnkvMIGCBggrBgEFBQcB
... AQR2MHQwKgYIKwYBBQUHMAGGHmh0dHA6Ly9vY3NwLnN0YXJmaWVsZHRlY2guY29t
... LzBGBggrBgEFBQcwAoY6aHR0cDovL2NlcnRpZmljYXRlcy5zdGFyZmllbGR0ZWNo
... LmNvbS9yZXBvc2l0b3J5L3NmaWcyLmNydDAfBgNVHSMEGDAWgBQlRYFoUCY4PTst
... LL7Natm2PbNmYzArBgNVHREEJDAighAqLnRvb2xzLmlldGYub3Jngg50b29scy5p
... ZXRmLm9yZzAdBgNVHQ4EFgQUrYq0HAdR15KJB7C3hGIvNlV6X00wDQYJKoZIhvcN
... AQELBQADggEBAAxfzShHiatHrWnTGuRX9BmFpHOFGmLs3PtRRPoOUEbZrcTbaJ+i
... EZpjj4R3eiLITgObcib8+NR1eZsN6VkswZ+rr54aeQ1WzWlsVwBP1t0h9lIbaonD
... wDV6ME3KzfFwwsZWqMBgLin8TcoMadAkXhdfcEKNndKSMsowgEjigP677l24nHf/
... OcnMftgErmTm+jEdW1wUooJoWgbt8TT2uWD8MC62sIIgSQ6miKtg7LhCC1ScyVuN
... Erk3YzF8mPwouOcnNOKsUnkDXLA2REMedVp48c4ikjLClu6AcIg03ZU+o8fLNqcZ
... zd1s7DbacrRSSQ+nXDTodqw1HB+77u0RFs0=
... -----END CERTIFICATE-----
... """)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xb1\xe17\xe8\xeb\x82\xd6\x89\xfa\xdb\xf5\xc2Kw\xf0,J\xdern>\x13`\xd1\xa8f\x1e\xc4\xad=2`\xe5\xf0\x99\xb5\xf4zzHU!\xee\x0e9\x12\xf9\xce\r\xca\xf5ia\xc7\x04\xedn\x0f\x1d;\x1eP\x88y:\x0e1A\x16\xf1\xb1\x02dh\xa5\xcd\xf5J\n\xca\x99\x965\x08\xc3~']\xd0\xa9\xcf\xf3\xe7(\xaf7\xd8\xb6{\xdd\xf3~\xaen\x97\x7f\xf7\xcaiN\xcc\xd0\x06\xdf]'\x9b;\x12\xe7\xe6\xfe\x08kR{\x82\x11|r\xb3F\xeb\xc1\xe8x\xb8\x0f\xcb\xe1\xeb\xbd\x06DX\xdc\x83P\xb2\xa0b[\xdc\x81\xb86\xe3\x9e|y\xb2\xa9S\x8a\xe0\x0b\xc9J*\x1391\x13\xbd,\xcf\xa8p\xcf\x8c\x8d=\x01\xa3\x88\xae\x12\x006\x1d\x1e$+\xddy\xd8S\x01&\xed(O\xc9\x86\x94\x83N\xc8\xe1\x14.\x85\xb3\xaf\xd4n\xddiF\xafA%\x0ez\xad\x8b\xf2\x92\xcay\xd9{2O\xf7w\xe8\xf9\xb4O#\\\xd4\\\x03\xae\xd8\xab:\xca\x13_]]]\xa1\x02\x03\x01\x00\x01"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(053)=[failed] Cert class : Checking isSelfSigned()

[34m[1m>>> [0mc2.isSelfSigned() and not c1.isSelfSigned() and not c0.isSelfSigned()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c2' is not defined


###(054)=[failed] PubKey class : Checking verifyCert()

[34m[1m>>> [0mc2.pubKey.verifyCert(c2) and c1.pubKey.verifyCert(c0)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c2' is not defined


###(055)=[failed] Chain class : Checking chain construction

[34m[1m>>> [0massert(len(Chain([c0, c1, c2])) == 3)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c0' is not defined


###(056)=[failed] Chain class : repr

[34m[1m>>> [0mexpected_repr = """__ /C=US/ST=Arizona/L=Scottsdale/O=Starfield Technologies, Inc./CN=Starfield Root Certificate Authority - G2 [Self Signed]
...   _ /C=US/ST=Arizona/L=Scottsdale/O=Starfield Technologies, Inc./OU=http://certs.starfieldtech.com/repository//CN=Starfield Secure Certificate Authority - G2
...     _ /OU=Domain Control Validated/CN=*.tools.ietf.org"""
[34m[1m>>> [0massert str(Chain([c0, c1, c2])) == expected_repr
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c0' is not defined


###(057)=[failed] Chain class : Checking chain verification

[34m[1m>>> [0massert(Chain([], c0).verifyChain([c2], [c1]))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c0' is not defined


###(058)=[failed] Chain class: Checking chain verification with file

[34m[1m>>> [0mimport tempfile
[34m[1m>>> [0m
[34m[1m>>> [0mtf_folder = tempfile.mkdtemp()
[34m[1m>>> [0m
[34m[1m>>> [0mtry:
...     os.makedirs(tf_folder)
... except:
...     pass
... 
[34m[1m>>> [0mtf = os.path.join(tf_folder, "trusted")
[34m[1m>>> [0mutf = os.path.join(tf_folder, "untrusted")
[34m[1m>>> [0m
[34m[1m>>> [0mtf
'/tmp/tmpgcr6zw26/trusted'
[34m[1m>>> [0mutf
'/tmp/tmpgcr6zw26/untrusted'
[34m[1m>>> [0m
[34m[1m>>> [0mtrusted = open(tf, "w")
[34m[1m>>> [0mtrusted.write("""
... -----BEGIN CERTIFICATE-----
... MIIFADCCA+igAwIBAgIBBzANBgkqhkiG9w0BAQsFADCBjzELMAkGA1UEBhMCVVMx
... EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxJTAjBgNVBAoT
... HFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xMjAwBgNVBAMTKVN0YXJmaWVs
... ZCBSb290IENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTExMDUwMzA3MDAw
... MFoXDTMxMDUwMzA3MDAwMFowgcYxCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6
... b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMSUwIwYDVQQKExxTdGFyZmllbGQgVGVj
... aG5vbG9naWVzLCBJbmMuMTMwMQYDVQQLEypodHRwOi8vY2VydHMuc3RhcmZpZWxk
... dGVjaC5jb20vcmVwb3NpdG9yeS8xNDAyBgNVBAMTK1N0YXJmaWVsZCBTZWN1cmUg
... Q2VydGlmaWNhdGUgQXV0aG9yaXR5IC0gRzIwggEiMA0GCSqGSIb3DQEBAQUAA4IB
... DwAwggEKAoIBAQDlkGZL7PlGcakgg77pbL9KyUhpgXVObST2yxcT+LBxWYR6ayuF
... pDS1FuXLzOlBcCykLtb6Mn3hqN6UEKwxwcDYav9ZJ6t21vwLdGu4p64/xFT0tDFE
... 3ZNWjKRMXpuJyySDm+JXfbfYEh/JhW300YDxUJuHrtQLEAX7J7oobRfpDtZNuTlV
... Bv8KJAV+L8YdcmzUiymMV33a2etmGtNPp99/UsQwxaXJDgLFU793OGgGJMNmyDd+
... MB5FcSM1/5DYKp2N57CSTTx/KgqT3M0WRmX3YISLdkuRJ3MUkuDq7o8W6o0OPnYX
... v32JgIBEQ+ct4EMJddo26K3biTr1XRKOIwSDAgMBAAGjggEsMIIBKDAPBgNVHRMB
... Af8EBTADAQH/MA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUJUWBaFAmOD07LSy+
... zWrZtj2zZmMwHwYDVR0jBBgwFoAUfAwyH6fZMH/EfWijYqihzqsHWycwOgYIKwYB
... BQUHAQEELjAsMCoGCCsGAQUFBzABhh5odHRwOi8vb2NzcC5zdGFyZmllbGR0ZWNo
... LmNvbS8wOwYDVR0fBDQwMjAwoC6gLIYqaHR0cDovL2NybC5zdGFyZmllbGR0ZWNo
... LmNvbS9zZnJvb3QtZzIuY3JsMEwGA1UdIARFMEMwQQYEVR0gADA5MDcGCCsGAQUF
... BwIBFitodHRwczovL2NlcnRzLnN0YXJmaWVsZHRlY2guY29tL3JlcG9zaXRvcnkv
... MA0GCSqGSIb3DQEBCwUAA4IBAQBWZcr+8z8KqJOLGMfeQ2kTNCC+Tl94qGuc22pN
... QdvBE+zcMQAiXvcAngzgNGU0+bE6TkjIEoGIXFs+CFN69xpk37hQYcxTUUApS8L0
... rjpf5MqtJsxOYUPl/VemN3DOQyuwlMOS6eFfqhBJt2nk4NAfZKQrzR9voPiEJBjO
... eT2pkb9UGBOJmVQRDVXFJgt5T1ocbvlj2xSApAer+rKluYjdkf5lO6Sjeb6JTeHQ
... sPTIFwwKlhR8Cbds4cLYVdQYoKpBaXAko7nv6VrcPuuUSvC33l8Odvr7+2kDRUBQ
... 7nIMpBKGgc0T0U7EPMpODdIm8QC3tKai4W56gf0wrHofx1l7
... -----END CERTIFICATE-----
... """)
1794
[34m[1m>>> [0mtrusted.close()
[34m[1m>>> [0m
[34m[1m>>> [0muntrusted = open(utf, "w")
[34m[1m>>> [0muntrusted.write("""
... -----BEGIN CERTIFICATE-----
... MIID3TCCAsWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBjzELMAkGA1UEBhMCVVMx
... EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxJTAjBgNVBAoT
... HFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xMjAwBgNVBAMTKVN0YXJmaWVs
... ZCBSb290IENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTA5MDkwMTAwMDAw
... MFoXDTM3MTIzMTIzNTk1OVowgY8xCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6
... b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMSUwIwYDVQQKExxTdGFyZmllbGQgVGVj
... aG5vbG9naWVzLCBJbmMuMTIwMAYDVQQDEylTdGFyZmllbGQgUm9vdCBDZXJ0aWZp
... Y2F0ZSBBdXRob3JpdHkgLSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
... ggEBAL3twQP89o/8ArFvW59I2Z154qK3A2FWGMNHttfKPTUuiUP3oWmb3ooa/RMg
... nLRJdzIpVv257IzdIvpy3Cdhl+72WoTsbhm5iSzchFvVdPtrX8WJpRBSiUZV9Lh1
... HOZ/5FSuS/hVclcCGfgXcVnrHigHdMWdSL5stPSksPNkN3mSwOxGXn/hbVNMYq/N
... Hwtjuzqd+/x5AJhhdM8mgkBj87JyahkNmcrUDnXMN/uLicFZ8WJ/X7NfZTD4p7dN
... dloedl40wOiWVpmKs/B/pM293DIxfJHP4F8R+GuqSVzRmZTRouNjWwl2tVZi4Ut0
... HZbUJtQIBFnQmA4O5t78w+wfkPECAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAO
... BgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFHwMMh+n2TB/xH1oo2Kooc6rB1snMA0G
... CSqGSIb3DQEBCwUAA4IBAQARWfolTwNvlJk7mh+ChTnUdgWUXuEok21iXQnCoKjU
... sHU48TRqneSfioYmUeYs0cYtbpUgSpIB7LiKZ3sx4mcujJUDJi5DnUox9g61DLu3
... 4jd/IroAow57UvtruzvE03lRTs2Q9GcHGcg8RnoNAX3FWOdt5oUwF5okxBDgBPfg
... 8n/Uqgr/Qh037ZTlZFkSIHc40zI+OIF1lnP6aI+xy84fxez6nH7PfrHxBy22/L/K
... pL/QlwVKvOoYKAKQvVR4CSFx09F9HdkWsKlhPdAKACL8x3vLCWRFCztAgfd9fDL1
... mMpYjn0q7pBZc2T5NnReJaH1ZgUufzkVqSr7UIuOhWn0
... -----END CERTIFICATE-----
... """)
1400
[34m[1m>>> [0muntrusted.close()
[34m[1m>>> [0m
[34m[1m>>> [0massert Chain([], c0).verifyChainFromCAFile(tf, untrusted_file=utf)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c0' is not defined


###(060)=[failed] Test __repr__

[34m[1m>>> [0mrepr_str = Chain([], c0).__repr__()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'c0' is not defined


###(061)=[failed] Test GeneralizedTime

[34m[1m>>> [0mdata = b"MHAwXAIBADANBgkqhkiG9w0BAQ0FADAAMCIYDzIwMTExMDA2MDgzOTU2WhgPMjA0NjEwMDYwODM5NTZaMAAwHDANBgkqhkiG9w0BAQEFAAMLADAIAgEAAgMBAAGjAjAAMA0GCSqGSIb3DQEBDQUAAwEA"
[34m[1m>>> [0mimport tempfile, os
[34m[1m>>> [0m_, filename = tempfile.mkstemp()
[34m[1m>>> [0mfd = open(filename, "wb")
[34m[1m>>> [0mfd.write(b"-----BEGIN CERTIFICATE-----\n")
28
[34m[1m>>> [0mfd.write(data)
152
[34m[1m>>> [0mfd.write(b"-----END CERTIFICATE-----\n")
26
[34m[1m>>> [0mfd.close()
[34m[1m>>> [0mcert = Cert(filename)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x0b\x000\x08\x02\x01\x00\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


[32m
Regression tests for Scapy regarding fields
[0m━ Run at 12:48:41 from [test/fields.uts] by UTscapy in 0.1497206687927246
[34m[1m └ Passed=128
[0m └ Failed=0

[32m
Import tests
[0m━ Run at 12:48:49 from [test/imports.uts] by UTscapy in [31m7.335312843322754[0m
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Regression tests for Linux only
[0m━ Run at 12:48:49 from [test/linux.uts] by UTscapy in 0.009325742721557617
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Regression tests for Scapy Nmap module
[0m━ Run at 12:48:49 from [test/nmap.uts] by UTscapy in 0.3422544002532959
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Tests for Scapy's p0f module.
[0m━ Run at 12:48:49 from [test/p0f.uts] by UTscapy in 0.2944929599761963
[34m[1m └ Passed=17
[0m └ Failed=0

[32m
Tests for Scapy's p0fv2 module.
[0m━ Run at 12:48:51 from [test/p0fv2.uts] by UTscapy in 1.1240487098693848
[34m[1m └ Passed=12
[0m └ Failed=0

[32m
Pipetool related tests
[0m━ Run at 12:48:54 from [test/pipetool.uts] by UTscapy in 3.0561070442199707
[34m[1m └ Passed=29
[0m └ Failed=0

[32m
Regression tests for Scapy random objects
[0m━ Run at 12:48:54 from [test/random.uts] by UTscapy in 0.0075528621673583984
[34m[1m └ Passed=11
[0m └ Failed=0

[32m
Regression tests for Scapy
[0m━ Run at 12:49:01 from [test/regression.uts] by UTscapy in [31m6.960958242416382[0m
[34m[1m └ Passed=261
[0m[31m[1m └ Failed=7
[0m
######
## Main.py tests
######


###(057)=[failed] Test manuf DB methods

[34m[1m>>> [0massert(conf.manufdb._resolve_MAC("00:00:0F:01:02:03") == "Next:01:02:03")
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


######
## pcap / pcapng format support
######


###(154)=[failed] Check offline sniff() with a filter (by filename)

[34m[1m>>> [0mpktpcap_flt = [(proto, sniff(offline=filename, filter=proto.__name__.lower()))
...                for proto in [ICMP, UDP, TCP]]
Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2258, in tcpdump
    proc = subprocess.Popen(
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tcpdump'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 2, in <listcomp>
  File "/home/scapy/scapy/sendrecv.py", line 1300, in sniff
    sniffer._run(*args, **kwargs)
  File "/home/scapy/scapy/sendrecv.py", line 1109, in _run
    sniff_sockets.update((PcapReader(
  File "/home/scapy/scapy/sendrecv.py", line 1111, in <genexpr>
    tcpdump(fname,
  File "/home/scapy/scapy/utils.py", line 2258, in tcpdump
    proc = subprocess.Popen(
  File "/home/scapy/scapy/utils.py", line 744, in __exit__
    raise exc_type(msg)
FileNotFoundError: Could not execute tcpdump, is it installed?


###(155)=[failed] Check offline sniff() with a filter (by file object)

[34m[1m>>> [0mfdesc = open(filename, "rb")
[34m[1m>>> [0mpktpcap_tcp = sniff(offline=fdesc, filter="tcp")
Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2289, in tcpdump
    proc = subprocess.Popen(
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tcpdump'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/sendrecv.py", line 1300, in sniff
    sniffer._run(*args, **kwargs)
  File "/home/scapy/scapy/sendrecv.py", line 1141, in _run
    tcpdump(offline,
  File "/home/scapy/scapy/utils.py", line 2289, in tcpdump
    proc = subprocess.Popen(
  File "/home/scapy/scapy/utils.py", line 744, in __exit__
    raise exc_type(msg)
FileNotFoundError: Could not execute tcpdump, is it installed?


###(156)=[failed] Check offline sniff() with a PcapNg file and a filter (by file object)

[34m[1m>>> [0mpcapng_data = b'\n\r\r\n`\x00\x00\x00M<+\x1a\x01\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x04\x009\x00TShark (Wireshark) 3.2.3 (Git v3.2.3 packaged as 3.2.3-1)\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00\xe4\x00\x00\x00\xff\xff\x00\x00\x14\x00\x00\x00\x06\x00\x00\x00<\x00\x00\x00\x00\x00\x00\x00\x98\xcd\x05\x00\x19\x83\xf7\x9e\x1c\x00\x00\x00\x1c\x00\x00\x00E\x00\x00\x1c\x00\x01\x00\x00@\x11|\xce\x7f\x00\x00\x01\x7f\x00\x00\x01\x005\x005\x00\x08\x01r<\x00\x00\x00'
[34m[1m>>> [0m
[34m[1m>>> [0mfdesc, filename = tempfile.mkstemp()
[34m[1m>>> [0mos.close(fdesc)
[34m[1m>>> [0mfd = open(filename, "wb")
[34m[1m>>> [0mfd.write(pcapng_data)
176
[34m[1m>>> [0mfd.close()
[34m[1m>>> [0m
[34m[1m>>> [0mpackets = sniff(offline=filename, filter="udp")
/usr/local/lib/python3.9/code.py:140: ResourceWarning: unclosed file <_io.BufferedReader name='/tmp/tmpb1vkox5d'>
  sys.last_traceback = last_tb
ResourceWarning: Enable tracemalloc to get the object allocation traceback
Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2258, in tcpdump
    proc = subprocess.Popen(
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tcpdump'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/sendrecv.py", line 1300, in sniff
    sniffer._run(*args, **kwargs)
  File "/home/scapy/scapy/sendrecv.py", line 1109, in _run
    sniff_sockets.update((PcapReader(
  File "/home/scapy/scapy/sendrecv.py", line 1111, in <genexpr>
    tcpdump(fname,
  File "/home/scapy/scapy/utils.py", line 2258, in tcpdump
    proc = subprocess.Popen(
  File "/home/scapy/scapy/utils.py", line 744, in __exit__
    raise exc_type(msg)
FileNotFoundError: Could not execute tcpdump, is it installed?


###(157)=[failed] Check offline sniff() with Packets and tcpdump

[34m[1m>>> [0ml = sniff(offline=IP()/UDP(sport=(10000, 10001)), filter="udp")
Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2286, in tcpdump
    pktlist.fileno()  # type: ignore
  File "/home/scapy/scapy/supersocket.py", line 197, in fileno
    return self.ins.fileno()
AttributeError: 'IterSocket' object has no attribute 'ins'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2298, in tcpdump
    proc = subprocess.Popen(
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tcpdump'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/sendrecv.py", line 1300, in sniff
    sniffer._run(*args, **kwargs)
  File "/home/scapy/scapy/sendrecv.py", line 1131, in _run
    tcpdump(offline,
  File "/home/scapy/scapy/utils.py", line 2298, in tcpdump
    proc = subprocess.Popen(
  File "/home/scapy/scapy/utils.py", line 744, in __exit__
    raise exc_type(msg)
FileNotFoundError: Could not execute tcpdump, is it installed?


###(169)=[failed] Check tcpdump()
 No very specific tests because we do not want to depend on tcpdump output
 Non existing tcpdump binary

[34m[1m>>> [0mfrom io import BytesIO
[34m[1m>>> [0mpcapfile = BytesIO(b'\xd4\xc3\xb2\xa1\x02\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x01\x00\x00\x000}$]\xff\\\t\x006\x00\x00\x006\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00(\x00\x01\x00\x00@\x06|\xcd\x7f\x00\x00\x01\x7f\x00\x00\x01\x00\x14\x00P\x00\x00\x00\x00\x00\x00\x00\x00P\x02 \x00\x91|\x00\x000}$]\x87i\t\x00*\x00\x00\x00*\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00\x1c\x00\x01\x00\x00@\x11|\xce\x7f\x00\x00\x01\x7f\x00\x00\x01\x005\x005\x00\x08\x01r0}$]\xfbp\t\x00*\x00\x00\x00*\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00\x1c\x00\x01\x00\x00@\x01|\xde\x7f\x00\x00\x01\x7f\x00\x00\x01\x08\x00\xf7\xff\x00\x00\x00\x00')
[34m[1m>>> [0m
[34m[1m>>> [0mdata = tcpdump(pcapfile, dump=True, args=['-nn']).split(b'\n')
Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2286, in tcpdump
    pktlist.fileno()  # type: ignore
io.UnsupportedOperation: fileno

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2298, in tcpdump
    proc = subprocess.Popen(
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tcpdump'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/utils.py", line 2298, in tcpdump
    proc = subprocess.Popen(
  File "/home/scapy/scapy/utils.py", line 744, in __exit__
    raise exc_type(msg)
FileNotFoundError: Could not execute tcpdump, is it installed?


###(172)=[failed] Check sniff() offline with linktype & 802.11 filter

[34m[1m>>> [0mfd = get_temp_file()
[34m[1m>>> [0mwrpcap(fd, [RadioTap()/Dot11()/Dot11ProbeReq(), RadioTap()/Dot11()])
[34m[1m>>> [0mlst = sniff(offline=fd, filter="subtype probe-req")
Traceback (most recent call last):
  File "/home/scapy/scapy/utils.py", line 2258, in tcpdump
    proc = subprocess.Popen(
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'tcpdump'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/sendrecv.py", line 1300, in sniff
    sniffer._run(*args, **kwargs)
  File "/home/scapy/scapy/sendrecv.py", line 1109, in _run
    sniff_sockets.update((PcapReader(
  File "/home/scapy/scapy/sendrecv.py", line 1111, in <genexpr>
    tcpdump(fname,
  File "/home/scapy/scapy/utils.py", line 2258, in tcpdump
    proc = subprocess.Popen(
  File "/home/scapy/scapy/utils.py", line 744, in __exit__
    raise exc_type(msg)
FileNotFoundError: Could not execute tcpdump, is it installed?


[32m
send, sniff, sr* tests for Scapy
[0m━ Run at 12:49:01 from [test/sendsniff.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Tests for TLS module
[0m━ Run at 12:49:01 from [test/sslv2.uts] by UTscapy in 0.0733652114868164
[34m[1m └ Passed=10
[0m[31m[1m └ Failed=17
[0m
######
## Read a vulnerable SSLv2 session
######


###(005)=[failed] Reading SSLv2 session - ServerHello

[34m[1m>>> [0mt = SSLv2(sh, tls_session=t.tls_session.mirror())
[34m[1m>>> [0msh = t.msg[0]
[34m[1m>>> [0massert(isinstance(sh, SSLv2ServerHello))
[34m[1m>>> [0massert(sh.msgtype == 4)
[34m[1m>>> [0massert(sh.sid_hit == 0)
[34m[1m>>> [0massert(sh.certtype == 1)
[34m[1m>>> [0massert(sh.version == 0x0002)
[34m[1m>>> [0massert(sh.certlen == 930)
[34m[1m>>> [0massert(sh.cipherslen == 3)
[34m[1m>>> [0massert(sh.connection_idlen == 16)
[34m[1m>>> [0massert(isinstance(sh.cert, Cert))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(006)=[failed] Reading SSLv2 session - ClientMasterKey with unknown server key

[34m[1m>>> [0mt_enc = SSLv2(mk)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 81, in __init__
    super(SSLv2, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 175, in getfield
    p.post_dissection_tls_session_update(raw_msg)
  File "/home/scapy/scapy/layers/tls/session.py", line 1007, in post_dissection_tls_session_update
    self.tls_session_update(msg_str)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 360, in tls_session_update
    s.pwcs = writeConnState(ciphersuite=cs_cls,
  File "/home/scapy/scapy/layers/tls/session.py", line 336, in __init__
    connState.__init__(self, read_or_write="write", **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 140, in __init__
    self.ciphersuite = ciphersuite(tls_version=tls_version)
  File "/home/scapy/scapy/layers/tls/crypto/suites.py", line 143, in __init__
    self.key_block_len = self._key_block_len_v1_0
AttributeError: 'SSL_CK_RC4_128_EXPORT40_WITH_MD5' object has no attribute '_key_block_len_v1_0'


###(008)=[failed] Reading SSLv2 session - ClientMasterKey with compromised server key

[34m[1m>>> [0mt = SSLv2(mk, tls_session=t.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 81, in __init__
    super(SSLv2, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 44, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 267, in __init__
    super(SSLv2ClientMasterKey, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1000, in dissect
    s = self.pre_dissect(s)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 277, in pre_dissect
    self.tls_session.server_rsa_key.decrypt(encryptedkey)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


###(009)=[failed] Reading SSLv2 session - Checking session secrets

[34m[1m>>> [0ms = t.tls_session
[34m[1m>>> [0massert(s.sslv2_common_cs == [0x020080])
[34m[1m>>> [0massert(s.sslv2_challenge == ch.challenge)
[34m[1m>>> [0massert(not s.pre_master_secret)
[34m[1m>>> [0massert(s.master_secret == b'~\xc2\xf9\x9e\x94i\x02\xfe\xed\xc4\xdc\xe2\xd40\xfc\x04')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(010)=[failed] Reading SSLv2 session - Record with ciphertext

[34m[1m>>> [0mt = SSLv2(sv, tls_session=t.tls_session.mirror())
[34m[1m>>> [0massert(t.len == 33)
[34m[1m>>> [0massert(not t.padlen)
[34m[1m>>> [0massert(t.mac == b'?:\xf3vE\xf3\xe83\x1a\xd0\xab\xba\xb6\x86\xe6\x89')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(011)=[failed] Reading SSLv2 session - ServerVerify

[34m[1m>>> [0msv = t.msg[0]
[34m[1m>>> [0massert(isinstance(sv, SSLv2ServerVerify))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(012)=[failed] Reading SSLv2 session - ClientFinished

[34m[1m>>> [0mt = SSLv2(cf, tls_session=t.tls_session.mirror())
[34m[1m>>> [0mcf = t.msg[0]
[34m[1m>>> [0massert(isinstance(cf, SSLv2ClientFinished))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(013)=[failed] Reading SSLv2 session - RequestCertificate

[34m[1m>>> [0mt = SSLv2(rc, tls_session=t.tls_session.mirror())
[34m[1m>>> [0mrc = t.msg[0]
[34m[1m>>> [0massert(isinstance(rc, SSLv2RequestCertificate))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(014)=[failed] Reading SSLv2 session - ClientCertificate

[34m[1m>>> [0mt = SSLv2(cc, tls_session=t.tls_session.mirror())
[34m[1m>>> [0mcc = t.msg[0]
[34m[1m>>> [0massert(isinstance(cc, SSLv2ClientCertificate))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(015)=[failed] Reading SSLv2 session - ServerFinished

[34m[1m>>> [0mt = SSLv2(sf, tls_session=t.tls_session.mirror())
[34m[1m>>> [0msf = t.msg[0]
[34m[1m>>> [0massert(isinstance(sf, SSLv2ServerFinished))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(016)=[failed] Reading SSLv2 session - Application data

[34m[1m>>> [0mt1 = SSLv2(d1, tls_session=t.tls_session.mirror())
[34m[1m>>> [0mdata1 = t1.msg[0]
[34m[1m>>> [0massert(isinstance(data1, Raw))
[34m[1m>>> [0massert(data1.load == b'These are horrendous parameters for a TLS session.\n')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(017)=[failed] Reading SSLv2 session - Checking final sequence numbers

[34m[1m>>> [0mt2.tls_session.rcs.seq_num == 6 and t2.tls_session.wcs.seq_num == 4
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't2' is not defined


######
## Check TLS-related scapy internals
######


###(018)=[failed] Check TLS-related scapy internals - Checking raw() harmlessness (with RC4)

[34m[1m>>> [0mt1.show()
[0m###[[0m [31m[1mSSLv2[0m [0m]###[0m 
  [34mlen[0m       [0m=[0m [35m67[0m
  [34mpadlen[0m    [0m=[0m [35mNone[0m
  [34mmac[0m       [0m=[0m [35mb''[0m
  \[34mmsg[0m       \
   |[0m###[[0m [31m[1mRaw[0m [0m]###[0m 
   |  [34mload[0m      [0m=[0m [35m'\\x99\\x83z\\xc0\\xdc\\xe7\\xf0I\\x80\\x8c\\x8e\x1c\\xc7bx\\x98ӄ\\xd6\x06\\xc8r\\x9b\x197\\xd2\\xe9\x08\\xc53s\\x88 y\\x8e)\\x9f\\xdcE*e\\xb2r\\xa2$<h\x1c/\\x89\\x9e\\xc0\\xc2D9KWB7\\xddSi\\xb6\\xaeE\x13\\xe2'[0m
  [34mpad[0m       [0m=[0m [35mb''[0m

[34m[1m>>> [0massert(t1.msg[0].load == b'These are horrendous parameters for a TLS session.\n')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(019)=[failed] Check TLS-related scapy internals - Checking show2() harmlessness (with RC4)

[34m[1m>>> [0mt2.show2()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't2' is not defined


###(020)=[failed] Check TLS-related scapy internals - Checking show2() harmlessness (with 3DES)

[34m[1m>>> [0mch = b'\x80.\x01\x00\x02\x00\x15\x00\x00\x00\x10\x07\x00\xc0\x05\x00\x80\x03\x00\x80\x01\x00\x80\x06\x00@\x04\x00\x80\x02\x00\x80!2bc\x97^\xa3\r9\x14*\xe4\xd6\xd4\n\x1e'
[34m[1m>>> [0msh = b'\x83\xd2\x04\x00\x01\x00\x02\x03\xa2\x00\x15\x00\x100\x82\x03\x9e0\x82\x02\x86\xa0\x03\x02\x01\x02\x02\t\x00\xfe\x04W\r\xc7\'\xe9\xf60\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000T1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x160\x14\x06\x03U\x04\x03\x0c\rScapy Test CA0\x1e\x17\r160916102811Z\x17\r260915102811Z0X1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x1a0\x18\x06\x03U\x04\x03\x0c\x11Scapy Test Server0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xcc\xf1\xf1\x9b`-`\xae\xf2\x98\r\')\xd9\xc0\tYL\x0fJ0\xa8R\xdf\xe5\xb1!\x9fO\xc3=V\x93\xdd_\xc6\xf7\xb3\xf6U\x8b\xe7\x92\xe2\xde\xf2\x85I\xb4\xa1,\xf4\xfdv\xa8g\xca\x04 `\x11\x18\xa6\xf2\xa9\xb6\xa6\x1d\xd9\xaa\xe5\xd9\xdb\xaf\xe6\xafUW\x9f\xffR\x89e\xe6\x80b\x80!\x94\xbc\xcf\x81\x1b\xcbg\xc2\x9d\xb5\x05w\x04\xa6\xc7\x88\x18\x80xh\x956\xde\x97\x1b\xb6a\x87B\x1au\x98E\x82\xeb>2\x11\xc8\x9b\x86B9\x8dM\x12\xb7X\x1b\x19\xf3\x9d+\xa1\x98\x82\xca\xd7;$\xfb\t9\xb0\xbc\xc2\x95\xcf\x82)u\x16)?B \x17+M@\x8cVl\xad\xba\x0f4\x85\xb1\x7f@yqx\xb7\xa5\x04\xbb\x94\xf7\xb5A\x95\xee|\xeb\x8d\x0cyhY\xef\xcb\xb3\xfa>x\x1e\xeegLz\xdd\xe0\x99\xef\xda\xe7\xef\xb2\t]\xbe\x80 !\x05\x83,D\xdb]*v)\xa5\xb0#\x88t\x07T"\xd6)z\x92\xf5o-\x9e\xe7\xf8&+\x9cXe\x02\x03\x01\x00\x01\xa3o0m0\t\x06\x03U\x1d\x13\x04\x020\x000\x0b\x06\x03U\x1d\x0f\x04\x04\x03\x02\x05\xe00\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14\xa1+ p\xd2k\x80\xe5e\xbc\xeb\x03\x0f\x88\x9ft\xad\xdd\xf6\x130\x1f\x06\x03U\x1d#\x04\x180\x16\x80\x14fS\x94\xf4\x15\xd1\xbdgh\xb0Q725\xe1\xa4\xaa\xde\x07|0\x13\x06\x03U\x1d%\x04\x0c0\n\x06\x08+\x06\x01\x05\x05\x07\x03\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x01\x00\x81\x88\x92sk\x93\xe7\x95\xd6\xddA\xee\x8e\x1e\xbd\xa3HX\xa7A5?{}\xd07\x98\x0e\xb8,\x94w\xc8Q6@\xadY\t(\xc8V\xd6\xea[\xac\xb4\xd8?h\xb7f\xca\xe1V7\xa9\x00e\xeaQ\xc9\xec\xb2iI]\xf9\xe3\xc0\xedaT\xc9\x12\x9f\xc6\xb0\nsU\xe8U5`\xef\x1c6\xf0\xda\xd1\x90wV\x04\xb8\xab8\xee\xf7\t\xc5\xa5\x98\x90#\xea\x1f\xdb\x15\x7f2(\x81\xab\x9b\x85\x02K\x95\xe77Q{\x1bH.\xfb>R\xa3\r\xb4F\xa9\x92:\x1c\x1f\xd7\n\x1eXJ\xfa.Q\x8f)\xc6\x1e\xb8\x0e1\x0es\xf1\'\x88\x17\xca\xc8i\x0c\xfa\x83\xcd\xb3y\x0e\x14\xb0\xb8\x9b/:-\t\xe3\xfc\x06\xf0:n\xfd6;+\x1a\t*\xe8\xab_\x8c@\xe4\x81\xb2\xbc\xf7\x83g\x11nN\x93\xea"\xaf\xff\xa3\x9awWv\xd0\x0b8\xac\xf8\x8a\x945\x8e\xd7\xd4a\xcc\x01\xff$\xb4\x8fa#\xba\x88\xd7Y\xe4\xe9\xba*N\xb5\x15\x0f\x9c\xd0\xea\x06\x91\xd9\xde\xab\x07\x00\xc0\x05\x00\x80\x03\x00\x80\x01\x00\x80\x06\x00@\x04\x00\x80\x02\x00\x80\x03\xea\xd5\x88T&\xe7\\\xc9wM\x05\x1fo\xbf\xec'
[34m[1m>>> [0mmk = b'\x81\x12\x02\x07\x00\xc0\x00\x00\x01\x00\x00\x08(\xc98#b\xc1\x94\x9e\xf1|\xd3\x98/\x84\xa6\xfb\x1e}b7\xf1\xfa9\xc3\xb4A\xe4\xb7\x97\xcd\x0c\xd4\x81\x82\xee\x8b\x80f]_\xbc\xe5\xeb\xe4}b\x82 \xa1S\xd5\xbe\xb3\xf7\xbb\x1c]zm\xe6\xc5\x95\xe3Y\x9d\x84b\xf2\x89\x08i\xf9"\x8d\xf7\xb9\xe3\xb5\xcb\x90\xc2V\xcel\x14\xb0\xd4-\xb3\xd3\xfe\x83\x8a(\x025\xd0Y\x9b4M\xde\xc6\x99{H\x89u.\xfa\x17\x13|\xd39\xf6sc\xaat\x9fy\xf69s9\xbfM\xdc\xcdT\x8d~U"\xdd\xce\xab\xfa\x0e\xa9\x90$s&\x0c8\xe4\x13b\x15\xc7\xc2\r#\xc96\x04{\x14\xd0\x19\xef\x13ql\x07\xbf\'\xfb\xdc\x14t\xf6I\xe6\x0b\xe7\xf2\xd6e\'%2H\x81\x16\x0bT;0\x95G%E\xc559p\x85S\x07\xbf\x03\xb0^\x06\xf0\xdcL\xd4\xf2\x9b\xf7\xc6T\xdb%MS\x8ch\xb5\x91H\xffF\xf0\xafCw\x1a:7\x1f\xf8\x05\x944\xc1p\xb6\x8e\x12.#,a\xd4s\xc7\x9f\xe5\xbf\xcb\xee\x1aS\xa71\x15\xf5pE'
[34m[1m>>> [0msv = b'\x00(\x07q\x8c\x08\xdb\xa8\xaa\x8d\x87\x0b\xe8\x01^\xed\x87\x8e\xb2\xc0\xa9\x84\x11v)~\xf8\xd9,\xea\xe2\x05\x86\x1d\x01n\xe1\xe6\xccE[\xcej'
[34m[1m>>> [0mt = SSLv2(ch)
[34m[1m>>> [0mt.show2()
[0m###[[0m [31m[1mSSLv2[0m [0m]###[0m 
  [34mlen[0m       [0m=[0m [35m46[0m
  [34mpadlen[0m    [0m=[0m [35mNone[0m
  [34mmac[0m       [0m=[0m [35mb''[0m
  \[34mmsg[0m       \
   |[0m###[[0m [31m[1mSSLv2 Handshake - Client Hello[0m [0m]###[0m 
   |  [34mmsgtype[0m   [0m=[0m [35mclient_hello[0m
   |  [34mversion[0m   [0m=[0m [35mSSLv2[0m
   |  [34mcipherslen[0m[0m=[0m [35m21[0m
   |  [34msidlen[0m    [0m=[0m [35m0[0m
   |  [34mchallengelen[0m[0m=[0m [35m16[0m
   |  [34msid[0m       [0m=[0m [35mb''[0m
   |  [34mciphers[0m   [0m=[0m [35m[SSL_CK_DES_192_EDE3_CBC_WITH_MD5, SSL_CK_IDEA_128_CBC_WITH_MD5, SSL_CK_RC2_128_CBC_WITH_MD5, SSL_CK_RC4_128_WITH_MD5, SSL_CK_DES_64_CBC_WITH_MD5, SSL_CK_RC2_128_CBC_EXPORT40_WITH_MD5, SSL_CK_RC4_128_EXPORT40_WITH_MD5][0m
   |  [34mchallenge[0m [0m=[0m [35m21326263975ea30d39142ae4d6d40a1e[0m
  [34mpad[0m       [0m=[0m [35mb''[0m

[34m[1m>>> [0mchallenge = t.msg[0].challenge
[34m[1m>>> [0mt = SSLv2(sh, tls_session=t.tls_session.mirror())
[34m[1m>>> [0mt.show2()
[0m###[[0m [31m[1mSSLv2[0m [0m]###[0m 
  [34mlen[0m       [0m=[0m [35m978[0m
  [34mpadlen[0m    [0m=[0m [35mNone[0m
  [34mmac[0m       [0m=[0m [35mb''[0m
  \[34mmsg[0m       \
   |[0m###[[0m [31m[1mSSLv2 Handshake - Server Hello[0m [0m]###[0m 
   |  [34mmsgtype[0m   [0m=[0m [35mserver_hello[0m
   |  [34msid_hit[0m   [0m=[0m [35m0[0m
   |  [34mcerttype[0m  [0m=[0m [35mx509_cert[0m
   |  [34mversion[0m   [0m=[0m [35mSSLv2[0m
   |  [34mcertlen[0m   [0m=[0m [35m930[0m
   |  [34mcipherslen[0m[0m=[0m [35m21[0m
   |  [34mconnection_idlen[0m[0m=[0m [35m16[0m
   |  [34mcert[0m      [0m=[0m [35m'0\\x82\x03\\x9e0\\x82\x02\\x86\\xa0\x03\x02\x01\x02\x02\t\x00\\xfe\x04W\r\\xc7\'\\xe9\\xf60\r\x06\t*\\x86H\\x86\\xf7\r\x01\x01\x0b\x05\x000T1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x160\x14\x06\x03U\x04\x03\x0c\rScapy Test CA0\x1e\x17\r160916102811Z\x17\r260915102811Z0X1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x1a0\x18\x06\x03U\x04\x03\x0c\x11Scapy Test Server0\\x82\x01"0\r\x06\t*\\x86H\\x86\\xf7\r\x01\x01\x01\x05\x00\x03\\x82\x01\x0f\x000\\x82\x01\n\x02\\x82\x01\x01\x00\\xcc\\xf1\\xf1\\x9b`-`\\xae\\xf2\\x98\r\')\\xd9\\xc0\tYL\x0fJ0\\xa8R\\xdf\\xe5\\xb1!\\x9fO\\xc3=V\\x93\\xdd_\\xc6\\xf7\\xb3\\xf6U\\x8b\\xe7\\x92\\xe2\\xde\\xf2\\x85I\\xb4\\xa1,\\xf4\\xfdv\\xa8g\\xca\x04 `\x11\x18\\xa6\U000a9da6\x1d٪\\xe5\\xd9ۯ\\xe6\\xafUW\\x9f\\xffR\\x89e\\xe6\\x80b\\x80!\\x94\\xbcρ\x1b\\xcbg\x9d\\xb5\x05w\x04\\xa6ǈ\x18\\x80xh\\x956ޗ\x1b\\xb6a\\x87B\x1au\\x98E\\x82\\xeb>2\x11ț\\x86B9\\x8dM\x12\\xb7X\x1b\x19\\xf3\\x9d+\\xa1\\x98\\x82\\xca\\xd7;$\\xfb\t9\\xb0\\xbc\x95ς)u\x16)?B \x17+M@\\x8cVl\\xad\\xba\x0f4\\x85\\xb1\x7f@yqx\\xb7\\xa5\x04\\xbb\\x94\\xf7\\xb5A\\x95\\xee|\\xeb\\x8d\x0cyhY\\xef˳\\xfa>x\x1e\\xeegLz\\xdd\\xe0\\x99\\xef\\xda\\xe7\\xef\\xb2\t]\\xbe\\x80 !\x05\\x83,D\\xdb]*v)\\xa5\\xb0#\\x88t\x07T"\\xd6)z\\x92\\xf5o-\\x9e\\xe7\\xf8&+\\x9cXe\x02\x03\x01\x00\x01\\xa3o0m0\t\x06\x03U\x1d\x13\x04\x020\x000\x0b\x06\x03U\x1d\x0f\x04\x04\x03\x02\x05\\xe00\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14\\xa1+ p\\xd2k\\x80\\xe5e\\xbc\\xeb\x03\x0f\\x88\\x9ft\\xad\\xdd\\xf6\x130\x1f\x06\x03U\x1d#\x04\x180\x16\\x80\x14fS\\x94\\xf4\x15ѽgh\\xb0Q725ᤪ\\xde\x07|0\x13\x06\x03U\x1d%\x04\x0c0\n\x06\x08+\x06\x01\x05\x05\x07\x03\x010\r\x06\t*\\x86H\\x86\\xf7\r\x01\x01\x0b\x05\x00\x03\\x82\x01\x01\x00\\x81\\x88\\x92sk\\x93\\xe7\\x95\\xd6\\xddA\\xee\\x8e\x1e\\xbd\\xa3HX\\xa7A5?{}\\xd07\\x98\x0e\\xb8,\\x94w\\xc8Q6@\\xadY\t(\\xc8V\\xd6\\xea[\\xac\\xb4\\xd8?h\\xb7f\\xca\\xe1V7\\xa9\x00e\\xeaQ\\xc9\\xec\\xb2iI]\\xf9\\xe3\\xc0\\xedaT\\xc9\x12\\x9fư\nsU\\xe8U5`\\xef\x1c6\\xf0\\xdaѐwV\x04\\xb8\\xab8\\xee\\xf7\tť\\x98\\x90#\\xea\x1f\\xdb\x15\x7f2(\\x81\\xab\\x9b\\x85\x02K\\x95\\xe77Q{\x1bH.\\xfb>R\\xa3\r\\xb4F\\xa9\\x92:\x1c\x1f\\xd7\n\x1eXJ\\xfa.Q\\x8f)\\xc6\x1e\\xb8\x0e1\x0es\\xf1\'\\x88\x17\\xca\\xc8i\x0c\\xfa\\x83ͳy\x0e\x14\\xb0\\xb8\\x9b/:-\t\\xe3\\xfc\x06\\xf0:n\\xfd6;+\x1a\t*\\xe8\\xab_\\x8c@䁲\\xbc\\xf7\\x83g\x11nN\\x93\\xea"\\xaf\\xff\\xa3\\x9awWv\\xd0\x0b8\\xac\\xf8\\x8a\\x945\\x8e\\xd7\\xd4a\\xcc\x01\\xff$\\xb4\\x8fa#\\xba\\x88\\xd7Y\\xe4\\xe9\\xba*N\\xb5\x15\x0f\\x9c\\xd0\\xea\x06\\x91\\xd9ޫ'[0m
   |  [34mciphers[0m   [0m=[0m [35m[SSL_CK_DES_192_EDE3_CBC_WITH_MD5, SSL_CK_IDEA_128_CBC_WITH_MD5, SSL_CK_RC2_128_CBC_WITH_MD5, SSL_CK_RC4_128_WITH_MD5, SSL_CK_DES_64_CBC_WITH_MD5, SSL_CK_RC2_128_CBC_EXPORT40_WITH_MD5, SSL_CK_RC4_128_EXPORT40_WITH_MD5][0m
   |  [34mconnection_id[0m[0m=[0m [35m03ead5885426e75cc9774d051f6fbfec[0m
  [34mpad[0m       [0m=[0m [35mb''[0m

[34m[1m>>> [0mt.tls_session.server_rsa_key = rsa_key
[34m[1m>>> [0mt = SSLv2(mk, tls_session=t.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 81, in __init__
    super(SSLv2, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 44, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 267, in __init__
    super(SSLv2ClientMasterKey, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1000, in dissect
    s = self.pre_dissect(s)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 277, in pre_dissect
    self.tls_session.server_rsa_key.decrypt(encryptedkey)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


######
## Build SSLv2 packets
######


###(023)=[failed] Building SSLv2 packets - Various default messages

[34m[1m>>> [0mraw(SSLv2())
b'\x80\x00'
[34m[1m>>> [0mraw(SSLv2Error())
b'\x00\x00\x00'
[34m[1m>>> [0mraw(SSLv2ClientHello())
b'\x01\x00\x02\x00\x03\x00\x00\x00\x00\x07\x00\xc0'
[34m[1m>>> [0mraw(SSLv2ServerHello())
b'\x04\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00'
[34m[1m>>> [0mraw(SSLv2ClientMasterKey())
No known common cipher suite between SSLv2 Hellos.
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/compat.py", line 291, in raw
    return bytes(x)
  File "/home/scapy/scapy/layers/tls/session.py", line 1047, in __bytes__
    built_packet = super(_GenericTLSSessionInheritance, self).__bytes__()
  File "/home/scapy/scapy/packet.py", line 562, in __bytes__
    return self.build()
  File "/home/scapy/scapy/packet.py", line 703, in build
    p = self.do_build()
  File "/home/scapy/scapy/packet.py", line 688, in do_build
    return self.post_build(pkt, pay)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 323, in post_build
    if self.keyarg == b"" and cs_cls.cipher_alg.type == "block":
AttributeError: type object 'SSL_CK_DES_192_EDE3_CBC_WITH_MD5' has no attribute 'cipher_alg'


###(026)=[failed] Building SSLv2 packets - ClientMasterKey context linking

[34m[1m>>> [0mmk = SSLv2ClientMasterKey(cipher='SSL_CK_DES_192_EDE3_CBC_WITH_MD5', clearkey=b'\xff'*19, encryptedkey=b'\0'*256, decryptedkey=b'\xaa'*5, keyarg=b'\x01'*8)
[34m[1m>>> [0mt = SSLv2(msg=mk)
[34m[1m>>> [0mt.tls_session.sslv2_connection_id = b'\xba'*16
[34m[1m>>> [0mt.tls_session.sslv2_challenge = b'\x42'*16
[34m[1m>>> [0mt.raw_stateful()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/tls/session.py", line 1020, in raw_stateful
    return super(_GenericTLSSessionInheritance, self).__bytes__()
  File "/home/scapy/scapy/packet.py", line 562, in __bytes__
    return self.build()
  File "/home/scapy/scapy/packet.py", line 703, in build
    p = self.do_build()
  File "/home/scapy/scapy/packet.py", line 683, in do_build
    pkt = self.self_build()
  File "/home/scapy/scapy/packet.py", line 662, in self_build
    raise ex
  File "/home/scapy/scapy/packet.py", line 653, in self_build
    p = f.addfield(self, p, val)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 62, in addfield
    res += self.i2m(pkt, p)
  File "/home/scapy/scapy/layers/tls/record_sslv2.py", line 52, in i2m
    p.post_build_tls_session_update(cur)
  File "/home/scapy/scapy/layers/tls/session.py", line 1004, in post_build_tls_session_update
    self.tls_session_update(msg_str)
  File "/home/scapy/scapy/layers/tls/handshake_sslv2.py", line 360, in tls_session_update
    s.pwcs = writeConnState(ciphersuite=cs_cls,
  File "/home/scapy/scapy/layers/tls/session.py", line 336, in __init__
    connState.__init__(self, read_or_write="write", **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 140, in __init__
    self.ciphersuite = ciphersuite(tls_version=tls_version)
  File "/home/scapy/scapy/layers/tls/crypto/suites.py", line 143, in __init__
    self.key_block_len = self._key_block_len_v1_0
AttributeError: While disescting field 'msg': 'SSL_CK_DES_192_EDE3_CBC_WITH_MD5' object has no attribute '_key_block_len_v1_0'


[32m
Regression tests for TFTP
[0m━ Run at 12:49:01 from [test/tftp.uts] by UTscapy in 0.034234046936035156
[34m[1m └ Passed=9
[0m └ Failed=0

[32m
Tests for TLS module
[0m━ Run at 12:49:01 from [test/tls.uts] by UTscapy in 0.5955080986022949
[34m[1m └ Passed=41
[0m[31m[1m └ Failed=38
[0m
######
## Test RC4
######


###(014)=[failed] Crypto - RC4 stream cipher, encryption/decryption checks from RFC 6229

[34m[1m>>> [0mclass _rc4_40_test:
...     k= b"\x01\x02\x03\x04\x05"
...     s=(b"\xb2\x39\x63\x05\xf0\x3d\xc0\x27\xcc\xc3\x52\x4a\x0a\x11\x18\xa8" +
...        b"\x69\x82\x94\x4f\x18\xfc\x82\xd5\x89\xc4\x03\xa4\x7a\x0d\x09\x19")
...     s_1024= b"\x30\xab\xbc\xc7\xc2\x0b\x01\x60\x9f\x23\xee\x2d\x5f\x6b\xb7\xdf"
... 
[34m[1m>>> [0mclass _rc4_128_test:
...     k= b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
...     s=(b"\x9a\xc7\xcc\x9a\x60\x9d\x1e\xf7\xb2\x93\x28\x99\xcd\xe4\x1b\x97"
...        b"\x52\x48\xc4\x95\x90\x14\x12\x6a\x6e\x8a\x84\xf1\x1d\x1a\x9e\x1c")
...     s_1024=b"\xbd\xf0\x32\x4e\x60\x83\xdc\xc6\xd3\xce\xdd\x3c\xa8\xc5\x3c\x16"
... 
[34m[1m>>> [0mdef _all_rc4_tests():
...     from scapy.layers.tls.crypto.cipher_stream import (Cipher_RC4_40,
...                                                        Cipher_RC4_128)
...     res = True
...     t = _rc4_40_test
...     c = Cipher_RC4_40(t.k).encrypt(b"\x00"*(1024+16))
...     res = res and (c[:32] == t.s) and (c[-16:] == t.s_1024)
...     res = res and Cipher_RC4_40(t.k).decrypt(t.s) == b"\x00"*32
...     t = _rc4_128_test
...     c = Cipher_RC4_128(t.k).encrypt(b"\x00"*(1024+16))
...     res = res and (c[:32] == t.s) and (c[-16:] == t.s_1024)
...     res = res and Cipher_RC4_128(t.k).decrypt(t.s) == b"\x00"*32
...     return res
... 
[34m[1m>>> [0m_all_rc4_tests()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 3, in _all_rc4_tests
ImportError: cannot import name 'Cipher_RC4_40' from 'scapy.layers.tls.crypto.cipher_stream' (/home/scapy/scapy/layers/tls/crypto/cipher_stream.py)


###(016)=[failed] Crypto - DES cipher in CBC mode, check from FIPS PUB 81

[34m[1m>>> [0mclass _descbc_test:
...     k= binascii.unhexlify("0123456789abcdef")
...     p= binascii.unhexlify("4e6f77206973207468652074696d6520666f7220616c6c20")
...     c= binascii.unhexlify("e5c7cdde872bf27c43e934008c389c0f683788499a7c05f6")
...     iv=binascii.unhexlify("1234567890abcdef")
... 
[34m[1m>>> [0mdef _all_aes_cbc_tests():
...     from scapy.layers.tls.crypto.cipher_block import Cipher_DES_CBC
...     res = True
...     t = _descbc_test
...     tmp = (Cipher_DES_CBC(t.k, t.iv).encrypt(t.p) == t.c and
...            Cipher_DES_CBC(t.k, t.iv).decrypt(t.c) == t.p)
...     res = res and tmp
...     return res
... 
[34m[1m>>> [0m_all_aes_cbc_tests()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 3, in _all_aes_cbc_tests
ImportError: cannot import name 'Cipher_DES_CBC' from 'scapy.layers.tls.crypto.cipher_block' (/home/scapy/scapy/layers/tls/crypto/cipher_block.py)


###(017)=[failed] Crypto - AES cipher in CBC mode, checks from RFC 3602

[34m[1m>>> [0mclass _aes128cbc_test_1:
...     k= b"\x06\xa9\x21\x40\x36\xb8\xa1\x5b\x51\x2e\x03\xd5\x34\x12\x00\x06"
...     p= b"Single block msg"
...     c= b"\xe3\x53\x77\x9c\x10\x79\xae\xb8\x27\x08\x94\x2d\xbe\x77\x18\x1a"
...     iv=b"\x3d\xaf\xba\x42\x9d\x9e\xb4\x30\xb4\x22\xda\x80\x2c\x9f\xac\x41"
... 
[34m[1m>>> [0mclass _aes128cbc_test_2:
...     k= b"\x56\xe4\x7a\x38\xc5\x59\x89\x74\xbc\x46\x90\x3d\xba\x29\x03\x49"
...     p=(b"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf" +
...        b"\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf" +
...        b"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf" +
...        b"\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf")
...     c=(b"\xc3\x0e\x32\xff\xed\xc0\x77\x4e\x6a\xff\x6a\xf0\x86\x9f\x71\xaa" +
...        b"\x0f\x3a\xf0\x7a\x9a\x31\xa9\xc6\x84\xdb\x20\x7e\xb0\xef\x8e\x4e" +
...        b"\x35\x90\x7a\xa6\x32\xc3\xff\xdf\x86\x8b\xb7\xb2\x9d\x3d\x46\xad" +
...        b"\x83\xce\x9f\x9a\x10\x2e\xe9\x9d\x49\xa5\x3e\x87\xf4\xc3\xda\x55")
...     iv=b"\x8c\xe8\x2e\xef\xbe\xa0\xda\x3c\x44\x69\x9e\xd7\xdb\x51\xb7\xd9"
... 
[34m[1m>>> [0mclass _aes256cbc_test_1:
...     k=(b"\x60\x3d\xeb\x10\x15\xca\x71\xbe\x2b\x73\xae\xf0\x85\x7d\x77\x81" +
...        b"\x1f\x35\x2c\x07\x3b\x61\x08\xd7\x2d\x98\x10\xa3\x09\x14\xdf\xf4")
...     p= b"\x6b\xc1\xbe\xe2\x2e\x40\x9f\x96\xe9\x3d\x7e\x11\x73\x93\x17\x2a"
...     c= b"\xf5\x8c\x4c\x04\xd6\xe5\xf1\xba\x77\x9e\xab\xfb\x5f\x7b\xfb\xd6"
...     iv=b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
... 
[34m[1m>>> [0mclass _aes256cbc_test_2:
...     k=(b"\x60\x3d\xeb\x10\x15\xca\x71\xbe\x2b\x73\xae\xf0\x85\x7d\x77\x81" +
...        b"\x1f\x35\x2c\x07\x3b\x61\x08\xd7\x2d\x98\x10\xa3\x09\x14\xdf\xf4")
...     p= b"\xf6\x9f\x24\x45\xdf\x4f\x9b\x17\xad\x2b\x41\x7b\xe6\x6c\x37\x10"
...     c= b"\xb2\xeb\x05\xe2\xc3\x9b\xe9\xfc\xda\x6c\x19\x07\x8c\x6a\x9d\x1b"
...     iv=b"\x39\xF2\x33\x69\xA9\xD9\xBA\xCF\xA5\x30\xE2\x63\x04\x23\x14\x61"
... 
[34m[1m>>> [0mdef _all_aes_cbc_tests():
...     from scapy.layers.tls.crypto.cipher_block import (Cipher_AES_128_CBC,
...                                                       Cipher_AES_256_CBC)
...     res = True
...     for t in [_aes128cbc_test_1, _aes128cbc_test_2]:
...         tmp = (Cipher_AES_128_CBC(t.k, t.iv).encrypt(t.p) == t.c and
...                Cipher_AES_128_CBC(t.k, t.iv).decrypt(t.c) == t.p)
...         res = res and tmp
...     for t in [_aes256cbc_test_1, _aes256cbc_test_2]:
...         tmp = (Cipher_AES_256_CBC(t.k, t.iv).encrypt(t.p) == t.c and
...                Cipher_AES_256_CBC(t.k, t.iv).decrypt(t.c) == t.p)
...         res = res and tmp
...     return res
... 
[34m[1m>>> [0m_all_aes_cbc_tests()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 3, in _all_aes_cbc_tests
ImportError: cannot import name 'Cipher_AES_128_CBC' from 'scapy.layers.tls.crypto.cipher_block' (/home/scapy/scapy/layers/tls/crypto/cipher_block.py)


###(018)=[failed] Crypto - AES cipher in GCM mode, auth_encrypt() and auth_decrypt() checks

[34m[1m>>> [0mclass _aes128gcm_test_1:
...     k= b"\x4c\x80\xcd\xef\xbb\x5d\x10\xda\x90\x6a\xc7\x3c\x36\x13\xa6\x34"
...     n= b"\x22\x43\x3c\x64\x48\x55\xec\x7d\x3a\x23\x4b\xfd"
...     p=(b"\x08\x00\xc6\xcd\x02\x00\x07\x00\x61\x62\x63\x64\x65\x66\x67\x68" +
...        b"\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x01\x02\x02\x01")
...     a= b"\x00\x00\x43\x21\x87\x65\x43\x21\x00\x00\x00\x07"
...     ct=(b"\x74\x75\x2e\x8a\xeb\x5d\x87\x3c\xd7\xc0\xf4\xac\xc3\x6c\x4b\xff" +
...        b"\x84\xb7\xd7\xb9\x8f\x0c\xa8\xb6\xac\xda\x68\x94\xbc\x61\x90\x69" +
...        b"\xef\x9c\xbc\x28\xfe\x1b\x56\xa7\xc4\xe0\xd5\x8c\x86\xcd\x2b\xc0")
... 
[34m[1m>>> [0mclass _aes128gcm_test_2:
...     k= b"\x3d\xe0\x98\x74\xb3\x88\xe6\x49\x19\x88\xd0\xc3\x60\x7e\xae\x1f"
...     n= b"\x57\x69\x0e\x43\x4e\x28\x00\x00\xa2\xfc\xa1\xa3"
...     p=(b"\x45\x00\x00\x30\xda\x3a\x00\x00\x80\x01\xdf\x3b\xc0\xa8\x00\x05" +
...        b"\xc0\xa8\x00\x01\x08\x00\xc6\xcd\x02\x00\x07\x00\x61\x62\x63\x64" +
...        b"\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74" +
...        b"\x01\x02\x02\x01")
...     a= b"\x3f\x7e\xf6\x42\x10\x10\x10\x10\x10\x10\x10\x10"
...     ct=(b"\xfb\xa2\xca\xa8\xc6\xc5\xf9\xf0\xf2\x2c\xa5\x4a\x06\x12\x10\xad" +
...        b"\x3f\x6e\x57\x91\xcf\x1a\xca\x21\x0d\x11\x7c\xec\x9c\x35\x79\x17" +
...        b"\x65\xac\xbd\x87\x01\xad\x79\x84\x5b\xf9\xfe\x3f\xba\x48\x7b\xc9" +
...        b"\x63\x21\x93\x06\x84\xee\xca\xdb\x56\x91\x25\x46\xe7\xa9\x5c\x97" +
...        b"\x40\xd7\xcb\x05")
... 
[34m[1m>>> [0mclass _aes256gcm_test_1:
...     k=(b"\x6c\x65\x67\x61\x6c\x69\x7a\x65\x6d\x61\x72\x69\x6a\x75\x61\x6e" +
...        b"\x61\x61\x6e\x64\x64\x6f\x69\x74\x62\x65\x66\x6f\x72\x65\x69\x61")
...     n= b"\x74\x75\x72\x6e\x33\x30\x21\x69\x67\x65\x74\x6d"
...     p=(b"\x45\x00\x00\x30\xda\x3a\x00\x00\x80\x01\xdf\x3b\xc0\xa8\x00\x05" +
...        b"\xc0\xa8\x00\x01\x08\x00\xc6\xcd\x02\x00\x07\x00\x61\x62\x63\x64" +
...        b"\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74" +
...        b"\x01\x02\x02\x01")
...     a= b"\x79\x6b\x69\x63\xff\xff\xff\xff\xff\xff\xff\xff"
...     ct=(b"\xf9\x7a\xb2\xaa\x35\x6d\x8e\xdc\xe1\x76\x44\xac\x8c\x78\xe2\x5d" +
...        b"\xd2\x4d\xed\xbb\x29\xeb\xf1\xb6\x4a\x27\x4b\x39\xb4\x9c\x3a\x86" +
...        b"\x4c\xd3\xd7\x8c\xa4\xae\x68\xa3\x2b\x42\x45\x8f\xb5\x7d\xbe\x82" +
...        b"\x1d\xcc\x63\xb9\xd0\x93\x7b\xa2\x94\x5f\x66\x93\x68\x66\x1a\x32" +
...        b"\x9f\xb4\xc0\x53")
... 
[34m[1m>>> [0mclass _aes256gcm_test_2:
...     # this funny plaintext is not our deed
...     k=(b"\xab\xbc\xcd\xde\xf0\x01\x12\x23\x34\x45\x56\x67\x78\x89\x9a\xab" +
...        b"\xab\xbc\xcd\xde\xf0\x01\x12\x23\x34\x45\x56\x67\x78\x89\x9a\xab")
...     n= b"\x73\x61\x6c\x74\x61\x6e\x64\x01\x69\x76\x65\x63"
...     p=(b"\x63\x69\x73\x63\x6f\x01\x72\x75\x6c\x65\x73\x01\x74\x68\x65\x01" +
...        b"\x6e\x65\x74\x77\x65\x01\x64\x65\x66\x69\x6e\x65\x01\x74\x68\x65" +
...        b"\x74\x65\x63\x68\x6e\x6f\x6c\x6f\x67\x69\x65\x73\x01\x74\x68\x61" +
...        b"\x74\x77\x69\x6c\x6c\x01\x64\x65\x66\x69\x6e\x65\x74\x6f\x6d\x6f" +
...        b"\x72\x72\x6f\x77\x01\x02\x02\x01")
...     a= b"\x17\x40\x5e\x67\x15\x6f\x31\x26\xdd\x0d\xb9\x9b"
...     ct=(b"\xd4\xb7\xed\x86\xa1\x77\x7f\x2e\xa1\x3d\x69\x73\xd3\x24\xc6\x9e" +
...        b"\x7b\x43\xf8\x26\xfb\x56\x83\x12\x26\x50\x8b\xeb\xd2\xdc\xeb\x18" +
...        b"\xd0\xa6\xdf\x10\xe5\x48\x7d\xf0\x74\x11\x3e\x14\xc6\x41\x02\x4e" +
...        b"\x3e\x67\x73\xd9\x1a\x62\xee\x42\x9b\x04\x3a\x10\xe3\xef\xe6\xb0" +
...        b"\x12\xa4\x93\x63\x41\x23\x64\xf8\xc0\xca\xc5\x87\xf2\x49\xe5\x6b" +
...        b"\x11\xe2\x4f\x30\xe4\x4c\xcc\x76")
... 
[34m[1m>>> [0mdef _all_aes_gcm_tests():
...     from scapy.layers.tls.crypto.cipher_aead import (Cipher_AES_128_GCM,
...                                                      Cipher_AES_256_GCM)
...     res = True
...     ciphers = []
...     for t in [_aes128gcm_test_1, _aes128gcm_test_2]:
...         c = Cipher_AES_128_GCM(key=t.k, fixed_iv=t.n[:4],
...                                nonce_explicit=pkcs_os2ip(t.n[4:]))
...         ne = t.n[-c.nonce_explicit_len:]
...         tup = ne, t.p, t.ct[-c.tag_len:]
...         tmp1 = c.auth_decrypt(t.a, ne + t.ct, add_length=False) == tup
...         tmp2 = c.auth_encrypt(t.p, t.a) == (ne + t.ct)
...         res = res and tmp1 and tmp2
...     for t in [_aes256gcm_test_1, _aes256gcm_test_2]:
...         c = Cipher_AES_256_GCM(key=t.k, fixed_iv=t.n[:4],
...                                nonce_explicit=pkcs_os2ip(t.n[4:]))
...         ne = t.n[-c.nonce_explicit_len:]
...         tup = ne, t.p, t.ct[-c.tag_len:]
...         tmp1 = c.auth_decrypt(t.a, ne + t.ct, add_length=False) == tup
...         tmp2 = c.auth_encrypt(t.p, t.a) == (ne + t.ct)
...         res = res and tmp1 and tmp2
...     return res
... 
[34m[1m>>> [0m_all_aes_gcm_tests()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 3, in _all_aes_gcm_tests
ImportError: cannot import name 'Cipher_AES_128_GCM' from 'scapy.layers.tls.crypto.cipher_aead' (/home/scapy/scapy/layers/tls/crypto/cipher_aead.py)


###(021)=[failed] Crypto - Camellia cipher, encryption/decryption checks

[34m[1m>>> [0mclass _Camellia128_test:
...     k= b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
...     p= b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
...     c= b"\x67\x67\x31\x38\x54\x96\x69\x73\x08\x57\x06\x56\x48\xea\xbe\x43"
...     iv=b"\0"*16
... 
[34m[1m>>> [0mclass _Camellia256_test:
...     k=(b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10" +
...        b"\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff")
...     p= b"\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10"
...     c= b"\x9a\xcc\x23\x7d\xff\x16\xd7\x6c\x20\xef\x7c\x91\x9e\x3a\x75\x09"
...     iv=b"\0"*16
... 
[34m[1m>>> [0mdef _all_camellia_tests():
...     from scapy.layers.tls.crypto.cipher_block import (Cipher_CAMELLIA_128_CBC,
...                                                       Cipher_CAMELLIA_256_CBC)
...     res = True
...     t = _Camellia128_test
...     tmp = (Cipher_CAMELLIA_128_CBC(t.k, t.iv).encrypt(t.p) == t.c and
...            Cipher_CAMELLIA_128_CBC(t.k, t.iv).decrypt(t.c) == t.p)
...     res = res and tmp
...     t = _Camellia256_test
...     tmp = (Cipher_CAMELLIA_256_CBC(t.k, t.iv).encrypt(t.p) == t.c and
...            Cipher_CAMELLIA_256_CBC(t.k, t.iv).decrypt(t.c) == t.p)
...     res = res and tmp
...     return res
... 
[34m[1m>>> [0m_all_camellia_tests()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 3, in _all_camellia_tests
ImportError: cannot import name 'Cipher_CAMELLIA_128_CBC' from 'scapy.layers.tls.crypto.cipher_block' (/home/scapy/scapy/layers/tls/crypto/cipher_block.py)


######
## Read a protected TLS session
######


###(023)=[failed] Reading TLS test session - TLS parsing (no encryption) does not throw any error

[34m[1m>>> [0mfrom scapy.layers.tls.record import TLS
[34m[1m>>> [0mt1 = TLS(p1_ch)
[34m[1m>>> [0mt2 = TLS(p2_sh, tls_session=t1.tls_session.mirror())
TLS cipher suite not usable. Is the cryptography Python module installed?
TLS cipher suite not usable. Is the cryptography Python module installed?
[34m[1m>>> [0mt3 = TLS(p3_cert, tls_session=t2.tls_session)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xfb\xd5\x94\n\n\xe0P\xdc\x0f\xfc\x90\xb7qG\x9f,\x05\xde\x0e\x9a\xbc*\x8f\xd4\xf2\x9f\x08F\xf9\xf2\xd1\x18\xb4#\xa5*\xd2\xdf\x91?\xf9\xc5\xd0\xb2@\xbd\xd6\xbc@v.\x8d\xd8\x1e\r7\x8fz\x90W\xef\xe3\xa2\xc0\x11a\x03F\x0e\xfa\xb37\x0bf|!\x16\x8d\xfe/^.Y\xfec':\xf3\xeds\xf8Mt\xb3Q\x17u\x9a\xed\x0ck\xcd\xe8\xc1\xea\xca\x01\xacu\xf9\x17)\xf0KP\x9dAdHl\xf6\xc0g}\xc8\xea\xdeHy\x81\x97A\x02\xb7F\xf6^M\xa5\xd9\x90\x86\xd7\x1ehQ\xac>%\xae'\x11\xb1G4\xb8\x8b\xdeoyA\xd6\x92\x13)\x11\x80\xc4\x10\x17\\\x0clj\x02\xbb\xd0\n\xfc\xd2\x96x\x1d\xb6\xd4\x02\x7f\x1f\x0eR@Sop@\xda\x89)O\x0c\t~\xa3\xec\xc5W\xad\x03\xaa\x91\xedC\\\xf9\xf5[\xe8\xa1\xf0\xbem\x1b\xce-\xabC|p\xdc?\xec\xc9\x11\xf0t\xc9)\xa1P\xd0<)8\xdc\x7fV\xb9\xf8\x1f\x04\xa4^\x9f\xce\xdd\x17\x02\x03\x01\x00\x01"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 857, in getfield
    lst.append((clen, Cert(m[3:3 + clen])))
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(029)=[failed] Reading TLS test session - Certificate

[34m[1m>>> [0mfrom scapy.layers.tls.cert import Cert
[34m[1m>>> [0mcert = t3.msg[0]
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'msg'


###(030)=[failed] Reading TLS test session - Multiple TLS layers

[34m[1m>>> [0mcert_stat = t4.msg[0]
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'msg'


###(031)=[failed] Reading TLS test session - CertificateStatus

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSCertificateStatus
[34m[1m>>> [0massert(isinstance(cert_stat, TLSCertificateStatus))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'cert_stat' is not defined


###(032)=[failed] Reading TLS test session - ServerKeyExchange

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSServerKeyExchange
[34m[1m>>> [0mfrom scapy.layers.tls.keyexchange import ServerECDHNamedCurveParams
[34m[1m>>> [0massert(isinstance(ske, TLSServerKeyExchange))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'ske' is not defined


###(033)=[failed] Reading TLS test session - ServerHelloDone

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSServerHelloDone
[34m[1m>>> [0massert(isinstance(shd, TLSServerHelloDone))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'shd' is not defined


###(034)=[failed] Reading TLS test session - Context checks after 1st RTT

[34m[1m>>> [0mt = shd.tls_session
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'shd' is not defined


###(035)=[failed] Reading TLS test session - TLS parsing (with encryption) does not throw any error

[34m[1m>>> [0mt5 = TLS(p5_cke_ccs_fin, tls_session=t4.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'tls_session'


###(036)=[failed] Reading TLS test session - ClientKeyExchange

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSClientKeyExchange
[34m[1m>>> [0mfrom scapy.layers.tls.keyexchange import ClientECDiffieHellmanPublic
[34m[1m>>> [0mcke = t5.msg[0]
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'msg'


###(037)=[failed] Reading TLS test session - ChangeCipherSpec

[34m[1m>>> [0mfrom scapy.layers.tls.record import TLSChangeCipherSpec
[34m[1m>>> [0massert(isinstance(ccs, TLSChangeCipherSpec))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'ccs' is not defined


###(038)=[failed] Reading TLS test session - Finished

[34m[1m>>> [0massert(rec_fin.version == 0x0303)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'rec_fin' is not defined


###(039)=[failed] Reading TLS test session - Ticket, CCS & Finished

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSNewSessionTicket
[34m[1m>>> [0mt6 = TLS(p6_tick_ccs_fin, tls_session=t5.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'tls_session'


###(040)=[failed] Building x25519 ecdh_Yc

[34m[1m>>> [0mfrom scapy.layers.tls.record import TLS
[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSClientKeyExchange
[34m[1m>>> [0m
[34m[1m>>> [0mcli_hello = hex_bytes('160303008f0100008b0303000027104268d53e923ce05aa04cb21b8fe33aed93266c00bd1f13ea6a6dad24000018c02cc02bc030c02fc024c023c028c027c00ac009c014c0130100004a00000013001100000e7777772e676f6f676c652e636f6d000500050100000000000a00080006001d00170018000b00020100000d00140012040105010201040305030203020206010603')
[34m[1m>>> [0mser_hello = hex_bytes('16030300520200004e03035f9b52e4206fdc2410d1d482905c9b45a204641d9d856afb444f574e4752440120c4d1479e11a26edf0dbcb07e7a5f7d41c3d7b500015ff8c1ceed473bf457b193c02b000006000b0002010016030309270b0009230009200004cc308204c8308203b0a003020102021100b2fe3f66ac447c9f02000000007d9a03300d06092a864886f70d01010b05003042310b3009060355040613025553311e301c060355040a1315476f6f676c65205472757374205365727669636573311330110603550403130a47545320434120314f31301e170d3230313030363036343132305a170d3230313232393036343132305a3068310b3009060355040613025553311330110603550408130a43616c69666f726e6961311630140603550407130d4d6f756e7461696e205669657731133011060355040a130a476f6f676c65204c4c43311730150603550403130e7777772e676f6f676c652e636f6d3059301306072a8648ce3d020106082a8648ce3d030107034200046a7c4a9d35904b2b1b3f7c7326ff2adfb1bcb273b2a1a02003978dd1df8cecce5094e2309201fcd2294270ef359f4bdea177665d9e7321586682392ccc93ac89a382025c30820258300e0603551d0f0101ff04040302078030130603551d25040c300a06082b06010505070301300c0603551d130101ff04023000301d0603551d0e041604145d7ced1d850e92337bf7a0602ae3dd70668b895b301f0603551d2304183016801498d1f86e10ebcf9bec609f18901ba0eb7d09fd2b306806082b06010505070101045c305a302b06082b06010505073001861f687474703a2f2f6f6373702e706b692e676f6f672f677473316f31636f7265302b06082b06010505073002861f687474703a2f2f706b692e676f6f672f677372322f475453314f312e63727430190603551d1104123010820e7777772e676f6f676c652e636f6d30210603551d20041a30183008060667810c010202300c060a2b06010401d67902050330330603551d1f042c302a3028a026a0248622687474703a2f2f63726c2e706b692e676f6f672f475453314f31636f72652e63726c30820104060a2b06010401d6790204020481f50481f200f0007600b21e05cc8ba2cd8a204e8766f92bb98a2520676bdafa70e7b249532def8b905e00000174fcdb8af4000004030047304502207610c2e9b008b8ebf2f27a1e65631b8ae7534294c60f55a4c78c9e4927f56a23022100b61c72d94468cd6b4e376ea5d2ba7a6605a765c575f6a536b819a2d8031be4f7007600e712f2b0377e1a62fb8ec90c6184f1ea7b37cb561d11265bf3e0f34bf241546e00000174fcdb8af7000004030047304502204aae6373290fd01ad53e8ff9d6ef4f21d0badc0e65fef15c52c8f6af9468e12f022100c77dff6b266313b172ef8815beff3032d6058129baaa767361fe95e2c541ad81300d06092a864886f70d01010b05000382010100657bfcc7fd99ffed6f032bb056dc7712ec3ea437cf17750db8527ae0dcdd630f3ec4b2b95b7d482cc3a94082351117e45362319a842556954160d34c9019cc3cd312073ce540d031c4bf197b924a139b0e91bffc168a80c1641834445c509d6edf2daf8a247b72104b184968ef25cc260c75b28f470fc355477ac403da12701556e6e7550a38346f444238a154f1efb1a1a297eff39e35d76bc285599d19b0bd475d6f1daba94f1365dbc930041a79ca2df1bb724d53e4fb8831b8dc486522ee7d8eee0e1fea658352736fe949fcb233c08a3b9e14abc56a5556f9b469925cb5916ed058a4cf332c4c13a75ca83850773f9182ad95fadff51203c08e684df63b00044e3082044a30820332a003020102020d01e3b49aa18d8aa981256950b8300d06092a864886f70d01010b0500304c3120301e060355040b1317476c6f62616c5369676e20526f6f74204341202d205232311330110603')
[34m[1m>>> [0mser_cert = hex_bytes('16030309270b0009230009200004cc308204c8308203b0a003020102021100b2fe3f66ac447c9f02000000007d9a03300d06092a864886f70d01010b05003042310b3009060355040613025553311e301c060355040a1315476f6f676c65205472757374205365727669636573311330110603550403130a47545320434120314f31301e170d3230313030363036343132305a170d3230313232393036343132305a3068310b3009060355040613025553311330110603550408130a43616c69666f726e6961311630140603550407130d4d6f756e7461696e205669657731133011060355040a130a476f6f676c65204c4c43311730150603550403130e7777772e676f6f676c652e636f6d3059301306072a8648ce3d020106082a8648ce3d030107034200046a7c4a9d35904b2b1b3f7c7326ff2adfb1bcb273b2a1a02003978dd1df8cecce5094e2309201fcd2294270ef359f4bdea177665d9e7321586682392ccc93ac89a382025c30820258300e0603551d0f0101ff04040302078030130603551d25040c300a06082b06010505070301300c0603551d130101ff04023000301d0603551d0e041604145d7ced1d850e92337bf7a0602ae3dd70668b895b301f0603551d2304183016801498d1f86e10ebcf9bec609f18901ba0eb7d09fd2b306806082b06010505070101045c305a302b06082b06010505073001861f687474703a2f2f6f6373702e706b692e676f6f672f677473316f31636f7265302b06082b06010505073002861f687474703a2f2f706b692e676f6f672f677372322f475453314f312e63727430190603551d1104123010820e7777772e676f6f676c652e636f6d30210603551d20041a30183008060667810c010202300c060a2b06010401d67902050330330603551d1f042c302a3028a026a0248622687474703a2f2f63726c2e706b692e676f6f672f475453314f31636f72652e63726c30820104060a2b06010401d6790204020481f50481f200f0007600b21e05cc8ba2cd8a204e8766f92bb98a2520676bdafa70e7b249532def8b905e00000174fcdb8af4000004030047304502207610c2e9b008b8ebf2f27a1e65631b8ae7534294c60f55a4c78c9e4927f56a23022100b61c72d94468cd6b4e376ea5d2ba7a6605a765c575f6a536b819a2d8031be4f7007600e712f2b0377e1a62fb8ec90c6184f1ea7b37cb561d11265bf3e0f34bf241546e00000174fcdb8af7000004030047304502204aae6373290fd01ad53e8ff9d6ef4f21d0badc0e65fef15c52c8f6af9468e12f022100c77dff6b266313b172ef8815beff3032d6058129baaa767361fe95e2c541ad81300d06092a864886f70d01010b05000382010100657bfcc7fd99ffed6f032bb056dc7712ec3ea437cf17750db8527ae0dcdd630f3ec4b2b95b7d482cc3a94082351117e45362319a842556954160d34c9019cc3cd312073ce540d031c4bf197b924a139b0e91bffc168a80c1641834445c509d6edf2daf8a247b72104b184968ef25cc260c75b28f470fc355477ac403da12701556e6e7550a38346f444238a154f1efb1a1a297eff39e35d76bc285599d19b0bd475d6f1daba94f1365dbc930041a79ca2df1bb724d53e4fb8831b8dc486522ee7d8eee0e1fea658352736fe949fcb233c08a3b9e14abc56a5556f9b469925cb5916ed058a4cf332c4c13a75ca83850773f9182ad95fadff51203c08e684df63b00044e3082044a30820332a003020102020d01e3b49aa18d8aa981256950b8300d06092a864886f70d01010b0500304c3120301e060355040b1317476c6f62616c5369676e20526f6f74204341202d20523231133011060355040a130a476c6f62616c5369676e311330110603550403130a476c6f62616c5369676e301e170d3137303631353030303034325a170d3231313231353030303034325a3042310b3009060355040613025553311e301c060355040a1315476f6f676c65205472757374205365727669636573311330110603550403130a47545320434120314f3130820122300d06092a864886f70d01010105000382010f003082010a0282010100d018cf45d48bcdd39ce440ef7eb4dd69211bc9cf3c8e4c75b90f3119843d9e3c29ef500d10936f0580809f2aa0bd124b02e13d9f581624fe309f0b747755931d4bf74de1928210f651ac0cc3b222940f346b981049e70b9d8339dd20c61c2defd1186165e7238320a82312ffd2247fd42fe7446a5b4dd75066b0af9e426305fbe01cc46361af9f6a33ff6297bd48d9d37c1467dc75dc2e69e8f86d7869d0b71005b8f131c23b24fd1a3374f823e0ec6b198a16c6e3cda4cd0bdbb3a4596038883bad1db9c68ca7531bfcbcd9a4abbcdd3c61d7931598ee81bd8fe264472040064ed7ac97e8b9c05912a1492523e4ed70342ca5b4637cf9a33d83d1cd6d24ac070203010001a38201333082012f300e0603551d0f0101ff040403020186301d0603551d250416301406082b0601050507030106082b0601050507030230120603551d130101ff040830060101ff020100301d0603551d0e0416041498d1f86e10ebcf9bec609f18901ba0eb7d09fd2b301f0603551d230418301680149be20757671c1ec06a06de59b49a2ddfdc19862e303506082b0601050507010104293027302506082b060105050730018619687474703a2f2f6f6373702e706b692e676f6f672f6773723230320603551d1f042b30293027a025a0238621687474703a2f2f63726c2e706b692e676f6f672f677372322f677372322e63726c303f0603551d20043830363034060667810c010202302a302806082b06010505070201161c68747470733a2f2f706b692e676f6f672f7265706f7369746f72792f300d06092a864886f70d01010b050003820101001a803e3679fbf32ea946377d5e541635aec74e0899febdd13469265266073d0aba49cb62f4f11a8efc114f68964c742bd367deb2a3aa058d844d4c20650fa596da0d16f86c3bdb6f0423886b3a6cc160bd689f718eee2d583407f0d554e98659fd7b5e0d2194f58cc9a8f8d8f2adcc0f1af39aa7a90427f9a3c9b0ff02786b61bac7352be856fa4fc31c0cedb63cb44beaedcce13cecdc0d8cd63e9bca42588bcc16211740bca2d666efdac4155bcd89aa9b0926e732d20d6e6720025b10b090099c0c1f9eadd83beaa1fc6ce8105c085219512a71bbac7ab5dd15ed2bc9082a2c8ab4a621ab63ffd7524950d089b7adf2affb50ae2fe1950df346ad9d9cf5ca')
[34m[1m>>> [0m
[34m[1m>>> [0mr1 = TLS(cli_hello)
[34m[1m>>> [0mr2 = TLS(ser_hello, tls_session=r1.tls_session.mirror())
more TLS cipher suite not usable. Is the cryptography Python module installed?
[34m[1m>>> [0mr3 = TLS(ser_cert, tls_session=r2.tls_session)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xd0\x18\xcfE\xd4\x8b\xcd\xd3\x9c\xe4@\xef~\xb4\xddi!\x1b\xc9\xcf<\x8eLu\xb9\x0f1\x19\x84=\x9e<)\xefP\r\x10\x93o\x05\x80\x80\x9f*\xa0\xbd\x12K\x02\xe1=\x9fX\x16$\xfe0\x9f\x0btwU\x93\x1dK\xf7M\xe1\x92\x82\x10\xf6Q\xac\x0c\xc3\xb2"\x94\x0f4k\x98\x10I\xe7\x0b\x9d\x839\xdd \xc6\x1c-\xef\xd1\x18ae\xe7#\x83 \xa8#\x12\xff\xd2$\x7f\xd4/\xe7Dj[M\xd7Pf\xb0\xaf\x9eBc\x05\xfb\xe0\x1c\xc4ca\xaf\x9fj3\xffb\x97\xbdH\xd9\xd3|\x14g\xdcu\xdc.i\xe8\xf8mxi\xd0\xb7\x10\x05\xb8\xf11\xc2;$\xfd\x1a3t\xf8#\xe0\xeck\x19\x8a\x16\xc6\xe3\xcd\xa4\xcd\x0b\xdb\xb3\xa4Y`8\x88;\xad\x1d\xb9\xc6\x8c\xa7S\x1b\xfc\xbc\xd9\xa4\xab\xbc\xdd<a\xd7\x93\x15\x98\xee\x81\xbd\x8f\xe2dG @\x06N\xd7\xac\x97\xe8\xb9\xc0Y\x12\xa1I%#\xe4\xedp4,\xa5\xb4c|\xf9\xa3=\x83\xd1\xcdm$\xac\x07\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 857, in getfield
    lst.append((clen, Cert(m[3:3 + clen])))
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(041)=[failed] Reading TLS test session - Extended master secret

[34m[1m>>> [0mfrom scapy.layers.tls.cert import PrivKey
[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSFinished
[34m[1m>>> [0mfrom scapy.layers.tls.record import TLS
[34m[1m>>> [0m
[34m[1m>>> [0mchello_extms = hex_bytes(b'1603010200010001fc0303f8b3dbcb70ed3804009c15af4a4298720619b70d1ad4f24d0e99de9e93ce3c3b201c3b2cf3266bcba19b29479ec66fe815f7db0a6b976111f70958395e7aeebaba003e130213031301c02cc030009fcca9cca8ccaac02bc02f009ec024c028006bc023c0270067c00ac0140039c009c0130033009d009c003d003c0035002f00ff01000175000b000403000102000a000c000a001d0017001e00190018337400000010000e000c02683208687474702f312e31001600000017000000310000000d002a0028040305030603080708080809080a080b080408050806040105010601030303010302040205020602002b00050403040303002d00020101003300260024001d0020e8410f5ab09d96b05f10183ccd9e93a057a73290b4c9e1c254cdfc299fc01d41001500d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
[34m[1m>>> [0mshello_extms = hex_bytes(b'160303005502000051030320a54032477ea3a963b8a700090459f11f1f4ad1896e1d75745b7e2bdc51dde0200600f552db6c51b97a309717ff847bb6e8fef1ce2601544413fda7b66075b887009d000009ff0100010000170000160303036e0b00036a0003670003643082036030820248a003020102020900eb73b71c3e2f9fdc300d06092a864886f70d01010b05003045310b30090603550406130241553113301106035504080c0a536f6d652d53746174653121301f060355040a0c18496e7465726e6574205769646769747320507479204c7464301e170d3139303231353135313430335a170d3239303231323135313430335a3045310b30090603550406130241553113301106035504080c0a536f6d652d53746174653121301f060355040a0c18496e7465726e6574205769646769747320507479204c746430820122300d06092a864886f70d01010105000382010f003082010a0282010100d2f7d36b233a5619368fc3a7db0f2364dc71986dd4eebcbee85b783e139cfeb0a80de50147c936aa84230e2fa2eb91ef1737410387b932440ac7cfda3c5966eef88f688bcbee6a5d0dfaa075b77dfe836f2cb318375ff5be2b35f6d62dd7c4b147224f67d53d95c7fcc11cda7bc622369b4d4a685655169fb28f66e511724f0c9af2f74ea4cdf09b92f917246a582f67fade3eff7eca2c794d713c13f80cd53f847aa196d0adc04494790a628e327f4b53d05b83025c3ea541195f953ce6fc37edcc68a8fd6eca621f38bc08bc2d8d72cfcdf85c68f9f4f4485b32133c63299f85ffd62bde5a9d585e5a896f08319448277f19e86d5d6878bc53768b2ef9b3210203010001a3533051301d0603551d0e041604148297fb8cf3d9ddf2f60ec90f92815c28e3f3ff35301f0603551d230418301680148297fb8cf3d9ddf2f60ec90f92815c28e3f3ff35300f0603551d130101ff040530030101ff300d06092a864886f70d01010b050003820101003c001f0f5d106072e0beedfa47895329d4623422080e66caa4beb4c3d9b6868fa107467d6160e512ede7cbbefdeb17c09b9f594f86f1a9922c982ccf9655d4d67eda061f667eeb25fe7203bea00e40f150a490a78ca963d87c185ade8b7c294f5052fb1e1edb3403831e33e4026c8e56717cb77bc32321858be37a77fe7f5511ef8c2013c86e2730c5b2366875131cae0c7616fdc7c8605696133e7a685f20203c0db8e0ff1d1a5991d2f058f48f20b10a5fb0df27a1f9874cc0fe8d6ebf77e9a7ba38490e9d63241a0fb3fd7701ff3b130c9aa7aa77770280b7003c1bb5e0784c34aacb74ce8114960e50eee04602a7ab20e5c878028e4292e90e40fd631fee16030300040e000000')
[34m[1m>>> [0mfinished_extms = hex_bytes(b'160303010610000102010007534dd8642e57edd33d156d8002f70562864c1dfe5d721763e8e4ef2c03fb14b4e4eac1864c41fcce57367f95798f04954ef957deb934536b0ac39a72c14f772d0f64b7cc0d8260e2019748fc65fd6f382da6d4f873afe6fc1fa17e786cf6c72b6a46950d2030c7b42ed10f2c4dba37282001132ddb151a44f6face6b049338217784cf2a5ac6a054a2a1d205fb7657d7affa14113c43314b54b28164423455174f57eb50f6eea0836ba1c68616db720641bf18f0cdf7bb729c9cc0b4cfeee8aeed94e00573210eb5328cbcca4ccb1aa29a910c5b5f2c96cf3a431e9677980400d574244ff6bfdabf36ba9dda84703f5760d607e4b731d4f1dc16372b0feac11403030001011603030028269118aa98b35c71e35034f35c23c78d55c04662cdb71c11b1ef862e3b4ebf8ace2aff053257bb08')
[34m[1m>>> [0mkey = base64_bytes(b'LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2UUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktjd2dnU2pBZ0VBQW9JQkFRRFM5OU5ySXpwV0dUYVAKdzZmYkR5TmszSEdZYmRUdXZMN29XM2crRTV6K3NLZ041UUZIeVRhcWhDTU9MNkxya2U4WE4wRURoN2t5UkFySAp6OW84V1didStJOW9pOHZ1YWwwTitxQjF0MzMrZzI4c3N4ZzNYL1crS3pYMjFpM1h4TEZISWs5bjFUMlZ4L3pCCkhOcDd4aUkybTAxS2FGWlZGcCt5ajJibEVYSlBESnJ5OTA2a3pmQ2JrdmtYSkdwWUwyZjYzajcvZnNvc2VVMXgKUEJQNEROVS9oSHFobHRDdHdFU1VlUXBpampKL1MxUFFXNE1DWEQ2bFFSbGZsVHptL0RmdHpHaW8vVzdLWWg4NAp2QWk4TFkxeXo4MzRYR2o1OVBSSVd6SVRQR01wbjRYLzFpdmVXcDFZWGxxSmJ3Z3hsRWduZnhub2JWMW9lTHhUCmRvc3UrYk1oQWdNQkFBRUNnZ0VBSGQ5NTBISHNrTVNCTlZvL0tvVzZQVTM1eDl2Rml3aXUvN2YwRHRZNEpOaGUKODVpNTFiQm9UVHpvdWRtRStGWnh4SmZPWFBHYkI4TWF3N0JxOXFDeU1xUi9xZzRoa21EOVREMXcrenBBWFFtLwpkRlRuMk85OW5MQUJ0RElmeTYzT2JJUXZPa1MzczczZHpIcUpkWDFZMnVLaXp5WjNFeFZoQjZmR3Fpa09ScU1BCmNYbjJSRzN1UXFNWk4yUkVUK1hFYWdsa1dkbGphVTdaTC9CbklRT2xGS0h2ZzVSeGFwWGpJbTM2NnFUVStreGEKWDJFZnllOUJycWxWK0o4cnYzODVjRDBQc3RkSVFTQzMxZFBzUHMrSnJMVlBKQVpGZTBLVk1lYkk2ODU1cERYZApGd1ZGcC9BOXhFa3NwRW1jS0tnL1ZkZ3JQZUxMQmxhVm9mMVhPeUhWQVFLQmdRRHhPdXFGaXJvNTNQNGZQUGlMCkFnTTNvRnpmY2xwdDFMdnduelprUmVMU1NvVFBvZSt1R2xMdTBpS3lMUHBjWm1DTCt0bldsSXBheHRYOU1CRmUKOWNvMlJpSU9WM2JZM0ZpOTBLYjlvN3NyZURhaWE5NElHNGlBYktyWjJJdktBZmFkWnBqb1hBTXZpWnBEYWxGYgprZWVCd29nV0sreTdic2EwU1RYTGVMdjF5d0tCZ1FEZjRwT2lUZ3RBNFdtMXo2WFB4Z0ZCa3A3OWVjaWhINTlICnF1cVJNNkhtQ2YzSnZqZzJCZnYyb2hYNTlTU2VnZTI5ek0yZEhmVGhSeW1vZlg5VkpyMnRYY2FhVWpkRnp1Ui8Kcm1EblJMTjVDTUFnUWNCU3M5UXFCaXdTM0hqVmpML1REcFMvblJwY2VCQnNZTFYvR1YvQkpvWDkxTlVodVRXcwpjQ0VvRmNVOVF3S0JnUUNjbCtGTHhTMTBpSGZTY1hMcVVla2l3QS9wNFVMQWoxdGRMUTFTOUdiMG1ma3pDKzBaCitPNmpKM2ZzYi9RcDdTOTVUdU1BUDdhOGpOeTJtZkI4MDFOci9nVDNpR0dYRHhyd1JUVlI2MnFDSW14YzdXYloKbm4zeTJCZmtpSVRlSW40ajJVa2pkUytBT1hRUmxUK3hFTHJXNmlBTFBJSlZmZWl4ZWVEWTc4d2NGd0tCZ0Z5aQoxcTFvbDNWd0Q1cGY0ZDdYc2Z0YzNKWkxCcjNNWk01MXBQc1JueUtjN2JyRkQyTWpGTDlYRDdyT09TbXczeHNTCm05MHY0UHc1d3IzcHQzOFhPWko3WThyRXpBUUJlRUJ3ZWI0WGloOUJoS1dVTHl6SkpiZUJ1RWpSbXRuWmxDR1QKUGU4TzVUSnZwM1FBaS9pY0dpZkVkZHF5YnNHMmJjUDgzV3RGbnNnYkFvR0FMOHF4VUx3bGlMck1ML3c3aEJNegpXSHdKM21PK0NXbzFWR3p4bi9lK3I2ejVTUW03M0VuYzlSZnVkN3RBWmU1QUhXYXVSR3RNaVNoY0J1bkl5Q0g1CnU2Q2laZU5UOTBRdElLRmVCS09QSk5WNDR1QzJtK0xKQkNGa0hzU085MHp0dHZzcmVyU0tiNG5oZ2tiZDhxQ24KbDVFZFBpZEx2NXdiY0tyc3dIVzZYSm89Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=')
[34m[1m>>> [0mssl_key = PrivKey(key)
[34m[1m>>> [0m
[34m[1m>>> [0mr1 = TLS(chello_extms)
[34m[1m>>> [0mr1.tls_session.server_rsa_key = ssl_key
[34m[1m>>> [0mr2 = TLS(shello_extms, tls_session=r1.tls_session.mirror())
[34m[1m>>> [0mr3 = TLS(finished_extms, tls_session=r2.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/fields.py", line 1424, in getfield
    i = self.m2i(pkt, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 1277, in m2i
    if s.prcs and s.prcs.key_exchange:
AttributeError: 'writeConnState' object has no attribute 'key_exchange'


###(042)=[failed] Reading TLS test session - Encrypt-then-MAC extension

[34m[1m>>> [0mfrom scapy.layers.tls.cert import PrivKey
[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSFinished
[34m[1m>>> [0mfrom scapy.layers.tls.record import TLS
[34m[1m>>> [0m
[34m[1m>>> [0mclient_hello = hex_bytes(b'16030100c9010000c50303611a2f42b70345cfbc5c5c4da1929bea8a2cb8b1fd10ab1341e43ffaa8856a63000038c02cc030009fcca9cca8ccaac02bc02f009ec024c028006bc023c0270067c00ac0140039c009c0130033009d009c003d003c0035002f00ff01000064000b000403000102000a000c000a001d0017001e00190018337400000010000e000c02683208687474702f312e310016000000170000000d002a0028040305030603080708080809080a080b080408050806040105010601030303010302040205020602')
[34m[1m>>> [0mserver_hello = hex_bytes(b'1603030059020000550303a22c975875df69bea936cbd28b083cde754693b4f34a15a036e5e57b7f4755cf20226e6386f90e3751723beea9196640d5bbe6c7c9f314568fa3645cb7218e9159003d00000dff010001000016000000170000160303036e0b00036a0003670003643082036030820248a003020102020900eb73b71c3e2f9fdc300d06092a864886f70d01010b05003045310b30090603550406130241553113301106035504080c0a536f6d652d53746174653121301f060355040a0c18496e7465726e6574205769646769747320507479204c7464301e170d3139303231353135313430335a170d3239303231323135313430335a3045310b30090603550406130241553113301106035504080c0a536f6d652d53746174653121301f060355040a0c18496e7465726e6574205769646769747320507479204c746430820122300d06092a864886f70d01010105000382010f003082010a0282010100d2f7d36b233a5619368fc3a7db0f2364dc71986dd4eebcbee85b783e139cfeb0a80de50147c936aa84230e2fa2eb91ef1737410387b932440ac7cfda3c5966eef88f688bcbee6a5d0dfaa075b77dfe836f2cb318375ff5be2b35f6d62dd7c4b147224f67d53d95c7fcc11cda7bc622369b4d4a685655169fb28f66e511724f0c9af2f74ea4cdf09b92f917246a582f67fade3eff7eca2c794d713c13f80cd53f847aa196d0adc04494790a628e327f4b53d05b83025c3ea541195f953ce6fc37edcc68a8fd6eca621f38bc08bc2d8d72cfcdf85c68f9f4f4485b32133c63299f85ffd62bde5a9d585e5a896f08319448277f19e86d5d6878bc53768b2ef9b3210203010001a3533051301d0603551d0e041604148297fb8cf3d9ddf2f60ec90f92815c28e3f3ff35301f0603551d230418301680148297fb8cf3d9ddf2f60ec90f92815c28e3f3ff35300f0603551d130101ff040530030101ff300d06092a864886f70d01010b050003820101003c001f0f5d106072e0beedfa47895329d4623422080e66caa4beb4c3d9b6868fa107467d6160e512ede7cbbefdeb17c09b9f594f86f1a9922c982ccf9655d4d67eda061f667eeb25fe7203bea00e40f150a490a78ca963d87c185ade8b7c294f5052fb1e1edb3403831e33e4026c8e56717cb77bc32321858be37a77fe7f5511ef8c2013c86e2730c5b2366875131cae0c7616fdc7c8605696133e7a685f20203c0db8e0ff1d1a5991d2f058f48f20b10a5fb0df27a1f9874cc0fe8d6ebf77e9a7ba38490e9d63241a0fb3fd7701ff3b130c9aa7aa77770280b7003c1bb5e0784c34aacb74ce8114960e50eee04602a7ab20e5c878028e4292e90e40fd631fee16030300040e000000')
[34m[1m>>> [0mclient_finished = hex_bytes(b'1603030106100001020100482bf86fa7047c767ecc5f46e971f2349232d57d4c40b04856b6ea2b5645b5b233c0cd2ad7b05101d6a3fcbd2698b25064501ba4f0cde40c8189abc29aebfffcb87413d4590cae7cf3589fa371ad5e0d161da9c275a4b8ca1aa9a400a3d76021f92b872403a72a22bad6368276010209ca1344971adf7d7a9cdeefd534cd933ec3d2852ea1dfff217f7cd55eac7d2b18f7c5600c56f28746389d1d6c33cd2ac24817632fc0fbd81ffcf528b1c2a5b328a0105e88513e6b2f95b51ca3adf390146662115a721bfd718eae3033388aaa5cb37e2c16428a6f7c994f961137f6a7f933327ed300f15621500d427d261f39970bbf40f4ba303963609439007d34e6bc1403030001011603030050f4b7962d5455e9244efe886bbd4156ca20936e4b8868d80c82b06ceac7cff6d69f130a610f2aa4c4fd8cb2681f84e3ebecad1b563bcd258255aa509ba2b6388f90ac5f1c1f84f1569dc3809667b86ba4')
[34m[1m>>> [0mserver_finished = hex_bytes(b'14030300010116030300509e8e5fd6aebaa98263e98266fffcf7fd21eb50fb0510b8598660afb65c57a025374c1e63aff3e260dd5d027180e8aa0d85d43e0c0b54e8783e4ce51a71ef0ae555ab81404020342ca1a34643ce713688')
[34m[1m>>> [0m
[34m[1m>>> [0mr1 = TLS(client_hello)
[34m[1m>>> [0mr1.tls_session.server_rsa_key = ssl_key
[34m[1m>>> [0mr2 = TLS(server_hello, tls_session=r1.tls_session.mirror())
[34m[1m>>> [0mr3 = TLS(client_finished, tls_session=r2.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/fields.py", line 1424, in getfield
    i = self.m2i(pkt, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 1277, in m2i
    if s.prcs and s.prcs.key_exchange:
AttributeError: 'writeConnState' object has no attribute 'key_exchange'


###(044)=[failed] Reading TLS test session - ApplicationData

[34m[1m>>> [0mt7 = TLS(p7_data, tls_session=t6.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'tls_session'


######
## Read handshake with NULL Cipher
######


###(049)=[failed] Reading TLS test session

[34m[1m>>> [0mt1 = TLS(p1_ch)
[34m[1m>>> [0mt2 = TLS(p2_sh, tls_session=t1.tls_session.mirror())
[34m[1m>>> [0mt3 = TLS(p3_cert, tls_session=t2.tls_session)
[34m[1m>>> [0mt4 = TLS(p4_ske, tls_session=t3.tls_session)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 161, in __init__
    self.dissection_done(self)
  File "/home/scapy/scapy/packet.py", line 325, in dissection_done
    self.post_dissection(pkt)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 1085, in post_dissection
    sig_test = self.sig._verify_sig(m, s.server_certs[0])
  File "/home/scapy/scapy/layers/tls/keyexchange.py", line 215, in _verify_sig
    return cert.verify(m, self.sig_val, t=t, h=h)
  File "/home/scapy/scapy/layers/tls/cert.py", line 658, in verify
    return self.pubKey.verify(msg, sig, t=t, h=h, mgf=mgf, L=L)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


###(050)=[failed] Verify TLSClientKeyExchange

[34m[1m>>> [0mcke = t6.msg[0]
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'msg'


###(051)=[failed] Verify TLSChangeCipherSpec

[34m[1m>>> [0mccs = t6.payload.msg[0]
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'payload'


###(052)=[failed] Verify TLSFinished

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLSFinished
[34m[1m>>> [0mcfin = t6.payload.payload.msg[0]
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'payload'


###(053)=[failed] Verify MAC - TLSFinished record

[34m[1m>>> [0massert (t6.payload.payload.mac == b'\x10\xce\xca2\xb4\xc3m\xf1\x16c\xdb\xfc\x08\x16\x1d\x82\x83U\x8c\xe1')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'bool' object has no attribute 'payload'


######
## Read a vulnerable TLS session
######


###(054)=[failed] Reading TLS vulnerable session - Decrypt data from using a compromised server key

[34m[1m>>> [0mload_layer("tls")
[34m[1m>>> [0m
[34m[1m>>> [0mfrom scapy.layers.tls.cert import PrivKeyRSA
[34m[1m>>> [0mfrom scapy.layers.tls.record import TLSApplicationData
[34m[1m>>> [0mimport os
[34m[1m>>> [0mfilename = scapy_path("/test/tls/pki/srv_key.pem")
[34m[1m>>> [0mkey = PrivKeyRSA(filename)
[34m[1m>>> [0mch = b'\x16\x03\x01\x005\x01\x00\x001\x03\x01X\xac\x0e\x8c\xe46\xe9\xedo\xda\x085$M\xae$\x90\xd9\xa93\xb7(\x13J\xf9\xc5?\xef\xf4\x96\xa1\xfa\x00\x00\x04\x00/\x00\xff\x01\x00\x00\x04\x00#\x00\x00'
[34m[1m>>> [0msh = b'\x16\x03\x01\x005\x02\x00\x001\x03\x01\x88\xac\xd4\xaf\x93~\xb5\x1b8c\xe7)\xa6\x9b\xa9\xed\xf3\xf3*\xdb\x00\x8bB\xf6\n\xcbz\x8eP\x83`G\x00\x00/\x00\x00\t\xff\x01\x00\x01\x00\x00#\x00\x00\x16\x03\x01\x03\xac\x0b\x00\x03\xa8\x00\x03\xa5\x00\x03\xa20\x82\x03\x9e0\x82\x02\x86\xa0\x03\x02\x01\x02\x02\t\x00\xfe\x04W\r\xc7\'\xe9\xf60\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000T1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x160\x14\x06\x03U\x04\x03\x0c\rScapy Test CA0\x1e\x17\r160916102811Z\x17\r260915102811Z0X1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x1a0\x18\x06\x03U\x04\x03\x0c\x11Scapy Test Server0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xcc\xf1\xf1\x9b`-`\xae\xf2\x98\r\')\xd9\xc0\tYL\x0fJ0\xa8R\xdf\xe5\xb1!\x9fO\xc3=V\x93\xdd_\xc6\xf7\xb3\xf6U\x8b\xe7\x92\xe2\xde\xf2\x85I\xb4\xa1,\xf4\xfdv\xa8g\xca\x04 `\x11\x18\xa6\xf2\xa9\xb6\xa6\x1d\xd9\xaa\xe5\xd9\xdb\xaf\xe6\xafUW\x9f\xffR\x89e\xe6\x80b\x80!\x94\xbc\xcf\x81\x1b\xcbg\xc2\x9d\xb5\x05w\x04\xa6\xc7\x88\x18\x80xh\x956\xde\x97\x1b\xb6a\x87B\x1au\x98E\x82\xeb>2\x11\xc8\x9b\x86B9\x8dM\x12\xb7X\x1b\x19\xf3\x9d+\xa1\x98\x82\xca\xd7;$\xfb\t9\xb0\xbc\xc2\x95\xcf\x82)u\x16)?B \x17+M@\x8cVl\xad\xba\x0f4\x85\xb1\x7f@yqx\xb7\xa5\x04\xbb\x94\xf7\xb5A\x95\xee|\xeb\x8d\x0cyhY\xef\xcb\xb3\xfa>x\x1e\xeegLz\xdd\xe0\x99\xef\xda\xe7\xef\xb2\t]\xbe\x80 !\x05\x83,D\xdb]*v)\xa5\xb0#\x88t\x07T"\xd6)z\x92\xf5o-\x9e\xe7\xf8&+\x9cXe\x02\x03\x01\x00\x01\xa3o0m0\t\x06\x03U\x1d\x13\x04\x020\x000\x0b\x06\x03U\x1d\x0f\x04\x04\x03\x02\x05\xe00\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14\xa1+ p\xd2k\x80\xe5e\xbc\xeb\x03\x0f\x88\x9ft\xad\xdd\xf6\x130\x1f\x06\x03U\x1d#\x04\x180\x16\x80\x14fS\x94\xf4\x15\xd1\xbdgh\xb0Q725\xe1\xa4\xaa\xde\x07|0\x13\x06\x03U\x1d%\x04\x0c0\n\x06\x08+\x06\x01\x05\x05\x07\x03\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x01\x00\x81\x88\x92sk\x93\xe7\x95\xd6\xddA\xee\x8e\x1e\xbd\xa3HX\xa7A5?{}\xd07\x98\x0e\xb8,\x94w\xc8Q6@\xadY\t(\xc8V\xd6\xea[\xac\xb4\xd8?h\xb7f\xca\xe1V7\xa9\x00e\xeaQ\xc9\xec\xb2iI]\xf9\xe3\xc0\xedaT\xc9\x12\x9f\xc6\xb0\nsU\xe8U5`\xef\x1c6\xf0\xda\xd1\x90wV\x04\xb8\xab8\xee\xf7\t\xc5\xa5\x98\x90#\xea\x1f\xdb\x15\x7f2(\x81\xab\x9b\x85\x02K\x95\xe77Q{\x1bH.\xfb>R\xa3\r\xb4F\xa9\x92:\x1c\x1f\xd7\n\x1eXJ\xfa.Q\x8f)\xc6\x1e\xb8\x0e1\x0es\xf1\'\x88\x17\xca\xc8i\x0c\xfa\x83\xcd\xb3y\x0e\x14\xb0\xb8\x9b/:-\t\xe3\xfc\x06\xf0:n\xfd6;+\x1a\t*\xe8\xab_\x8c@\xe4\x81\xb2\xbc\xf7\x83g\x11nN\x93\xea"\xaf\xff\xa3\x9awWv\xd0\x0b8\xac\xf8\x8a\x945\x8e\xd7\xd4a\xcc\x01\xff$\xb4\x8fa#\xba\x88\xd7Y\xe4\xe9\xba*N\xb5\x15\x0f\x9c\xd0\xea\x06\x91\xd9\xde\xab\x16\x03\x01\x00\x04\x0e\x00\x00\x00'
[34m[1m>>> [0mck = b"\x16\x03\x01\x01\x06\x10\x00\x01\x02\x01\x00w\x93\xec\xfa\xf3\xdf[\x9a4\xa7\x9e\xcd\x06=\x8dH\xf1\x069\x8c\x06\x01S\xf7\xb5\x16h\xf6\xd5 I\xd7\xf0\xc5Z\xf6\xe0f7\x95\x91\xddNC\xe7$\xf5\xdaZ\xcdG\xd8\x14\xcaV\x98\xc4\xb2\x8cm\xe51@\x9b\x9c\xb8\xadul\xd0\xdf\xf2\xd7@Q\xe4\x05J\xf31[\xdf\xc8'(\x8f#\xf0\xc4\x1c\xc6\x07G\xb327\x85\xad\xa2\xa6\xa2E\x18\x85rP\xb8\x86uL\\7\x82\x18\xceh\xc6\xd1\xf4\xcc\xb9VN\x85\x7f9c\x92\t\x96\x8e\x80\x06\xe4\r\xbfu<\xabgP^z\xc7\xfd\x8e\x12t^\xb7\xc7Lr\xdc5\xf8\xa7\xdb\x9c\xbd\xd5\xad\xabP<\xe7\x9f%f\xb4\xd8\xf4\xf0~\x99\xbeZ\xe9\xbc\x0c9\r\xb2Uq\xfcd\xa4\xda\x89\x90\xd1\x15\x05\xcc\x00\xb1\xcd\xa9c\xb4\xe8\x7fRH\xbd\xe1\xd2\xd8\x9c\xb6\xd2\x8dq9\xe5\t\xeb\xfc\x1b\x06\xac\xab\x96\xa7\xfd{\xdf\xf2\x16\r\xd6'\xb8\xd3\xa5L\xc8\x08 \xb9\xccN\xe5\xf0\xa0S\xf3\xc3\xc9\xdf\xee\xd0\r\xd8[\x14\x03\x01\x00\x01\x01\x16\x03\x01\x000~\x01\xe1!2\x90\xba\xc8 \xb6\x8c\xb7\xd9\xf5\x80\x1d$Z^\xc8\xa3\x9f\xb3\xf1M\x0c\xd1\xedd\xb1'\x0f\xe4ER\xc9\xf7L\xf3;\xc1\xbaz\xfa\xb76\xe3q"
[34m[1m>>> [0mfin = b"\x16\x03\x01\x00\xaa\x04\x00\x00\xa6\x00\x00\x1c \x00\xa0*\xf5.4:\xe4;t\xf0v\xed\xeaLX\xa5\xce*@\xe7\x83\rWx\xadWkM-\x95\xe7\x98\xcb6x\xeb\xca\xfe8\xf5\x84*\x9bAmZ/o9\xb03\xea\x1e\x99\xfdQ\xbfe\r\xe8W\xd5\xdb\xdd\x83\x90\x14\xc6\xef\x10s\x15\xff\xc2U\xce\xb0\x00\x11\x02|\xed\x99\xbac\xfb\x03M\xce\xd3\x92\xbe\x98\x95\x1c\xef\x9b\xb1\xd6,\x0c6Td\xc9j*\x17\xb9\xde\x13\x8f\xba[\xbcD\x1b\x9a~\xe9\xa2\xf3\xa4V3\xfe\xd6'\xc8i+\xb0m\xf8&\x86\x83\xaa\xe5\x1d\x06\x07lOx\x06 \x02\xbe\xfe\xda\x93-\x9fk\xeaHu\x8a\xec_\x14\x03\x01\x00\x01\x01\x16\x03\x01\x000Pc\xe0T+\x17\\>\xd0\xbc\xe6Xx}\xe5\xa26\xea\x0b\xad\x1bY\x1b\x05,\x7f\xeeQ\xd6\xea!\x9d.\xe0\xf3\x88\xe6'jV\xfdz]M'\xcejJ"
[34m[1m>>> [0mdata = b'\x17\x03\x01\x00 \xe8\x91\'mRT\x17\xa1\xd6}+\x80\x02\xda\xadw.\x82TA\'\xdep\xa4\xe1\xb1H\xa9\xb1\x81gw\x17\x03\x01\x00P\xddD\x18\xdb\x82pz\xb75>\x1c\xd7\xa9=\x18C\xbd\xf0F\xa1k\x0c\xe5&\xf2\xdf\x97\xf0\xab5\xf41W\x85 \xcf\xd9\x98\xa4\xe8\xcc\xff \x1c\xbc\xb3U\xc8\x9c>\xc4$\xa5U\xc6\xd4\x1f"\xce\xf0\x98\xf0D\xd2\x1d\r*\x99*\xdcd4?\xc9\x0b\xa6\xb2\x81%\xfc'
[34m[1m>>> [0mt = TLS(ch)
[34m[1m>>> [0mt = TLS(sh, tls_session=t.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 175, in getfield
    p.post_dissection_tls_session_update(raw_msg)
  File "/home/scapy/scapy/layers/tls/session.py", line 1007, in post_dissection_tls_session_update
    self.tls_session_update(msg_str)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 571, in tls_session_update
    s.pwcs = writeConnState(ciphersuite=cs_cls,
  File "/home/scapy/scapy/layers/tls/session.py", line 336, in __init__
    connState.__init__(self, read_or_write="write", **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 140, in __init__
    self.ciphersuite = ciphersuite(tls_version=tls_version)
  File "/home/scapy/scapy/layers/tls/crypto/suites.py", line 143, in __init__
    self.key_block_len = self._key_block_len_v1_0
AttributeError: 'TLS_RSA_WITH_AES_128_CBC_SHA' object has no attribute '_key_block_len_v1_0'


###(055)=[failed] Auto provide the session

[34m[1m>>> [0mconf.debug_dissector = 2
[34m[1m>>> [0mclient = "192.168.0.1"
[34m[1m>>> [0mserver = "1.2.3.4"
[34m[1m>>> [0mbc = Ether()/IP(src=client, dst=server)/TCP(sport=51478, dport=443, seq=1)
[34m[1m>>> [0mbs = Ether()/IP(src=server, dst=client)/TCP(sport=443, dport=51478, seq=1)
[34m[1m>>> [0mpcap = [
...     bc/ch,
...     bs/sh,
...     bc/ck,
...     bs/fin,
...     bc/data
... ]
[34m[1m>>> [0mres = sniff(offline=pcap, session=TLSSession(server_rsa_key=key))
Socket <scapy.supersocket.IterSocket object at 0xffff886509a0> failed with ''TLS_RSA_WITH_AES_128_CBC_SHA' object has no attribute '_key_block_len_v1_0''. It was closed.
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/sendrecv.py", line 1300, in sniff
    sniffer._run(*args, **kwargs)
  File "/home/scapy/scapy/sendrecv.py", line 1218, in _run
    p = s.recv()
  File "/home/scapy/scapy/supersocket.py", line 542, in recv
    return pkt.__class__(bytes(pkt))
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 175, in getfield
    p.post_dissection_tls_session_update(raw_msg)
  File "/home/scapy/scapy/layers/tls/session.py", line 1007, in post_dissection_tls_session_update
    self.tls_session_update(msg_str)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 571, in tls_session_update
    s.pwcs = writeConnState(ciphersuite=cs_cls,
  File "/home/scapy/scapy/layers/tls/session.py", line 336, in __init__
    connState.__init__(self, read_or_write="write", **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 140, in __init__
    self.ciphersuite = ciphersuite(tls_version=tls_version)
  File "/home/scapy/scapy/layers/tls/crypto/suites.py", line 143, in __init__
    self.key_block_len = self._key_block_len_v1_0
AttributeError: 'TLS_RSA_WITH_AES_128_CBC_SHA' object has no attribute '_key_block_len_v1_0'


######
## Build TLS packets
######


###(058)=[failed] Building packets - application data with Encrypt-then-MAC

[34m[1m>>> [0msession = tlsSession(
...     rcs=connState(ciphersuite=TLS_RSA_WITH_AES_256_CBC_SHA256),
...     wcs=connState(ciphersuite=TLS_RSA_WITH_AES_256_CBC_SHA256),
... )
[34m[1m>>> [0msession.encrypt_then_mac = True
[34m[1m>>> [0msession.tls_version = 0x0303
[34m[1m>>> [0msession.rcs.cipher.key = b'A' * 32
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'connState' object has no attribute 'cipher'


###(059)=[failed] Building packets - ServerHello context linking

[34m[1m>>> [0mfrom scapy.layers.tls.crypto.kx_algs import KX_ECDHE_RSA
[34m[1m>>> [0mfrom scapy.layers.tls.crypto.cipher_block import Cipher_AES_256_CBC
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ImportError: cannot import name 'Cipher_AES_256_CBC' from 'scapy.layers.tls.crypto.cipher_block' (/home/scapy/scapy/layers/tls/crypto/cipher_block.py)


###(069)=[failed] Test tls.tools

[34m[1m>>> [0mdef test_tls_tools():
...     from scapy.layers.tls.crypto.compression import Comp_Deflate
...     from scapy.layers.tls.crypto.common import CipherError
...     from scapy.layers.tls.crypto.cipher_stream import Cipher_RC4_40
...     from scapy.layers.tls.crypto.cipher_aead import (Cipher_AES_128_GCM,
...                                                      Cipher_AES_128_GCM_TLS13)
...     from scapy.layers.tls.crypto.hash import Hash_SHA256
...     from scapy.layers.tls.crypto.pkcs1 import pkcs_i2osp, pkcs_os2ip
...     from scapy.layers.tls.tools import TLSPlaintext, TLSCompressed, TLSCiphertext
...     from scapy.layers.tls.tools import _tls_compress, _tls_decompress
...     from scapy.layers.tls.tools import _tls_mac_add, _tls_mac_verify
...     from scapy.layers.tls.tools import _tls_add_pad, _tls_del_pad
...     from scapy.layers.tls.tools import _tls_encrypt, _tls_decrypt
...     from scapy.layers.tls.tools import _tls_aead_auth_encrypt, _tls_aead_auth_decrypt
...     plain = TLSPlaintext()
...     plain.type = 'application_data'
...     plain.version = 'TLS 1.2'
...     plain.data = b'X\xe1\xb1T\xaa\xb1\x0b\xa0zlg\xf8\xd14]%\xa9\x91d\x08\xc7t\xcd6\xd4"\x9f\xcf'
...     plain.len = len(plain.data)
...     # Compress/decompress test
...     alg = Comp_Deflate()
...     comp = _tls_compress(alg, plain)
...     assert isinstance(comp, TLSCompressed)
...     assert comp != plain
...     dcomp = _tls_decompress(alg, comp)
...     assert isinstance(dcomp, TLSPlaintext)
...     assert dcomp == plain
...     # Encrypt/decrypt test
...     ch = Cipher_RC4_40(_rc4_40_test.k)
...     encr = _tls_encrypt(ch, plain)
...     assert isinstance(encr, TLSCiphertext)
...     assert encr != plain
...     decr = _tls_decrypt(ch, encr)
...     assert isinstance(decr, TLSPlaintext)
...     assert decr == plain
...     encr = _tls_encrypt(ch, comp)
...     assert isinstance(encr, TLSCiphertext)
...     assert encr != comp
...     decr = _tls_decrypt(ch, encr)
...     assert isinstance(decr, TLSPlaintext)
...     assert (decr.version == comp.version and decr.type == comp.type
...             and decr.len == comp.len and decr.data == comp.data)
...     # MAC add/verify test
...     mac = Hash_SHA256()
...     save_encr = encr.copy()
...     assert save_encr is not encr
...     _tls_mac_add(mac, encr, 1)
...     assert isinstance(encr, TLSCiphertext)
...     had_mac = _tls_mac_verify(mac, encr, 1)
...     assert had_mac
...     assert encr == save_encr
...     # Pad add/delete test
...     save_comp = comp.copy()
...     assert save_comp is not comp
...     block_size = 8
...     _tls_add_pad(comp, block_size)
...     assert isinstance(comp, TLSCompressed)
...     assert comp.len == save_comp.len + -save_comp.len % block_size + 1
...     had_pad = _tls_del_pad(comp)
...     assert had_pad
...     assert comp == save_comp
...     block_size = save_comp.len // 2
...     _tls_add_pad(comp, block_size)
...     assert isinstance(comp, TLSCompressed)
...     assert comp.len == save_comp.len + -save_comp.len % block_size + 1
...     had_pad = _tls_del_pad(comp)
...     assert had_pad
...     assert comp == save_comp
...     # AEAD auth encrypt/decrypt test
...     ch_auth = Cipher_AES_128_GCM(key=_aes128gcm_test_1.k,
...                                  fixed_iv=_aes128gcm_test_1.n[:4],
...                                  nonce_explicit=pkcs_os2ip(_aes128gcm_test_1.n[4:]))
...     auth_encr = _tls_aead_auth_encrypt(ch_auth, comp, 1)
...     assert isinstance(auth_encr, TLSCiphertext)
...     assert auth_encr != comp
...     # auth_decr = _tls_aead_auth_decrypt(ch_auth, auth_encr, 1)
...     # assert isinstance(auth_decr, TLSCompressed)
...     # assert auth_decr == comp
...     ch_auth = Cipher_AES_128_GCM_TLS13(key=_aes128gcm_test_1.k,
...                                        fixed_iv=_aes128gcm_test_1.n)
...     auth_encr = _tls_aead_auth_encrypt(ch_auth, comp, 1)
...     assert isinstance(auth_encr, TLSCiphertext)
...     assert auth_encr != comp
...     # auth_decr = _tls_aead_auth_decrypt(ch_auth, auth_encr, 1)
...     # assert isinstance(auth_decr, TLSCompressed)
...     # assert auth_decr == comp
... 
[34m[1m>>> [0mtest_tls_tools()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "<input>", line 5, in test_tls_tools
ImportError: cannot import name 'Cipher_RC4_40' from 'scapy.layers.tls.crypto.cipher_stream' (/home/scapy/scapy/layers/tls/crypto/cipher_stream.py)


###(071)=[failed] Test complex TLSServerKeyExchange dissection & build

[34m[1m>>> [0ma = b'\x16\x03\x03\x0e4\x02\x00\x00M\x03\x03^\xfa\xb5~\x88\xdf\xdc#}\'\xa0\xff\xa2\xe2\xb5\xec\x0e\x93\xa8\xe0\xde\x01[\x13[F\x151 x\xc6\xcc `)\x00\x00\x8aZ\x90l\xda\x0b\xe1\xec[i\x13\xa7\x8e\xb9a\x98"\x8a7L\x9d\x90\xe0\x01\x06c$9\xc0\'\x00\x00\x05\xff\x01\x00\x01\x00\x0b\x00\x0c\x8e\x00\x0c\x8b\x00\x06n0\x82\x06j0\x82\x05R\xa0\x03\x02\x01\x02\x02\x10EY\xe8\x1c\x1e\x9a\xe0?X\xaa\xc3\xbc\xcd`jh0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000\x81\x8f1\x0b0\t\x06\x03U\x04\x06\x13\x02GB1\x1b0\x19\x06\x03U\x04\x08\x13\x12Greater Manchester1\x100\x0e\x06\x03U\x04\x07\x13\x07Salford1\x180\x16\x06\x03U\x04\n\x13\x0fSectigo Limited1705\x06\x03U\x04\x03\x13.Sectigo RSA Domain Validation Secure Server CA0\x1e\x17\r190309000000Z\x17\r210308235959Z0W1!0\x1f\x06\x03U\x04\x0b\x13\x18Domain Control Validated1\x1d0\x1b\x06\x03U\x04\x0b\x13\x14PositiveSSL Wildcard1\x130\x11\x06\x03U\x04\x03\x0c\n*.mql5.net0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xcb\xbcn=\xbaGd\xe1XB\x07\xc9\xb1\xc8/\x86\xaa4Z\xbdNk\xfb\xffR\x8f\xe4\x1c^\x91m8\xb9^\x97\xa5\xd3N\xfb\x80\x92\x8ap\xda\x15\x9f\xee\xe7\xb3\xc8?\xb0>~\xaa\x07\x91\xb1\x99q\xe2\xe5\xc8\x9b\x1d5\xa0\x96,\x98\xdaW\x93\x95\x8e%\xe8\xd4L\xeb\xcbSg\x15"\xba\xb7\xc7\x1f\xe9\xd6\x1a\xe6E\x1d\xc8\x1e%\xd36\xe0/r\xd1\xce1C\xce\x91&\xa1\x08*R\xbf\x8cu\xb0\xda\x0e\x1e2\xd66\x1df&3\x9b\x03\x0b\xcam:\xf7\x12\xd9ud(\xae\xdc\xbci\x85\xbd\xcf\xeb{\x15:\xbd\x0e\x11\x1bi\xd8\xff]y~E\x15\x95\xee\xe9\xea\xc6Cr</\x0b\xe8\xc2\x9d\xe3\x83\x07R\xeb1\xf0\x93<|.\xf8G\xab\xa8=\xac\x16\x1d\xf9\x93%\x1b;)\xb2FN\x15\xc4\x17\xa9}\xb0\x80\xba\xfb\xc8\x15-G\x9e\x05\xe9\xf6\xc76\xc1\x9af\xa3\x91\n\xa4\x80,\x11=\x87\xec\xf9\xd6iJ\xd0\xbe\xc3K\x99J\xe7&\xc4\x86\x84:W\xc4/\x7f\x02\x03\x01\x00\x01\xa3\x82\x02\xf70\x82\x02\xf30\x1f\x06\x03U\x1d#\x04\x180\x16\x80\x14\x8d\x8c^\xc4T\xad\x8a\xe1w\xe9\x9b\xf9\x9b\x05\xe1\xb8\x01\x8da\xe10\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14z\x87\xb6T\xcbt:a\x03\xef:\x1f_\xad\xc0\x1cT\x15\x9d\xe30\x0e\x06\x03U\x1d\x0f\x01\x01\xff\x04\x04\x03\x02\x05\xa00\x0c\x06\x03U\x1d\x13\x01\x01\xff\x04\x020\x000\x1d\x06\x03U\x1d%\x04\x160\x14\x06\x08+\x06\x01\x05\x05\x07\x03\x01\x06\x08+\x06\x01\x05\x05\x07\x03\x020I\x06\x03U\x1d \x04B0@04\x06\x0b+\x06\x01\x04\x01\xb21\x01\x02\x02\x070%0#\x06\x08+\x06\x01\x05\x05\x07\x02\x01\x16\x17https://sectigo.com/CPS0\x08\x06\x06g\x81\x0c\x01\x02\x010\x81\x84\x06\x08+\x06\x01\x05\x05\x07\x01\x01\x04x0v0O\x06\x08+\x06\x01\x05\x05\x070\x02\x86Chttp://crt.sectigo.com/SectigoRSADomainValidationSecureServerCA.crt0#\x06\x08+\x06\x01\x05\x05\x070\x01\x86\x17http://ocsp.sectigo.com0\x1f\x06\x03U\x1d\x11\x04\x180\x16\x82\n*.mql5.net\x82\x08mql5.net0\x82\x01\x7f\x06\n+\x06\x01\x04\x01\xd6y\x02\x04\x02\x04\x82\x01o\x04\x82\x01k\x01i\x00v\x00\xbb\xd9\xdf\xbc\x1f\x8aq\xb5\x93\x94#\x97\xaa\x92{G8W\x95\n\xabR\xe8\x1a\x90\x96d6\x8e\x1e\xd1\x85\x00\x00\x01icH\xf8\x9b\x00\x00\x04\x03\x00G0E\x02 =\xab\xac\xefa \xc3\xf3J\xbb] w8\xc1+\xa9\x1b8\xcc\x94LP,T\xe0\x07\xe8\x87\x93s\xf5\x02!\x00\xf4D\x0e\x86a\xc9M\x8b\xc5\xf8\xec\x821\x9b\xbf]^\xacB1p\xfc\x8a\n\x07\xefz\xb6\x82 \xe0\xd5\x00v\x00D\x94e.\xb0\xee\xce\xaf\xc4@\x07\xd8\xa8\xfe(\xc0\xda\xe6\x82\xbe\xd8\xcb1\xb5?\xd33\x96\xb5\xb6\x81\xa8\x00\x00\x01icH\xf8\xdb\x00\x00\x04\x03\x00G0E\x02 ]\x91\x03.5\xaaA\xa82\xf4Bg\x08\xf7\xf1\x948N\x08,\xf5\x96\x01\x08\xdcM]&7J\xebv\x02!\x00\xeb\x90\r\xd5k\xf9\xa3L<\xc67]\xc5]\x16\xb2\x10\xed\xd5\x9b\xec\xdc$\xe1\xd5r+\x99\x19\xdbb\xe4\x00w\x00\\\xdcC\x92\xfe\xe6\xabED\xb1^\x9a\xd4V\xe6\x107\xfb\xd5\xfaG\xdc\xa1s\x94\xb2^\xe6\xf6\xc7\x0e\xca\x00\x00\x01icH\xf8\xe5\x00\x00\x04\x03\x00H0F\x02!\x00\x8f\xf5W\xd5 \xea\x02\xc4v\x1b\xd0h\x03\xe7`\xec\xdfp\xd7\xb8\x10\xd9nb7\xadDp\xf6V\xa0l\x02!\x00\xa9\x935\x94\xe3\xdb\xab\xc8N\xd2t\xa2M\xd5\xf0\x1c8\xccl\xd3}\xceQ\xc5u\xbc\xa1>!=~y0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x01\x00\x17\x7f\x18\x82[\t\x18@R@\xa6\xb7\xc5[\xf1su\xc7\x8cG?\xf7\x91\xe2E]\x1b\x7f\xc3su\x88\xb6\x17t\xc3\x8b\xb1g\xd2\x06\xfc\x82\x84\x8d\xbb\x13\xc1\x8c\xf71\xc0>(?\xa3\xf0P\x14Z\x8a\x97\x9c\xa3\xb1!ddy\xa3 .\xdb\xd3\xfb\xa6\x0b\xf7k\xdbP\xb48\xeb\xc7\x90\x00\xa9\x90\xa4\x9d\xbf\x9c\xa7\n\x8e\x90\xfe\x8f\xa3\x95Th\xe6,\xdd\xde\xde\x06\x0b\x8e+\xf5\xca\x85>n\xbf\xd87\xff\xe3\xd2|*\xc0\x89\x07\x95\xbeV\x90:lG[\xf0\xadUF\xa1\x88nmj\xbb\xa9\x16\x90\xdd\x84\xe4\xbf\xe7\xe8\xe3"\xd4+0\xa0d\xdc.\x8e\x85+\xbd\x99\xd8\x02\xa7K}\xb1\xc4\xed;\xe2\xaf\x81R\xceJ\xb9iZ\xec\xda\x8f`\x8eI\xf6]\x83-\x9e\xa7{]\x02\x9d\x1fh\xf4\xef\x14\xf4\xb3\x0e\r\xe6\x9b\x9d\x96\xb4\x90iWA\xe0\xf4\x1d_\xbeRD\x15a;?\t\x8c\x8f6\xea!\xf2\xd6/Yg\x82e/5\xe1\xb4\xa1\x94\xef\xd7\x94\x82\x04\x00\x06\x170\x82\x06\x130\x82\x03\xfb\xa0\x03\x02\x01\x02\x02\x10}[Q&\xb4v\xba\x11\xdbt\x16\x0b\xbcS\r\xa70\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0c\x05\x000\x81\x881\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x130\x11\x06\x03U\x04\x08\x13\nNew Jersey1\x140\x12\x06\x03U\x04\x07\x13\x0bJersey City1\x1e0\x1c\x06\x03U\x04\n\x13\x15The USERTRUST Network1.0,\x06\x03U\x04\x03\x13%USERTrust RSA Certification Authority0\x1e\x17\r181102000000Z\x17\r301231235959Z0\x81\x8f1\x0b0\t\x06\x03U\x04\x06\x13\x02GB1\x1b0\x19\x06\x03U\x04\x08\x13\x12Greater Manchester1\x100\x0e\x06\x03U\x04\x07\x13\x07Salford1\x180\x16\x06\x03U\x04\n\x13\x0fSectigo Limited1705\x06\x03U\x04\x03\x13.Sectigo RSA Domain Validation Secure Server CA0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xd6s3\xd6\xd7< \xd0\x00\xd2\x17E\xb8\xd6>\x07\xa2?\xc7A\xee20\xc9\xb0l\xfd\xf4\x9f\xcb\x12\x98\x0f-?\x8dM\x01\x0c\x82\x0f\x17\x7fb.\xe9\xb8Hy\xfb\x16\x83N\xad\xd72%\x93\xb7\x07\xbf\xb9P?\xa9L\xc3@*\xe99\xff\xd9\x81\xca\x1f\x162A\xda\x80&\xb9#z\x87 \x1e\xe3\xff \x9a<\x95Do\x87u\x06\x90@\xb42\x93\x16\t\x10\x08#>\xd2\xdd\x87\x0fo]Q\x14j\ni\xc5O\x01ri\xcf\xd3\x93Lm\x04\xa0\xa3\x1b\x82~\xb1\x9a\xb9\xed\xc5\x9e\xc57x\x9f\x9a\x084\xfbV.X\xc4\t\x0e\x06d[\xbc7\xdc\xf1\x9f(h\xa8V\xb0\x92\xa3\\\x9f\xbb\x88\x98\x08\x1b$\x1d\xab0\x85\xae\xaf\xb0.\x9ez\x9d\xc1\xc0B\x1c\xe2\x02\xf0\xea\xe0J\xd2\xef\x90\x0e\xb4\xc1@\x16\xf0o\x85BJd\xf7\xa40\xa0\xfe\xbf.\xa3\'Z\x8e\x8bX\xb8\xad\xc3\x19\x17\x84c\xedoV\xfd\x83\xcb`4\xc4t\xbe\xe6\x9d\xdb\xe1\xe4\xe5\xca\x0c_\x15\x02\x03\x01\x00\x01\xa3\x82\x01n0\x82\x01j0\x1f\x06\x03U\x1d#\x04\x180\x16\x80\x14Sy\xbfZ\xaa+J\xcfT\x80\xe1\xd8\x9b\xc0\x9d\xf2\xb2\x03f\xcb0\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14\x8d\x8c^\xc4T\xad\x8a\xe1w\xe9\x9b\xf9\x9b\x05\xe1\xb8\x01\x8da\xe10\x0e\x06\x03U\x1d\x0f\x01\x01\xff\x04\x04\x03\x02\x01\x860\x12\x06\x03U\x1d\x13\x01\x01\xff\x04\x080\x06\x01\x01\xff\x02\x01\x000\x1d\x06\x03U\x1d%\x04\x160\x14\x06\x08+\x06\x01\x05\x05\x07\x03\x01\x06\x08+\x06\x01\x05\x05\x07\x03\x020\x1b\x06\x03U\x1d \x04\x140\x120\x06\x06\x04U\x1d \x000\x08\x06\x06g\x81\x0c\x01\x02\x010P\x06\x03U\x1d\x1f\x04I0G0E\xa0C\xa0A\x86?http://crl.usertrust.com/USERTrustRSACertificationAuthority.crl0v\x06\x08+\x06\x01\x05\x05\x07\x01\x01\x04j0h0?\x06\x08+\x06\x01\x05\x05\x070\x02\x863http://crt.usertrust.com/USERTrustRSAAddTrustCA.crt0%\x06\x08+\x06\x01\x05\x05\x070\x01\x86\x19http://ocsp.usertrust.com0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0c\x05\x00\x03\x82\x02\x01\x002\xbfa\xbd\x0eH\xc3O\xc7\xbaGM\xf8\x9cx\x19\x01\xdc\x13\x1d\x80o\xfc\xc3p\xb4R\x9a13\x9aWR\xfb1\x9ek\xa4\xefT\xaa\x89\x8d@\x17h\xf8\x11\x10|\xd2\xca\xb1\xf1U\x86\xc7\xee\xb36\x91\x86\xf69Q\xbfF\xbf\x0f\xa0\xba\xb4\xf7~I\xc4*6\x17\x9e\xe4h9z\xaf\x94NVo\xb2{;\xbf\n\x86\xbd\xcd\xc5w\x1c\x03\xb88\xb1\xa2\x1f_~\xdb\x8a\xdcFH\xb6h\n\xcf\xb2\xb5\xb4\xe24\xe4g\xa98f\t^\xd2\xb8\xfc\x9d(:\x17@\'\xc2rN)\xfd!<|\xcf\x13\xfb\x96,\xc51D\xfd\x13\xed\xd5\x9b\xa9ihw|\xee\xe1\xff\xa4\xf968\x08S9\xa2\x844\x9c\x19\xf3\xbe\x0e\xac\xd5$7\xeb#\xa8x\xd0\xd3\xe7\xef\x92Gdb9"\xef\xc6\xf7\x11\xbe"\x85\xc6fD$&\x8e\x102\x8d\xc8\x93\xae\x07\x9e\x83>/\xd9\xf9\xf5F\x8ec\xbe\xc1\xe6\xb4\xdc\xa6\xcd!\xa8\x86\n\x95\xd9.\x85&\x1a\xfd\xfc\xb1\xb6WBm\x95\xd13\xf69\x14\x06\x82A8\xf5\x8fX\xdc\x80[\xa4\xd5}\x95x\xfd\xa7\x9b\xff\xfd\xc5\xa8i\xab&\xe7\xa7\xa4\x05\x87[\xa9\xb7\xb8\xa3 \x0b\x97\xa9E\x85\xdd\xb3\x8b\xe5\x897\x8e)\r\xfc\x06\x17\xf68@\x0eB\xe4\x12\x06\xfb{\xf3\xc6\x11hb\xdf\xe3\x98\xf4\x13\xd8\x15O\x8b\xb1i\xd9\x10`\xbcd*\xea1\xb7\xe4\xb5\xa3:\x14\x9b&\xe3\x0b{\xfd\x02\x8e\xb6\x99\xc18\x97Y6\xf6\xa8t\xa2\x86\xb6^\xeb\xc6d\xea\xcf\xa0\xa3\xf9n\x9e\xba-\x11\xb6\x86\x98\x08X-\xc9\xac%d\xf2^u\xb48\xc1\xae\x7fZF\x83\xeaQ\xca\xb6\xf1\x99\x115k\xa5j{\xc6\x00\xb0\xe7\xf8\xbed\xb2\xad\xc8\xc2\xf1\xac\xe3Q\xea\xa4\x93\xe0y\xc8\xe1\x81@\xc9\n[\xe1\x12<\xc1`*\xe3\x97\xc0\x89B\xca\x94\xcfF\x98\x12i\xbb\x98\xd0\xc2\xd3\rrKGn\xe5\x93\xc42(c\x87C\xe4\xb02>\n\xd3K\xbf#\x9b\x14)A+\x9a\x04\x1f\x93-\xf1\xc79H<\xadZ\x12\x7f\x0c\x00\x01I\x03\x00\x17A\x04\x13\x1c\x02q\xd4m\x97\x01\x99\xcf\xf2\x80G\xa8\xe1\xdf\x1ak\xbf\x1fJ\xf9\x9e\xd0\x02\x01W\x9d\xb8\xbc*\xf9S\xb6\xbf\xb8\xf1\xc1\x89\xcd\x96C(\xa8|\x189\x13\xcd\xc5\xf7Q\x1e\xe17h~\x8c`\x1f8\x8e\xacq\x04\x01\x01\x00\xc1R`\xb8\x14!\xed\xb9\xbca\x9d0{\xb7\x95\x94\x80\x06\t.A\xcc\x82\x99\x89N_\xa1\x08M%#\x1fg\xb6\xa2\xfe\x00\xd6\xa8\xe9\x9fd\x91O\xdbzw\xbfS\x88?\xeb[2\x7f\xa1\xeb\xd1vmi_\x95\xd0A\x04`\x01+\x02\\\x99\xa0\xe9\n\xb5\xb5j\x85\x89J\x82\xf8\x00\xbb\xa3%\x14\x15D\xbf9\x12{\x9e\xca\x0e\x92\xdf\xbb\xfd\xd3\xc8\x0ez\x04n \x12\x01\xd2|\xc6t\xc36\xce>:J\xc3\x81+d\xbc\xb1\x1d\x8d\x00o\x00\xc9\xd4%\xb6\x90\x1f\xe1\xc5\x14\xb5Qk\x06\x1e\xf6{\xbdJ\xb2H\xcbf\xe9_mQ(\x9e4\x10U#\xcd4\x88\x1c\xfb\x03\x80(Q:\x9c\x0f\x16\xed\xad\xb4\x18k\t\xc5$\x97}~s\xc1\xca\xae\x9d\xd1q\x94\x9fi+Pj\x80:v\xc1z#\xf6\xee]ou~\xa3\xd9I\xce\xb8Z|\x1b\x8ep\xc6\x19\xb4A\x03\x92\x1bp\x16\x10\x0f\x84\xa9\x9f\xb7\xc9\x01\xc8^\x93\xaat\r\x87\x96\x86\xf6\xc5\xfe\x88\x13\xc3N\x0e\x00\x00\x00'
[34m[1m>>> [0mp = TLS(a)
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xcb\xbcn=\xbaGd\xe1XB\x07\xc9\xb1\xc8/\x86\xaa4Z\xbdNk\xfb\xffR\x8f\xe4\x1c^\x91m8\xb9^\x97\xa5\xd3N\xfb\x80\x92\x8ap\xda\x15\x9f\xee\xe7\xb3\xc8?\xb0>~\xaa\x07\x91\xb1\x99q\xe2\xe5\xc8\x9b\x1d5\xa0\x96,\x98\xdaW\x93\x95\x8e%\xe8\xd4L\xeb\xcbSg\x15"\xba\xb7\xc7\x1f\xe9\xd6\x1a\xe6E\x1d\xc8\x1e%\xd36\xe0/r\xd1\xce1C\xce\x91&\xa1\x08*R\xbf\x8cu\xb0\xda\x0e\x1e2\xd66\x1df&3\x9b\x03\x0b\xcam:\xf7\x12\xd9ud(\xae\xdc\xbci\x85\xbd\xcf\xeb{\x15:\xbd\x0e\x11\x1bi\xd8\xff]y~E\x15\x95\xee\xe9\xea\xc6Cr</\x0b\xe8\xc2\x9d\xe3\x83\x07R\xeb1\xf0\x93<|.\xf8G\xab\xa8=\xac\x16\x1d\xf9\x93%\x1b;)\xb2FN\x15\xc4\x17\xa9}\xb0\x80\xba\xfb\xc8\x15-G\x9e\x05\xe9\xf6\xc76\xc1\x9af\xa3\x91\n\xa4\x80,\x11=\x87\xec\xf9\xd6iJ\xd0\xbe\xc3K\x99J\xe7&\xc4\x86\x84:W\xc4/\x7f\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 857, in getfield
    lst.append((clen, Cert(m[3:3 + clen])))
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


###(073)=[failed] Test TLS TCP defragmentation

[34m[1m>>> [0mimport os
[34m[1m>>> [0m
[34m[1m>>> [0mfilename = scapy_path("/test/pcaps/tls_tcp_frag.pcap.gz")
[34m[1m>>> [0m
[34m[1m>>> [0mdd = conf.debug_dissector
[34m[1m>>> [0mconf.debug_dissector = False
[34m[1m>>> [0m
[34m[1m>>> [0ma = sniff(offline=filename, session=TCPSession)[0]
[34m[1m>>> [0m
[34m[1m>>> [0mconf.debug_dissector = dd
[34m[1m>>> [0m
[34m[1m>>> [0massert len(a.msg) == 4
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(074)=[failed] Issue 2527

[34m[1m>>> [0mp = TLS(b'\x16\x03\x00\x05\'\x02\x00\x00&\x03\x00\x00\x00\x00\x00\x7fk77\n\xe2\x1d\xdf\x82e\x06p$\xbaV7_\xa9\xb1\x03\x01\x0c\x0c\x18\x90\x00H\x01\x00\x00\x03\x00\x0b\x00\x03\xa8\x00\x03\xa5\x00\x03\xa20\x82\x03\x9e0\x82\x02\x86\xa0\x03\x02\x01\x02\x02\t\x00\xfe\x04W\r\xc7\'\xe9\xf60\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000T1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x160\x14\x06\x03U\x04\x03\x0c\rScapy Test CA0\x1e\x17\r160916102811Z\x17\r260915102811Z0X1\x0b0\t\x06\x03U\x04\x06\x13\x02MN1\x140\x12\x06\x03U\x04\x07\x0c\x0bUlaanbaatar1\x170\x15\x06\x03U\x04\x0b\x0c\x0eScapy Test PKI1\x1a0\x18\x06\x03U\x04\x03\x0c\x11Scapy Test Server0\x82\x01"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\xcc\xf1\xf1\x9b`-`\xae\xf2\x98\r\')\xd9\xc0\tYL\x0fJ0\xa8R\xdf\xe5\xb1!\x9fO\xc3=V\x93\xdd_\xc6\xf7\xb3\xf6U\x8b\xe7\x92\xe2\xde\xf2\x85I\xb4\xa1,\xf4\xfdv\xa8g\xca\x04 `\x11\x18\xa6\xf2\xa9\xb6\xa6\x1d\xd9\xaa\xe5\xd9\xdb\xaf\xe6\xafUW\x9f\xffR\x89e\xe6\x80b\x80!\x94\xbc\xcf\x81\x1b\xcbg\xc2\x9d\xb5\x05w\x04\xa6\xc7\x88\x18\x80xh\x956\xde\x97\x1b\xb6a\x87B\x1au\x98E\x82\xeb>2\x11\xc8\x9b\x86B9\x8dM\x12\xb7X\x1b\x19\xf3\x9d+\xa1\x98\x82\xca\xd7;$\xfb\t9\xb0\xbc\xc2\x95\xcf\x82)u\x16)?B \x17+M@\x8cVl\xad\xba\x0f4\x85\xb1\x7f@yqx\xb7\xa5\x04\xbb\x94\xf7\xb5A\x95\xee|\xeb\x8d\x0cyhY\xef\xcb\xb3\xfa>x\x1e\xeegLz\xdd\xe0\x99\xef\xda\xe7\xef\xb2\t]\xbe\x80 !\x05\x83,D\xdb]*v)\xa5\xb0#\x88t\x07T"\xd6)z\x92\xf5o-\x9e\xe7\xf8&+\x9cXe\x02\x03\x01\x00\x01\xa3o0m0\t\x06\x03U\x1d\x13\x04\x020\x000\x0b\x06\x03U\x1d\x0f\x04\x04\x03\x02\x05\xe00\x1d\x06\x03U\x1d\x0e\x04\x16\x04\x14\xa1+ p\xd2k\x80\xe5e\xbc\xeb\x03\x0f\x88\x9ft\xad\xdd\xf6\x130\x1f\x06\x03U\x1d#\x04\x180\x16\x80\x14fS\x94\xf4\x15\xd1\xbdgh\xb0Q725\xe1\xa4\xaa\xde\x07|0\x13\x06\x03U\x1d%\x04\x0c0\n\x06\x08+\x06\x01\x05\x05\x07\x03\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x01\x01\x00\x81\x88\x92sk\x93\xe7\x95\xd6\xddA\xee\x8e\x1e\xbd\xa3HX\xa7A5?{}\xd07\x98\x0e\xb8,\x94w\xc8Q6@\xadY\t(\xc8V\xd6\xea[\xac\xb4\xd8?h\xb7f\xca\xe1V7\xa9\x00e\xeaQ\xc9\xec\xb2iI]\xf9\xe3\xc0\xedaT\xc9\x12\x9f\xc6\xb0\nsU\xe8U5`\xef\x1c6\xf0\xda\xd1\x90wV\x04\xb8\xab8\xee\xf7\t\xc5\xa5\x98\x90#\xea\x1f\xdb\x15\x7f2(\x81\xab\x9b\x85\x02K\x95\xe77Q{\x1bH.\xfb>R\xa3\r\xb4F\xa9\x92:\x1c\x1f\xd7\n\x1eXJ\xfa.Q\x8f)\xc6\x1e\xb8\x0e1\x0es\xf1\'\x88\x17\xca\xc8i\x0c\xfa\x83\xcd\xb3y\x0e\x14\xb0\xb8\x9b/:-\t\xe3\xfc\x06\xf0:n\xfd6;+\x1a\t*\xe8\xab_\x8c@\xe4\x81\xb2\xbc\xf7\x83g\x11nN\x93\xea"\xaf\xff\xa3\x9awWv\xd0\x0b8\xac\xf8\x8a\x945\x8e\xd7\xd4a\xcc\x01\xff$\xb4\x8fa#\xba\x88\xd7Y\xe4\xe9\xba*N\xb5\x15\x0f\x9c\xd0\xea\x06\x91\xd9\xde\xab\x0c\x00\x01I\x00@\xd1L\xf3\xe7\x8b\xdd\x98\xff\xb2\xf5Rd\xd6\x85\x0f\r{\x9f\xc2\xc0\x8aY\xbf.\xfb\xf0o\x96\xa5\xba;\x877qet\xe8\xe4K\xd7\xcb\xb8\xecAk>S\xe0\xa5\xc3\xfc\xe8\xde\xf1\xb0\xe5\x15s|\xb7\xe6D\x15+\x00\x03\x01\x00\x01\x01\x00H\xf1\x08\x88\xe9\xf8\xe6\xb2y\\\xf9\xf64\x95r\xf9\x8c]\x0b\x88%s\xee{\xd4\xa3{|Jd>\xfb\x01\x0b\xfdAf\xea\x13%\x1f\xcc\xba\xf8H\xed\xeb?u\x00\xc46\xe4\x9f!r\x99\xec\'!\xa1+\xe9\xcd;\xfa\x00a\xd1ME7\x9a\xc3C\xb2\xb0>\xec\x07\xff>\xb3\xa3\xbd\x8db\xa2\x17\x0b\xce\xe1H\xaf\xba_\xdc\x18\x83Fr^\xf6\xfd\x8f\xbd\xc1\xdf\xc3\xf9T\xc2RC\xfa1\xe1\x16\x94RgZ\xb1\xe8rycp\xaeEa@\xe2\xb7T\xe4\xaa7\x02\x1e\xb3\x0c_P\x14\xd9\x023]\xc9)\x1b\xd7]\xba\x8aS\x18\xe5\x88\x1e08W\xc7\xd5\xc0\x7f\xf6n\n>\x83_\r\t\x1f\x01\x99\xda\x88(\xbc\xd9\xb8!=\xb6%\x15wh\xacl)\xde\xb3-\x81M\xc6(,\xceom\x15W7\xcc\xd3\xe3\xc2e\xb4\x96\xf1\xfc\x1e\xa5?\xe1B\xbd\x00\x89\xc1\xd0t\xd6\xaa\xf8\xa7\x1f\xa1z}\x91M\x8egg\xa1}\x93\xaal\xec\x16@\xf3\xd7\x0b\x91\n\xcc\x0e\x00\x00\x00')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 175, in getfield
    p.post_dissection_tls_session_update(raw_msg)
  File "/home/scapy/scapy/layers/tls/session.py", line 1007, in post_dissection_tls_session_update
    self.tls_session_update(msg_str)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 571, in tls_session_update
    s.pwcs = writeConnState(ciphersuite=cs_cls,
  File "/home/scapy/scapy/layers/tls/session.py", line 336, in __init__
    connState.__init__(self, read_or_write="write", **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 140, in __init__
    self.ciphersuite = ciphersuite(tls_version=tls_version)
  File "/home/scapy/scapy/layers/tls/crypto/suites.py", line 143, in __init__
    self.key_block_len = self._key_block_len_v1_0
AttributeError: 'TLS_RSA_EXPORT_WITH_RC4_40_MD5' object has no attribute '_key_block_len_v1_0'


###(077)=[failed] Issue 3324 - FFDH support

[34m[1m>>> [0mhex_data = "16030102a8010002a4030330cc71861d50119dbe2b9c3a5207b7eff49aff19408096b32926d6fe8a4878e520c03832cba05660b5facc4b9991f3b006d326325ab1e0a9463287271952f4235f0004130200ff0100025700000020001e00001b6578616d706c653132333435362e6d79636f6d70616e792e636f6d000a000400020102002300000016000000170000000d000400020403002b0003020304002d00020101003302060204010202003476f00e12d8c768be0bd6db6af9e539441edd84b87178e8843bb2febc4b2097ac9619e65ed61837550e51834c32c7cb007b9b9a2f129d7127ee9f8bcbc2ba2141677300bc660d080d32257731d8d795bda7467df240cf07e8f1cde33bfc1f168385babee0f5834269f3c1070f7d89b3b9607b474edd306af54638d14e58cdc524b8972035a762dc446ef95b30a8c5e06876804ec9fb180f0255ea93b1438336e414761e1e1e2772909ce3fadc5282674337267f9697204b81a0b3ded2a3ecb03b46c1a4113e44b23a67d349b0406903b6acfdce0595e16b4f41dee9351f16e1267f9bdc6abbd897332552cb9b139f1556fc207fb8dee337d185acbe6b1b42c09751339e7d441933bec3cc4b24740b1640a2af73eadf700e0bee5065c38886f6a5983e1029f67085590f95f9546057725c004804cd97ed2c1c5ca0383751e77c087449719e65d9a39adad84e1bab92c0f9b7b472e58f60d4f81e3b622d7f62fd61c747e5951b54e9ef7b1a65b07e25c94baa7c19284ecf855a5cff7dae958359f3bd5d6184f11a3785026f8479d25595948160de89e8af62f306783c79b0bf28fb18da512737b52ede9f826ed95ed1ce8386e3ff3e74ba0b7ad82bef0c046223986475de12c9654f0fc3cb162d24ab02fe51120566bc993583e10149c16d953640357785e88748739cf84a3f0930fe5b4732f17f32e7e7fdf00023643a798cf7"
[34m[1m>>> [0m
[34m[1m>>> [0mkey = "3476f00e12d8c768be0bd6db6af9e539441edd84b87178e8843bb2febc4b2097ac9619e65ed61837550e51834c32c7cb007b9b9a2f129d7127ee9f8bcbc2ba2141677300bc660d080d32257731d8d795bda7467df240cf07e8f1cde33bfc1f168385babee0f5834269f3c1070f7d89b3b9607b474edd306af54638d14e58cdc524b8972035a762dc446ef95b30a8c5e06876804ec9fb180f0255ea93b1438336e414761e1e1e2772909ce3fadc5282674337267f9697204b81a0b3ded2a3ecb03b46c1a4113e44b23a67d349b0406903b6acfdce0595e16b4f41dee9351f16e1267f9bdc6abbd897332552cb9b139f1556fc207fb8dee337d185acbe6b1b42c09751339e7d441933bec3cc4b24740b1640a2af73eadf700e0bee5065c38886f6a5983e1029f67085590f95f9546057725c004804cd97ed2c1c5ca0383751e77c087449719e65d9a39adad84e1bab92c0f9b7b472e58f60d4f81e3b622d7f62fd61c747e5951b54e9ef7b1a65b07e25c94baa7c19284ecf855a5cff7dae958359f3bd5d6184f11a3785026f8479d25595948160de89e8af62f306783c79b0bf28fb18da512737b52ede9f826ed95ed1ce8386e3ff3e74ba0b7ad82bef0c046223986475de12c9654f0fc3cb162d24ab02fe51120566bc993583e10149c16d953640357785e88748739cf84a3f0930fe5b4732f17f32e7e7fdf00023643a798cf7"
[34m[1m>>> [0m
[34m[1m>>> [0mtls_packet = TLS(hex_bytes(hex_data))
[34m[1m>>> [0massert tls_packet.msg[0].ext[8].client_shares[0].sprintf("%group%") == 'ffdhe4096'
[34m[1m>>> [0massert tls_packet.msg[0].ext[8].client_shares[0].key_exchange == hex_bytes(key)
[34m[1m>>> [0massert tls_packet.tls_session.tls13_client_pubshares['ffdhe4096'].key_size == 4096
Traceback (most recent call last):
  File "<input>", line 2, in <module>
KeyError: 'ffdhe4096'


###(078)=[failed] OCSP: payload after OCSP - GH3291

[34m[1m>>> [0mdata = b'1603031616020000660303602161b58e22f4966f18f9aa6afd5759f343935ed437cf09c554dd27691a1eb420a13c0000eaad0a6cd4f11bfc59788daec98422be4f3810c19669207e509aaa11c03000001e000500000023000000100005000302683200170000ff01000100000000000b000d5d000d5a0007f6308207f2308205daa00302010202136b000006c55514d0a6c4891be20000000006c5300d06092a864886f70d01010b0500304f310b3009060355040613025553311e301c060355040a13154d6963726f736f667420436f72706f726174696f6e3120301e060355040313174d6963726f736f66742052534120544c53204341203031301e170d3230303930393231343530355a170d3231303930393231343530355a30223120301e060355040313177074692e73746f72652e6d6963726f736f66742e636f6d30820122300d06092a864886f70d01010105000382010f003082010a028201010094876b9572b7c3d7fbb2d569ffff6b8f716245a2d9b413c9e8238ee88d98b1002cec8c2198b52f3b7f0a679ceb1aeb2c1467d2eda3c71b4bb0756ba42354a956b8d40bd422921793b3dec0aab3f5e0b023bcb7dfdf48bd4b064c1a62255e9b58c16ad482087fd1505b01aad9474f06925f3821fbe92f680e87db3f0aa150e2066848f88ebe08d8280185bbba697b39d12e03eae6d4e481319432f2752793fcd125f2714cd92b37e3d9b8fcec7fd7b3c121fdedc42b50ff65f73352cbc1202ac59c846df2a9168c00fc4754f5e19c3b0503dbe4f58b0f8b3e0fa411d4dcb8e1acdef9a2ca7db52e282a14119e1ef3a867a3b7d8fdaccc27d3d2033bb5082a1b510203010001a38203f2308203ee30820105060a2b06010401d6790204020481f60481f300f10076007d3ef2f88fff88556824c2c0ca9e5289792bc50e78097f2e6a9768997e22f0d70000017474dd866500000403004730450221008886de3960d7fe8cbaa9bcf91f961d920af99ec72adaf07fb6f6e2759d6d045b02201f90de8ad6dc333cbf920fe6cd66b41d97a01397831b2ea39f618c1505ecc7e70077004494652eb0eeceafc44007d8a8fe28c0dae682bed8cb31b53fd33396b5b681a80000017474dd86d200000403004830460221008f66e7ce568540722b5a09d96bc08d78a1cc98dda6c7c2cda1daaa7ea49d75f302210099ccca061b9b31f938988f2e4182fcb39035f6e90d5dee8c928582bd4e5fb693302706092b060104018237150a041a3018300a06082b06010505070301300a06082b06010505070302303e06092b06010401823715070431302f06272b060104018237150887da867583eed90182c9851b81b59e6185f4eb60815d85868e4187c2985002016402012530818706082b06010505070101047b3079305306082b060105050730028647687474703a2f2f7777772e6d6963726f736f66742e636f6d2f706b692f6d73636f72702f4d6963726f736f6674253230525341253230544c53253230434125323030312e637274302206082b060105050730018616687474703a2f2f6f6373702e6d736f6373702e636f6d301d0603551d0e041604142746d09d123c3c91382ef590e0aab2a901f0d0c3300b0603551d0f0404030204b030780603551d110471306f821b7074692d696e742e73746f72652e6d6963726f736f66742e636f6d82177074692e73746f72652e6d6963726f736f66742e636f6d821a7074692d696e742e747261666669636d616e616765722e6e6574821b7074692d70726f642e747261666669636d616e616765722e6e65743081b00603551d1f0481a83081a53081a2a0819fa0819c864d687474703a2f2f6d7363726c2e6d6963726f736f66742e636f6d2f706b692f6d73636f72702f63726c2f4d6963726f736f6674253230525341253230544c53253230434125323030312e63726c864b687474703a2f2f63726c2e6d6963726f736f66742e636f6d2f706b692f6d73636f72702f63726c2f4d6963726f736f6674253230525341253230544c53253230434125323030312e63726c30570603551d200450304e304206092b0601040182372a013035303306082b060105050702011627687474703a2f2f7777772e6d6963726f736f66742e636f6d2f706b692f6d73636f72702f6370733008060667810c010201301f0603551d23041830168014b5760c3011cec792424d4cc75c2cc8a90ce80b64301d0603551d250416301406082b0601050507030106082b06010505070302300d06092a864886f70d01010b0500038202010086dd00ab90b01c8f5c87d59c2cc45e2cb81998699e5e97aeceea13670bbf2b76e9add7cd11bc4ef347dbab7ea7c28300223bd43e5d2904db1516c55572181534f4efc11eccf4d10a9c08ddfbff53cad870856e0e3377b7639cfc3de5d3c7ca8294cc6e7ac0cac0e1a3cd4b0b81cdcb2fa1dbf6ebc2659d6f1947e8047be27c02fba8b6a991837781cea269246353e5441aa33c8494d4591ee482f448bef23460578f96c5c1e92f5a7cd7c81815b40a7cc00aeee6976a708c1d236c7fe64a4a45f7fd83707c0e621ff7e78fe089dd3ff539148a0acba6a99a8ca630ef2e2c83529596bbb3fb1c9ea7f371158d70b36120217154003e791db16390877c83dd27543c15e73c1af5f22b4c7c73347a9b97de633abdd9413363877a8a428f18cd624e310e2ea17aa4740a167aabecfb5f5c244ef8ada6638f90592df625885b9a57ec478acca5ec2c35e6c66b597be4570057d6769f3e5c2487ea70f84ecabc0f4064bb0e7be746d652f3861b931eb0e75846253e7eeae987cf7d4193bd1dc85044ee798d821536944c7ade7e269b13e4ece47093c641e7fc8d31dc0e3d211d94e8b450cfed2733ad78fac2eae225acd505117c39243a8e24feebd47ff875643d1ef777dd2a1a18f370dd83fdf85ca2eadf3c46711aedc68fc13b1db8bf71e015c77f69882613ea096c216e759553ea475a48db8ac4e92b8b184b7dbc9d458758e85200055e3082055a30820442a00302010202100f14965f202069994fd5c7ac788941e2300d06092a864886f70d01010b0500305a310b300906035504061302494531123010060355040a130942616c74696d6f726531133011060355040b130a43796265725472757374312230200603550403131942616c74696d6f7265204379626572547275737420526f6f74301e170d3230303732313233303030305a170d3234313030383037303030305a304f310b3009060355040613025553311e301c060355040a13154d6963726f736f667420436f72706f726174696f6e3120301e060355040313174d6963726f736f66742052534120544c5320434120303130820222300d06092a864886f70d01010105000382020f003082020a0282020100aa6277cf9a63b20684f39036f499f31451abea950a3b4606fd11411ffe5b0658c9386e08fc4f4448cd3aa4f7bd1ea2e295b8be5120c5bfb270635d780c43c029cd64490996daafcefd055f2b2a91e8016e2e189b2c9cd0017f69f5ee3f53885cba056cbe2215671482f22cd2be5b6337ccaf6085e8966b6b8008a86ebe009c6b9570fce41812b11d1bb2c11331673334e625c9625b58827576f2fef23f3b16dfaa4283e3326d9b8e4326f0bd0e1fa1a73aaf2cc88ae6ea3ff9a5d2258f92aa1a08129cfeac4ac7c3eb8094ab8716d12349e7a4bbc791dfe679343f414aa73a26d2ea6f46e33873e6e5d491ae0b789e78a5ef96e373d8f79565e905bf4f5cff52a7f9cf08afa74d0999c071a3527aa53bd79b015403e3b662b05a279c30268eb64d56a117177a7b95a107ac5331b6d62e0fcd4174ecf101b2fd45bffc31e146423136431eb9aa055f847f91b18bae0fd754c3fdf064086ad39c8eea7934ec033d73e01b36d46811c75970b0877cc0dc6e45ca36ce43267702a9700de8b857544442c3fbac1b632608c2d2231f7f930b7c6f08549a2b4e5dce9fa53ed2985bd102dbf183ce3052483863f1b1fbed23d33e92b5278dd04273d79d236871ba595e0752a6964dbf7c4e6f742205c0538016d8604e97314f894e4863d8edf9e5c2d90eb20bf6694cbd4b01c9cbdd06bf3a02eb1cdd308b0d4a1460f9d5644f4344a1ed0203010001a382012530820121301d0603551d0e04160414b5760c3011cec792424d4cc75c2cc8a90ce80b64301f0603551d23041830168014e59d5930824758ccacfa085436867b3ab5044df0300e0603551d0f0101ff040403020186301d0603551d250416301406082b0601050507030106082b0601050507030230120603551d130101ff040830060101ff020100303406082b0601050507010104283026302406082b060105050730018618687474703a2f2f6f6373702e64696769636572742e636f6d303a0603551d1f04333031302fa02da02b8629687474703a2f2f63726c332e64696769636572742e636f6d2f4f6d6e69726f6f74323032352e63726c302a0603551d20042330213008060667810c0102013008060667810c010202300b06092b0601040182372a01300d06092a864886f70d01010b050003820101009f2bbe92675bda7b8aade8ff9d4d050eedb60d1541d1e615dc0360f9f422569c48f99daeda2b3ca8c0abd0ba95b8c8c1fd7c6371b6c87a889b3046a38e7d9602e3f82204efe036c06fc2bf2e0d6eedd676280d81873e9be7a7108cda661f4051eae7bebf4e6798bb5459636f42e30f31601964000f260c97d184c0a67a193b70de4526dc96463d9c663fe13a8238e53603042857a4e94b64a218886d60898d7abe10918bace63f3130bfeb64d79e8de9c192566e388d343faecd6c6b4252623cd46989e0a057590b839fc6722442f5080384ce1663f334f105763719b206de133e137061d304f2b8476f05e38a88302b47455e7954c5f9ddebfa3f785175d25b160006d6010006d2308206ce0a0100a08206c7308206c306092b0601050507300101048206b4308206b03081a5a21604149a0190a5b9942f43bc62113fcd3d404bead25250180f32303231303230383036303930325a307a3078304c300906052b0e03021a05000414521ee36c478119a9cb03fab74e57e1197af1818b0414b5760c3011cec792424d4cc75c2cc8a90ce80b6402136b000006c55514d0a6c4891be20000000006c58000180f32303231303230383036303930325aa011180f32303231303231323036303930325aa1023000300d06092a864886f70d01010b05000382010100784c3cee7765bf5cb164c0cf465462c37e97d11041443dcd9052e413747a71f8c37a051a29cdba11ea15cac3c252eeab533c7e9141431649a3a57a7dacc1fa697fdd360c139a35af181b7154574e7b87ade8da951d1894362082f80eb56d3775e729e930a097e72a7339e6e63719acc8166fd9c77c068cc75240a3b2149da8bcc24187addcfcc7330ad057b1d7a215380ea8e060b2a85330bc262c58e119672d846b87be7edf535d68a4bc2a643516df1c134401d96f0944d4d7ebe7a769ecdcfa90418486c9d62a9a4c46e232fa94221392f59a9c8df520b19e1214ed4ac70f54367b640924c48d2d3596056ff7424fc1734b98edc02dc67d8d72f6d10f44e8a08204f0308204ec308204e8308202d0a00302010202136b00086694d48d4b29943630f5000000086694300d06092a864886f70d01010b0500304f310b3009060355040613025553311e301c060355040a13154d6963726f736f667420436f72706f726174696f6e3120301e060355040313174d6963726f736f66742052534120544c53204341203031301e170d3231303230323139353831335a170d3232303230323139353831335a30353133303106035504030c2a4d6963726f736f66745f5253415f544c535f49737375696e675f43415f30315f4b657942696e64696e6730820122300d06092a864886f70d01010105000382010f003082010a0282010100b65a936febea1694e5de2b8dfc1997d265f3582b94f9be1fb56bb96e2191c5df170bb52d276c30c8fdc876f1e5b3d9b900571e17fd505534f56db0ab7953261a34911e9fb0340aac76c1baede9a580ee86eba49f0e3d7cddcc60d973c69afc157aaa5d2d6ede3cd7d9a265098ee932fde13049e0f1490b2bb88bd56b6e26033ad99f49f6b7366eb275e6550c6b74f1823ac6dcf86a843825ade03f670a7ce895c840a7cfca247bc94d608ee30feefa8346470bc69f0f2e847b5896b377d70fa20e99d3af06b2d8c286b512fad8070cdc33f3302f48ad02014a21de13d1a04fbdf6fca54cc7364e303a1b458d2093fb8e98f686c2d8da374e757f8ac25b2210e70203010001a381d63081d3301d0603551d0e041604149a0190a5b9942f43bc62113fcd3d404bead25250300e0603551d0f0101ff04040302078030130603551d25040c300a06082b06010505070309300f06092b060105050730010504020500301f0603551d23041830168014b5760c3011cec792424d4cc75c2cc8a90ce80b64303e06092b06010401823715070431302f06272b060104018237150887da867583eed90182c9851b81b59e6185f4eb60815d81cc9b4781c8e916020164020107301b06092b060104018237150a040e300c300a06082b06010505070309300d06092a864886f70d01010b0500038202010012d83b821ff2afc4d67c63cee2d9a1045c1a1f0628274e1da3ef03fcdc720d420423478090afe6cbbaf4c753fdcad04aef5ca919c96ab9b540a64cc23d24181e7016391e780ae56a0897a372ea9a93a959c0d713ae0cbd5e6ca420724a110ac0901d671ea8c57ba31db062a7df4bbc8cb78d820262f9ba12e4313edb85155f69c47a05fa6171958e6577b61910357a5940a3c3f186eb07a37968c7f17b5614603aae4e71cb2d5f122bbea187888452239cb9c0d338d913604034e4eb3be2639a15836d08b4b4f38287414e5cd144a23aa95edb59236205397263ead5b0ef1a2239f54149f9b5992a2964a28373652a1bb31a772a04c5d4eef2fd0e5853094590ccc5b1bcb9fc1910d31652cc8f2e72c685665834f3826613dd456655ae9c9f21283a1684123fa144bc3276f50ead086fd9c149b670b27804057472602a984a3de016f65bf0980baa8a0cbadd53b061800347fec63d80b0b68d164e295e682a890ae433c439ae04a31dd8b9260c81692a110e8583038e767ceab2b87db2067eeb1973aa5bbcd5f3b4fca071ca60361d9815e87c76c44e9791c7aa25defaaaa28d72c709ad434b44974ed50546b685e215c7a70065503f0014d5f9f1fdf851930af51e7c425d0ea0d966377f44d60bf6345a05d750d2de25ebb1957bdac56b1d9a3a4e556bf398e063062ea7e1400a279abb085c1fadb9e517231b5fdcb0d868c10c00016903001861040089499a5bf709647d1cd5e41d381c15ab96100c86f0d66d0ba53a224b2adb7897f63de0368a080e17e80da5f70505d58c5317cb047dfeeecc1c7e160fdbf4747c78fb2641b233ad509c12de3a83c3d9cab174c8ca3a748d43766a11eeaa3e8c080401006f041a8741e47e744c7b6b83abf44bc722ae7f1ca19e12989106c2a78a37c8713cac664d1d1dbff6a566b05f478f15123fb155850cafeb36120e9fb24ae4fc5f4c6e4614ebcaf1dab4a79405325d4774cef1c85facffdf57c182c7e22d29facb2ee7460b716aaa6b5e3235036d21a6212414f2d75fc85caa91317fcd0318c651f8459f32bfbda3f3b2e04c1f0c2f8982ea16d2df599133881106b27d53276703bc43230f0fdcadb8b1fe13101d1055a14d6cc6af8fa48d6dd23a0a36fb5d6ebb8f5021e3e20900b5de2442da9853d2446d75b1c2198d24cdc2a5a3d07a9aab451e196c6c49fce20bdb71a7190de2964afd934a7f14afb7872a49ab6a7a5cf2d30e000000'
[34m[1m>>> [0m
[34m[1m>>> [0mpkt = TLS(hex_bytes(data))
Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 219, in __call__
    obj.import_from_asn1pkt(pubkey)
  File "/home/scapy/scapy/layers/tls/cert.py", line 302, in import_from_asn1pkt
    self.fill_and_store(modulus=modulus, pubExp=pubExp)
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/scapy/scapy/layers/tls/cert.py", line 231, in __call__
    pubkey = RSAPublicKey(obj.der)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/asn1packet.py", line 55, in do_dissect
    return self.ASN1_root.dissect(self, x)
  File "/home/scapy/scapy/asn1fields.py", line 487, in dissect
    _, x = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 478, in m2i
    s = obj.dissect(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 197, in dissect
    v, s = self.m2i(pkt, s)
  File "/home/scapy/scapy/asn1fields.py", line 150, in m2i
    return codec.dec(s, context=self.context)  # type: ignore
  File "/home/scapy/scapy/asn1/ber.py", line 370, in dec
    return cls.do_dec(s, context, safe)
  File "/home/scapy/scapy/asn1/ber.py", line 439, in do_dec
    l, s, t = cls.check_type_check_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 328, in check_type_check_len
    l, s3 = cls.check_type_get_len(s)
  File "/home/scapy/scapy/asn1/ber.py", line 319, in check_type_get_len
    s2 = cls.check_type(s)
  File "/home/scapy/scapy/asn1/ber.py", line 310, in check_type
    raise BER_BadTag_Decoding_Error(
scapy.asn1.ber.BER_BadTag_Decoding_Error: BERcodec_INTEGER: Got tag [48/0x30] while expecting <ASN1Tag INTEGER[2]>
### Already decoded ###
None
### Remaining ###
b'0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\x00\x94\x87k\x95r\xb7\xc3\xd7\xfb\xb2\xd5i\xff\xffk\x8fqbE\xa2\xd9\xb4\x13\xc9\xe8#\x8e\xe8\x8d\x98\xb1\x00,\xec\x8c!\x98\xb5/;\x7f\ng\x9c\xeb\x1a\xeb,\x14g\xd2\xed\xa3\xc7\x1bK\xb0uk\xa4#T\xa9V\xb8\xd4\x0b\xd4"\x92\x17\x93\xb3\xde\xc0\xaa\xb3\xf5\xe0\xb0#\xbc\xb7\xdf\xdfH\xbdK\x06L\x1ab%^\x9bX\xc1j\xd4\x82\x08\x7f\xd1P[\x01\xaa\xd9GO\x06\x92_8!\xfb\xe9/h\x0e\x87\xdb?\n\xa1P\xe2\x06hH\xf8\x8e\xbe\x08\xd8(\x01\x85\xbb\xbai{9\xd1.\x03\xea\xe6\xd4\xe4\x811\x942\xf2u\'\x93\xfc\xd1%\xf2qL\xd9+7\xe3\xd9\xb8\xfc\xec\x7f\xd7\xb3\xc1!\xfd\xed\xc4+P\xffe\xf73R\xcb\xc1 *\xc5\x9c\x84m\xf2\xa9\x16\x8c\x00\xfcGT\xf5\xe1\x9c;\x05\x03\xdb\xe4\xf5\x8b\x0f\x8b>\x0f\xa4\x11\xd4\xdc\xb8\xe1\xac\xde\xf9\xa2\xca}\xb5.(*\x14\x11\x9e\x1e\xf3\xa8g\xa3\xb7\xd8\xfd\xac\xcc\'\xd3\xd2\x03;\xb5\x08*\x1bQ\x02\x03\x01\x00\x01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 857, in getfield
    lst.append((clen, Cert(m[3:3 + clen])))
  File "/home/scapy/scapy/layers/tls/cert.py", line 569, in __call__
    obj.import_from_asn1pkt(cert)
  File "/home/scapy/scapy/layers/tls/cert.py", line 615, in import_from_asn1pkt
    self.pubKey = PubKey(raw(tbsCert.subjectPublicKeyInfo))
  File "/home/scapy/scapy/layers/tls/cert.py", line 237, in __call__
    raise Exception("Unable to import public key")
Exception: Unable to import public key


######
## Decrypt packets from a pcap
######


###(079)=[failed] pcap file & external TLS Key Log file

[34m[1m>>> [0mbck_conf = conf
[34m[1m>>> [0mconf.tls_session_enable = True
[34m[1m>>> [0mconf.tls_nss_filename = scapy_path("doc/notebooks/tls/raw_data/tls_nss_example.keys.txt")
[34m[1m>>> [0m
[34m[1m>>> [0mpackets = rdpcap(scapy_path("doc/notebooks/tls/raw_data/tls_nss_example.pcap"))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/utils.py", line 1117, in rdpcap
    return fdesc.read_all(count=count)
  File "/home/scapy/scapy/utils.py", line 1385, in read_all
    res = self._read_all(count)
  File "/home/scapy/scapy/utils.py", line 1295, in _read_all
    p = self.read_packet()  # type: Packet
  File "/home/scapy/scapy/utils.py", line 1355, in read_packet
    p = self.LLcls(s)  # type: Packet
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/fields.py", line 1424, in getfield
    i = self.m2i(pkt, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 1277, in m2i
    if s.prcs and s.prcs.key_exchange:
AttributeError: 'writeConnState' object has no attribute 'key_exchange'


PACKET DISSECTION FAILED ON:
 Ether(hex_bytes('00000000000000000000000086dd6007e1a8007d06400000000000000000000000000000000100000000000000000000000000000001e2ec01bb2a509f2686c1778f80180200008500000101080add0f27d7dd0f27d616030300251000002120ecca4517f009a7f98794d965273ad09b86964fbd55e9a40fe083909359cf97401403030001011603030028ff7f6987e91f058f0de5bb64d8b1da6487d8a5b529af8ffa801b153d46ee8edd0b2aa980f70b9e0d'))

###(080)=[failed] pcapng file with a Decryption Secrets Block

[34m[1m>>> [0mimport shutil
[34m[1m>>> [0mif shutil.which("editcap"):
...     bck_conf = conf
...     key_log_path = scapy_path("doc/notebooks/tls/raw_data/tls_nss_example.keys.txt")
...     pcap_path = scapy_path("doc/notebooks/tls/raw_data/tls_nss_example.pcap")
...     pcapng_path = get_temp_file()
...     exit_status = os.system("editcap --inject-secrets tls,%s %s %s" % (key_log_path, pcap_path, pcapng_path))
...     assert(exit_status == 0)
...     packets = rdpcap(pcapng_path)
...     assert b"GET /secret.txt HTTP/1.0\n" in packets[11].msg[0].data
...     assert b"z2|gxarIKOxt,G1d>.Q2MzGY[k@" in packets[13].msg[0].data
...     conf = bck_conf
... 
Traceback (most recent call last):
  File "<input>", line 9, in <module>
  File "/home/scapy/scapy/utils.py", line 1117, in rdpcap
    return fdesc.read_all(count=count)
  File "/home/scapy/scapy/utils.py", line 1385, in read_all
    res = self._read_all(count)
  File "/home/scapy/scapy/utils.py", line 1295, in _read_all
    p = self.read_packet()  # type: Packet
  File "/home/scapy/scapy/utils.py", line 1684, in read_packet
    p = cls(s)  # type: Packet
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1007, in dissect
    self.do_dissect_payload(payl)
  File "/home/scapy/scapy/packet.py", line 982, in do_dissect_payload
    p = cls(s, _internal=1, _underlayer=self)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 163, in getfield
    p = self.m2i(pkt, remain)
  File "/home/scapy/scapy/layers/tls/record.py", line 121, in m2i
    return cls(m, tls_session=pkt.tls_session)
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/fields.py", line 1424, in getfield
    i = self.m2i(pkt, s)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 1277, in m2i
    if s.prcs and s.prcs.key_exchange:
AttributeError: 'writeConnState' object has no attribute 'key_exchange'


[32m
Tests for TLS 1.3
[0m━ Run at 12:49:01 from [test/tls13.uts] by UTscapy in 0.031170368194580078
[34m[1m └ Passed=7
[0m[31m[1m └ Failed=17
[0m
######
## Read a protected TLS 1.3 session
######


###(001)=[failed] Reading TLS 1.3 session - TLS parsing (no encryption) does not throw any error

[34m[1m>>> [0mfrom scapy.layers.tls.record import TLS
[34m[1m>>> [0mt1 = TLS(clientHello)
[34m[1m>>> [0mt2 = TLS(serverHello, tls_session=t1.tls_session.mirror())
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/base_classes.py", line 401, in __call__
    i.__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/record.py", line 311, in __init__
    super(TLS, self).__init__(*args, **kargs)
  File "/home/scapy/scapy/layers/tls/session.py", line 983, in __init__
    Packet.__init__(self, _pkt=_pkt, post_transform=post_transform,
  File "/home/scapy/scapy/packet.py", line 159, in __init__
    self.dissect(_pkt)
  File "/home/scapy/scapy/packet.py", line 1002, in dissect
    s = self.do_dissect(s)
  File "/home/scapy/scapy/packet.py", line 959, in do_dissect
    s, fval = f.getfield(self, s)
  File "/home/scapy/scapy/layers/tls/record.py", line 175, in getfield
    p.post_dissection_tls_session_update(raw_msg)
  File "/home/scapy/scapy/layers/tls/session.py", line 1007, in post_dissection_tls_session_update
    self.tls_session_update(msg_str)
  File "/home/scapy/scapy/layers/tls/handshake.py", line 676, in tls_session_update
    s.compute_tls13_early_secrets()
  File "/home/scapy/scapy/layers/tls/session.py", line 664, in compute_tls13_early_secrets
    if self.prcs and self.prcs.hkdf:
AttributeError: 'readConnState' object has no attribute 'hkdf'


###(006)=[failed] Reading TLS 1.3 session - ServerHello

[34m[1m>>> [0mfrom scapy.layers.tls.handshake import TLS13ServerHello
[34m[1m>>> [0mfrom scapy.layers.tls.extensions import TLS_Ext_SupportedVersion_SH
[34m[1m>>> [0mfrom scapy.layers.tls.keyexchange_tls13 import TLS_Ext_KeyShare_SH
[34m[1m>>> [0m
[34m[1m>>> [0massert(TLS13ServerHello in t2)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't2' is not defined


###(007)=[failed] Reading TLS 1.3 session - TLS parsing (with encryption) does not throw any error

[34m[1m>>> [0mfrom scapy.layers.tls.record_tls13 import TLS13
[34m[1m>>> [0mt3 = TLS13(serverEncHS, tls_session=t2.tls_session)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't2' is not defined


###(008)=[failed] Reading TLS 1.3 session - TLS13 Record header

[34m[1m>>> [0massert(t3.type == 0x17)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't3' is not defined


###(009)=[failed] Reading TLS 1.3 session - TLS13 Record __getitem__

[34m[1m>>> [0mTLS13 in t3
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't3' is not defined


###(010)=[failed] Reading TLS 1.3 session - TLS13 ApplicationData

[34m[1m>>> [0mfrom scapy.layers.tls.record_tls13 import TLSInnerPlaintext
[34m[1m>>> [0mTLSInnerPlaintext in t3
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 't3' is not defined


######
## Decrypt a TLS 1.3 session with a retry
######


###(033)=[failed] Decrypt a TLS 1.3 session with a retry - Parse ServerHelloRetryRequest

[34m[1m>>> [0mfrom scapy.layers.tls.keyexchange_tls13 import TLS_Ext_KeyShare_HRR
[34m[1m>>> [0mfrom scapy.layers.tls.extensions import TLS_Ext_Cookie
[34m[1m>>> [0mfrom cryptography.hazmat.backends import default_backend
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ModuleNotFoundError: No module named 'cryptography'


###(035)=[failed] Decrypt a TLS 1.3 session with a retry - Parse ServerHello

[34m[1m>>> [0mfrom cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateNumbers
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ModuleNotFoundError: No module named 'cryptography'


###(036)=[failed] Decrypt a TLS 1.3 session with a retry - Handshake traffic secret derivation

[34m[1m>>> [0mearly_secret = clean("""
...          33 ad 0a 1c 60 7e c0 3b 09 e6 cd 98 93 68 0c
...          e2 10 ad f3 00 aa 1f 26 60 e1 b2 2e 10 f1 70 f9 2a
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mecdhe_secret = clean("""
...          c1 42 ce 13 ca 11 b5 c2 23 36 52 e6 3a d3 d9 78
...          44 f1 62 1f bf b9 de 69 d5 47 dc 8f ed ea be b4
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mhandshake_secret = clean("""
...          ce 02 2e 5e 6e 81 e5 07 36 d7 73 f2 d3 ad fc
...          e8 22 0d 04 9b f5 10 f0 db fa c9 27 ef 42 43 b1 48
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mclient_handshake_traffic_secret = clean("""
...          15 8a a7 ab 88 55 07 35 82 b4 1d 67 4b 40
...          55 ca bc c5 34 72 8f 65 93 14 86 1b 4e 08 e2 01 15 66
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mserver_handshake_traffic_secret = clean("""
...          34 03 e7 81 e2 af 7b 65 08 da 28 57 4f 6e
...          95 a1 ab f1 62 de 83 a9 79 27 c3 76 72 a4 a0 ce f8 a1
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0massert(len(t.tls_session.tls13_derived_secrets) == 5)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(037)=[failed] Decrypt a TLS 1.3 session with a retry - Server handshake traffic key calculation

[34m[1m>>> [0mserver_hs_traffic_key = clean("""
...          46 46 bf ac 17 12 c4 26 cd 78 d8 a2 4a
...          8a 6f 6b
...    """)
[34m[1m>>> [0mserver_hs_traffic_iv = clean("""
...          c7 d3 95 c0 8d 62 f2 97 d1 37 68 ea
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0massert(t.tls_session.prcs.cipher.key == server_hs_traffic_key)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'NoneType' object has no attribute 'cipher'


###(038)=[failed] Decrypt a TLS 1.3 session with a retry - Decrypt and parse server handshake

[34m[1m>>> [0mserverEncHS = clean("""
...          17 03 03 02 96 99 be e2 0b af 5b 7f
...          c7 27 bf ab 62 23 92 8a 38 1e 6d 0c f9 c4 da 65 3f 9d 2a 7b 23
...          f7 de 11 cc e8 42 d5 cf 75 63 17 63 45 0f fb 8b 0c c1 d2 38 e6
...          58 af 7a 12 ad c8 62 43 11 4a b1 4a 1d a2 fa e4 26 21 ce 48 3f
...          b6 24 2e ab fa ad 52 56 6b 02 b3 1d 2e dd ed ef eb 80 e6 6a 99
...          00 d5 f9 73 b4 0c 4f df 74 71 9e cf 1b 68 d7 f9 c3 b6 ce b9 03
...          ca 13 dd 1b b8 f8 18 7a e3 34 17 e1 d1 52 52 2c 58 22 a1 a0 3a
...          d5 2c 83 8c 55 95 3d 61 02 22 87 4c ce 8e 17 90 b2 29 a2 aa 0b
...          53 c8 d3 77 ee 72 01 82 95 1d c6 18 1d c5 d9 0b d1 f0 10 5e d1
...          e8 4a a5 f7 59 57 c6 66 18 97 07 9e 5e a5 00 74 49 e3 19 7b dc
...          7c 9b ee ed dd ea fd d8 44 af a5 c3 15 ec fe 65 e5 76 af e9 09
...          81 28 80 62 0e c7 04 8b 42 d7 f5 c7 8d 76 f2 99 d6 d8 25 34 bd
...          d8 f5 12 fe bc 0e d3 81 4a ca 47 0c d8 00 0d 3e 1c b9 96 2b 05
...          2f bb 95 0d f6 83 a5 2c 2b a7 7e d3 71 3b 12 29 37 a6 e5 17 09
...          64 e2 ab 79 69 dc d9 80 b3 db 9b 45 8d a7 60 31 24 d6 dc 00 5e
...          4d 6e 04 b4 d0 c4 ba f3 27 5d b8 27 db ba 0a 6d b0 96 72 17 1f
...          c0 57 b3 85 1d 7e 02 68 41 e2 97 8f bd 23 46 bb ef dd 03 76 bb
...          11 08 fe 9a cc 92 18 9f 56 50 aa 5e 85 d8 e8 c7 b6 7a c5 10 db
...          a0 03 d3 d7 e1 63 50 bb 66 d4 50 13 ef d4 4c 9b 60 7c 0d 31 8c
...          4c 7d 1a 1f 5c bc 57 e2 06 11 80 4e 37 87 d7 b4 a4 b5 f0 8e d8
...          fd 70 bd ae ad e0 22 60 b1 2a b8 42 ef 69 0b 4a 3e e7 91 1e 84
...          1b 37 4e cd 5e bb bc 2a 54 d0 47 b6 00 33 6d d7 d0 c8 8b 4b c1
...          0e 58 ee 6c b6 56 de 72 47 fa 20 d8 e9 1d eb 84 62 86 08 cf 80
...          61 5b 62 e9 6c 14 91 c7 ac 37 55 eb 69 01 40 5d 34 74 fe 1a c7
...          9d 10 6a 0c ee 56 c2 57 7f c8 84 80 f9 6c b6 b8 c6 81 b7 b6 8b
...          53 c1 46 09 39 08 f3 50 88 81 75 bd fb 0b 1e 31 ad 61 e3 0b a0
...          ad fe 6d 22 3a a0 3c 07 83 b5 00 1a 57 58 7c 32 8a 9a fc fc fb
...          97 8d 1c d4 32 8f 7d 9d 60 53 0e 63 0b ef d9 6c 0c 81 6e e2 0b
...          01 00 76 8a e2 a6 df 51 fc 68 f1 72 74 0a 79 af 11 39 8e e3 be
...          12 52 49 1f a9 c6 93 47 9e 87 7f 94 ab 7c 5f 8c ad 48 02 03 e6
...          ab 7b 87 dd 71 e8 a0 72 91 13 df 17 f5 ee e8 6c e1 08 d1 d7 20
...          07 ec 1c d1 3c 85 a6 c1 49 62 1e 77 b7 d7 8d 80 5a 30 f0 be 03
...          0c 31 5e 54
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mserver_finished = clean("""
...          88 63 e6 bf b0 42 0a 92 7f a2 7f 34 33 6a
...          70 ae 42 6e 96 8e 3e b8 84 94 5b 96 85 6d ba 39 76 d1
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mt = TLS13(serverEncHS, tls_session=t.tls_session)
[34m[1m>>> [0massert(t.deciphered_len == 646)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(039)=[failed] Decrypt a TLS 1.3 session with a retry - Client handshake traffic key calculation

[34m[1m>>> [0mclient_hs_traffic_key = clean("""
...          2f 1f 91 86 63 d5 90 e7 42 11 49 a2 9d
...          94 b0 b6
...    """)
[34m[1m>>> [0mclient_hs_traffic_iv = clean("""
...          41 4d 54 85 23 5e 1a 68 87 93 bd 74
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0massert(t.tls_session.pwcs.cipher.key == client_hs_traffic_key)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AttributeError: 'NoneType' object has no attribute 'cipher'


###(040)=[failed] Decrypt a TLS 1.3 session with a retry - Decrypt and parse client finished

[34m[1m>>> [0mclientFinished = clean("""
...          23 f5 2f db 07 09 a5 5b d7 f7 9b 99 1f 25
...          48 40 87 bc fd 4d 43 80 b1 23 26 a5 2a 28 b2 e3 68 e1
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mclientEncHS = clean("""
...          17 03 03 00 35 d7 4f 19 23 c6 62 fd
...          34 13 7c 6f 50 2f 3d d2 b9 3d 95 1d 1b 3b c9 7e 42 af e2 3c 31
...          ab ea 92 fe 91 b4 74 99 9e 85 e3 b7 91 ce 25 2f e8 c3 e9 f9 39
...          a4 12 0c b2
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mt = TLS13(clientEncHS, tls_session=t.tls_session.mirror())
[34m[1m>>> [0massert(t.deciphered_len == 37)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(041)=[failed] Decrypt a TLS 1.3 session with a retry - Application traffic secret derivation

[34m[1m>>> [0mmaster_secret = clean("""
...          11 31 54 5d 0b af 79 dd ce 9b 87 f0 69 45 78
...          1a 57 dd 18 ef 37 8d cd 20 60 f8 f9 a5 69 02 7e d8
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mclient_application_traffic_secret_0 = clean("""
...          75 ec f4 b9 72 52 5a a0 dc d0 57 c9 94 4d
...          4c d5 d8 26 71 d8 84 31 41 d7 dc 2a 4f f1 5a 21 dc 51
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mserver_application_traffic_secret_0 = clean("""
...          5c 74 f8 7d f0 42 25 db 0f 82 09 c9 de 64
...          29 e4 94 35 fd ef a7 ca d6 18 64 87 4d 12 f3 1c fc 8d
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mexporter_master_secret = clean("""
...       7c 06 d3 ae 10 6a 3a 37 4a ce 48 37 b3 98
...       5c ac 67 78 0a 6e 2c 5c 04 b5 83 19 d5 84 df 09 d2 23
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mresumption_master_secret = clean("""
...       09 17 0c 6d 47 27 21 56 6f 9c f9 9b 08 69
...       9d af f5 61 ec 8f b2 2d 5a 32 c3 f9 4c e0 09 b6 99 75
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0m
[34m[1m>>> [0massert(t.tls_session.tls13_master_secret is not None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(042)=[failed] Decrypt a TLS 1.3 session with a retry - Application traffic keys calculation

[34m[1m>>> [0mclient_ap_traffic_key = clean("""
...          a7 eb 2a 05 25 eb 43 31 d5 8f cb f9 f7
...          ca 2e 9c
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mclient_ap_traffic_iv = clean("""
...          86 e8 be 22 7c 1b d2 b3 e3 9c b4 44
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mserver_ap_traffic_key = clean("""
...          f2 7a 5d 97 bd 25 55 0c 48 23 b0 f3 e5
...          d2 93 88
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mserver_ap_traffic_iv = clean("""
...          0d d6 31 f7 b7 1c bb c7 97 c3 5f e7
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0massert(t.tls_session.rcs.cipher.key == client_ap_traffic_key)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(043)=[failed] Decrypt a TLS 1.3 session with a retry - Decrypt and parse client Alert

[34m[1m>>> [0mclientEncAlert = clean("""
...          17 03 03 00 13 2e a6 cd f7 49 19 60
...          23 e2 b3 a4 94 91 69 55 36 42 60 47
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mt = TLS13(clientEncAlert, tls_session = t.tls_session)
[34m[1m>>> [0massert(t.deciphered_len == 3)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


###(044)=[failed] Decrypt a TLS 1.3 session with a retry - Decrypt and parse server Alert

[34m[1m>>> [0mserverEncAlert = clean("""
...          17 03 03 00 13 51 9f c5 07 5c b0 88
...          43 49 75 9f f9 ef 6f 01 1b b4 c6 f2
...    """)
[34m[1m>>> [0m
[34m[1m>>> [0mt = TLS13(serverEncAlert, tls_session = t.tls_session.mirror())
[34m[1m>>> [0massert(t.deciphered_len == 3)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


[32m
tuntap tests for Scapy
[0m━ Run at 12:49:01 from [test/tuntap.uts] by UTscapy in 0.002244710922241211
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
Tests for generic ASN.1 encoding
[0m━ Run at 12:49:01 from [test/scapy/layers/asn1.uts] by UTscapy in 0.010427713394165039
[34m[1m └ Passed=35
[0m └ Failed=0

[32m
Scapy Bluetooth layer tests
[0m━ Run at 12:49:01 from [test/scapy/layers/bluetooth.uts] by UTscapy in 0.05606698989868164
[34m[1m └ Passed=23
[0m └ Failed=0

[32m
Regression tests for the bluetooth4LE layer
[0m━ Run at 12:49:01 from [test/scapy/layers/bluetooth4LE.uts] by UTscapy in 0.038136959075927734
[34m[1m └ Passed=37
[0m └ Failed=0

[32m
Regression tests for the CAN layer
[0m━ Run at 12:49:03 from [test/scapy/layers/can.uts] by UTscapy in 1.3334782123565674
[34m[1m └ Passed=67
[0m └ Failed=0

[32m
DHCP regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/dhcp.uts] by UTscapy in 0.00792384147644043
[34m[1m └ Passed=5
[0m[31m[1m └ Failed=1
[0m
######
## DHCP
######


###(005)=[failed] Check that the dhcpd alias is properly defined and documented

[34m[1m>>> [0massert dhcpd
[34m[1m>>> [0mimport IPython
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ModuleNotFoundError: No module named 'IPython'


[32m
DHCPv6 regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/dhcp6.uts] by UTscapy in 0.09549307823181152
[34m[1m └ Passed=318
[0m └ Failed=0

[32m
DNS regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/dns.uts] by UTscapy in 0.030588150024414062
[34m[1m └ Passed=17
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:03 from [test/scapy/layers/dns_dnssec.uts] by UTscapy in 0.01039576530456543
[34m[1m └ Passed=30
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:03 from [test/scapy/layers/dns_edns0.uts] by UTscapy in 0.003367185592651367
[34m[1m └ Passed=10
[0m └ Failed=0

[32m
Dot11 regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/dot11.uts] by UTscapy in 0.07982158660888672
[34m[1m └ Passed=45
[0m[31m[1m └ Failed=2
[0m
######
## 802.11
######


###(009)=[failed] Dot11WEP - build

[34m[1m>>> [0mconf.wepkey = ""
[34m[1m>>> [0massert raw(PPI()/Dot11(FCfield=0x40)/Dot11WEP()) == b'\x00\x00\x08\x00i\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/compat.py", line 291, in raw
    return bytes(x)
  File "/home/scapy/scapy/packet.py", line 562, in __bytes__
    return self.build()
  File "/home/scapy/scapy/packet.py", line 703, in build
    p = self.do_build()
  File "/home/scapy/scapy/packet.py", line 686, in do_build
    pay = self.do_build_payload()
  File "/home/scapy/scapy/packet.py", line 672, in do_build_payload
    return self.payload.do_build()
  File "/home/scapy/scapy/packet.py", line 686, in do_build
    pay = self.do_build_payload()
  File "/home/scapy/scapy/packet.py", line 672, in do_build_payload
    return self.payload.do_build()
  File "/home/scapy/scapy/packet.py", line 688, in do_build
    return self.post_build(pkt, pay)
  File "/home/scapy/scapy/layers/dot11.py", line 1569, in post_build
    p = self.encrypt(p, raw(pay))
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


###(033)=[failed] WEP tests

[34m[1m>>> [0mconf.wepkey = ""
[34m[1m>>> [0mbck_conf_crypto_valid = conf.crypto_valid
[34m[1m>>> [0mp = Dot11WEP(b'\x00\x00\x00\x00\xe3OjYLw\xc3x_%\xd0\xcf\xdeu-\xc3pH#\x1eK\xae\xf5\xde\xe7\xb8\x1d,\xa1\xfe\xe83\xca\xe1\xfe\xbd\xfe\xec\x00)T`\xde.\x93Td\x95C\x0f\x07\xdd')
[34m[1m>>> [0massert isinstance(p, Dot11WEP)
[34m[1m>>> [0mconf.crypto_valid = bck_conf_crypto_valid
[34m[1m>>> [0m
[34m[1m>>> [0mconf.wepkey = "Fobar"
[34m[1m>>> [0mr = raw(Dot11WEP()/LLC()/SNAP()/IP()/TCP(seq=12345678))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/compat.py", line 291, in raw
    return bytes(x)
  File "/home/scapy/scapy/packet.py", line 562, in __bytes__
    return self.build()
  File "/home/scapy/scapy/packet.py", line 703, in build
    p = self.do_build()
  File "/home/scapy/scapy/packet.py", line 688, in do_build
    return self.post_build(pkt, pay)
  File "/home/scapy/scapy/layers/dot11.py", line 1569, in post_build
    p = self.encrypt(p, raw(pay))
  File "/home/scapy/scapy/config.py", line 917, in func_in
    raise ImportError("Cannot execute crypto-related method! "
ImportError: Cannot execute crypto-related method! Please install python-cryptography v1.7 or later.


[32m
Regression tests for the Dot15D4, SixLoWPAN and Zigbee layers
[0m━ Run at 12:49:03 from [test/scapy/layers/dot15d4.uts] by UTscapy in 0.11149954795837402
[34m[1m └ Passed=59
[0m └ Failed=0

[32m
EAP regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/eap.uts] by UTscapy in 0.024654150009155273
[34m[1m └ Passed=40
[0m └ Failed=0

[32m
HSRP regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/hsrp.uts] by UTscapy in 0.0013816356658935547
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
HTTP regression tests for Scapy
[0m━ Run at 12:49:03 from [test/scapy/layers/http.uts] by UTscapy in 0.07035303115844727
[34m[1m └ Passed=7
[0m[31m[1m └ Failed=2
[0m
######
## HTTP
######


###(003)=[failed] HTTP decompression (brotli)

[34m[1m>>> [0mconf.debug_dissector = True
[34m[1m>>> [0mload_layer("http")
[34m[1m>>> [0m
[34m[1m>>> [0mimport os
[34m[1m>>> [0mimport brotli
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ModuleNotFoundError: No module named 'brotli'


###(004)=[failed] HTTP decompression (zstd)

[34m[1m>>> [0mconf.debug_dissector = True
[34m[1m>>> [0mload_layer("http")
[34m[1m>>> [0m
[34m[1m>>> [0mimport os
[34m[1m>>> [0mimport zstandard
Traceback (most recent call last):
  File "<input>", line 2, in <module>
ModuleNotFoundError: No module named 'zstandard'


[32m
Scapy IPv4 layers tests
[0m━ Run at 12:49:03 from [test/scapy/layers/inet.uts] by UTscapy in 0.12283849716186523
[34m[1m └ Passed=44
[0m └ Failed=0

[32m
Scapy IPv6 layers tests
[0m━ Run at 12:49:04 from [test/scapy/layers/inet6.uts] by UTscapy in 0.38068532943725586
[34m[1m └ Passed=499
[0m └ Failed=0

[32m
IPsec layer regression tests
[0m━ Run at 12:49:04 from [test/scapy/layers/ipsec.uts] by UTscapy in 0.16904282569885254
[34m[1m └ Passed=4
[0m[31m[1m └ Failed=100
[0m
######
## IPv4 / ESP - Transport - Encryption Algorithms
######


###(001)=[failed] IPv4 / ESP - Transport - DES - NULL
 the encrypted packet should have an ESP layer
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='DES', crypt_key=b'8bytekey',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'DES', try ['NULL']


###(002)=[failed] IPv4 / ESP - Transport - 3DES - NULL
 the encrypted packet should have an ESP layer
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='3DES', crypt_key=b'threedifferent8byteskeys',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo '3DES', try ['NULL']


###(003)=[failed] IPv4 / ESP - Transport - AES-CBC - NULL
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(004)=[failed] IPv4 / ESP - Transport - AES-CTR - NULL
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CTR', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CTR', try ['NULL']


###(005)=[failed] IPv4 / ESP - Transport - Blowfish - NULL
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='Blowfish', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'Blowfish', try ['NULL']


###(006)=[failed] IPv4 / ESP - Transport - CAST - NULL
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='CAST', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'CAST', try ['NULL']


######
## IPv4 / ESP - Tunnel - Encryption Algorithms
######


###(008)=[failed] IPv4 / ESP - Tunnel - DES - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 the encrypted packet should have an ESP layer
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='DES', crypt_key=b'8bytekey',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'DES', try ['NULL']


###(009)=[failed] IPv4 / ESP - Tunnel - 3DES - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 the encrypted packet should have an ESP layer
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='3DES', crypt_key=b'threedifferent8byteskeys',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo '3DES', try ['NULL']


###(010)=[failed] IPv4 / ESP - Tunnel - AES-CBC - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(011)=[failed] IPv4 / ESP - Tunnel - AES-CTR - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CTR', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CTR', try ['NULL']


###(012)=[failed] IPv4 / ESP - Tunnel - Blowfish - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='Blowfish', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'Blowfish', try ['NULL']


###(013)=[failed] IPv4 / ESP - Tunnel - CAST - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='CAST', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'CAST', try ['NULL']


######
## IPv4 / ESP - Transport - Authentication Algorithms
######


###(014)=[failed] IPv4 / ESP - Transport - NULL - HMAC-SHA1-96
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(015)=[failed] IPv4 / ESP - Transport - NULL - HMAC-SHA1-96 - altered packet
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(016)=[failed] IPv4 / ESP - Transport - NULL - SHA2-256-128
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(017)=[failed] IPv4 / ESP - Transport - NULL - SHA2-256-128 - altered packet
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(018)=[failed] IPv4 / ESP - Transport - NULL - SHA2-384-192
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(019)=[failed] IPv4 / ESP - Transport - NULL - SHA2-384-192 - altered packet
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(020)=[failed] IPv4 / ESP - Transport - NULL - SHA2-512-256
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(021)=[failed] IPv4 / ESP - Transport - NULL - SHA2-512-256 - altered packet
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(022)=[failed] IPv4 / ESP - Transport - NULL - HMAC-MD5-96
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(023)=[failed] IPv4 / ESP - Transport - NULL - HMAC-MD5-96 - altered packet
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(024)=[failed] IPv4 / ESP - Transport - NULL - AES-CMAC-96
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(025)=[failed] IPv4 / ESP - Transport - NULL - AES-CMAC-96 - altered packet
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


######
## IPv4 / ESP - Tunnel - Authentication Algorithms
######


###(026)=[failed] IPv4 / ESP - Tunnel - NULL - HMAC-SHA1-96
 after encryption packet should be encapsulated with the given ip tunnel header
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(027)=[failed] IPv4 / ESP - Tunnel - NULL - HMAC-SHA1-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(028)=[failed] IPv4 / ESP - Tunnel - NULL - SHA2-256-128
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(029)=[failed] IPv4 / ESP - Tunnel - NULL - SHA2-256-128 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(030)=[failed] IPv4 / ESP - Tunnel - NULL - SHA2-384-192
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(031)=[failed] IPv4 / ESP - Tunnel - NULL - SHA2-384-192 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(032)=[failed] IPv4 / ESP - Tunnel - NULL - SHA2-512-256
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(033)=[failed] IPv4 / ESP - Tunnel - NULL - SHA2-512-256 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(034)=[failed] IPv4 / ESP - Tunnel - NULL - HMAC-MD5-96
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(035)=[failed] IPv4 / ESP - Tunnel - NULL - HMAC-MD5-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(036)=[failed] IPv4 / ESP - Tunnel - NULL - AES-CMAC-96
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 integrity verification should pass
 after decryption the original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(037)=[failed] IPv4 / ESP - Tunnel - NULL - AES-CMAC-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


######
## IPv4 / ESP - Encryption + Authentication
######


###(038)=[failed] IPv4 / ESP - Transport - AES-CBC - HMAC-SHA1-96
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(039)=[failed] IPv4 / ESP - Transport - AES-CBC - HMAC-SHA1-96 - altered packet
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(040)=[failed] IPv4 / ESP - Transport - AES-GCM - NULL
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(041)=[failed] IPv4 / ESP - Transport - AES-GCM - NULL -- ESN
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved
 Check for ICMP layer in decrypted reference

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None, esn_en = True, esn = 0x1)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(042)=[failed] IPv4 / ESP - Transport - AES-GCM - NULL - altered packet
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(043)=[failed] IPv4 / ESP - Transport - AES-GCM - NULL - altered packet -- ESN
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None, esn_en = True, esn = 0x200)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(046)=[failed] IPv4 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(047)=[failed] IPv4 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(048)=[failed] IPv4 / ESP - Tunnel - AES-GCM - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(049)=[failed] IPv4 / ESP - Tunnel - AES-GCM - NULL -- ESN
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'), esn_en = True, esn = 0x2)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(050)=[failed] IPv4 / ESP - Tunnel - AES-GCM - NULL - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(051)=[failed] IPv4 / ESP - Tunnel - AES-GCM - NULL - altered packet - ESN
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'), esn_en = True, esn = 0x2)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


######
## IPv4 / AH - Transport
######


###(054)=[failed] IPv4 / AH - Transport - HMAC-SHA1-96
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'sixteenbytes key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(055)=[failed] IPv4 / AH - Transport - HMAC-SHA1-96 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'sixteenbytes key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(056)=[failed] IPv4 / AH - Transport - SHA2-256-128
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(057)=[failed] IPv4 / AH - Transport - SHA2-256-128 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(058)=[failed] IPv4 / AH - Transport - SHA2-384-192
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(059)=[failed] IPv4 / AH - Transport - SHA2-384-192 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(060)=[failed] IPv4 / AH - Transport - SHA2-512-256
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(061)=[failed] IPv4 / AH - Transport - SHA2-512-256 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(062)=[failed] IPv4 / AH - Transport - HMAC-MD5-96
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(063)=[failed] IPv4 / AH - Transport - HMAC-MD5-96 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(064)=[failed] IPv4 / AH - Transport - AES-CMAC-96
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(065)=[failed] IPv4 / AH - Transport - AES-CMAC-96 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(066)=[failed] IPv4 / AH - Transport - AES-CMAC-96 -- ESN
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          esn_en=True, esn=0x200)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(067)=[failed] IPv4 / AH - Transport - AES-CMAC-96 - altered packet -- ESN
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          esn_en=True, esn=0x200)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


######
## IPv4 / AH - Tunnel
######


###(068)=[failed] IPv4 / AH - Tunnel - HMAC-SHA1-96
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(069)=[failed] IPv4 / AH - Tunnel - HMAC-SHA1-96 - altered packet
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(070)=[failed] IPv4 / AH - Tunnel - SHA2-256-128
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(071)=[failed] IPv4 / AH - Tunnel - SHA2-256-128 - altered packet
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(072)=[failed] IPv4 / AH - Tunnel - SHA2-384-192
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(073)=[failed] IPv4 / AH - Tunnel - SHA2-384-192 - altered packet
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-384-192', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-384-192', try ['NULL']


###(074)=[failed] IPv4 / AH - Tunnel - SHA2-512-256
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(075)=[failed] IPv4 / AH - Tunnel - SHA2-512-256 - altered packet
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-512-256', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-512-256', try ['NULL']


###(076)=[failed] IPv4 / AH - Tunnel - HMAC-MD5-96
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(077)=[failed] IPv4 / AH - Tunnel - HMAC-MD5-96 - altered packet
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-MD5-96', auth_key=b'secret key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-MD5-96', try ['NULL']


###(078)=[failed] IPv4 / AH - Tunnel - AES-CMAC-96
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(079)=[failed] IPv4 / AH - Tunnel - AES-CMAC-96 - altered packet
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(080)=[failed] IPv4 / AH - Tunnel - AES-CMAC-96 -- ESN
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet should be unaltered

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'),
...                          esn_en=True, esn=0x200)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


###(081)=[failed] IPv4 / AH - Tunnel - AES-CMAC-96 - altered packet -- ESN
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IP(src='1.1.1.1', dst='2.2.2.2')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IP(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIP[0m  [34mversion[0m[0m=[0m[35m4[0m [34mihl[0m[0m=[0m[35m5[0m [34mtos[0m[0m=[0m[35m0x0[0m [34mlen[0m[0m=[0m[35m48[0m [34mid[0m[0m=[0m[35m1[0m [34mflags[0m[0m=[0m[35m[0m [34mfrag[0m[0m=[0m[35m0[0m [34mttl[0m[0m=[0m[35m64[0m [34mproto[0m[0m=[0m[35mtcp[0m [34mchksum[0m[0m=[0m[35m0x74c2[0m [34m[4m[1msrc[0m[0m=[0m[35m[4m[1m1.1.1.1[0m [34m[4m[1mdst[0m[0m=[0m[35m[4m[1m2.2.2.2[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1914[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='AES-CMAC-96', auth_key=b'sixteenbytes key',
...                          tunnel_header=IP(src='11.11.11.11', dst='22.22.22.22'),
...                          esn_en=True, esn=0x200)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'AES-CMAC-96', try ['NULL']


######
## IPv6 / ESP
######


###(083)=[failed] IPv6 / ESP - Transport - AES-CBC - NULL
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(084)=[failed] IPv6 / ESP - Transport - NULL - HMAC-SHA1-96
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(085)=[failed] IPv6 / ESP - Transport - NULL - HMAC-SHA1-96 - altered packet
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(086)=[failed] IPv6 / ESP - Transport - AES-CBC - HMAC-SHA1-96
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(087)=[failed] IPv6 / ESP - Transport - AES-CBC - HMAC-SHA1-96 - altered packet
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(088)=[failed] IPv6 / ESP - Transport - AES-GCM - NULL
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(089)=[failed] IPv6 / ESP - Transport - AES-GCM - NULL - altered packet
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None)
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(093)=[failed] IPv6 / ESP - Tunnel - AES-CBC - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(094)=[failed] IPv6 / ESP - Tunnel - NULL - HMAC-SHA1-96
 after encryption packet should be encapsulated with the given ip tunnel header
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(095)=[failed] IPv6 / ESP - Tunnel - NULL - HMAC-SHA1-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='NULL', crypt_key=None,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(096)=[failed] IPv6 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(097)=[failed] IPv6 / ESP - Tunnel - AES-CBC - HMAC-SHA1-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-CBC', crypt_key=b'sixteenbytes key',
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-CBC', try ['NULL']


###(098)=[failed] IPv6 / ESP - Tunnel - AES-GCM - NULL
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 after decryption original packet should be preserved

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


###(099)=[failed] IPv6 / ESP - Tunnel - AES-GCM - NULL - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 after encryption the original packet payload should NOT be readable
 simulate the alteration of the packet before decryption
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(ESP, spi=0x222,
...                          crypt_algo='AES-GCM', crypt_key=b'16bytekey+4bytenonce',
...                          auth_algo='NULL', auth_key=None,
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 845, in __init__
    raise TypeError('unsupported encryption algo %r, try %r' %
TypeError: unsupported encryption algo 'AES-GCM', try ['NULL']


######
## IPv6 / AH
######


###(102)=[failed] IPv6 / AH - Transport - HMAC-SHA1-96
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(103)=[failed] IPv6 / AH - Transport - HMAC-SHA1-96 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(104)=[failed] IPv6 / AH - Transport - SHA2-256-128
 the encrypted packet should have an AH layer
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(105)=[failed] IPv6 / AH - Transport - SHA2-256-128 - altered packet
 the encrypted packet should have an AH layer
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(106)=[failed] IPv6 / AH - Tunnel - HMAC-SHA1-96
 after encryption packet should be encapsulated with the given ip tunnel header
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(107)=[failed] IPv6 / AH - Tunnel - HMAC-SHA1-96 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(108)=[failed] IPv6 / AH - Tunnel - SHA2-256-128
 after encryption packet should be encapsulated with the given ip tunnel header
 alter mutable fields in the packet
 integrity verification should pass
 after decryption the original packet payload should be unaltered

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


###(109)=[failed] IPv6 / AH - Tunnel - SHA2-256-128 - altered packet
 after encryption packet should be encapsulated with the given ip tunnel header
 simulate the alteration of the packet before verification
 integrity verification should fail

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m28[0m [34mnh[0m[0m=[0m[35mTCP[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='SHA2-256-128', auth_key=b'secret key',
...                          tunnel_header=IPv6(src='aa::bb', dst='bb::aa'))
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'SHA2-256-128', try ['NULL']


######
## IPv6 + Extensions / AH
######


###(110)=[failed] IPv6 + Extensions / AH - Transport
 AH header should be inserted between the routing header and the dest options header

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= IPv6ExtHdrHopByHop()
[34m[1m>>> [0mp /= IPv6ExtHdrDestOpt()
[34m[1m>>> [0mp /= IPv6ExtHdrRouting()
[34m[1m>>> [0mp /= IPv6ExtHdrDestOpt()
[34m[1m>>> [0mp /= IPv6ExtHdrFragment()
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m68[0m [34mnh[0m[0m=[0m[35mHop-by-Hop Option Header[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrHopByHop[0m  [34mnh[0m[0m=[0m[35mDestination Option Header[0m [34mlen[0m[0m=[0m[35m0[0m [34mautopad[0m[0m=[0m[35mOn[0m [34moptions[0m[0m=[0m[35m[[0m<[0m[31m[1mPadN[0m  [34motype[0m[0m=[0m[35mPadN [00: skip, 0: Don't change en-route][0m [34moptlen[0m[0m=[0m[35m4[0m [34moptdata[0m[0m=[0m[35m'\x00\x00\x00\x00'[0m [0m|[0m[0m>[0m][0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrDestOpt[0m  [34mnh[0m[0m=[0m[35mRouting Header[0m [34mlen[0m[0m=[0m[35m0[0m [34mautopad[0m[0m=[0m[35mOn[0m [34moptions[0m[0m=[0m[35m[[0m<[0m[31m[1mPadN[0m  [34motype[0m[0m=[0m[35mPadN [00: skip, 0: Don't change en-route][0m [34moptlen[0m[0m=[0m[35m4[0m [34moptdata[0m[0m=[0m[35m'\x00\x00\x00\x00'[0m [0m|[0m[0m>[0m][0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrRouting[0m  [34mnh[0m[0m=[0m[35mDestination Option Header[0m [34mlen[0m[0m=[0m[35m0[0m [34mtype[0m[0m=[0m[35m0[0m [34msegleft[0m[0m=[0m[35m0[0m [34mreserved[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrDestOpt[0m  [34mnh[0m[0m=[0m[35mFragment Header[0m [34mlen[0m[0m=[0m[35m0[0m [34mautopad[0m[0m=[0m[35mOn[0m [34moptions[0m[0m=[0m[35m[[0m<[0m[31m[1mPadN[0m  [34motype[0m[0m=[0m[35mPadN [00: skip, 0: Don't change en-route][0m [34moptlen[0m[0m=[0m[35m4[0m [34moptdata[0m[0m=[0m[35m'\x00\x00\x00\x00'[0m [0m|[0m[0m>[0m][0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrFragment[0m  [34mnh[0m[0m=[0m[35mTCP[0m [34mres1[0m[0m=[0m[35m0[0m [34moffset[0m[0m=[0m[35m0[0m [34mres2[0m[0m=[0m[35m0[0m [34mm[0m[0m=[0m[35m0[0m [34mid[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1eb4[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


###(111)=[failed] IPv6 + Routing Header / AH - Transport
 AH header should be inserted between the routing header and TCP
 reorder the routing header as the receiver will get it
 integrity verification should pass

[34m[1m>>> [0mp = IPv6(src='11::22', dst='22::11')
[34m[1m>>> [0mp /= IPv6ExtHdrHopByHop()
[34m[1m>>> [0mp /= IPv6ExtHdrRouting(addresses=['aa::bb', 'cc::dd', 'ee::ff'])
[34m[1m>>> [0mp /= TCP(sport=45012, dport=80)
[34m[1m>>> [0mp /= Raw('testdata')
[34m[1m>>> [0mp = IPv6(raw(p))
[34m[1m>>> [0mp
[0m<[0m[31m[1mIPv6[0m  [34mversion[0m[0m=[0m[35m6[0m [34mtc[0m[0m=[0m[35m0[0m [34mfl[0m[0m=[0m[35m0[0m [34mplen[0m[0m=[0m[35m92[0m [34mnh[0m[0m=[0m[35mHop-by-Hop Option Header[0m [34mhlim[0m[0m=[0m[35m64[0m [34msrc[0m[0m=[0m[35m11::22[0m [34mdst[0m[0m=[0m[35m22::11[0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrHopByHop[0m  [34mnh[0m[0m=[0m[35mRouting Header[0m [34mlen[0m[0m=[0m[35m0[0m [34mautopad[0m[0m=[0m[35mOn[0m [34moptions[0m[0m=[0m[35m[[0m<[0m[31m[1mPadN[0m  [34motype[0m[0m=[0m[35mPadN [00: skip, 0: Don't change en-route][0m [34moptlen[0m[0m=[0m[35m4[0m [34moptdata[0m[0m=[0m[35m'\x00\x00\x00\x00'[0m [0m|[0m[0m>[0m][0m [0m|[0m[0m<[0m[31m[1mIPv6ExtHdrRouting[0m  [34mnh[0m[0m=[0m[35mTCP[0m [34mlen[0m[0m=[0m[35m6[0m [34mtype[0m[0m=[0m[35m0[0m [34msegleft[0m[0m=[0m[35m3[0m [34mreserved[0m[0m=[0m[35m0[0m [34maddresses[0m[0m=[0m[35m[ aa::bb, cc::dd, ee::ff ][0m [0m|[0m[0m<[0m[31m[1mTCP[0m  [34msport[0m[0m=[0m[35m45012[0m [34mdport[0m[0m=[0m[35mhttp[0m [34mseq[0m[0m=[0m[35m0[0m [34mack[0m[0m=[0m[35m0[0m [34mdataofs[0m[0m=[0m[35m5[0m [34mreserved[0m[0m=[0m[35m0[0m [34mflags[0m[0m=[0m[35mS[0m [34mwindow[0m[0m=[0m[35m8192[0m [34mchksum[0m[0m=[0m[35m0x1cfa[0m [34murgptr[0m[0m=[0m[35m0[0m [0m|[0m[0m<[0m[31m[1mHTTP[0m  [0m|[0m[0m<[0m[31m[1mRaw[0m  [34mload[0m[0m=[0m[35m'testdata'[0m [0m|[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m[0m>[0m
[34m[1m>>> [0m
[34m[1m>>> [0msa = SecurityAssociation(AH, spi=0x222,
...                          auth_algo='HMAC-SHA1-96', auth_key=b'secret key')
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/layers/ipsec.py", line 864, in __init__
    raise TypeError('unsupported integrity algo %r, try %r' %
TypeError: unsupported integrity algo 'HMAC-SHA1-96', try ['NULL']


[32m
Scapy ISAKMP layer tests
[0m━ Run at 12:49:04 from [test/scapy/layers/isakmp.uts] by UTscapy in 0.006216526031494141
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Layer 2 regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/l2.uts] by UTscapy in 0.006150722503662109
[34m[1m └ Passed=6
[0m[31m[1m └ Failed=1
[0m
######
## Layer 2 Unit Tests
######


###(001)=[failed] Test ARPingResult output

[34m[1m>>> [0mar = ARPingResult([(None, Ether(src='70:ee:50:50:ee:70')/ARP(psrc='192.168.0.1'))])
[34m[1m>>> [0mwith ContextManagerCaptureOutput() as cmco:
...     ar.show()
...     result_ar = cmco.get_output()
... 
[34m[1m>>> [0massert result_ar.startswith("  70:ee:50:50:ee:70 Netatmo 192.168.0.1")
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError


[32m
L2TP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/l2tp.uts] by UTscapy in 0.0012984275817871094
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
LDAP TESTS
[0m━ Run at 12:49:04 from [test/scapy/layers/ldap.uts] by UTscapy in 0.036200761795043945
[34m[1m └ Passed=8
[0m └ Failed=0

[32m
LLMNR regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/llmnr.uts] by UTscapy in 0.0028238296508789062
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
LLTD regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/lltd.uts] by UTscapy in 0.02252793312072754
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
MGCP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/mgcp.uts] by UTscapy in 0.0013036727905273438
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
Mobile IP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/mobileip.uts] by UTscapy in 0.0012812614440917969
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
NETBIOS regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/netbios.uts] by UTscapy in 0.00635981559753418
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
NetFlow regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/netflow.uts] by UTscapy in 0.0569760799407959
[34m[1m └ Passed=12
[0m └ Failed=0

[32m
NTP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/ntp.uts] by UTscapy in 0.05884814262390137
[34m[1m └ Passed=73
[0m └ Failed=0

[32m
Regression tests for the PFLog layer
[0m━ Run at 12:49:04 from [test/scapy/layers/pflog.uts] by UTscapy in 0.009002923965454102
[34m[1m └ Passed=9
[0m └ Failed=0

[32m
Scapy PPP layer tests
[0m━ Run at 12:49:04 from [test/scapy/layers/ppp.uts] by UTscapy in 0.01148080825805664
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
PPTP Related regression tests
[0m━ Run at 12:49:04 from [test/scapy/layers/pptp.uts] by UTscapy in 0.044133901596069336
[34m[1m └ Passed=36
[0m └ Failed=0

[32m
Scapy Radius layer tests
[0m━ Run at 12:49:04 from [test/scapy/layers/radius.uts] by UTscapy in 0.019916534423828125
[34m[1m └ Passed=15
[0m └ Failed=0

[32m
RIP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/rip.uts] by UTscapy in 0.0028727054595947266
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
RTP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/rtp.uts] by UTscapy in 0.0022301673889160156
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
SCTP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/sctp.uts] by UTscapy in 0.015720844268798828
[34m[1m └ Passed=25
[0m └ Failed=0

[32m
Skinny regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/skinny.uts] by UTscapy in 0.0010025501251220703
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:04 from [test/scapy/layers/smb.uts] by UTscapy in 0.018550395965576172
[34m[1m └ Passed=9
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:04 from [test/scapy/layers/smb2.uts] by UTscapy in 0.028515100479125977
[34m[1m └ Passed=28
[0m └ Failed=0

[32m
SNMP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/snmp.uts] by UTscapy in 0.006331682205200195
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
TFTP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/tftp.uts] by UTscapy in 0.002079010009765625
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Scapy USB tests
[0m━ Run at 12:49:04 from [test/scapy/layers/usb.uts] by UTscapy in 0.004065275192260742
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
VRRP regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/vrrp.uts] by UTscapy in 0.004841804504394531
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
VXLAN regression tests for Scapy
[0m━ Run at 12:49:04 from [test/scapy/layers/vxlan.uts] by UTscapy in 0.015524625778198242
[34m[1m └ Passed=8
[0m └ Failed=0

[32m
Tests for X.509 objects
[0m━ Run at 12:49:04 from [test/scapy/layers/x509.uts] by UTscapy in 0.049663543701171875
[34m[1m └ Passed=54
[0m └ Failed=0

[32m
AltBeacon unit tests
[0m━ Run at 12:49:04 from [test/contrib/altbeacon.uts] by UTscapy in 0.004259347915649414
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Regression tests for aoe module
[0m━ Run at 12:49:04 from [test/contrib/aoe.uts] by UTscapy in 0.002948760986328125
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Regression tests for the avs module
[0m━ Run at 12:49:04 from [test/contrib/avs.uts] by UTscapy in 0.002485036849975586
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:04 from [test/contrib/bfd.uts] by UTscapy in 0.001184225082397461
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
Regression tests for the bgp module
[0m━ Run at 12:49:04 from [test/contrib/bgp.uts] by UTscapy in 0.09230351448059082
[34m[1m └ Passed=153
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:04 from [test/contrib/bier.uts] by UTscapy in 0.0016350746154785156
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Bundle Protocol tests
[0m━ Run at 12:49:04 from [test/contrib/bp.uts] by UTscapy in 0.004629611968994141
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Regression tests for compatibility between NativeCANSocket and PythonCANSocket
[0m━ Run at 12:49:04 from [test/contrib/cansocket.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Regression tests for nativecansocket
[0m━ Run at 12:49:04 from [test/contrib/cansocket_native.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Regression tests for the CANSocket
[0m━ Run at 12:49:04 from [test/contrib/cansocket_python_can.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Regression tests for the avs module
[0m━ Run at 12:49:04 from [test/contrib/carp.uts] by UTscapy in 0.0011887550354003906
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Regression tests for the cdp module
[0m━ Run at 12:49:04 from [test/contrib/cdp.uts] by UTscapy in 0.008033990859985352
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Regression tests for the avs module
[0m━ Run at 12:49:04 from [test/contrib/chdlc.uts] by UTscapy in 0.0031423568725585938
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
CoAP layer test campaign
[0m━ Run at 12:49:04 from [test/contrib/coap.uts] by UTscapy in 0.005951642990112305
[34m[1m └ Passed=12
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/concox.uts] by UTscapy in 0.002122640609741211
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
DCE/RPC layer test campaign
[0m━ Run at 12:49:05 from [test/contrib/dce_rpc.uts] by UTscapy in 0.00866556167602539
[34m[1m └ Passed=20
[0m └ Failed=0

[32m
Validation of Diameter layer
[0m━ Run at 12:49:05 from [test/contrib/diameter.uts] by UTscapy in 0.04561972618103027
[34m[1m └ Passed=36
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/dtp.uts] by UTscapy in 0.003832578659057617
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/eddystone.uts] by UTscapy in 0.004179239273071289
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
EIGRP Tests
[0m━ Run at 12:49:05 from [test/contrib/eigrp.uts] by UTscapy in 0.023700714111328125
[34m[1m └ Passed=53
[0m └ Failed=0
 Tests for the Scapy EIGRP layer

[32m
ENIP Tests
[0m━ Run at 12:49:05 from [test/contrib/enipTCP.uts] by UTscapy in 0.011435270309448242
[34m[1m └ Passed=22
[0m └ Failed=0

[32m
ERSPAN
[0m━ Run at 12:49:05 from [test/contrib/erspan.uts] by UTscapy in 0.004689931869506836
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
EtherCat test campaign
[0m━ Run at 12:49:05 from [test/contrib/ethercat.uts] by UTscapy in 0.08985042572021484
[34m[1m └ Passed=9
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/etherip.uts] by UTscapy in 0.0007331371307373047
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Exposure Notification System tests
[0m━ Run at 12:49:05 from [test/contrib/exposure_notification.uts] by UTscapy in 0.0032660961151123047
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/geneve.uts] by UTscapy in 0.007273674011230469
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/gtp.uts] by UTscapy in 0.07241702079772949
[34m[1m └ Passed=73
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:05 from [test/contrib/gtp_v2.uts] by UTscapy in 0.10603952407836914
[34m[1m └ Passed=89
[0m └ Failed=0

[32m
Regression tests for Scapy
[0m━ Run at 12:49:05 from [test/contrib/homeplugav.uts] by UTscapy in 0.011811494827270508
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
Regression tests for Scapy
[0m━ Run at 12:49:05 from [test/contrib/homepluggp.uts] by UTscapy in 0.0062258243560791016
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Regression tests for Scapy
[0m━ Run at 12:49:05 from [test/contrib/homeplugsg.uts] by UTscapy in 0.0012221336364746094
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
HTTP/2 Campaign
[0m━ Run at 12:49:08 from [test/contrib/http2.uts] by UTscapy in 3.112952947616577
[34m[1m └ Passed=106
[0m └ Failed=0

[32m
iBeacon unit tests
[0m━ Run at 12:49:08 from [test/contrib/ibeacon.uts] by UTscapy in 0.009662866592407227
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:08 from [test/contrib/icmp_extensions.uts] by UTscapy in 0.0016829967498779297
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
IEC 60870-5-104 test campaign
[0m━ Run at 12:49:08 from [test/contrib/iec104.uts] by UTscapy in 0.21504807472229004
[34m[1m └ Passed=25
[0m └ Failed=0

[32m
IFE test campaign
[0m━ Run at 12:49:08 from [test/contrib/ife.uts] by UTscapy in 0.004072427749633789
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
IGMP tests
[0m━ Run at 12:49:08 from [test/contrib/igmp.uts] by UTscapy in 0.007793426513671875
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
IGMPv3 tests
[0m━ Run at 12:49:08 from [test/contrib/igmpv3.uts] by UTscapy in 0.006121158599853516
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Ikev2 Tests
[0m━ Run at 12:49:08 from [test/contrib/ikev2.uts] by UTscapy in 0.053926944732666016
[34m[1m └ Passed=14
[0m └ Failed=0
 Tests for the Ikev2 layer

[32m
IS-IS Tests
[0m━ Run at 12:49:08 from [test/contrib/isis.uts] by UTscapy in 0.11282610893249512
[34m[1m └ Passed=5
[0m └ Failed=0
 Tests for the IS-IS layer

[32m
Regression tests for ISOTP Message Builder
[0m━ Run at 12:49:09 from [test/contrib/isotp_message_builder.uts] by UTscapy in 0.03737688064575195
[34m[1m └ Passed=20
[0m └ Failed=0

[32m
Regression tests for ISOTPNativeSocket
[0m━ Run at 12:49:09 from [test/contrib/isotp_native_socket.uts] by UTscapy in 0.015546798706054688
[34m[1m └ Passed=2
[0m[31m[1m └ Failed=26
[0m
######
## Configuration
######


###(000)=[failed] Imports

[34m[1m>>> [0mwith open(scapy_path("test/contrib/automotive/interface_mockup.py")) as f:
...     exec(f.read())
... 
Traceback (most recent call last):
  File "<input>", line 3, in <module>
  File "<string>", line 60, in <module>
  File "<string>", line 41, in test_and_setup_socket_can
  File "/usr/local/lib/python3.9/subprocess.py", line 349, in call
    with Popen(*popenargs, **kwargs) as p:
  File "/usr/local/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/lib/python3.9/subprocess.py", line 1837, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'cansend'


######
## Compatibility with can-isotp linux kernel modules
######


###(002)=[failed] Compatibility with isotpsend

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(003)=[failed] Compatibility with isotpsend - extended addresses

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(004)=[failed] Compatibility with isotprecv

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(005)=[failed] Compatibility with isotprecv - extended addresses

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


######
## ISOTPNativeSocket tests
######


###(006)=[failed] Create ISOTP socket

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(007)=[failed] Send single frame ISOTP message

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(008)=[failed] Send single frame ISOTP message Test init with CANSocket

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(009)=[failed] Test init with wrong type

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(010)=[failed] Send two-frame ISOTP message

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(011)=[failed] Send a single frame ISOTP message with padding

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(012)=[failed] Send a two-frame ISOTP message with padding

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(013)=[failed] Receive a padded single frame ISOTP message with padding disabled

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(014)=[failed] Receive a padded single frame ISOTP message with padding enabled

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(015)=[failed] Receive a non-padded single frame ISOTP message with padding enabled

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(016)=[failed] Receive a padded two-frame ISOTP message with padding enabled

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(017)=[failed] Receive a padded two-frame ISOTP message with padding disabled

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(018)=[failed] Receive a single frame ISOTP message

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(019)=[failed] Receive a single frame ISOTP message, with extended addressing

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(020)=[failed] Receive a two-frame ISOTP message

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(021)=[failed] Receive a two-frame ISOTP message and test python with statement

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(022)=[failed] ISOTP Socket sr1 test

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(023)=[failed] ISOTP Socket sr1 and ISOTP test

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(024)=[failed] ISOTP Socket sr1 and ISOTP test vice versa

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


###(025)=[failed] ISOTP Socket sniff

[34m[1m>>> [0mexit_if_no_isotp_module()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'exit_if_no_isotp_module' is not defined


######
## Cleanup
######


###(031)=[failed] Delete vcan interfaces

[34m[1m>>> [0massert cleanup_interfaces()
Traceback (most recent call last):
  File "<input>", line 2, in <module>
NameError: name 'cleanup_interfaces' is not defined


[32m
Regression tests for ISOTP packet definitions
[0m━ Run at 12:49:10 from [test/contrib/isotp_packet.uts] by UTscapy in 1.2338688373565674
[34m[1m └ Passed=50
[0m └ Failed=0

[32m
Regression tests for ISOTPSoftSocket
[0m━ Run at 12:49:18 from [test/contrib/isotp_soft_socket.uts] by UTscapy in [31m8.048869371414185[0m
[34m[1m └ Passed=52
[0m └ Failed=0

[32m
Regression tests for isotp_scan
[0m━ Run at 12:49:18 from [test/contrib/isotpscan.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0
 Some tests are disabled to lower the CI utilitzation

[32m
knx layer test campaign
[0m━ Run at 12:49:18 from [test/contrib/knx.uts] by UTscapy in 0.009318113327026367
[34m[1m └ Passed=18
[0m └ Failed=0

[32m
LACP unit tests
[0m━ Run at 12:49:18 from [test/contrib/lacp.uts] by UTscapy in 0.0038306713104248047
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
Regression tests for the ldp module
[0m━ Run at 12:49:18 from [test/contrib/ldp.uts] by UTscapy in 0.008658170700073242
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
LLDP test campaign
[0m━ Run at 12:49:18 from [test/contrib/lldp.uts] by UTscapy in 0.04905366897583008
[34m[1m └ Passed=11
[0m └ Failed=0

[32m
Regression tests for Scapy
[0m━ Run at 12:49:18 from [test/contrib/loraphy2wan.uts] by UTscapy in 0.004063844680786133
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Licklider Transmission Protocol tests
[0m━ Run at 12:49:18 from [test/contrib/ltp.uts] by UTscapy in 0.0062007904052734375
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
MACControl test campaign
[0m━ Run at 12:49:18 from [test/contrib/mac_control.uts] by UTscapy in 0.011836528778076172
[34m[1m └ Passed=12
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:18 from [test/contrib/macsec.uts] by UTscapy in 0.04844832420349121
[34m[1m └ Passed=17
[0m[31m[1m └ Failed=16
[0m
######
## MACsec
######


###(001)=[failed] MACsec - basic encryption - encrypted

[34m[1m>>> [0msa = MACsecSA(sci=b'\x52\x54\x00\x13\x01\x56\x00\x01', an=0, pn=100, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=1, send_sci=1)
[34m[1m>>> [0mp = Ether(src='aa:aa:aa:bb:bb:bb', dst='cc:cc:cc:dd:dd:dd')/IP(src='192.168.0.1', dst='192.168.0.2')/ICMP(type='echo-request')/"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(002)=[failed] MACsec - basic decryption - encrypted

[34m[1m>>> [0msa = MACsecSA(sci=b'\x52\x54\x00\x13\x01\x56\x00\x01', an=0, pn=100, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=1, send_sci=1)
[34m[1m>>> [0mp = Ether(src='aa:aa:aa:bb:bb:bb', dst='cc:cc:cc:dd:dd:dd')/IP(src='192.168.0.1', dst='192.168.0.2')/ICMP(type='echo-request')/"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(003)=[failed] MACsec - basic decap - decrypted

[34m[1m>>> [0msa = MACsecSA(sci=b'\x52\x54\x00\x13\x01\x56\x00\x01', an=0, pn=100, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=1, send_sci=1)
[34m[1m>>> [0mp = Ether(src='aa:aa:aa:bb:bb:bb', dst='cc:cc:cc:dd:dd:dd')/IP(src='192.168.0.1', dst='192.168.0.2')/ICMP(type='echo-request')/"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(005)=[failed] MACsec - basic encryption - integrity only

[34m[1m>>> [0msa = MACsecSA(sci=b'\x52\x54\x00\x13\x01\x56\x00\x01', an=0, pn=200, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mp = Ether(src='aa:aa:aa:bb:bb:bb', dst='cc:cc:cc:dd:dd:dd')/IP(src='192.168.0.1', dst='192.168.0.2')/ICMP(type='echo-request')/"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(006)=[failed] MACsec - basic decryption - integrity only

[34m[1m>>> [0msa = MACsecSA(sci=b'\x52\x54\x00\x13\x01\x56\x00\x01', an=0, pn=200, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mp = Ether(src='aa:aa:aa:bb:bb:bb', dst='cc:cc:cc:dd:dd:dd')/IP(src='192.168.0.1', dst='192.168.0.2')/ICMP(type='echo-request')/"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(007)=[failed] MACsec - basic decap - integrity only

[34m[1m>>> [0msa = MACsecSA(sci=b'\x52\x54\x00\x13\x01\x56\x00\x01', an=0, pn=200, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mp = Ether(src='aa:aa:aa:bb:bb:bb', dst='cc:cc:cc:dd:dd:dd')/IP(src='192.168.0.1', dst='192.168.0.2')/ICMP(type='echo-request')/"1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(018)=[failed] MACsec - authenticate

[34m[1m>>> [0mtx = Ether(b"RT\x00\x12\x01V.\xbc\x84\xd5\xca\x13\x88\xe5 \x00\x00\x00\x00\rRT\x00\x13\x01V\x00\x01\x08\x00E\x00\x00T\x11:@\x00@\x01\xa6\x1b\xc0\xa8\x01\x01\xc0\xa8\x01\x02\x08\x00a\xeaG+\x00\x01\xc0~RY\x00\x00\x00\x00w>\x06\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\xf1\xb8\xe4,b\xb00\x98L\x85m1Q9\t:")
[34m[1m>>> [0mrx = Ether(b".\xbc\x84\xd5\xca\x13RT\x00\x12\x01V\x88\xe5 \x00\x00\x00\x00#RT\x00\x12\x01V\x00\x01\x08\x00E\x00\x00T\xd4\x1a\x00\x00@\x01#;\xc0\xa8\x01\x02\xc0\xa8\x01\x01\x00\x00i\xeaG+\x00\x01\xc0~RY\x00\x00\x00\x00w>\x06\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37z\x11\xf8S\xe5u\x81\xe8\x19\\nxX\x02\x13\x01")
[34m[1m>>> [0mrxsa = MACsecSA(sci=0x5254001201560001, an=0, pn=31, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mtxsa = MACsecSA(sci=0x5254001301560001, an=0, pn=31, key=b'\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mtxdec = txsa.decap(txsa.decrypt(tx))
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 199, in decrypt
    decryptor = Cipher(
NameError: name 'Cipher' is not defined


###(020)=[failed] MACsec - decrypt

[34m[1m>>> [0mtx = Ether(b"RT\x00\x12\x01V.\xbc\x84\xd5\xca\x13\x88\xe5,\x00\x00\x00\x00\x1fRT\x00\x13\x01V\x00\x01\xf1\xd6\xf7\x03\xf0%\x19\x8e\x88\xb0\xac\xa1\x82\x98\x94]\x85&\xc4U*\x84kX#O\xb6\x8f\xf1\x9d\xc5\xdc\xe0\x80,\x98\x8e_\xd53e\x16b0\xaf\xd9\x9e;A\x8aM\xfe\x16\xf6j\xe6\xea\xb7\x9c\xf3\x9bCc#,\x93\xf7\xc0\xdb\x9a\xd0\x0c\xfd?\xcbd\xe5D\xb7\xc9\xbb\xf5\x93M\xc5\x1d'LR\xed\xf3\xbc\xa0\xdf\x86\xf7\xc2JN\xcd\x19\xc1?\xf7\xd2\xbe\x00\x0f`\xe0\x04\xcfX5\xdc\xe7\xb6\xe6\x82\xc4\xac\xd7\x06\xe31\xbe|\x98l\xc8\xc1#*n+x|\xad\x0b<\xfd\xb8\xceoR\x1e")
[34m[1m>>> [0mrx = Ether(b".\xbc\x84\xd5\xca\x13RT\x00\x12\x01V\x88\xe5,\x00\x00\x00\x005RT\x00\x12\x01V\x00\x01\x04\xbaV\xe6\xcf\xcfbhy\x7f\xce\x12.\x80WI\xe5\xd5\x98)6\xe1vjVO@\x84\xde\x9b\x83\xbaw\xef\x13\xc3\xfd\xad\x81\xd4S?\x01\x01\xab\xa8 PzSq2\x905\xf6\x8cT\xd7\xb0P\xe2\xd04\xc7F\x88\x85\x10\xc3\x99\x80\xe3(\t\x10\x87\xa9{z\x22\xce>;Mr\xbe\xc1\xa0\x07%\x01\x96\xe5\xa3\x18]\xec\xbb\x7f\xde0\xa1\x99\xb2\xad\x93j\x97\xef\xf4\xee\xf0\xe4s\xb7h\x95\xc3\x8b[~hX\xbf|\xee\x99\x97\xe0;Q\x9aa\xb9\x13$\xd6\xe4\xb4\xce\njt\xc0\xa1.")
[34m[1m>>> [0mrxsa = MACsecSA(sci=0x5254001201560001, an=0, pn=31, key=b'aaaaaaaaaaaaaaaa', icvlen=16, encrypt=1, send_sci=1)
[34m[1m>>> [0mtxsa = MACsecSA(sci=0x5254001301560001, an=0, pn=31, key=b'\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61', icvlen=16, encrypt=1, send_sci=1)
[34m[1m>>> [0mtxdec = txsa.decap(txsa.decrypt(tx))
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 199, in decrypt
    decryptor = Cipher(
NameError: name 'Cipher' is not defined


###(025)=[failed] MACsec - Standard Test Vectors - C.1.1 GCM-AES-128 (54-octet frame integrity protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\x12\x15\x35\x24\xC0\x89\x5E\x81', an=2, pn=0xB2C28465, key=b'\xAD\x7A\x2B\xD0\x3E\xAC\x83\x5A\x6F\x62\x0F\xDC\xB5\x06\xB3\x45', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mp = Ether(src='7A:0D:46:DF:99:8D', dst='D6:09:B1:F0:56:63', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340001")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\x12\x15\x35\x24\xC0\x89\x5E\x81\xB2\xC2\x84\x65'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(026)=[failed] MACsec - Standard Test Vectors - C.1.2 GCM-AES-256 (54-octet frame integrity protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\x12\x15\x35\x24\xC0\x89\x5E\x81', an=2, pn=0xB2C28465, key=b'\xE3\xC0\x8A\x8F\x06\xC6\xE3\xAD\x95\xA7\x05\x57\xB2\x3F\x75\x48\x3C\xE3\x30\x21\xA9\xC7\x2B\x70\x25\x66\x62\x04\xC6\x9C\x0B\x72', icvlen=16, encrypt=0, send_sci=1)
[34m[1m>>> [0mp = Ether(src='7A:0D:46:DF:99:8D', dst='D6:09:B1:F0:56:63', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340001")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\x12\x15\x35\x24\xC0\x89\x5E\x81\xB2\xC2\x84\x65'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(027)=[failed] MACsec - Standard Test Vectors - C.1.3 GCM-AES-XPN-128 (54-octet frame integrity protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\x12\x15\x35\x24\xC0\x89\x5E\x81', an=2, pn=0xB0DF459CB2C28465, key=b'\xAD\x7A\x2B\xD0\x3E\xAC\x83\x5A\x6F\x62\x0F\xDC\xB5\x06\xB3\x45', icvlen=16, encrypt=0, send_sci=1, xpn_en = True, ssci = 0x7A30C118, salt = b'\xE6\x30\xE8\x1A\x48\xDE\x86\xA2\x1C\x66\xFA\x6D')
[34m[1m>>> [0mp = Ether(src='7A:0D:46:DF:99:8D', dst='D6:09:B1:F0:56:63', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340001")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\x9C\x00\x29\x02\xF8\x01\xC3\x3E\xAE\xA4\x7E\x08'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(028)=[failed] MACsec - Standard Test Vectors - C.1.4 GCM-AES-XPN-256 (54-octet frame integrity protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\x12\x15\x35\x24\xC0\x89\x5E\x81', an=2, pn=0xB0DF459CB2C28465, key=b'\xE3\xC0\x8A\x8F\x06\xC6\xE3\xAD\x95\xA7\x05\x57\xB2\x3F\x75\x48\x3C\xE3\x30\x21\xA9\xC7\x2B\x70\x25\x66\x62\x04\xC6\x9C\x0B\x72', icvlen=16, encrypt=0, send_sci=1, xpn_en = True, ssci = 0x7A30C118, salt = b'\xE6\x30\xE8\x1A\x48\xDE\x86\xA2\x1C\x66\xFA\x6D')
[34m[1m>>> [0mp = Ether(src='7A:0D:46:DF:99:8D', dst='D6:09:B1:F0:56:63', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340001")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\x9C\x00\x29\x02\xF8\x01\xC3\x3E\xAE\xA4\x7E\x08'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(029)=[failed] MACsec - Standard Test Vectors - C.5.1 GCM-AES-128 (54-octet frame confidentiality protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\xF0\x76\x1E\x8D\xCD\x3D\x00\x01', an=0, pn=0x76D457ED, key=b'\x07\x1B\x11\x3B\x0C\xA7\x43\xFE\xCC\xCF\x3D\x05\x1F\x73\x73\x82', icvlen=16, encrypt=1, send_sci=0)
[34m[1m>>> [0mp = Ether(src='F0:76:1E:8D:CD:3D', dst='E2:01:06:D7:CD:0D', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340004")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0mm[MACsec].ES = 1
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\xF0\x76\x1E\x8D\xCD\x3D\x00\x01\x76\xD4\x57\xED'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(030)=[failed] MACsec - Standard Test Vectors - C.5.2 GCM-AES-256 (54-octet frame confidentiality protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\xF0\x76\x1E\x8D\xCD\x3D\x00\x01', an=0, pn=0x76D457ED, key=b'\x69\x1D\x3E\xE9\x09\xD7\xF5\x41\x67\xFD\x1C\xA0\xB5\xD7\x69\x08\x1F\x2B\xDE\x1A\xEE\x65\x5F\xDB\xAB\x80\xBD\x52\x95\xAE\x6B\xE7', icvlen=16, encrypt=1, send_sci=0)
[34m[1m>>> [0mp = Ether(src='F0:76:1E:8D:CD:3D', dst='E2:01:06:D7:CD:0D', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340004")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0mm[MACsec].ES = 1
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\xF0\x76\x1E\x8D\xCD\x3D\x00\x01\x76\xD4\x57\xED'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(031)=[failed] MACsec - Standard Test Vectors - C.5.3 GCM-AES-XPN-128 (54-octet frame confidentiality protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\xF0\x76\x1E\x8D\xCD\x3D\x00\x01', an=0, pn=0xB0DF459C76D457ED, key=b'\x07\x1B\x11\x3B\x0C\xA7\x43\xFE\xCC\xCF\x3D\x05\x1F\x73\x73\x82', icvlen=16, encrypt=1, send_sci=0, xpn_en = True, ssci = 0x7A30C118, salt = b'\xE6\x30\xE8\x1A\x48\xDE\x86\xA2\x1C\x66\xFA\x6D')
[34m[1m>>> [0mp = Ether(src='F0:76:1E:8D:CD:3D', dst='E2:01:06:D7:CD:0D', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340004")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0mm[MACsec].ES = 1
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\x9C\x00\x29\x02\xF8\x01\xC3\x3E\x6A\xB2\xAD\x80'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


###(032)=[failed] MACsec - Standard Test Vectors - C.5.4 GCM-AES-XPN-256 (54-octet frame confidentiality protection)

[34m[1m>>> [0msa = MACsecSA(sci=b'\xF0\x76\x1E\x8D\xCD\x3D\x00\x01', an=0, pn=0xB0DF459C76D457ED, key=b'\x69\x1D\x3E\xE9\x09\xD7\xF5\x41\x67\xFD\x1C\xA0\xB5\xD7\x69\x08\x1F\x2B\xDE\x1A\xEE\x65\x5F\xDB\xAB\x80\xBD\x52\x95\xAE\x6B\xE7', icvlen=16, encrypt=1, send_sci=0, xpn_en = True, ssci = 0x7A30C118, salt = b'\xE6\x30\xE8\x1A\x48\xDE\x86\xA2\x1C\x66\xFA\x6D')
[34m[1m>>> [0mp = Ether(src='F0:76:1E:8D:CD:3D', dst='E2:01:06:D7:CD:0D', type=0x0800)/Raw(bytes(bytearray.fromhex("0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F30313233340004")))
[34m[1m>>> [0mm = sa.encap(p)
/home/scapy/scapy/packet.py:394: DeprecationWarning: sci has been deprecated in favor of SCI since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: an has been deprecated in favor of AN since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: shortlen has been deprecated in favor of SL since 2.4.4 !
  warnings.warn(
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0mm[MACsec].ES = 1
[34m[1m>>> [0miv = sa.make_iv(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
[34m[1m>>> [0massert(raw(iv) == raw(b'\x9C\x00\x29\x02\xF8\x01\xC3\x3E\x6A\xB2\xAD\x80'))
[34m[1m>>> [0me = sa.encrypt(m)
/home/scapy/scapy/packet.py:394: DeprecationWarning: pn has been deprecated in favor of PN since 2.4.4 !
  warnings.warn(
Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/contrib/macsec.py", line 173, in encrypt
    encryptor = Cipher(
NameError: name 'Cipher' is not defined


[32m
Modbus layer test campaign
[0m━ Run at 12:49:18 from [test/contrib/modbus.uts] by UTscapy in 0.04722714424133301
[34m[1m └ Passed=163
[0m └ Failed=0

[32m
Test mount layer
[0m━ Run at 12:49:18 from [test/contrib/mount.uts] by UTscapy in 0.012618780136108398
[34m[1m └ Passed=8
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:18 from [test/contrib/mpls.uts] by UTscapy in 0.0032634735107421875
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:18 from [test/contrib/mqtt.uts] by UTscapy in 0.009648323059082031
[34m[1m └ Passed=23
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:18 from [test/contrib/mqttsn.uts] by UTscapy in 0.043347835540771484
[34m[1m └ Passed=78
[0m └ Failed=0

[32m
Tests for nfs module
[0m━ Run at 12:49:18 from [test/contrib/nfs.uts] by UTscapy in 0.2677915096282959
[34m[1m └ Passed=8
[0m └ Failed=0

[32m
Tests for nlm module
[0m━ Run at 12:49:18 from [test/contrib/nlm.uts] by UTscapy in 0.0612177848815918
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:18 from [test/contrib/nsh.uts] by UTscapy in 0.004086494445800781
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
Tests for oncrpc module
[0m━ Run at 12:49:18 from [test/contrib/oncrpc.uts] by UTscapy in 0.01705789566040039
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Scapy OPC DA layer tests
[0m━ Run at 12:49:18 from [test/contrib/opc_da.uts] by UTscapy in 0.01438140869140625
[34m[1m └ Passed=9
[0m └ Failed=0

[32m
Tests for OpenFlow v1.0 with Scapy
[0m━ Run at 12:49:19 from [test/contrib/openflow.uts] by UTscapy in 0.013335227966308594
[34m[1m └ Passed=16
[0m └ Failed=0

[32m
Tests for OpenFlow v1.3 with Scapy
[0m━ Run at 12:49:19 from [test/contrib/openflow3.uts] by UTscapy in 0.02542257308959961
[34m[1m └ Passed=24
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:19 from [test/contrib/ospf.uts] by UTscapy in 0.00789952278137207
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
PCOM tests
[0m━ Run at 12:49:19 from [test/contrib/pcom.uts] by UTscapy in 0.008357048034667969
[34m[1m └ Passed=10
[0m └ Failed=0

[32m
PFCP tests
[0m━ Run at 12:49:20 from [test/contrib/pfcp.uts] by UTscapy in 1.6475813388824463
[34m[1m └ Passed=10
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:20 from [test/contrib/pim.uts] by UTscapy in 0.017879724502563477
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
ProfinetIO layer test campaign
[0m━ Run at 12:49:20 from [test/contrib/pnio.uts] by UTscapy in 0.016123533248901367
[34m[1m └ Passed=20
[0m └ Failed=0

[32m
ProfinetIO DCP layer test campaign
[0m━ Run at 12:49:20 from [test/contrib/pnio_dcp.uts] by UTscapy in 0.01715087890625
[34m[1m └ Passed=11
[0m └ Failed=0

[32m
PNIO RPC layer test campaign
[0m━ Run at 12:49:20 from [test/contrib/pnio_rpc.uts] by UTscapy in 0.14589190483093262
[34m[1m └ Passed=75
[0m └ Failed=0

[32m
Tests for portmap module
[0m━ Run at 12:49:20 from [test/contrib/portmap.uts] by UTscapy in 0.01067042350769043
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
PPI/PPI_CACE/PPI_GEOTAG Global Campaign
[0m━ Run at 12:49:21 from [test/contrib/ppi_cace.uts] by UTscapy in 0.14954042434692383
[34m[1m └ Passed=13
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/ppi_geotag.uts] by UTscapy in 0.003169536590576172
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/ripng.uts] by UTscapy in 0.0018281936645507812
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Regression tests for the RoCE layer
[0m━ Run at 12:49:21 from [test/contrib/roce.uts] by UTscapy in 0.010419368743896484
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
RPL layer test campaign
[0m━ Run at 12:49:21 from [test/contrib/rpl.uts] by UTscapy in 0.01917099952697754
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Regression tests for the rsvp module
[0m━ Run at 12:49:21 from [test/contrib/rsvp.uts] by UTscapy in 0.0022749900817871094
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
RTCP regression tests for Scapy
[0m━ Run at 12:49:21 from [test/contrib/rtcp.uts] by UTscapy in 0.003496885299682617
[34m[1m └ Passed=3
[0m[31m[1m └ Failed=1
[0m
######
## RTCP Receiver Report tests
######


###(001)=[failed] test receiver report parse

[34m[1m>>> [0mraw = b'\x81\xc9\x00\x07\xa2\xdf\x02\x72\x49\x6e\x93\xbd\x00\xff\xff\xff\x00\x00\x59\x47\x00\x00\x00\x00\xe4\x8f\xb9\x3a\x00\x03\x3f\x1b'
[34m[1m>>> [0mparsed = RTCP(raw)
[34m[1m>>> [0massert parsed.version == 2
[34m[1m>>> [0massert parsed.padding == 0
[34m[1m>>> [0massert parsed.count == 1
[34m[1m>>> [0massert parsed.packet_type == 201
[34m[1m>>> [0massert parsed.length == 7
[34m[1m>>> [0massert parsed.sourcesync == 0xa2df0272
[34m[1m>>> [0massert parsed.report_blocks[0].sourcesync == 0x496e93bd
[34m[1m>>> [0massert parsed.report_blocks[0].fraction_lost == 0
[34m[1m>>> [0massert parsed.report_blocks[0].cumulative_lost == 0xffffff
[34m[1m>>> [0massert parsed.report_blocks[0].highest_seqnum_recv == 22855
Traceback (most recent call last):
  File "/home/scapy/scapy/packet.py", line 428, in __getattr__
    fld, v = self.getfield_and_val(attr)
  File "/home/scapy/scapy/packet.py", line 423, in getfield_and_val
    raise ValueError
ValueError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<input>", line 2, in <module>
  File "/home/scapy/scapy/packet.py", line 430, in __getattr__
    return self.payload.__getattr__(attr)
  File "/home/scapy/scapy/packet.py", line 428, in __getattr__
    fld, v = self.getfield_and_val(attr)
  File "/home/scapy/scapy/packet.py", line 1722, in getfield_and_val
    raise AttributeError(attr)
AttributeError: highest_seqnum_recv


[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/rtr.uts] by UTscapy in 0.02700018882751465
[34m[1m └ Passed=42
[0m └ Failed=0

[32m
SDNV library tests
[0m━ Run at 12:49:21 from [test/contrib/sdnv.uts] by UTscapy in 0.008024215698242188
[34m[1m └ Passed=6
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/sebek.uts] by UTscapy in 0.005873441696166992
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/send.uts] by UTscapy in 0.009913921356201172
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/socks.uts] by UTscapy in 0.008560419082641602
[34m[1m └ Passed=3
[0m └ Failed=0

[32m
Regression tests for the spbm module
[0m━ Run at 12:49:21 from [test/contrib/spbm.uts] by UTscapy in 0.0025491714477539062
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/tacacs.uts] by UTscapy in 0.027928590774536133
[34m[1m └ Passed=34
[0m └ Failed=0

[32m
TZSP test campaign
[0m━ Run at 12:49:21 from [test/contrib/tzsp.uts] by UTscapy in 0.07839226722717285
[34m[1m └ Passed=25
[0m └ Failed=0

[32m
VQP tests
[0m━ Run at 12:49:21 from [test/contrib/vqp.uts] by UTscapy in 0.0019321441650390625
[34m[1m └ Passed=2
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:21 from [test/contrib/vtp.uts] by UTscapy in 0.0005140304565429688
[34m[1m └ Passed=1
[0m └ Failed=0

[32m
WireGuard tests
[0m━ Run at 12:49:21 from [test/contrib/wireguard.uts] by UTscapy in 0.003899097442626953
[34m[1m └ Passed=4
[0m └ Failed=0

[32m
Regression tests for isotpscanner
[0m━ Run at 12:49:21 from [test/tools/isotpscanner.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Regression tests for obdscanner
[0m━ Run at 12:49:21 from [test/tools/obdscanner.uts] by UTscapy in 0.0
 └ Passed=0
 └ Failed=0

[32m
Regression tests for the XCP_CAN
[0m━ Run at 12:49:24 from [test/tools/xcpscanner.uts] by UTscapy in 3.0316216945648193
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
Regression tests for the CCP layer
[0m━ Run at 12:49:24 from [test/contrib/automotive/ccp.uts] by UTscapy in 0.15564966201782227
[34m[1m └ Passed=63
[0m └ Failed=0

[32m
Regression tests for the DoIP layer
[0m━ Run at 12:49:24 from [test/contrib/automotive/doip.uts] by UTscapy in 0.07340741157531738
[34m[1m └ Passed=23
[0m └ Failed=0

[32m
Regression tests for the Ecu utility
[0m━ Run at 12:49:24 from [test/contrib/automotive/ecu.uts] by UTscapy in 0.24105620384216309
[34m[1m └ Passed=31
[0m └ Failed=0

[32m
Regression tests for EcuAnsweringMachine
[0m━ Run at 12:49:26 from [test/contrib/automotive/ecu_am.uts] by UTscapy in 1.8105742931365967
[34m[1m └ Passed=10
[0m └ Failed=0

[32m
Regression tests for the KWP2000 layer
[0m━ Run at 12:49:26 from [test/contrib/automotive/kwp.uts] by UTscapy in 0.035265445709228516
[34m[1m └ Passed=66
[0m └ Failed=0

[32m
Test campaign
[0m━ Run at 12:49:26 from [test/contrib/automotive/someip.uts] by UTscapy in 0.055505990982055664
[34m[1m └ Passed=55
[0m └ Failed=0

[32m
Regression tests for TestSocket
[0m━ Run at 12:49:27 from [test/contrib/automotive/testsocket.uts] by UTscapy in 0.500676155090332
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Regression tests for the UDS layer
[0m━ Run at 12:49:27 from [test/contrib/automotive/uds.uts] by UTscapy in 0.07924294471740723
[34m[1m └ Passed=157
[0m └ Failed=0

[32m
Regression tests for the OBD layer
[0m━ Run at 12:49:27 from [test/contrib/automotive/obd/obd.uts] by UTscapy in 0.09662914276123047
[34m[1m └ Passed=90
[0m └ Failed=0

[32m
Regression tests for obd_scan
[0m━ Run at 12:49:29 from [test/contrib/automotive/obd/scanner.uts] by UTscapy in 1.845038652420044
[34m[1m └ Passed=8
[0m └ Failed=0

[32m
Regression tests for automotive scanner configuration
[0m━ Run at 12:49:29 from [test/contrib/automotive/scanner/configuration.uts] by UTscapy in 0.007846355438232422
[34m[1m └ Passed=8
[0m └ Failed=0

[32m
Regression tests for enumerators
[0m━ Run at 12:49:29 from [test/contrib/automotive/scanner/enumerator.uts] by UTscapy in 0.39917778968811035
[34m[1m └ Passed=42
[0m └ Failed=0

[32m
Regression tests for graph
[0m━ Run at 12:49:29 from [test/contrib/automotive/scanner/graph.uts] by UTscapy in 0.0030341148376464844
[34m[1m └ Passed=5
[0m └ Failed=0

[32m
Regression tests for automotive scanner staged test_case
[0m━ Run at 12:49:29 from [test/contrib/automotive/scanner/staged_test_case.uts] by UTscapy in 0.014386892318725586
[34m[1m └ Passed=10
[0m └ Failed=0

[32m
Regression tests for automotive scanner test_case
[0m━ Run at 12:49:29 from [test/contrib/automotive/scanner/test_case.uts] by UTscapy in 0.0038328170776367188
[34m[1m └ Passed=7
[0m └ Failed=0

[32m
Regression tests for Simulated ECUs and UDS Scanners
[0m━ Run at 12:50:22 from [test/contrib/automotive/scanner/uds_scanner.uts] by UTscapy in [41m52.994439363479614[0m
[34m[1m └ Passed=23
[0m └ Failed=0

[32m
gmlan unit tests
[0m━ Run at 12:50:22 from [test/contrib/automotive/gm/gmlan.uts] by UTscapy in 0.03528857231140137
[34m[1m └ Passed=66
[0m └ Failed=0

[32m
Regression tests for gmlanutil
[0m━ Run at 12:50:39 from [test/contrib/automotive/gm/gmlanutils.uts] by UTscapy in [41m17.14499020576477[0m
[34m[1m └ Passed=52
[0m └ Failed=0

[32m
Regression tests for GMLAN Scanners
[0m━ Run at 12:50:50 from [test/contrib/automotive/gm/scanner.uts] by UTscapy in [41m10.652989149093628[0m
[34m[1m └ Passed=15
[0m └ Failed=0

[32m
Regression tests for the HSFZ layer
[0m━ Run at 12:50:50 from [test/contrib/automotive/bmw/hsfz.uts] by UTscapy in 0.007348775863647461
[34m[1m └ Passed=9
[0m └ Failed=0

[32m
Regression tests for the XCP
[0m━ Run at 12:50:50 from [test/contrib/automotive/xcp/xcp.uts] by UTscapy in 0.04558086395263672
[34m[1m └ Passed=37
[0m └ Failed=0

[32m
Regression tests for the XCP using CANSockets
[0m━ Run at 12:50:50 from [test/contrib/automotive/xcp/xcp_comm.uts] by UTscapy in 0.0073854923248291016
[34m[1m └ Passed=6
[0m └ Failed=0


[31mUTscapy ended with error code 1[0m
