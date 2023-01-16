/* Use the slash-star style comments or the system won't see your
   identification information */
/*
ID: 16881681
TASK: ride
LANG: C++                 
*/
/* LANG can be C++11 or C++14 for those more recent releases */
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
/*
* 
*/
int main() {
 
    char cname[8];
    char gname[8];

    ofstream fout ("ride.out");
    ifstream fin ("ride.in");

    fin >> cname;
    fin >> gname;

    int cn=1, gn=1;

    int ii=0;

    while(cname[ii] != '\0' && cname[ii] != ' '){
        cn *= (int(cname[ii]-'A')+1);
        ++ii;
    }

    ii=0;
    while(gname[ii] != '\0' && gname[ii] != ' '){
        gn *= (int(gname[ii]-'A')+1);
        ++ii;
    }
    // cout << " cn: " << cn << endl;
    // cout << " gn: " << gn << endl;

    if(cn%47==gn%47){
        fout << "GO" << endl;
    }else{
        fout << "STAY" << endl;
    }
    return 0;
}