---
title: "Why I wanted to learn Rust"
date: "July 14, 2025"
description: "A quick dive into how Rust made me rethink systems programming and memory safety..."
---

Rust is one of those languages that you hear about everywhere, but until you sit down and wrestle with the borrow checker, you don't really understand *why* people love it.

I started using it to build a CLI tool for parsing JSON. What surprised me most wasn't the performance (which was excellent, as expected), but the confidence I had once the code finally compiled. The compiler isn't just catching syntax errors; it's enforcing a rigorous discipline around memory ownership that eliminates entire classes of runtime bugs. 

## The Borrow Checker is a Teacher

At first, fighting the borrow checker feels restrictive. You can't just pass references around willy-nilly. But eventually, you realize it's forcing you to design your data structures and data flow properly.

Here is a quick example of a simple function:

```rust
fn main() {
    let message = String::from("Hello, World!");
    print_message(&message);
    println!("Still own the message: {}", message);
}

fn print_message(msg: &String) {
    println!("{}", msg);
}
```

By passing a reference `&message`, we don't transfer ownership. 

Overall, Rust is shaping up to be an incredible tool in my arsenal.
