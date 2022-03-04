#include <iostream>
#include <fstream>
#include "windows.h"
using namespace std;

//ref: https://www.cnblogs.com/huangsitao/p/10297455.html
std::string getProgramDir() {
    char exeFullPath[MAX_PATH]; // Full path
    std::string strPath = "";
    GetModuleFileName(NULL,exeFullPath,MAX_PATH);
    strPath=(std::string)exeFullPath;
    return strPath;
}

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

string getPath(string path) {
  int pos = path.find_last_of('\\', path.length());
  return path.substr(0, pos);
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
//  cout << "main" << endl;
  string fullPath = getProgramDir();
  string name = getName(fullPath);
  string env = getPath(fullPath);

  ifstream file(env + "\\" + name + ".txt");
  string line;
  getline(file, line);
  for (int i = 1; i < argc; i++) {
    string tmp = argv[i];
    line = line + " " + addQuote(tmp);
  }
  const char *cmd = line.c_str();
//  cout  << "[cmd] " << cmd << endl;
  system(cmd);
  return 0;
}