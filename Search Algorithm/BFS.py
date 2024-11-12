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

# 기본적으로 BFS는 일단 확인, 그 주위 노드들 방문 안했으면 큐에 넣음.
# 하나씩 빼고, 그 주위 노드 방문 여부 확인 후, no방문이면 다시 큐에 넣음.
# 큐에 하나도 없을 때까지 반복

from collections import deque

def bfs(graph, start) :
    visited = [False]*len(graph) #만약 좌표가 중요하면 set으로 해서 방문 여부를 한방에 아는 것도 좋음
    queue = deque([start])  #데크라는 자료형에 start 원소만 있는 리스트를 넣어준거임 일단
    visited[start] = True #꼭 첫 방문 노드 표시
    
    while queue : #queue의 원소가 빌 때까지
        current = queue.popleft() # 데크를 큐처럼 pop 하겠다는 뜻
        print(current, end = " ")
        
        for i, connected in enumerate(graph[current]) :
            if connected and not visited[i] :
                visited[i] = True 
                queue.append(i)
                    
bfs(graph, 0)