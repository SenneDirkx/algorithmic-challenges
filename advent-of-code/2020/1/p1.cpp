#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<int> readInputFile(string filename);
void getComplements(int target, vector<int> inputs, int result[2]);

int main() {
    vector<int> inputs = readInputFile("input1.txt");
    int complements[2];
    getComplements(2020, inputs, complements);
    int result = complements[0]*complements[1];
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

void getComplements(int target, vector<int> inputs, int result[2]) {
    set<int> charStore;
    set<int> store;
    for (int i = 0; i < inputs.size(); i++) {
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