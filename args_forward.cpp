#include <iostream>
#include <fstream>
using namespace std;

string getName(string path) {
  string output = "";
  int i = path.length() - 1;
  if (path.length() > 4 && path.substr(path.length()-4) == ".exe") {
    i -= 4;
  };
  while (i >= 0 && path[i] != '\\' && path[i] != '/') {
    output = path[i] + output;
    i--;
  }
  return output;
}

string addQuote(string s) {
  bool haveSpace = false;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == ' ') {
      return "\"" + s + "\"";
    }
  }
  return s;
}

int main(int argc, char *argv[]) {
  string name = argv[0];
  name = getName(name);
  string env = getenv("FASTCMD_HOME");
  cout << env << endl;
  ifstream file(env + "\\" + name + ".txt");
  string line;
  getline(file, line);
  for (int i = 1; i < argc; i++) {
    string tmp = argv[i];
    line = line + " " + addQuote(tmp);
  }
  const char *cmd = line.c_str();
  cout  << "[cmd] " << cmd << endl;
  system(cmd);
  return 0;
}