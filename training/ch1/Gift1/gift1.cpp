/* Use the slash-star style comments or the system won't see your
   identification information */
/*
ID: 16881681
TASK: gift1
LANG: C++                 
*/
/* LANG can be C++11 or C++14 for those more recent releases */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;
/*
* 
*/
int main() {
 
    ifstream fin ("gift1.in");
    ofstream fout ("gift1.out");
    
    //first line number of members
    int num_of_member=0;
    fin >> num_of_member;
    cout << "numOfMember: " << num_of_member << endl;
    
    unordered_map<string, int>  name2amt;
    vector<string> names;
    for(int ii=0; ii<num_of_member; ++ii){
        string name;
        fin>>name;
        name2amt[name]=0;
        names.push_back(name);

    }

    //getline(fin, line)
    for(int ii=0; ii<num_of_member; ++ii){
        //read name
        string name;
        fin>>name;
        cout << "---------------------------------------- " << endl;
        cout << " Giver >>> " << name << " !!!" << endl;
        cout << "---------------------------------------- " << endl;
        //read amt, num pays
        int amt, nn;
        fin >> amt >> nn;
        cout << " having amt: " << amt << " given num: " << nn << endl;
        if(nn != 0){
            cout << " name: " << name << " got remainder: " << amt%nn << endl;
            name2amt[name] += -amt;
            name2amt[name] += amt%nn;
        }

        //read receiver names
     
        cout << " receivers: " << endl;
        cout << " --- " << endl;
        for(int ii=0; ii<nn; ++ii){
            fin >> name;                    
            if(nn==0){
                name2amt[name] += 0;
            }else{
                name2amt[name] += amt/nn;
                cout << ' ' << name << " received " << amt/nn << endl;
            }
           
        }
    }
    // for(auto x: name2amt){
    //     fout << x.first << ' ' << x.second << endl;
    // }

    for(auto name: names){
        fout << name << " " << name2amt[name] << endl;
    }

    return 0;
}