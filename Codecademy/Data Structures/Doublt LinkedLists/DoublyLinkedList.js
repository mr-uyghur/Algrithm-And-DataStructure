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

    addToTail(data) {
        const newTail = new Node(data);
        const currentTail = this.tail;
        if (currentTail) {
            currentTail.setNextNode(newTail);
            newTail.setPreviousNode(currentTail);
        }
        this.tail = newTail;
        if (!this.head) {
            this.head = newTail;
        }
    }

    removeHead() {
        const removedHead = this.head;
        if (!removedHead) {
            return;
        }
        this.head = removedHead.getNextNode();
        if (this.head) {
            this.head.setPreviousNode(null);
        }
        if (removedHead === this.tail) {
            this.removeTail();
        }
        return removedHead.data;
    }

    // Create your .removeTail() method below:
    removeTail() {
        const removedTail = this.tail
        // if The list is empty, so there’s nothing to return, and the method ends
        if (!removedTail) {
            return
        }
        // update the list’s tail to be the current tail’s previous node
        this.tail = removedTail.getPreviousNode()
        // If there is still a tail to the list (meaning the list had more than one element when we started)
        // Set the tail’s next node to null
        if (this.tail) {
            this.tail.setNextNode(null)
        }
        // If the removed tail was also the head of the list (meaning there was only one element in the list), call .removeHead() to make the necessary changes to the head of the list
        if (removedTail === this.head) {
            this.removeHead()
        }
        // Finally, return the old tail
        return removedTail.data

    }


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