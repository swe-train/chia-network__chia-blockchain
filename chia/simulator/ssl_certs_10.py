# Package: simulator

from __future__ import annotations

from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUWzGLmUq3RgS/u2oYomRSyKsXWwcwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDczMTAyMDgyM1oXDTMyMDcy
ODAyMDgyM1owRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAzB+IyNSmoJt99NpPQ2agYv/3Bxa70ZKHmCRHT6h2eNFg
87Mw6Dntpq8uS4zAa2pUohWNRPFrWLkHMxngQuuCJqfu7sqTJwwSNodYK6ajoidI
qKyZGZd4kj8AYhKe/2O0cefjWbc1leOzXwqtQSdlr65pXaJMWG7jckNGf8hj+Dfe
ZqJdonS9w6LYJPFH7l8njHaECLm6fWusJjq8nhVlAbbjetnl5wYsWjdJZCWfcSG2
PRrHncuPLSJVPn9Gdo/bqC+zQ3VJhXLELM/Fz10+cxWpaUvjEJEnhaRjAYsD6wk0
yBoaNXzVo3e/gsPcppG14dgFC+bdfFytDHMFqw2kHwIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBNwno+FoJnwcJpltsDfPnTYAMD
+9gm/dMBrwVtYZyB6OJKrOUYY49KA5p5/O06n0S7DOYKXVGZmXPownj9Hc1/0kUE
KKg3GTzekBIso91wUL9isR5eEUnLfnHwa1OAsu2ycv1pQWwsyFvcl8ttBdmYWN5z
3EgF3kDtIc0erz91hpkixev4ZpWQzf22UKhp58EehwODI5CRRJKeVUP/pMPkrfUm
58aU31u+rCSX+uJWH/wnWeE6WZDBS5/4abcY8KLnW+ArEXrZPpEqWWsuj0lWrM24
yyfyhCmRMmeS6XSgpitKZk6kWG0VUUF6NKSilGCYUD1tEKq89oUCdDoMqJIC
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDMH4jI1Kagm330
2k9DZqBi//cHFrvRkoeYJEdPqHZ40WDzszDoOe2mry5LjMBralSiFY1E8WtYuQcz
GeBC64Imp+7uypMnDBI2h1grpqOiJ0iorJkZl3iSPwBiEp7/Y7Rx5+NZtzWV47Nf
Cq1BJ2WvrmldokxYbuNyQ0Z/yGP4N95mol2idL3Dotgk8UfuXyeMdoQIubp9a6wm
OryeFWUBtuN62eXnBixaN0lkJZ9xIbY9Gsedy48tIlU+f0Z2j9uoL7NDdUmFcsQs
z8XPXT5zFalpS+MQkSeFpGMBiwPrCTTIGho1fNWjd7+Cw9ymkbXh2AUL5t18XK0M
cwWrDaQfAgMBAAECggEBAI/8aotn3YYLSQUv/ZuIx/gtoH4inigN2ZILfTYGmlNN
NruRGh2lxyq+BcULKyxaHAsdcsJAHb2+/wIf7Z6m6+8CpLtSsAxqKmrGe/6GlISs
e0doQLLZsxZOVKHZisiR91YmAaxmXOk3bm7LZD1CYitTt0VyV7JFvjD6nb9Dhqku
1SDH4igl/AqrnTUuZ1NPv+xTJGuDfCL4PPinGu/9F0VuWU8PDDzm+Xl7pqbCFw0d
nvoqlXVoruqq+FDY4uQG9F7h4oAfk7+EdYy3MML/HkGef07ifeY6HtpUC6f73zHb
cpqQ++pAFK2QYCpQZB5Yoja1JGvyn7jjXGNT58tPLlECgYEA6cjpeucBU/Yxp56i
SIM1IJQZjliGMtVf4Ulmy88t2hUpT6nn1yYKdK+NNCN85KK+QT4a9ZCU+7YpCj8B
yF0/80Vn/dUXPHw4TURCBGFDl+tNOVaQHRXZca2/GEm9dGz2fybCQxUZKawhapGR
S16h19ed7XW44mDeeZsvaNof5/cCgYEA34URizWh+97565qsNGNHNCxwVl3RdcdD
59/9Tbq94amy+BQgVvQ40sVa6+w+nkqtZSuwyKHSHaCNFPOZiWP/0IT9hBRdEODv
bzt1li4UgS+aUKrD5fX6Lw9cgD08OVKWgMSMWehrm4sgL6itzjUqbMVerFJmBhMb
x12owc5yqxkCgYEA3h3PBsAX2OfeAX2Mfgx7G3raVQ3yYrWrpOYSTq2GyN62I0Qw
S4+O+5IXPGRDMw8UZ/RTtOArTIOjtmJqlS1TpxRYWyhsLUFwVKj3eCXZDKu48TM3
NQsfTwxetPrKj6U/BUuT4hxXjepGzXOEcfF1HxdyqrvgbuTOOwegIaSsD70CgYA5
G15oGsPP/iAMOfBVUigXBGOPLVkeplKLI4csHNH2nczD5SB+FteNwi6AqFM3Tg0P
FCKOoAl22FYzTCmmGI57T/8Vh75fWZjS6nYYcJ18hBUBFyAF2Nqau2n+uaZxXtBl
BdJ2BhO4IcuPYaFGVf8I20Rc8pBubONkBGHhYkWZwQKBgB7xvvDZEWSbhW8xgs5g
4a4AElP2al8Rmki4nv+q10z3cgqH5l1EoT1nKhZ6tvVOZj5SDwKHA+shp2PYnV7o
yX9Opy5+wwYqbpwx+D1j4C64bJ31k7NiJ3kh18I1tS8Pc+uvAKUepjZcRvgaRJsP
DEuyC4irkg/3ZMIPxYmI6ZLY
-----END PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUSj1pdOwRwJrEORU+fqWLTHMZr3cwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC76QDovPz74lN1tpHAA/sXtUXVu3UiikJjnFpgUQIK44wX
+QSbiY3W4fvvmrDv2c283ZiH2td080R/sACUVW3o87hqYJI3aSsuoE0AtOkBjPbg
xvn4T9C0DpJQIiqhBWXBZ7JnLVcgihCblRd/LsjWQOB/G42VC7ikLe5zW5fto0DS
sTwFLmY6wKMmuSN0HoHvk/fv7YSTFKPNW6ofwwQ7gaeqwBRUsRqCXoREUe0wLvUP
7HRfJ6+mDn3Yd+upymCuUOhXQNTjD5mfiijxawq8MYIO3niObValyqNU6mHUyaOj
4abGws3Y8Mju+5dlHmQmBBL/HXme1Irw/Ta4G7TnAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAWfUyskkstyDNjFG9EseOZ
YPvtjkjbrlk+IKPfACfpiwAGsEMYS3P/GVQXkA/VYAUiaqhZqJvGvb7zceXKDqcD
3/UiId3YtlcZYzaAcAbf7xmPkmb/kMjtsmao17lm//YldbM9zp9kh6JJS+8Gh1cp
Q4c4pR1NPS5/m/dPHNe5K/BrAQZUEV4TBlfEUSkQ9vYJeOIekHGWVTFOgJ9mfML5
aP01qLcDOvTwV9BewpjHL0RXPqn7w9v4nUQa9Tqla5ce/OBgAOfB9xO2+9IpWI8a
NCigB+qkSal87TL2/jGgry1aPpT5SHP2iGaLYbG5//Z75rTZzGHQJQxgJeR5zm+7
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC76QDovPz74lN1
tpHAA/sXtUXVu3UiikJjnFpgUQIK44wX+QSbiY3W4fvvmrDv2c283ZiH2td080R/
sACUVW3o87hqYJI3aSsuoE0AtOkBjPbgxvn4T9C0DpJQIiqhBWXBZ7JnLVcgihCb
lRd/LsjWQOB/G42VC7ikLe5zW5fto0DSsTwFLmY6wKMmuSN0HoHvk/fv7YSTFKPN
W6ofwwQ7gaeqwBRUsRqCXoREUe0wLvUP7HRfJ6+mDn3Yd+upymCuUOhXQNTjD5mf
iijxawq8MYIO3niObValyqNU6mHUyaOj4abGws3Y8Mju+5dlHmQmBBL/HXme1Irw
/Ta4G7TnAgMBAAECggEAU3Qt9S9J48wmaNcGcBLUhzj4pO22HfrtdTPRZ4lSsOdS
Jqtvgmxa1B5VN5qqDjvbBZAc1+k3WzdXKqZN+5LdV2I2evgcuAM7LGABEtlFymyC
kF2OUtuPwwfdrz0dVZoCER0uvGgEk+z9ZzuVzeRHSfBSQ+FGxfUIsdG8XvtExELC
5SBx+0/Kka08IEuyTjjp37tVHN1DCYunWN8PvkDPLcmw0jjt78pWpIylNTctcFMG
rhLz0CFAAJGEAF082xZdwSi2BFlQ3RSufZYDygHGvQvRVIvL/jLIBtIe+gPjvSvW
WxqSCzS/Akt0O65unCebkjaBQuBvql8lYfBhGDu/oQKBgQD0g3jDh9a3SuGoMvXN
jjNllf7uWrGSA9gWcMbAk/i5E1aMArjN+RmOv0tG8DEs6qRKe0ZCxVlGCVfMjDzh
Nh+uvPH4MqhCU9uEBolLPArPlr41tayc1AWpBLa63mXLeS+m38mjjMnJEmV4OoFG
pps6edbvw9pqSRbbjvRjOziZvwKBgQDEvNFKWdQaypSAk5zk6aMOw5v++VKs/4NU
fFjjBp9XdxvMcgbQ6i5iRmE0V0X3tHKy37Zy3vtbJ3CEfrAdbfTi0IHK9tAUIVo5
o5axahu+Qu2ELbxCMe2c+WH15rR0SuTXOAJvpBdub06WP9Osqz+ZQMiKP8STpXkn
OFQfoiMe2QKBgEnfTqUEbUKDRRnkC49G3xBZ+ONaUzuiHa7p86JLEmIYDZXPXLYe
BDK0aLHN7416dphqFhgmN4qJWBVcaShBieDpBNHPvDYNz8xbjS9FvJ5rFJx1fukC
xZMC8ZITjv2iZ1srUWgwKOauwClKw7PssglAtkdKDLr/ygAbeIpiYf9RAoGAPPv2
uGBuAjwHmm+nc8IEnIAALCJnAV9W+2psNzuHSxqN0GsMN9hPtoDwgsQG2UjjQRVd
ve/m5JOuKjQHLag2/9P4V8z4JTVNfY57GNW2cdzXOWDf+Xj2mfEn74yrJV1N4HTp
NGgeJ0pzhtmUKPMQjNXrFAe+TLI/guvQD9o3nskCgYEAoeo/RX+o6x0Hm+MVoj6a
BFladjP1XzDeInXLS1g46Bngu+4JlxAb0/Xw+tnkopxQLGWkFeWMRZ6vLZDxzwVl
Z+32ERySVgI1HPur5NqucNg6/Ms5KZCRgIZ7uKzMxgH6ziVUBiv693xsZj572L8L
pLWEzgClPUX+Df9VTSsG/JE=
-----END PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUU6xhWBWAz/LanKKEiMOFsRIw0mAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDC7U3QVRjBkgeNtXO74IHz9vlkL0MA1DWGglxzPDTUArgx
qaOySonFeh5kjMhYqRNulUsdCoRyNIUz02cvg0UAE323BkJUPJBaz/F+jS9rX/f3
KLqbbsxDc2l+R3uz+MqD6DAiuBJuqD/273oIdGmhp3j0be2/DGCPpfTeh8h9lM8u
eIvBClLWPsVaZAD93ahflId1XIji+D3xsRao6ss2zWkYtQC33giSTC30+DVmVbJG
wsTGkEki6SZa04m8nrCcMAMyujspmrO3Z9ybDMq77HzF334QSkG7M5Jl0Z4lA0R5
g25Poi3Ej0GBU4nPfJoChSnelV4emG6G2FxZfXZHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB80O3SW7hciWlkcRKrl6tL
iBVLFxobmIVUVjSeXfSx1fiVzdSoPKy5S1NLzisGqPkFQnngz85CWb+frFUSiCQw
jKepxTKluiWzW2IUTgu6lwPFcupd2EfTv3RLiN6NY/ivjYKtMvOGP7c7WFf21r3B
39SmTfwJoEfJAkRmi4bTOwTjVC1fV8j3idyjWudvEtH/QdOIMp7+CdDJAa+loPCT
V5jXF2gVyaLZJkilr2ZGj9+uy2w6LGyrxU2LKvuaMzFWRC4X8EmnFuO2o0Dbss7Y
zSofQc72b5XtaaTkfHaGWzLBeebu8ICo5zJwCzMkK2fWp4tAegetnlUKlEWpvT2Z
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDC7U3QVRjBkgeN
tXO74IHz9vlkL0MA1DWGglxzPDTUArgxqaOySonFeh5kjMhYqRNulUsdCoRyNIUz
02cvg0UAE323BkJUPJBaz/F+jS9rX/f3KLqbbsxDc2l+R3uz+MqD6DAiuBJuqD/2
73oIdGmhp3j0be2/DGCPpfTeh8h9lM8ueIvBClLWPsVaZAD93ahflId1XIji+D3x
sRao6ss2zWkYtQC33giSTC30+DVmVbJGwsTGkEki6SZa04m8nrCcMAMyujspmrO3
Z9ybDMq77HzF334QSkG7M5Jl0Z4lA0R5g25Poi3Ej0GBU4nPfJoChSnelV4emG6G
2FxZfXZHAgMBAAECggEBAKsYB9j5GIWvW5nyzub1pJszCKv7H+C2Y1TxT5yGGAiP
aoWM1PZFnrALBGpVd/T6UugZepi/BooHt3NJ96QooIP0l7/yan3tuvc61kmyOxEQ
Z2I2CbUsh3Yc81e3/sh1c6xcPQP8dZFTdPGWOZL6O0185hoF80xh3M+5Zzl8DWrL
jvYA0D3H+IQ2Fx7+5uL0Bhujbobgigi39b3H0DU6Cx3TTDetXusWcfX9QGT0Hl7G
xoIboZ1S9Sl+nd198O4GcgnnRcdnM7WGbrAqAoHsHJdlQNdENpB5nLN+xeGrrCV4
wycAGoKsbLBhtN/UggLTQslHbaM3LA6uqRhgzuUSAsECgYEA4LG1Zp9z5gFrLylk
TptxnjyDB/qh6NrlTRIuIV64JrrvjqzcGIs+G/WlrBiDjx5d8DyezJKa550UEpc0
Em66/hrSfw1IZrzmVdBC9/G7y0JVNjHeY8IrscTVs9YHb9lI4Vyi6IH48R4pI3xb
paLCpN77K1HkqkShxfi/l2W/NIkCgYEA3hXfObc5XiBvR47x5HgOL8U2lg8WwqrN
5YsypdaRjq2KCSd3LynpsCOa9iETxy7KrfAkIYiDEWWzuHF0AJsGbWGnyNRWdJRS
FcdG2Jw4hx9v5fNX26RCSMUqk+tDeHf1zhTnx2N/w0cCUVn2lWg2ara6VGAhTH0w
Y4/HhxEKQE8CgYAsDKqzY68k+EI7DLJNdsvfaZ2Gguwa6k7pvRauFBOmBB/SqLC9
Xw7eDFpeUq/37swbvMak9FjJ71FwE5RxyKOADWIW5lO7UG0XhaybTxix0F9EMKKY
jAhk4WHDz8HFe6N+CtslGdXj7zXBby/IWRAvokc7RuK9Ppc4aHunAptpgQKBgAUI
P9eh9DXSzFK1xXtk0QV6FYOO8fgVQLcb0Vj6pK+z9PXCJCw4aego1mEPXNBdmhAY
6eisnDOvt0PNplBBMwMVfGTLku3vUnDV5CASYiGFr9ZpDiuW7D2T4iQZ55x6M2Kp
DJtzALkfCcloHXNDOkBuxYgV6Ys/JvKKln3UAAR3AoGAVG5YvRAT7zRz2gMx0avK
MWg52cRvxnI24njN8Tiw73Mb2KOK64ObpluopIXlKnvo8QbTCkRKcOtoZsIGQPyJ
yo6eYIgJ1n+uX+jl3OpHUV1qRj9Oy38tzGaFwo1sRCNsnkL56lrI6CR1mQT4PHdM
wm871rBGNc/esbPNXmuLvUE=
-----END PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUE3WYHLRte9HfED08IQ/HsX/LM78wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCtro19tmukTk4ClxM7EsqL4nEG8deswAwgpxvHAqwruOLO
fn8VrWOruj+WCLwPiFulAFA79eX6qoUNj+KskOqhseLPQgw/PPXNVmFr4pCIhUJR
m1RsSnN8/rbQwGwqaZTNv9ziwPY9N+sRAO+dNK9JWaRQYnUYM7aVO7ze0T5TAGZx
Xc1RnRH4z66mvyK2o+RxGrm9bRRJckXHewcpmGKzWlJWBeUpgTMb7i32y83sfR4K
hKCee7YQqb4NBO+Xi3+NWxks62qjrInupxE3x7bm/uBRFGxxQEko4Nuy9gIs9as3
nJKwxxb0t1k0DPfZVBMOa6rmsXw2XAT7Gy2Mu+tfAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAy6Rn3XCcZIwdoTlqcXGTq
SxOJ2YD8vluqyGdk7oF8sv7hprQy4fiuIKgVM6H0j6o/ITZeAqZfYOJ7XwmbrhBn
XBCjWqa5GLIqjG/SH9qjxnqI7zPkVwyGXfUEUu2q934fq5hZ3/KC+9mAqOXyYpgI
pEuJlgqP8F1mc/QoSgbEldCJonGFnJo5tXx5p9a7lTz9y9EUFBR74hPfpUKWilGG
9YZ0UFnsV3NsAyngQ5/SeY1/leBWCXy6YPpVZZD8l5vOvRYeRKzZbPhJnbL22ba+
rUZ/b1sBH0+aW7wOGfR/dQgIoGgHjgpztLm4dmdwmJNRI5J94yQSJLswgTbvl8ka
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtro19tmukTk4C
lxM7EsqL4nEG8deswAwgpxvHAqwruOLOfn8VrWOruj+WCLwPiFulAFA79eX6qoUN
j+KskOqhseLPQgw/PPXNVmFr4pCIhUJRm1RsSnN8/rbQwGwqaZTNv9ziwPY9N+sR
AO+dNK9JWaRQYnUYM7aVO7ze0T5TAGZxXc1RnRH4z66mvyK2o+RxGrm9bRRJckXH
ewcpmGKzWlJWBeUpgTMb7i32y83sfR4KhKCee7YQqb4NBO+Xi3+NWxks62qjrInu
pxE3x7bm/uBRFGxxQEko4Nuy9gIs9as3nJKwxxb0t1k0DPfZVBMOa6rmsXw2XAT7
Gy2Mu+tfAgMBAAECggEBAIZ1uWKWxJTqbmiA70lvjdFoGFrpBjDeaUUqOk4C2qnq
s+RreBWfK6e6RBnyXy2jQlfmezdAcrByLRnHyBQTCSLvZYlRN8wJdL5oXnm4aG7Y
w/QLzfscVHZzd7L7FYJsROBY5jfCbaANV3XNhLPvIrklphj5cG+xMWwtWFYkJhz4
ztWa3kE0yW9Ylw+IpojdMapOudXXvVaxnmii9lqWTJROtU4WXyroCq3/ehxNdsvH
ybpwunB5bYYuMmDC6ZTfHdED/cpwGujpJUUB4qKfs9c+ORqOtWQprdkBkBrJwE4B
QvfNq7cW6MoZiuFda1BkMslxnHZ4CBlyMFZaS6k4L9ECgYEA1KlyM6PdA1IhRVbn
IK3YfC5vFK1TIdUHWsLrtK87gblps0se9+k9vus7by03EG6PtVYk5jGcy3ZYznMx
mex2YgKvf1sqyIA3Dky3hwAVCsGxmL5rnDiAd6RdlBSmP2fs/pqOtjBb/eH8J53m
QmqP1oZmB7IqQWKnhoa6WOEoBVcCgYEA0ROFPD5P8fiY0GS4EFDgtQ1m3frQ5USy
QfUtzOMd6JZNbrdy8lnLFmRN2jORCpAIfxSuvQHzFXPGJemHo26+S/8A1m4oSK87
jFKeHtQzlfxPlWxIiHAs1tjvJlDEG4NtguLFeqxVFFXU01mNPMw4FUnK038ZoX9/
Q4D5Vv27PTkCgYBoALKERMhK3ni9A4Infj3YhZD3qMh2TEu7fIZvqB9PExF5iOyN
S7lRzJMVjSRX2epYQdfr6CmJa8iEttt0Lqu6xRt1Cm4C/oluaeB7mnOv/ghP7hiM
nylc2bqWN/8SFU5XOdk/iqkCoemCqns40gqkXLg7XUvDDG9noC40V3EOIwKBgQC1
U+++8vAVFR07x86XX/2zKN9pcCmSXkUXzVOeme+LlCet+W6438WyMuYOc6C8f3TO
+poeFL3FgjZ9FQ/tX5Oth4krcDiB6XCE3/aBGFtxHnXLSzGRG3DYGSc4nN2oWxE0
bgcFwMa9Lz+42bcT3q5ZUDmXumj5VwGCAy69Eqw8iQKBgCQDVi6aAdPq8dN/AdIp
KdxiXxAz1CH0TJnioWtOQSz5LuPcdyq7sufQOP8VfegWk8mP+qM0l6qyiyLf29Ex
4Qy+B9I7DgXuGiKFPU+juAFGBOIQWG1vIFLHO1GMj7Z2E8YRycI1RRk4qxcOjRUB
NJV4QI4scqqU0oA0jHlzqDic
-----END PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUceygR6j1lNbh5j15q1GRBLaqODwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDXxvUiBZjy1HMvZuOEeXSx6ByH7NrLbdQargaCuhpNP1M8
B4Be5t+5UJK40oDpMrVNg5hdqIRGn6kH9j6sA/mNDdHt1d7alAIAAljSe1RXnk/o
r2znyAjnA3UpkQl1JT4pyPXfsE8ucIq4XcC66MWtKj5mVH2CWbPqbJbVqtvwO2eV
MC3G4x7gj3LCPxiTmGyt2v730lsMeShYN/H2ocZ1ZvFKDBInK7iLwycaM7GGaRkf
oXYodbVwZydd0DLMuumqml+6U52tWtB2mFYJeKEAauJr2h0n/QdBFRzVpDjRXU7/
AIGzHl6tpQys2fhFa+wAY4n4oSu4CHTsIiZLKWSrAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBZWLumeHQXOK9mju8KhC05
FvTz0X6osRIIu+B85ZBh4xh52xpaIe52xeNAzZ1CH7IKuLoQdSROWhLOEQu4YUGX
KvN+2/8D60M1WXtAXmQwX27ZNEVfCsveLVqV+KD3Eb6y7YsXzS+GneQInlP+b3+H
3YYPfhKwqUjYcSsj9A3u0iSu6NM8Iefwl89NYN0Rk4//dM0blK17gcT2TiGNJB5z
uEXtvL3+78oWgY/nNbqcf0yHa7mjMwebnU5RQRs0gYIWnlGmqfctwSFgEw/V8Kq0
Pgau9uqub3bfFJ+bV4wScRnOkjq1h4KkQkHSqLOVPRK86fa57pQw4FOQyykvzD25
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDXxvUiBZjy1HMv
ZuOEeXSx6ByH7NrLbdQargaCuhpNP1M8B4Be5t+5UJK40oDpMrVNg5hdqIRGn6kH
9j6sA/mNDdHt1d7alAIAAljSe1RXnk/or2znyAjnA3UpkQl1JT4pyPXfsE8ucIq4
XcC66MWtKj5mVH2CWbPqbJbVqtvwO2eVMC3G4x7gj3LCPxiTmGyt2v730lsMeShY
N/H2ocZ1ZvFKDBInK7iLwycaM7GGaRkfoXYodbVwZydd0DLMuumqml+6U52tWtB2
mFYJeKEAauJr2h0n/QdBFRzVpDjRXU7/AIGzHl6tpQys2fhFa+wAY4n4oSu4CHTs
IiZLKWSrAgMBAAECggEBAM7ECAIh+v42Nmol3b8D457XHP/jJ4XoKGeoevSqAKol
FE1hotFNyvR5ER+qF31e6fztLQQShy5lsEPA4y1SYb+YjqGpX3N0gLYhiZuoMpoD
Se9eqq0wMdesqIi8QqPOnFLOD03aVQXbMhKZRCXXCBV3dXP5YouWCaGJjMASic8Y
WbbiQMByQ//ZMUqNADwKpmF35BB+r8RxO4+SEpUA6+n/t7nQ8KrVN6CMQaZMSCvd
PzYAk8o7Mz71+WJxgLcpMWQO/hdvJH7sDqFlFEimNyPrNLNLqmCSQoF2oPyA/DZy
PO1v/VpX94Fr6+eqBSk1SJv4MJw0ia4YWFHTKnyz9QECgYEA/qrStd7i8w0J9ox5
Awl3aZ518fr7OhsKJEPWcAkcdOo1Ikuwf1hOAE2npOD46mCKdxxKPg1ivJjPlNfD
7F86OCbhjwhcr+Y1zkHeGtDBVnKeTreE/vm3K/k4cOyMfHTOBGd0UCQVsA6zB6ed
4xQsods4H/s+OFDeWj6cHHYxZ8kCgYEA2OgIlQzGK33UdywxZalkPzYk6f51rz8s
4T9OpjpnggZrIesU5PDjcwR/8WsRf3/8VFG9UX+m6G4GF1kyBrwfBROJdGDnW2zw
Yjl5PwOEOPe2K51fXgyhrYtUm0QSF1E3njWHtuXCO9sAcdznHDkpbrrrDY0NOU+t
C7NIF3bLCtMCgYEAjnSX8cyAP11n2VayypQdDCPr7jRrHBHMFoUsCvfNx0jL+CdG
z7VhzKGjyYNfOhxO2Fom3Zc3SDBizev0WODb/FUjj5Mp5ets5bfKuk1UGTt8eqQF
7Wtan2qFvAVWgLgGFkiYs8u7pgRS+VE17LR4UwIB30H3iCEUgH7NbM5gzKECgYEA
m/VqhlEjBA57gBykf+ZmEBVMQXsW/yS7jlHIqTkBR7p5uW+gHGUgBYlMvTcw464Q
rkf/iePxDNpfQtZ9Y95Lp4i+opEyiMgxp06P4UEUByoFMCL9eVA3x+KQuPsezuk0
xmrS5C0blZIIJdahzedD5Tw82gd7ZKPnVqxXv5dIssUCgYEAhOLYFE7w6NdfFo5Q
wrwABNVHpYAfuQLoZe2pQNkWySiphjAr9sb+itN8gbR/1gUCJ3hdkwjJbxUDh3eR
pn+/k44oxXQZUpw1mkfU1PyH1DJ+1hQfdNnu0V62d1PQLmdQgzbWVdmjI8Us9LSd
RyAKeQittjiV/2JVbDzin50aL/M=
-----END PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUD/plueTF8nkLakTDG0grFBs+OUIwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDcF8mA8F+FreurCbiCrW0e9t6QrME4w37dwoXxN1YamOO/
15IVMCd4HJRiCp9FN6Z/MrZeBgVqzzZW4XwdH4EcIAr3yFkRo21mxvlRKPe70NJw
ZByFhtkzTo+Sb8drAbl4LsBb7obxWAIhZvMT/1Od0QH+7mhkSi11gxR1AI9EF7cd
bK85MnAuH4UXDM4w4fg/n4gFlNiHhH2gaF5xFwEn+Bksy/lxFA9lEXnOI4QSTeCO
UtTPN7q2Ns5i1tx1zLmQDFfxkaC9BNq0GFDCRvgvEdFW3VGN44C8TTBbXDucdAFK
O8Lmhvj59Re4ulJuEeHS2Z6BTwEWdRXFPQ2j1kiLAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAhakbfc0tiTSdyXNqxXMzZ
EdQJOupcHLuBC4rIN5qlV416r8H+sBKMJoKNUjI/pUHdGiIiM5bsfVqBYeVF26WS
B4VWaj6KG5t+kmp+DTjur1MmgKt2mgMtbeziCe0N34mX7EdO6JBYriGQcq5B8+S+
WVcM3JBsTi7ou+6+V0AIs80e2BpGiqpkTOi8Weu8f3x1WjSbGjFCck/Om1M67v+O
SJo2TXv1boz1yFcjD7Ha8qTzDSDRQQJ9Td4LheooCd3TSQ6bTG7mNDaYh7WT5Ra6
TOlbXp/CnnSsF67XY7w4LjPXhOKpGNriDiyq0/DeKx+3Ie0kSCSoQZe04Zm40+OO
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDcF8mA8F+Freur
CbiCrW0e9t6QrME4w37dwoXxN1YamOO/15IVMCd4HJRiCp9FN6Z/MrZeBgVqzzZW
4XwdH4EcIAr3yFkRo21mxvlRKPe70NJwZByFhtkzTo+Sb8drAbl4LsBb7obxWAIh
ZvMT/1Od0QH+7mhkSi11gxR1AI9EF7cdbK85MnAuH4UXDM4w4fg/n4gFlNiHhH2g
aF5xFwEn+Bksy/lxFA9lEXnOI4QSTeCOUtTPN7q2Ns5i1tx1zLmQDFfxkaC9BNq0
GFDCRvgvEdFW3VGN44C8TTBbXDucdAFKO8Lmhvj59Re4ulJuEeHS2Z6BTwEWdRXF
PQ2j1kiLAgMBAAECggEBAKUzlaSayJhmu4ZefYhY9JdRZi3h/gbFduytniw5BQBh
0lGlVZlh075sdVRB9NrXsrm3LvvUOSy67Ga6SZbyls6tno3ubCy5Jt0GbQ1mWs03
KT4DZwUy+sVwKoQYMu83FCgJr4lRuShejvrTc5GHDRRgVccs3F6q7wRNp4VLLj5E
ymUIRihgVbv+QveJly92+rjNHnmAojklu5FyjxoEERbR12RTsDpEYurdEABH67/A
C1ginviUORrQJ3EFNAbt2cHREhP09MlLTvOgmHP7bo++CfKmSZrxmv1fFUrS6fko
Z5jKzleszXILXhg5G5hJX/fn5STZWMG0/8+eBj4GTMECgYEA8MMCASq08UmWHE5g
lI/Bl2pdTQxoUIT8/QEzq8oqVC7PYpd2bNJKWb0tan47Zm4Mod0HwakPsdZmJeq8
k4gTfEXbVTjCkXJy4axtsQ7fj7q/Jz+Cz3o2ir/sfsb5S3zK8iWdsVGJRhaGRNNe
oFmC1O0GKNYUnp5J+/y7s6ZgYMUCgYEA6gXjZfyjOY02Rignlvbw8nc2CSVkggwQ
Pdjgg3VSyOTTtVgI4S/lU6f5ZwvWZqAntThcUL+5HbzA82btAPc0wqQv0xwGWB27
MB2b/U8hyOaqCveWJVAGxge7kG4VTzvACVmP1bN90V6evg+T9pnCAfERTLgZtyJ1
SE39wuzd+Q8CgYBjYVt2d9ZwsttPm9qp+B0FD1ar8y8r7XkwRkq54p1OWnQoUjUD
/lnKaRhSGQET6uEz/zSwb8SWt9U6WYa1rzm71moO53sI5qEdHju5FlaZ0ZAN911b
nyrcYxSP0DofOsfa5EQPaYSsdae+yTEKJ2il06DzQksInnYTmeMw6MBnsQKBgQDM
vfQSETLYsiPuw0jHuipZZ1SeMdm6MUWwZmMef/G6kwBp4qh6I0Y2p3n63o9oX+v9
j16swt/5FV+WU9E8jArb03uH7jfatcBEO1NzDd1X//5689unr1kNvkwp8zWviW3c
gD/nzk5gc7DcRZLFKAZlXnwtK9BLudj0Nk+yTztwnwKBgQDh35ck35wwTffrrCo8
lXdDGxqjH2spxuesSPf2YxTFShbV6BLDoQ+hVD+QOgByQQP78Qv+ATHEr2TOtV/3
TdTn5+PzxmV+TB16BvImbHFp0I5jOlfGO+tkI9IGNfnh7zuXbcD5ud51E/aRRXAs
1+6WZaW9kC9W+BaaIgTvka1leg==
-----END PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUGEsNvk3tP0A/OO8kzGApLrkPgqAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDfU/KtYwJBDRNT1ohOQiZyWS21uU249ykMPIUmryL6/2wf
V8QGoXSPapX1nDi5scC6/m9WBGeQkvytkqkfDCKXeQkcwDWslstYJrYQUL/aDnLE
Kd/EWkoFiQM2ALcPRk/v4W1s7e1UfZCn/LWRZok1mTvLhO7/ReanpQ9p7AcKgE7b
I2HCEpe6YT8X1eFWBQnsep3FqipKRTfOL3lAv3vd3ufahcU0rFY+REae5DKSyKzK
rlWb1CHUxEIHTHvUdmCRVkEBUfudbsS/9SDi6N4KHyW3k05FZ11E0iM0ugimlVAe
h8A968IFxcZj9iMU/WYuuOQz/xsrkie2VC0Un3P9AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB3bfnPsdtBRoQhCzF+TbF2
tJjl5Aa22Hdgkp+ew6X1l+BsOtSyKnWhfDE3Vc5ImWbwXCRXqh8R2GrlG1qACRFr
EoMr7XwYSMxF9BE/dsBNiVszs+cLoSmVKEzLdHMcdgptaJLbKRP+p3/M9qUgs6cS
7Iuwl8mqH0ebCgSMYrteVYu/XPanmTRfHIWNIVa0S8Wfrcu1FY+UiVSRVmSCPlGS
HOsYKko8JKlLG3ZpKOJ9wDLGIbOEelqCB/ysYXbzLTl/qzbrfdun3pk4rL3UPQir
FmXo/0MLHgnl1qJpHCXsrTIpxzCR2+7KpkA31JrM01T+6FBGEFQBVPo6zIHlPLDD
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDfU/KtYwJBDRNT
1ohOQiZyWS21uU249ykMPIUmryL6/2wfV8QGoXSPapX1nDi5scC6/m9WBGeQkvyt
kqkfDCKXeQkcwDWslstYJrYQUL/aDnLEKd/EWkoFiQM2ALcPRk/v4W1s7e1UfZCn
/LWRZok1mTvLhO7/ReanpQ9p7AcKgE7bI2HCEpe6YT8X1eFWBQnsep3FqipKRTfO
L3lAv3vd3ufahcU0rFY+REae5DKSyKzKrlWb1CHUxEIHTHvUdmCRVkEBUfudbsS/
9SDi6N4KHyW3k05FZ11E0iM0ugimlVAeh8A968IFxcZj9iMU/WYuuOQz/xsrkie2
VC0Un3P9AgMBAAECggEAK0mbTU5WnoNJTsPTkc+yohF1EbdEQGjv9OY6LOBfmGUv
8PdTELH05OOVA5FvUVcJ83Tj4bli1ZwYDBDUZSc2AUQ9puv+u2BTM9f1DD6KoVqR
lkJDlEyn8mC3VZ1X3kcTsXxxeF651Nmt01HhY7iLOe9krrMqnCJRbgdJcI+GYdtW
MQdYm95c3Jwwuvw1ePtEqaQ2SKoFwGT+k0qRHeo/waIwo2BNJEnyqdAUH5B6oa42
HwHkIldC5smV73hxuIlgiUmUAfy7My0YNef3KZAw8BZa9M79uYFPk5/n/2cRjEdb
Jo9mhKicvE5uPQNrQlwrW1VKXu6NOlA9pW3aDystYQKBgQD2iDAvGJmVZX5Vo5hy
KK7BoOTEEbjGguB4HyDrO20Gv2bFHI4XXJyz6xUoy7rTJfXLWxMgXct6K4ucgAhs
6QrfEPMivPQH2vDCOTsNRCYUu7VvenUtpmvpHy7pUVnB2oY04ul/pq/EdpHm67eO
BOakF+WbdBwdBIHbkEuppKTJCQKBgQDn56A8iFJxNl/FdTA5m3oUr5sXdA15ahya
RkzWromATl+Vj5PAX2KAxoX0s0m77ECoDofHJLGhbs8Sc+Q1RUdpLxa7xPJVOFwL
dDP1ey8oV0Yzr6WK/0qXfwZ8YszmlL3h3BpzsmXHfcRlsrG6u5R01WqtaGzqLxhb
/skvCZQUVQKBgH3PkG9oaXBxZCCGJVUU5+IOntBkjtxXjAAhOqZxJDmOUf8DjIvl
il7S+HBiT8xTkfUeXEtnMmD9efj66dHSt+aQetPeg9bCZ51moXkqrxhjlrr2Tnhm
dql4bXNKPbkNMPIqXqjzQr3LGLg00O6cF6vkOhu0DGjOlQqcv9AqIqIpAoGASiZi
stg33CExsDZPTCwtdc3MfkxKPqcyLBYMXZyDNLZak7zL1nfpTBmuHVbyXZcl+VZk
DcXq0h5XMaRCtNHJCpXW5AUOIzeZHsRyFKzloDV/qekgunf0hspD7aO9toCa0kwJ
XTMOniHVmVrwvy9ZQZ43tOit4pdaZ5fpBhQ+990CgYAdeLfNGaSXmt4ex+Wg2A/n
3yvHpLuSTWHEALREY9b3CS/8PMKxpHBShbrfPuBSiinOwL9Px8ZuEygPmyS+bjA+
+fjR1zprPU+8ujAt8Sszxb22DBa4vq4qogyYWA4Pt5OwiyW+uKQ76w39IdZbx06U
/HMX1zYDm8q2rO1hOvyQ/w==
-----END PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUYuDSVIYA8huPudIdi0WG2abkweswDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCpomQtc8V53Akl8GGEiAmySQBqEdpHzezrfzmZULGkPHIi
brx5QAUpzLTaRQL8vTKls0wN2qjf3k3oQXB8NDuveUTuosms14KeNhSj2AK/3baH
aUCe+F/UnPb3ns/YLZltuGUzsf9mp8P9yluTMhUqLweaRG4rfWkzu8aug6uuKt5o
5FBV8AHLLNe89WHBRDqR29BiQV7rrdfjVEPrlW0ZuVJ2obcp/OvXt6c7XEq/FgOG
r7qVxK9VELEZM2auH+wDHFghIdLgsbj3dUNOqxqhE3Mg3bKiTqxmrLsV15ZLQCcE
erJPLQsqjQla6+yGPOKou26C3n0ukdyWvPuipjqPAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCtDYfrHPXlP8OR62xr/Eve
dD+2Sl8KLDX+ekaV2p6GLO6+nTeD//8NFG7gh22LGBAyGYSKDcFSVy7fIl4iV98t
qXpYfC8PA+pXIhCI0bEHz0Jd/g0oCgtbvGs/1SGWYzVvvfrDunGM2d/IRLFtIwde
xNz661oFWR4UzbF16wPlxZ4S2BolgBAq9V3vr8G6r58/wfKLaR+kM11u3MupI/iz
z/b67IsYicnYf+r8tLs0NMxI3nt6bkMth4552GGOx0490faxSH2wvS8r9OhvHfh1
yzpmzqgcGJ5vVyzPcj0ADCe7USBsTF5ocL5wLpj5i1OWtGeuevkyJ4CUHOUn2l3T
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCpomQtc8V53Akl
8GGEiAmySQBqEdpHzezrfzmZULGkPHIibrx5QAUpzLTaRQL8vTKls0wN2qjf3k3o
QXB8NDuveUTuosms14KeNhSj2AK/3baHaUCe+F/UnPb3ns/YLZltuGUzsf9mp8P9
yluTMhUqLweaRG4rfWkzu8aug6uuKt5o5FBV8AHLLNe89WHBRDqR29BiQV7rrdfj
VEPrlW0ZuVJ2obcp/OvXt6c7XEq/FgOGr7qVxK9VELEZM2auH+wDHFghIdLgsbj3
dUNOqxqhE3Mg3bKiTqxmrLsV15ZLQCcEerJPLQsqjQla6+yGPOKou26C3n0ukdyW
vPuipjqPAgMBAAECggEAZZdUqYfpH2bwr6D7thSGwhhIQD363P/twMfL5g7WpIZy
0D5Db9YwgW0QbpvgAx8IAwaTKMToWFJZlBwE0s2xZRCagNRLNdFHb5rx14IZe3C7
zPLy+YHEWp+6pGefEFeWyIgjS8dxLriQfyC+oTPgSwgpZHFRDYipBYuSnJdMrRwT
KrBKjPjef4NDf/F2xUDZxi1BJDJzjog+3r964cdG9homLe2UvR1QKfXZnXxVwpgj
Z+x2I/tEGlVJ/rfWywddIYar58/u3xKvyRYMlV/OlmDQfOtuxRqPscNWiUJF91E8
BjjIZM+Gb4ndffvGo9/k92WwshQI2D1LYaUX44WPKQKBgQDfbGLp0Pc+VXUPt7/5
cX0fuwPWHlYoVIRMXtDT4G5aNUYm6kwukL2HdiQty+6zf55dP1WEnZr3bGlW1zmV
NjE+gn8iWcWsNo5zhZ7I1fPjEZR41hd7RRoTTPRfgy55pCa3Jxup8h5grzfuT6VB
oEgvbMPaNN6hQKcCVie8c1sA8wKBgQDCXj+Ao+EBcmFEcQFrN0nT6fD03/OkUWLk
9CFG7koqlFjKnGMv8Nm2MMm5c3WUR9lygMboPQSV4j1VmcNBKPG/sA9MUTToT1Jq
oXWYkDuukW/kYoeTm5PcITHWKJtNatSdxE6B3Ck183sPQ/YDZ176Zh4TAvDU9H9l
wvUT7Hzm9QKBgQC+LzonxJyiMAZ8wbKl+IhFOWGzo5E9tWwEwnVK1nG5Uj4MJEeD
H+xl4hg776uamljJEX+PasWeNmeY5455yG60wkrMh9RvmuU5yxV16kI4GR/kmIHW
ieT/ZvNiVn16SFQ4dg7jZFmdfanDr4KB0ZmA3Tn+hiC47Rr9Ly+WCDAAJwKBgHcV
uYB+Z4g0ZQXC2uSuriwJBBlz8Nm3B4lRTeYgbw5hb3lLkbW4shrfD2jxJZPg5Ygz
ACsf32RZhcyhdbDBfkQ8gVL32huPJeaw39TGYdqVvuFFwN0eD9xp9hfJL0Wic3vp
31PO6OzmLXpv4BW7ysRNtpVdUuKWnkthxDgdx3TVAoGATUxRuwlAj4sQutVM4nJl
Rn+EjohYj+5eQbiKX6PtrPBq35N+HBiW/Nll3DNQycQofWPiNfeMt5L0OzTwjOlJ
e/LWCQhKDlw+uvqczJtWR8c+YIJ1Q8/c75B9FU7ZDZBZ8UoX1Tj4V9N9rcY5TctQ
/XazFAYtNVeeJiw6nKXrMYs=
-----END PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUN/JXfTKKgYd8tAmAAwPecG1x5qswDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDRq9bspUpXBycLMb0rLXGVMD4xnT9+VfLF9GD5EFVOCG9N
t2VmZ8Tvlq76G/5MI7nI/wf2E+Z5e46DFdsCwH3uZRja//eQQ3jhiNN92qPaHpZo
15CXLRm0HUEX+YHTBCQ4A2evFhH3CkxVmTwJYEIfQUf1N8XRMTV+LUGdjeYJSMR7
GuDrRft1AJDmGEeECp9o/DxBc/Na6a3hSM6EKfVacXh3XZBuRtfXvArOiZw18U80
qzi905hw0UnsCd34hHc30gYMI1ZGnhafFQRzLQuIAzCQgKGZJ6S6mwY1Ovu8qi6T
vjGGzWc58yRv4SgiI+wMEJGcfDGEjedXnH5Sb14VAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCY5SoXBJC1OtM3oDPvrbD0
ziondPDLGfS3zOXZ224c9s3vV8VOfUtdamrjn3OJnip5U8jlTg16gpSOqNK62CTl
kgRtmR3tBLZmSfQIDB3SVN9OLWS+bpb2BtAdrUu/3vdP9EClbPMCO6lCDnjt2LBV
qGmfBl57J9p9j/2z2ln+C9AboGmJGlNWiu56kOYUCM3+WYSSAq56FCGpqMSzBvX8
0q7lAy/dG07fVtnE6FSQ44nEmqY9zq2goy0F/w3h9EPXaIuixz/PnJuFhPHVZLZm
GmpR9Aqxnu1EURt0I/reYetoXB4oYP8b+3LtQ00o64fQV7byKNSrji6Nw6VVaCUI
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDRq9bspUpXBycL
Mb0rLXGVMD4xnT9+VfLF9GD5EFVOCG9Nt2VmZ8Tvlq76G/5MI7nI/wf2E+Z5e46D
FdsCwH3uZRja//eQQ3jhiNN92qPaHpZo15CXLRm0HUEX+YHTBCQ4A2evFhH3CkxV
mTwJYEIfQUf1N8XRMTV+LUGdjeYJSMR7GuDrRft1AJDmGEeECp9o/DxBc/Na6a3h
SM6EKfVacXh3XZBuRtfXvArOiZw18U80qzi905hw0UnsCd34hHc30gYMI1ZGnhaf
FQRzLQuIAzCQgKGZJ6S6mwY1Ovu8qi6TvjGGzWc58yRv4SgiI+wMEJGcfDGEjedX
nH5Sb14VAgMBAAECggEAU6Hkd74ymeYbd8aeOwPEY4q7tBSSB/WGgdlJeO8/54FL
zEcT5jYMArkrEE5sL7isWXUImuozK0/Sd40XL9DSKm4e7PPerqeLJwLpwTCd3NoI
isc5QGPX9dUZatO2KhJj1AffqqH2BoEQE7CsltzTYx4p8rENcbTcLnkkzBCWqiqo
NPJyGyyqP7iD5n0gWv+ojeXH00ktghop/oPldwIaarEkEKjURnZhiYDKs1XtPZP8
yNx1uXCcvpXTpli7++tROOlokqoqH4ZiX7OQo4GLwV/cW5JBeVz8/gg4oc3knn1T
E4h7rkmyMLwKeoiYGyx09bvxSHeJ4hTtjEiFA2CC/QKBgQD18A74b6E9UQndBHgE
uI7xufylsCbZeuu6p1HcbNPbhYnIjh6sknsul1FomPOLt+mWYXefldIAERm4nDVo
O6TAEilnozj5eUN6Oxl7Ri/HBJMAYhjDKBlUwwp4tGiJAjLh7ddpkhsQ2MmQuvsA
p2yEhxBrrd+gNybSzeyUoEn9awKBgQDaP+1ugSjEt7ay83L4ODcVIcKC+xhtIfiQ
H7rqHFrHHyF/dQNW1ftacDaSYexG2TsGMQk/Vd+hkVAwn5cr+t7mta3GZOSiukCm
iQpAX6CacDpgx6kwJhNpO5/NxlP1AGOPlbzL04shlL14LrvNhdDz/7fbEe1T0Mc4
4LUer+NyfwKBgHsWSmfMdsZZaLZVJjw2olQY4XmLT+ZIvvIMC8xmKyITE4Jsnq2A
ImaPFQ9kfX/P6/h3j4cvVIr0BAuBIrmoICyA6ngUGM/DASKLsZUg64iPoYLvlbUW
vJbPhs4ifK8ViqHIh6cumJ014qus6TLKmGU7s9wwiVuGPsgCiAVas61BAoGBAJWq
LRoQfHKaQTFqfTb25d8Z7ZeAtXlxSFEdUUJl+2J9WK1dAtMznlCgjuvHNw5GvZE7
Y0oJi3fyfHk7l6FTQjQX9nkMizWEX/1UELGgYjRGLeJcSQt5sOoDN00Xak+i2qOG
XZexE8INi/i0o5kG4QnSHLSgEI3fqB67CblniKPlAoGBALhkgKNAIFriwetJUhGE
7FD/9YtQUE2oGc4Ipey3zHgjzbt+BxCrNGlCNtxeqRKW9yy1amUUJMFptHlk6ccI
YexcFwMqtA6/fzs4Lbv18bRE14yVpmZILdrWk6AYPOF+3RiOiD7CFWDWV2sMxTyr
2+6SbxkutiKAmAd+GQ2QcILk
-----END PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUH0ogquGB4mndRRHavQuBPNDRMc0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCfuudKm7y0TVi6OOD54Ir9f0LaXBWRy+Xdq+0Jtmbc5TPk
9XMgt4DP+U6KukAwSb7jEudyiHjWIeB8EXkQ6bVRPWUxo9CZtzPjYVi8yZhJnOqE
r5oSgiS0L45mEuhrVeero+K6QtMlU07UaZk2OPq+AppeYLexMDvexxx1yVf36mby
VG+o1s/Eu1RPLaViaF8Owjl/A3YgccKUSx+/KKYGRnSIaEpoXdnLbD6HfgLWZbw2
qBg+eiy6GGYVFTJ0CcnfxgTJQ5wN9je+VFEPvdJQpuU/aBZ/CLxI/BCqF91xRg/A
kND8+WqZI2X5ET+gnRuDA0SzNARyUx6ng93vyCAZAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBWOG1W4dxscVyJPt2hczoN
OOuS9uA6cHeqtRyXxwBfCxFMTBJn3nEnNFNt1CgLhyPQY1CFyf+8ZycaIfeeCqE2
+qHdIpwoFOF0usRUi1oH2Pb4F/62x1EERDdl+tDdVE1vgm5Mh/teDBmHZwPnAhyZ
rX3FAN/he6JXmZpQCuMazJ0PhcMPbrwtv2RBkFGneQamHYbTcsofQlecgRIcGRbO
N5nr1d6LGoBlGRNFJRcH+9VZtw09dOixh9+uzKHIhzkUpJWrfpZXGq/Zxjjhj+7G
z1LWzIV/uatBy6TyHsnHicPyc3dYW01OPE3TjsiFMaGFB2A38IcyqP+3PmzD5vwG
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCfuudKm7y0TVi6
OOD54Ir9f0LaXBWRy+Xdq+0Jtmbc5TPk9XMgt4DP+U6KukAwSb7jEudyiHjWIeB8
EXkQ6bVRPWUxo9CZtzPjYVi8yZhJnOqEr5oSgiS0L45mEuhrVeero+K6QtMlU07U
aZk2OPq+AppeYLexMDvexxx1yVf36mbyVG+o1s/Eu1RPLaViaF8Owjl/A3YgccKU
Sx+/KKYGRnSIaEpoXdnLbD6HfgLWZbw2qBg+eiy6GGYVFTJ0CcnfxgTJQ5wN9je+
VFEPvdJQpuU/aBZ/CLxI/BCqF91xRg/AkND8+WqZI2X5ET+gnRuDA0SzNARyUx6n
g93vyCAZAgMBAAECggEAMwiZW2oUyZqozZ7cqpmGbuXZK0Eelx2JTODgdCj2Bn+o
q++MIBjhLBGgeYx2c7csKQriLeLSkL/0JE/E2ZWCG/m8ujZ3sJUrG+v/WRoj8OkU
uN4OIPm51mQXYB+MaLbitSFAkHhHU/ahChbPH9bmrgzQ23SVXCRoDI6bVjrFQ2z8
oqb+Ct4o9GVkLBwdSDdFgTcPTcyCLLq/sof9B6V9SETNO9snfyaN3p2Oz0Vgd6Ib
tcfnodAHZIXQw1oo3az0SP6L1lR/Zag61Y2oz2Ll7KZpXQuoDIK1T7hFMCFEykf7
6cfDGb3QeFvsNtIvnM53+ZHdMMqyFLxXx+sor25fjQKBgQDUzzO4pOpu1PuX2sQn
hLSed9UMqupbIC85ww29XazjZb9nU2kHAUSi/FYadCtOSNrtp0McYD1QbOJ/T3Ib
OkOc4pzywk0CY/EPJiuQGuBMByfAs/Yv4Wz2iQM1vZ8EAj44c5w0pfwlRnRIfHir
SxQP5eXnHUn2Ck7HncPVTtpxCwKBgQDAJeU6GqYkfAN2EEcYXKAoTxRjxhoCsV3U
caLqDpv9JMNIa/K9VCwKuE3i4FnDTB0o9eCeyGsiJ3dkgIZFeoZxL6TDR/b7iyRR
DYXNIg5gNWrfNJ2erQdHG5xqZAyEDYsYzFFPQtFHcrxcdCSZMBxPYcWPuoUxg5sX
pKRVnuXx6wKBgFHqjGM4ABG3pD0Y9case4ZAZF8i72Eya1tVrNVG2MUTpnDUl6od
n9kJPu+h5gWVX8h5SQkENrXdo/YTk73NWLdsN7PufQw9gk4tiDlJTyuU2YWBAHP/
1xyzMuwd2LcHUgIS5n8RoZSLoTlByIVPOiLAgRXMnWq7HwYRwY87cjRvAoGAahOB
nLYhinq8Hm2WEijwcdBWXU58BYiNWD7zxWsTSokFFfIiK8tQFQryVJGufFaEspwq
yP2zx0Mqcl1RwwGFPu8icnxEKVIDVou0li566ToUKe0OJw82uVbQ3xsknbIsXCBP
swYcKul4e0HTAo7A0kIToulBprgU4tSNtIboQskCgYA1t7lDpzjyEslx1l7gCY1f
hVw+uFE3Y/ITxBvCqrTiUGlsepuKOixf2hACoyRgtq9bzlgOu7mL62um6rzSaxf5
j0RaNeZOSPCDrLGFXCRkcsBWtkyr0Xt7e8rNNJxfIkaOPQ4mRSFs1MfY7dLYTk+q
t93+b6J1Gj2wv6Bl5olceg==
-----END PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUchZN2ld769tiYoK60GmFQF/Q1z8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCmD4gtULYn91b8jZo0/I0JUA6j3lbV40/ivqH9AqEoHiKY
qQMbT1IywATq0/oaawM0sz3JfPPWpRVMVHHXWZdNtSinnXheqraWJX8ZDLmMKhMP
srRgX1eDjY+brHB1+E/0BGhFmajopdv2RDlfjljh+J+/nFMqvR5m2Eap0m6peINV
m6gYloHwCfa/ieYsF+zpHJNX5t4Z3q6BiTZPwcmxF19gfS35ea4SEqW9Skvm2+o8
VbOiC0y9VtSl925phEn7ptefu2vT+QtgNVllMZ1r51s8T76bs/pVBUTE0ZSycQsU
LAgNP7luy+PepQf5JsGPM9M71idQudkjiNKRe1EjAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBAwLNxGGdf9VqeqG3RO5lS
a4B7k276NjG9Fl1Ys5BbbUzpSPwLunNGGNI0rhlY+uUZDCg8kAdwfnrMwtoTwH8d
ez0cYCW210Gdtg0z4X2L0oHkGMxJwsRvl7cp3v1k5R1iupFzdE4lUsxapfRrQeOt
JJGVVDdQKKZ86DuDMpanrBGUWl8e4b4/8bQS/8PgCQEJqkJjVB4qS9km/CV83D83
aeJVOvBlf1TfJgmxKvUksgnKUoN1L1sN6JIcWtVqe4qj39wmCZLIUaupFE0fmUYt
JPrsEwbkgm1PN+n0+gyV9uNwW3WFGoildZ/hCN0f9KuH2uz/LmnMpEmBMnnk/DAS
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmD4gtULYn91b8
jZo0/I0JUA6j3lbV40/ivqH9AqEoHiKYqQMbT1IywATq0/oaawM0sz3JfPPWpRVM
VHHXWZdNtSinnXheqraWJX8ZDLmMKhMPsrRgX1eDjY+brHB1+E/0BGhFmajopdv2
RDlfjljh+J+/nFMqvR5m2Eap0m6peINVm6gYloHwCfa/ieYsF+zpHJNX5t4Z3q6B
iTZPwcmxF19gfS35ea4SEqW9Skvm2+o8VbOiC0y9VtSl925phEn7ptefu2vT+Qtg
NVllMZ1r51s8T76bs/pVBUTE0ZSycQsULAgNP7luy+PepQf5JsGPM9M71idQudkj
iNKRe1EjAgMBAAECggEAL2NTSwszUChnLF8EWIaRgMzVwLGcOiFKFLyt4VO0xYwD
92iTuGFkZZMiVBj10EAlhA56XVtJAkHN2CBo9Dle0hAWb+6iAPHadPJyWKWm9Xa0
RdCLZM0QXjwxdQ06co/P0STI1MPKzck3AgnqDXjDqIiYncdwfEvHtzWUxLWGWtnR
WZTjj9iVbStcgRgAeljtmDlp0RcaGURoWer63TbacOU5hRj3Uf0jB+1E1P+OPVSn
GC7qWZACpW12CNOLc9wbZ1WvzwRDby3ugXqo7EoOIaQUGQJlX9XbZ6p2cSrvk1VS
sEbGRaVLjgoOLupAegI6TUC1+1eoV7Uiao5jAZhxoQKBgQDZWMju6BYd027MHyEA
B2oRtXXuaBZy2KwYUaksGsVa70XriOqVn4AA9HxT5XWiKvngDo+6Q2Gd0/ov9uhx
i1XlWWeCDsHN5Ud0HKttOc3BnyOt3YmICUBqW8YLUSMYYNYCEm/ZQAXsPFvAjiUO
Wp8eh5fK+u4/t1Io/tUthrrsOQKBgQDDl9O4frcEg/hOguQEot3gOSrRlNQgPMFx
m3KTsLub9aWd3GljLDj1ExIGXJpHYm5P+mMU/IMiSO7CqE1gJObCGwvLqPTD21jW
+kM68mDXZXgQ87JxILYnLpQlR8AbJ63zxJUw2WMRuuqeVRDcdZ6MA1MqckVmjc3w
Q5JcTV3gOwKBgQCuDR2LxCvB4sl9iQgiP82/NLOmIZCok77tEqgI+79DnQ0/GzvQ
ahRVr3PIs55KKWRE+yQ6Iy+O9mwJ8Q4fr1cv/TKYwjyNJ6ja4QKey4VsIoat+xTh
7Za6FZg5A9a49QMsUZtkPJMBpSxMvQgLwKJgDnGOSPh16dZPohMRDC2wcQKBgCi9
sFEmu9KJ9qfL5dj9X7/7yGp9WK4aWaTjXztaPcnfog6+wYjxxi9uOHvwwAYMf7PT
EN5nNp1mma0cR3m2VgaqgYt7dvhw8RFecbCOmhNjxF2rlUixKqAAuMUHLAG8AyTa
lsTlExi3WXV/fJKfQVYivykBQml5MiNQv+TQDLTPAoGAVNb5EodqcFnLoFSB9N07
D33n32H2XUKvO+TQU5Y4Q6xFz2SwcQAtOUAtpR/2vhxMML47PxhpveeePf6jwVZh
jFEGMGRMIalqyxy9sDNFr0QHDZExZopvy6axylLmm1DgLO55pP61P4CnD408F4sS
f+NKfr5p/QNnq3RB/S16J0k=
-----END PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUa42MrlXu0Vb3u6bdR8DwCfMsPV8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC7oQMwbqJoeS3oiLCgTaa5ruJkb9tPKzPKwHSrRcyXsFim
wNp6dtw3rxT4i7Fa5gAe7Y4iH72pQYOVMfTLH+5gEciUjnhTZwilMi/PzcEbsjVV
UUr23RoZ5iLVZNAcUP8lcf1eSWJk6ohmA738artmaXdcjXO3gL/FVi5E8BG3n5Dj
ZcQ5e+eTm0CbsF0cBa42TjTyjr27/o1J79kmoHVVlZIxZXVJNMcnXHcMF68UQi/i
czEZdpby/T4bnU8e/fnXe94v5Tsr1wWtaqQp1xh4r+Ngtn6ovu+JGHdX5FGsnOGM
Wjnzu3gXm4BvSVq6R5OZptP8NPZELRq4S5RbZoCbAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCcYWvDW8WbK0OkXEDGR2DZ
yv8g9+Wtg77krCngqMnLcd33IBEqm5Tc02WfZCd786yj7Qfz1v9Y0qHQodibgfYK
FtN7zUMaovGltm8M0sP5XdQKh/UAjmvCtOn/qB4mYImkx5vkbTF38kH+wWac7kWg
3ehxJ8Xsv6SLLNb0KQgrFt0HblVC5Xr0JfHLKDm9j4QmIjeE+DkS/xW2ERr+E8MR
iXgoWjbeXfSwvstAj3IRSN6Wh4gsi38unpC7sxsrCalRvASgkvaAykV20HcaueVq
BzQ1jKOQ2zKpAr0n4mXtrtvw/t2VNVRu+QEir8Kwm4TtTHsgaIuU/sVchYqDsKgy
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC7oQMwbqJoeS3o
iLCgTaa5ruJkb9tPKzPKwHSrRcyXsFimwNp6dtw3rxT4i7Fa5gAe7Y4iH72pQYOV
MfTLH+5gEciUjnhTZwilMi/PzcEbsjVVUUr23RoZ5iLVZNAcUP8lcf1eSWJk6ohm
A738artmaXdcjXO3gL/FVi5E8BG3n5DjZcQ5e+eTm0CbsF0cBa42TjTyjr27/o1J
79kmoHVVlZIxZXVJNMcnXHcMF68UQi/iczEZdpby/T4bnU8e/fnXe94v5Tsr1wWt
aqQp1xh4r+Ngtn6ovu+JGHdX5FGsnOGMWjnzu3gXm4BvSVq6R5OZptP8NPZELRq4
S5RbZoCbAgMBAAECggEAdQI2YO+9rHVVodwMeguy270qRgRTug1xIRHgMCc5Lae1
wVgnZ5PURY2UAGPtWIhyrtbqenFc776BdntO85WYLKUqdypZ83kftRWVJ3xi3wjF
pc0qeMTt0BTqyDU0a1Q/qXRq02/kQpbYNPZEdrOA5p8C5t73uQo7ja7u7+LeyalR
aJz5VY46QICN1A3dqPhzs7DFbZYkv4wXIZTb7UyuXu+AOJDOJ/4sbTWQGHBMvYeb
dcU2Fskc7dfMMphvi22oEphS5Ez6HFkYiOyePtH3MSlags/TyKK4XF2U0YtZbHZA
TYem+a3DQh9cjwKPHPazGd7vTDolfgdschS27/kSYQKBgQDeqQcji7kAqIjHUFel
E/e/zzUVaOPQ/HAWMMcqaiX6ax42RUISV+4N/6qEWTbdVpuUpF+7COHHIVvvZjdv
tmNmdhVD+DFTTWjO9Kr6LxhHC85neSzV9rN1Dd765JXWpYGbi6oN1vzo5gjRYY/y
Hi+oBw/Sj8qaCZIythStLx1MgwKBgQDXuSu9vUK4uYVPwwLrbTncb/b0IK1aYOsW
6fr1zczZxta5UJCicIQrC/JbPa5DaqqSSgkdRQn+/dXPYFg3gMY/8hDxQUMXwNhx
D+7cQYZLNftUkSVSgNIvDw/v/Bf0aHwrSGiWPLXCWCD6ziPasDnxzsjOxHZgPJQm
pj4czIzwCQKBgHl6CE4JTb6hNDZhi9+hPDpmZtSubBQ5lUFWDWMDlILB7DK5qGlv
lY4HnVUlgzxQowL+hsf4+Yz1kz3SK46EGEjvRXzWrLqA8hxu+dUS2pDwTQTA5Ig7
Vv8WuT9ydJktpL9i/D0evM6nqcnqC2mRtHhcmfJLxsIxVJTcJ/2wRbDXAoGAYIe9
qQPdrWdm3hA3aD3SHHAFo6xTphOkXvaIlCFpPzIYt4fzkJykp9aKtoVdS1GZzihO
98gC9xWC7W8BSqTXEZoyNqKrcR+cOsuUaP7xJwqa0na4qrh2VRR6XzsBRR7UIVIf
asrz0mk5KMHBjYQ6CZgsh0mmZt30tW7CcISftHECgYAavwNWxF/Xjx1A4J0pKOlP
wz6yGSs6Cynr6IbMZh65zBKcJLVB5uQYJlJQH4cXkhEdwf2reC9BoJ6z9r2hldqC
lRWu7geb25N7uBo/e9XnHr7wIxW2iWsoITSXBquZdI7qSnJXHJCRFtFYFKW+HaY0
nDrLCA30oEA02+rthIp3LQ==
-----END PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUICyWEmsr4MlpJdYd26hP/SeDpY0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDcyOTE5MDgyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCo9A1mRiRjlRDVdiu0aQjkJKzorb9LTNnlkWGIjTjoFOhS
w8+lxt4Ul/MQf4xx3KetsUT32OUOGy8RGOWhCnDI1v4V9QzvUWUniDLu7DKFmmHq
uvoW9LGVy/2rA19OeTu+rg5XbygTHnhfMlHwd1jlg7fc6eQlouwA+HtJ6yPNAgRK
3i4IyqHsM/UQQpoE0hb0cMTSR9S+LlGsmL2TciPV00YYzGLWVYXGIT4OAtZg6rsx
FzxjzEDGIxqKZwh6O82L/nM+/bZz9cemdKKnJhEByxeErBotD81y7lrlG5PRNjzY
/1h0QhovQ1Qq0St8/JuJERWln+lB4hh3MtmChTW5AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQACE2BlPeJVC1dMaotYniTu
G7WsfsRbNaozT55kXwMQ8/SYGLutUZr7pqO7VwGFlEiIKD2nbypZx69Q7/GjMtTd
5bFFtrkZcuTViaLARZFbSTAYeakp3CGrUanlJT2xLTFvu4HFxFCBzpIYGjhLcm82
spMaHzr7Ch9jZIlFqB8bHJcedEtOSnIbeetVNDnkES1JZCN8GBDpUmbKxWm5qfPs
WDG546VZbigBvsWDke+z/mcB7NkbasyXzzHqAdlvBMjo9ZHQZfvqB+6Ira0Hir+R
KA9hMtCL1MTX9Hg5+V8MZpoOi66B4q71svDoL/I/VjO3w2QFyt+2+Y2gQp6YfGdf
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCo9A1mRiRjlRDV
diu0aQjkJKzorb9LTNnlkWGIjTjoFOhSw8+lxt4Ul/MQf4xx3KetsUT32OUOGy8R
GOWhCnDI1v4V9QzvUWUniDLu7DKFmmHquvoW9LGVy/2rA19OeTu+rg5XbygTHnhf
MlHwd1jlg7fc6eQlouwA+HtJ6yPNAgRK3i4IyqHsM/UQQpoE0hb0cMTSR9S+LlGs
mL2TciPV00YYzGLWVYXGIT4OAtZg6rsxFzxjzEDGIxqKZwh6O82L/nM+/bZz9cem
dKKnJhEByxeErBotD81y7lrlG5PRNjzY/1h0QhovQ1Qq0St8/JuJERWln+lB4hh3
MtmChTW5AgMBAAECggEBAJB3tyl32s/H/A/7Lt3iXnbuoWeIgiU6PqvdR2ADGeDh
V9LFmr3vMaC8WVwHJKmL+1k7VnTz4tDQD8v31QqCKfSiWbuewYO1vuAxxxOjpoO1
gfq8DPMqIturBWqAxLMOWTbwEFVVOBg5GsaT+Zq8Aqimm8ZrvOktyc3+qzWGuiMm
LPcVTlN3SPWhiBFwAh0mRYkYUwLOXFNDZzDmK3G3ONdlIuyvRdvGZQc4bd0z6bsJ
UorXTjB294MsEO9Ev6+BEtRCpCnm7+rB7ZBmUaH4tDGDmO47inrWeU9uQ6roKHvZ
yIPU7DO8P5/YohXiJKXBtwHZcYTfproFJOQ9yQjhcDECgYEA3V8pSkFdUfNimcfY
+waG7m7+kZq8Gt1uFZ4ZWaO7zxsgzspENm0Ik4xf3U3yFsiNlCO4e0HWxNIgpDf5
kdy20aL3Ila78quuX4dxZONychzCalIJS7sMc65kD7c1ZrVHJTTv4xwThwlw65W2
WT+E6jeZ0wTecfF4NJQ5pyrakd0CgYEAw2HLZ5/NxgeP1eiQ2u/pNkGeDgRjjWTh
K2nCqlaRXeLD7KbzDxCPq8DFvFO3fV/EgtUGrIWSyrkKQCVGx5YaC14g/gJlXIOR
khxox5B2b/kjw6RydkRvlwvwdR6dVEN2NwDuTBzvLM4L4vMgnIJDgY3743TKRoWs
6CIhg8Xh640CgYADcuEUzBHlHfKSTL+/oWlmu4nxwMRfcsWtRopEkD1zy4tmTVZk
tqwkiFJSA03bNwKlpSzRlsP+yvtBM7IKqLKcb3qEKW/CJxSPXm/Qz45P4szQlTiZ
2m8mOjhK2mLVl8tk8/8svZo8R1RgBzQRDeFHONiHphLFGaryvsBrL0q6bQKBgEeY
/sDqfq2i98Kbhvm0EPIg+ZqJYTHfVeRizUM+leahwspmI4vRtdRqwAtTYlo/TfPj
vJ5cFH7VcDwxbM6W4tRnmg97MUnFrQKuBnebKMu/sKtxB8DvMzVW2rcQkPbgAeIG
JU0fDUaN+y0fi0PPOI2xSi0AD1/ofIRUfZOcYD3BAoGAJ7V3ipczlg0j5OQ/XT8o
TiJVzyBwQy0S3AQI9zeo9tlVfCd+BwnSdSWlb5AxLOJWBYO/ptOvW6I4wtkYNSLT
j6gSYVfRLqAbBVWydCQuSVAHhM4Fonqcis5S7Yd1U05GLsvpG5T7uqG5N7pgS4SD
EMu0jkyvnFmDWG65WRzbD5c=
-----END PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_10: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_10: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
