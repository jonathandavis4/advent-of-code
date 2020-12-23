#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using std::smatch, std::cout, std::ifstream, std::regex, std::string, std::vector;

vector<string> get_input() {
    ifstream input_stream ("input.txt");
    vector<string> strings;
    string s;
    while(getline(input_stream, s)) {
        strings.push_back(s);
    }
    input_stream.close();
    return strings;
}

bool is_password_valid(string &str, string &c, int position_1, int position_2) {
    int count = 0;
    if (str.substr(position_1 - 1, 1) == c) {
        count += 1;
    }
    if (str.substr(position_2 - 1, 1) == c) {
        count += 1;
    }
    return count == 1;
}

int main() {
    vector<string> strings = get_input();

    regex pattern ("(\\d+)-(\\d+) (.): (.+)");
    smatch match;

    int valid_password_count = 0;

    for (string s: strings) {
        std::regex_match (s, match, pattern);
        int position_1 = stoi(match.str(1));
        int position_2 = stoi(match.str(2));
        string c = match[3];
        string password = match[4];

        if (is_password_valid(password, c, position_1, position_2)) {
            valid_password_count++;
        }
    }
    
    cout << valid_password_count << "\n";
    
    return 0;
}