#!/usr/bin/env swift
// imports

//
// Free coding session for 2015-06-14
// Written by Matt Warren
//


class Shape {
  var sides = 0
  var name: String
  init(name: String) {
    self.name = name
  }
  func description() -> String {
    return "A shape with \(sides) sides.\n"
  }
}

let s = Shape("Nonagon")
s.sides = 9
print(s.description())
