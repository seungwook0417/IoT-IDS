# IoT-IDS

IoT ARP Spoof Attacks IDS

***

## 프로젝트 개요

* 4차 산업혁명 시대를 이끌어가는 스마트 홈, 스마트 헬스 케어, 자율 자동차 등 기술은 IoT를 기반으로 동작한다. 지금 우리 주변에는 많은 IoT기기가 늘어가고 있으며, 공격자들은 IoT기기를 대상으로 공격하는 사례가 늘고 있다. 
  공공기관이나 기업에서도 재산을 보호하고 침입자를 막기 위해 경보 시스템을 이용하고 있다.  하지만, 가정에서도 많은 IoT 기기들을 사용하지만 침입자를 막기 위한 경보 시스템이 많이 나와있지 않다. 
* 본 프로젝트는 가정용 IoT, 서버, 네트워크에서 이상 징후(ARP Spoof)를 탐지하는 시스템을 구현하였다.



## 프로젝트 결과

* 모니터링 프로그램
  * 현재 네트워크에 있는 모든 디바이스의 IP Address, MAC Address, Status. Connection Time 정보를 실시간으로 보여주는 CLI, Web 시스템 개발
  * Status는 현재 상태 표시를 나타내며 ARP Spoofing 발생시 피해자는 Target, 공격자는 Attcker으로 정보를 보여줌
  * Connection Time은 ARP Spoofing 발생시 공격자, 피해자 시간을 나타냄
  * Web에서는 현재 네트워크 접속중인 디바이스 갯수, 공격당한 디바이스 갯수를 나타내며 ARP Spoofing 발생시 디바이스 리스트에 정보를 나타냄

* 정상 상황 시

![정상 상황 시](https://github.com/seungwook0417/IoT-IDS/blob/master/resource/basic.png)

* 공격 상황 시(CLI)

![공격 상황 시](https://github.com/seungwook0417/IoT-IDS/blob/master/resource/attack.png)

* 공격 상황 시(WEB)

![공격 상황 시](https://github.com/seungwook0417/IoT-IDS/blob/master/resource/web.png)

