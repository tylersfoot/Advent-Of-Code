// Advent of Code 2024 - Day 2

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;

fn main() -> io::Result<()> {
    let start_time = Instant::now();
    let input_path = "input.txt";

    let mut safe_count = 0;
    let mut safe_count_damp = 0;
    let mut reports: Vec<Vec<i64>> = Vec::new();

    if let Ok(lines) = read_lines(input_path) {
        // convert lines (reports) into array of numbers (levels)
        for report in lines {
            if let Ok(content) = report {
                let levels: Vec<i64> = content
                    .split_whitespace()
                    .map(|s| s.parse().expect("could not parse number"))
                    .collect();

                reports.push(levels);
            }
        }

        // part 1: check if reports are safe
        for report in 0..reports.len() {
            let mut safe = true;

            // direction is either -1, 0, or 1 for increasing or decreasing
            let direction = (reports[report][1] - reports[report][0]).clamp(-1, 1);
            for level in 0..reports[report].len() - 1 {
                let current = reports[report][level];
                let next = reports[report][level + 1];

                // unsafe conditions
                if ((current - next).abs() > 3) ||           // difference is greater than 3
                    ((direction > 0) && (current > next)) || // increasing pattern with decreasing difference
                    ((direction < 0) && (current < next)) || // decreasing pattern with increasing difference
                    (current - next == 0) {                  // difference is 0
                    safe = false;
                    break;
                }
            }

            // add 1 if report was safe, else 0
            safe_count += safe as i64;
        }

        // part 2: check if reports are safe with a dampening factor
        for report in 0..reports.len() {
            let mut safe = true;

            // direction is either -1, 0, or 1 for increasing or decreasing
            let direction = (reports[report][1] - reports[report][0]).clamp(-1, 1);
            for level in 0..reports[report].len() - 1 {
                let current = reports[report][level];
                let next = reports[report][level + 1];

                // unsafe conditions
                if ((current - next).abs() > 3) ||           // difference is greater than 3
                    ((direction > 0) && (current > next)) || // increasing pattern with decreasing difference
                    ((direction < 0) && (current < next)) || // decreasing pattern with increasing difference
                    (current - next == 0) {                  // difference is 0
                    safe = false;
                    break;
                }
            }

            // add 1 if report was safe, else 0
            safe_count_damp += safe as i64;
        }

        println!("Part 1: {:?}", safe_count);

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
