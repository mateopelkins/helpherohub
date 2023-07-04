// Function to calculate the integral of a given polynomial 
function integratePolynomial(polynomial) { 
  
  // Initialize the result variable 
  let result = 0; 
  
  // Loop through each term in the polynomial 
  for (let i = 0; i < polynomial.length; i++) { 
    
    // Calculate the coefficient and exponent of the current term 
    let coefficient = polynomial[i][0]; 
    let exponent = polynomial[i][1]; 
    
    // Calculate the integral of the current term 
    let termIntegral = coefficient / (exponent + 1); 
    
    // Add the integral of the current term to the result 
    result += termIntegral; 
  } 
  
  // Return the result 
  return result; 
} 

// The function spends most of its execution time looping through the polynomial terms and calculating the integral of each term.