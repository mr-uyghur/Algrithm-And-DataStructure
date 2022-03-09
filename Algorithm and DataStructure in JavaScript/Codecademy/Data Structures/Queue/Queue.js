const LinkedList = require("./LinkedList");

class Queue {
  constructor(maxSize = Infinity) {
    this.queue = new LinkedList();
    this.size = 0;
    this.maxSize = maxSize;
  }

  //this method checks if the queue has reached capacity
  hasRoom() {
    if (this.size < this.maxSize) {
      return true;
    } else {
      return false;
    }
  }

  isEmpty() {
    if (this.size == 0) {
      return true;
    } else {
      return false;
    }
  }

  enqueue(data) {
    if (this.hasRoom()) {
      this.queue.addToTail(data);
      this.size++;
      console.log(`Added ${data} to queue! Queue size is now ${this.size}.`);
    } else {
      throw "Queue is full!";
    }
  }

  dequeue() {
    if (!this.isEmpty()) {
      const data = this.queue.removeHead();
      this.size--;
      console.log(
        `Removed ${data} from queue! Queue size is now ${this.size}.`
      );
      return data;
    }
    if (this.isEmpty()) {
      throw "Queue is empty!";
    }
  }
}

module.exports = Queue;
