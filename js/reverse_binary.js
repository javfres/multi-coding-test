


// Only this function defined in the module
module.exports = (num) => {

    // Extra protection
    if(num<0){
        throw "Negative numbers not supported";
    }

    // To bin str
    let bin = num.toString(2);

    // Reverse. TODO: check if this is efficient or not
    bin = [...bin].reverse().join('');

    // bin str to num
    return parseInt(bin, 2);

};