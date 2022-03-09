class BinaryTree {
  constructor(value, depth = 1) {
    this.value = value;
    this.depth = depth;
    this.left = null;
    this.right = null;
  }
  //insert new value to the tree
  /*------------------------------------------------------------
  insersion Logic:
  If the new value is less than the root node's value
  If a left child node doesn't exist 
    Create a new BinaryTree with the new value at a greater depth and assign it to the left pointer
  Else
    Recursively call .insert() on the left child node  
Else
  If a right child node doesn't exist
    Create a new BinaryTree with the new value at a greater depth and assign it to a right pointer
  Else
    Recursively call .insert() on the right child node 
  ----------------------------------------------------------------*/
  insert(value){
    if(value < this.value){
      if(!this.left){
        this.left = new BinaryTree(value, this.depth + 1);
      }
      else{
        this.left.insert(value)
      }
    }
    else{
      if(!this.right){
        this.right = new BinaryTree(value, this.depth + 1);
      }
      else{
        this.right.insert(value)
      }
    }
  }

   //getter node method
  /*--------------------------------------------------
  If target value is the same as the current node value
  Return the current node
Else
  If target value is less than the root node's value and there is a left child node
    Recursively search from the left child node
  Else if there is a right child node
    Recursively search from the right child node
  ---------------------------------------------------*/
  getNodeByValue(value){
    if(value === this.value){
      return this
    }
    else if((this.left) && (value < this.value)){
      return this.left.getNodeByValue(value)
    }
    else if((this.right) && (value > this.value)){
      return this.right.getNodeByValue(value)
    }
    else{
    return null
    }
  }

  //Traversing a binary tree
  depthFirstTraversal(){
    if(this.left){
      this.left.depthFirstTraversal()
    }
    console.log(`Depth=${this.depth}, Value=${this.value}`);

    if(this.right){
      this.right.depthFirstTraversal()
    }
  }
  
};

module.exports = BinaryTree;
