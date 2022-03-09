const LinkedList = require('./LinkedList');
const seasons = new LinkedList()
console.log(seasons.printList())

seasons.addToHead('summer')
seasons.addToHead('spring')
console.log(seasons.printList())
seasons.addToTail('fall')
seasons.addToTail('winter')
console.log(seasons.printList())

seasons.removeHead()
console.log(seasons.printList())