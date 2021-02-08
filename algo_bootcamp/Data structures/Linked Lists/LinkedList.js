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

    prepend(value){
        // add value to the beginning of the linked list
        const newNode = {
            value:value,
            next:null
        }
        newNode.next = this.head
        this.head = newNode
        return this

    }


}
const myList = new LinkedList(100)
myList.append(200)
myList.append(300)
myList. prepend(700)
console.log(myList)