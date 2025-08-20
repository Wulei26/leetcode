#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void DFS(vector<vector<int>>& graph, vector<bool>& isVisited, int node) {
        if (isVisited[node]) {
            return;
        }
        isVisited[node] = true;
        for (int nextNode : graph[node]) {
            if (!isVisited[nextNode]) {
                DFS(graph, isVisited, nextNode);
            }
        }
    }

    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // 构建有向图
        vector<vector<int>> graph(n);
        for (const auto& edge : invocations) {
            int x = edge[0];
            int y = edge[1];
            graph[x].push_back(y);
        }

        // 初始化访问标记数组
        vector<bool> isVisited(n, false);
        vector<int> ans;

        // 从可疑节点k开始DFS遍历
        DFS(graph, isVisited, k);

        // 收集未被访问的节点（非可疑方法）
        for (int i = 0; i < n; ++i) {
            if (!isVisited[i]) {
                ans.push_back(i);
            }
        }

        // 检查是否存在剩余方法调用可疑方法的情况
        for (const auto& edge : invocations) {
            int x = edge[0];
            int y = edge[1];
            // 如果x在剩余方法中 且y是可疑方法
            if (!isVisited[x] && isVisited[y]) {
                // 返回所有节点
                vector<int> allNodes(n);
                for (int i = 0; i < n; ++i) {
                    allNodes[i] = i;
                }
                return allNodes;
            }
        }

        return ans;
    }
};