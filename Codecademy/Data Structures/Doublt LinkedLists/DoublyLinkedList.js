const Node = require('./Node');

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToHead(data) {
        const newHead = new Node(data);
        const currentHead = this.head;
        if (currentHead) {
            currentHead.setPreviousNode(newHead);
            newHead.setNextNode(currentHead);
        }
        this.head = newHead;
        if (!this.tail) {
            this.tail = newHead;
        }
    }

    // Create your .addToTail() method below:


    printList() {
        let currentNode = this.head;
        let output = '<head> ';
        while (currentNode !== null) {
            output += currentNode.data + ' ';
            currentNode = currentNode.getNextNode();
        }
        output += '<tail>';
        console.log(output);
    }
}

module.exports = DoublyLinkedList;