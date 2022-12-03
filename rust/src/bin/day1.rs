use std::{env, fs};

fn main() {
    let args: Vec<_> = env::args().collect();
    let file = fs::read_to_string(&args[1]).unwrap();

    let answer = file.trim().split("\n\n")
        .map(|group| group.split("\n")
            .map(|line| line.parse::<i64>().unwrap())
            .sum::<i64>())
        .max();
    println!("{:?}", answer);
}
