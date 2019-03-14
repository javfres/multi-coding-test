

// Import the reverse binary function
const reverse_binary = require('./reverse_binary');

// Helper function to pretty print
const num_2_binary = num => num.toString(2).padStart(10);
const pad_num = num => (num+'').padStart(3);

// Some numbers to test
const numbers = [13,11,5,667];

// Iterate over the numbres
numbers.map(num => {

    // Call the function
    const rnum = reverse_binary(num);

    // Print the result
    console.log(
        pad_num(num),
        num_2_binary(num),
        '->',
        pad_num(rnum),
        num_2_binary(rnum),
    );

});