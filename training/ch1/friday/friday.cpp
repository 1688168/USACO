/* Use the slash-star style comments or the system won't see your
   identification information */
/*
ID: 16881681
TASK: friday
LANG: C++                 
*/
/* LANG can be C++11 or C++14 for those more recent releases */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    string filename="friday";
    ofstream fout (filename+".out");
    ifstream fin (filename+".in");
    int n;
    fin >> n;
    double ans=0;

    cout << " Hello Friday!" << endl;

    fout << ans << endl;
    return 0;
}