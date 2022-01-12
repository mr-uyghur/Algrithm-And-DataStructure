const LinkedList = require("./Linkedlist");

class Queue {
  constructor() {
    this.queue = new LinkedList();
    this.size = 0;
  }

  //enqueue method
  enqueue(data) {
    this.queue.addToTail(data);
    //also increase the size of queue
    this.size += 1;
    console.log(`Added ${data}! Queue size is now ${this.size}`);
  }

  dequeue() {
    const data = this.queue.removeHead();
    this.size--;
    console.log(`Removed ${data} from queue! Queue size is now ${this.size}.`);
    return data;
  }
}

module.exports = Queue;

const restaurantOrder = new Queue();
console.log(`restaurantOrder queue has ${restaurantOrder.size} orders.\n`);
restaurantOrder.enqueue("apple pie");
restaurantOrder.enqueue("roast chicken");
restaurantOrder.enqueue("quinoa salad");
