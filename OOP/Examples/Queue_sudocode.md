Public Class Queue extends ADT # ADT is Abstract Data Type
    # attributes
    private [object] items # list of items
    private int rear 
    private int front
    private int length 
    
    # constructor '__init__' in python
    public procedure new(given_length)
        length = given_length
        rear = items[-1]
        front = items[0]

    # dequeue - thsi si probably not a great example of a deque function
    public function dequeue()
        if front == -1
            return null
        else
            temp = items[front]
            front = front + 1
            return temp
