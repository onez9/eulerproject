#include <vector>
#include <iostream>

int main() {
    using namespace std;
    vector<unsigned int> lastPos(3, 5);

    for (const auto b:lastPos) {
        std::cout << b << std::endl;
    }
    return 0;
}
