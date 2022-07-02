# Two Pointers (투 포인터)

### 알고리즘
* 배열에서 원래 이중 for문으로 탐색하면  $O(N^2)$에 처리되는 작업을 2개 포인터(커서)의 움직임으로 $O(N)$에 해결하는 알고리즘
* 시간복잡도를 줄일 수 있는 이유? -> 이중 for문에서는 i=0일 때 계산하면서 얻은 정보가 i=1일 때 전혀 쓰이지 않지만 투 포인터에서는 i=0에서 계산하면서 얻은 정보를 i=1일 때 활용한다.(그 정보가 포인터의 이동으로 나타난다.)
* 1차원 배열에서 각자 다른 원소를 가리키고 있는 2개의 포인터를 조작해가며 원하는 것을 얻는 형태
* 이전 반복에서 결과를 기억해 그 다음 반복문에서 불필요하게 탐색하는 작업을 방지한다.

  :bulb: 투포인터는 이분탐색으로 해결할 수 있는 경우가 많다. (반대도 마찬가지)

### 시간 복잡도
* 정렬 : $O(NlogN)$
* 두 포인터가 움직이는 최대 거리 = $2N = O(N)$

## 문제

[백준 문제집](https://www.acmicpc.net/workbook/view/6782)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |        내 풀이         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11728" target="_blank">11728</a> | <a href="https://www.acmicpc.net/problem/11728" target="_blank">배열 합치기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21921" target="_blank">21921</a> | <a href="https://www.acmicpc.net/problem/21921" target="_blank">블로그</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20922" target="_blank">20922</a> | <a href="https://www.acmicpc.net/problem/20922" target="_blank">겹치는 건 싫어</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/two_pointer/20922">바로가기</a> |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/22862" target="_blank">22862</a> | <a href="https://www.acmicpc.net/problem/22862" target="_blank">가장 긴 짝수 연속한 부분 수열 (large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2470" target="_blank">2470</a> | <a href="https://www.acmicpc.net/problem/2470" target="_blank">두 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/two_pointer/2470">바로가기</a> |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15961" target="_blank">15961</a> | <a href="https://www.acmicpc.net/problem/15961" target="_blank">회전 초밥</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/two_pointer/15961">바로가기</a> |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1806" target="_blank">1806</a> | <a href="https://www.acmicpc.net/problem/1806" target="_blank">부분합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/two_pointer/1806">바로가기</a> | <a href="./../Problems/two_pointers/BOJ_1806.md">BOJ_1806</a>
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/3151" target="_blank">3151</a> | <a href="https://www.acmicpc.net/problem/3151" target="_blank">합이 0</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/22945" target="_blank">22945</a> | <a href="https://www.acmicpc.net/problem/22945" target="_blank">팀 빌딩</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20366" target="_blank">20366</a> | <a href="https://www.acmicpc.net/problem/20366" target="_blank">같이 눈사람 만들래?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20442" target="_blank">20442</a> | <a href="https://www.acmicpc.net/problem/20442" target="_blank">ㅋㅋ루ㅋㅋ</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/7453" target="_blank">7453</a> | <a href="https://www.acmicpc.net/problem/7453" target="_blank">합이 0인 네 정수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21279" target="_blank">21279</a> | <a href="https://www.acmicpc.net/problem/21279" target="_blank">광부 호석</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/> |                      |
| 13 |                      | <a href="https://www.acmicpc.net/problem/2018" target="_blank">2018</a> | <a href="https://www.acmicpc.net/problem/2018" target="_blank">수들의 합 5</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/two_pointer/2018">바로가기</a> |
| 14 |                      | <a href="https://www.acmicpc.net/problem/1940" target="_blank">1940</a> | <a href="https://www.acmicpc.net/problem/1940" target="_blank">주몽</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | <a href="./../solution/two_pointer/1940">바로가기</a> |
| 15 |                      | <a href="https://www.acmicpc.net/problem/10025" target="_blank">10025</a> | <a href="https://www.acmicpc.net/problem/10025" target="_blank">게으른 백곰</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 16 |                      | <a href="https://www.acmicpc.net/problem/6159" target="_blank">6159</a> | <a href="https://www.acmicpc.net/problem/6159" target="_blank">코스튬 파티</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 17 |                      | <a href="https://www.acmicpc.net/problem/2428" target="_blank">2428</a> | <a href="https://www.acmicpc.net/problem/2428" target="_blank">표절</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 18 |                      | <a href="https://www.acmicpc.net/problem/3273" target="_blank">3273</a> | <a href="https://www.acmicpc.net/problem/3273" target="_blank">두 수의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 19 |                      | <a href="https://www.acmicpc.net/problem/2003" target="_blank">2003</a> | <a href="https://www.acmicpc.net/problem/2003" target="_blank">수들의 합 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      | <a href="./../Problems/two_pointers/BOJ_2003.md">BOJ_2003</a>
| 20 |                      | <a href="https://www.acmicpc.net/problem/2559" target="_blank">2559</a> | <a href="https://www.acmicpc.net/problem/2559" target="_blank">수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | <a href="./../solution/two_pointer/2559">바로가기</a> |
| 21 |                      | <a href="https://www.acmicpc.net/problem/15565" target="_blank">15565</a> | <a href="https://www.acmicpc.net/problem/15565" target="_blank">귀여운 라이언</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |                      | <a href="https://www.acmicpc.net/problem/2531" target="_blank">2531</a> | <a href="https://www.acmicpc.net/problem/2531" target="_blank">회전 초밥</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 23 |                      | <a href="https://www.acmicpc.net/problem/2118" target="_blank">2118</a> | <a href="https://www.acmicpc.net/problem/2118" target="_blank">두 개의 탑</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 24 |                      | <a href="https://www.acmicpc.net/problem/2467" target="_blank">2467</a> | <a href="https://www.acmicpc.net/problem/2467" target="_blank">용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 25 |                      | <a href="https://www.acmicpc.net/problem/2230" target="_blank">2230</a> | <a href="https://www.acmicpc.net/problem/2230" target="_blank">수 고르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/two_pointer/2230">바로가기</a> | <a href="./../Problems/two_pointers/BOJ_2230.md">BOJ_2230</a>
| 26 |                      | <a href="https://www.acmicpc.net/problem/14921" target="_blank">14921</a> | <a href="https://www.acmicpc.net/problem/14921" target="_blank">용액 합성하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 27 |                      | <a href="https://www.acmicpc.net/problem/9024" target="_blank">9024</a> | <a href="https://www.acmicpc.net/problem/9024" target="_blank">두 수의 합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 28 |                      | <a href="https://www.acmicpc.net/problem/2473" target="_blank">2473</a> | <a href="https://www.acmicpc.net/problem/2473" target="_blank">세 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/two_pointer/2473">바로가기</a> |
| 29 |                      | <a href="https://www.acmicpc.net/problem/16472" target="_blank">16472</a> | <a href="https://www.acmicpc.net/problem/16472" target="_blank">고냥이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 30 |                      | <a href="https://www.acmicpc.net/problem/1484" target="_blank">1484</a> | <a href="https://www.acmicpc.net/problem/1484" target="_blank">다이어트</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 31 |                      | <a href="https://www.acmicpc.net/problem/13422" target="_blank">13422</a> | <a href="https://www.acmicpc.net/problem/13422" target="_blank">도둑</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 32 |                      | <a href="https://www.acmicpc.net/problem/15831" target="_blank">15831</a> | <a href="https://www.acmicpc.net/problem/15831" target="_blank">준표의 조약돌</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 33 |                      | <a href="https://www.acmicpc.net/problem/6137" target="_blank">6137</a> | <a href="https://www.acmicpc.net/problem/6137" target="_blank">문자열 생성</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 34 |                      | <a href="https://www.acmicpc.net/problem/1644" target="_blank">1644</a> | <a href="https://www.acmicpc.net/problem/1644" target="_blank">소수의 연속합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 35 |                      | <a href="https://www.acmicpc.net/problem/20181" target="_blank">20181</a> | <a href="https://www.acmicpc.net/problem/20181" target="_blank">꿈틀꿈틀 호석 애벌레 - 효율성</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |

### Reference 
* 문제 : [tony9402](https://github.com/tony9402/baekjoon/blob/main/two_pointer/README.md)
* [[실전알고리즘]0x14강-투포인터](https://blog.encrypted.gg/1004?category=773649)
* [투 포인터(Two Pointers Algorithm), 슬라이딩 윈도우(Sliding Window)](https://m.blog.naver.com/kks227/220795165570)
