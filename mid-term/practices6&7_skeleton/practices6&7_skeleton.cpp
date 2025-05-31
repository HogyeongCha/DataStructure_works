// Practices 6&7. Binary Search Tree Operations
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <tuple>
#include <utility>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
const char BUILD = 'B';
const char FIND_MIN = 'm';
const char FIND_MAX = 'M';
const char SEARCH = 'S';
const char INSERT = 'I';
const char DELETE = 'D';
const char INORDER = 'N';
const char PREORDER = 'R';
const char POSTORDER = 'O';

class TreeNode {
public:
  int key;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int k, TreeNode* l=nullptr, TreeNode* r=nullptr) {
    key = k;
    left = l;
    right = r;
  }
};

class BinarySearchTree {
public:
  TreeNode* root;
  BinarySearchTree(): root(nullptr) {}
  ~BinarySearchTree();

  TreeNode* arrayToBST(vector<int>&, int, int);
  // Return true if tree is empty; false otherwise
  bool isEmpty() { return (root == nullptr); }
  TreeNode* findMin();
  TreeNode* findMax();
  TreeNode* search(int);
  void insertNode(int);
  void deleteNode(int);
  void writeInorder(ofstream&);
  void writePreorder(ofstream&);
  void writePostorder(ofstream&);
  void printTree();
private:
  int _getHeight(TreeNode*);
  void _printSpaces(double, TreeNode*);
};

BinarySearchTree::~BinarySearchTree() {
  // Practice 5
}

// Given a sequence arr of integers, start index l, the end index r, 
// build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
// Return the root node of the tree
TreeNode* BinarySearchTree::arrayToBST(vector<int>& arr, int l, int r) {
  // Practice 5
}

// Return the node with the minimum value 
TreeNode* BinarySearchTree::findMin() {
  // Practice 5
}

// Return the node with the maximum value 
TreeNode* BinarySearchTree::findMax() {
  // Practice 5

}

// Given a query, search for the node whose key is equal to query.
// If the node exists, return the key
// Otherwise, return nullptr
TreeNode* BinarySearchTree::search(int query) {
  // TODO. Practice 6
}

// If node with key k alreay exists in the tree, do nothing
// Otherwise, insert a new node with key k 
void BinarySearchTree::insertNode(int k) {
  // TODO. Practice 7
}

// If deletion fails, immediately terminate the program
// Otherwise, delete the node with key k
void BinarySearchTree::deleteNode(int k) { 
  // TODO. Practice 7
}

// Given an output file stream, write the keys of all the nodes 
// visited in inorder traversal
void BinarySearchTree::writeInorder(ofstream& outFile) {
  // Practice 6
}

// Given an output file stream, write the keys of all the nodes 
// visited in preorder traversal
void BinarySearchTree::writePreorder(ofstream& outFile) {
  // Practice 6
}

// Given an output file stream, write the keys of all the nodes 
// visited in postorder traversal
void BinarySearchTree::writePostorder(ofstream& outFile) {
  // Practice 6
}

int BinarySearchTree::_getHeight(TreeNode* curr) {
  if (curr == nullptr) 
    return 0;
  return 1 + max(_getHeight(curr->left), _getHeight(curr->right));
}

void BinarySearchTree::_printSpaces(double n, TreeNode* curr) {
  for(double i = 0; i < n; ++i) 
    cout<<"  ";
  if (curr == nullptr)
    cout<<" ";
  else
    cout<<curr->key;
}

void BinarySearchTree::printTree() {
  if (root == nullptr)
    return;
  queue<TreeNode*> q;
  q.push(root);
  queue<TreeNode*> temp;
  int cnt = 0;
  int height = _getHeight(root) - 1;
  double nMaxNodes = pow(2, height + 1) - 1;
  while (cnt <= height) {
    TreeNode* curr = q.front();
    q.pop();
    if (temp.empty())
      _printSpaces(nMaxNodes / pow(2, cnt + 1) + height - cnt, curr);
    else
      _printSpaces(nMaxNodes / pow(2, cnt), curr);
    if (curr == nullptr) {
      temp.push(nullptr);
      temp.push(nullptr);
    }
    else {
      temp.push(curr->left);
      temp.push(curr->right);
    }
    if (q.empty()) {
      cout<<endl<<endl;
      q = temp;
      queue<TreeNode*> empty;
      swap(temp, empty);
      ++cnt;
    }
  }
}

int main(int argc, char* argv[]) {
  if (argc != 3) {
    cerr<<"Correct usage: [exe] [input] [output]"<<endl;
    exit(1);
  }
  BinarySearchTree tree;
  ifstream inFile(argv[1]);
  ofstream outFile(argv[2]);
  string line;
  while (getline(inFile, line))
  {
    char op = line[0];
    istringstream iss(line.substr(1));
    int k;
    TreeNode* found = nullptr;
    vector<int> data;
    switch(op)
    {
      case BUILD:
        while (iss >> k)
          data.push_back(k);
        tree.root = tree.arrayToBST(data, 0, data.size() - 1);
        if (tree.root) {
          outFile<<BUILD<<endl;
        }
        else {
          cerr<<"BUILD: invalid input"<<endl;
          exit(1);
        }
        tree.printTree();
        break;
      case FIND_MIN:
        found = tree.findMin();
        if (found == nullptr) {
          cerr<<"FindMin failed"<<endl;
          exit(1);
        }
        else {
          outFile<<found->key<<endl;
        }
        break;
      case FIND_MAX:
        found = tree.findMax();
        if (found == nullptr) {
          cerr<<"FindMax failed"<<endl;
          exit(1);
        }
        else {
          outFile<<found->key<<endl;
        }
        break;
      case SEARCH:
        if (!(iss >> k)) {
          cerr<<"SEARCH: invalid input"<<endl;
          exit(1);
        }
        // Practice 6. Call the function for search
        break;
      case INORDER:
        // Practice 6. Call the function for inorder traversal;
        break;
      case PREORDER:
        // Practice 6. Call the function for preorder traversal;
        break;
      case POSTORDER:
        // Practice 6. Call the function for postorder traversal;
        break;
      case INSERT:
        if (!(iss >> k)) {
          cerr<<"INSERT: invalid input"<<endl;
          exit(1);
        }
        // TODO. Practice 7. Call the function for insertion
        break;
      case DELETE:
        if (!(iss >> k)) {
          cerr<<"DELETE: invalid input"<<endl;
          exit(1);
        }
        // TODO. Practice 7. Call the function for deletion
        break;
      default:
        cerr<<"Undefined operator"<<endl;
        exit(1);
    }
  }
  outFile.close();
  inFile.close();
}
