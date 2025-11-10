/* Include necessary directories */
#include <iostream>     // Inlucde directory for using "cout" to display the data
#include <cstdint>      // Include directory to use some data types
#include <cmath>        // Include directory to use some calculation fuction  
#include <iomanip>      // Include directory to use "setprecision" for controlling number of displayed digits

/* Declare namespace*/
using namespace std;

int main()
{
    /* Example of "bool" data type */
    bool isSucessfull = true;
    cout << isSucessfull << endl;



    /* Example of 1 byte (8 bits) data type*/
    // char digit1 = 'A';
    // cout << digit1 << endl;

    // uint8_t digit2 = 200;
    // cout << digit2 << endl;
    // cout << static_cast<int>(digit2) << endl;

    // int8_t digit3 = 200;
    // cout << digit3 << endl;
    // cout << static_cast<int>(digit3) << endl;



    /* Example of 2 bytes (16 bits) data type */
    // int16_t number1 = 66000;
    // cout << number1 << endl;

    // uint16_t number1 = 65535;
    // cout << number1 << endl;



    /* Example of 4 bytes (32 bits) data type */
    // int number3 = -100000;
    // cout << number3 << endl;
    
    // uint32_t number4 = 3000000000;
    // cout << number4 << endl;



    /* Example of float and double data types */
    // float number5 = 18.237845;
    // cout << number5 << endl;

    // double number6 = 30.589425;
    // cout << number6 << endl;



    /* Example illustrating the difference between float and double data types */
    // cout << setprecision(20);           // Set the number of displayed digits to 20.

    // float number7 = sqrt(50000);
    // cout << number7 << endl;

    // double number8 = sqrt(50000);
    // cout << number8 << endl;


    return 1;
}



