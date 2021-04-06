#include "People.h"

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

