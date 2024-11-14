'''
> 얘도 최단 경로 알고리즘
> Dajkstra's Algorithm을 발전시킨 것
- 다익스트라는 시작지점과 가까운 곳부터 순서대로 결정.

> A*는 추정 코스트를 힌트로 설정해서 불필요한 탐색 줄임
- 추정코스트는 마음대로 설정할 수 있음
- 사람이 미리 설정하는 추정 코스트를 heuristic cost 라고 함. ex) 목표 지점까지 직선 경로 반올림
- 시작지점에서 실제 cost와 추정 cost의 합이 적은 쪽을 택하여 진행

> 미로가 아니더라도, 괜찮음. 너비우선탐색임. 결국 총코스트가 최소가 되는 것을 선택하는 것
'''


# openList와 closeList 사용함
# F(total cost) = G(real cost) + H(heuristic cost) 를 노드 생성할 때마다 계산
# openList에는 현재 노드에서 갈 수 있는 노드를 전부 추가해서 F, G, H 계산
# openList에 중복 노드 있으면 F가 제일 작은 노드 선택

# closeList에는 openList에서 F가 가장 작은 노드 추가


matrix = [
    [True, True, True, False, False, False, False],
    [True, False, True, False, False, False, False],
    [True, False, True, True, True, True, True],
    [True, False, True, False, False, False, True],
    [True, False, True, False, True, True, True],
    [True, False, True, False, True, False, False],
    [True, True, True, True, True, True, True],
]