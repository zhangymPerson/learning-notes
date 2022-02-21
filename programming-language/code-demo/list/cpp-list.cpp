#include <iostream>
#include <list>
#include <vector>

void testList()
{
    std::list<int> l1;
    std::list<int> l2(0, 3);

    l1.push_back(3);
    l1.push_back(30);
    l1.push_back(300);
    l1.push_back(3000);

    // 打印
    for (std::list<int>::iterator ite = l1.begin(); ite != l1.end(); ite++)
    {
        std::cout << *ite << std::endl;
    }
}

void testVector()
{
    std::vector<int> vec;
    vec.push_back(4);
    vec.push_back(40);
    vec.push_back(400);
    vec.push_back(4000);
    for (size_t i = 0; i < vec.size(); i++)
    {
        std::cout << vec[i] << std::endl;
    }
}

int main(int argc, char const *argv[])
{
    std::string splitStr = "===========================";
    std::cout << "test list" << std::endl;
    testList();
    std::cout << splitStr << std::endl;
    testVector();
    std::cout << splitStr << std::endl;
    return 0;
}
