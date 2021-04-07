#include"Building.h"
#include"People.h"
Building::Building()//Class "People" should be changed
{
}


void Building::DeleteBuilding()//Class "People" should be changed
{
}


void Building::setType(int x)
{
	type=x;
}

void Building::setLevel(int x)
{
	level=x;
}

void Building::setCapacity(int x)
{
	capacity=x;
}

void Building::setDurability(int x)
{
	durability=x;
}

void Building::setName(std::string x)
{
	building_name=x;
}

void Building::setArea(int x)
{
	area=x;
}


void Building::AttackBuilding(int x)
{
	durability-=x;
	if (x<=0)
		DeleteBuilding();
}

void Building::RepairBuilding(int x)
{
	durability+=x;
}

void Building::AddPeople(People* x)
{
	contained_people.insert(x);
}

void Building::ErasePeople(People* x)
{
	contained_people.erase(x);
}

int Building::getPopulation()
{
	return contained_people.size();
}

int Building::getType()
{
	return type;
}

int Building::getLevel()
{
	return level;
}

int Building::getCapacity()
{
	return capacity;
}

int Building::getDuability()
{
	return durability;
}

int Building::getBuild_Time()//Round when build
{
	return build_time;
}

int Building::getArea()
{
	return area;
}
