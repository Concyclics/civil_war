//defintion of people class
#ifndef PEOPLE_H    
#define PEOPLE_H
#include<utility>

class People
{
    public:
        People(int,int strength=100,int intelligence=100,int age=0,int health_ability=80,int happy_ability=80);
        bool setHealthAbility(int);
        bool setStrength(int);
        bool setHappyAbility(int);
        int getHealthability();
        int getStrength();
        int getHappyAbility();
    protected:
        bool sex;//0/1 girl boy
        int strength;//0-200
        int intelligence;
        int age;
        int health_ability;//0-100
        int happy_ability;//0-100
       /*std::pair<int,int>born*/;
};
#endif