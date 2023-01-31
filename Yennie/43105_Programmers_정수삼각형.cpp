#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;

int dp[501][501];

int solution(vector<vector<int>> triangle) {   
    dp[0][0] = triangle[0][0];
    
    for(int i = 1; i < triangle.size(); i++) {
        dp[i][0] = dp[i-1][0] + triangle[i][0]; //각 층의 첫 번째 자리
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]; //각 층의 마지막 자리
        for(int j = 1; j < i; j++){
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
        }
    }
    
    int last_floor = triangle.size() - 1;
    int max_path_num = dp[last_floor][0];
    for(int i = 1; i < last_floor; i++) {
        if (dp[last_floor][i] > max_path_num) {
            max_path_num = dp[last_floor][i];
        }
    }
    
    return max_path_num;
}