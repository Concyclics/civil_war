#include<unordered_set>
#include<cstring>
#include"People.h"
#include<string>
class Building
{
public:
	Building();
	int getPopulation();
	int getType();
	int getLevel();
	int getCapacity();
	int getDuability();
	int getBuild_Time();
	int getArea();
	void setType(int);
	void setLevel(int);
	void setCapacity(int);
	void setDurability(int);
	void setArea(int);
	void setName(std::string);
	std::string getName();
	void DeleteBuilding();
	void AttackBuilding(int);
	void RepairBuilding(int);
	void AddPeople(People*);
	void ErasePeople(People*);
protected:
	int build_time;
	int type;
	int level;
	std::string building_name;
	int capacity;
	int durability;
	int area;
	std::unordered_set <People*> contained_people;
};
