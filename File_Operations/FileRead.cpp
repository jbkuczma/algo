#include <iostream>
#include <fstream>

using namespace std;

string readFile(string file) {
	string line;
	string output;
	ifstream fileReader (file);
	if(fileReader.is_open()){
		while(getline(fileReader, line)){
			output = output + line + "\n";
		}
		fileReader.close();
	}
	return output;
}

int main(){
	string file = "read.txt";
	string output = readFile(file);
	cout << output;
	return 1;
}

/*
	Running from command line:
		1) Make <--- compile Makefile
		2) ./runFileRead.cpp <--- Execute compiled C++ file
*/

