#!/usr/bin/env swift
// imports

//
// Free coding session for 2015-07-01
// Written by Matt Warren
//


let tester_a = "Something"
let tester_b = tester_a
let tester_c = "Something"

if tester_a == tester_b {
  // note: the identical operator doesn't work on strings
  print("a and b Strings are equal\n")
}

class Matt {
  var name: String
  init(name: String) {
    self.name = name
  }
}

// implement equatable for Matt classes
func ==(lhs: Matt, rhs: Matt) -> Bool {
  return lhs.name == rhs.name
}

let test_a = Matt(name: "matt")
let test_b = test_a
let test_c = Matt(name: "matt")

if test_a === test_b {
  print("a and b classes are identical\n")
}
if test_a == test_c {
  print("a and c classes are equal\n")
}
