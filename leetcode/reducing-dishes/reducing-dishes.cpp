class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        
        int result = 0, tmp = 0, n = satisfaction.size();
        for (int i = n - 1; i >= 0 && satisfaction[i] > -tmp; --i) {
            tmp += satisfaction[i];
            result += tmp;
        }
        return result;
    }
};
