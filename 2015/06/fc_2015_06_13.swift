#!/usr/bin/env swift
// imports

//
// Free coding session for 2015-06-13
// Written by Matt Warren
//

let vegetable = "red pepper"
var vegetableComment: String

switch vegetable {
case "celery":
    vegetableComment = "ok then"
case "cucumber", "pickle":
    vegetableComment = "nice choice"
case let x where x.hasSuffix("pepper"):
    vegetableComment = "is it a spicy \(x)"
default:
    vegetableComment = "all vegetables are good"
}

print(vegetableComment)
print("\n")


func fib(n: Int) -> Int {
  // massively inefficient
  if n == 1 || n == 2 {
    return 1
  } else {
    return fib(n-1) + fib(n-2)
  }
}

print("the 25th fibonnaci number is \(fib(25))\n")


func avg(numbers: Int...) -> Int {
  var sum = 0
  for i in numbers {
    sum += i
  }
  return sum / count(numbers)
}

let result = avg(12, 14, 153, 12, 53, 23 ,65)
print("The average is \(result)\n")


func makeIncrementer() -> (Int -> Int) {
  let offset = 15
    func addOne(number: Int) -> Int {
        return 1 + number + offset
    }
    return addOne
}
var increment = makeIncrementer()
print(increment(7))
