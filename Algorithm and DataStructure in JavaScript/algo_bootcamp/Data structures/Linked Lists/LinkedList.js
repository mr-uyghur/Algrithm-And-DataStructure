class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head
    }

    append(value) {
        // add values 
        const newNode = {
            value: value,
            next: null
        }
        this.tail.next = newNode
        this.tail = newNode
        return this
    }

    prepend(value) {
        // add value to the beginning of the linked list
        const newNode = {
            value: value,
            next: null
        }
        newNode.next = this.head
        this.head = newNode
        return this

    }
    printList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value)
            currentNode = currentNode.next
        }
        return array;
    }
    insert(index, value) {
        // if added index is greater than the linkedlist length then add value to the tail 
        if (index >= this.length) {
            return this.append(value)
        }
        // create newNode 
        const newNode = {
            value: value,
            next: null
        }
        // get to the node index
        const leader = this.findIndex(index - 1)
        const holdingPointer = leader.next
        leader.next = newNode
        newNode.next = holdingPointer
        this.length++
        return this.printList()
    }
    findIndex(index) {
        let currentNode = this.head;
        let count = 0

        while (count !== index) {
            currentNode = currentNode.next
            count++
        }
        return currentNode
    }
    // remove
    remove(index) {
        const leader = this.findIndex(index - 1)
        const pointerHolder = leader.next
        leader.next = pointerHolder.next
        this.length--
        return this.printList()
    }

    reverse() {
        // check if list only has 1 node, return that node
        if (!this.head.next) {
            return this.head
        }
        let first = this.head //first node
        this.tail = this.head
        let second = first.next // first node --> second node

        // as long as there's a next node
        // swap nodes
        while(second){
            const temp = second.next // temp var that holds the 3rd value initially
            second.next = first // reverse the pointer
            first = second 
            second = temp
        }
        this.head.next = null
        this.head = first
        return this.printList()
    }
}
const myList = new LinkedList(100)
myList.append(200)
myList.append(300)
myList.prepend(700)
myList.insert(2, 99)
myList.printList()
myList.reverse()
