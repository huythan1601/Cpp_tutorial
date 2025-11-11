/* Include necessary directories */
#include <iostream>     // Inlucde directory for using "cout" to display the data
#include <cstdint>      // Include directory to use some data types
#include <string>       // Include directory to use string data type
#include <cmath>        // Include directory to use some calculation fuction  
#include <iomanip>      // Include directory to use "setprecision" for controlling number of displayed digits

/* Declare namespace*/
using namespace std;

int main()
{
    /* Example of declaring a variable*/
    int age = 23;   // Declare (create) a variable named "age" with the data type "int" (integer), and assign the value "23" to it
    cout << age << endl;

    
    /* Example of declaring a variable without assigning the value*/
    string name;                // Declare (create) a variable named "name" with the data type "string" (text)
    name = "Than Hoang Huy";    // Assign value "Than Hoang Huy" to variable "name"
    cout << name << endl;

    /* Example of "bool" data type */
    bool isSucessfull = true;
    cout << isSucessfull << endl;



    /* Example of 1 byte (8 bits) data type*/
    char digit1 = 'A';
    cout << digit1 << endl;

    uint8_t digit2 = 200;
    cout << digit2 << endl;
    cout << static_cast<int>(digit2) << endl;

    int8_t digit3 = 200;
    cout << digit3 << endl;
    cout << static_cast<int>(digit3) << endl;



    /* Example of 2 bytes (16 bits) data type */
    int16_t number1 = 66000;
    cout << number1 << endl;

    uint16_t number2 = 65535;
    cout << number2 << endl;



    /* Example of 4 bytes (32 bits) data type */
    int number3 = -100000;
    cout << number3 << endl;
    
    uint32_t number4 = 3000000000;
    cout << number4 << endl;



    /* Example of float and double data types */
    float number5 = 18.237845;
    cout << number5 << endl;

    double number6 = 30.589425;
    cout << number6 << endl;



    /* Example illustrating the difference between float and double data types */
    cout << setprecision(20);           // Set the number of displayed digits to 20.

    float number7 = sqrt(50000);
    cout << number7 << endl;

    double number8 = sqrt(50000);
    cout << number8 << endl;


    /* Example of changing variable values*/
    int myNum = 15;  // myNum is 15
    myNum = 10;  // Now myNum is 10
    cout << myNum << endl;  // Outputs 10


    return 1;
}



