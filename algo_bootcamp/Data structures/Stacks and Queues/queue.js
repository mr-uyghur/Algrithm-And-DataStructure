class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    peek() {
        if (!this.first) {
            return null
        }
        else {
            return this.first
        }
    }

    enqueue(value) {
        const newNode = new Node(value)
        if (this.length == 0) {
            this.first = newNode;
            this.last = newNode
        }
        else {
            this.last.next = newNode // point next value to the newNode
            this.last = newNode
            
        }
        this.length++;
        return this
    }

    dequeue() {
        if(!this.first){
            return null //return null if the queue is empty
        }
        if(this.first === this.last){
            this.last = null; //if there's only one node in the queues
        }

        this.first = this.first.next // set the first value to its next value in Queue
        this.length--
        return this
    }
}