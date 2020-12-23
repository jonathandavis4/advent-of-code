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

int count_char_in_string(string str, string c) {
    if (str.length() == 0) {
        return 0;
    }
    else {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.substr(i, 1) == c) {
                count += 1;
            }
        }
        return count;
    }
}

int main() {
    vector<string> strings = get_input();

    regex pattern ("(\\d+)-(\\d+) (.): (.+)");
    smatch match;

    int valid_password_count = 0;

    for (string s: strings) {
        std::regex_match (s, match, pattern);
        int min_count = stoi(match.str(1));
        int max_count = stoi(match.str(2));
        string c = match[3];
        string password = match[4];

        int char_count = count_char_in_string(password, c);
        
        if (min_count <= char_count && char_count <= max_count) {
            valid_password_count++;
        }
    }
    
    cout << valid_password_count << "\n";
    
    return 0;
}