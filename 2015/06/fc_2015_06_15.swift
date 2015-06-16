#!/usr/bin/env swift
// imports

//
// Free coding session for 2015-06-15
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

class Circle: Shape {
  var radius: Double
  init(radius: Double, name: String) {
    self.radius = radius
    super.init(name: name)
  }
  func area() -> Double {
    return 3.1415926 * radius * radius
  }
  override func description() -> String {
    return "A Circle with radius \(radius) and area \(area())"
  }
}

let c = Circle(radius: 1.3, name: "My circle")
print("\(c.description())\n")


enum Suit {
  case Spades, Hearts, Clubs, Diamonds
  func color() -> String {
    switch self {
      case .Spades, .Clubs:
        return "black"
      case .Hearts, .Diamonds:
        return "red"
    }
  }
}

let s = Suit.Hearts
print(s.color())
