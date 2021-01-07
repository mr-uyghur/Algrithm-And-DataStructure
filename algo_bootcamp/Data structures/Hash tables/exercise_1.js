//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined


function firstRecurringCharacter(input) {
    // place holder for our data 
    let data = {}
    // loop through the given input, add them to my data hash as key, increase the value by 1 if the key repeats
    for(let i =0; i<input.length; i++) {   
        // temp var for current index 
        let temp = input[i]
        // add temp into data, if the same key already exist, increase value by 1
        if(data[temp] === undefined){
            data[temp] = 1 
        } else if(data[temp] == 1){ //this logic return the first recurring number
            ++data[temp]
            return temp
        }
    }
    return false
}
console.log(firstRecurringCharacter([2,5,5,2,3,5,1,2,4]))


//Bonus... What if we had this:
// [2,5,5,2,3,5,1,2,4]
// return 5 because the pairs are before 2,2