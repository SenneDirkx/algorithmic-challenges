​
class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int> > solution;
        map<int, vector<int> > store;
        
        for (int i = 0; i < groupSizes.size(); i++) {
            store[groupSizes[i]].push_back(i);
            if (store[groupSizes[i]].size() == groupSizes[i]) {
                solution.push_back(store[groupSizes[i]]);
                store[groupSizes[i]].clear();
            }
        }
        return solution;
        
    }
};
