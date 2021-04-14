#include"People.h"
#include"Building.h"
#include<vector>
class People;
class Building;
class Area
{
public:
	int getPopulation();
	int getWealth();//class people should be changed.
	void addPeople(Peolpe*);
	void addBuilding(Building*);
	void addNearArea(Area*);
	void erasePeople(People*);
	void eraseBuilding(Building*);
protected:
	int belong;//belong to who
	int wealth;
	vector <Area*> to;
	set <Building*> contained_building;
	set <People*> contained_people;
}
