require 'set'

input = File.readlines('24.in')

dict = {
    "e"=> [2, 0],
    "w"=> [-2, 0],
    "ne"=>[1, -1],
    "nw"=> [-1, -1],
    "se"=> [1, 1],
    "sw"=> [-1, 1] 
}    

def get_coord(line, dict)
    (line.scan /(ne|nw|se|sw|e|w)/)
        .map { |c| dict[c[0]] }
        .inject { |a, b| [a[0]+b[0], a[1]+b[1]] }
end

blacks = Set.new()

input.each do |line|
    coord = get_coord(line, dict)
    if blacks.include? coord
        blacks.delete coord
    else
        blacks.add coord
    end
end

res1 = blacks.size
puts res1 # 287

# part 2

for day in 1..100 do
    new_blacks = Set.new()
    to_check = Set.new()
    blacks.each { |pos|
        to_check.add pos
        dict.values.each { |off| to_check.add [pos[0] + off[0], pos[1] + off[1]] }
    }

    to_check.each { |pos|
        cnt = dict.values.count { |off| blacks.include? [pos[0] + off[0], pos[1] + off[1]] }
        is_black = blacks.include? pos
        if (is_black and (cnt == 1 or cnt == 2)) or (not is_black and cnt == 2)
            new_blacks.add pos
        end
    }
    blacks = new_blacks
end

res2 = blacks.size
puts res2 # 3636
