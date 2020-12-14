#include <fstream>
#include <iostream>
#include <vector>

using std::cout, std::ifstream, std::vector;

vector<int> get_input() {
    ifstream input_stream ("input.txt");
    vector<int> numbers;
    int number;
    while(! input_stream.eof()) {
        input_stream >> number;
        numbers.push_back(number);
    }
    input_stream.close();
    return numbers;
}

int main() {
    vector<int> numbers = get_input();

    for (int number_1: numbers) {
        for (int number_2: numbers) {
            for (int number_3: numbers) {
                if (number_1 + number_2 + number_3 == 2020) {
                    cout << number_1 * number_2 * number_3 << "\n";
                    return 0;
                }
            }
        }
    }
    
    return 0;
}