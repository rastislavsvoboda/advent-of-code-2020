fn main() {
    let file_path = "10.in";
    let xs ={
        let mut xs = std::fs::read_to_string(file_path)
            .expect(&format!("Could not read file `{}`", file_path))
            .lines()
            .map(|line| line.parse::<i64>().expect(&format!("`{}` is not a number", line)))
            .collect::<Vec<_>>();
        xs.sort();
        xs.insert(0,0);
        xs.push(xs.last().expect("Rust bug") +3);
        xs
    };

    let mut dp = Vec::<i64>::new();
    dp.push(1);
    for i in 1..xs.len() {
        dp.push(0);
        for j in (0..i).rev() {
            assert!(xs[i]>xs[j]);
            if xs[i]-xs[j] > 3 {
                break;
            }
            dp[i] += dp[j];

        }
    }

    println!("{:?}",dp.last().expect("Rust bug")); // 64793042714624
}