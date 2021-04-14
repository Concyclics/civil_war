//defintion of people class
#ifndef PEOPLE_H    
#define PEOPLE_H
#include<utility>
#include "Building.h"
class People
{
    public:
        People(int strength=100,int intelligence=100,int age=0,int health_ability=80,int happy_ability=80);
        bool setHealthAbility(int);
        bool setStrength(int);
        bool setHappyAbility(int);
        void setSex();
        bool getSex();
        int getHealthability();
        int getStrength();
        int getHappyAbility();
        void EraseSelf();   //delete from building
    protected:
        bool sex;//0/1 girl boy
        int strength;//0-200
        int intelligence;
        int age;
        int health_ability;//0-100
        int happy_ability;//0-100
        Building* belonging;//NULL为空
       /*std::pair<int,int>born*/;
};

#endif