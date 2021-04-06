#include "People.h"
#include<random>
#include<ctime>
std::mt19937 sex_rnd(time(NULL));
People::People(int m_strength,int m_intelligence,int m_age,int m_health_ability,int m_happy_ability)
{   
    setSex();
    strength=m_strength;
    intelligence=m_intelligence;
    age=m_age;
    health_ability=m_health_ability;
    happy_ability=m_happy_ability;
}

bool People::getSex()
{
    return sex;
}

void People::setSex()
{
    sex=sex_rnd()&1;
}

bool People::setHappyAbility(int x)
{
    if(x<=100&&x>=0)
    {
        happy_ability=x;
        return 1;
    }
    else return 0;
}

bool People::setHealthAbility(int x)
{
    if(x<=100&&x>=0)
    {
        health_ability=x;
        return 1;
    }
    else return 0;
}

bool People::setStrength(int x)
{
    if(x<=200&&x>=0)
    {
        strength=x;
        return 1;
    }
    return 0;
}

int People::getStrength()
{
    return strength;
}

int People::getHappyAbility()
{
    return happy_ability;
}

int People::getHealthability()
{
    return health_ability;
}

