'''
     1
   /   \
  2     3
 / \   / \
4   5 6   7
그래프 예시
'''

#인접행렬
graph = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0]
]

def dfs(graph, visited, node) : #DFS 에서의 핵심은 재귀.
    visited[node] = True #node로 시작할거고, 방문했으니깐 True로 바꿈
    print(node, end = " ")
    for i, connected in enumerate(graph[node]) : # enumerate : index와 값을 반환
        if connected and not visited[i] : #if connected라는건 1이냐는 뜻. 1이면 if문 진행
            dfs(graph, visited, i)
            
# 그래프 탐색 시작
visited = [False] * 7
dfs(graph, visited, 1) # 실제 index와 node 가 1차이 나기 떄문에 결과값하고, 입력값이 node-1이라는 것을 알고 있어야함.