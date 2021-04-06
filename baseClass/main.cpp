#include<iostream>
#include "People.h"
#include<random>
#include<ctime>
People a[10000];
int main(){
    int cnt0=0,cnt1=0;
    int T=5;
    for(int i=1;i<9999;++i){
        if(a[i].getSex())cnt1++;
        else cnt0++;
    }
    std::cout<<cnt1<<" "<<cnt0<<"\n";
    return 0;
}