use std::{env, fs, collections::{HashMap, HashSet}};

fn main() {
    let args: Vec<_> = env::args().collect();
    let file = fs::read_to_string(&args[1]).unwrap();

    let score_map = HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]);
    let answer = file.trim().split("\n")
        .map(|line| {
            // first half of line
            let l1 = &line[0..line.len()/2];
            // second half of line
            let l2 = &line[line.len()/2..];
            let chr = l1.chars().collect::<HashSet<_>>()
                .intersection(&l2.chars().collect::<HashSet<_>>())
                .into_iter().next().unwrap();
            if chr.is_uppercase() {
                chr.
            }
        })
        .sum::<i64>();

    println!("{:?}", answer);
}
