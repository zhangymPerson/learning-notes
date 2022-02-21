#include <iostream>
#include <string>

void testString()
{
    // 定义变量
    std::string str = "Hello word test";
    std::cout << str << std::endl;
    printf("aaa\n");
    // printf(str);

    const char *a=str.c_str();
    str = "bbbsss";
    printf("%s\n",a);
    printf("%s\n",str.c_str());
}

int main(int argc, char const *argv[])
{
    // 执行系统命令
    // system("ls");
    testString();
    return 0;
}
