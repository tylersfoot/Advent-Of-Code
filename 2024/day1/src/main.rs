use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;

fn main() -> io::Result<()> {
    let start_time = Instant::now();
    let file_path = "input.txt";

    let mut difference = 0;

    if let Ok(lines) = read_lines(file_path) {
        let mut list1: Vec<i64> = Vec::new();
        let mut list2: Vec<i64> = Vec::new();

        for line in lines {
            if let Ok(content) = line {
                let mut numbers = content.split_whitespace();

                let num1: i64 = numbers
                    .next()
                    .expect("expected number")
                    .parse()
                    .expect("couldnt parse");
                let num2: i64 = numbers
                    .next()
                    .expect("expected number")
                    .parse()
                    .expect("couldnt parse");

                list1.push(num1);
                list2.push(num2);
            }
        }


        list1.sort();
        list2.sort();

        for i in 0..list1.len() {
            difference += (list1[i] - list2[i]).abs();
        }

        // print the array
        println!("{:?}", difference);
    } else {
        println!("Error: Could not read the file at '{}'", file_path);
    }

    let elapsed_time = start_time.elapsed();
    println!("Process completed in: {:.2?}", elapsed_time);

    Ok(())
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
