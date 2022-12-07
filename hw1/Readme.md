Все конфиги лежат в zip файле с лабой

# Клиенты

## Клиент 1

IP адрес клиента + Gateway:
```
VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.10.1/24
GATEWAY     : 10.0.10.254
DNS         : 
MAC         : 00:50:79:66:68:01
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500
```

Пинг второго клиента:
```
VPCS> ping 10.0.20.1

84 bytes from 10.0.20.1 icmp_seq=1 ttl=63 time=18.104 ms
84 bytes from 10.0.20.1 icmp_seq=2 ttl=63 time=11.331 ms
84 bytes from 10.0.20.1 icmp_seq=3 ttl=63 time=9.854 ms
84 bytes from 10.0.20.1 icmp_seq=4 ttl=63 time=29.924 ms
84 bytes from 10.0.20.1 icmp_seq=5 ttl=63 time=8.266 ms
```

## Клиент 2

IP адрес клиента + Gateway:
```
VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.20.1/24
GATEWAY     : 10.0.20.254
DNS         : 
MAC         : 00:50:79:66:68:02
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500
```

Пинг первого клиента:
```
VPCS> ping 10.0.10.1

84 bytes from 10.0.10.1 icmp_seq=1 ttl=63 time=13.223 ms
84 bytes from 10.0.10.1 icmp_seq=2 ttl=63 time=11.503 ms
84 bytes from 10.0.10.1 icmp_seq=3 ttl=63 time=8.745 ms
84 bytes from 10.0.10.1 icmp_seq=4 ttl=63 time=8.112 ms
84 bytes from 10.0.10.1 icmp_seq=5 ttl=63 time=8.868 ms
```

# Коммутаторы

## Коммутаторы уровня доступа

У первого все интерфейсы работают в vlan 10:
```
Switch#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3
10   VLAN0010                         active    Et0/0, Et0/1, Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup
```

У второго в vlan 20:
```
Switch#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3
20   VLAN0020                         active    Et0/0, Et0/1, Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup
```

## Коммутатор уровня распределения

Он является корнем spanning-tree обеих vlan:
```
Switch#show spanning-tree

...

VLAN0010  
  Spanning tree enabled protocol ieee
  Root ID    Priority    24586
             Address     aabb.cc00.6000
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
          
  Bridge ID  Priority    24586  (priority 24576 sys-id-ext 10)
             Address     aabb.cc00.6000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    Shr 
Et0/2               Desg FWD 100       128.3    Shr


VLAN0020  
  Spanning tree enabled protocol ieee
  Root ID    Priority    24586
             Address     aabb.cc00.6000
             Cost        300
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
          
  Bridge ID  Priority    24596  (priority 24576 sys-id-ext 20)
             Address     aabb.cc00.6000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    Shr 
Et0/2               Desg FWD 100       128.3    Shr
```

# Роутер

На роутере настроена таблица маршрутизации:
```
Router>show ip route 
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C        10.0.10.0/24 is directly connected, Ethernet0/0.1
L        10.0.10.254/32 is directly connected, Ethernet0/0.1
C        10.0.20.0/24 is directly connected, Ethernet0/0.2
L        10.0.20.254/32 is directly connected, Ethernet0/0.2
```
