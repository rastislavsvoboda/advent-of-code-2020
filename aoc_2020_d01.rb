input = File.readlines('1.in')
ns = input.map &:to_i

[2,3].each do |k|
    puts ns.combination(k).find{ |xs| xs.sum == 2020 }.inject :*
end