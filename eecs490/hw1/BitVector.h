#include <stdexcept>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

class BitVector {
public:
	BitVector(string const &bitString_in) :bitString(bitString_in) {}	
	size_t size() { return bitString.size(); }
	bool operator[](const int index) { return bitString[index] == '0' ? 0 : 1; }
	string get_string() const { return bitString; }

	void push_back(bool val) {
		ostringstream o;
		o << val; 
		bitString.append(o.str()); 
	}

	friend ostream &operator<<( ostream &output, const BitVector &bVector ){ 
   		output << bVector.bitString;
    	return output;            
  	}
private:
	string bitString;
};

string buildInitialString(string &a, string &b, char operatorType) {
	int size = min(a.size(), b.size());
	string res; 
	for(int i = 0; i < size; i++) {
		int first = a[i] - '0'; 
		int second = b[i] - '0';
		int pushBack;

		if(operatorType == '&') pushBack = first & second; 
		else if(operatorType == '|') pushBack = first | second;
		else pushBack = first ^ second; 
		
		res.push_back('0' + pushBack); 
	}
	return res; 
}

void addEndOfString(string &a, string &b, string &res, char operatorType) {
	int additionalToAdd = abs((int)a.size() - (int)b.size()); 
	string longerString = (a.size() > b.size()) ? a : b; 
	for(int i = 0; i < additionalToAdd; i++) {
		if(operatorType == '&') { res.push_back('0'); }
		else { res.push_back(longerString[i]); }
	}
}

BitVector &operator &(const BitVector &a, const BitVector &b) {
	string aString = a.get_string(); 
	string bString = b.get_string(); 
	string res = buildInitialString(aString, bString, '&');  
	addEndOfString(aString, bString, res, '&'); 
	BitVector *returnVal = new BitVector(res); 
	return *returnVal; 
}

BitVector &operator |(const BitVector &a, const BitVector &b) {
	string aString = a.get_string(); 
	string bString = b.get_string(); 
	string res = buildInitialString(aString, bString, '|');  
	addEndOfString(aString, bString, res, '|'); 
	BitVector *returnVal = new BitVector(res); 
	return *returnVal; 
} 

BitVector &operator ^(const BitVector &a, const BitVector &b) {
	string aString = a.get_string(); 
	string bString = b.get_string();
	string res = buildInitialString(aString, bString, '^');  
	addEndOfString(aString, bString, res, '^'); 
	BitVector *returnVal = new BitVector(res); 
	return *returnVal; 
} 

BitVector operator "" _bv(char const * text, std::size_t const size)
{
   return BitVector(std::string(text, text + size));
}