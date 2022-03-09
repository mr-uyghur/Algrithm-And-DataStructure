class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor(){
        this.item = []
    }

    peek(){
        // this will show the top value of the stack(latest value in the stack)
        return this.item[this.item.length-1]
    }

    push(value){
        this.item.push(value);
        return this
    }
    // removes the top from stack
    pop(){
        this.item.pop(value)
        return this
    }
}

const myStack = new Stack();
myStack.push('google')
console.log(myStack.peek())