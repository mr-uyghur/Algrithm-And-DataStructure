const Node = require("./Node");

class LinkedList {
  constructor() {
    this.head = null;
  }

  addToHead(data) {
    const newHead = new Node(data);

    const currentHead = this.head;
    //change the list head to newHead node
    this.head = newHead;
    //if currentHead Exist in the list, set the current head to
    //the next value of new head node
    if (currentHead) {
      this.head.setNextNode(currentHead);
    }
  }

  addToTail(data) {
    let tail = this.head;
    //first check if the list is empty
    //if the linked list is empty then add a new node to the list
    if (!tail) {
      this.head = new Node(data);
    }
    //if the list isn't empty iterate through the data
    //till we reach the end(tail) of the linked list
    else {
      while (tail.getNextNode() !== null) {
        tail = tail.getNextNode();
      }
      tail.setNextNode(new Node(data));
    }
  }

  //remove head method
  //in this method, check if the list has a head
  //if it does then remove it by simply setting
  //the head equal to original head's next velue
  removeHead() {
    const removedHead = this.head;
    //if head don't exist in the list then just return
    if (!removedHead) {
      return;
    }
    //set head equal to original head node's next value
    this.head = removedHead.getNextNode();
    return removedHead.data;
  }
}

module.exports = LinkedList;
