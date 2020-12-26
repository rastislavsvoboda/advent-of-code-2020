lines = File.readlines('3.in')

def items(entries, slope)
    dc, dr = slope
    r = dr
    c = dc
    res = []
    while r < entries.size
        res.append(entries[r][c % entries[r].size])
        r += dr
        c += dc
    end
    res
end

entries = lines.map &:chomp
counter = ->(slope) { items(entries, slope).count{ |e| e == "#" } }

slope = [3,1]
res1 = counter.(slope)
puts res1

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
cnts = slopes.map{ |slope| counter.(slope) }
res2 = cnts.inject :*
puts res2
