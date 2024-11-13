import sys
inf = int(1e9)

#가중치 인접 행렬
graph = [
    [5, 1, 1],
    [1, 2, 1],
    [1, 3, 3],
    [2, 3, 1],
    [2, 4, 5],
    [3, 4, 2]
]

visited = [False]*len(graph)
distance = [inf]*len(graph)

def get_smallest_node() : #방문하지 않았으면서 시자노트와 최단거리인 노드 반환
    min_value = inf
    index = 0
    for i in range(len(graph)):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #일단 시작노드에서 시작노드는 거리가 0이니 업데이트
    distance[start] = 0
    #방문했으니 업데이트
    visited[start] = True
    #인접 노드들에 대해 최단 거리 계산
    for i in graph[start]:
        distance[i[0]] = i[1] #시작 노드와 연결된 노드들의 거리 입력
    
    for j in range(len(graph)):
        now = get_smallest_node() #거리가 가장 짧은 노트 선택
        visited[now] = True
        
        for k in graph[now]:
            if distance[now] + k[i] < distance[j[0]]: #기존에 입력된 값보다 더 작은 거리가 있으면
                distance[j[0]] = distance[now] + j[1] #값 갱신
                
dijkstra(0)
print(distance)

