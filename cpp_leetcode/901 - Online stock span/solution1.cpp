#include <stack>
#include <vector>
#include <iostream>

using namespace std;

class Node {
public:
    int price;
    int span;
    Node(int price, int span){
        this->price = price;
        this->span = span;
    }
};

class StockSpanner {
public:
    vector<Node> stk;
    StockSpanner() {
           
    }
    
    int next(int price) {
        
        int span = 1;
        int endPos = (int)stk.size() - 1;
        while ( (endPos >= 0) && (stk[endPos].price <= price)) {
            span += stk[endPos].span;
            endPos = endPos -  stk[endPos].span;
        }
        
        stk.push_back(Node(price, span));
        return span;
    }
};

int main () {
    int *ptr = {};
    int num = 6;
    ptr = &num;
    cout << "memory address pointer: " << ptr << endl;

    return 0;
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */