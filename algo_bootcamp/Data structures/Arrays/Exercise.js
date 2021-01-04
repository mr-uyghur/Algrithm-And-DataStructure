// Reverse a String 
// "Hi my name is Ali" shouble be:
// 'ilA si eman ym iH'

function reverse(str){
    // check input, mke sure its a str
    if(!str || str.length < 2 || typeof str !== 'string'){
        return 'hmm pass in a str'
    }
    // place holder var for new string 
    let newStr = ""
    // loop through str in rever order and add each index to the new Str
    for(let i=str.length - 1; i >=0 ; i--){
        newStr += str[i]
    }
    return newStr
}

console.log(reverse("Hi my name is Ali"))

// alternate way with built in method
function reverse2(str){
    // check for input
    if(!str || str.length < 2 || typeof str !== 'string'){
        return 'hmm pass in a str'
    }
    // split str into array and reverse the array and convert to str with join method
    return str.split('').reverse().join('')
}
console.log(reverse2("Hi my name is Ali"))






