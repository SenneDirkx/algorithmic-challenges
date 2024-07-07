#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<int> readInputFile(string filename);
void getThreeComplements(int target, vector<int> inputs, int result[3]);
void getComplements(int target, vector<int> inputs, int result[2], int start);
int main() {
    vector<int> inputs = readInputFile("input1.txt");
    int complements[3];
    getThreeComplements(2020, inputs, complements);
    int result = complements[0]*complements[1]*complements[2];
    cout << result << endl;

    return 0;
}

vector<int> readInputFile(string filename) {
    vector<int> result;
    string line;
    ifstream inputfile (filename);
    if (inputfile.is_open()) {
        while (getline(inputfile, line))  {
            int number = stoi(line);
            result.push_back(number);
        }
    }
    return result;
}

void getThreeComplements(int target, vector<int> inputs, int result[3]) {
    int pivot;
    for (int i = 0; i < inputs.size()-2; i++) {
        pivot = inputs[i];
        int complements[2] = {-1, -1};
        getComplements(target-pivot, inputs, complements, i+1);
        if (complements[0] != -1 && complements[1] != -1) {
            result[0] = pivot;
            result[1] = complements[0];
            result[2] = complements[1];
            return;
        }
    }
}

void getComplements(int target, vector<int> inputs, int result[2], int start) {
    set<int> charStore;
    set<int> store;
    for (int i = start; i < inputs.size(); i++) {
        int number = inputs[i];
        set<int>::iterator place = store.find(number);
        if (place != store.end()) {
            result[0] = number;
            result[1] = target-number;
            return;
        }
        store.insert(target-number);
    }
}