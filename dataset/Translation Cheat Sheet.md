C++ → Python Translation Cheat Sheet
One-Page Quick Reference for Python IR Labs

Basic I/O & Variables
|                      |                   | C++  |                   | Python       |     |                               |                 | Notes  |     |
| -------------------- | ----------------- | ---- | ----------------- | ------------ | --- | ----------------------------- | --------------- | ------ | --- |
| #include <iostream>  |                   |      | No import needed  |              |     |                               | Use print()     |        |     |
|                      | cout << "Hello";  |      | print("Hello")    |              |     |                               | Auto newline    |        |     |
|                      | cin >> x;         |      |                   | x = input()  |     | Convert with int() if needed  |                 |        |     |
|                      | int x = 0;        |      |                   | x = 0        |     |                               | Dynamic typing  |        |     |
|                      | float y = 0.0;    |      |                   | y = 0.0      |     |                               | Dynamic typing  |        |     |
Loops
|                         |     | C++  |     |                     | Python  |     |     |           | Notes  |
| ----------------------- | --- | ---- | --- | ------------------- | ------- | --- | --- | --------- | ------ |
| for(int i=0;i<n;i++){}  |     |      |     | for i in range(n):  |         |     |     | 0 to n-1  |        |
for(auto item: container){}  for item in container:  Iterate over elements
while(condition){}  while condition:  Indentation replaces braces
Containers
|     |                 | C++  |     |     | Python  |     |     |     | Notes  |
| --- | --------------- | ---- | --- | --- | ------- | --- | --- | --- | ------ |
|     | vector<int> v;  |      |     |     | v = []  |     |     |     |        |
Dynamic list
|     | v.push_back(x);  |           |     |     | v.append(x)  |     |     | Append element  |     |
| --- | ---------------- | --------- | --- | --- | ------------ | --- | --- | --------------- | --- |
|     |                  | v.size()  |     |     | len(v)       |     |     |                 |     |
List length
|     | map<string,int> freq;  |     |     |     | freq = {}  |     |     |     | Dictionary  |
| --- | ---------------------- | --- | --- | --- | ---------- | --- | --- | --- | ----------- |
for(it = m.begin(); it !=
|     |     |     |     | for key, value in m.items():  |     |     |     |     | Dict iteration  |
| --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --------------- |
m.end(); ++it){}

Strings
|                      | C++             |                     | Python          |     | Notes              |
| -------------------- | --------------- | ------------------- | --------------- | --- | ------------------ |
| string s = "text";   |                 |                     | s = "text"      |     | Strings immutable  |
|                      | s.length()      |                     | len(s)          |     | Length             |
| s.substr(start,len)  |                 | s[start:start+len]  |                 |     | Slice              |
|                      | s.find(substr)  |                     | s.find(substr)  |     | Index or -1        |
| s.replace(old,new)   |                 | s.replace(old,new)  |                 |     |                    |
Returns new string
|     | tolower(s[i])  |     | s.lower()  |     |     |
| --- | -------------- | --- | ---------- | --- | --- |
Whole string lowercase
|     | toupper(s[i])  |     | s.upper()  | Whole string uppercase  |     |
| --- | -------------- | --- | ---------- | ----------------------- | --- |
Algorithms & Utilities
|     | C++  |     | Python  |     | Notes  |
| --- | ---- | --- | ------- | --- | ------ |
Libraries for text
import re, collections,
#include <algorithm>
|     |     |     | nltk  |     | processing  |
| --- | --- | --- | ----- | --- | ----------- |
sort(v.begin(),
|     |     |     | v.sort()  |     | In-place sort  |
| --- | --- | --- | --------- | --- | -------------- |
v.end())
Tips for Week 2 Lab
  Focus on text processing and IR logic, not syntax.
Dictionaries replace C++ maps for frequency counting.

  Indentation is critical; no semicolons.
  Use NLTK for stemming, tokenization, and stop-word removal.