// fsi .\aoc_2020_d06f.fsx
open System
open System.IO

let data = 
    let text = File.ReadAllText("6.in")
    text.Split( [|"\n\n"|], StringSplitOptions.RemoveEmptyEntries)
    |> List.ofArray
    |> List.map (fun a -> a.Split([|'\n'|], StringSplitOptions.RemoveEmptyEntries) |> List.ofArray)
    |> List.map (List.map Set.ofSeq)
  
data |> (List.map (List.reduce Set.union >> Set.count) >> List.sum) |> Console.WriteLine
data |> (List.map (List.reduce Set.intersect >> Set.count) >> List.sum) |> Console.WriteLine
