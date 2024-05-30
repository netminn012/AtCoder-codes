>>++++++++++<<  [>>++++++++++<<-]>     // base = 10000
>>>++++++++++[>++++++++++<-]>+>++++   // n = 8400, i = 0, temp = 0
[<+>-]<                        // Move to i

// Calculate numerator array
<[
  >>>>++++++++++[<----->-]<[>+>+<<-]>>   // base / 5
  [<+>-]                           // Copy to numerator[i]
  <+                               // Increment i
  >-]                             // Loop until i == n

// Main calculation loop
>>>>>                               // Move to n
[
  <<<<<<[-]>[-]                     // Set out = 0
  <[->>+>+<<<]>>[-<<+>>]<<          // Move n to temp and denom
  >[-<+>]>-                        // denom = 2 * n - 1
  [                                // Inner loop for each term
    <<<<<<+>>>>                      // Move to numerator[i]
    [->-[>+>>]>[+[-<+>]>+>>]<<<<<]   // Multiply numerator[i] by base and store in temp
    >>[-<<+>>]                       // Copy temp back to numerator[i]
    <+>+<                             // Move to denom, temp = temp + i
    [->-[>+>>]>[+[-<+>]>+>>]<<<<<]   // Multiply temp by i and store in temp
    >[-<+>]                          // Move temp back to numerator[i]
    >                               // Move to denom
    [                                // Modulo operation
      ->                         
      [->+>+<<]                 // Duplicate denom
      >[-<-]>                    // Compare temp and denom
      [<                        // If temp >= denom
        +                       //  Increment quotient
        >>-<                      //  temp -= denom
      ]>                        
      [-<+>]                     // Restore temp
    ]                             
    <                               // Move to numerator[i]
    >-                             // Decrement i
  ]                                // End of inner loop
  <                               // Move to numerator[0]
  >>>>>>>>>[-]+                     // Add temp / base to out
  <<<<<<<<<                        // Move to temp
  [->+>+<<]>>[-<<+>>]<<             // temp %= base
  >>>>>>                            // Move to n
  >>-->>-                          // n -= 14
]                                // End of main loop
                                  // Output remaining digits in out