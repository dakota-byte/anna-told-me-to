#include <iostream>

// the xor product
// my 3rd iteration but I found this on chatgpt
// the slower ones are in python
int xorp(int a, int b) {
    int indent = 0;
    int product = 0;

    while (b > 0) {
        if (b & 1) {
            product ^= a << indent;
        }
        indent++;
        b = b >> 1;
    }

    return product;
}

// individual check for an xor prime, iteration 3
// replaced: hashmap w/ a simple counter for n
// entirely by me, except chatgpt suggested the early exit
bool is_xor_prime(int n) {
    int count_n = 0;  // track `n` as an XOR product

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            int xor_prod = xorp(i, j);
            if (xor_prod == n) {
                count_n++;
                if (count_n > 2) {  // early exit if count exceeds 2
                    return false;
                }
            }
        }
    }

    return count_n == 2;
}

// 
void nth_xor_prime(int n) {
    int xor_primes = 1;    // We already know 2 is an XOR prime
    int current_try = 3;    // start at 3 to skip even numbers

    while (xor_primes < n) {
        if (current_try % 2 == 0) {
            current_try++;  // skip even numbers, as they don't seem to be XOR primes
            continue;
        }

        if (is_xor_prime(current_try)) {
            xor_primes++;
            std::cout << "xor_prime #" << xor_primes << " = " << current_try << std::endl;
        }
        current_try++;
    }
}

int main() {
    nth_xor_prime(5000000);
    return 0;
}