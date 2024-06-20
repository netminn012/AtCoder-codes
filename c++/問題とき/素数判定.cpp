#include <iostream>
#include <cmath>

bool isPrime(int num) {
if (num <= 1) return false;
if (num <= 3) return true;

if (num % 2 == 0 || num % 3 == 0) return false;

for (int i = 5; i * i <= num; i += 6) {
if (num % i == 0 || num % (i + 2) == 0) return false;
}
return true;
}

int main() {
int number;
std::cout << "数値を入力してください: ";
std::cin >> number;

if (isPrime(number)) {
std::cout << "true" << std::endl;
} else {
std::cout << "false" << std::endl;
}

return 0;
}