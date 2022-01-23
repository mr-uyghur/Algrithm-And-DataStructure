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
};

module.exports = BinaryTree;
