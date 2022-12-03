use std::{env, fs, collections::HashMap};

fn main() {
    let args: Vec<_> = env::args().collect();
    let file = fs::read_to_string(&args[1]).unwrap();

    let score_map = HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]);
    let answer = file.trim().split("\n")
        .map(|line| {
            let parts: Vec<_> = line.split(" ").collect();
            let p1 = score_map[parts[0]];
            let p2i = score_map[parts[1]];
            let p2 = match p2i {
                1 => match p1 {
                    1 => 3,
                    2 => 1,
                    3 => 2,
                    _ => 0,
                },
                2 => p1,
                3 => match p1 {
                    1 => 2,
                    2 => 3,
                    3 => 1,
                    _ => 0,
                },
                _ => 0,
            };
            let res = match p1 {
                1 => p2 != 3,
                2 => p2 != 1,
                3 => p2 != 2,
                _ => false,
            };
            let score = if p1 == p2 { 3 } else if res { 6 } else { 0 };
            println!("line {} p1 {} p2 {} res {} score {} f {}", line, p1, p2, res, score, p2 + score);
            p2 + score
        })
        .sum::<i64>();

    println!("{:?}", answer);
}
