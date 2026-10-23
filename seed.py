"""Demo data. Questions 1-14 come from the uploaded GATE paper (Q15-40 were blank placeholders, so skipped)."""
from datetime import datetime, timedelta
N1, N2 = 1 / 3, 2 / 3
# (type, text, options, answer, marks, negative)
QS = [
 ("MCQ", "A population contains equal numbers of men and women. 20% of men and 10% of women are unemployed. A person is selected at random; the probability that the person is employed is [GATE ME 2014 Set 3]", ["0.65", "0.70", "0.75", "0.85"], ["D"], 1, N1),
 ("MCQ", "A fair six-faced die is rolled repeatedly. The long-run mean of the outcomes is", ["2.5", "3.0", "3.5", "4.0"], ["C"], 1, N1),  # source key highlighted B (3.0); 3.5 is correct
 ("MCQ", "Two fair coins are tossed simultaneously. The probability of obtaining at least one head is [GATE ME 2017 Set 2]", ["1/4", "3/4", "1", "1/2"], ["B"], 1, N1),
 ("MSQ", "A fair coin is tossed 5 times. The probability of obtaining exactly 2 heads is", ["10/32", "6/32", "5/32", "15/32"], ["A"], 1, 0),
 ("MSQ", "If X is uniformly distributed on [0,4], its standard deviation is", ["1", "Sqrt(3)", "2/sqrt(3)", "4/sqrt(3)"], ["C"], 1, 0),
 ("NAT", "The lifetime X of a component is exponentially distributed with parameter λ=2. What is P(X>1)? (up to 4 decimals)", [], ["0.1353"], 1, 0),
 ("MCQ", "Let Y be uniformly distributed on (1,6). The probability that the quadratic 3x^2+6xY+3Y+6=0 has real roots is", ["0.4", "0.8", "0.5", "1"], ["B"], 2, N2),
 ("MCQ", "Events A and B satisfy P(A)=0.6, P(B)=0.5 and P(A∩B)=0.3. Then P(A|B) equals", ["0.3", "0.5", "0.6", "0.8"], ["C"], 2, N2),
 ("MCQ", "Let X be a Gaussian random variable with mean 0 and variance σ². Define Y=max(X,0). A median of Y is", ["-σ", "0", "2σ", "σ"], ["B"], 2, N2),
 ("MSQ", "If X~Poisson(5), then E[(X+2)^2] is", ["25", "49", "54", "59"], ["C"], 2, 0),
 ("MSQ", "A lot contains 10% defective items. If 5 items are selected independently, the probability of exactly one defective item is", ["0.32805", "0.59049", "0.40951", "0.65610"], ["A"], 2, 0),
 ("NAT", "A density is f(x)=1/x^2 on [a,1] and 0 elsewhere. For f to be a valid PDF, 'a' must be ___", [], ["0.5"], 2, 0),
 ("NAT", "A bag has 10 red and 15 blue balls. Two are drawn without replacement. Given the first is red, P(second is red) = ___ (decimal)", [], ["0.375"], 2, 0),
]

P="Data Structures"
QB = [
 ("MCQ","Which data structure is most suitable for checking whether parentheses in an expression are balanced?",["Queue","Stack","Binary heap","Hash table"],"B",1),
 ("MCQ","A queue follows which order of element removal?",["LIFO","FIFO","Sorted order","Random order"],"B",1),
 ("MCQ","In a singly linked list, insertion at the beginning, when a head pointer is available, takes:",["Θ(1)","Θ(log n)","Θ(n)","Θ(n log n)"],"A",1),
 ("MCQ","Which traversal of a binary search tree outputs keys in non-decreasing order?",["Preorder","Postorder","Inorder","Level order"],"C",1),
 ("MCQ","The maximum number of edges in a tree with n vertices is:",["n","n − 1","n + 1","2n"],"B",1),
 ("MCQ","Which data structure is typically used to implement recursion?",["Stack","Queue","Heap","Graph"],"A",1),
 ("MCQ","In a min-heap, the key at the root is:",["The maximum key","The minimum key","Always the median","Unrelated to other keys"],"B",1),
 ("MCQ","For a hash table with chaining, collisions are handled by:",["Sorting the table","Storing colliding entries in a list/bucket","Rejecting duplicate hash values","Rehashing after every insertion"],"B",1),
 ("MCQ","Which operation is supported in Θ(1) time by a stack implemented using a linked list with a head pointer?",["Access the middle element","Push at the head","Search an arbitrary key","Sort all elements"],"B",1),
 ("MCQ","A complete binary tree with n nodes has height (edges on the longest root-to-leaf path) of order:",["Θ(1)","Θ(log n)","Θ(n)","Θ(n log n)"],"B",1),
 ("MSQ","Which are valid properties of a binary search tree with distinct keys? Select all that apply.",["Every key in the left subtree is smaller than the node key","Every key in the right subtree is smaller than the node key","Inorder traversal yields sorted keys","The tree must be height-balanced"],"A,C",1),
 ("MSQ","Which statements about stacks and queues are correct? Select all that apply.",["Stack removal is LIFO","Queue removal is FIFO","A queue is always implemented using an array","A stack can be used for postfix evaluation"],"A,B,D",1),
 ("NAT","A stack is initially empty. push(4), push(7), pop(), push(2), push(9), pop(). What value is returned by the second pop? (integer)",[],"9",1),
 ("NAT","A tree has 18 vertices. How many edges does it contain? (integer)",[],"17",1),
 ("MCQ","A circular queue is stored in an array of size n, one slot left unused to distinguish full from empty. The next insertion position is (REAR + 1) mod n. Which condition indicates the queue is full?",["FRONT = REAR","(REAR + 1) mod n = FRONT","REAR = n − 1","FRONT = 0"],"B",2),
 ("MCQ","A non-circular singly linked queue has head and tail pointers and n nodes. Enqueue inserts at the head and dequeue deletes from the tail. Most efficient worst-case complexities for enqueue and dequeue, respectively?",["Θ(1), Θ(1)","Θ(1), Θ(n)","Θ(n), Θ(1)","Θ(n), Θ(n)"],"B",2),
 ("MCQ","A binary min-heap contains n elements. The worst-case time complexity of inserting one new element is:",["Θ(1)","Θ(log n)","Θ(n)","Θ(n log n)"],"B",2),
 ("MCQ","Insert 40, 20, 60, 10, 30 into an initially empty BST in that order. What is the preorder traversal?",["10, 20, 30, 40, 60","40, 20, 10, 30, 60","10, 30, 20, 60, 40","40, 60, 20, 30, 10"],"B",2),
 ("MCQ","Evaluate the postfix expression: 5 2 3 * + 8 −. What is the result?",["3","5","9","13"],"A",2),
 ("MCQ","A hash table has m slots and uses separate chaining. If n keys are stored, the load factor α is:",["m/n","n/m","n + m","n × m"],"B",2),
 ("MCQ","A full binary tree has 15 internal nodes. How many leaves does it have?",["7","14","15","16"],"D",2),
 ("MCQ","For an array-based binary heap, the left child of a node at zero-based index i is at index:",["2i","2i + 1","2i + 2","(i − 1)/2"],"B",2),
 ("MSQ","Which operations can be performed in Θ(1) time in a singly linked list when the relevant pointer(s) are available? Select all that apply.",["Insert after a given node","Delete the head node","Find the node at position n/2 without traversal","Insert at the head"],"A,B,D",2),
 ("MSQ","Which statements about binary heaps are correct? Select all that apply.",["A min-heap is a complete binary tree","In a min-heap, every parent key is no greater than its children","An inorder traversal of a heap always gives sorted order","The minimum element of a min-heap is at the root"],"A,B,D",2),
 ("MSQ","Which statements about graph representations are correct? Select all that apply.",["An adjacency matrix uses Θ(V²) space","An adjacency list uses Θ(V + E) space for a sparse graph","BFS commonly uses a queue","DFS cannot be implemented using a stack"],"A,B,C",2),
 ("NAT","A max-heap is built by inserting the keys 12, 7, 25, 15 in that order. What is the root key after all insertions? (integer)",[],"25",2),
 ("NAT","A hash table has 10 slots and stores 25 keys using separate chaining. Calculate the load factor α. (decimal)",[],"2.5",2),
]
for t,q,o,a,m in QB: QS.append((t,q,o,a.split(","),m,(m/3 if t=="MCQ" else 0)))
def seed(s, hash_pw, User, Exam, Question):
    users = [("admin", "Administrator", "admin", "admin123", ""), ("faculty1", "Dr. Faculty", "faculty", "faculty123", "")]
    users += [(f"21AIML{i:03d}", f"Student {i}", "student", "student123", "II-AIML-B") for i in range(1, 6)]
    # Student batch 25AM064 to 25AM127
    users += [(f"25AM{i:03d}", f"Student 25AM{i:03d}", "student", "student123", "I-AIML") for i in range(64, 128)]
    # Lateral entry logins
    laterals = ["26AML08", "26AML09", "26AML10", "26AML11"]
    users += [(lat, f"Student {lat}", "student", "student123", "II-AIML-Lateral") for lat in laterals]
    for u, n, r, p, k in users: s.add(User(username=u, name=n, role=r, pw=hash_pw(p), klass=k, dept="AIML"))
    s.commit()
    fac = s.query(User).filter_by(username="faculty1").one()
    ids = [x.id for x in s.query(User).filter_by(role="student")]
    e = Exam(title="GATE Aptitude I - CIAT (Probability + Data Structures)", subject="GATE", start=datetime.utcnow() - timedelta(hours=1), end=datetime.utcnow() + timedelta(days=30),
             duration=90, pass_pct=40, published=True, show_results=False, seb_required=False, public=True, access_code="GATE2026", assigned=ids, created_by=fac.id)
    s.add(e); s.commit()
    for i, (t, q, o, a, m, n) in enumerate(QS, 1): s.add(Question(exam_id=e.id, pos=i, text=q, qtype=t, options=o, answer=a, marks=m, neg=n, subject="Probability" if i<14 else "Data Structures"))
    s.commit()

