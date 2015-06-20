#!/usr/bin/env swift
// imports

//
// Free coding session for 2015-06-19
// Written by Matt Warren
//

class User {
  var name: String
  init(name: String) {
    self.name = name
  }
}

var user: User?
user = User(name: "Matt")

func do_something() {
  if let name = user?.name where user != nil {
    print(name)
  }
}

do_something()
