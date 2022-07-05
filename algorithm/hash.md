# Hash (해시)

### 해시 자료구조
- 키에 대응되는 값을 저장하는 자료구조
- insert, erase, find, update 등의 모든 연산이 $O(1)$
- 해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 대응시키는 함수
- 해시 함수로 키를 적당히 배열의 인덱스로 보내고 이를 테이블로 관리하는 것이 해시 자료구조

### 충돌
- 서로 다른 키가 값을 해시 값을 가지게 되는 경우
- 해시 함수의 목적 자체가 원래 함수의 입력으로 주어지는 정의역의 공간이 너무 커서 배열의 인덱스로 활용할 수 없으니 범위를 줄이고자 한것이다. 즉 충돌 차제를 막을 방법은 없으나 충돌 발생시 회피 방안 Chaining과 Open Addresing이 있다.

### Chaining
- 각 인덱스 마다 연결 리스트를 하나씩 둔다.
- 최악의 경우(모두 해시 값이 같은 경우) $O(N)$ 가 되어 성능 저하
- 해시 값이 최대한 균등하게 퍼져야 성능이 좋아지기 때문에 주어진 데이터의 특징에 따라 적절한 해시 함수를 정해야 한다.

### Open Addressing
- 삽입할 때 해당 칸에 이미 값이 있다면 다음 칸으로 가서 삽입한다.
- 단, 삭제할 때 그냥 값을 날려서 빈 칸을 만들면 안되고 해당 칸에 쓰레기 값 or 별도의 배열 등을 둬서 원래 값이 있었지만 제거된 상태임을 명시해줘야 한다.
- find, erase 등에서 탐색할 때 쓰레기 값이 들어있는 칸을 만났을 경우 계속 탐색을 이어나가게 한다. 빈칸을 만나야 멈춤.
- insert 할 때 빈공간을 찾기위해 다음 칸으로 이동하는데 쓰레기 값이 들어있는 칸은 마주하면 거기에 바로 삽입할 수 있다.
    
    ### Probing
    - Open Addressing 방식에서 탐색하는 방법
        
        ### Linear Probing
        - 충돌 발생 시, 오른쪽으로 한 칸 이동해서 확인
        - 장점: 구현 간단하고 cache hit rate가 높다.
        - 단점: clustering 이 생겨 성능에 영향을 준다.
        
        ### Quadratic Probing
        - 충돌 발생 시, 오른쪽으로 1, 3, 5, … 칸 이동하는 방법 ( 처음 위치 기준으로는 1,4,9, .. 칸)
        - 장점: cache hit rate가 나쁘지 않다. clustering을 어느 정도 회피할 수 있다.
        - 단점: 해시 값이 동일하다면 여전히 clustering이 발생한다.
        
        ### Double Hashing
        - 해시 함수를 하나 더 둬서 충돌 발생 시 몇 칸 점프할지 이 새로운 해시 함수 값으로 계산하는 방법
        - 장점: clustering을 효과적으로 회피할 수 있다.
        - 단점: cache hit rate이 아주 안 좋아진다.
        -

## 문제

[백준 문제집 - 해시를 이용한 set과 map](https://www.acmicpc.net/problemset?sort=ac_desc&algo=136)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |        내 풀이         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/7785" target="_blank">7785</a> | <a href="https://www.acmicpc.net/problem/7785" target="_blank">회사에 있는 사람</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |                      | <a href="./../Problems/hash/BOJ_7785.md">BOJ_7785</a> |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1620" target="_blank">1620</a> | <a href="https://www.acmicpc.net/problem/1620" target="_blank">나는야 포켓몬 마스터 이다솜</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      | <a href="./../Problems/hash/BOJ_1620.md">BOJ_1620</a> |

### Reference 
* [[실전알고리즘]0x15강-해시](https://blog.encrypted.gg/1004?category=773649](https://blog.encrypted.gg/1009?category=773649)
