// nav: 108.00 - 117.95 MHz
// com: 118.00 - 136.97 MHz
#include <iostream>
#include <cmath>
class Radio
{
public:
int com_mhz = 118;
int nav_mhz = 108;
int com_khz = 0;
int nav_khz = 0;

double com_actv = 118.00;
double nav_actv = 108.00;


Radio(double com, double nav, double com_actv, double nav_actv)
{

    this->com_mhz = static_cast<int>(com);
    this->nav_mhz = static_cast<int>(nav);
    this->com_khz = static_cast<int>(std::round((com - com_mhz) * 100));
    this->nav_khz = static_cast<int>(std::round((nav - nav_mhz) * 100));
    this->com_actv = com_actv;
    this->nav_actv = nav_actv;
}




void com_mhz_incr()
{
    if (com_mhz == 136) com_mhz = 118;
    else com_mhz++;
}
void com_khz_incr()
{
    if (com_khz == 97) 
    {
        com_khz = 0;
        com_mhz_incr();
    }
    else if (com_khz % 5 == 0) com_khz += 2;
    else com_khz += 3;
}

void nav_mhz_incr()
{
    if (nav_mhz == 117) nav_mhz = 108;
    else nav_mhz++;
}

void nav_khz_incr()
{
    if (nav_khz == 95) 
    {
        nav_khz = 0;
        nav_mhz_incr();
    }
    else nav_khz += 5;
}

void com_mhz_decr()
{
    if (com_mhz == 118) com_mhz = 136;
    else com_mhz--;
    
}
void com_khz_decr()
{
    if (com_khz == 0) 
    {
        com_khz = 97;
        com_mhz_decr();
    }
        else if (com_khz % 5 == 0) com_khz -= 3;
    else com_khz -= 2;
}

void nav_mhz_decr()
{
    if (nav_mhz == 108) nav_mhz = 117;
    else nav_mhz--;
}

void nav_khz_decr()
{
    if (nav_khz == 0) 
    {
        nav_khz = 95;
        nav_mhz_decr();
    }
    else nav_khz -= 5;
}



};


// class AutoPilot;
// class Rnav;
// class Xpndr;


class Rnav_true_calculations
{
public:
float x_plane, y_plane, dist_plane, theta;
float dist_point, crs_point;




};

class Rnav
{
private:
struct Waypoint_rnav
{
    double freq;
    float crs;
    float dist;
    int number;
};


void rnav_calc
(
    Waypoint_rnav &wpt, 
    float dist_plane, 
    float crs_plane
)
{
    float 
    x_plane, y_plane, 
    x_wpt, y_wpt, 
    delta_x, delta_y,
    dist_plane, crs_plane, 
    theta, DIST, CRS;

    theta = std::abs(crs_plane - wpt.crs);

    x_plane = dist_plane * std::sin(theta);
    y_plane = dist_plane * std::cos(theta);

    x_wpt = wpt.dist * std::sin(theta);
    y_wpt = wpt.dist * std::cos(theta);

    delta_x = std::abs(x_wpt - x_plane);
    delta_y = std::abs(y_wpt - y_plane);

    DIST = sqrt(delta_x * delta_x + delta_y * delta_y);

    CRS = atan2(delta_y,delta_x);


}

public:
Waypoint_rnav list[10];
int current_waypoint = 0;





};


int main()
{
    Radio radio(110.50, 108.50, 118.00, 108.00);

    int choice;
    while (true)
    {
        std::cout << "COM: " << radio.com_mhz << "." << radio.com_khz << std::endl;
        std::cout << "NAV: " << radio.nav_mhz << "." << radio.nav_khz << std::endl;
        std::cout << "1. COM MHz Increment\n";
        std::cout << "2. COM KHz Increment\n";
        std::cout << "3. COM MHz Decrement\n";
        std::cout << "4. COM KHz Decrement\n";
        std::cout << "5. NAV MHz Increment\n";
        std::cout << "6. NAV KHz Increment\n";
        std::cout << "7. NAV MHz Decrement\n";
        std::cout << "8. NAV KHz Decrement\n";
        std::cout << "9. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;
        switch (choice)
        {
        case 1:
            radio.com_mhz_incr();
            break;

        case 2:
            radio.com_khz_incr();
            break;
        case 3:
            radio.com_mhz_decr();
            break; 
        case 4:
            radio.com_khz_decr();
            break;  
        case 5:
            radio.nav_mhz_incr();
            break;
        case 6:
            radio.nav_khz_incr();
            break;
        case 7:
            radio.nav_mhz_decr();
            break;
        case 8:
            radio.nav_khz_decr();
            break; 
        case 9:
            std::cout << "Exiting..." << std::endl;
            return 0;

        default:
            break;
        }
    }
    
    
    return 0;
}