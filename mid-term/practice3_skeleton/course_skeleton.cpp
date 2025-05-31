#include <cstdlib>
#include <cstddef>
#include <cstring>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
const char ADD = 'A';
const char DELETE = 'D';
const char FIND = 'F';

class Student {
  //TODO
};

class Course {
public:
  Student* head;
  Course() {
    //TODO
  }
  ~Course() {
    //TODO
  }
  
  bool isEmpty() {
    return (head == nullptr);
  }

  bool addStudent(int id, string name);
  bool deleteStudent(int id);
  Student* find(int id);
  void write(ofstream& outFile);
};

bool Course::addStudent(int id, string name) {
  //TODO
}

bool Course::deleteStudent(int id) {
  //TODO
}

Student* Course::find(int id) {
  //TODO
}

void Course::write(ofstream& outFile) {
  //TODO
}

int main(int argc, char* argv[]) {
  if (argc != 3) {
    cerr<<"Correct usage: [program] [input] [output]"<<endl;
    exit(1);
  }
  Course course;
  ifstream inFile(argv[1]);
  ofstream outFile(argv[2]);
  string line;
  while (getline(inFile, line))
  {
    char op = line[0];
    istringstream iss(line.substr(1));
    int id;
    string name;
    Student* found = nullptr;
    cout <<line<<endl;
    switch(op)
    {
      case ADD:
        if (!(iss >> id >> name)) {
          cerr<<"ADD: invalid input"<<endl;
          exit(1);
        }
        if (course.addStudent(id, name))
          course.write(outFile);
        else
          outFile<<"Addition failed"<<endl;
        break;
      case DELETE:
        if (!(iss >> id)) {
          cerr<<"DELETE: invalid input"<<endl;
          exit(1);
        }
        if (course.deleteStudent(id))
          course.write(outFile);
        else
          outFile<<"Deletion failed"<<endl;
        break;
      case FIND:
        if (!(iss >> id)) {
          cerr<<"FIND: invalid input"<<endl;
          exit(1);
        }
        found = course.find(id);
        if (found == nullptr)
          outFile<<"Search failed"<<endl;
        else
          outFile<<found->id<<" "<<found->name<<endl;
        break;
      default:
        cerr<<"Undefined operator"<<endl;
        exit(1);
    }
  }
  outFile.close();
  inFile.close();
}
