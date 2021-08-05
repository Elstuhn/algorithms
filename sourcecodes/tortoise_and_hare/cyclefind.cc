#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

node cyclefind(sequence) { 
    node tortoise = sequence.head;
    node hare = sequence.head;  //initialise tortoie and hare pointers on the start of sequence (update accordingly)
    while (true) {
        tortoise = tortoise.next;
        hare = hare.next.next; //update accordingly   
        if (tortoise == hare) {
            break;
        }
    }
    hare = sequence.head;
    while (hare != tortoise) {
        hare = hare.next;
        tortoise = tortoise.next;
    }
    return hare;
}
