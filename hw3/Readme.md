# Клиенты
IP настраивается по dhcp:
```
VPCS> dhcp
DORA IP 10.0.10.12/24 GW 10.0.10.254

VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.10.12/24
GATEWAY     : 10.0.10.254
DNS         : 1.1.1.1  
DHCP SERVER : 10.0.10.254
DHCP LEASE  : 86393, 86400/43200/75600
MAC         : 00:50:79:66:68:01
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500
```

```
VPCS> dhcp
DORA IP 10.0.20.12/24 GW 10.0.20.254

VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.20.12/24
GATEWAY     : 10.0.20.254
DNS         : 1.1.1.1  
DHCP SERVER : 10.0.20.254
DHCP LEASE  : 86392, 86400/43200/75600
MAC         : 00:50:79:66:68:02
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500
```
Можно заметить, что ip адреса выдаются начиная с 10.0.x.12, потому что адреса 10.0.x.1 - 10.0.x.11 добавлены в исключения dhcp

Пинг с одного клиента на другой:
```
VPCS> ping 10.0.20.12

84 bytes from 10.0.20.12 icmp_seq=1 ttl=63 time=17.824 ms
84 bytes from 10.0.20.12 icmp_seq=2 ttl=63 time=6.940 ms
84 bytes from 10.0.20.12 icmp_seq=3 ttl=63 time=9.032 ms
84 bytes from 10.0.20.12 icmp_seq=4 ttl=63 time=21.184 ms
84 bytes from 10.0.20.12 icmp_seq=5 ttl=63 time=9.328 ms
```

Пинг верхнего роутера с клиента:
```
VPCS> ping 11.0.0.2

84 bytes from 11.0.0.2 icmp_seq=1 ttl=254 time=9.798 ms
84 bytes from 11.0.0.2 icmp_seq=2 ttl=254 time=7.037 ms
84 bytes from 11.0.0.2 icmp_seq=3 ttl=254 time=11.210 ms
84 bytes from 11.0.0.2 icmp_seq=4 ttl=254 time=4.886 ms
84 bytes from 11.0.0.2 icmp_seq=5 ttl=254 time=5.707 ms
```

# Свитчи
Я сконфигурировал все коммутаторы как в ДЗ1

# Маршрутизатор
На нижнем роутере настроены dhcp пулы:
```
Router#show ip dhcp pool                                               

Pool vlan10 :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 254
 Leased addresses               : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased addresses
 10.0.10.13           10.0.10.1        - 10.0.10.254       1

Pool vlan20 :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 254
 Leased addresses               : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased addresses
 10.0.20.13           10.0.20.1        - 10.0.20.254       1
```

И на нем же настроен nat:
```
Router#show ip nat statistics 
Total active translations: 2 (0 static, 2 dynamic; 0 extended)
Peak translations: 12, occurred 00:06:47 ago
Outside interfaces:
  Ethernet0/1
Inside interfaces: 
  Ethernet0/0.1, Ethernet0/0.2
Hits: 38  Misses: 0
CEF Translated packets: 38, CEF Punted packets: 0
Expired translations: 20
Dynamic mappings:
-- Inside Source
[Id: 2] access-list 1 pool natpool refcount 2
 pool natpool: netmask 255.255.255.0
start 11.0.0.3 end 11.0.0.13
type generic, total addresses 11, allocated 2 (18%), misses 0
-- Outside Destination
[Id: 1] access-list 1 interface Ethernet0/1 refcount 0

Total doors: 0
Appl doors: 0
Normal doors: 0
Queued Packets: 0
```

На верхнем роутере на интерфейсе en0/0 настроен ip адрес 11.0.0.2/24
