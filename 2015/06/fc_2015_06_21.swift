#!/usr/bin/env swift
// imports

//
// Free coding session for 2015-06-21
// Written by Matt Warren
//

var list = ["one", "two", "three"]

list.append("four")
list.append("five")

for num in list {
  print("\(num)\n")
}


var dict = Dictionary<Int, String>()

for i in 0...4 {
  dict[i+1] = list[i]
}

for (k, v) in dict {
  print("\(k): \(v)\n")
}
