#include <bits/stdc++.h>
#define MAX 50001
#define ALL(X) X.begin(), X.end()

using namespace std;

vector<int> answer;
vector<pair<int,int>> graph[MAX]; //{비용, 다음지점}
int intensity[MAX]; // 각 지점에 도달하는 동안 최소 intensity(비용)
bool is_summit[MAX]; // 산봉우리 배열


void dijkstra(vector<int>& gates) {
    // 오름차순으로 정렬되는 우선순위 큐
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<pair<int, int>> temp;
    
    memset(intensity, -1, sizeof(intensity));
    
    for (auto g : gates) {
        pq.push({0, g}); // {비용, 목적지}
        intensity[g] = 0; // g까지 경로 중 최소 비용(intensity)
    }
    
    while(!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();
        
        if (cost > intensity[now]) continue; // 이미 최소 비용을 구한 경우
        
        if (is_summit[now]) { // 봉우리 도착인 경우, 비용과 봉우리 위치 저장
            temp.push_back({cost, now});
            continue;
        }
        
        for (auto g : graph[now]) {
            int weight = g.first; //now에서 to로 이동하는 비용
            int to = g.second;
            
            // 방문 전 또는 경유하는게 더 최소비용일 경우
            // intensity를 구해야하므로 max(cost, weight) 사용
            if (intensity[to] == -1 || max(cost, weight) < intensity[to]) {
                intensity[to] = max(cost, weight);
                pq.push({intensity[to], to});
            }
        }
    }
    
    sort(ALL(temp)); // cost 오름차순 정렬
    answer.push_back(temp[0].second);
    answer.push_back(temp[0].first);
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    
    // 그래프 정보 저장
    for (auto p : paths) {
        graph[p[0]].push_back({p[2], p[1]});
        graph[p[1]].push_back({p[2], p[0]});
    }
    
    // 산 봉우리 정보 저장
    for (auto s : summits) {
        is_summit[s] = true;
    }
    
    dijkstra(gates);
    
    return answer;
}