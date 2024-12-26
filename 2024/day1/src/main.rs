// Advent of Code 2024 - Day 1
//
// Notes: its a pretty straightforward problem, probably can be
// improved but its fine the way it is
//
// Provided: A text file with two lists of numbers, seperated by spaces
//
// Part 1: Difference
// Calculate the total difference between the lists by pairing the
// smallest numbers together, the second smallest, and so on.
// For each pair, calculate the absolute difference and sum them up.
//
// Part 2: Similarity
// Calculate a similarity score between the two lists.
// For each number in the first list, multiply it by the number of times it appears
// in the second list, then sum up these products.

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;

fn main() -> io::Result<()> {
    let start_time = Instant::now();
    let input_path = "input.txt";

    let mut difference = 0;
    let mut similarity = 0;
    let mut list1: Vec<i64> = Vec::new();
    let mut list2: Vec<i64> = Vec::new();

    if let Ok(lines) = read_lines(input_path) {
        // separate lines into two numbers and add them to lists
        for line in lines {
            if let Ok(content) = line {
                let mut numbers = content.split_whitespace();

                let num1: i64 = numbers
                    .next().expect("expected number")
                    .parse().expect("couldnt parse");
                let num2: i64 = numbers
                    .next().expect("expected number")
                    .parse().expect("couldnt parse");

                list1.push(num1);
                list2.push(num2);
            }
        }

        // sort lists
        list1.sort();
        list2.sort();

        // part 1: calculate the difference between the two lists
        for i in 0..list1.len() {
            difference += (list1[i] - list2[i]).abs();
        }

        // part 2: calculate the similarity between the two lists
        for i in 0..list1.len() {
            for j in 0..list2.len() {
                if list1[i] == list2[j] {
                    similarity += list1[i];
                }
            }
        }

        println!("Part 1: {:?}", difference);
        println!("Part 2: {:?}", similarity);
    } else {
        println!("Could not read input file: '{}'", input_path);
    }

    let elapsed_time = start_time.elapsed();
    println!("Completed in: {:.2?}", elapsed_time);

    Ok(())
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
