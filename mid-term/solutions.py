# Practice 3. Linked List
# 학생 정보를 저장하는 노드 클래스
class Student:
    def __init__(self, i, n, p=None):
        self.id = i
        self.name = n
        self.next = p

# 정렬된 연결 리스트로 학생들을 관리하는 클래스
class Course:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    # 리스트가 비어있는지 확인
    def isEmpty(self):
        return len(self) == 0

    # 학생 추가 (정렬 유지)
    def addStudent(self, newID, newName):
        if self.find(newID):
            return False
        newStudent = Student(newID, newName)
        if self.isEmpty() or newID < self.head.id:
            newStudent.next = self.head
            self.head = newStudent
        else:
            prev = None
            current = self.head
            while current and current.id < newID:
                prev = current
                current = current.next
            newStudent.next = current
            prev.next = newStudent
        self.size += 1
        return True
    
    # 학생 삭제
    def deleteStudent(self, queryID):
        if self.isEmpty():
            return False
        prev, curr = None, self.head
        while curr and curr.id != queryID:
            if not prev: # 첫 번째인지
                self.head = curr.next
            else: # 중간인지/끝인지
                prev.next = curr.next
            prev, curr = curr, curr.next
        self.size -= 1
        return True

    # 학생 찾기
    def find(self, queryID):
        curr = self.head
        while curr:
            if curr.id == queryID:
                return curr
            elif curr.id > queryID:
                return None
            curr = curr.next
        return None

# Practice 4. Palindromes and Balance
# 문자열이 회문인지 판별하는 함수
def isPalindrome(string):
    stack = []
    for s in string:
        stack.append(s)
    for s in string:
        if stack.pop() != s:
            return False
    return True

# 괄호 문자열이 올바르게 짝지어졌는지 확인하는 함수
def balance(string):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    match = {}
    for i, ch in enumerate(closing):
        match[ch] = opening[i]
    stack = []
    for ch in string:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if len(stack) == 0 or stack[-1] != match[ch]:
                return False
            stack.pop()
    return len(stack) == 0

# Practice 5. Binary Search Tree
# 이진 탐색 트리의 노드 클래스
class TreeNode:
    def __init__(self, k, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r

# 이진 탐색 트리 클래스
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 트리가 비었는지 확인
    def isEmpty(self):
        return self.root == None
    
    # 정렬된 배열을 BST로 변환
    def arrayToBST(self, arr, l, r):
        if l > r:
            return None
        prev = arr[0]
        for k in arr:
            if prev > k:
                return None
            prev = k
        mid = (l + r) // 2
        node = TreeNode(arr[mid])
        node.left = self.arrayToBST(arr, l, mid - 1)
        node.right = self.arrayToBST(arr, mid + 1, r)
        return node
    
    # 최솟값 노드 반환
    def findMin(self):
        if self.isEmpty():
            return None
        p = self.root
        while p.left:
            p = p.left
        return p
    
    # 최댓값 노드 반환
    def findMax(self):
        if self.isEmpty():
            return None
        p = self.root
        while p.right:
            p = p.right
        return p

# Practices 6&7. Binary Search Tree Operations
# 이진 탐색 트리의 노드 클래스 (위와 동일)
class TreeNode:
    def __init__(self, k, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r

# 다양한 BST 연산이 구현된 클래스
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 트리가 비었는지 확인
    def isEmpty(self):
        return self.root == None

    # 정렬된 배열을 BST로 변환
    def arrayToBST(self, arr, l, r):
        if l == 0 and r == len(arr) - 1:
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return None
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(arr[mid])
        root.left = self.arrayToBST(arr, l, mid - 1)
        root.right = self.arrayToBST(arr, mid + 1, r)
        return root

    # 최솟값 노드 반환
    def findMin(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    # 최댓값 노드 반환
    def findMax(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current

    # 트리의 높이 구하기 (재귀)
    def _getHeight(self, curr):
        if not curr:
            return 0
        return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

    # 트리 출력 시 공백 출력 함수
    def _printSpaces(self, n, curr):
        for i in range(int(n)):
            print("  ", end="")
        if not curr:
            print(" ", end="")
        else:
            print(str(curr.key), end="")

    # 트리 구조를 계층적으로 출력
    def printTree(self):
        if not self.root:
            return  None
        queue = []
        queue.append(self.root)
        temp = []
        cnt = 0
        height = self._getHeight(self.root) - 1
        nMaxNodes = 2**(height + 1) - 1
        while cnt <= height:
            curr = queue.pop(0)
            if len(temp) == 0:
                self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
            else:
                self._printSpaces(nMaxNodes / (2**cnt), curr)
            if not curr:
                temp.append(None)
                temp.append(None)
            else:
                temp.append(curr.left)
                temp.append(curr.right)
            if len(queue) == 0:
                print("\n")
                queue = temp
                temp = []
                cnt += 1

    # 키 값으로 노드 탐색
    def search(self, query):
        current = self.root
        while current:
            if current.key == query:
                return current
            elif query < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # 중위 순회 결과를 파일에 기록
    def writeInorder(self, outFile):
        result = []
        self._inorderTraversal(self.root, result)
        outFile.write(" ".join(map(str, result)) + "\n")
        
    def _inorderTraversal(self, node, result):
        if node:
            self._inorderTraversal(node.left, result)
            result.append(node.key)
            self._inorderTraversal(node.right, result)

    # 전위 순회 결과를 파일에 기록
    def writePreorder(self, outFile):
        result = []
        self._preorderTraversal(self.root, result)
        outFile.write(" ".join(map(str, result)) + "\n")
        
    def _preorderTraversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorderTraversal(node.left, result)
            self._preorderTraversal(node.right, result)

    # 후위 순회 결과를 파일에 기록
    def writePostorder(self, outFile):
        result = []
        self._postorderTraversal(self.root, result)
        outFile.write(" ".join(map(str, result)) + "\n")
        
    def _postorderTraversal(self, node, result):
        if node:
            self._postorderTraversal(node.left, result)
            self._postorderTraversal(node.right, result)
            result.append(node.key)

    # 노드 삽입 (BST)
    def insertNode(self, k):
        if not self.root:
            self.root = TreeNode(k)
            return None
        current = self.root
        while True:
            if k < current.key:
                if current.left is None:
                    current.left = TreeNode(k)
                    return None
                current = current.left
            elif k > current.key:
                if current.right is None:
                    current.right = TreeNode(k)
                    return None
                current = current.right
            else:
                return None
                
    # 노드 삭제 (BST)
    def deleteNode(self, k):
        if not self.root:
            return None
        parent = None
        current = self.root
        while current and current.key != k:
            parent = current
            if k < current.key:
                current = current.left
            else:
                current = current.right
        if not current:
            return None
        # Case 1: 자식이 없는 경우
        if not current.left and not current.right:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        # Case 2: 자식이 하나인 경우
        elif not current.left:
            if current != self.root:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            else:
                self.root = current.right
        elif not current.right:
            if current != self.root:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
            else:
                self.root = current.left
        # Case 3: 자식이 둘인 경우
        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            current.key = successor.key
            if successor_parent != current:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

# Practices 6&7. Binary Search Tree Operations(AVL Tree)
# AVL 트리 노드 클래스 (높이 포함)
class TreeNode:
    def __init__(self, k, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r
        self.height = 1

# AVL 트리 클래스 (균형 잡힌 BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None
        
    # 노드의 높이 반환
    def _getNodeHeight(self, node):
        if not node:
            return 0
        return node.height
        
    # 균형 계수 계산
    def _getBalance(self, node):
        if not node:
            return 0
        return self._getNodeHeight(node.left) - self._getNodeHeight(node.right)
        
    # 오른쪽 회전
    def _rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._getNodeHeight(y.left), self._getNodeHeight(y.right)) + 1
        x.height = max(self._getNodeHeight(x.left), self._getNodeHeight(x.right)) + 1
        return x
         
    # 왼쪽 회전
    def _leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._getNodeHeight(x.left), self._getNodeHeight(x.right)) + 1
        y.height = max(self._getNodeHeight(y.left), self._getNodeHeight(y.right)) + 1
        return y

    # 배열을 AVL 트리로 변환
    def arrayToBST(self, arr, l, r):
        if l == 0 and r == len(arr) - 1:
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return None
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(arr[mid])
        root.left = self.arrayToBST(arr, l, mid - 1)
        root.right = self.arrayToBST(arr, mid + 1, r)
        # 높이 업데이트
        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
        # AVL 트리 균형 조정
        balance = self._getBalance(root)
        # Left Left Case
        if balance > 1 and self._getBalance(root.left) >= 0:
            return self._rightRotate(root)
        # Left Right Case
        if balance > 1 and self._getBalance(root.left) < 0:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)
        # Right Right Case
        if balance < -1 and self._getBalance(root.right) <= 0:
            return self._leftRotate(root)
        # Right Left Case
        if balance < -1 and self._getBalance(root.right) > 0:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)
        return root

    # 최솟값 노드 반환
    def findMin(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    # 최댓값 노드 반환
    def findMax(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current

    # 트리의 높이 구하기 (재귀)
    def _getHeight(self, curr):
        if not curr:
            return 0
        return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

    # 트리 출력 시 공백 출력 함수
    def _printSpaces(self, n, curr):
        for i in range(int(n)):
            print("  ", end="")
        if not curr:
            print(" ", end="")
        else:
            print(str(curr.key), end="")

    # 트리 구조를 계층적으로 출력
    def printTree(self):
        if not self.root:
            return None
        queue = []
        queue.append(self.root)
        temp = []
        cnt = 0
        height = self._getHeight(self.root) - 1
        nMaxNodes = 2**(height + 1) - 1
        while cnt <= height:
            curr = queue.pop(0)
            if len(temp) == 0:
                self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
            else:
                self._printSpaces(nMaxNodes / (2**cnt), curr)
            if not curr:
                temp.append(None)
                temp.append(None)
            else:
                temp.append(curr.left)
                temp.append(curr.right)
            if len(queue) == 0:
                print("\n")
                queue = temp
                temp = []
                cnt += 1

    # 키 값으로 노드 탐색
    def search(self, query):
        current = self.root
        while current:
            if current.key == query:
                return current
            elif query < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # 중위 순회 결과를 파일에 기록
    def writeInorder(self, outFile):
        result = []
        self._inorderTraversal(self.root, result)
        outFile.write(" ".join(map(str, result)) + "\n")
        
    def _inorderTraversal(self, node, result):
        if node:
            self._inorderTraversal(node.left, result)
            result.append(node.key)
            self._inorderTraversal(node.right, result)

    # 전위 순회 결과를 파일에 기록
    def writePreorder(self, outFile):
        result = []
        self._preorderTraversal(self.root, result)
        outFile.write(" ".join(map(str, result)) + "\n")
        
    def _preorderTraversal(self, node, result):
        if node:
            result.append(node.key)
            self._preorderTraversal(node.left, result)
            self._preorderTraversal(node.right, result)

    # 후위 순회 결과를 파일에 기록
    def writePostorder(self, outFile):
        result = []
        self._postorderTraversal(self.root, result)
        outFile.write(" ".join(map(str, result)) + "\n")
        
    def _postorderTraversal(self, node, result):
        if node:
            self._postorderTraversal(node.left, result)
            self._postorderTraversal(node.right, result)
            result.append(node.key)

    # 노드 삽입 (AVL)
    def insertNode(self, k):
        self.root = self._insertAVL(self.root, k)
        
    def _insertAVL(self, node, k):
        # 일반적인 BST 삽입
        if not node:
            return TreeNode(k)
        if k < node.key:
            node.left = self._insertAVL(node.left, k)
        elif k > node.key:
            node.right = self._insertAVL(node.right, k)
        else:  # 중복 키는 허용하지 않음
            return node
        # 노드 높이 업데이트
        node.height = 1 + max(self._getNodeHeight(node.left), self._getNodeHeight(node.right))
        # 균형 인수 확인 및 회전
        balance = self._getBalance(node)
        # Left Left Case
        if balance > 1 and k < node.left.key:
            return self._rightRotate(node)
        # Right Right Case
        if balance < -1 and k > node.right.key:
            return self._leftRotate(node)
        # Left Right Case
        if balance > 1 and k > node.left.key:
            node.left = self._leftRotate(node.left)
            return self._rightRotate(node)
        # Right Left Case
        if balance < -1 and k < node.right.key:
            node.right = self._rightRotate(node.right)
            return self._leftRotate(node)
        return node

    # 노드 삭제 (AVL)
    def deleteNode(self, k):
        if not self.root:
            return
        self.root = self._deleteAVL(self.root, k)
        
    def _deleteAVL(self, node, k):
        # 일반적인 BST 삭제
        if not node:
            return node
        if k < node.key:
            node.left = self._deleteAVL(node.left, k)
        elif k > node.key:
            node.right = self._deleteAVL(node.right, k)
        else:
            # 삭제할 노드 찾음
            # 자식이 하나이거나 없는 경우
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # 두 자식이 있는 경우, 오른쪽 서브트리에서 가장 작은 값(인오더 후속자) 찾기
            temp = node.right
            while temp.left:
                temp = temp.left
            node.key = temp.key
            node.right = self._deleteAVL(node.right, temp.key)
        # 삭제 후 노드가 없으면 반환
        if not node:
            return node
        # 높이 업데이트
        node.height = 1 + max(self._getNodeHeight(node.left), self._getNodeHeight(node.right))
        # 균형 계수 확인 및 회전
        balance = self._getBalance(node)
        # Left Left Case
        if balance > 1 and self._getBalance(node.left) >= 0:
            return self._rightRotate(node)
        # Left Right Case
        if balance > 1 and self._getBalance(node.left) < 0:
            node.left = self._leftRotate(node.left)
            return self._rightRotate(node)
        # Right Right Case
        if balance < -1 and self._getBalance(node.right) <= 0:
            return self._leftRotate(node)
        # Right Left Case
        if balance < -1 and self._getBalance(node.right) > 0:
            node.right = self._rightRotate(node.right)
            return self._leftRotate(node)
        return node