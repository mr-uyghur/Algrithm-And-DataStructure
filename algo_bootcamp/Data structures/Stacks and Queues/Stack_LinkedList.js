class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor(){
        this.top = null;
        this.bottom = null;
        this.length = 0
    }

    peek(){
        // this will show the top value of the stack
        return this.top
    }

    push(value){
        const newNode = new Node(value) 
        // check if the stack is empty
        if(this.length === 0){
            this.top = newNode
            this.bottom = newNode
        } else{
            // if the list is not empty, we will replace the top with the new value
            const holdingPointer = this.top //this var is original value on stop of the stack
            this.top = newNode // set top equal to the newNode 
            this.top.next = holdingPointer // set the next value of newNode to the head
        }
        this.length++ 
        return this
    }
    // removes the top from stack
    pop(){
        // check if the stack is emoty
        if (!this.top){
            return null
        }
        // if there's only one node in the stack
        if(this.top === this.bottom){
            this.bottom = null
        }
        // const holdingPointer = this.top //var for whats currently on top
        this.top = this.top.next //top value equals its next value
        this.length --;
        return this

    }
}

const myStack = new Stack();
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.peek()
myStack.pop()
myStack.peek()