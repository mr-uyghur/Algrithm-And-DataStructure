// create a Binary tree structure

class Node {
    constructor(value){
        this.left = null
        this.right = null
        this.value = value
    }
}

class BinarySearchTree{
    constructor(){
        this.root= null
    }

    insert(value){
        const newNode = new Node(value)
        if(this.root === null){
            this.root = newNode
            return this
        }
        else {
            let currentNode = this.root 
            while(true){ //treversing
                if(value < currentNode.value){ //is the value less than the current root?
                    //left
                    //logic below will keep looping till we find a node that doesn't have a left side
                    if(!currentNode.left){ //if the left node is empty
                        currentNode.left = newNode
                        return this
                    }
                    currentNode = currentNode.left //shift currentNode to its left if node left isn't null
                } else{
                    //Right if value is greater than current node
                    //similar logic as above
                    if(!currentNode.right){
                        currentNode.right = newNode
                        return this
                    }
                    currentNode = currentNode.right //keep looping to the right till node right is null
                }
            } 
        }

    }

    lookup(value){

    }
}